from personalPokeREST.models import pokemon, pokemon_species
from rest_framework import viewsets
from personalPokeREST.serializers import pokemonSerializer, pokemon_speciesSerializer


# Create your views here.

class pokemonViewSet(viewsets.ModelViewSet):
    queryset = pokemon.objects.all()
    serializer_class = pokemonSerializer

class pokemon_speciesViewSet(viewsets.ModelViewSet):
    queryset= pokemon_species.objects.all()
    serializer_class = pokemon_speciesSerializer


