import requests
import json
from pprint import pprint


#region Get all pokemon
# initially went with the aproach of getting all pokemon and then getting all details but it was too slow 
def get_all_pokemon():
    '''Fetchs full list of all pokemon'''
    response = requests.get("https://pokeapi.co/api/v2/pokemon")
    json_count = json.loads(response.content)
    count =json_count['count'] 
    
    all_pokemon_list_response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={count}')
    all_pokemon_list = json.loads(all_pokemon_list_response.content)['results']
    return all_pokemon_list  

def populate_pokemon_details(pokemon_list):
    '''takes full list of pokemon and generates a new list with all pokemon details'''
    full_list = []
    for i in pokemon_list:
        response = requests.get(i['url'])
        result = json.loads(response.content)
        full_list.append(result)
    return full_list

def fetch_individual_pokemon(name):
    '''Fetches and returns an individual pokemon's full data object'''
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if(response.status_code == 200): 
        #I Considered mapping this to a Model object I am just not too sure how to go about this
        pokemon = json.loads(response.content)
        return pokemon
    else:
        raise Exception
#endregion 


def get_pokemon_types():
    '''fetches full list of pokemon types'''
    types_response = requests.get('https://pokeapi.co/api/v2/type')
    result = json.loads(types_response.content)
    return result 

def get_pokemon_by_type(pokemon_object):
    '''fetches all pokemon by type'''
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

def prompt_for_name(name):
    '''prompts the user for a pokemon name with very basic error handling'''
    try:
        response = fetch_individual_pokemon(name)
        pprint(response)
    except:
        user_input = input("it seems that pokemon could not be found perhaps try another name:")
        prompt_for_name(user_input)