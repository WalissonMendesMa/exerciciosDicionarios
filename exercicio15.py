estoque = {
    "item1" : 10,
    "item2" : 5,
    "item3" : 20
}
soma = 0

for item in estoque:
    soma = soma + estoque.get(item)
   
print(soma)

if "item2" in estoque:
    print('ok, item encontrado.')
else:
    print('item nao encontrado no estoque.')

estoque.pop("item3")

print(estoque)

estoque["novoItem"] = 45

print(estoque)
