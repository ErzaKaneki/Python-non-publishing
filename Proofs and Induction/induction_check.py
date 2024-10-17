end = 5
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

a = -1
n = 0
b = n ** 2

if a == b:
  print('True')
else:
  print('False')
  
  
x = 1
if x <= x ** 2:
    k = x
print(k)