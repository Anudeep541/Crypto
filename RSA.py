'''
Created by Jane2197 on 23-09-19
RSA Algo
'''

### Extended Euclidean ###

def exteuc(num,dnm):
    tmp = num                                       # Storing "first num" value in tmp so it is used for mod at last
    quols = []
    remls = []
    remind = 0
    #print ("Inside Euclidean mat>>>")
    while True:
        rem = num%dnm
        quot = num//dnm
        if rem == 0:
            #print ("No Multiplicative Inverse")
            #quit()
            return 0
        #print ("quotient>>> ",quot)
        #print ("remainder>>> ",rem)
        remls.append(rem)
        quols.append(quot)
        #print ("Quotient List>>> ",quols)
        #print ("remainder list>>> ",remls)
        if rem == 1:
            break
        num = dnm
        dnm = remls[remind]
        #print (num,dnm)
        remind+=1
    r11,r12 = 1,0
    r21,r22 = 0,1
    qind = 0
    while qind<len(quols):
        tmpr1,tmpr2 = r21,r22
        r21,r22 = r11-r21*quols[qind],r12-r22*quols[qind]
        r11,r12 = tmpr1,tmpr2
        #print (r21,r22)
        qind+=1
    '''
    if r21<0 or r21>=num:
        r21 = r21%dnm
    '''
    if r22<0 or r22>=dnm:
        return r22%tmp
    else:
        return r22

### Calculating Φ(n) ###
'''
def funphi(a):
    pcnt = 0
    for j in range(1,a):
        if j==1:
            pcnt+=1
        var = exteuc(a,j)
        if var != 0:
            pcnt+=1
    return pcnt
'''
def pip():
    p = int(input("Enter p:"))
    for i in range(1,p):
        if i!= 1 and p%i==0:
            print ("The value of p you entered is not prime")
            return pip()
    return p

def qip():
    q = int(input("Enter q:"))
    for j in range(1,q):
        if j!= 1 and q%j==0:
            print ("The value of q you entered is not prime")
            return qip()
    return q

### p,q,n,Φ(n) values

p = pip()
q = qip()
n = p*q
phifn = (p-1)*(q-1)
#phifn = funphi(n)

def kyip():
    print ("Please select a number in [1,"+str(phifn)+"]")
    pubky = int(input())
    if pubky==0:
        print ("The number you entered can't be used as public key")
        return kyip()

    ### Calculating Private Key using input public key ###

    priky = exteuc(phifn,pubky)
    if priky == 0:
        print ("The number you entered can't be used as key")
        return kyip()
    return pubky,priky

pubky,priky = kyip()

print ("The public key 'e' = ",pubky)
print ("The private key 'd' = ",priky)

### Encryption ###
encls = []
print ("Please Enter Message in integer format")
enpltxt = int(input())
encitxt = pow(enpltxt,pubky)%n
'''
enpltxt = input()
for i in enpltxt:
    encitxt = (ord(i)**pubky)%n
    encls.append(encitxt)
'''
print ("Cipher Text>>>",encitxt)

### Decryption ###
decls = []
print ("Enter Cipher text in integer format")
decitxt = int(input())
depltxt = pow(decitxt,priky)%n
'''
for j in encls:
    depltxt = (j**priky)%n
    print (depltxt)
    decls.append(chr(j))
'''
print ("Decrypted Plain Text>>>",depltxt)
