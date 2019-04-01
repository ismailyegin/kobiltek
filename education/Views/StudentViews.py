from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.http import JsonResponse

from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from education.Forms.UserForm import UserForm
from education.Forms.StudentProfileForm import StudentProfileForm
from education.models import Parent
from education.models.Student import Student
from education.serializers.student_serializer import StudentSerializer
from education.services import general_methods


@login_required
def student_add(request):
    form = UserForm()
    form_student = StudentProfileForm()
    if request.method == 'POST':

        form = UserForm(request.POST)
        form_student = StudentProfileForm(request.POST, request.FILES)

        if form.is_valid() and form_student.is_valid():

            group = Group.objects.filter(name='Öğrenci')
            form.cleaned_data['groups'] = group
            user = form.save(commit=False)
            user.set_password("oxit2016")
           # form.cleaned_data['password'] = make_password(form.cleaned_data['password'])
            user.save()


           # parent = Parent(user=user2, address=form_student.cleaned_data['address'], profileImage=form_student.cleaned_data['profileImage'],
           #               mobilePhone=form_student.cleaned_data['mobilePhone'])
           # parent.save()



            student = Student(user=user, tc=form_student.cleaned_data['tc'],
                              address=form_student.cleaned_data['address'],
                              gender=form_student.cleaned_data['gender'],
                              profileImage=form_student.cleaned_data['profileImage'],
                              mobilePhone=form_student.cleaned_data['mobilePhone'],
                              studentNumber='asasasa',)
            student= student.save()

            return redirect('education:list')
        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
            #messages.add_message(request, messages.INFO, 'Hello world.')

    return render(request, 'student_add.html', {'form': form, 'form_student': form_student})


@login_required
def updateStudent(request,pk):
    user = User.objects.get(pk=pk)
    profile_info = Student.objects.get(user=user)

    form = UserForm(request.POST or None, instance=user)
    form_student = StudentProfileForm(request.POST or None, request.FILES or None, instance=profile_info)

    if all([form.is_valid() and form_student.is_valid()]):
        form.save()
        form_student.save()
        return redirect("education:list")
    return render(request, 'student_add.html', {'form': form, 'form_student': form_student})

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})



@api_view()
#@permission_classes((IsAuthenticated, ))
def getStudent(request, pk):
    students = Student.objects.filter(pk=pk).defer("user__password")
    students[0].user.password = "*********"
    data = StudentSerializer(students.defer('user__password'), many=True)

    responseData = {}
    responseData['students'] =data.data
    #data = serializers.serialize('json',patients)
    responseData['students'][0]['user']['password']= "********"
    return JsonResponse(responseData, safe=True)
