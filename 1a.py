import numpy as np
import random

print("------------- Matriz Diagonal -------------")
x = int(input("Ordem da matriz: "))
y=x*x

mat = np.arange(y).reshape(x,x)

for i in range(x):
	for j in range(x):
		if i==j:
			mat[i][j] = random.randint(0,9)
		else:
			mat[i][j]=0
print()
for i in range(x):
	for j in range(x):
		print(mat[i][j], end=" ")
	print()
