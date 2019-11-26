import sys
import math

stop = {}
f = open("stopwords.lst", "r")
for line in f:
  stop[line.rstrip()] = 1
f.close

def main():
  wordfreq = {}
  bifreq = {}
  N = 0
  B = 0

  f = open(sys.argv[1], "r")
  for line in f:
    words = line.split()
    for word in words:
      if stop.get(word) == 1:
        continue
      N += 1
      if wordfreq.get(word) == None:
        wordfreq[word] = 1
      else:
        wordfreq[word] += 1

    for k in range(1,len(words)):
      if stop.get(words[k-1]) == 1 or stop.get(words[k]) == 1:
        continue
      bigram = words[k-1] + ' ' + words[k]
      B += 1
      if bifreq.get(bigram) == None:
        bifreq[bigram] = 1
      else:
        bifreq[bigram] += 1

  for word in sorted(wordfreq, key=wordfreq.get, reverse=True):
    print (word + "\t" +  str(wordfreq[word]))

#   print ('N=' + str(N))
#   print ('B=' + str(B))

  for word in sorted(bifreq, key=bifreq.get, reverse=True):
    print (word + "\t" +  str(bifreq[word]))

  
#### PMI ####

  for word in sorted(bifreq, key=bifreq.get, reverse=True):
    (w1,w2) = word.split()
    p_joint = bifreq[word] / B                      # P(A,B)
    p_marg = wordfreq[w1] / N * wordfreq[w2] / N    # P(A) * P(B)
    pmi = math.log((p_joint/p_marg),10)             # log(P(A,B)/(P(A)*P(B)))
    print (str(pmi) + ' ' + word)



if __name__ == '__main__':
  main()
