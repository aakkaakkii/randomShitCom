from django.urls import path

from .views import app


urlpatterns = [
    path('', app.index, name='index'),
    path('get_id/', app.get_id, name='get_id')
]
