import math

def binary_to_decimal(binary):
    dec_list = []
    decimal = 0
    i = 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
        dec_list.insert(0, decimal)
    return dec_list[0]
        
def decimal_to_octal(decimal):
    octal = []
    while decimal > 0:
        dnum = decimal % 8
        decimal = math.floor(decimal / 8)
        octal.insert(0, dnum)
        
    octal_num = "".join(map(str, octal))
    print("0o" + str(octal_num))
    
decimal_to_octal(binary_to_decimal(1100111000))