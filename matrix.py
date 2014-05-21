from os import linesep
import re
class Matrix:
  def __init__(self, n, m):
    self.m = m
    self.n = n
    self.data = [[0 for i in range(m)] for j in range(n) ] 

  def __str__(self):
    temp = str(self.data)[1:][:-1].replace("]","]" + linesep).replace(", ", " ")
    return re.sub(' (?=\[)','', temp)

  def __getitem__(self, index):
    return self.data[index] 

  def __setitem__(self, key, item):
    self.data[key] = item

  def __mul__(self, other):
    m = Matrix(self.n, other.m)
    if self.m != other.n:
      raise Exception("Matrixes should have equal dims")
    for new_row in range(self.n):
      for new_col in range(other.m):
	for iter in range(other.n): #or self.m
	  m[new_row][new_col] ^= self[new_row][iter] * other[iter][new_col]
    return m
  
  def extend_right(self, other):
    if self.n == other.n:
      for row in range(other.n):
	self.data[row].extend([0] * other.m)
	for col in range(other.m):
	  self.data[row][self.m + col] = other[row][col]
      self.m += other.m
    return self

  def extend_bottom(self, other):
    if self.m == other.m:
      for row in range(other.n):
	self.data[row + self.n].extend([0] * other.m)
	for col in range(other.m):
	  self.data[row+self.n][col] = other[row][col]
      self.n += other.n
    return self

  def T(self):
    matrix = Matrix(self.m, self.n)
    for j in range(self.m):
      matrix.data[j] = [self.data[i][j] for i in range(self.n)] 
    #temp = self.n
    #self.n = self.m
    #self.m = temp 
    #self.data = matrix.data
    return matrix

	  
def get_identity_matrix(n):
  m = Matrix(n, n)
  for i in range(n):
    m.data[i] = [0 for j in range(n)]
    m.data[i][i] = 1
  return m

