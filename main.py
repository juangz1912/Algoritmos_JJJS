import random

def sumar(m):  #(n)(n)
  contador = 0  #(1)
  for i in range(len(m)):  #(n)
    for j in range(len(m)):  #(n)(n)
      contador += m[i][j]  #(n)(n)
  print(contador)  #(1)

def crear(matriz, n):  #(n)(n)
  for i in range(n):  #(n)
    matriz.append([])  #(n)
    for j in range(n):  #(n)(n)

      # matriz[i].append(random.randint(0,10)) #(n)(n)
      matriz[i].append(1)  #(n)(n)
  print(*map(print, matriz))
  sumar(matriz)
  
crear([], 5)  #(n)(n)


#(n)(n)+(n)(n)+(1)+(1)+(n)(n)+(n)(n)+(n)+(n)
