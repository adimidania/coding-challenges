'''
You are given an m x n matrix mat and two integers r and c representing the number of rows
and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in 
the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output 
the new reshaped matrix; Otherwise, output the original matrix.
'''
# Let's go with my naive solution
def matrixReshape(mat, r, c):
    m = len(mat)
    n = len(mat[0])
    reshaped = []
    if(r*c != m*n):
        return mat
    else:
        p = 0
        k = 0
        for _ in range(r):
            row = []
            while(len(row) !=c):
                row.append(mat[p][k])
                k = k + 1
                if(k == n):
                    k = 0
                    p = p + 1
            reshaped.append(row)
    return reshaped

# Another solution from LeetCode!
def matrixReshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    # Check for validity of reshape
    if (m * n != r * c) or (m == r and n == c):
        return mat
    # Create output matrix
    out = []
    # Flatten the matrix, let it be a row
    M_flat = []
    for row in mat:
        M_flat += row
        
    # Populate rows with c elements taken sequentially from the flattened matrix, then add the row to the output matrix
    # Once complete the output matrix will have r rows consisting of c elements with the same row-traversing order as mat, as was desired
    while len(M_flat) > 0:
        row = []
        for i in range(c):
            x = M_flat.pop(0)
            row.append(x)
        out.append(row)
    
    return out 