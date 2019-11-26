import sys
import re
import math
import numpy as np


def normalize(word):
 return re.sub(r"[\.\,\?\:\;\"\'\-]",r"",word.lower())

# la liste de mots w et c:
vocabulary = []

f = open("words.lst", "r")
for line in f:
  w = (line.rstrip())
  vocabulary.append(w)
f.close


# definir les dimensions de la matrice M à partir de vocabulary
# initialiser la matrice numpy, avec des valeurs 0 :

M = np.zeros([len(vocabulary),len(vocabulary)])


def main():

  f = open(sys.argv[1], "r")
  for line in f:
    words = line.split()

    for k in range(len(words)):
      if normalize(words[k]) in vocabulary:
        for i in range(k-5, k+6):
          if i == k:
            i += 1
          else:
            if i >= 0 and i <= len(words)-1:
              if words[i] in vocabulary:
                M[vocabulary.index(normalize(words[k])), vocabulary.index(normalize(words[i]))] += 1
            #    print (normalize(words[k]) + ' ' + normalize(words[i]) + ' ' + str(M[vocabulary.index(normalize(words[k])), vocabulary.index(normalize(words[i]))]))
      
#  print(M)      

  user = input("Entrez deux mots: ")
  ws = user.split()
  try: 
    print(M[vocabulary.index(normalize(ws[0])),vocabulary.index(normalize(ws[1]))])
  except ValueError:
    print("Je ne trouve pas ce mot.")
  
  
if __name__ == '__main__':
  main()
