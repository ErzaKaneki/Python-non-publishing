end = 4
x = 1
counter = 0
guess = 0
while counter < end:
    if x % 2 > 0:
        guess += x
        counter += 1
        x += 1
    else:
        x += 1
print(guess)    