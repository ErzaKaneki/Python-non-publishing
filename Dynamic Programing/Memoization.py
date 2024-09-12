memo = {}

def fibonacci(num):
    answer = None

    if num in memo:
        return memo[num]
    else:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            memo[num] = fibonacci(num -1) + fibonacci(num - 2)
            return memo[num]
        
print(fibonacci(20))
print(fibonacci(200))        