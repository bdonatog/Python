import string
class Names_Scores(object):
	def __init__(self, fileName):
		self.filename = fileName
	def GetListOfNames(self):
		listNames = []
		with open(self.filename, 'r') as namesFile:
			listNames = sorted(namesFile.read().replace('"','').split(","))
		namesFile.closed
		return listNames
	def AlphabetValues(self):
		alphabetDict = dict()
		for i, letter in enumerate(string.ascii_uppercase, 1):
			alphabetDict[letter] = i
		return alphabetDict
	def CalculateNamesScores(self,namesList):	
		alphabetDict = dict()
		namesScores = dict()
		alphabetDict = self.AlphabetValues()
		for v,nameScore in enumerate([sum(alphabetDict[l] for l in name) for name in namesList], 1):
			namesScores[v] = nameScore * v
		return namesScores
	def CalculateTotalNameScores(self):
		dictNamesScores= dict()
		dictNamesScores = self.CalculateNamesScores(self.GetListOfNames())
		print 'There are ' + str(len(dictNamesScores)) + ' name is the text file.'
		print 'The score for Colin is: ' + str(dictNamesScores[938])
		print 'the total of all names scores in the file is: ' + str(sum(dictNamesScores.itervalues()))

print 'Project Euler problem 22 - Names scores'
_Names_Scores = Names_Scores('c:\p022_names.txt')
_Names_Scores.CalculateTotalNameScores()

