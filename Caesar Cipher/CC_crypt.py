#get the plain text
#function to get the shift number
#funtion to shift the specific letter then all letters
def getPlainText():
    plaintext = input('Please enter your plain text: ')
    return plaintext

def getShiftNumber():
    shiftnumber = int(input('Please enter your shift number: '))
    return shiftnumber

def shiftAlphabets():
    x = getPlainText()
    y = getShiftNumber()
    v =''
    for i in x:
        ord_i = ord(i)
        if ord_i >64 and ord_i <92:
            v += chr(ord(i)+y)
    return v
    
print('WELCOME BOY!')
j = shiftAlphabets()
print(j)