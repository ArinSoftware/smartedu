from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('dashboard/', views.user_dashboard, name="dashboard"),
    path('logout/', views.user_logout, name="logout"),
    path('enroll_the_course/', views.enroll_the_course, name="enroll_the_course"),
    path('release_the_course/', views.release_the_course, name="release_the_course"),

]