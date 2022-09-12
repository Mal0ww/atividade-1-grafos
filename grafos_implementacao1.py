'''
UNIVERSIDADE FEDERAL DE SERGIPE
CENTRO DE CIENCIAS EXATAS E TECNOLOGIAS
DEPARTAMENTO DE COMPUTACAO
ALUNO: MICHAEL HITLER BATISTA DO NASCIMENTO
GRAFOS E ALGORITMOS COMPUTACIONAIS

-------------------------------------------------------
Implementacao da grafos, primeira atividade.

code by: Michael Hitler.

'''
#classe de grafos
import copy
class Grafos:
    def __init__(self, numDeVertices=0): #inicializando os vertices por construtor
        self.vertices = numDeVertices
        self.grafos =  [[] for arestas  in range(self.vertices)]#lista de adjacencias.
    
    #funcao para adicionar vertices
    def AdicionarVertices(self, numVertices):
        self.vertices += numVertices
        self.grafos += [[] for arestas  in range(numVertices)]
    
    def RemoverVertice(self, numVertices):
        self.grafos.remove(numVertices)
        for i in range(len(self.vertices)):
            self.grafos[i].remove(numVertices)

    def NumVertices(self):
        print(f"Numero de vertices: {len(self.grafos)}")
        #return len(self.grafos)

    def AdicionarAresta1(self, vertice1, vertice2): #adicao para um grafo direcional (Digrafos)
        self.grafos[vertice2].append(vertice1)

    def AdicionarAresta2(self, vertice1, vertice2): #adicao para um grafo nao direcional
        self.grafos[vertice2].append(vertice1)
        self.grafos[vertice1].append(vertice2)

    def RemoverAresta1(self, vertice1, vertice2): #remocao para um grafo nao direcional
        self.grafos[vertice2].remove(vertice1)

    def RemoverAresta2(self, vertice1, vertice2): #remocao para um grafo direcional
        self.grafos[vertice2].remove(vertice1)
        self.grafos[vertice1].remove(vertice2)

    
    def Adjacencias(self, vertice1, vertice2): #verifica se dois vertices sao vizinhos
        if vertice2 in self.grafos[vertice1]:
            return True
        else:
            return False
    
    def TodasAdjacencias(self, vertice): #mostrar todas as adjacencias
        print(f"Adjacencias de {vertice}: ", end = " ")
        for adjacencias in self.grafos[vertice]:
            print(f"{adjacencias} ---> ", end=" ")
    
    def GrauDoVertice(self, i):
        print(f"O vertice {i} tem grau {len(self.grafos[i])}")
        #return len(self.grafos[i-1]) #ou retoronando o tamanho do grau
 
    def Euleriano(self):
        contador = 0
        for i in range(self.vertices):
            grau = 0
            for j in range(self.vertices):
                if i == j:
                    grau = grau + 2 * len(self.grafos[i])
                else:
                    grau += len(self.grafos[i])
            if grau % 2 != 0:
                contador += 1
        if contador == 0:
            print("Grafo com ciclo euleriano")
            return True
        elif contador == 2:
            print("Grafo com ciclo semieuleriano")
            return False
        else:
            print("Grafo nao euleriano e nem semieulariano")
            return False

    def Hierholzer(self):
        caminho = [0]
        circuitoFinal = []
        aux = copy.deepcopy(self.grafos) 

        while (caminho):
            i = caminho[-1]
            if aux[i]:
                proxVert = aux[i].pop()
                caminho.append(proxVert)
            else:
                circuitoFinal.append(caminho.pop())
        print(circuitoFinal)

    def MostrarGrafos(self):
        for i in range(self.vertices):
            print(f"Vertice {i}: --->", end=" ")
            for k in self.grafos[i]:
                print(f"{k} --->", end=" ")
            print("")


