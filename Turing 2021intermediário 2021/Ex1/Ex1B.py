N=int(input(''))
lst=[]
lst_arrumada=[]
#Criar lista de emails:
for i in range(0,N):
    nvemail=str(input(''))
    lst.append(nvemail)
#Remover emails inseridos com inicio ou final ' ' para evitar bugs
#for i in range(0,len(lst)):
#    email=lst[i]
#    while email[0]==' ':
#        email=email[1:]
#    while email[-1]==' ':
#        email=email[0:-1]
#    lst[i]=email
#(Codigo funcionou nos meus testes, mas nao foi pedido e fiquei com medo de dar algum bug, entao tirei na ultima hora)

#Pegaremos cada email, e separaremos no meio, reescreveremos cada parte ao contrario e juntaremos depois.
#O meio para numeros e a funcao round do comprimento dividido por 2
for e in range(0,len(lst)):
    email=lst[e]
    if (len(email))%2==0:
        meio=len(email)//2
    else:
        meio=round(len(email)//2)
    prim_metade= email[0:meio]
    seg_metade=email[meio:]
    email_certo=(prim_metade[::-1])+(seg_metade[::-1])
    lst_arrumada.append(email_certo)
#Se o final do email não for @usp.br, sera printado ERRO, caso contrário teremos o email certo
for email in lst_arrumada:
    if email[-7:]!= '@usp.br': 
        print('ERRO')
    else:
        print(email)