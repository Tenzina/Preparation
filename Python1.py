#task_106
N=int(input())
nul=0
one=0
for i in range(N):
    coin=input()
    if (coin=="0"):
        nul+=1
    else:
        one+=1
if nul>one:
    print(one)
else:
    print(nul)

