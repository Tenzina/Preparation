#программа,которая заполняет двумерный массив случайными числами от 1 до 10
#m-количество строк,n-количество столбцов
from random import randint 
def create(m,n):
    arr=[[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            arr[i][j]=randint(1,10)
    return arr

#print(create(4,4))