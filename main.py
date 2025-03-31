import helpers
import json

#get all base pokemon types to use for data manipulation
type_list =helpers.get_pokemon_types()
all_pokemon_primary={}
all_pokemon_secondary={}
allpoke = {}

#construct new dict using pokemon types
for type in type_list['results']:
    print(f'fetch all pokemon for {type['name']}')
    pokemon_by_type =  helpers.get_pokemon_by_type(type)
    allpoke = helpers.add_pokemon_to_full_list(pokemon_by_type,allpoke)
    all_pokemon_primary,all_pokemon_secondary = helpers.add_pokemon_to_list(pokemon_by_type , all_pokemon_primary , all_pokemon_secondary)


#writing pokemon to json files as it is easier to see and check
with open('Pokemon_primary.json', 'w') as fp:
    json.dump(all_pokemon_primary, fp)

with open('Pokemon_secondary.json', 'w') as fd:
    json.dump(all_pokemon_secondary, fd)

with open('Pokemon_all.json', 'w') as fs:
    json.dump(allpoke, fs)

    




