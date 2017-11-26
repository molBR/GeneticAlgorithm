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
			for i in range (0,20):
				rand = random.randint(0,1)
				self.geneticCodeX.append(str(rand))
			self.geneticCodeX = ''.join(self.geneticCodeX)
		if(geneticCodeY!=""):
			self.geneticCodeY = geneticCodeY
		else:
			for i in range (0,20):
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

		dec1 = self.geneticCodeX[:5]
		dec2 = self.geneticCodeX[5:]
		dec3 = dec2[5:]
		dec4 = dec3[5:]
		dec2 = dec2[:5]
		dec3 = dec3[:5]
		
		dec11 = dec1[3]
		dec12 = dec1[4]
		dec1 = dec1[:3]

		dec21 = dec2[3]
		dec22 = dec2[4]
		dec2 = dec2[:3]

		dec31 = dec3[3]
		dec32 = dec3[4]
		dec3 = dec3[:3]

		dec41 = dec4[3]
		dec42 = dec4[4]
		dec4 = dec4[:3]

		TrueX1 = "0.%s%s" % ((int(dec1,2)+int(dec11,2)+int(dec12,2)),
			(int(dec2,2)+int(dec21,2)+int(dec22,2)))

		TrueX2 = "0.%s%s" % ((int(dec3,2)+int(dec31,2)+int(dec32,2)),
			(int(dec3,2)+int(dec31,2)+int(dec32,2)))
		self.TrueX = float(TrueX1) + float(TrueX2) - 0.99
		#print self.TrueX 

	def setTrueY(self):
		dec1 = self.geneticCodeY[:5]
		dec2 = self.geneticCodeY[5:]
		dec3 = dec2[5:]
		dec4 = dec3[5:]
		dec2 = dec2[:5]
		dec3 = dec3[:5]
		
		dec11 = dec1[3]
		dec12 = dec1[4]
		dec1 = dec1[:3]

		dec21 = dec2[3]
		dec22 = dec2[4]
		dec2 = dec2[:3]

		dec31 = dec3[3]
		dec32 = dec3[4]
		dec3 = dec3[:3]

		dec41 = dec4[3]
		dec42 = dec4[4]
		dec4 = dec4[:3]

		TrueY1 = "0.%s%s" % ((int(dec1,2)+int(dec11,2)+int(dec12,2)),
			(int(dec2,2)+int(dec21,2)+int(dec22,2)))

		TrueY2 = "0.%s%s" % ((int(dec3,2)+int(dec31,2)+int(dec32,2)),
			(int(dec3,2)+int(dec31,2)+int(dec32,2)))
		self.TrueY = float(TrueY1) + float(TrueY2) - 0.99

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
		self.TrueZ = (math.pow(self.TrueX,2) + math.pow(self.TrueY,2) 
			- math.cos(18*self.TrueX) - math.cos(18*self.TrueY))
		if self.TrueZ == None:
			print "oi" 
		#print self.TrueZ

def crossingOver(pai,mae):
	
		filho = []
		'''---------------------- INTEIRO
		index1 = random.randint(1,4)
		index2 = 5 - index1

		intMae = mae[:5]
		intPai = pai[:5]
		intMae = intMae[index1:]
		intPai = intPai[:index1]'''
		#----------------------- DECIMAL1
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae1 = mae[:5]
		decPai1 = pai[:5]
		decMae1 = decMae1[index1:]
		decPai1 = decPai1[:index1]
		#-----------------------DECIMAL2
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae2 = mae[5:]
		decMae2 = decMae2[:5]
		decPai2 = pai[5:]
		decPai2 = decPai2[:5]
		decMae2 = decMae2[index1:]
		decPai2 = decPai2[:index1]
		#-----------------------DECIMAL3
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae3 = mae[10:]
		decMae3 = decMae3[:5]
		decPai3 = pai[10:]
		decPai3 = decPai3[:5]
		decMae3 = decMae3[index1:]
		decPai3 = decPai3[:index1]
		#-----------------------DECIMAL4
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae4 = mae[15:]
		decMae4 = decMae4[:5]
		decPai4 = pai[15:]
		decPai4 = decPai4[:5]
		decMae4 = decMae4[index1:]
		decPai4 = decPai4[:index1]
		#----------------------- DECIMAL5
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae5 = mae[20:]
		decMae5 = decMae5[:5]
		decPai5 = pai[20:]
		decPai5 = decPai5[:5]
		decMae5 = decMae5[index1:]
		decPai5 = decPai5[:index1]
		#-----------------------DECIMAL6
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae6 = mae[25:]
		decMae6 = decMae6[:5]
		decPai6 = pai[25:]
		decPai6 = decPai6[:5]
		decMae6 = decMae6[index1:]
		decPai6 = decPai6[:index1]
		#-----------------------DECIMAL7
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae7 = mae[30:]
		decMae7 = decMae7[:5]
		decPai7 = pai[30:]
		decPai7 = decPai7[:5]
		decMae7 = decMae7[index1:]
		decPai7 = decPai7[:index1]
		#-----------------------DECIMAL8
		index1 = random.randint(1,4)
		index2 = 5 - index1

		decMae8 = mae[35:]
		decMae8 = decMae8[:5]
		decPai8 = pai[35:]
		decPai8 = decPai8[:5]
		decMae8 = decMae8[index1:]
		decPai8 = decPai8[:index1]
		#-----------------------FILHO
		filho = (decPai1 + decMae1 + decPai2 + 
			decMae2 + decPai3 + decMae3 + decPai4 + decMae4)
		return filho


