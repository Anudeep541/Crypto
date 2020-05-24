'''
Created by Jane1729 on 23-05-2020
'''

# <----------   Program to encrypt or decrypt text with all possible ROT combos or using given key    ---------->

## Function to select the user key or generate al possible combos ##

def user_choice():
    print ('1. Use your key\n2. Print all possible rotation ciphers')
    choice = input('What do you want to do: ')
    if choice < '1' or choice > '2':
        print ('Please select only from given options')
        user_choice()
    else:
        return choice

## Function to select between Encryption and Decryption ##

def select():
    print ('1. Encrypt\n2. Decrypt')
    selection = input('Select any of the given: ')

    ### Checking the input is valid or not ###
    if selection < '1' or selection > '2':
        print ('Please select only from given options')
        select()
    else:
        choice_opted = user_choice()
        if choice_opted == '1':
            user_key = int(input('Enter your key: '))
        else:
            user_key = None
        return selection, user_key

## Function to encrypt the given message ##

def encrypt(rot_key):
    print ('Please enter plaintext to encrypt')
    pltxt = input().lower()

    ### Checking if the entered text is only of alphabets with space allowed ###
    for indx in pltxt:
        if (ord(indx)<97 or ord(indx)>122) and ord(indx)!=32:
            print ('This program only works on alphabets')
            encrypt()
    
    ### Generating all possible combos ###
    if rot_key == None:
        for rotatn in range(1,26):
            ciphrtxt = ''
            for alphbt in pltxt:
                if alphbt == ' ':
                    ciphrtxt = ciphrtxt + ' '
                else:
                    shift = ord(alphbt)+rotatn
                    if shift > 122:
                        shift -= 26
                    ciphrtxt = ciphrtxt + chr(shift)
            print ('ROT',rotatn,'>>> ',ciphrtxt)
    
    ### Using provided key ###
    else:
        ciphrtxt = ''
        for alphbt in pltxt:
            if alphbt == ' ':
                ciphrtxt = ciphrtxt + ' '
            else:
                shift = ord(alphbt)+rot_key
                if shift > 122:
                    shift -= 26
                ciphrtxt = ciphrtxt + chr(shift)
        print ('ROT',rot_key,'>>> ',ciphrtxt)

## Function to decrypt the given ciphertext ##

def decrypt(rot_key):
    print ('Please enter ciphertext to decrypt')
    cipher = input().lower()

    ### Checking if the entered text is only of alphabets with space allowed ###
    for indx in cipher:
        if (ord(indx)<97 or ord(indx)>122) and ord(indx)!=32:
            print ('This program only works on alphabets')
            decrypt()
    
    ### Generating all possible combos ###
    if rot_key == None:
        for rotatn in range(1,26):
            decrypt_pltxt = ''
            for alphbt in cipher:
                if alphbt == ' ':
                    decrypt_pltxt = decrypt_pltxt + ' '
                else: 
                    shift = ord(alphbt)-rotatn
                    if shift < 97:
                        shift += 26
                    decrypt_pltxt = decrypt_pltxt + chr(shift)
            print ('ROT',rotatn,'>>> ',decrypt_pltxt)
    
    ### Using provided key ###
    else:
        decrypt_pltxt = ''
        for alphbt in cipher:
            if alphbt == ' ':
                decrypt_pltxt = decrypt_pltxt + ' '
            else: 
                shift = ord(alphbt)-rot_key
                if shift < 97:
                    shift += 26
                decrypt_pltxt = decrypt_pltxt + chr(shift)
        print ('ROT',rot_key,'>>> ',decrypt_pltxt)

opt,key = select()

if opt == '1':
    encrypt(key)

if opt == '2':
    decrypt(key)
