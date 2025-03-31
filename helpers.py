import requests
import json

#region Get all pokemon
# initially went with the aproach of getting all pokemon and then getting all details but it was too slow 
def getAllPokemon():
    '''Fetchs full list of all pokemon'''
    response = requests.get("https://pokeapi.co/api/v2/pokemon")
    jsonCount = json.loads(response.content)
    count =jsonCount['count'] 
    
    allPokemonListResponse = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={count}')
    allPokemonList = json.loads(allPokemonListResponse.content)['results']
    return allPokemonList  

def PopulatePokemonDetails(pokemonList):
    '''takes full list of pokemon and generates a new list with all pokemon details'''
    fullList = []
    for i in pokemonList:
        response = requests.get(i['url'])
        result = json.loads(response.content)
        fullList.append(result)
    return fullList
#endregion 


def get_pokemon_types():
    '''fetchs full list of pokemon types'''
    types_response = requests.get('https://pokeapi.co/api/v2/type')
    result = json.loads(types_response.content)
    return result 

def get_pokemon_by_type(pokemon_object):
    '''fetchs all pokemon by type'''
    pokemon = requests.get(pokemon_object['url'])
    result = json.loads(pokemon.content)
    return result

def add_pokemon_to_list(pokemon_by_type,all_pokemon_primary , all_pokemon_secondary):
    '''passes singular pokemon through to add_singular_pokemon_to_list to sort by primary or secondary types'''
    workable_pokemon_list = pokemon_by_type['pokemon']
    poke_type = pokemon_by_type['name']
    for pokemon in workable_pokemon_list:
        if(pokemon['slot']==1):
            all_pokemon_primary=add_singular_pokemon_to_list(pokemon,poke_type,all_pokemon_primary)
        else:
            all_pokemon_secondary=add_singular_pokemon_to_list(pokemon,poke_type,all_pokemon_secondary)
    return (all_pokemon_primary , all_pokemon_secondary)
                
def add_singular_pokemon_to_list(pokemon,poke_type,all_pokemon):
    '''this method populates the pokemon dicts where specefic pokemon are required'''
    poke_name = pokemon['pokemon']['name']
        #first cheeck if type is in list 
    if(poke_type in all_pokemon):
        all_pokemon[poke_type].append(poke_name)
    else:
        all_pokemon[poke_type] = ([poke_name]) 
       
         
    return all_pokemon

def add_pokemon_to_full_list(pokemon_by_type,all_pokemon):
    '''this method populates the all pokemon list dict using the pokemon types'''
    workable_pokemon_list = pokemon_by_type['pokemon']
    poke_type = pokemon_by_type['name']
    for pokemon in workable_pokemon_list:
        poke_name = pokemon['pokemon']['name']
        #first cheeck if type is in list 
        if(poke_type in all_pokemon):
            all_pokemon[poke_type].append(poke_name)
        else:
            all_pokemon[poke_type] = ([poke_name]) 
         
    return all_pokemon