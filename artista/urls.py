from django.conf.urls import url

from artista import views

urlpatterns = [
    url(r'^$', views.Artista.as_view()),
    url(r'^(?P<pk>\d+)$', views.ArtistaId.as_view()),
]