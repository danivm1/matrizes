import numpy as np
import random

print("------------- Matriz Transposta -------------")
m = int(input("Numero de linhas: "))
n = int(input('numero de colunas: '))
x=m*n

mat = np.arange(x).reshape(m,n)
mattrans = np.arange(x).reshape(n,m)

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

for i in range(n):
	for j in range(m):
		mattrans[i][j] = mat[j][i]


print('Matriz transposta')
for i in range(n):
	for j in range(m):
		print(mattrans[i][j], end=' ')
	print()
