def menorNota(notasAlunos):
    auxiliar = 2**10
    for nota in notasAlunos:
        if notasAlunos.get(nota) < auxiliar:
            chaveMenorNota = nota
            auxiliar = notasAlunos.get(nota)
    return chaveMenorNota

def maiorNota(notasAlunos):
    auxiliar = 0
    for nota in notasAlunos:
        if auxiliar > notasAlunos.get(nota):
            maiorNota = auxiliar
        auxiliar = notasAlunos.get(nota)
    return maiorNota


notasAlunos = {
    'joao'    :  7.5,
    'pedro'   :  6.8,
    'ana'     :  9.2,
    'maria'   :  7.3,
    'gabriel' :  8.4
}
mediaNotas = 0

for nota in notasAlunos:
    mediaNotas = mediaNotas + notasAlunos.get(nota)

mediaNotas = mediaNotas / len(notasAlunos)


maiorNota = maiorNota(notasAlunos)
chaveMenorNota = menorNota(notasAlunos)

for nota in notasAlunos:
    if menorNota == notasAlunos.get(nota):
        chaveMenorNota = nota

notasAlunos.pop(chaveMenorNota)

print(f"A media da turma é: {round(mediaNotas, 2)}")
print(f"A maior nota da classe é {maiorNota}")
print(f"O aluno '{chaveMenorNota}' foi removido do dicionario por possuir menor nota.")
