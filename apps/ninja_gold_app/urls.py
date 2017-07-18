from django.conf.urls import url
from views import index, process_money, reset

urlpatterns = [
    url(r'^$', index),
    url(r'^process_money$', process_money),
    url(r'^reset$', reset)
]