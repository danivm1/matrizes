import numpy as np
import random

print("------------- Multiplicacao de Matriz por escalar -------------")
m = int(input("Numero de linhas: "))
n = int(input('numero de colunas: '))
k = int(input('Digite o valor do escalar: '))
x=m*n

mat = np.arange(x).reshape(m,n)

for i in range(m):
	for j in range(n):
		mat[i][j]= random.randint(0,9)

print()
print('Matriz')
for i in range(m):
	for j in range(n):
		print(mat[i][j], end=" ")
	print()
print()

print('Matriz *', k)
for i in range(m):
	for j in range(n):
		mat[i][j]*= k


for i in range(m):
	for j in range(n):
		print(mat[i][j], end=" ")
	print()
