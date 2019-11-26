import numpy as np

def main():

  A = np.arange(0,100).reshape(10,10)
  print(A)
  
  B = A[6:]
  print(B)
  
  y = A[:,0]
  print(y)

  C = A[3:7,0:6]
  print(C)
  
  z = np.arange(21,49,3)
  print(z)
  
  print(np.dot(y,z))
  
  print(np.dot(B,z))
 
 #exos https://github.com/fastai/numerical-linear-algebra :
  
  AIDS = np.array([[0.9,0.07,0.02,0.01],[0,0.93,0.05,0.02],[0,0,0.85,0.15],[0,0,0,1]])
  props = np.array([0.85,0.1,0.05,0])

  print(np.dot(props,AIDS))
  print(np.dot(np.transpose(AIDS),props))
  
  P = np.array([[6,5,3,1],[3,6,2,2],[3,4,3,1]])
  S = np.array([[1.5,1],[2,2.5],[5,4.5],[16,17]])

  print(np.dot(P,S))


if __name__ == '__main__':
  main()
