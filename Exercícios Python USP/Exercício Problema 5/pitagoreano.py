# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
    Nome: João Pedro Apolonio De Sousa Matos
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

# Escreva seu programa a seguir
n= int(input('Digite n: '))
check='?'
lmenorantigo=0
lmaiorantigo=0
hipotenusaantiga=0
for u in range(1, n+1):
    for v in range(1,n+1):
        lado1= u
        lado2= v
        hipotenusa= ((u**2)+(v**2))**(1/2)
        if (u+v+hipotenusa==n):
            lmenor=min(lado1, lado2)
            lmaior=max(lado1, lado2)                     
            if min(lado1,lado2)>lmenorantigo:
                lmenorantigo=lmenor
                lmaiorantigo=lmaior
                hipotenusaantiga=hipotenusa
                check='ss'
if check=='?':
    print(f'{n} não é pitagoreano')
else:
    print(f'{n} é pitagoreano ({lmenorantigo},{lmaiorantigo},{int(hipotenusaantiga)})')