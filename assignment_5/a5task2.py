# 
# a5task2.py - Assignment 5, Task 2
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#

from a5task1 import *

# function add_matrices(A, B)
def add_matrices(A, B):
    """ this function takes as parameters 2 matrices (2d lists) and returns 
        a new matrix which is the element-wise sum of the matrices A and B.
        
        input A: a matrix
        input B: a matrix
    """
    # validate the dimensions of the matrices
    assert len(A) == len(B) and len(A[0]) == len(B[0]), \
        f"Incompatible dimensions: cannot add ({len(A)},{len(A[0])}) with ({len(B)},{len(B[0])})!"
    # create a new matrix that is the element-wise sum of A and B
    return [[sum(x) for x in zip(a_row, b_row)] for a_row, b_row in zip(A, B)]

# function sub_matrices(A, B)
def sub_matrices(A, B):
    """ this function takes as parameters 2 matrices (2d lists) and returns 
        a new matrix which is the element-wise difference of the matrices A and B.
        
        input A: a matrix
        input B: a matrix
    """
    # validate the dimensions of the matrices
    assert len(A) == len(B) and len(A[0]) == len(B[0]), \
        f"Incompatible dimensions: cannot subtract ({len(A)},{len(A[0])}) from ({len(B)},{len(B[0])})!"
    # create a new matrix that is the element-wise difference of A and B
    return [[a - b for a, b in zip(a_row, b_row)] for a_row, b_row in zip(A, B)]

# function mult_scalar(M, s)
def mult_scalar(M, s):
    """ this function takes as a parameter a 2-dimension list M (the matrix) 
        and a scalar value s (i.e., an int or float), and returns a new matrix 
        containing the values of the original matrix multiplied by the scalar value.
        
        input M: a matrix
        input s: any number(int or float)
    """
    # create a new matrix that is the original matrix multiplied by the scalar
    return [[s * element for element in row] for row in M]

# function dot_product(M, N)
def dot_product(M, N):
    """ this function takes as parameters two matrices M and N, and returns 
        a new matrix containing dot product of these matrices.

        input M: a matrix
        input N: a matrix
    """
    # validate the dimensions of the matrices
    assert len(M[0]) == len(N), \
        f"Incompatible dimensions: cannot dot-product ({len(M)},{len(M[0])}) with ({len(N)},{len(N[0])})!"
    # create a new matrix that is the dot product of M and N
    return [[sum(a * b for a, b in zip(m_row, n_col)) for n_col in zip(*N)] for m_row in M]

# function create_sub_matrix(M, exclude_row, exclude_col)
def create_sub_matrix(M, exclude_row, exclude_col):
    """ this function returns a sub-matrix of M, with all values that are not 
        in row exclude_row or column exclude_col.

        input M: a matrix
        input exclude_row: any number(int)
        input exclude_col: any number(int)
    """
    
    return [[M[i][j] for j in range(len(M[i])) if j != exclude_col] for i in range(len(M)) if i != exclude_row]

# function determinant(M)
def determinant(M):
    """ this function returns takes a parameter M that is a (non-singular) 
        matrix, and returns its determinant. The “Laplace expansion” method of 
        calculating a determinant is a simple recursive algorithm.

        input M: a matrix
    """
    # Check if M is a square matrix
    assert len(M) == len(M[0]), f"Incompatible dimensions: ({len(M)},{len(M[0])})!"

    # If M is a 1x1 matrix, return the scalar value
    if len(M) == 1:
        return M[0][0]

    # If M is a 2x2 matrix, return the determinant
    if len(M) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]

    # If M is larger than 2x2, calculate the determinant using the Laplace expansion
    det = 0
    for col in range(len(M[0])):
        sub_matrix = create_sub_matrix(M, 0, col)
        det += ((-1) ** col) * M[0][col] * determinant(sub_matrix)
    return det

# function matrix_of_minors(M)
def matrix_of_minors(M):
    """ this function takes a matrix and returns the corresponding matrix 
        of minors.

        input M: a matrix
    """
    # Check if M is a square matrix
    assert len(M) == len(M[0]), f"Incompatible dimensions: ({len(M)},{len(M[0])})!"
    
    minors = []
    for i in range(len(M)):
        minor_row = []
        for j in range(len(M[0])):
            sub_matrix = create_sub_matrix(M, i, j)
            minor = determinant(sub_matrix)
            minor_row.append(minor)
        minors.append(minor_row)
    return minors

