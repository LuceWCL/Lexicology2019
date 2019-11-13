import numpy as np

def main():

# solution avec boucle
  x = 1
  A = np.zeros([15,10])
  for i in range(0,A.shape[0]) :
    for j in range(0,A.shape[1]) :
      A[i,j] = x
      x = x+2
  print(A)

# sans boucle
  A = np.arange(1,300,2).reshape(15,10)
  print(A)

  B = A[:,2:6]
  print(B)

  C = A[0:5]
  print(C)

  z = np.zeros(10)
  z[4] = 1
  print(z)

  p = np.dot(A[0],z)
  print(p)

  q = np.dot(C,z)
  print(q)

if __name__ == '__main__':
  main()
