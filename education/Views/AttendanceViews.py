import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from education.Forms.AttendanceDateForm import AttendanceDateForm
from education.models import Student, Settings, Class, Attendance
from education.models.AttentanceObject import AttendanceObject
from education.services import class_services, attendance_services


@login_required
def class_list(request):
    class_lists = class_services.get_class_list()

    return render(request, 'Attendance/class_list_atndc.html', {'classes': class_lists})


@login_required
def student_list(request, pk):
    students = Student.objects.filter(class__pk=pk)
    total_lecture = Settings.objects.filter(name='total_lecture')
    return render(request, 'Attendance/student_list.html',
                  {'students': students, 'total_lecture': range(int(total_lecture[0].value))})


@login_required
def attendances_of_the_day(request, pk):
    class_object = Class.objects.get(pk=pk)
    total_lecture = range(int(Settings.objects.filter(name='total_lecture')[0].value))
    students = Student.objects.filter(class__pk=pk)
    attendance_object = AttendanceObject(total_lecture, class_object, students, None)

    gelenArray = list()
    gelmeyenArray = list()
    kayitArray = list()

    if request.method == 'POST':
        x = 1
        attendance_form = AttendanceDateForm(request.POST)
        if attendance_form.is_valid():

            if attendance_form.cleaned_data['birthDate'] > datetime.datetime.now().date():
                messages.warning(request, 'ileri tarihli yoklama alınamaz')
            else:

                attendance_object.date = attendance_form.cleaned_data['birthDate']
                attendance_form = AttendanceDateForm(initial={'birthDate': attendance_object.date})
                attendance = attendance_services.get_attendance_by_order(total_lecture, pk, attendance_object.date)
                gelenArray = attendance['gelenSayisi']
                gelmeyenArray = attendance['gelmeyenSayisi']
                kayitArray = attendance['kayitSayisi']
                return render(request, "Attendance/attendance_list.html",
                             {'attendance': attendance_object, 'att_dict': attendance, 'form': attendance_form})

    attendance_form = AttendanceDateForm(initial={'birthDate': attendance_object.date})
    date = datetime.datetime.now().date()
    attendance = attendance_services.get_attendance_by_order(total_lecture, pk, date)
    gelenArray = attendance['gelenSayisi']
    gelmeyenArray = attendance['gelmeyenSayisi']
    kayitArray = attendance['kayitSayisi']
    return render(request, "Attendance/attendance_list.html", {'attendance': attendance_object, 'att_dict': attendance,
                                                               'form': attendance_form})


def get_attendance(request, class_object, date, order):
    class_object = Class.objects.get(pk=class_object)
    students = class_object.students.all()
    date = date
    order = order
    return render(request, "Attendance/student_list.html",
                  {'class': class_object, 'students': students, 'date': date, 'order': order})


@login_required
def attendance_post(request):
    if request.POST:
        try:
            students = request.POST.getlist('valuesChecked[]')
            students2 = request.POST.getlist('valuesUnChecked[]')
            the_class = Class.objects.get(pk=request.POST.get('class'))
            checked_students = list()
            un_checked_students = list()
            education_year = Settings.objects.filter(name='education_year')[0].value
            lecture_order = request.POST.get('order')
            date = request.POST.get('date')

            session = request.session

            user = User.objects.get(pk=session._session['_auth_user_id'])

            for id in students:
                if id != 'on':
                    checked_students.append(id)

            for id in students2:
                if id != 'on':
                    un_checked_students.append(id)

            for student in checked_students:
                student_checked = Student.objects.get(pk=student)
                attendance = Attendance(student=student_checked, class_object=the_class, education_year=education_year,
                                        lecture_order=lecture_order,
                                        is_exist=True, date=date, taken_by_who=user)
                attendance.save()

            for student in un_checked_students:
                student_un_checked = Student.objects.get(pk=student)
                attendance = Attendance(student=student_un_checked, class_object=the_class,
                                        education_year=education_year,
                                        lecture_order=lecture_order,
                                        is_exist=False, date=date, taken_by_who=user)
                attendance.save()

            # student, class, education_year, lecture_order, date, teacher
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Class.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})
