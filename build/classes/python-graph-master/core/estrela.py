from lib import *

#A*

listaAberta = {}
listaFechada = []
exp = []
caminho = []




class busca():
    
    grafo = None
    matriz = None
    objetivo = None

    def __init__(self,grafo,matriz,objetivo):
        self.grafo = grafo
        self.matriz = matriz
        self.objetivo = objetivo


        
    def buscaA(self):
        self.matriz[0][0].setValor(0)
        self.matriz[0][0].setNode(self.matriz[0][0])
        listaFechada.append(self.matriz[0][0])
            
        


        while True:
       
            exp.append(self.grafo.neighbors(listaFechada[len(listaFechada)-1]))
            
            if listaFechada in exp[len(exp)-1]:
                for i in exp[len(exp)-1]:
                    if i in listaFechada:
                        del i
            try:

                for i in range(0,len(exp[len(exp)-1])):
                    exp[len(exp)-1][i].setValor(self.grafo.edge_weight((listaFechada[len(listaFechada)-1],exp[len(exp)-1][i]))+listaFechada[len(listaFechada)-1].getValor())
                    exp[len(exp)-1][i].setNode(listaFechada[len(listaFechada)-1])
                    listaAberta[(exp[len(exp)-1][i].getValor()+exp[len(exp)-1][i].getHeuristic())] = exp[len(exp)-1][i]

            except IndexError:
                print("erro no index")
                pass   
            
            ordenar = sorted(listaAberta)
            
            
            listaFechada.append(listaAberta[ordenar[0]])
            del listaAberta[ordenar[0]]
                

    
            
            if listaFechada[len(listaFechada)-1].getId() == self.objetivo:
                i = listaFechada[len(listaFechada)-1]

                while i.getId() != "0x0":
                    caminho.append(i.getId())
                    i = i.getNode()
                return caminho
