import math

def hex_to_decimal(hex_value):
    return int(hex_value, 16)

def decimal_to_octal(decimal):
    octal = []
    while decimal > 0:
        dnum = decimal % 8
        decimal = math.floor(decimal / 8)
        octal.insert(0, dnum)
        
    octal_num = "".join(map(str, octal))
    print("0o" + str(octal_num))
    
decimal_to_octal(hex_to_decimal("0xDAD"))