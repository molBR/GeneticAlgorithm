import random
import matplotlib.pyplot as plt
import geneticIndividualProb1
import geneticIndividualProb2	


class GeneticEnviroment():

	def __init__ (self,mutationProb,crossProb,tamFilhos,tamGen,lutadores,indivInfo):
		self.populationList = []
		self.mutationProb = mutationProb #0.2
		self.crossProb = crossProb#1.0
		self.tamFilhos = tamFilhos#500
		self.bestFitInd = None
		self.tamGen = tamGen#10000
		self.lutadores = lutadores
		if indivInfo == 0:
			self.indiv = geneticIndividualProb1
		else:
			self.indiv = geneticIndividualProb2
		self.bestZs = []
		self.graph = self.run()


	def getMutationProb(self):
		return self.mutationProb

	def getCrossProb(self):
		return self.crossProb

	def startPop(self):
		for i in range (0,self.tamFilhos):
			self.populationList.append(self.indiv.GeneticIndividual("",""))
			self.bestFit(self.populationList[i])		



	def acasalamento(self):
		numCasos = self.tamFilhos*2
		for i in range(0,numCasos):
			paiMae = []
			for j in range(0,2):
				listaGene = []
				for k in range(0,self.lutadores):
					auxNum = random.randint(0,len(self.populationList)-1)
					auxGene = self.populationList[auxNum]
					if auxGene not in listaGene:
						listaGene.append(auxGene)
					else:
						k = k - 1
				paiMae.append(self.torneio(listaGene))
			x = random.random()
			if(x<=self.crossProb):
				filhoX = self.indiv.crossingOver(paiMae[0].getgeneticCodeX(),paiMae[1].getgeneticCodeX())
				filhoY = self.indiv.crossingOver(paiMae[0].getgeneticCodeY(),paiMae[1].getgeneticCodeY())
				filho = self.indiv.GeneticIndividual(filhoX,filhoY)
				filho.mutate(self.mutationProb)
				self.bestFit(filho)
				self.populationList.append(filho)

	def torneio(self,listaGene):
		campeao = listaGene[0]
		for i in (0,len(listaGene)-1):
			if listaGene[i].getTrueZ() < campeao.getTrueZ():
				campeao = listaGene[i]
		return campeao

	def bestFit(self,gene1):
		if self.bestFitInd == None:
			self.bestZs.append(gene1.getTrueZ())
			self.bestFitInd = gene1
		else:
			if(gene1.getTrueZ()<self.bestFitInd.getTrueZ()):
				self.bestFitInd = gene1
				self.bestZs.append(gene1.getTrueZ())

	def run(self):
		self.startPop()
		controle = 0
		while(controle<self.tamGen):
			random.seed()
			self.acasalamento()
			controle = controle+1
			if controle % 3 == 0:
				self.populationList = self.populationList[self.tamFilhos:]
			#print "Geracao: " + str(controle)
		print "BEST: "  + str(self.bestFitInd.getgeneticCodeX())
		print "Y:" + str(self.bestFitInd.getTrueY())
		print "X:" + str(self.bestFitInd.getTrueX())
		print "Z:" + str(self.bestFitInd.getTrueZ())
		print len(self.bestZs)
		plt.plot(self.bestZs)
		plt.ylabel('Menores Valores de Z')
		plt.xlabel('Numero de individuos')
		return plt

	