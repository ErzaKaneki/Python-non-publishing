def two_d_list(n, m, figures):
    matrix = [[0 for _ in range(m)]for _ in range(n)]
    
    if figures[0] == 'D':
        d_value = 1
        p2m = [(0, 0), (1, 0), (2, 0), (1, 1)]
        for row, col in p2m:
            matrix[row][col] = d_value
    if figures[1] == 'B':
        b_value = 2
        p2m = [(3, 0), (3, 1), (3, 2), (2, 1)]
        for row, col in p2m:
            matrix[row][col] = b_value
    if figures[2] == 'A':
        a_value = 3
        p2m = [(3, 3)]
        for row, col in p2m:
            matrix[row][col] = a_value
    if figures[3] == 'C':
        c_value = 4
        p2m = [ (1, 2), (1, 3), (2, 2), (2, 3)]
        for row, col in p2m:
            matrix[row][col] = c_value
    if figures[4] == 'E':
        e_value = 5
        p2m = [(0, 1), (0, 2), (0, 3)]
        for row, col in p2m:
            matrix[row][col] = e_value
    for row in matrix:
        print(row)

two_d_list(4, 4, ['D', 'B', 'A', 'C', 'E'])