import pokebase as pb
import requests



page = 0
i = 'null'

while (i != 'e'):
    if (page < 0):
        page = 0
        r = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=20')
    else:
        r = requests.get('https://pokeapi.co/api/v2/pokemon?offset=' + str(page * 20) + '&limit=20')
    dict = r.json()
    text = '''------------------------\nPOKEMONS GUIDE\n------------------------\n\n'''
    for j in range(20):
        name = dict['results'][j]['name']
        name = str(name).capitalize()
        text += str(page * 20 + j + 1) + '. ' + name + '\n'
    text += '''\nEnter the name of the pokemon to get more info about it or choose one of options below:
    [p - Previous page]
    [n - Next page]
    [e - Exit]'''
    print(text)
    i = input()
    if (i == 'p'):
        page -= 1
    elif (i == 'n'):
        page += 1
    elif (i == 'e'):
        break
    else:
        pokemon = pb.pokemon(i.lower())
        abilities = ''
        forms = ''
        for k in range(len(pokemon.abilities)):
            ability = f'{pokemon.abilities[k].ability.name}, '
            ability = ability.capitalize()
            abilities += ability
        for k in range(len(pokemon.forms)):
            form = f'{pokemon.forms[k].name}, '
            form = form.capitalize()
            forms += form
        abilities.title()

        info = f'''\n\n~~~~~~~~~~~~~~~
Name: {pokemon.name},
Order: {pokemon.order},
Base XP: {pokemon.base_experience},
Height: {pokemon.height},
Weight: {pokemon.weight},
Default: {pokemon.is_default},
Abilities: {abilities}
Forms: {form}
'''
        print(info + '\n\n [Enter any key to return...]')
        temp = input()



    