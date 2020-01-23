import requests

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Query evolution chain and get the pokemons that belong to that chain'

    def add_arguments(self, parser):
        #pass
        parser.add_argument('chain_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        if len(options['chain_ids']) > 1:
            print('Only one parameter please')
        else:
            try:
                id_chain=  int(options['chain_ids'][0])
                url_chain = 'https://pokeapi.co/api/v2/evolution-chain/'
                
                response_chain = requests.get(url_chain)
                chain = response_chain.json()
                #Verificación de rango de cadenas de evolución
                if id_chain > 0 and id_chain < int(chain['count']):
                    #Consulta de la cadena de evolucion
                    response_chain = requests.get(url_chain+ str(id_chain))
                    chain = response_chain.json()

                    #Información del pokemon
                    pokemon_name = chain['chain']['species']['name']
                    pokemon = queryPoke(pokemon_name)
                    stats = pokemon['stats']
                    evolutions = chain['chain']['evolves_to']
                    #Impresión de los datos
                    imprimirData (pokemon)
                    #Construcción de strings para evoluciones
                    string_evol= '\n' + pokemon_name 
                    for x in evolutions:
                        string_evol= string_evol + '\n |->' + str(x['species']['name'])
                        poke = queryPoke(x['species']['name'])
                        imprimirData(poke)
                        if len(x['evolves_to'])!= 0:
                            string_evol = string_evol + '\n'
                            for y in x['evolves_to']:
                                string_evol = string_evol + '\t|->' + str(y['species']['name'])
                                poke = queryPoke(y['species']['name'])
                                imprimirData(poke)
                    print(string_evol)
                else:
                    print('The number is out of range')
            except Exception as e:
                raise CommandError(repr(e))

def imprimirData(pokemon):
    print('Name: ',pokemon['name'])
    print('Bases stats: ')
    stats = pokemon['stats']
    for x in stats:
        print('\t' + x['stat']['name'], ': ' ,x['base_stat'])
    print('Height:', pokemon['height'])
    print('Weight: ', pokemon['weight'])
    print('Id: ', pokemon['id']) 

def queryPoke(pokemon_name):
    url_pokemon = 'https://pokeapi.co/api/v2/pokemon/'
    response_pokemon = requests.get(url_pokemon + str(pokemon_name))
    pokemon = response_pokemon.json()
    return pokemon      
    
    