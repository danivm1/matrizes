import numpy as np
import random
import os

print('------------- Multiplicacao Entre Matrizes -------------')

while True:
	mA = int(input("Linhas de A: "))
	nA = int(input("Colunas de A: "))
	x=mA*nA
	matA = np.arange(x).reshape(mA,nA)

	mB = int(input("Linhas de B: "))
	nB = int(input("Colunas de B: "))
	y=mB*nB
	matB = np.arange(y).reshape(mB,nB)
	
	if (nA!=mB):
		os.system('cls' if os.name == 'nt' else 'clear')
		print('Impossivel multiplicar, numero de colunas de A diferente do numero de linhas de B')
	else:	
		break

z=mA*nB
matC = np.arange(z).reshape(mA,nB)

for i in range(mA):
	for j in range(nA):
		matA[i][j] = random.randint(0,9)

for i in range(mB):
	for j in range(nB):
		matB[i][j] = random.randint(0,9)

for i in range(mA):
	for j in range(nB):
		prod = 0
		for k in range(mB):
			prod += matA[i][k] * matB[k][j]
		matC[i][j] = prod

print('Matriz A')
for i in range(mA):
	for j in range(nA):
		print(matA[i][j], end=' ')
	print()
print()

print('Matriz B')
for i in range(mB):
	for j in range(nB):
		print(matB[i][j], end=' ')
	print()
print()

print('Produto das matrizes')
for i in range(mA):
	for j in range(nB):
		print(matC[i][j], end=' ')
	print()
