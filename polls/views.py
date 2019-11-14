from django.http import HttpResponse
from rest_framework.decorators import api_view

from rabbity.celery import app as celery_app

@api_view(['GET'])
def add(request):
    response = celery_app.send_task('add_task', kwargs={'a': 5, 'b': 10})
    output = response.get()
    msg = f'Today is quite cool. Adding 2 numbers, we get our sum: {output}'
    return HttpResponse(msg, content_type='text/plain')
