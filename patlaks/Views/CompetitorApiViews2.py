from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

from patlaks.models import Competitor
from patlaks.serializers.CompetitorSerializer import CompetitorSerializer1
from django.http import HttpResponse


@csrf_exempt
def competitor_list(request):
    if request.method == 'GET':
        competitors = Competitor.objects.all()
        serializer = CompetitorSerializer1(competitors, many=True)
        return JSONResponse(serializer.data)
