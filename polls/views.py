from django.http import HttpResponse
from rest_framework.decorators import api_view

from polls.tasks import add_task


@api_view(['GET'])
def add(request):
    response_id = add_task.delay(3, 2)
    output = response_id.get()
    msg = f'Today is quite cool. Adding 2 numbers, we get our sum: {output}'
    return HttpResponse(msg, content_type='text/plain')
