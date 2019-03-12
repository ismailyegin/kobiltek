from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from education.Forms.ParentForm import ParentProfileForm
from education.Forms.UserForm import UserForm
from education.models import Student, Parent


def parent_add(request, student_pk):

    student = Student.objects.get(pk=student_pk)

    form_user = UserForm()
    form_parent = ParentProfileForm()

    if request.method == 'POST':

        form_user= UserForm(request.POST)
        form_parent = ParentProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_parent.is_valid():

            group = Group.objects.filter(name='Veli')
            form_user.cleaned_data['groups'] = group
            user = form_user.save(commit=False)
            user.set_password("oxit2016")

            user.save()
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

