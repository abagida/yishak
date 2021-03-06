from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/ui/$', views.ui, name='ui'),
    url(r'^about/frontend/$', views.frontend, name='frontend'),
    url(r'^about/backend/$', views.backend, name='backend'),
    url(r'^about/projects/$', views.projects, name='projects'),
]
