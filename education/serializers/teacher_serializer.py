from rest_framework import serializers

from education.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source="user.password", write_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'

        depth = 3
