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
	det = (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])

if m == 3:
	det = (mat[0][0] * mat[1][1] * mat[2][2]) + (mat[0][1] * mat[1][2] * mat[2][0]) + (mat[0][2] * mat[1][0] * mat[2][1]) - (mat[0][2] * mat[1][1] * mat[2][0]) - (mat[0][1] * mat[1][0] * mat[2][2]) - (mat[0][0] * mat[1][2] * mat[2][1])
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
