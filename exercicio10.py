pessoas = {
    "nome"   : "Joao",
    "idade"  : 21,
    "cidade" : "Belo Horizonte"
}

if "altura" in pessoas:
    print(pessoas["altura"])

pessoas.pop("cidade")

pessoas["idade"] = 22

pessoas.update({"idade" : 23})

for chave in pessoas:
    print(f"{chave} : {pessoas[chave]}")
