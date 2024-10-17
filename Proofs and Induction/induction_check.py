end = 5             #intro to Proofs and Induction
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

a = -1                  #applications of Induction
n = 0
b = n ** 2

if a == b:
  print('True')
else:
  print('False')
  
  
x = 1                   #Induction: Base Case
if x <= x ** 2:
    k = x
print(k)


k = 9                   #Induction: Induction Hypothesis
s = 0
for i in range(1, k + 1): #Proving the Inductive Step add one to k to get "True" again
    s += 2 * i - 1
print(s)
print(s == k ** 2)


k = 0                   #Strong Induction: Multiple Base Cases
k += k + 1
first = k
k += k
second = k
k += k - 1
third = k
print(first, second, third)


k = 10                 #Strong Induction: Induction Hypothesis
s = k + 1 + k + k - 1
print(s)
print(s == k * 3)


