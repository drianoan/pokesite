from personalPokeREST.models import pokemon, pokemon_species
from personalPokeREST.serializers import pokemonSerializer, pokemon_speciesSerializer
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework import status, viewsets
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
import json


# Create your views here.

class pokemonViewSet(viewsets.ModelViewSet):
    queryset = pokemon.objects.all()
    serializer_class = pokemonSerializer

class pokemon_speciesViewSet(viewsets.ModelViewSet):
    queryset= pokemon_species.objects.all()
    serializer_class = pokemon_speciesSerializer
#
# Author: Diego Ricardo Riaño driano@mailserver.com
# Description: Exposed method from retrieve object with a condition parameter.
# @request: Request from web services
#
@api_view(['GET'])
def pokemon_list(request):
    if request.method == 'GET':
        #Get a complete list of all pokemon
        pkmn_list_complete = pokemon.objects.all()
        # Get the parameter name from request
        name = request.GET.get('name', None)
        # Validate that parameter exist
        if name is not None:
            #Filter the list with the name parameter
            pkmn = pkmn_list_complete.filter(identifier=name)
            # Verify that object exists
            if pkmn.exists():
                # Serialize the seek object
                pkmn_serializer = pokemonSerializer(pkmn, many=True)
                # Search the evolution_chain of the pokemon found
                specie_serializer  = pokemon_speciesSerializer(pokemon_species.objects.get(identifier=name))
                # Get the evolutions related
                evolutions_serializer = pokemon_speciesSerializer(pokemon_species.objects.all().filter(evolution_chain_id=specie_serializer.data["evolution_chain_id"]),many=True)
                #Verify if the pokemon has evolution or not
                if len(evolutions_serializer.data) == 1:
                    ev = "The pokemon has no evolution"
                else:
                    ev = []
                    # Maintain id of searched pokemon
                    id_flag = pkmn_serializer.data[0]["id"]
                    # Flag for handle evolutions
                    evolution_flag = 0
                    # Loop for walking evolution chain array
                    for evo in evolutions_serializer.data:
                        # Control for dont put the searched pokemon in the evolution information
                        if evo["identifier"]!= name and int(id_flag) != int(evo["id"]):
                            #Filter the complete list pokemon by identifier (name)
                            temp_pokemon = pokemonSerializer(pkmn_list_complete.filter(identifier=evo["identifier"]),many=True)
                            # prepare information from evolution
                            evo_text = ""
                            #When doesnt have previous evolution is a root evolution
                            if evo["evolves_from_species_id"] == '':
                                evo_text = "root evolution"
                                # Stores actual id for next comparison
                                evolution_flag = evo["id"]
                            else:
                                # Evaluate if current pokemon evolves from searched pokemon  
                                # or if id from searched pokemon are lower that current id (principle of evolution id are bigger)
                                if (int(id_flag) == int(evo["evolves_from_species_id"]) or int(id_flag) < int(evo["id"])):
                                    evo_text = "evolution"   
                                else:
                                    # Evaluate if previous pokemon have the same evolves_from_species_id of current
                                    if int(evolution_flag) == int(evo["evolves_from_species_id"]):
                                        evo_text = "same level evolution"
                                        # Change hte flag for other evolutions path
                                        evolution_flag = int(evo["evolves_from_species_id"])
                                    else:
                                        #After all is a pre evolution.
                                        evo_text = "pre evolution"
                            # Add information to data of current pokemon        
                            temp_pokemon.data[0]["evolution_type"] = evo_text
                            # Add object to part of the response
                            ev.append(temp_pokemon.data[0])
                            
                # Create the object response whit the searched pokemon and the information of chain evolution pokemons
                response = {'pokemon':pkmn_serializer.data, 'evolution': ev}
                # Build a json response with the object
                return JsonResponse(response, safe=False)
            else:
                return JsonResponse({'message': 'No item found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse({'message': 'Use ´name´ parameter'}, status=status.HTTP_404_NOT_FOUND) 
         
#
# Author: Diego Ricardo Riano driano@mailserver.com
# Description: Exposed method from retrieve object by id
# @request: Request from web services
# @pk: primary key search
#
@api_view(['GET', 'PUT', 'DELETE'])
def pokemon_detail(request,pk):
    # find pokemon by pk (id)
    try:
        pkmn = pokemon.objects.get(pk=pk)
        if request.method == 'GET':
            pkmn_serializer= pokemonSerializer(pkmn)
            return JsonResponse(pkmn_serializer.data)
    # pylint: disable=maybe-no-member
    except pokemon.DoesNotExist: 
        return JsonResponse({'message': 'The pokemon does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 