from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),### this is going to call the index function under views.py
    url(r'^process$', views.process, name='process'),
    url(r'^result$', views.result, name='result'),
    url(r'^back$', views.goBack, name='goBack')
]