a = input('')
da_pra_rolar='sim'#assumimos inicialmente que da pra rolar
#Separar os valores de a em K(tamanho do estacionamento) e N(numero de instantes)
lst_values= a.split(' ')
K = int(lst_values[0])
N = int(lst_values[1])

#Criar lista com 0's que serao substituidos pelo numero do carro que entrar
lst=[]
for i in range(0,K):
    lst.append(0)

#A cada instante perguntaremos qual carro entra ou sai:

    #Se o valor for positivo, veremos se ha espaços vazios na lista (0's)
        #Se nao houverem 0's, esperamos o usuario acabar e printamos nao
        #Se houver um espaço, procuraremos na lista o primeiro espaco 0(vazio) e colocaremos la o número do carro.

    #Se o valor for negativo, checamos se o valor oposto está na lista(+v) para evitar bugs(se ocorrer não impossibilita nada)
        #Se esta, procuramos a posicao do valor oposto na lista(+v) e:
            #Se ha valores diferentes de 0 atras dele, esperamos o usuario terminar e printamos nao
            #Se nao ha carros atras, a posição do carro na lista se torna 0, pois o carro vai embora 
for i in range(0,N):
    v=int(input('')) 
    if v>0:
        if 0 in lst:
            for e in range(len(lst)):
                if v not in lst:#para o carro nao ser inserido em todos os 0's
                    if lst[e]==0:
                        lst[e]=v
        else:
            da_pra_rolar='nao'
    posicao=0
    if v<0:
        if abs(v) in lst:
            while lst[posicao]!=abs(v):#descobrir a posicao de v
                posicao+=1
            for u in range(posicao+1, len(lst)):
                if lst[u]!=0:
                    da_pra_rolar='nao'
                else:
                    lst[posicao]=0
#Se nao der pra rolar printamos nao, se nada impedir de rolar, printamos sim
if da_pra_rolar== 'nao':
    print('nao')
else:
    print('sim')
