from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from education.Forms.ParentForm import ParentProfileForm
from education.Forms.UserForm import UserForm
from education.models import Student, Parent
from education.serializers.parent_serializer import ParentSerializer
from education.serializers.student_serializer import StudentSerializer


def parent_add(request, student_pk):

    student = Student.objects.get(pk=student_pk)

    form_user = UserForm()
    form_parent = ParentProfileForm()

    if request.method == 'POST':

        form_user= UserForm(request.POST)
        form_parent = ParentProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_parent.is_valid():

            group = Group.objects.get(name='Veli')
            form_user.cleaned_data['groups'] = group
            user = form_user.save(commit=False)
            user.set_password("oxit2016")
            #user.groups.add(group)

            user.save()

            group.user_set.add(user)
            group.save()
            parent = Parent(user=user, tc=form_parent.cleaned_data['tc'],
                              address=form_parent.cleaned_data['address'],
                              gender=form_parent.cleaned_data['gender'],
                              profileImage=form_parent.cleaned_data['profileImage'],
                              mobilePhone=form_parent.cleaned_data['mobilePhone'],
                            )
            parent.save()

            student.parents.add(parent)

            student.save()

            return redirect('education:list')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'parent_add.html', {'form_user': form_user, 'form_parent': form_parent})



@api_view()
#@permission_classes((IsAuthenticated, ))
def getParents(request, pk):
    students = Student.objects.filter(pk=pk).defer("user__password")

    parents=[]
    for parent in students[0].parents.all():
        parent.user.password="******"
        parents.append(parent)



    #parents = Parent.objects.filter(pk=pk).defer("user__password")
    #parents[0].user.password = "*********"
    data = ParentSerializer(parents, many=True)

    responseData = {}
    responseData['parents'] =data.data
    #data = serializers.serialize('json',patients)
   # responseData['parents'][0]['user']['password']= "********"
    return JsonResponse(responseData, safe=True)