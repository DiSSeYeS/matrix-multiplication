def matrix_mupltiplication():
    n, m = [int(c) for c in input('Select size of 1st matrix(n m): ').split()]
    matrix1, matrix2, res = [], [], []
    for i in range(n):
        matrix1.append([int(c) for c in input(f'Select {i+1} row of matrix: ').split()])
    
    print()    
    
    m, k = [int(c) for c in input('Select size of 2nd matrix(m k): ').split()]
    for i in range(m):
        matrix2.append([int(c) for c in input(f'Select {i+1} row of matrix: ').split()])
        
    for _ in range(n):
        temp = []
        for i in range(k):
            temp.append(0)
        res.append(temp)
    for i in range(k):
        for j in range(n):
            for x in range(m):
                res[i][j] += matrix1[i][x] * matrix2[x][j]
    print('A x B = ')        
    for c in res:
        for k in c:
            print(str(k).ljust(3), end = ' ')
        print()
        
def matrix_step_multiplication():    
    n = int(input('Select size of matrix: '))
    matrix1, res = [], []
    for i in range(n):
        matrix1.append([int(c) for c in input(f'Select {i+1} row of matrix: ').split()])
    deg = int(input('Select degree of matrix: ')) 
    for _ in range(n):
        temp = []
        for i in range(n):
            temp.append(0)
        res.append(temp)
    const_matrix = matrix1
    for _ in range(deg-1):
        for i in range(n):
            for j in range(n):
                for x in range(n):
                    res[i][j] += matrix1[i][x] * const_matrix[x][j]
        matrix1 = res.copy()
        res.clear()
        for _ in range(n):
            temp = []
            for i in range(n):
                temp.append(0)
            res.append(temp)
    print(f'A^{deg} = ')   
    for c in matrix1:
        for k in c:
            print(str(k).ljust(3), end = ' ')
        print()

while True:
    op = input('Select operation (m_deg, m_mult): ').lower()
    if op == 'm_deg':
        matrix_step_multiplication()
    elif op == 'm_mult':
        matrix_mupltiplication()
    else:
        print('Operation is not found :(')
