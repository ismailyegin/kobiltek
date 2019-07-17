from django.contrib.auth.models import User
from pytz import unicode
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

from patlaks.models import Competitor
from patlaks.serializers.CompetitorSerializer import CompetitorSerializer, CompetitorSerializer1


class CompetitorList(APIView):

    def get(self,request,format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        competitors = Competitor.objects.all()
        serializer =CompetitorSerializer(competitors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompetitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCompetitor(APIView):

    def get(self, request, format=None):

        competitors = Competitor.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = CompetitorSerializer1(competitors, many=True,context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = CompetitorSerializer1(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def user_detail(request,pk):
    return User.objects.get(pk=pk)