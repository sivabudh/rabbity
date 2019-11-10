from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def add(request):
    msg = 'Today is quite cool.'
    return HttpResponse(msg, content_type='text/plain')
