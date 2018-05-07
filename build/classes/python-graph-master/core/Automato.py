from pygraph.classes.digraph import *
from lib import *
#from aEstrela import *
from estrela import *
CUSTO = 5

estados = []

matriz = matrizNodes(matrizNumerica().getMatriz()).gerador()

for i in matriz:
    for j in i:
        estados.append(j)
        #print(j.getCusto(), end=" ")
    #print("")
        
grafo = digraph()
grafo.add_nodes(estados)

for i in range(0,10):
    try:
        for j in range(0,10):
            grafo.add_edge((matriz[i][j],matriz[i][j+1]),wt=matriz[i][j+1].getCusto())
    except IndexError:
        pass

for i in range(0,10):
    try:
        for j in range(0,10):
            grafo.add_edge((matriz[i][j],matriz[i+1][j]),wt=matriz[i+1][j].getCusto())
    except IndexError:
        pass

for i in matriz:
    for j in i:
        print(j.getCusto(),"->",j.getHeuristic(), end=" |")
    print("")

print("=======================================================================")
print("=======================================================================")
print("=======================================================================")

'''
a = grafo.neighbors(matriz[0][0])
f = grafo.edge_weight((matriz[0][0],a[1]))
print(f)
'''
lista = busca(grafo,matriz).buscaA()
arq = open("/home/nogueira/Documentos/LFA/LFA-tentativa666/build/classes/python-graph-master/core/matrizNUm.txt","w")
for i in matriz:
    for j in i:
        arq.writelines(str(j.getCusto())+" ")
    
arq.close()
arq = open("/home/nogueira/Documentos/LFA/LFA-tentativa666/build/classes/python-graph-master/core/caminhoBusca.txt","w")
for i in lista:
    arq.writelines(i.getId()+" ")
    #print(i.getId())
arq.close()


