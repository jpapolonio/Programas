nota = 0
soma=0
# O imput é sempre pergunta o número do semestre, que é o número do i+1
for i in range(0,4): 
    nota=float(input(f'{i+1} bimestre: '))
    soma+=nota
media=soma/4
#arredondar media:
media = round(media*1000)/1000
#determinar a condicao e printar resultado
if media>=6:
    condicao='foi aprovado!'
elif 6>media>=3:
    condicao='esta de recuperacao.'
else:
    condicao='foi reprovado.'
print(f'Media: {media}. Voce {condicao}')