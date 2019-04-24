import numpy as np
print("------------- Matriz Identitade -------------")
x = int(input("Ordem da matriz: "))
y=x*x

mat = np.arange(y).reshape(x,x)

for i in range(x):
	for j in range(x):
		if i==j:
			mat[i][j] = 1
		else:
			mat[i][j] = 0
print()
for i in range(x):
	for j in range(x):
		print(mat[i][j], end=" ")
	print()
