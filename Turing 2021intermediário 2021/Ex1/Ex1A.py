N=int(input(''))
economia=0
lst=[]
#Criar lista de emails:
for i in range(0,N):
    nvemail=str(input(''))
    lst.append(nvemail)
#Remover emails inseridos com inicio ou final ' ' para evitar bugs #for i in range(0,len(lst)):
#    email=lst[i]
#    while email[0]==' ':
#        email=email[1:]
#    while email[-1]==' ':
#        email=email[0:-1]
#    lst[i]=email
#(Codigo funcionou nos meus testes, mas nao foi pedido e fiquei com medo de dar algum bug, entao tirei na ultima hora)

#Para cada email na lista, vamos pegar cada letra de tras para frente e comparar com a respectiva letra do email posterior,
#se forem iguais, economia aumenta em um 
for e in range(0,len(lst)):
    try: #quando chegarmos ao ultimo email havera IndexError, pois nao ha email posterior para ser prox_email, por isso o try e except
        email=lst[e]
        prox_email=lst[e+1]
    except IndexError:
        continue
    for i in range(0,len(email)-7):#nao queremos considerar os 7 ultimos valores, '@usp.br'
        try:# quando email> prox_email, ha um IndexError, nao ha uma letra correspondente no proximo email para comparar.
            if prox_email[i]==email[i]:
                economia+=1
            else:
                break
        except IndexError: 
            continue
print(economia)