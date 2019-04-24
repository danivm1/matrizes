import numpy as np
import random
import os

cls="\n"*100
print("------------- Subtracao de Matrizes -------------")
while True:
	print("Matriz A")
	mA = int(input("Numero de linhas: "))
	nA = int(input("Numero de colunas: "))
	x=mA*nA
	matA = np.arange(x).reshape(mA,nA)

	print()
	
	print("Matriz B")
	mB = int(input("Numero de linhas: "))
	nB = int(input("Numero de colunas: "))
	x=mB*nB
	matB = np.arange(x).reshape(mB,nB)

	if (mA!=mB) or (nA!=nB):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Impossivel realizar a soma, numero de linhas ou de colunas diferentes entre as matrizes A e B")
	else:
		break

matC = np.arange(x).reshape(mB,nB)

for i in range(mA):
	for j in range(nA):
		matA[i][j] = random.randint(0,9)

for i in range(mA):
	for j in range(nA):
		matB[i][j] = random.randint(0,9)

for i in range(mA):
	for j in range(nA):
		matC[i][j] = matA[i][j] - matB[i][j]
print()

espaco = ' '*nA

print("Matriz A",espaco, end='		')
print("Matriz B",espaco, end='		')
print("Matriz C")

for i in range(mA):
	for j in range(nA):
		print(matA[i][j], end=" ")
	print("			", end='')
	for j in range(nA):
		print(matB[i][j], end=" ")
	print("			", end='')
	for j in range(nA):
		print(matC[i][j], end=" ")
	print()
