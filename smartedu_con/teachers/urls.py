from django.urls import path
from teachers.views import TeacherListView


urlpatterns = [
    path('', TeacherListView.as_view(), name="teachers"),

]