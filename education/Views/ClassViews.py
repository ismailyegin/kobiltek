import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from education.Forms.ClassForm import ClassForm
from education.models import Class, Student
from education.services import class_services


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
    students = Student.objects.filter(user__is_active=True)
    the_class = Class.objects.get(pk=pk)
    class_students = Student.objects.filter(class__pk  = pk)
    return render(request, 'student_preparing.html', {'students' :students, 'class':the_class, 'classStudents':class_students})


def form_ajax(request):
    data = {'is_valid': False,}
    if request.is_ajax():
        message = request.POST.getlist('values[]')
        the_class = Class.objects.get(pk=request.POST.get('class'))

        for id in message:
            student = Student.objects.get(pk=id)
            the_class.students.add(student)
            student = None

        the_class.save()

        data.update(is_valid=message)

    return JsonResponse(data)
