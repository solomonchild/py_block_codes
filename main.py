from comb_helper import *
import sys
from matrix import *

def test():
  H = Matrix(4, 3)
  H[0] = [1, 1, 1]
  H[1] = [1, 0, 1]
  H[2] = [1, 1, 0]
  H[3] = [1, 0, 0]
  G = get_identity_matrix(3).extend_right(H.T())
  H.extend_right(get_identity_matrix(4))

  v = Matrix(1, 3)
  v.data[0] = [1,1,0]
  u = v * G
  print u
  u[0][1]=0
  res = u*H.T()
  print "Is second digit?: ", H.T().data.index(res[0])+1 == 2


def get_distance(n, k):
  rhs = pow(2, n-k)
  for i in range(1, n + 1):
    acc = 0
    for j in range(1, i + 1):
      acc+= combine(n, j)
    if acc >= rhs -1:
      return i + 1  
  return -1
def get_mul_detection(d):
  for i in range(0, d):
    if d < i +1:
      return i -1
    elif d == i+1:
      return i
  return -1 

def get_mul_correction(d):
  for i in range(0, d):
    if d < 2*i +1:
      return i -1
    elif d == 2*i + 1:
      return i
  return -1 

def main():
  n = 10 
  k = 4 
  d = get_distance(n, k)
  qo = get_mul_detection(d)
  qu = get_mul_correction(d)
  print "n = {0}, k ={1}\nd = {2} \nqo = {3} \nqu = {4} \n".format(n, k, d,qo,qu)

  #test()
  G = Matrix(k, n-k)
  H = Matrix(n-k, k)
  G[0] = [1, 1, 0, 1, 1, 0]
  G[1] = [1, 0, 1, 1, 0, 1]
  G[2] = [0, 1, 1, 1, 1, 1]
  G[3] = [0, 0, 0, 0, 1, 1]
  H = G.T()
  G = get_identity_matrix(k).extend_right(G)


  H.extend_right(get_identity_matrix(n-k))

  print "G\n", G
  print "H\n", H
  print "Check G*H^t\n" ,G*H.T()

  u = Matrix(1, n)
  v = Matrix(1, k)
  v.data[0] = [0] * k
  v.data[0][0] = 1
  v.data[0][1] = 1
  u = v * G
  print "u", u
  print "H^T", H.T()
  u[0][1] = 0 #mistake in second

  res = u*H.T()
  print "u*H^T:", res
  print "Corrupt: ",H.T().data.index(res[0])+1

if __name__ == "__main__":
    main()
