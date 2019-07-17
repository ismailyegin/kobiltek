from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from oxiterp.serializers import UserSerializer
from patlaks.models import Competitor, Country


class CompetitorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Competitor
        fields = '__all__'
        depth = 2


class CompetitorSerializer1(serializers.Serializer):
    # user = serializers.HyperlinkedIdentityField(view_name='patlaks:user-detail', lookup_field='pk')
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    gender = serializers.CharField()
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    imei = serializers.CharField(required=False)
    iban = serializers.CharField(required=False)
    birthDate = serializers.DateField(required=False)
    country = serializers.SlugRelatedField(

        read_only=True,
        slug_field='name'
    )

    mobilePhone = serializers.CharField(required=False)
    country_post = serializers.IntegerField(write_only=True)
    reference = CompetitorSerializer(read_only=True)


    def create(self, validated_data):
        # user_data = validated_data.pop('user')

        # user = User.objects.create(**user_data)

        user = User.objects.create_user(username=validated_data.get('username'),
                                        first_name=validated_data.get('first_name'),
                                        last_name=validated_data.get('last_name')
                                        , email=validated_data.get('email'))
        user.set_password(validated_data.get('password'))
        user.save()
        gender = validated_data.get('gender')
        birthDate = validated_data.get('birthDate')
        imei = validated_data.get('imei')
        iban = validated_data('iban')
        country = Country.objects.get(pk=validated_data('country_post'))

        competitor = Competitor.objects.create(user=user, gender=gender, birthDate=birthDate)

        return competitor
