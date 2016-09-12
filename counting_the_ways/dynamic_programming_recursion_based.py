def genrange(min,max,stride=1):
    val=min
    while val<=max:
        yield val
        val+=stride


N = int(raw_input(""))
w = [int(x) for x in raw_input("").split(" ")]
LR = [int(x) for x in raw_input("").split(" ")]
mod = pow(10,9) + 7
w.sort()

di = dict()


def F_rec(x,w,w_idx):
    global di

    if x == 0 :
        return 1

    if w_idx==0:
        if x%w[w_idx]==0:
            return 1
        else:
            return 0
    
    if w[w_idx]>x:
        k = "f"+str(x)+","+str(w[w_idx-1])
        if k in di:
            return di[k]
        else:
            ris = F_rec(x,w,w_idx-1)
            di[k]=ris
            return ris
        
    else:

        k = "f"+str(x)+","+str(w[w_idx-1])
        if k in di:
            a = di[k]
        else:
            a = F_rec(x,w,w_idx-1)

        h = "f"+str(x-w[w_idx])+","+str(w[w_idx])
        if h in di:
            b = di[h]
        else:
            b = F_rec(x-w[w_idx],w,w_idx)
                
        return a+b

sol=0

for i in genrange(1,LR[1]):
    a =  F_rec(i,w,len(w)-1)
    di["f"+str(i)+","+str(w[len(w)-1])]=a
    if i>=LR[0]:
        sol += a
        sol %= mod

print sol
