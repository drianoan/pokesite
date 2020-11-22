from django.conf.urls import url,include
from personalPokeREST import views

urlpatterns = [
    url(r'^api/pokemon$', views.pokemon_list),
    url(r'^api/pokemon/(?P<pk>[0-9]+)$', views.pokemon_detail),
]