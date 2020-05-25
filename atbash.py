'''
Created by Jane1729 on 25-05-2020
'''

## <---------- ATBASH CIPHER ----------> ##

'''
alphabets are broken down into two sections one is 'a-m' and other is 'o-z' and 
respective logics are used to convert for ATBASH
'''

def atbash_conv():
    print ('This program gives output of input text using ATBASH cipher')
    message = input("Enter your message: ").lower()
    for charac in message:
        if (ord(charac)<97 or ord(charac)>122) and ord(charac)!=32:
            print ('This program only works on alphabets')
            atbash_conv()
    convtxt = ''
    for character in message:
        if character == ' ':
            convtxt += ' '
        ### Check for letter 'n' and convert to 'm' ###
        elif ord(character) == 110:
            convtxt += chr(ord(character)-1)
        ### Logic used for set 'a-m' letters ###
        elif ord(character) < 110:
            convtxt += chr(ord(character)+((110-ord(character))*2-1))
        ### Logic used for set 'o-z' letters ###
        elif ord(character) > 110:
            convtxt += chr(ord(character)-((ord(character)-110)*2+1))
    print(convtxt.upper())

atbash_conv()