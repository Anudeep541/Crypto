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

def funphi(a):
    pcnt = 0
    for j in range(1,a):
        if j==1:
            pcnt+=1
        var = exteuc(a,j)
        if var != 0:
            pcnt+=1
    return pcnt

n = 33
phifn = funphi(n)
print ("Please select a number in [0,"+str(phifn)+"]")
pubky = int(input())
if pubky==0:
    print ("The number you entered can't be used as public key")
    quit()

### Calculating Private Key using input public key ###

priky = exteuc(phifn,pubky)
if priky == 0:
    print ("The number you entered can't be used as key")
    quit()
print ("The public key 'e' = ",pubky)
print ("The private key 'd' = ",priky)

### Encryption ###

print ("Please Enter Message in integer format")
enpltxt = int(input())
encitxt = (enpltxt**pubky)%n
print ("Cipher Text>>>",encitxt)

### Decryption ###

print ("Enter Cipher text in integer format")
decitxt = int(input())
depltxt = (decitxt**priky)%n
print ("Decrypted Plain Text>>>",depltxt)
