import random
from geneticIndividual import *

class GeneticEnviroment():

	def __init__ (self):
		self.populationList = []
		self.mutationProb = 0.2
		self.crossProb = 1.0
		self.tamPopMax = 10000
		self.tamFilhos = 500
		self.bestFitInd = None
		self.tamGen = 10000
		self.run()

	def getMutationProb(self):
		return self.mutationProb

	def startPop(self):
		eva = []
		adao = []
		for i in range(0,30):
			eva.append(str(0))
			adao.append(str(1))
		#self.populationList.append(GeneticIndividual(adao))		
		for i in range (0,100):
			self.populationList.append(GeneticIndividual(""))
			self.bestFit(self.populationList[i])
			print self.populationList[i].getTrueY()
		#self.populationList.append(GeneticIndividual(eva))
		#for i in range (0,100):
		#	print self.populationList[i].getgeneticCode()

		self.crossingOver(self.populationList[0].getgeneticCode(),self.populationList[99].getgeneticCode())
		print "BEST: "  + str(self.bestFitInd.getgeneticCode())


	def acasalamento(self):
		for i in range(self.tamFilhos):
			indPai = random.randint(0,len(self.populationList)-1)
			indMae = random.randint(0,len(self.populationList)-1)
			if indPai == indMae:
				i = i-1
			else:
				filho = GeneticIndividual(self.crossingOver(self.populationList[indPai].getgeneticCode(),self.populationList[indMae].getgeneticCode()))
				self.bestFit(filho)
				self.populationList.append(filho)

	def bestFit(self,gene1):
		if self.bestFitInd == None:
			self.bestFitInd = gene1
		else:
			if(gene1.getTrueY()>self.bestFitInd.getTrueY()):
				self.bestFitInd = gene1

	def run(self):
		self.startPop()
		controle = 0
		while(controle<self.tamGen):
			self.acasalamento()
			controle = controle+1
			print "Geracao: " + str(controle)
		print "BEST: "  + str(self.bestFitInd.getgeneticCode())
		print "Y:" + str(self.bestFitInd.getTrueY())
		print "X:" + str(self.bestFitInd.getTrueX())


			

	def crossingOver(self,pai,mae):
		filho = []
		#---------------------- INTEIRO
		index1 = random.randint(1,8)
		index2 = 9 - index1

		intMae = mae[:9]
		intPai = pai[:9]
		intMae = intMae[index1:]
		intPai = intPai[:index1]
		#----------------------- DECIMAL1
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae1 = mae[9:]
		decMae1 = decMae1[:5]
		decPai1 = pai[9:]
		decPai1 = decPai1[:5]
		decMae1 = decMae1[index1:]
		decPai1 = decPai1[:index1]
		#-----------------------DECIMAL2
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae2 = mae[14:]
		decMae2 = decMae2[:5]
		decPai2 = pai[14:]
		decPai2 = decPai2[:5]
		decMae2 = decMae2[index1:]
		decPai2 = decPai2[:index1]
		#-----------------------DECIMAL3
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae3 = mae[19:]
		decMae3 = decMae3[:5]
		decPai3 = pai[19:]
		decPai3 = decPai3[:5]
		decMae3 = decMae3[index1:]
		decPai3 = decPai3[:index1]
		#-----------------------DECIMAL4
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae4 = mae[24:]
		decMae4 = decMae4[:5]
		decPai4 = pai[24:]
		decPai4 = decPai4[:5]
		decMae4 = decMae4[index1:]
		decPai4 = decPai4[:index1]
		#-----------------------FILHO
		filho = (intPai + intMae + decPai1 + decMae1 + decPai2 + 
			decMae2 + decPai3 + decMae3 + decPai4 + decMae4)
		return filho



