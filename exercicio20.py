frutas = {
    'banana'  : 3,
    'maca'    : 5,
    'abacate' : 2
}

frutas['goiaba'] = 1
frutas.update({'goiaba': 4})

print(frutas['goiaba'])

if len(frutas) > 0:
    print(f'O dicionario frutas contem {len(frutas)} itens.')
else:
    print('dicionario frutas nao possui nenhum item.')
