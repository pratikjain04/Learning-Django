from django.views.generic import TemplateView
from learn.forms import RegistrationForm, EditProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

class Homepage(TemplateView):
    template_name = 'learn/home.html'


class Homepage_LoggedIn(TemplateView):
    template_name = 'learn/loggedin.html'


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')       #We always write url in redirect
                                       #Which url to open when submit button is hit
    else:
        form = RegistrationForm()
        return render(request, 'learn/signup.html', {'form': form})   #We always write path of the html file in render


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/home/')

    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'learn/edit_profile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            update_session_auth_hash(request, form.user)   #to keep the useer loggedin after changing the password
            form.save()
            return redirect('/home/')
        else:
            return redirect('/home/edit/changepassword')

    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'learn/change_password.html', {'form': form})
