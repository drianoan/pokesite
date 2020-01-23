# pokesite
A basic library to query pokemon info 

## Current status
The project have two simply operations to use queries from an api ([pokeApi](https://pokeapi.co/docs/v2.html/)) and a database (mySql pokemon data base [veekun](https://github.com/veekun/pokedex/tree/master/pokedex/data/csv)).

### Using a command
----------
The comands *queryEvolutionChain* receives an parameter that identify the ID of a evolution chain of a groups of pokemon. 

 `python3 manage.py queryEvolutionChain 13`

Returns the information (Name, Base Stats, Height, Weight, Id) of the every pokemon belong to evolution chain. And print a console tree with the name of pokemons in the line of evolution.

`Name:  horsea
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
        |->kingdra`
