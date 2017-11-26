import random
import math
class GeneticIndividual():

	def __init__(self,geneticCodeX,geneticCodeY):
		self.geneticCodeX = []
		self.geneticCodeY = []
		self.Cont = 0

		if(geneticCodeX!=""):
			self.geneticCodeX = geneticCodeX
		else:
			for i in range (0,15):
				rand = random.randint(0,1)
				self.geneticCodeX.append(str(rand))
			self.geneticCodeX = ''.join(self.geneticCodeX)
		if(geneticCodeY!=""):
			self.geneticCodeY = geneticCodeY
		else:
			for i in range (0,15):
				rand = random.randint(0,1)
				self.geneticCodeY.append(str(rand))
			self.geneticCodeY = ''.join(self.geneticCodeY)
		self.setTrueX()
		self.setTrueY()
		self.fitnessFunction()

	def getgeneticCodeX(self):
		return self.geneticCodeX

	def getgeneticCodeY(self):
		return self.geneticCodeY

	def getTrueX(self):
		return self.TrueX

	def getTrueY(self):
		return self.TrueY

	def getTrueZ(self):
		return self.TrueZ

	def setTrueX(self):
		inteiro = self.geneticCodeX[:5]
		dec1 = self.geneticCodeX[5:]
		dec2 = dec1[5:]
		dec1 = dec1[:5]

		i1 = inteiro[3]
		i2 = inteiro[4]
		inteiro = inteiro[:3]

		dec11 = dec1[3]
		dec12 = dec1[4]
		dec1 = dec1[:3]

		dec21 = dec2[3]
		dec22 = dec2[4]
		dec2 = dec2[:3]

		self.TrueX = "%s.%s%s" % ((int(inteiro,2)+
			int(i1,2) + int(i2,2))+6,(int(dec1,2)+int(dec11,2)+int(dec12,2)),
			(int(dec2,2)+int(dec21,2)+int(dec22,2)))
		self.TrueX = float(self.TrueX)
		#print self.TrueX 

	def setTrueY(self):
		inteiro = self.geneticCodeY[:5]
		dec1 = self.geneticCodeY[5:]
		dec2 = dec1[5:]
		dec1 = dec1[:5]

		i1 = inteiro[3]
		i2 = inteiro[4]
		inteiro = inteiro[:3]

		dec11 = dec1[3]
		dec12 = dec1[4]
		dec1 = dec1[:3]

		dec21 = dec2[3]
		dec22 = dec2[4]
		dec2 = dec2[:3]

		self.TrueY = "%s.%s%s" % ((int(inteiro,2)+
			int(i1,2) + int(i2,2))+6,(int(dec1,2)+int(dec11,2)+int(dec12,2)),
			(int(dec2,2)+int(dec21,2)+int(dec22,2)))
		self.TrueY = float(self.TrueY)

	def mutate(self,mutateProb):
		for i in range (0,len(self.geneticCodeX)-1):
			x = random.random()
			if (x <= mutateProb):
				if(self.geneticCodeX[i]=='1'):
					list1 = list(self.geneticCodeX)
					list1[i] = '0'
					self.geneticCodeX= ''.join(list1)
				else:
					list1 = list(self.geneticCodeX)
					list1[i] = '1'
					self.geneticCodeX= ''.join(list1)

	def fitnessFunction(self):
		self.TrueZ = (self.TrueX * self.TrueY * 
			math.sin(self.TrueX) * math.sin(self.TrueY))
		#print self.TrueZ

def crossingOver(pai,mae):
	
		filho = []
		#---------------------- INTEIRO
		index1 = random.randint(1,4)
		index2 = 5 - index1

		intMae = mae[:5]
		intPai = pai[:5]
		intMae = intMae[index1:]
		intPai = intPai[:index1]
		#----------------------- DECIMAL1
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae1 = mae[5:]
		decMae1 = decMae1[:5]
		decPai1 = pai[5:]
		decPai1 = decPai1[:5]
		decMae1 = decMae1[index1:]
		decPai1 = decPai1[:index1]
		#-----------------------DECIMAL2
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae2 = mae[10:]
		decMae2 = decMae2[:5]
		decPai2 = pai[10:]
		decPai2 = decPai2[:5]
		decMae2 = decMae2[index1:]
		decPai2 = decPai2[:index1]
		#-----------------------DECIMAL3
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae3 = mae[15:]
		decMae3 = decMae3[:5]
		decPai3 = pai[15:]
		decPai3 = decPai3[:5]
		decMae3 = decMae3[index1:]
		decPai3 = decPai3[:index1]
		#-----------------------DECIMAL4
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae4 = mae[20:]
		decMae4 = decMae4[:5]
		decPai4 = pai[20:]
		decPai4 = decPai4[:5]
		decMae4 = decMae4[index1:]
		decPai4 = decPai4[:index1]
		#-----------------------FILHO
		filho = (intPai + intMae + decPai1 + decMae1 + decPai2 + 
			decMae2 + decPai3 + decMae3 + decPai4 + decMae4)
		return filho


