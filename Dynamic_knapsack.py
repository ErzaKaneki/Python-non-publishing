def dynamic_knapsack(weight_cap, weights, values):
    rows = len(weights) + 1
    cols = weight_cap + 1

    matrix = [[] for x in range(rows)]

    for index in range(rows):
        matrix[index] = [ -1 for y in range(cols)]
    
        for w in range(cols):
            if index == 0 or w == 0:
                matrix[index][w] = 0
            elif weights[index - 1] <= w:
                matrix[index][w] = max(values[index - 1] + matrix[index - 1][w - weights[index - 1]], matrix[index -1][w])
            else:
                matrix[index][w] = matrix[index - 1][w]
    return matrix[rows - 1][weight_cap]

values = [50, 100, 150, 200]
weights = [8, 16, 32, 40]
weight_cap = 64

print(dynamic_knapsack(weight_cap, weights, values))