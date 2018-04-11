# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:47:44 2018

@author: Amal Htait
"""
import sys
import re
import os
import nltk
import gensim.models as gm
from nltk.corpus import wordnet
import difflib
import time

filename = sys.argv[1] #The name of the file with the standard form words.
language = sys.argv[2] #The language of the list : AR for Arabic, FR for French and EN for English.
nbOfSimWords = int(sys.argv[3]) #The number of the most similar words extracted 

# Function to load the model according to the language : AR, FR or EN
def getTheModel(language):
	if language.upper() == 'EN':
		model_file = 'Models/EN/modelEN_newData_skip_gram'
	if language.upper() == 'FR':
		model_file = 'Models/FR/modelFR_newData_skip_gram'
	if language.upper() == 'AR':
		model_file = 'Models/AR/modelAR_newData_skip_gram'
	
	model = gm.Word2Vec.load(model_file)
	return model

# Function to get the first Antonym of a word from wordnet
def getAntonym(word):
	antonymList = []
	antonym = ''
	for syn in wordnet.synsets(word):
	    for l in syn.lemmas():
		if l.antonyms():
		    antonymList.append(l.antonyms()[0].name())
	if len(antonymList)>1:
		antonym = antonymList[1]

	return antonym

# Function to extract the list of misspelled words of "mainWord" from the result (data) of the function most_similar (of gensim)
def getTheListOfBadWords(data, mainWord):
	sim = 0
	finalArray = []

	for i in range(len(data)):
		theword = data[i][0]

		if (mainWord.lower() == (theword).lower()) or (theword).isdigit():
			pass
		else:
			val1 = removePunctuations(mainWord).lower()
			val2 = removePunctuations(theword).lower()
			if len(val1)>0 and len(val2)>0:
				seq = difflib.SequenceMatcher(None,val1,val2)
				sim = seq.ratio()*100
				if sim > 50.0 :
					finalArray.append(val2)
	return finalArray

# Function to remove punctuation in a string
def removePunctuations(str_input):
    ret = []
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in str_input:
        if char not in punctuations:
            ret.append(char)

    return "".join(ret)





start_time = time.time()
print ' --> Begin'

print ' --> Load Model'
# get the word embedding model
model = getTheModel(language)

print ' --> Create the Dictionary'
# get the list of misspelled words for each standard-form word
document = open(filename, 'r').readlines()
string = ""

for mylines in document:

	# get The antonym
	antonym = ''
	word = mylines.strip()

	if language.upper() != 'AR':
		antonym = getAntonym(word.decode('utf8', errors='ignore').encode('ascii', errors='ignore'))
	else:
		word = word.decode('utf-8')

	#get the list of misspelled words
	listMisspelled = ''
	arrayMisspelled = []

	try:
		listMisspelled = model.most_similar(positive=[word], topn=nbOfSimWords)
		arrayMisspelled = getTheListOfBadWords(listMisspelled, word)

	except:
		pass

	for i in range(len(arrayMisspelled)):
		string = string + arrayMisspelled[i] + '\t' + word + '\n'

# Create the Dictionary File
print ' --> Create the Dictionary File' + filename + "_" + str(nbOfSimWords) + "_dictionary"
resfile = open("Dictionaries/"+filename + "_" + str(nbOfSimWords) + "_dictionary", "w")


if language.upper() != 'AR':
	resfile.write(string)
else:
	resfile.write(string.encode('utf8'))

resfile.close()

print ' --> End'

# Calculate the time
end_time = time.time()
time = end_time - start_time

m, s = divmod(time, 60)
h, m = divmod(m, 60)
print " --> Time to Excecute %d:%02d:%02d" % (h, m, s)


