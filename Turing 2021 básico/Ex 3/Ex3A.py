altura= float(input('Qual e a altura? '))
peso= float(input('Qual e o peso? '))
IMC = (peso / (altura**2))
#arredondar IMC:
IMC = round(IMC*100)/100
if IMC>40:
    condicao= 'Obeso Mórbido'
elif IMC>30:
    condicao= 'Obeso'
elif IMC>25:
    condicao= 'Sobrepeso'
elif IMC>20:
    condicao= 'Normal'
elif IMC>16:
    condicao= 'Subpeso'
else:
    condicao= 'Subpeso Severo'
print(f'IMC = {IMC}; Condicao {condicao}')