if __name__ == '__main__':
    #grafo de teste basicos
    print("Grafo de Teste")
    grafoTeste = Grafos(7)
    grafoTeste.AdicionarAresta2(0,1)
    grafoTeste.AdicionarAresta2(0,6)
    grafoTeste.AdicionarAresta2(1,2)
    grafoTeste.AdicionarAresta2(2,0)
    grafoTeste.AdicionarAresta2(2,3)
    grafoTeste.AdicionarAresta2(3,4)
    grafoTeste.AdicionarAresta2(4,2)
    grafoTeste.AdicionarAresta2(4,5)
    grafoTeste.AdicionarAresta2(5,0)
    grafoTeste.AdicionarAresta2(6,4)
    grafoTeste.NumVertices()
    grafoTeste.Adjacencias(1,2)
    grafoTeste.GrauDoVertice(1)
    grafoTeste.MostrarGrafos()
    #grafoTeste.AdicionarVertices(2)
    print("\n")
    grafoTeste.MostrarGrafos()
    print("Grafo Euleriano: "+str(grafoTeste.Euleriano()))
    grafoTeste.Hierholzer()
    print("\n---------------------------------------------------------")
'''#-----------------------------------------------------------------------
    #primeiro grafo
    print("Grafo 1: ")
    grafo1 = Grafos(10)
    grafo1.AdicionarAresta(0,1)
    grafo1.AdicionarAresta(0,9)
    grafo1.AdicionarAresta(1,2)
    grafo1.AdicionarAresta(1,6)
    grafo1.AdicionarAresta(1,9)
    grafo1.AdicionarAresta(2,3)
    grafo1.AdicionarAresta(2,4)
    grafo1.AdicionarAresta(2,5)
    grafo1.AdicionarAresta(3,4)
    grafo1.AdicionarAresta(5,6)
    grafo1.AdicionarAresta(6,7)
    grafo1.AdicionarAresta(6,9)
    grafo1.AdicionarAresta(7,8)
    grafo1.AdicionarAresta(8,9)
    grafo1.MostrarGrafos()
    print("Grafo Euleriano: " + str(grafo1.Euleriano()))
    grafo1.Hierholzer()
    print("\n---------------------------------------------------------")
#-----------------------------------------------------------------------
    #segundo grafo
    print("Grafo: 2")
    grafo2 = Grafos(8)
    grafo2.AdicionarAresta(0,2)
    grafo2.AdicionarAresta(0,3)
    grafo2.AdicionarAresta(0,6)
    grafo2.AdicionarAresta(0,7)
    grafo2.AdicionarAresta(1,2)
    grafo2.AdicionarAresta(1,3)
    grafo2.AdicionarAresta(1,6)
    grafo2.AdicionarAresta(1,7)
    grafo2.AdicionarAresta(2,4)
    grafo2.AdicionarAresta(2,5)
    grafo2.AdicionarAresta(3,4)
    grafo2.AdicionarAresta(3,5)
    grafo2.AdicionarAresta(4,6)
    grafo2.AdicionarAresta(4,7)
    grafo2.AdicionarAresta(5,6)
    grafo2.AdicionarAresta(5,7)
    grafo2.MostrarGrafos()
    print("Grafo Euleriano: " + str(grafo2.Euleriano()))
    grafo2.Hierholzer()
    print("\n---------------------------------------------------------")
#-----------------------------------------------------------------------
    #terceiro grafo
    print("Grafo: 3")
    grafo3 = Grafos(9)
    grafo3.AdicionarAresta(0,1)
    grafo3.AdicionarAresta(0,2)
    grafo3.AdicionarAresta(0,6)
    grafo3.AdicionarAresta(0,7)
    grafo3.AdicionarAresta(1,2)
    grafo3.AdicionarAresta(0,1)
    grafo3.AdicionarAresta(2,3)
    grafo3.AdicionarAresta(2,6)
    grafo3.AdicionarAresta(3,6)
    grafo3.AdicionarAresta(3,4)
    grafo3.AdicionarAresta(3,8)
    grafo3.AdicionarAresta(4,8)
    grafo3.AdicionarAresta(5,6)
    grafo3.AdicionarAresta(5,8)
    grafo3.AdicionarAresta(6,7)
    grafo3.AdicionarAresta(6,8)
    grafo3.MostrarGrafos()
    print("Grafo Euleriano: " + str(grafo3.Euleriano()))
    grafo3.Hierholzer()'''
 


    
    
    
    
    
    
    
    