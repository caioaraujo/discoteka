from django.conf.urls import url

from album import views

urlpatterns = [
    url(r'^$', views.Album.as_view()),
    url(r'^(?P<pk>\d+)$', views.AlbumId.as_view()),
]