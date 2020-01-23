# pokesite
A basic library to query pokemon info 

## Current status
The project have two simply operations to use queries from an api ([pokeApi](https://pokeapi.co/docs/v2.html/)) and a database (mySql pokemon data base [veekun](https://github.com/veekun/pokedex/tree/master/pokedex/data/csv)).

### Using a command
----------
The comands *queryEvolutionChain* receives an parameter that identify the ID of a evolution chain of a groups of pokemon. 

 `python3 manage.py queryEvolutionChain 13`

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

The web service expose two url`s for CRUD operation of  the information of *pokemon* and *pokemon_species* tables of a Mysql database.  

`curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/pokemon/`

```
{
    "count": 964,
    "next": "http://127.0.0.1:8000/pokemon/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "identifier": "bulbasaur",
            "species_id": 1,
            "height": 7,
            "weight": 69,
            "base_experience": 64,
            "order": 1,
            "is_default": 1
        },
        {
            "id": 2,
            "identifier": "ivysaur",
            "species_id": 2,
            "height": 10,
            "weight": 130,
            "base_experience": 142,
            "order": 2,
            "is_default": 1
        },
        {
            "id": 3,
            "identifier": "venusaur",
            "species_id": 3,
            "height": 20,
            "weight": 1000,
            "base_experience": 236,
            "order": 3,
            "is_default": 1
        },
        {
            "id": 4,
            "identifier": "charmander",
            "species_id": 4,
            "height": 6,
            "weight": 85,
            "base_experience": 62,
            "order": 5,
            "is_default": 1
        },
        {
            "id": 5,
            "identifier": "charmeleon",
            "species_id": 5,
            "height": 11,
            "weight": 190,
            "base_experience": 142,
            "order": 6,
            "is_default": 1
        },
        {
            "id": 6,
            "identifier": "charizard",
            "species_id": 6,
            "height": 17,
            "weight": 905,
            "base_experience": 240,
            "order": 7,
            "is_default": 1
        },
        {
            "id": 7,
            "identifier": "squirtle",
            "species_id": 7,
            "height": 5,
            "weight": 90,
            "base_experience": 63,
            "order": 10,
            "is_default": 1
        },
        {
            "id": 8,
            "identifier": "wartortle",
            "species_id": 8,
            "height": 10,
            "weight": 225,
            "base_experience": 142,
            "order": 11,
            "is_default": 1
        },
        {
            "id": 9,
            "identifier": "blastoise",
            "species_id": 9,
            "height": 16,
            "weight": 855,
            "base_experience": 239,
            "order": 12,
            "is_default": 1
        },
        {
            "id": 10,
            "identifier": "caterpie",
            "species_id": 10,
            "height": 3,
            "weight": 29,
            "base_experience": 39,
            "order": 14,
            "is_default": 1
        }
    ]
}
```

`curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/pokemon/254/`

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

`curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/pokemon_species/254/`

```
{
    "id": 254,
    "identifier": "sceptile",
    "generation_id": 3,
    "evolves_from_species_id": "253",
    "evolution_chain_id": 130,
    "color_id": 5,
    "shape_id": 6,
    "habitat_id": 2,
    "gender_rate": 1,
    "capture_rate": 45,
    "base_happiness": 70,
    "is_baby": 0,
    "hatch_counter": 20,
    "has_gender_differences": 0,
    "growth_rate_id": 4,
    "forms_switchable": 1,
    "order": 279,
    "conquest_order": "132"
}
```