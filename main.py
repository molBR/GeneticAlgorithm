from geneticEnviroment import *
import time
import random

z1 = None
z2 = None
print "-----------------CASO 1:\n"
for i in range (0,30):

	start_time = time.time()
	prob = random.triangular(0,0.5,0.1)
	cross = random.triangular(0.6,1,0.1)
	filhos = random.randrange(0,100)
	geracoes = random.randrange(0,500)
	lutadores = random.randrange(2,10)
	print("Tentativa: %s" % str(i+1))
	print("Prob: %s\nCross: %s\nFilhos: %s\nGeracoes: %s\nLutadores: %s" % (prob,cross,filhos,geracoes,lutadores))
	a = GeneticEnviroment(prob,cross,filhos,geracoes,lutadores,0)
	print("--- %s segundos ---" % (time.time() - start_time))
	if z1 == None:
		z1 = a.bestFitInd
		graph = a.graph
	elif a.bestFitInd > z1:
		z1 = a.bestFitInd
		graph = a.graph
	print("\n\n")

graph.show()

print "----------------CASO 2:"
for i in range (0,30):
	start_time = time.time()
	prob = random.triangular(0,0.5,0.1)
	cross = random.triangular(0.6,1,0.1)
	filhos = random.randrange(5,100)
	geracoes = random.randrange(0,500)
	lutadores = random.randrange(2,10)
	print("Tentativa: %s" % str(i+1))
	print("Prob: %s\nCross: %s\nFilhos: %s\nGeracoes: %s\nLutadores: %s" % (prob,cross,filhos,geracoes,lutadores))
	b = GeneticEnviroment(prob,cross,filhos,geracoes,lutadores,1)
	print("--- %s segundos ---" % (time.time() - start_time))
	if z1 == None:
		z1 = b.bestFitInd
		graph = a.graph
	elif b.bestFitInd > z1:
		z1 = b.bestFitInd
		graph = b.graph
	print("\n\n")
graph.show()
	







