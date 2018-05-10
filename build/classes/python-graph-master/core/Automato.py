from pygraph.classes.digraph import *
from lib import *
from estrela import *
CUSTO = 5

estados = []

matriz = matrizNodes(matrizNumerica().getMatriz()).gerador()

for i in matriz:
    for j in i:
        estados.append(j)
   
grafo = digraph()
grafo.add_nodes(estados)

for i in range(0,10):
    try:
        for j in range(0,10):
            if matriz[i][j+1].getCusto() != 1000:
                grafo.add_edge((matriz[i][j],matriz[i][j+1]),wt=matriz[i][j+1].getCusto())
            if matriz[i+1][j].getCusto() != 1000:
                grafo.add_edge((matriz[i][j],matriz[i+1][j]),wt=matriz[i+1][j].getCusto())
            #if matriz[i-1][j].getCusto() != 1000:
            #    grafo.add_edge((matriz[i][j],matriz[i-1][j]),wt=matriz[i+1][j].getCusto())
            
                   
    except IndexError:
        pass



arq = open("/home/nogueira/Documentos/LFA/FSI-Aestrela/build/classes/python-graph-master/core/destino.txt","r")
objetivo = arq.readline()
arq.close()

lista = busca(grafo,matriz,objetivo).buscaA()


#arq = open("C:\\Users\\rafae\\Desktop\\LFA-tentativa666\\build\\classes\\python-graph-master\\core\\matrizNUm.txt","w")
arq = open("/home/nogueira/Documentos/LFA/FSI-Aestrela/build/classes/python-graph-master/core/matrizNUm.txt","w")
for i in matriz:
    for j in i:
        arq.writelines(str(j.getCusto())+" ")
    
arq.close()
#arq = open("C:\\Users\\rafae\\Desktop\\LFA-tentativa666\\build\\classes\\python-graph-master\\core\\caminhoBusca.txt","w")
arq = open("/home/nogueira/Documentos/LFA/FSI-Aestrela/build/classes/python-graph-master/core/caminhoBusca.txt","w")
for i in lista:
    if(i != None):
        arq.writelines(str(i) +" ")
arq.close()
