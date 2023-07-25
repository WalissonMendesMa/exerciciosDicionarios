pessoas = {
    "nome"   : "Joao",
    "idade"  : 21,
    "cidade" : "Belo Horizonte"
}

if "altura" in pessoas:
    print(pessoas["altura"])

for chave in pessoas:
    print(pessoas.get(chave))
