# pokesite
A basic library to query pokemon info 

## Current status
The project have two simply operations to use queries from an api ([pokeApi](https://pokeapi.co/docs/v2.html/)) and a database (mySql pokemon data base [veekun](https://github.com/veekun/pokedex/tree/master/pokedex/data/csv)).

### Using a command
----------
The comands *queryEvolutionChain* receives an parameter that identify the ID of a evolution chain of a groups of pokemon. 

 `python3 manage.py queryEvolutionChain 54`

Returns the information (Name, Base Stats, Height, Weight, Id) of the every pokemon belong to evolution chain. And print a console tree with the name of pokemons in the line of evolution.

```
Name:  horsea
Bases stats: 
        speed :  60
        special-defense :  25
        special-attack :  70
        defense :  70
        attack :  40
        hp :  30
Height: 4
Weight:  80
Id:  116
Name:  seadra
Bases stats: 
        speed :  85
        special-defense :  45
        special-attack :  95
        defense :  95
        attack :  65
        hp :  55
Height: 12
Weight:  250
Id:  117
Name:  kingdra
Bases stats: 
        speed :  85
        special-defense :  95
        special-attack :  95
        defense :  95
        attack :  95
        hp :  75
Height: 18
Weight:  1520
Id:  230

horsea
 |->seadra
        |->kingdra
```


### Using WebService
----------

The web service expose an api to query a mysql database. The first operation API query with a pokemon name parameter the information of the pokemon and all chain evolution.

`curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/pokemon?name=bulbasaur`

```
{
    "pokemon": [
        {
            "id": 1,
            "identifier": "bulbasaur",
            "species_id": 1,
            "height": 7,
            "weight": 69,
            "base_experience": 64,
            "order": 1,
            "is_default": 1
        }
    ],
    "evolution": [
        {
            "id": 2,
            "identifier": "ivysaur",
            "species_id": 2,
            "height": 10,
            "weight": 130,
            "base_experience": 142,
            "order": 2,
            "is_default": 1,
            "evolution_type": "evolution"
        },
        {
            "id": 3,
            "identifier": "venusaur",
            "species_id": 3,
            "height": 20,
            "weight": 1000,
            "base_experience": 236,
            "order": 3,
            "is_default": 1,
            "evolution_type": "evolution"
        }
    ]
}
```

The second operation search a pokemon with the id of the pokemon

`curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/pokemon/254`

```
{
    "id": 254,
    "identifier": "sceptile",
    "species_id": 254,
    "height": 17,
    "weight": 522,
    "base_experience": 239,
    "order": 333,
    "is_default": 1
}
```
