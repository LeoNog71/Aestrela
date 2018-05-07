from lib import *

#A*

listaAberta = {}
listaFechada = []
exp = []
lista = []




class busca():

    grafo = None
    matriz = None

    def __init__(self,grafo,matriz):
        self.grafo = grafo
        self.matriz = matriz

    def teste(self):
        for i in range(1,len(listaFechada)-1):
            if listaFechada[i] in self.grafo.neighbors(listaFechada[i-1]):
                lista.append(listaFechada[i])
            else:
                pass
        return lista
        
    def buscaA(self):
        self.matriz[0][0].setValor(0)
        listaFechada.append(self.matriz[0][0])
        lista.append(self.matriz[0][0])
        
        
        while True:

            

            exp.append(self.grafo.neighbors(listaFechada[len(listaFechada)-1]))
            if listaFechada in exp[len(exp)-1]:
                for i in exp[len(exp)-1]:
                    if i in listaFechada:
                        del i
            try:
                for i in range(0,len(exp[len(exp)-1])):
                    #print(exp[len(exp)-1][i])
                    exp[len(exp)-1][i].setValor(self.grafo.edge_weight((listaFechada[len(listaFechada)-1],exp[len(exp)-1][i]))+listaFechada[len(listaFechada)-1].getValor())
                    listaAberta[(exp[len(exp)-1][i].getValor()+exp[len(exp)-1][i].getHeuristic())]=exp[len(exp)-1][i]
            except IndexError:
                print("erro no index")
                pass   
            ordenar = sorted(listaAberta)
            t = ordenar[0]
            '''
            if t < (listaFechada[len(listaFechada)-1].getValor() + listaFechada[len(listaFechada)-1].getHeuristic()):
            
                
                del listaFechada[len(listaFechada)-1]
                #listaFechada.append(listaAberta[ordenar[0]])
                #teste(listaFechada[len(listaFechada)-1],t)
                listaFechada.append(listaAberta[ordenar[0]])
                del listaAberta[ordenar[0]]
            else:'''

            if len(listaAberta[ordenar[0]].getHistorico()) != 0:
                listaAberta[ordenar[0]].resetHistorico()
                for x in listaFechada[len(listaFechada)-1].getHistorico():

                    listaAberta[ordenar[0]].setHistorico(x)
                listaAberta[ordenar[0]].setHistorico(listaAberta[ordenar[0]].getId())
            else:
                for x in listaFechada[len(listaFechada)-1].getHistorico():
                    listaAberta[ordenar[0]].setHistorico(x)

                listaAberta[ordenar[0]].setHistorico(listaAberta[ordenar[0]].getId())

            listaFechada.append(listaAberta[ordenar[0]])
            del listaAberta[ordenar[0]]
                

            '''for x in listaFechada:
                print(x.getId(),"->", x.getValor()+x.getHeuristic())'''
            
            
            #input()
            
            
            
            
            
            if listaFechada[len(listaFechada)-1].getId() == "9x9":
                '''for i in range(0,len(listaFechada)):
                    for j in range(0,i):
                        if (listaFechada[i].getValor() + listaFechada[i].getHeuristic()) > (listaFechada[j].getValor() + listaFechada[j].getHeuristic()):
                 
                       listaFechada[i].setId("00") '''
                #return listaFechada[len(listaFechada)-1]
                return listaFechada
                '''assasasassa'''