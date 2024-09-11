def dynamic_knapsack(weight_cap, weights, values):
    rows = len(weights) + 1
    cols = weight_cap + 1

    matrix = [[] for x in range(rows)]

    for index in range(rows):
        matrix[index] = [ -1 for y in range(cols)]
    
        for weight in range(cols):
            if index == 0 or weight == 0:
                matrix[index][weight] = 0
            elif weights[index - 1] <= weight:
                matrix[index][weight] = max(values[index - 1] + matrix[index - 1][weight - weights[index - 1]], matrix[index -1][weight])
            else:
                matrix[index][weight] = matrix[index - 1][weight]
    return matrix[rows - 1][weight_cap]

values = [50, 100, 150, 200]
weights = [8, 16, 32, 40]
weight_cap = 64

print(dynamic_knapsack(weight_cap, weights, values))