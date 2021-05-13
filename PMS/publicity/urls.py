
from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login', views.login, name="login"),
path('aboutus',views.aboutus,name="aboutus"),
    path('uservisit', views.uservisit, name="uservisit"),
path('contactus',views.contactus,name="contactus"),
    path('rating', views.rating, name="rating"),
path('main',views.main,name="main"),
path('payment',views.payment,name="payment"),




]
