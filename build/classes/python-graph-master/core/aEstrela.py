from lib import *

#A*

listaAberta = {}
listaFechada = []
exp = []


        
class busca():

    grafo = None
    matriz = None

    def __init__(self,grafo,matriz):
        self.grafo = grafo
        self.matriz = matriz

    
        
    def buscaA(self):
        self.matriz[0][0].setValor(0)
        listaFechada.append(self.matriz[0][0])
        
        
        while True:

            

            exp.append(self.grafo.neighbors(listaFechada[len(listaFechada)-1]))
            
            for i in exp[len(exp)-1]:

                i.setValor(self.grafo.edge_weight((listaFechada[len(listaFechada)-1],i))+listaFechada[len(listaFechada)-1].getValor())
                listaAberta[(i.getValor()+i.getHeuristic())]=i
           
            ordenar = sorted(listaAberta)


            if ordenar[0] < listaFechada[len(listaFechada)-1].getValor():
                del listaFechada[len(listaFechada)-1]
                listaFechada.append(listaAberta[ordenar[0]])
            else:
                listaFechada.append(listaAberta[ordenar[0]])

            
            del listaAberta[ordenar[0]]
            
            if listaFechada[len(listaFechada)-1].getId() == "9x9":
                for i in range(0,len(listaFechada)):
                    for j in range(0,i):
                        if (listaFechada[i].getValor() + listaFechada[i].getHeuristic()) > (listaFechada[j].getValor()+listaFechada[j].getHeuristic()):
                            listaFechada[i] = "00"
                return listaFechada
            '''assasasassa'''
