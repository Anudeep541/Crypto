'''
Created by Jane1729 on 25-05-2020
'''

## <---------- SCYTALE CIPHER ----------> ##

def select():
    print ('1. Encrypt\n2. Decrypt')
    selection = input('Select any of the given: ')

    ### Checking the input is valid or not ###
    if selection < '1' or selection > '2':
        print ('Please select only from given options')
        select()
    return selection

### Funciton to define Cylinder diameter and number of turns ###
def rows_columns():
    no_of_rows = int(input('Enter diameter of cylinder(rows): '))
    no_of_columns = int(input('Enter number of turns(columns): '))
    return no_of_rows,no_of_columns

### Function to check if entered text is greater than cylinder dimensions ###
def len_check(text,r,c):
    matrx_size = r*c
    if len(text) > matrx_size:
        return False

### Function to encrypt the data ###
def encrypt(rows,columns):
    matrx_size = rows*columns
    msg_indx = 0
    cylinder = [[0 for i in range(columns)] for j in range(rows)]
    message = input('Enter message to encrypt: ').replace(" ","")
    bol = len_check(message,rows,columns)

    #### If message length is grater than cylinder dimensions then re-enter ###
    if bol == False:
        print ('Please enter text whose length is less than or equal to cylinder size')
        encrypt(rows,columns)
    
    #### Insering filler (here '☻') if message is less than cylinder dimensions and filling the cylinder and reading out encrypted text ####
    else:
        if len(message) < matrx_size:
            for var in range(matrx_size-len(message)):
                message += '☻'
        for r1 in range(rows):
            for c1 in range(columns):
                cylinder[r1][c1] = message[msg_indx]
                msg_indx +=1
        ciphrtxt = ''
        for c2 in range(columns):
            for r2 in range(rows):
                ciphrtxt += cylinder[r2][c2]
        print("Cipher Text: ",ciphrtxt)

### Function to decrypt the data ###
def decrypt(rows,columns):
    matrx_size = rows*columns
    ciph_indx = 0
    cylinder = [[0 for i in range(columns)] for j in range(rows)]
    cipher = input('Enter cipher to decrypt: ')
    bol = len_check(cipher,rows,columns)

    #### If message length is grater than cylinder dimensions then re-enter ###
    if bol == False:
        decrypt(rows,columns)
    
    #### Removing filler (here '☻') and filling the cylinder and reading out plaintext ####
    else:
        for c1 in range(columns):
            for r1 in range(rows):
                cylinder[r1][c1] = cipher[ciph_indx]
                ciph_indx +=1
        pltxt = ''
        for r2 in range(rows):
            for c2 in range(columns):
                pltxt += cylinder[r2][c2]
        pltxt_nofill = pltxt.replace('☻','')
        print("Plain Text: ",pltxt_nofill.upper())

opt = select()

if opt == '1':
    rows, columns = rows_columns()
    encrypt(rows,columns)

if opt == '2':
    rows, columns = rows_columns()
    decrypt(rows, columns)
