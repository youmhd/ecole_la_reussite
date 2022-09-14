from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.http import  HttpResponseRedirect
from .models import *
from django.db.models import Q

def index(request):
  return render(request, 'students/index.html')	

def students_list(request):
	students = Student.objects.all().order_by('name')
	return render(request, 'students/students_list.html', {
		'students': students,
	})


def add_student(request):
      submitted = False
      if request.method == "POST":
            form = StudentForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
            return HttpResponseRedirect('/add_student?submitted=True')
      else:
            form = StudentForm
      if 'submitted' in request.GET:
            submitted=True
      return render(request, 'students/add_student.html', {
        'form': form,
        'submitted': submitted,
        })    


def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('students-list')
    return render(request, 'students/update_student.html', {
        'student': student,
        'form': form,
    })


def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('students-list')

def show_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'students/show_student.html', {
        'student': student,
    
    })

def search_student(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            mutiple_q = Q(Q(name__icontains=query) | Q(email__icontains=query))
        students = Student.objects.filter(mutiple_q)
        if students:
            return render(request, 'students/students_list.html', {
                'students': students
            })
        else:
            print('Not found ...')
            return render(request, 'students/not_found.html', {})        