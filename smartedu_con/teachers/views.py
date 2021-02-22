from django.shortcuts import render
from django.views.generic.list import ListView
from teachers.models import Teacher

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    #paginate_by = 1
    #queryset = Teacher.objects.all()[:1]

    #def get_queryset(self):
        #return Teacher.objects.all()[:2]
