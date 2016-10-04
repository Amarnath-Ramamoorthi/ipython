import random, string
import pandas as pd

class Formatting():
	def __init__ (self, structure, nrows, file_name = "/home/amar/Documents/DummyData.csv"):
		self.formatt = structure
		self.nrows = nrows
		self.file_name = file_name
		self.strDataTypes = [str, "word"]
		self.passageDataTypes = ["sentence", "paragraph", "passage"]
		self.createData()		

	def generateData( self ):
		newData = {} 	# declare empty dictionary to generate and store values
		for key, value in self.formatt.iteritems():   #for each key,value in format 'structure'
			if value in self.strDataTypes+self.passageDataTypes:
				if value in self.passageDataTypes:
					newData[key] = ''.join([random.choice(string.ascii_letters) for n in xrange(32)])
				else:
					newData[key] = ''.join([random.choice(string.ascii_letters) for n in xrange(4)])
			elif value == int:
				newData[key] = random.randrange(5,75)
			elif value == float:
				newData[key] = random.uniform(20.5, 99.5)
		return newData

	def createData( self ):
		dataList = []
		# for each itertion call a function to generate dummy data
		for i in xrange(self.nrows):
			dataList.append(self.generateData()) # append the dummy data to list
		# print dataList
		dataFrame = pd.DataFrame(dataList, columns=list(self.formatt.keys()))
		print dataFrame    # to check the generated data output in terminal
		# dataFrame.to_csv(self.file_name,index=False)   
			# uncomment the above line to export to csv

structure = {"name": str, "age": int, "mark": float, "comments": "paragraph"}  
			# [1] : you can use word, paragraph, passage, etc.. for strings.
			# [2] : if you intented to add new datatype you can add in line 10 as well.
			
# calling a class with the parameters 
Formatting(structure, 4, "/home/amar/Documents/SampleData.csv")
		# use your file path and replace it

