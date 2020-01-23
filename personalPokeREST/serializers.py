from personalPokeREST.models import pokemon, pokemon_species
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class pokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pokemon
        fields = ['id','identifier','species_id','height','weight','base_experience','order','is_default']

class pokemon_speciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pokemon_species
        fields = ['id','identifier','generation_id','evolves_from_species_id','evolution_chain_id','color_id','shape_id','habitat_id','gender_rate','capture_rate','base_happiness','is_baby','hatch_counter','has_gender_differences','growth_rate_id','forms_switchable','order','conquest_order']