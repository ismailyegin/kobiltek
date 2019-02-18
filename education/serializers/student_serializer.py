from rest_framework import serializers

from education.models import Student


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source="user.password", write_only=True)


    class Meta:
        model = Student
        fields = '__all__'

        depth = 2
