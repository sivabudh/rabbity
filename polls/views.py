from django.http import HttpResponse
from rest_framework.decorators import api_view

from polls.tasks import add_task


@api_view(['GET'])
def add(request):
    response_id = add_task.delay(3, 2)
    msg = f'Today is quite cool. Adding 2 numbers, we get our Response ID: {response_id}'
    return HttpResponse(msg, content_type='text/plain')
