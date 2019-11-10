from django.conf.urls import url

from polls.views import add

urlpatterns = [
    url('add/', add),
]
