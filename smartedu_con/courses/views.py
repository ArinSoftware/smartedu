from django.shortcuts import render
from . models import Course

def course_list(request):
    courses = Course.objects.all().order_by('-date')

    context = {
        'courses': courses
    }

    return render(request, 'courses.html', context)

def course_detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id = course_id)

    context = {
        'course': course
    }

    return render(request, 'course.html', context)
