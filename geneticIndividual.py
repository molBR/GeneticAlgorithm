import random
import math
class GeneticIndividual():

	def __init__(self,geneticCode):
		self.geneticCode = []
		self.Cont = 0
		if(geneticCode!=""):
			self.geneticCode = geneticCode
		else:
			for i in range (0,30):
				rand = random.randint(0,1)
				self.geneticCode.append(str(rand))
			self.geneticCode = ''.join(self.geneticCode)
		self.setTrueX()
		self.fitnessFunction()

	def getgeneticCode(self):
		return self.geneticCode
	def getTrueX(self):
		return self.TrueX
	def getTrueY(self):
		return self.TrueY

	def setTrueX(self):
		inteiro = self.geneticCode[:9]
		int1 = self.geneticCode[:5]
		int2 = self.geneticCode[5:]
		int2 = int2[:3]
		int3 = self.geneticCode[8]
		#-------
		valorInt = int(int1,2) + int(int2,2) + int(int3,2)
		if(valorInt>20):
			valorInt = valorInt - 20
		else:
			valorInt = valorInt - 19  
		#------
		dec1 = self.geneticCode[9:]
		dec1 = dec1[:5]
		deca1 = dec1[:3]
		decb1 = dec1[3]
		decc1 = dec1[4]
		valorDec1 = int(deca1,2) + int(decb1,2) + int(decc1,2)       
		#------
		dec2 = self.geneticCode[14:]
		dec2 = dec2[:5]
		deca2 = dec2[:3]
		decb2 = dec2[3]
		decc2 = dec2[4]
		valorDec2 = int(deca2,2) + int(decb2,2) + int(decc2,2)
		#------
		dec3 = self.geneticCode[19:]
		dec3 = dec3[:5]
		deca3 = dec3[:3]
		decb3 = dec3[3]
		decc3 = dec3[4]
		valorDec3 = int(deca3,2) + int(decb3,2) + int(decc3,2)
		#------
		dec4 = self.geneticCode[24:]
		dec4 = dec4[:5]
		deca4 = dec4[:3]
		decb4 = dec4[3]
		decc4 = dec4[4]
		valorDec4 = int(deca3,2) + int(decb3,2) + int(decc3,2)
		self.TrueX = float(str(valorInt) + "." + str(valorDec1) + str(valorDec2) + str(valorDec3) + str(valorDec4))
	
	def fitnessFunction(self):
		self.TrueY = math.sin(self.TrueX) + math.cos(math.sqrt(3)*self.TrueX)



