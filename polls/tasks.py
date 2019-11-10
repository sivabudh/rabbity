from celery.task import task


@task(name="add_task")
def add_task(a, b):
    print(f"Adding 2 numbers: {a} + {b}")
    return a + b