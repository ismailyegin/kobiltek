from education.models import Class


def get_class_list():
    class_list = Class.objects.all()
    return class_list
