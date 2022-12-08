import numpy as np

def is_prime (y):
  result = True
  for x in range (2, round(np.sqrt(y))+1):
    if y%x == 0:
        result = False
        break
  return result

lista_no_primos_consecutivos = []
n = 0
while len(lista_no_primos_consecutivos) < 73:
  n += 1
  if is_prime(n):
    lista_no_primos_consecutivos = []
  else:
    lista_no_primos_consecutivos.append(n)

print(lista_no_primos_consecutivos)