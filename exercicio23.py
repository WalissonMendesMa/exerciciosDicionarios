notasAlunos = {
    'joao'    :  7.5,
    'pedro'   :  6.8,
    'ana'     :  9.2,
    'maria'   :  7.3,
    'gabriel' :  8.4
}
mediaNotas = 0
auxiliar = 0

for nota in notasAlunos:
    mediaNotas = mediaNotas + notasAlunos.get(nota)

mediaNotas = mediaNotas / len(notasAlunos)

print(f'A media da turma é: {round(mediaNotas, 2)}')

for nota in notasAlunos:
    if auxiliar > notasAlunos.get(nota):
        maiorNota = auxiliar
    auxiliar = notasAlunos.get(nota)

print(f'A maior nota da classe é {maiorNota}')
