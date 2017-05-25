import numpy as np
import scipy.linalg as la

M = 10

# Returns an Mxn+1 matrix of l of m of n
# Boolean vectors.

def l_of_m_of_n(l,m,n):
  print("l:%d m:%d n:%d"%(l,m,n))
  D = np.random.randint(2,size=(M,n+1))
  split = M/2
  D[:split,-1] = 1
  D[split:,-1] = 0
  m_idxs = np.random.choice(np.arange(n),m,replace=False)
  print(m_idxs)
  for i in range(split):
    x = D[i,:]
    l_idxs = np.random.choice(m_idxs,l,replace=False)
    for j in l_idxs:
      x[j] = 1

  for i in range(split, M):
    x = D[i,:]
    np.random.shuffle(m_idxs)
    high_ct = 0
    for i in m_idxs:
      high_ct+=x[i]
      if high_ct >= l:
        x[i] = 0
  np.random.shuffle(D)
  return D

if __name__ == "__main__":
  import sys
  l = int(sys.argv[1])
  m = int(sys.argv[2])
  n = int(sys.argv[3])
  l_of_m_of_n(l,m,n)
