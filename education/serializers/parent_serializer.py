from rest_framework import serializers

from education.models import Parent


class ParentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source="user.password", write_only=True)

    class Meta:
        model = Parent
        fields = '__all__'
        depth = 3
