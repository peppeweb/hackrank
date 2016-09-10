def genrange(min,max,stride=1):
    val=min
    while val<=max:
        yield val
        val+=stride

N = int(raw_input(""))
w = [int(x) for x in raw_input("").split(" ")]
LR = [int(x) for x in raw_input("").split(" ")]
mod = pow(10,9) + 7
matrice = [ [ 0 for i in range(len(w))] for j in genrange(1,LR[1]+1)]

for i in range(N):
    matrice[0][i]=1


for i in genrange(1,LR[1]):
    matrice[i][0] = 1 if (i % w[0]) == 0 else 0

for i in genrange(1,LR[1]):
    for j in range(1,N):
        if w[j]>i:
            matrice[i][j] = matrice[i][j-1]
        else:
            matrice[i][j] = matrice[i][j-1] + matrice[i-w[j]][j]
            
        matrice[i][j]= matrice[i][j] % mod

sol=0

for i in genrange(LR[0],LR[1]):
    sol += matrice[i][N-1]
    sol %= mod

print sol
