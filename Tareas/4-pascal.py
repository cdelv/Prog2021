from functools import lru_cache
 
@lru_cache(maxsize=50)
def combinatoria(n, k):
  if k in (0, n):
    return 1
  return combinatoria(n-1, k-1) + combinatoria(n-1, k)

def pascal(n):
  linea = []
  pascal = []
  for fila in range(n):
    for k in range(fila + 1):
        linea.append(combinatoria(fila,k))
    pascal.append(linea)
    linea = []
  print_pascal(pascal)

def print_pascal(pascal):
  max = len(' '.join(map(str,pascal[-1])))
  for p in pascal:
    print(' '.join(map(str,p)).center(max)+'\n')


pascal(100)