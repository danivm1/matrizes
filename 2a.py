import numpy as np
import random
import os

jooj=0
print('----------------- Determinante da Matriz -----------------')

while True:
	m = int(input('Insira a ordem da matriz (de 1 à 4)'))
	x = m*m
	mat = np.arange(x).reshape(m,m)

	if (m>4)or(m<1):
		jooj+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print('Ordem inválida, digite um número de 1 à 4')
		if jooj == 2:
			print('Posso ficar o dia todo nisso, sério.')
		if jooj > 2:
			print("I'm a joke to you?...")
	else:
		break

for i in range(m):
	for j in range(m):
		mat[i][j] = random.randint(0,9)

if m == 1:
	det = mat[0][0]

if m == 2:
	aux = [1,1]
	for i in range(m):
		j = i
		aux[0] *= mat[i][j]
	for i in range(m):
		j = m-i-1
		aux[1] *= mat[i][j]
	det = aux[0] - aux[1]

if m == 3:
	aux = [1,1,1,1,1,1]
	for i in range(m):
		j=i
		aux[0] *= mat[i][j]
	for i in range(m):
		j = i + 1
		if j == 3:
			j = 0
		aux[1] *= mat[i][j]
	for i in range(m):
		j = m-i*2-1
		if j == -2:
			j == 1
		aux[2] *= mat[i][j]
	for i in range(m):
		if i == 0:
			j = 0
		else:
			j = m-i
		aux[3] *= mat[i][j]
	for i in range(m):
		if i == 1:
			j = i
		else:
			j = m-i-1
		aux[4] *= mat[i][j]
	for i in range(m):
		if i == 2:
			j = i
		else:
			j = m-i-2
		aux[5] *= mat[i][j]
	det = 0
	for i in range(6):
		if i <= 2:
			det += aux[i]
		else:
			det -= aux[i]


'''
--- À fazer ---
if m == 4:
	det=0
	for k in range(m):
		for j in range(m):
			if k!=j:
				det+=(mat[0][k]*mat[1][j]*mat[2][2]*mat[3][3])
'''
for i in range(m):
	for j in range(m):
		print(mat[i][j], end=' ')
	print()
print()

print(det)
