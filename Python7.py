import Python6
m=int(input())
n=int(input())
A=Python6.create(m,n)
B=Python6.create(m,n)
C=[[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        C[i][j]=A[i][j]+B[i][j]

print("matrix A: " , A)
print("matrix B: " , B)
print("sum of matrix: ",C)
