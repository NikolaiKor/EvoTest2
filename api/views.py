from django.http import JsonResponse, HttpResponse

from api.models import People


def index(request):
    epithet = People.epithet_by_name(request.GET['name'])
    if epithet == '':
        return HttpResponse(status=404)
    else:
        return JsonResponse({'epithet': People.epithet_by_name(request.GET['name'])})
