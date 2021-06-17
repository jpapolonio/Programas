a = input('')
#Separar os valores de a em K(tamanho do estacionamento) e N(numero de instantes)
lst_values= a.split(' ')
K = int(lst_values[0])
N = int(lst_values[1])

#Criar lista com horários de entrada
horarios_de_entrada=[]
for i in range(0,N):
    horarios_de_entrada.append(int(input('')))

#Criar dicionario que enumera (da um 'nome') os carros em realação a ordem que foi colocado na lista a partir de 1,
#como 1(primeiro), 2(segundo)...
nome_dos_carros={}
for i in range(0,len(horarios_de_entrada)):
    nome_dos_carros[horarios_de_entrada[i]]=i+1

#Criar lista com K 0's, onde 0 indica espaço vazio
#e os carros futuramente irão passar da esquerda(entrada) até a direita(saída) ocupando o respectivo espaço
espacos_no_estacionamento=[]
for i in range(0,K):
    espacos_no_estacionamento.append(0)

instante_pedido= int(input(''))
#Para cada instante entre 1 e o instante_pedido+1,
#a partir do carro mais perto da saida, cada carro ira 1 unidade para a esquerda
#Pararemos quando chegar o instante_pedido,
for i in range(1,instante_pedido+1):#precisamos de >=1 para a adicao de novos carros como sera visto no fim da iteracao
    for e in range(1,len(espacos_no_estacionamento)+1):#para carros que já estejam no estacionamento
        e=-e#, de tras pra frente para evitar perca de valores
        if espacos_no_estacionamento[e]!= 0:
            if e==-1:#se o carro está no ultimo lugar, ele sai e o espaço vira 0(que podera mudar para o numero do prox carro depois)
                espacos_no_estacionamento[e]=0
            elif e==-len(espacos_no_estacionamento):#se o carro está no primeiro lugar, ele vai para o segundo e seu espaco vira 0(fiz separado para evitar bugs)
                espacos_no_estacionamento[e+1]=espacos_no_estacionamento[e]
                espacos_no_estacionamento[e]=0
            else:#o carro vai pro proximo lugar e seu espaço anterior fica vago(=0)
                espacos_no_estacionamento[e+1]=espacos_no_estacionamento[e]
                espacos_no_estacionamento[e]=0
    if i in horarios_de_entrada:#para novos carros, adiciona-los
        espacos_no_estacionamento[0]=i
#traduzir a lista das posicoes no estacionamento dos carros, enumerados pelo instante que entraram no estacionamento para
#sua ordem na lista de horarios('nome'), criando uma nova lista:
estacionamento_traduzido=[]
for i in range(0,len(espacos_no_estacionamento)):
    if espacos_no_estacionamento[i]==0:
        estacionamento_traduzido.append(0)
    else:
        estacionamento_traduzido.append(nome_dos_carros[espacos_no_estacionamento[i]])
#printar no padrão sem virgulas, com espacos e sem colchetes
resultado=''
for i in estacionamento_traduzido:
    resultado += str(i)
    resultado+= ' '
print(resultado)