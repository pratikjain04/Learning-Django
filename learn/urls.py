from django.urls import path , include
from learn import views


urlpatterns = [
    path('home/', include('practise.urls')),

]