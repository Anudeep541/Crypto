'''
Created by Jane1729                 23-05-19
'''
# <<<<< Ceaser Cipher >>>>>

#######
# First Ver
#######

enc = input('Enter data to encode>>>')
els = []

## Encrypt
for i in enc:
    n = ord(i)
    print (n)
    n = n+3
    if n>90 and n<94:
        n = n - 26
    if n>122:
        n = n - 26
    se = chr(n)
    els.append(se)
print (''.join(els))

dec = input('Enter data to decode>>>')
dls = []

## Decrypt
for j in dec:
    d = ord(j)
    print (d)
    d = d-3
    if d>65 and d<97:
        d = d+26
    if d>32 and d<65:
        d = d+26
    sd = chr(d)
    dls.append(sd)
print (''.join(dls))

#######
# Second Ver
#######

# A - 65, Z- 90, a - 97, z - 122, ' '-32, '#'-35
###
# Encrypt
###
print ('Hi!This is example for Ceaser Cipher')
print ('Please enter your key between 1 and 26 to continue:')
k = int(input())
enc = input('Enter data to encode>>>')
els = []
for i in enc:
    u = ord(i)
    u = u+k
    if u>90 and u<=97:                                       # Checks if letter is greater than 'Z' and less than 'a'
        u = u-26
    if u>122:                                               # Checks if letter is greater than 'z'
        u = u-26
    els.append(chr(u))
print (''.join(els))
###
# Decrypt
###
dec = input('Enter data to decode>>>')
dls = []
for i in dec:
    v = ord(i)
    v = v-k
    if v<65 and  v>=65-k:                                       # Checks if letter is less than 'A' and 'a'
        v = v+26
    if v>=97-k and v<97:
        v = v+26
    dls.append(chr(v))
print (''.join(dls))
