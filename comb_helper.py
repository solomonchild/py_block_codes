memo = {}
def fact(n):
  if n == 1:
    memo[0] = 1  
    return memo[0]
  if not n in memo:
    memo[n] = fact(n-1)*n
    return memo[n]
  else:
    return memo[n]

def combine(n, m):
  return fact(n)/(fact(m) * fact(n-m))
