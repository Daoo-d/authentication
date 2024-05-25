from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('about',views.about,name = 'about_page'),
    path('sign-up',views.signup,name='signup_page'),
    path('sign-in',views.signin,name='signin_page'),
    path('sign-out',views.signout,name='signout_page'),
    path('activate/<uidb64>/<token>',views.activate,name='activate')
]