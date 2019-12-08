import sys
import re
import math
import numpy as np

def normalize(word):
 return re.sub(r"[\.\,\?\:\;\"\'\-]",r"",word.lower())

wordlist = {}
vocab5000 = []

def main():
 # créer dictionnaire de fréquence avec tous les mots
  for k in range(7769):
    filename = "training/" + str(k) + ".txt"
    f = open(filename, "r")
    for line in f:
      for word in line.rstrip().split():  
        if word in wordlist:
          wordlist[normalize(word)] += 1
        else:
          wordlist[normalize(word)] = 1

  # sélectionner les top 5000 dans vocab5000
  g=0
  for x in sorted(wordlist, key=wordlist.get, reverse=True):
    if g == 5000: break
    vocab5000.append(x)
    g += 1

# construire la matrice terme-doc avec des valeurs de co-occurrence
  M = np.zeros([7769,len(vocab5000)])    
  for k in range(7769):     
    filename = "training/" + str(k) + ".txt"
    f = open(filename, "r")
    for line in f:
      for word in line.rstrip().split():  
        if normalize(word) in vocab5000:
          M[k,vocab5000.index(normalize(word))] += 1
        
  print (M[1,vocab5000.index("and")]) # test

  
# calculer le tf-idf à partir de M. tf est la valeur de co-occurrence (term frequency in document), 
# idf est la prop l'inverse du nombre de documents qui contiennent t (où M[doc,terme] > 0)
  TFIDF = np.zeros(M.shape)
  for i in range (TFIDF.shape[0]):
    for j in range (TFIDF.shape[1]):
      tf = M[i,j]   # M[i,j] : co-occurrences, tf
      idf = math.log(7769 /(np.count_nonzero(M[:,j])))  # nb de docs / nb de  valeurs >0 dans la colonne du mot j      
      TFIDF[i,j] = tf * idf         
                                                            

    
if __name__ == '__main__':
  main()
