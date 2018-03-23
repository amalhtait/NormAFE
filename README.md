# NormAFE
The tool creates dictionaries for micro-blogs normalisation, in a form of pairs of misspelled word with its standard-form word, in the languages: Arabic, French and English.

**Developer** <br />	
Amal Htait <br />
Ph.D. Candidate, Marseilles, France. <br />


**Citation** <br />
```	
If using this code or these word embedding models, please cite our work using : 
		@inproceedings{htait18, 
  		title={Unsupervised Creation of Normalisation Dictionaries for Micro-Blogs in Arabic, French and English}, 
  		author={Htait, Amal  and Fournier, Sebastien and Bellot, Patrice}, 
  		booktitle={International Conference on Computational Linguistics and Intelligent Text Processing}, 
  		year={2018} 
		} 
```

**Acknowledgments** <br />
This work has been supported by the French State, managed by the National Research Agency under the "Investissements d'avenir" program under the EquipEx DILOH projects (ANR-11-EQPX-0013). <br />

**License** <br />
NormAFE is released under the terms of the GPL version 2.

**Project Information** <br />
Text normalisation is a necessity to correct and make more sense of the micro-blogs messages, for information retrieval purposes. Unfortunately, tools and resources of text normalisation are rarely shared. In our paper, an approach is presented based on an unsupervised method for text normalisation using distributed representations of words, known also as "word embedding", applied on Arabic, French and English Languages. This tool is supplied to create dictionaries for micro-blogs normalisation, in a form of pairs of misspelled word with its standard-form word, in the languages: Arabic, French and English. <br />

**This script include** <br />
```
1 - Three word embedding models of size : <br />
	Arabic : 9 million words  (Models/AR/modelAR_newData_skip_gram)
	English : 5 million words  (Models/EN/modelEN_newData_skip_gram)
	French : 415 thousand words  (Models/FR/modelFR_newData_skip_gram)
```
```
2 - Three exemplary normalisation dictionaries :<br />
	English : 18 thousand pairs  (Example_Dictionaries/EN_18_thousand_pairs.txt)
	Arabic : 10 thousand pairs  (Example_Dictionaries/AR_10_thousand_pairs.txt)
	French : 3 thousand pairs  (Example_Dictionaries/FR_3_thousand_pairs.txt)
```

**Prerequisites** <br />
```
- Python 2.7.13
- gensim
- nltk 3.2.2
- difflib
```

**Usage by command line** <br />
python NormAFE.py file_name language nbOfSimilarWords <br />
The output will be found in the folder Dictionaries, and has the name : fileName_nbOfSimWords_dictionary. <br />
And will contain a list of pairs of misspelled word with its standard-form word. <br />
 
**Example** <br />
An example of use with a file named list_ar, in Arabic language, with dictionary created based on 5 most similar words: <br />
```
python NormAFE.py list_ar AR 5
```
