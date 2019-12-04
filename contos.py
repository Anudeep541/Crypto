'''

Created by Jane1729 on 06-10-2019
Solved Bugs --> Rejecting p or q inputs when <=0 or 1 on 27-10-19,29-10-19

'''

from PIL import Image
from datetime import datetime

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
    if r22<0 or r22>=dnm:
        return r22%tmp
    else:
        return r22

### Input p and q values and checking for prime ###


def pip():
    print ("Enter p:")
    p = int(input())
    if p == 1 or p <= 0:
        print ("This value can't be used as p")
        return pip()
    for i in range(1,p):
        if i!= 1 and p%i==0:
            print ("The value of p you entered is not prime")
            return pip()
    return p

def qip():
    print ("Enter q:")
    q = int(input())
    if q == 1 or q <= 0:
        print ("This value can't be used as q")
        return qip()
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

#### Tx side ####

def txky():
    print ("Please select a Tx pubkey in [1,"+str(phifn)+"]")
    txpubky = int(input())
    if txpubky==0:
        print ("The number you entered can't be used as public key")
        return txky()

    if txpubky > phifn:
        print ("The number you entered can't be used as public key")
        return txky()

    ### Calculating Private Key using input public key ###

    txpriky = exteuc(phifn,txpubky)
    if txpriky == 0:
        print ("The number you entered can't be used as key")
        return txky()
    return txpubky,txpriky

txpubky,txpriky = txky()
print ("The public key of sender 'e' = ",txpubky)
print ("The private key of sender 'd' = ",txpriky)

#### Rx Side ####

def rxky():
    print ("Please select a Rx pubkey in [1,"+str(phifn)+"]")
    rxpubky = int(input())
    if rxpubky==0:
        print ("The number you entered can't be used as public key")
        return rxky()
    
    if rxpubky > phifn:
        print ("The number you entered can't be used as public key")
        return rxky()

    ### Calculating Private Key using input public key ###

    rxpriky = exteuc(phifn,rxpubky)
    if rxpriky == 0:
        print ("The number you entered can't be used as key")
        return rxky()
    return rxpubky,rxpriky

rxpubky,rxpriky = rxky()

print ("The public key of receiver 'e' = ",rxpubky)
print ("The private key of receiver 'd' = ",rxpriky)

#### Mapping Heads and Tails and encrypting them ####

heads = 74
tails = 47
hednc = (heads**txpubky)%n
#print ("Heads after encrypting using txpubky",hednc)
taienc = (tails**txpubky)%n
#print ("Tails after encrypting using txpubky",taienc)

#### Giving options to Receiver ####

def selec():
    print ("Select one of the two options:")
    print ("1 or 2")
    opt = int(input())

    ### Getting system time ###

    now = datetime.now().time()
    ls = list(str(now))
    for i in ls:
        if i==':' or i=='.':
            ls.remove(i)
    temp = [int(j) for j in ls]
    timsum = sum(temp)

    if opt == 1:

        ### Checking if sum of time is even or not and assigning ###

        if timsum%2==0:
            opt = hednc
        else:
            opt = taienc
        #print ("You have selected option 1")

    elif opt == 2:
        if timsum%2==0:
            opt = taienc
        else:
            opt = hednc
        #print ("You have selected option 2")
    else:
        print ("You have selected wrong option")
        return selec()
    return opt

opt = selec()

#### Exchanging ####

rxenc  = (opt**rxpubky)%n
#print ("Rx side first encryption",rxenc)
txdec = (rxenc**txpriky)%n
#print ("Tx side decryption",txdec)
rxenc2 = (txdec**rxpriky)%n
#print ("Rx side second decrypt",rxenc2)

#### Output ####

if rxenc2 == heads:
    print ("You chose Heads")
elif rxenc2 == tails:
    print ("You chose Tails")
else:
    print ("Baaaam, wrong answer",rxenc2)

### Validating Output ###

def validation():
    print ("Please enter what you received")
    valid = input().capitalize()
    if valid == "Tails":
        chck = tails
    elif valid == "Heads":
        chck = heads
    else:
        print ("Input is Invalid")
        return validation()
    return chck

chck = validation()
if (chck**rxpubky)%n == txdec:
    print ("Honesty is the best policy and you are good at it")
else:
    print ("Liar!Liar! Pants on fire")
    #op = Image.open("meme.jpg")
    #op.show()