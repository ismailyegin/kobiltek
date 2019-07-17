from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory

from patlaks.models import Competitor
from patlaks.serializers.CompetitorSerializer import CompetitorSerializer


@api_view(['GET', 'POST'])
def topic_content_list(request):
    factory = APIRequestFactory()
    request = factory.get('/')

    serializer_context = {
        'request': Request(request),
    }

    if request.method == 'GET':
        competitors = Competitor.objects.all()
        serializer = CompetitorSerializer(competitors, many=True, context=serializer_context)
        return Response(serializer.data)

    elif request.method == 'POST':
        # request.data["user"] = topic
        serializer = CompetitorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
