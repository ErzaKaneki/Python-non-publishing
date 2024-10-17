import math
def decimal_to_binary(number):
    binary = []
    while number > 0:
        bnum = number % 2
        number = math.floor(number / 2)
        binary.insert(0, bnum)
        
    binary_num = "".join(map(str, binary))
    print("0b" + str(binary_num))
    
decimal_to_binary(8391)