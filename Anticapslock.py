def minuscular(n):
    n=n.lower()
    print(n)
    return 0
def maiuscular(n):
    n=n.upper()
    print(n)
    return 0
def ask():
    n=input('maiuscular(+), minuscular(-) ou sair(s)? ')
    if n=='s':
        print('bye')
        return 0
    if n=='+':
        n=input('bote o texto: ')
        maiuscular(n)
    elif n=='-':
        n=input('bote o texto: ')
        minuscular(n)
    ask()
    


ask()