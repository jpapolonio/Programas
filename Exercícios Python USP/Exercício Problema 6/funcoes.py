# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
    Nome: João Pedro Apolonio de Sousa Matos
    NUSP: 12558360

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

"""

#----------------------------------------------------    
def primo(n):
    '''(int) -> bool

       RECEBE um número inteiro n.
       RETORNA True se n é primo e False em caso contrário.
    '''
    # remova o print() e escreva suas função a seguir 
    primo=False
    if n>0:
      i=2
      while i<n:
        if n%i!=0:
          primo=True
        if n%i==0:
          primo=False
          return primo
        i+=1
      if n==2:
        primo=True
    return primo
#----------------------------------------------------        
def goldbach(n):
    '''(int) -> bool, int, int 

       RECEBE um número inteiro n.
       RETORNA True, p, q se n é soma de dois números primos p e q.
       Se n não é soma de dois números primos a função retorna False, 1, 1.
    '''
    # remova o print() e escreva suas função a seguir 
    i=0
    lst=[]
    while i!=n:
      if primo(i)==True:
        lst.append(i)
      i+=1
    for a in lst:
      for b in lst:
        if a+b==n:
          soma=a+b
          return True, a, b
    return False, 1, 1 

#----------------------------------------------------    
def exponencial(n0, e, p, d):
    '''(int, int, float, int) -> int 

       RECEBE 

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * um inteiro d,  d >=  0. 

      RETORNA o número total de indivíduos infectados até o dia d 
      determinado por (n0, e, p).
    '''
    nd=((1+e*p)**d)*n0
    return int(nd)
    
#--------------------------------------------------
def logistica(n0, e, p, n, d):
    '''(int, int, float, int, int) -> int
 
       RECEBE 

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * o número n de indivíduos na população; e
         * um inteiro d, d >= 0. 

       RETORNA o número total de indivíduos infectados até o dia d 
       determinado por (n0, e, p, n).

    '''
    ndantigo=n0
    nd=n0
    for i in range(1,d+1):
      nd=(1+e*p*(1-(ndantigo/n)))*ndantigo
      ndantigo=nd
    if nd>9999 or nd<0:
      nd=9999
    return int(nd)
