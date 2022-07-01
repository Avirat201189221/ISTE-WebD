from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('faculty',views.facultyPage,name='faculty'),
    path('profile',views.profilePage,name='profile'),
    path('myherupa-first-year',views.myHerupaFirstYear,name='myherupafirstyear'),
    path('myherupa-second-year',views.myHerupaSecondYear,name='myherupasecondyear'),
    path('myherupa-third-year',views.myHerupaThirdYear,name='myherupathirdyear'),
]