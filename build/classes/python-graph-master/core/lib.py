import random


class node():

    h = 0
    custo = None
    id = None
    historico = None
    valor = 0
    node = None
    
    def __init__(self,h,custo,id):
        self.h = h
        self.custo = custo
        self.id = id

    def setNode(self, node):
        self.node = node

    def getNode(self):
        return self.node

    def getHeuristic(self):
        return self.h

    def getValor(self):
        return self.valor

    def setValor(self,valor):
        self.valor = self.valor + valor

    def getCusto(self):
        return self.custo

    def getId(self):
        return self.id

    def setId(self,id):
         self.id = id
    
    def getHistorico(self):
        return self.historico
        
    def setHistorico(self,posicao):
        self.historico = posicao
  

class matrizNumerica():
    
    def getMatriz(self):

        matriz = []
        custos = [1,10,1000,4,20,1,1000,4,20]

        for i in range(0,10):
            matriz.append([])
            for j in range(0,10):
                matriz[i].append(custos[random.randrange(0,9,1)])
        return matriz
    

class matrizNodes():
    
    matriz = None

        
    def __init__(self,matriz):
        self.matriz = matriz
        
    def gerador(self):
        for i in range(0,10):
            for j in range(0,10):
                self.matriz[i][j] = node(((9-i)+(9-j)) ,self.matriz[i][j],(str(i)+"x"+str(j)))
                
        return self.matriz








                
