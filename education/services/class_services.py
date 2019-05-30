from education.models import Class, Student


def get_class_list():
    class_list = Class.objects.all()
    return class_list


def add_the_class_false(students):

    for student in students:
        student.isAddedToClass = False
        student.save()
        student = None


