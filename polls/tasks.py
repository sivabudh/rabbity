from celery.task import task
from django.contrib.auth.models import User


@task(name="add_task")
def add_task(a, b):
    print(f"Adding 2 numbers: {a} + {b}")
    user = User.objects.first()
    if not user:
        return a + b
    else:
        return user.email