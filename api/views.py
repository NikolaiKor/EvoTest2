from django.http import JsonResponse

from api.models import People


def index(request):
    return JsonResponse({'epithet': People.epithet_by_name(request.GET['name'])})
