from random import *
import math
import re

TAM = 20
N = 250000
T0 = 50000
TN = 17

def gerarRandomList(x):
    lista = []
    for i in range(x):
        lista.append(randrange(2))
    return lista

def ler():
    lista = []
    F = open("uf20_01.cnf","r")
    for linha in F:
        l = re.search("(\-?[0-9]+)\s+(\-?[0-9]+)\s+(\-?[0-9]+) 0", linha)
        if l != None:
            lista.append((int(l.group(1)), int(l.group(2)), int(l.group(3))))
    return lista

def avaliarAleatorio(inicial,listaCNF):
    contGeral = 0
    for cada in listaCNF:
        cont = 0
        for x in cada:
            if(x<0 and not inicial[abs(x) - 1]):
                cont += 1
            elif (x>0 and inicial[abs(x) - 1]):
                cont += 1

        if (cont == 3):
            contGeral += 1

    return contGeral

def temperatura(i):
    return T0*(TN/T0)**(i/N)

def vizinho(lista):
    x = randrange(len(lista))
    novaL = []
    for i in range(len(lista)):
        novaL.append(lista[i])
    if(lista[x]):
        novaL[x] = 0
    else:
        novaL[x] = 1
    return novaL

def simuAnne(s0,listaCNF):
    candidato = s0
    t = T0
    cont = 1
    while(True):
        proximo = vizinho(candidato)
        deltaE = avaliarAleatorio(proximo,listaCNF) - avaliarAleatorio(candidato,listaCNF)
        if(deltaE >= 0):
            candidato = proximo
        elif randrange(0,99) < math.e ** (-deltaE/t):
            candidato = proximo
        t = temperatura(cont)
        cont += 1
        if(t < TN or cont == N):
            return candidato

inicial = gerarRandomList(TAM)
print inicial
print
listaCNF = ler()
print avaliarAleatorio(inicial,listaCNF)
sa = simuAnne(inicial,listaCNF)
print sa
print avaliarAleatorio(sa,listaCNF)
