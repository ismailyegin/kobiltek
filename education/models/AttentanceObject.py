import datetime

from django.db import models


class AttendanceObject:

    def __init__(self, total_lecture, class_object, students, teacher):
        self.total_lecture = total_lecture
        self.class_object = class_object
        self.students = students
        self.teacher = teacher
        self.date = datetime.datetime.now()








