# NormAFE
The tool creates dictionaries for micro-blogs normalisation, in a form of pairs of misspelled word with its standard-form word, in the languages: Arabic, French and English.

Developer : 
		Amal Htait
		Ph.D. Researcher, Marseilles, France.


Citation :	
		If using this code or these word embedding models, please cite our work using :

		@inproceedings{htait18,
  		title={Unsupervised Creation of Normalisation Dictionaries for Micro-Blogs in Arabic, French and English},
  		author={Htait, Amal  and Fournier, Sebastien and Patrice, Bellot},
  		booktitle={International Conference on Computational Linguistics and Intelligent Text Processing},
  		year={2018}
		}


Acknowledgments : 
		This work has been supported by the French State, managed by the National Research Agency under the "Investissements d'avenir" program under the EquipEx DILOH projects (ANR-11-EQPX-0013).



Project Information :

		Text normalisation is a necessity to correct and make more sense of the micro-blogs messages, for information retrieval purposes.
		Unfortunately, tools and resources of text normalisation are rarely shared. In our paper, an approach is presented based on an unsupervised method for text normalisation using distributed 			representations of words, known also as "word embedding", applied on Arabic, French and English Languages. THis tool is supplied to create dictionaries for micro-blogs normalisation, in a 			form of pairs of misspelled word with its standard-form word, in the languages: Arabic, French and English.

		This script include :

		1 - Three word embedding models of size : 
			Arabic : 9 million words  (Models/AR/modelAR_newData_skip_gram)
			English : 5 million words  (Models/EN/modelEN_newData_skip_gram)
			French : 415 thousand words  (Models/FR/modelFR_newData_skip_gram)


		2 - Three exemplary normalisation dictionaries :
			English : 18 thousand pairs  (Example_Dictionaries/EN_18_thousand_pairs.txt)
			Arabic : 10 thousand pairs  (Example_Dictionaries/AR_10_thousand_pairs.txt)
			French : 3 thousand pairs  (Example_Dictionaries/FR_3_thousand_pairs.txt)


Prerequisites : 
		Python 2.7.13
		gensim
		nltk 3.2.2
		difflib


Usage : 	By command line :
		python NormAFE.py file_name language nbOfSimilarWords
		The output will be found in the folder Dictionaries, and has the name : fileName_nbOfSimWords_dictionary 
		And will contain a list of pairs of misspelled word with its standard-form word.
 
		Example : an example of use with a file named list_ar, in Arabic language, with dictionary created based on 5 most similar words
			  python NormAFE.py list_ar AR 5
