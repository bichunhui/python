class Render(object):
	def __init__(self,fieldList,dataList):
		self.fieldList = fieldList
		self.dataList = dataList
		self.flag = None
	def box(self):
			print("# "*self.generalLength)
			for i in range(self.generalHeight):
				print("#",end="")
				print(" "*(2*(self.generalLength-2)+1),end="")
				print("#")
			print("# "*self.generalLength)

	def addBox(self):
		if self.flag == None:
			self.dataList.insert(0,self.fieldList)
			self.flag == True
		print("# "*self.generalLength)
		line = 0
		for i in range(self.generalHeight):
			print("#",end="")
			if i%2 == 0:
				print(" "*(2*(self.generalLength-2)+1),end="")
			else:
				dataLen = 0
				for data in self.dataList[line]:
					print("  ",data,end="")
					dataLen = dataLen + len(data) + 3
				line += 1
				lenn = 2*self.generalLength-dataLen-3
				print(" "*lenn,end="")

			# print(" "*(2*(self.generalLength-2)+1),end="")
			
			print("#")
		print("# "*self.generalLength)

	def dealList(self):
		fieldSum = len(self.fieldList)
		self.dataList.append(self.fieldList)

		dataSum = len(self.dataList)
		maxLength = 0
		maxList = []
		for num in range(fieldSum):
			for data in self.dataList:
				if len(data[num]) > maxLength:
					maxLength = len(data[num])
			maxList.append(maxLength)

		allMaxDataLen = 0
		for length in maxList:
			allMaxDataLen += length
		self.generalLength = allMaxDataLen + fieldSum + 1
		self.generalHeight = dataSum*2 + 1

