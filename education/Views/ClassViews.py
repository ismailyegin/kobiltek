import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from education.Forms.ClassForm import ClassForm
from education.models import Class, Student
from education.serializers.student_serializer import StudentSerializer
from education.services import class_services
from education.services.class_services import add_the_class_false


@login_required
def class_list(request):
    class_lists = class_services.get_class_list()
    form_class = ClassForm()

    if request.method == 'POST':

        form_class = ClassForm(request.POST)

        if form_class.is_valid():

            form_class = form_class.save()

            food_lists_saved = class_services.get_class_list()
            form_class = ClassForm()
            messages.success(request, 'Başarıyla kaydedildi')
            return render(request, 'class_list_add.html', {'classes': food_lists_saved, 'form_class': form_class})
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'class_list_add.html', {'classes': class_lists, 'form_class': form_class})


@login_required
def class_delete(request, pk):

    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Class.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Class.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})



@login_required
def class_update(request,pk):
    the_class = Class.objects.get(id=pk)
    form_class = ClassForm(request.POST or None, instance=the_class)

    if form_class.is_valid():
        form_class.save()
        messages.warning(request, 'Başarıyla Güncellendi')
        class_lists = class_services.get_class_list()

        return redirect('education:sinif-listesi', message ='1')
    else:
        messages.warning(request, 'Alanları Kontrol Ediniz')
    #messages.add_message(request, messages.INFO, 'Hello world.')

    class_lists = class_services.get_class_list()

    return render(request, 'class_list_add.html', {'classes': class_lists, 'form_class': form_class})


@login_required
def class_add_students(request,pk):
    students = Student.objects.filter(user__is_active=True, isAddedToClass=False)
    the_class = Class.objects.get(pk=pk)
    class_students = Student.objects.filter(class__pk  = pk)
    data = StudentSerializer(class_students)
    return render(request, 'student_preparing.html', {'students' :students, 'class':the_class, 'classStudents': data})


@api_view()
def selected_students(request,pk):
    class_students = Student.objects.filter(class__pk=pk)
    data = StudentSerializer(class_students, many=True)
    responseData = {}
    responseData['students'] = data.data
    return JsonResponse(responseData, safe=True)



@login_required
def student_post(request):
    if request.POST:
        try:
            students = request.POST.getlist('values[]')
            the_class = Class.objects.get(pk=request.POST.get('class'))

            add_the_class_false(the_class.students.all())

            the_class.students.clear()
            if len(students) == 0:
                return JsonResponse({'status': 'Success', 'messages': 'Sınıf listesi boş'})
            else:
                for id in students:
                    student = Student.objects.get(pk=id)
                    the_class.students.add(student)
                    student.isAddedToClass = True
                    student.save()
                    student = None

            the_class.save()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Class.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})



