from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    url(r'^api/polls/', include('polls.urls')),
]