# function inverse_matrix(M)
def inverse_matrix(M):
    """ this function takes a parameter that is a (non-singular) matrix, and 
        returns its inverse.

        input M: a matrix
    """
    # Step 1: Calculate the determinant of matrix M.
    det = determinant(M)
    
    # Check if the matrix is singular
    assert det != 0, "Matrix is singular!"
    
    # Step 2: Compute the matrix of minors.
    minors = matrix_of_minors(M)
    
    # Step 3: Generating the cofactor matrix
    cofactors = [[((-1) ** (i + j)) * minors[i][j] for j in range(len(M[0]))] for i in range(len(M))]
    
    # Step 4: Transpose the cofactor matrix to get the adjugate matrix.
    adjugate = list(map(list, zip(*cofactors)))  # Transposing the matrix
    
    # Step 5: Divide every element of the adjugate matrix by the determinant.
    inverse = [[adjugate[i][j] / det for j in range(len(M[0]))] for i in range(len(M))]
    
    return inverse


if __name__ == '__main__':

    # sample test call for add_matrices(A, B)
    A = [[1,2,3],[4,5,6]]
    B = [[4,5,6],[1,2,3]]
    S = add_matrices(A, B)
    print_matrix(S, 'S')
    
    A = [[1,2],[4,5]]
    B = [[4,3,2],[3,2,1]]
    S = add_matrices(A,B)
    
    # sample test call for sub_matrices(A, B)
    A = [[1,2,3],[4,5,6]]
    B = [[4,5,6],[1,2,3]]
    D = sub_matrices(A, B)
    print_matrix(D, 'D')
    
    A = [[1,2],[4,5]]
    B = [[4,3,2],[3,2,1]]
    S = sub_matrices(A,B)
    
    # sample test call for mult_scalar(M, s)
    A = [[3,0,2,1],[2,0,-2,3]]
    print_matrix(A)
    B = mult_scalar(A, 3)
    print_matrix(B)
    
    # sample test call for dot_product(M, N)
    A = [[1,2,3],[4,5,6]]
    print_matrix(A)
    B = [[3,2],[4,1],[5,0]]
    print_matrix(B)
    P = dot_product(A,B)
    print_matrix(P, 'P')
    
    A = [[1,2,3],[4,5,6]]
    B = [[4,3,2],[3,2,1]]
    P = dot_product(A,B)
    
    # sample test call for function create_sub_matrix(M, exclude_row, exclude_col)
    A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print_matrix(A)
    print_matrix(create_sub_matrix(A, 0, 0)) # exclude row 0 and column 0
    print_matrix(create_sub_matrix(A, 2, 3)) # exclude row 2 and column 3
    
    
    # sample test call for function determinant(M)
    A = [[3,4],[8,6]]
    d = determinant(A)
    print(d)

    B = [[2,-1,0],[3,-5,2], [1,4,-2]]
    d = determinant(B)
    print(d)

    # a 4x4 matrix example 
    C = [[3, 2, 0, 1], [4, 0, 1, 2], [3, 0, 2, 1], [9, 2, 3, 1]]
    d = determinant(C)
    print(d)
    
    A = [[3]]
    determinant(A)
    
    A = [[3,4],[8,6], [10,7]]
    determinant(A)
    
    # sample test call for function matrix_of_minors(M)
    A = [[3,0,2],[2,0,-2],[0,1,1]]
    print_matrix(A, 'A')
    M = matrix_of_minors(A)
    print_matrix(M)
    
    # sample test call for function inverse_matrix(M)
    A = [[7,8],[9,10]]
    print_matrix(A)
    determinant(A)
    AI = inverse_matrix(A)
    print_matrix(AI)
    # check that we have the correct inverse; A * AI should be the identity matrix
    DP = dot_product(A,AI)
    print_matrix(DP, 'DP')
    
    A = [[3,0,2],[2,0,-2],[0,1,1]]
    print_matrix(A)
    determinant(A)
    AI = inverse_matrix(A)
    print_matrix(AI)
    # check that we have the correct inverse; A * AI should be the identity matrix
    DP = dot_product(A,AI)
    print_matrix(DP, 'DP')
    
    A = [[3,2,0,1],[4,0,1,2],[3,0,2,1],[9,2,3,1]]
    print_matrix(A)
    determinant(A)
    AI = inverse_matrix(A)
    print_matrix(AI)
    # check that we have the correct inverse; A * AI should be the identity matrix
    DP = dot_product(A,AI)
    print_matrix(DP, 'DP')
    









