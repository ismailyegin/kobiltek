import datetime

from django.contrib.auth.decorators import login_required
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
def student_list(request,pk):
    students = Student.objects.filter(class__pk=pk)
    total_lecture = Settings.objects.filter(name='total_lecture')
    return render(request, 'Attendance/student_list.html', {'students': students, 'total_lecture': range(int(total_lecture[0].value))})


@login_required
def attendances_of_the_day(request, pk):

    class_object = Class.objects.get(pk=pk)
    total_lecture = range(int(Settings.objects.filter(name='total_lecture')[0].value))
    students = Student.objects.filter(class__pk=pk)
    attendance_object = AttendanceObject(total_lecture, class_object, students, None)
    attendance_form = AttendanceDateForm(initial={'birthDate': attendance_object.date})
    gelenArray = list()
    gelmeyenArray = list()
    kayitArray = list()

    if request.method == 'POST':
        x=1
        return render(request, "Attendance/attendance_list.html",
                      {'attendance': attendance_object, 'form': attendance_form})
    else:
        date = datetime.datetime.now().date()
        attendance = attendance_services.get_attendance_by_order(total_lecture, pk, date)
        gelenArray = attendance['gelenSayisi']
        gelmeyenArray = attendance['gelmeyenSayisi']
        kayitArray = attendance['kayitSayisi']
        return render(request, "Attendance/attendance_list.html",
                      {'attendance': attendance_object, 'att_dict': attendance, 'form': attendance_form})


def get_attendance(request, class_object, date, lecture_order):
    class_object = Class.objects.get(pk=class_object)
    date = date
    order = lecture_order
    return render(request, "Attendance/student_list.html", {'class': class_object, 'date': date, 'order': order})

