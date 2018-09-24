from kuang import Render


class Table(object):
	def __init__(self,tableName):
		self.tableName = tableName
		self.table = []
		self.fieldName = ["id"]

	def settingFields(self):
		print("请输入字段名，字段名间用逗号分隔开!")
		fieldList = input().split(",")
		for field in fieldList:
			self.fieldName.append(field)

	def insert(self):
		flist = []
		for field in self.fieldName:
			print(field,":",end=" ")
			value = input()
			flist.append(value)
		self.table.append(flist)
	def show(self):
		for one in self.table:
			for num in range(len(self.fieldName)):
				print(self.fieldName[num],": ",one[num])
			print("\n"*2)
		render = Render(self.fieldName,self.table)
		render.dealList()
		render.addBox()

	def update(self,ctb):
		print("请输入学号ID:",end=" ")
		id = input()
		noOne = True
		for man in ctb.table:
			if man[0] == id:
				manIndex = ctb.table.index(man)
				del ctb.table[manIndex]
				self.insert()
				noOne = False
				break
		if noOne:
			print("没有这个学号的人！")

	def delete(self,ctb):
		print("请输入学号ID:",end=" ")
		id = input()
		noOne = True
		for man in ctb.table:
			if man[0] == id:
				manIndex = ctb.table.index(man)
				del ctb.table[manIndex]
				noOne = False
				print("删除成功！")
				break
		if noOne:
			print("没有这个学号的人！")


class Db(object):
	def __init__(self,dbName):
		self.dbName = dbName
		self.db = []

	def useTable(self,tableName):
		tempTable = None
		dbLength = len(self.db)
		for table in self.db:
			if table.tableName == tableName:
				tempTable = table
				break
		if table == self.db[dbLength-1]:
			if table.tableName == tableName:
				tempTable = table
			else:
				tempTable = None
				print("无此table")

		while tempTable:
			print("功能0 :settingFields   功能1 :insert   功能2 :show   功能3 :update   功能4 :delete   功能5 :exit")
			function = int(input("请输入功能号码:"))
			if function == 0:
				tempTable.settingFields()
			elif function == 1:
				tempTable.insert()
			elif function == 2:
				tempTable.show()
			elif function == 3:
				tempTable.update(table)
			elif function == 4:
				tempTable.delete(table)
			elif function == 5:
				break


	def createTable(self,tableName):
		self.table = Table(tableName)
		self.db.append(self.table)

	def showTables(self):
		print("tableNames:",end=" ")
		for table in self.db:
			print(table.tableName,end=" ")

	def deleteTable(self,tableName):
		for table in self.db:
			if table.tableName == tableName:
				index = self.db.index(table)
				del self.db[index]
			else:
				continue

print("place use \"class Db(dbName)\" create database")
print("place use \"Db object.createTable(tableName)\" create table")
print("place use \"Db object.showTables()\" show tables")
print("place use \"Db object.deleteTable(tableName)\" delete table")
print("place use \"Db object.useTable(tableName)\" completed create,update,select,delete function")
