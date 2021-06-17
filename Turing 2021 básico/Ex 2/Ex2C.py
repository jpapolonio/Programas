#dic_dias_semana representa os dias da semana na forma: Domingo= 0, Segunda-feira= 1,... até Sábado= 6
#dic representa o total de votos para cada dia da semana com Domingo= 0, Segunda-feira= 1,... até Sábado= 6
dic_dias_semana={0:'Domingo',1:'Segunda',2:'Terca',3:'Quarta',4:'Quinta',5:'Sexta',6:'Sabado'}
dic={0:0,1:0,2:0,3:0,4:0,5:0,6:0}
for i in range(0,7):
    votos=int(input(''))
    if votos==-1:
        break
    dic[i]=votos
#Achar o dia mais votado(raciocinio analogo ao usado em 2B):
count=0
for key in dic:
    if dic[key] > count:
        maisvotado=key
        count=dic[key]
#Printar o resultado:
print('resultados')
for e in range(0,7):
    print(f'{dic_dias_semana[e]} = {dic[e]}')
print(f'O dia vencedor e {dic_dias_semana[maisvotado]}')