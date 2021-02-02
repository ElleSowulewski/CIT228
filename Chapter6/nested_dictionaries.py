pokemon = {
    'P1': {
        'name':"Goodra",
        'type': 'Dragon',
        'sex': 'Male',
        },

    'P2': {
        'name':"Inteleon",        
        'type': 'Water',
        'sex': 'Male',
        },

    'P3': {
        'name':"Mew",        
        'type': 'Psychic',
        'sex': 'N/A',
        },

    'P4': {
        'name':"Leafeon",        
        'type': 'Grass',
        'sex': 'Female',
        },        
}


for key, value in pokemon.items():
    print(f"\nPokemon: {value['name']}")
    type = value['type']
    sex = value['sex']

    print(f"\tType: {type}")
    print(f"\tSex: {sex}")