'''
Created by Sai@Anudeep on 26-07-19
Mod by admin on 28-07-19
'''
# <<<<< Playfair Cipher >>>>>
#######
# Initialization
#######
import numpy as np
alph = """ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&'()*+,-./:;<=>?@[\]^_"""
matsz = 8                                                               # Matrix size
arr = [[0 for i in range(matsz)] for j in range(matsz)]                 # Creating null matrix of given size
r,ki,c = 0,0,0                                                          # row,column and key index
aind = 0                                                                # alphabet index
def keyip():
    kls = []
    bolst = []
    yek = input('Please enter the key>>> ').upper()
    if len(yek)<matsz:
        print ('Please Enter the key length >= {}'.format(matsz))
        keyip()
    
    # Checking for character repitition in key
    
    def kichck():
        for i in yek:
            if i in kls:
                bolst.append(False)
            else:
                kls.append(i)
                bolst.append(True)
        return all(bolst)
    bol = kichck()
    if len(yek)>=matsz and bol==True:       
        return yek
    #elif len(yek)<matsz and bol == False:
    #    print ('Please Enter the key length >= {} and without character repetition'.format(matsz))
    #    keyip()
    elif bol == False:
        print ('Please Enter key without character repitition')
        keyip()
#######
# Matrix Generation
#######
key = keyip()
while r<matsz and ki<=len(key):
    while c<matsz:
        if ki>=len(key):
            filr,filc = r,c
            break
        arr[r][c] = key[ki]
        c+=1
        ki+=1
    if ki>=len(key):
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
    #print (arr)
mat = np.array(arr)                                                         # Flat to matrix
print (mat)
#######
# Encrypt
#######
pltxt = input('Enter PlainText>>> ').upper()                                    # Plain text
orgpltxt = pltxt
i1,i2 = 0,1
###
# Checking for two same letters in a pair
###
while i2<len(pltxt):
    if pltxt[i1] == pltxt[i2]:
        fils = list(pltxt)
        fils.insert(i2,'?')
        pltxt = ''.join(fils)
        print ('Plain Text after filler>>> ',pltxt)
    i1+=2
    i2+=2
cils = []                                                                       # List for cipher text
###
# Matrix Traverse to encrypt
###
def enc(pltxt):
    id1,id2=0,1
    while id2<len(pltxt):
        for sub1 in arr:
            if pltxt[id1] in sub1:
                l1p1 = arr.index(sub1)                                          # letter1 position1 i.e row number 
                l1p2 = sub1.index(pltxt[id1])                                   # letter1 position2 i.e column number
    #print (p1,p2)
        for sub2 in arr:
            if pltxt[id2] in sub2:
                l2p1 = arr.index(sub2)                                          # letter2 pos1 i.e row number
                l2p2 = sub2.index(pltxt[id2])                                   # letter2 pos2 i.e column number
        
        # Checking if both letters are in same row
        
        if l1p1 == l2p1:                                                        
            cip1 = (l1p2+1)%matsz
            cip2 = (l2p2+1)%matsz
            cils.append(arr[l1p1][cip1])
            cils.append(arr[l2p1][cip2])

        # Checking if both letters are in same column    

        if l1p2 == l2p2:
            cip1 = (l1p1+1)%matsz
            cip2 = (l2p1+1)%matsz
            cils.append(arr[cip1][l1p2])
            cils.append(arr[cip2][l2p2])
        
        # If not above cases
        
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

#######
# Decrypt
#######
pnls = []                                                                   # Plaintext list
citxt = ''.join(cils)
#print ('Cipher text>>> ',citxt)
cid1,cid2 = 0,1
while cid2<len(citxt):
    for csub1 in arr:
        if citxt[cid1] in csub1:
            c1p1 = arr.index(csub1)
            c1p2 = csub1.index(citxt[cid1])
    for csub2 in arr:
        if citxt[cid2] in csub2:
            c2p1 = arr.index(csub2)
            c2p2 = csub2.index(citxt[cid2])
    
    # Checking if both cipher letters belong to same row

    if c1p1 == c2p1:
        pip1 = (c1p2-1)
        pip2 = (c2p2-1)
        if pip1<0:                                                              # Checking if cipher is in any column of 1st row
            pip1 = matsz-1                                                      # making cipher to go to last row
        if pip2<0:
            pip2 = matsz-1
        pnls.append(arr[c1p1][pip1])
        pnls.append(arr[c2p1][pip2])
    if c1p2 == c2p2:
        pip1 = (c1p1-1)
        pip2 = (c2p1-1)
        if pip1<0:                                                              # Checking if cipher is any row of 1st column
            pip1 = matsz-1                                                      # making cipher to go to last column
        if pip2<0:
            pip2 = matsz-1
        pnls.append(arr[pip1][c1p2])
        pnls.append(arr[pip2][c2p2])
    elif citxt[cid1]!=citxt[cid2] and c1p1!=c2p1 and c1p2!=c2p2:
        pip1 = c2p2
        pip2 = c1p2
        pnls.append(arr[c1p1][pip1])
        pnls.append(arr[c2p1][pip2])
    cid1 +=2
    cid2 +=2
decpntxt = ''.join(pnls)                                                    # Decrypted Plain text
did1,did2 = 0,1
while did2<len(decpntxt):
    if did2+1>=len(decpntxt):
        break
    if decpntxt[did1]==decpntxt[did2+1] and decpntxt[did2]=='?':            # Checking for filler '?'
        firmls = list(decpntxt)
        firmls.pop(did2)
        decpntxt=''.join(firmls)
    did1+=2
    did2+=2
#print ('Plain Text after Decrypt>>> ',decpntxt)
#print ('Original Plain txt>>> ',orgpltxt)
if len(decpntxt)!=len(orgpltxt):
    lcrls = list(decpntxt)
    lcrls.pop()
    decpntxt = ''.join(lcrls)
print ('Plain Text after check>>> ',decpntxt)
