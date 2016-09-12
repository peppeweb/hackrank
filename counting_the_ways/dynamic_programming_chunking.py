def genrange(min,max,stride=1):
    val=min
    while val<=max:
        yield val
        val+=stride

N = int(raw_input(""))
w = [int(x) for x in raw_input("").split(" ")]
w.sort()
LR = [int(x) for x in raw_input("").split(" ")]
mod = pow(10,9) + 7

chunk = max(w) + 5
matrice = [ [ 0 for i in range(len(w))] for j in range(chunk+1)]


def init(m,N):
    for i in range(N):
        m[0][i]=1


def divisible(m,x,w,idxChunk):
    
    for i in range(1,x+1):
        l = (idxChunk-1)*x  + i +1
        m[i][0] = 1 if (l % w[0]) == 0 else 0
        for j in range(1,len(w)):
            m[i][j]=0

def calculateLocal(m,x,w,N,idxChunk):
    global di
  
    for i in range(1,x+1):
        l = (idxChunk-1)*x  + i

        for j in range(1,N):
            if w[j]>l:
                m[i][j] = m[i][j-1]
            else:
                k =  (l-w[j])          
                if (k in di):
                    v = di[k]
                    if w[j] in v:
                        m[i][j] += v[w[j]]
                    else:
                        m[i][j] += m[i-w[j]][j]
                else:
                    m[i][j] += m[i-w[j]][j]
                
                m[i][j] += m[i][j-1] 
                
            m[i][j]= m[i][j] % mod
       

def storeLocalSolution(m,x,w,LR,idxChunk):
    global di
    for i in range(1,x+1):
    
        l = (idxChunk-1)*x  + i
        tmp = dict()
        k = l
        di[k]= dict()
        for j in range(len(w)):
            if l<=LR:
                di[k][w[j]]= m[i][j]
 
    clean = (idxChunk-3)*x+1

    
    if clean>=1 and idxChunk>=3:
         valuesRemoved = [di.pop(ve, None) for ve in range(clean,clean+x)]



nIterazioni = LR[1] / chunk
sol2=0
for i in genrange(1,nIterazioni+1):
        l = (i-1)*chunk +1
        init(matrice,N)
        
        divisible(matrice,chunk,w,i)
        
        calculateLocal(matrice,chunk,w,N,i)
        storeLocalSolution(matrice,chunk,w,LR[1],i)
        
        for sd in range(l,l+chunk):
            loc = di[sd]
            if len(loc)>0:
                ma = max(loc.keys())
                
                if sd>=LR[0] and sd<=LR[1]:
                    sol2 += loc[ma]
           

print sol2
