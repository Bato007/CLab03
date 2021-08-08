from random import randint


def wichmanhill(size):
  k = ''
  a = 1
  b = 30000
  # Se generan los 3 numeros
  s1, s2, s3 = [randint(a, b) for _ in range(3)]
  for _ in range(size):
    s1 = (171*s1) % 30269
    s2 = (172*s2) % 30307
    s3 = (170*s3) % 30323
    v = ((s1/30269.0) + (s2/30307.0) + (s3/30323.0)) % 1  # Se genera el numero
    k += str(round(v))  # Se agrega el
  return k


def xor(x1, xp):
  size = len(x1)
  if (size != len(xp)):
    return
  xored = ''
  # Ahora se hace la operacion xor
  for i in range(size):
    xored += '0' if x1[i] == xp[i] else '1'
  return xored
