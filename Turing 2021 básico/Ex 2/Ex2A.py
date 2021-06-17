lst=[]
soma=0
for i in range(0,6):
    value=int(input(''))
    if i==0:
        min=max=value
    if min>value:
        min=value
    if max<value:
        max=value
    soma+=value
    lst.append(value)
print(f'A soma dos elementos da lista e {soma}, o maior numero e {max} e o menor e {min}.')