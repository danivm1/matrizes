import numpy as np
import random

print("------------- Matriz Simetrica -------------")
x = int(input("Ordem da matriz: "))
y=x*x

mat = np.arange(y).reshape(x,x)

for i in range(x):
	for j in range(x):
		mat[i][j] = mat[j][i] = random.randint(0,9)
		
print()
for i in range(x):
	for j in range(x):
		print(mat[i][j], end=" ")
	print()
