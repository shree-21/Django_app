from django.conf.urls import url
from photo_app import views

urlpatterns = [
    url(r'^$', views.photo_upload, name='photo_upload'),
]