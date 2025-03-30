import requests
import json

def getAllPokemon():
    response = requests.get("https://pokeapi.co/api/v2/pokemon")
    # print(response.content)
    jsonCount = json.loads(response.content)
    count =jsonCount['count'] 
    
    allPokemonListResponse = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={count}')
    allPokemonList = json.loads(allPokemonListResponse.content)['results']
    return allPokemonList  

def PopulatePokemonDetails(pokemonList):
    fullList = []
    print('start')
    for i in pokemonList:
        response = requests.get(i['url'])
        result = json.loads(response.content)
        # print(result)
        fullList.append(result)
    print(fullList)    