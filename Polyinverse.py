'''
Created by Jane2197 on 12-9-19
'''
iredpol = [1,0,1,1]                     # Irreducible Polynomial -> x^3+x+1
'''
print ("Choose how to enter your polynomial")
print ("1) Enter Coefficients")
print ("2) Enter Polynomial")
chce = int(input())
'''
#if chce == 1:
print ("Please enter coefficinets in order with space:")
poly = list(map(int,input().split()))
polen = len(poly)

'''
elif chce == 2:
    print ("Please enter the polynomial in variable 'x':")
    polyinx = input().split('+')
'''

### Counting for number of zeros ###

cntr = 0
for i in poly:
    if i==0:
        cntr+=1

### Checking if coeff's entered is greater than required 

if len(poly)>4:
    print ("Please Enter the polynomial of degree<=4")
    quit()

### Checking for all zeros in input ###

if cntr==polen:
    print ("No Multiplicative Inverse Exists")
    quit()

### Checking if entered polynomial is '1'

if cntr == polen-1 and poly[-1] == 1:
    print ("Multiplicative Inverse is 1")
    quit()

ind = 0
polystr = 0
while ind<polen:
    if poly[ind]!=0:
        polystr = str(polystr)+"x^"+str(4-(ind+1))+ "+"
    ind+=1
tmpls = list(polystr)
tmpls.pop(0)
tmpls.pop(len(tmpls)-1)
print ("The polynomial with coefficients you entered is:")
print (''.join(tmpls))


### Division ###

def div(num,den):
    i,j = 0,0
    rempow = 0
    qls = [0,0,0,0]                             # Quotient List
    while i<polen:
        if den[i]!=0:
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
            if den[k]!=0:
                #print ("k>>>",k)
                #print ("Index>>>",3-(quopow+4-(k+1)))
                itmls[3-(quopow+4-(k+1))] = 1
            k+=1
        #print ("Intermd List",itmls)
        
        ## XOR Funcn

        x = 0
        while x<polen:
            if num[x]!=itmls[x]:
                remls[x] = 1
            elif num[x]==itmls[x]:
                remls[x] = 0
            x+=1
        #print ("Remls>>>",remls)
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
    #print ("z>>>",z)
    #print ("u>>>",u)
    #print ("v>>>",v)
    rmidx = 0
    eultnt = [z]
    eucrem = []
    while True:
        #print ("Before eultnt>>>",eultnt)
        #print ("Before Eucrem>>>",eucrem)
        quo1,rem1 = div(u,v)
        #print ("Quo1>>>",quo1)
        #print ("rem1>>>",rem1)
        eultnt.append(quo1)
        eucrem.append(rem1)
        #print ("After eultnt>>>",eultnt)
        #print ("After Eucrem>>>",eucrem)
        zrocnt = 0
        for d in rem1:
            if d == 0:
                zrocnt+=1
        if zrocnt == len(rem1)-1 and rem1[-1] == 1:
            break
        u = v
        v = eucrem[rmidx]
        rmidx+=1
    r11,r12 = [0,0,0,1],[0 for f in range(4)]
    r21,r22 = [0 for g in range(4)],[0,0,0,1]
    qind = 0
    while qind<len(eultnt):
        mulfac = eultnt[qind]
        #print ("Mulfac>>>",mulfac)
        tmpr1,tmpr2 = r21,r22
        l = 0
        res = [0,0,0,0]
        tmp = [0,0,0,0]
        while l<len(r22):
            m = 0
            if r22[l]!=0:
                r22pow = 4-(l+1)
                while m<len(mulfac):
                    if mulfac[m]!=0:
                        mulpow = 4-(m+1)
                        tmp[3-(r22pow+mulpow)] = 1
                        res = [res[i]+tmp[i] for i in range(4)]
                        tmp = [0,0,0,0]
                    m+=1
            l+=1
        #print ("Res",res)
        r22 = res
        #print ("Before r11>>>",r11)
        #print ("Before r12>>>",r12)
        #print ("Before r21>>>",r21)
        #print ("Before r22>>>",r22)
        c = 0
        while c<polen:
            r21[c] = r11[c] - r21[c]
            r22[c] = r12[c] - r22[c]
            c+=1
        r11,r12 = tmpr1,tmpr2
        #print ("After r11>>>",r11)
        #print ("After r12>>>",r12)
        #print ("After r21>>>",r21)
        #print ("After r22>>>",r22)
        qind+=1
    p = 0
    while p<len(r22):
        r22[p] = r22[p]%2
        p+=1
    return r22


quot,remn = div(iredpol,poly)
#print ("Quot>>>",quot)
#print ("Remn>>>",remn)

### Counting for number of zeros ###

znt = 0
for i in remn:
    if i == 0:
        znt+=1

### Checking for only '1' in remainder and if yes that is the multiplicative inverse ###

if znt == len(remn)-1 and remn[-1] == 1:              
    print ("Coefficients of inverse polynomial>>>",quot)
    ind1 = 0
    polystr1 = 0
    while ind1<len(quot):
        if quot[ind1]!=0:
            polystr1 = str(polystr1)+"x^"+str(4-(ind1+1))+ "+"
        ind1+=1
    tmpls1 = list(polystr1)
    tmpls1.pop(0)
    tmpls1.pop(len(tmpls1)-1)
    print ("Inverse Polynomial>>> ",''.join(tmpls1))

### If not above proceed to Extended Euclidean

else:
    mulinv = exteuc(quot,poly,remn)
    print ("Coefficients of inverse polynomial>>>",mulinv)
    ind2 = 0
    polystr2 = 0
    while ind2<len(mulinv):
        if mulinv[ind2]!=0:
            polystr2 = str(polystr2)+"x^"+str(4-(ind2+1))+ "+"
        ind2+=1
    tmpls2 = list(polystr2)
    tmpls2.pop(0)
    tmpls2.pop(len(tmpls2)-1)
    print ("Inverse Polynomial>>> ",''.join(tmpls2))
