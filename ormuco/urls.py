from django.conf.urls import url

from . import views

app_name = "ormuco"
urlpatterns = [
 url(r'^new$', views.person_create, name='person_create'),
 url(r'^$', views.person_list, name='person_list'),
]

