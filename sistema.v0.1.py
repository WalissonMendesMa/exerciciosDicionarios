itens = ['Celular', 'Batedeira', 'Televisao', 'Notebook', 'Aparelho DVD']
valores = [1000.0, 350.0, 3450.0, 6700.0, 200.0]
estoque = {}

for i in range(len(itens)):
    estoque[itens[i]] = valores[i]

for item in estoque:
    print(f'{item} = {estoque.get(item)}')
