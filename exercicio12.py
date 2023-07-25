estoque = {
    "item1" : 10,
    "item2" : 5,
    "item3" : 20
}
soma = 0

for item in estoque:
    soma = soma + estoque.get(item)
   
print(soma)
