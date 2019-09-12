'''
Created by Jane2197 on 12-9-19
'''
iredpol = [1,0,1,1]
print ("Please Enter polynomial coeff in order>>>")
poly = list(map(int,input().split()))
if len(poly)>4:
    print ("Please Enter the polynomial of degree<=4")
    quit()
#print ("Poly>>>",poly)
qls = [0,0,0,0]                             # Quotient List
polen = len(poly)



### Division ###

def div(num,den):
    i,j = 0,0
    while i<polen:
        if poly[i]!=0:
            polypow = 4-(i+1)                   # Starting Power of Polynomial
            break
        i+=1
    while j<len(num):
        if num[j]!=0:
            iredpow = 4-(j+1)                   # Starting Power of irreducible Polynomial
            break
        j+=1
    while True:
        itmls = [0,0,0,0]                           # Intermediate List
        remls = [0,0,0,0]                           # rem1der List
        quopow = iredpow - polypow
        #print ("Quopow>>>",quopow)
        qls[3-quopow] = 1                           # 3-quopow gives with what degree of x we need in quotient
        #print ("Quot List>>>",qls)
        k = 0
        while k<polen:
            if poly[k]!=0:
                #print ("k>>>",k)
                #print ("Index>>>",3-(quopow+4-(k+1)))
                itmls[3-(quopow+4-(k+1))] = 1
            k+=1
        print ("Intermd List",itmls)
        
        ## XOR Funcn

        x = 0
        while x<polen:
            if num[x]!=itmls[x]:
                remls[x] = 1
            elif num[x]==itmls[x]:
                remls[x] = 0
            x+=1
        print ("Remls>>>",remls)
        y = 0
        while y<len(remls):
            if remls[y]!=0:
                rempow = 4-(y+1)                   # Starting Power of rem1der Polynomial
                break
            y+=1
        if rempow>=polypow:
            iredpow = rempow
            num = remls
        else:
            #print ("Remls>>>",remls)
            return qls,remls

# Extended Euclidean

def exteuc(z,u,v):
    eucquo = [z]
    eucrem = []
    rmidx = 0
    while True:
        quo1,rem1 = div(u,v)
        eucquo.append(quo1)
        eucrem.append(rem1)
        zrocnt = 0
        for d in rem1:
            if d == 0:
                zrocnt+=1
        if zrocnt == len(rem1)-1 and rem1[-1] == 1:
            break
        u = v
        v = eucrem[rmidx]
        rmidx+=1
    r11,r12 = [1 for e in range(4)],[0 for f in range(4)]
    r21,r22 = [0 for g in range(4)],[1 for h in range(4)]
    





quot,remn = div(iredpol,poly)
znt = 0
for i in remn:
    if i == 0:
        znt+=1
if znt == len(remn)-1 and remn[-1] == 1:              # Checking for only '1' in remainder
    print ("Mul List>>>",quot)
else:
    mulinv = exteuc(quot,poly,remn)
