'''
Created by Sai@Anudeep on 26-07-19
'''
# <<<<< Playfair Cipher >>>>>
#######
# Initialization
#######
import numpy as np
print ('Please enter the key>>>')
key = input().upper()
alph = """ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&'()*+,-./:;<=>?@[\]^_"""
f = len(key)
matsz = 8
arr = [[0 for i in range(matsz)] for j in range(matsz)]
r,ki,c = 0,0,0
aind = 0
#######
# Matrix Generation
#######
if f>=matsz:
    while r<matsz and ki<=f:
        while c<matsz:
            if ki>=f:
                filr,filc = r,c
                break
            arr[r][c] = key[ki]
            c+=1
            ki+=1
        if ki>=f:
            filr,filc = r,c
            break
        c = 0
        r+=1
#print (arr)
    print (filr,filc)
    while filr<matsz:
        while filc<matsz:
            if alph[aind] not in key:
                arr[filr][filc] = alph[aind]
                filc+=1
                aind+=1
            else:
                aind+=1
        filc = 0
        filr+=1
    print (arr)
    mat = np.array(arr)                                                         # Flat to matrix
    print (mat)
else:
    print ('Please Enter the key length greater than or equal to matsz')
    quit()
#######
# Encrypt
#######
pltxt = input('Enter PlainText>>> ').upper()
i1,i2 = 0,1
###
# Checking for two same letters in a pair
###
while i2<len(pltxt):
    if pltxt[i1] == pltxt[i2]:
        fils = list(pltxt)
        fils.insert(i2,'X')
        pltxt = ''.join(fils)
        print ('Plain Text after filler>>> ',pltxt)
    i1+=2
    i2+=2
cils = []
###
# Matrix Traverse to encrypt
###
def enc(pltxt):
    id1,id2=0,1
    while id2<len(pltxt):
        for sub1 in arr:
            if pltxt[id1] in sub1:
                l1p1 = arr.index(sub1)
                l1p2 = sub1.index(pltxt[id1])
    #print (p1,p2)
        for sub2 in arr:
            if pltxt[id2] in sub2:
                l2p1 = arr.index(sub2)
                l2p2 = sub2.index(pltxt[id2])
        if l1p1 == l2p1:
            cip1 = (l1p2+1)%matsz
            cip2 = (l2p2+1)%matsz
            cils.append(arr[l1p1][cip1])
            cils.append(arr[l2p1][cip2])
        if l1p2 == l2p2:
            cip1 = (l1p1+1)%matsz
            cip2 = (l2p1+1)%matsz
            cils.append(arr[cip1][l1p2])
            cils.append(arr[cip2][l2p2])
        elif pltxt[id1]!=pltxt[id2] and l1p1!=l2p1 and l1p2!=l2p2:
            cip1 = l2p2
            cip2 = l1p2
            cils.append(arr[l1p1][cip1])
            cils.append(arr[l2p1][cip2])
        id1 +=2
        id2 +=2
    print ('Cipher Text>>> ',''.join(cils))
#######
# Checking for length of plaintext
#######
if len(pltxt)%2==0:
    enc(pltxt)
else:
    apls = list(pltxt)
    apls.append('B')
    pltxt = ''.join(apls)
    enc(pltxt)