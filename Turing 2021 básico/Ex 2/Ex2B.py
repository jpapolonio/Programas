lst=[]
soma=0
dic={}
#Os valores serão perguntados, somados, adicionados a uma lista e a uma key de dicionário(se a key não existe, será criada)
for i in range(0,6):
    value=int(input(''))
    soma+=value
    lst.append(value)
    if value not in dic:
        dic[value] = 1
    else:
        dic[value]+=1
#Para achar a moda, a "countmoda" servirá para comparar as keys mais frequentes anteriores com a frequencia das novas keys.
countmoda=0
for key in dic:
    if dic[key] > countmoda:
        moda=key
        countmoda=dic[key]
media=(soma/6)
#arredondar media:
media = round(media*100)/100
if dic[moda]==1:
    print(f'A media e {media}. A lista e amodal.')
else:
    print(f'A media e {media}. A moda e {moda}.')