from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view

from education.Forms.TeacherProfileForm import TeacherProfileForm
from education.Forms.UserForm import UserForm
from education.models import Teacher
from education.serializers.teacher_serializer import TeacherSerializer


@login_required
def teacher_add(request):



    form_user = UserForm()
    form_teacher = TeacherProfileForm()

    if request.method == 'POST':

        form_user= UserForm(request.POST)
        form_teacher = TeacherProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_teacher.is_valid():

            group = Group.objects.get(name='Öğretmen')
            form_user.cleaned_data['groups'] = group
            user = form_user.save(commit=False)
            user.set_password("oxit2016")
            #user.groups.add(group)

            user.save()

            group.user_set.add(user)
            group.save()
            teacher = Teacher(user=user, tc=form_teacher.cleaned_data['tc'],
                              address=form_teacher.cleaned_data['address'],
                              gender=form_teacher.cleaned_data['gender'],
                              profileImage=form_teacher.cleaned_data['profileImage'],
                              mobilePhone=form_teacher.cleaned_data['mobilePhone'],
                            )
            teacher.save()

            return redirect('education:ogretmen-liste')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'Teacher/teacher_add.html', {'form_user': form_user, 'form_teacher': form_teacher})

@login_required
def updateTeacher(request,pk):
    user = User.objects.get(pk=pk)
    profile_info = Teacher.objects.get(user=user)

    form = UserForm(request.POST or None, instance=user)
    form_teacher = TeacherProfileForm(request.POST or None, request.FILES or None, instance=profile_info)

    if all([form.is_valid() and form_teacher.is_valid()]):
        form.save()
        form_teacher.save()
        return redirect("education:ogretmen-liste")
    return render(request, 'Teacher/teacher_add.html', {'form_user': form, 'form_teacher': form_teacher})


@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'Teacher/teacher_list.html', {'teachers': teachers})



@api_view()
#@permission_classes((IsAuthenticated, ))
def getTeacher(request, pk):
    teachers = Teacher.objects.filter(pk=pk).defer("user__password")
    teachers[0].user.password = "*********"
    data = TeacherSerializer(teachers.defer('user__password'), many=True)

    responseData = {}
    responseData['teachers'] =data.data
    #data = serializers.serialize('json',patients)
    responseData['teachers'][0]['user']['password']= "********"
    return JsonResponse(responseData, safe=True)