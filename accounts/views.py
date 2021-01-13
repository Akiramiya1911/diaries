from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from . import forms
from classrooms.models import Classrooms
from .models import Students


def student_regist_view(request):

    classroom = Classrooms.objects.last()
    student = Students.objects.last()
    StudentsFormSet = modelformset_factory(Students, form=forms.StudentsRegistForm, extra=classroom.members)
    if student:
        formset = StudentsFormSet(request.POST or None, queryset=Students.objects.filter(id__gt=student.id))
    else:
        formset = StudentsFormSet(request.POST or None)
    if formset.is_valid():
        formset.save()
        return redirect('diary:home')
    return render(request, 'accounts/students_regist.html', context={
        'formset': formset
        }
    )
