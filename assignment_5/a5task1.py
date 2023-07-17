# 
# a5task1.py - Assignment 5, Task 1
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#

# function print_matrix(m, label)
def print_matrix(m, label=''):
    """ this function  takes two parameters, m which is a 2-dimension list 
    (the matrix) and label (a string), and creates a nicely-formatted printout.
        
        input m: a 2-dimension list
        input label: a string
    """
    if label:
        print(label, '=')
        
    print('[', end='')
    i = 0
    print('[', end='')
    for j in range(len(m[i])):
        if j != len(m[i]) - 1:
            print(f'{m[i][j]:.2f}', end=', ')
        else:
            print(f'{m[i][j]:.2f}', end='')
            print(']')
            
    for i in range(1,len(m)):
        if i != len(m) - 1:
            print(' [', end='')
            for j in range(len(m[i])):
                if j != len(m[i]) - 1:
                    print(f'{m[i][j]:.2f}', end=', ')
                else:
                    print(f'{m[i][j]:.2f}', end='')
                    print(']')
        else:
            print(' [', end='')
            for j in range(len(m[i])):
                if j != len(m[i]) - 1:
                    print(f'{m[i][j]:.2f}', end=', ')
                else:
                    print(f'{m[i][j]:.2f}', end='')
                    print(']]')
    print()
    
# function zeros(n, m)
def zeros(n, m=None):
    """ this function creates and returns an n * m matrix containing all zeros.
        input n: any number(int)
        input m: any number(int)
    """
    if m is None:  # if m is not provided, make it equal to n
        m = n
    return [[0 for _ in range(m)] for _ in range(n)]

# function identity_matrix(n)
def identity_matrix(n):
    """ this function creates and returns an n * n identity matrix containing 
        the value of 1 along the diagonal.
        input n: any number(int)
    """
    matrix = zeros(n)  # create an n by n matrix with all zeros
    for i in range(n):  # set the diagonal elements to 1
        matrix[i][i] = 1
    return matrix

# function transpose(M)
def transpose(M):
    """ this function creates and returns the transpose of a matrix.
        input M: a matrix
    """
    # create a new matrix with dimensions reversed
    transposed = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    return transposed

# function swap_rows(M, src, dest)
def swap_rows(M, src, dest):
    """ this function perform the elementary row operation that exchanges two 
        rows within the matrix. This function will modify the matrix M such 
        that its row order has changed, but none of the values within the rows 
        have changed.
        
        input M: a matrix
        input src: any number(int)
        input dest: any number(int)
    """
    # validate the row indices
    if not (0 <= src < len(M) and 0 <= dest < len(M)):
        raise ValueError("Both src and dest must be valid row indices.")
    # swap the rows
    M[src], M[dest] = M[dest], M[src]
 
# function mult_row_scalar(M, row, scalar)
def mult_row_scalar(M, row, scalar):
    """ this function perform the elementary row operation that multiplies all 
        values in the row row by the numerical value scalar.
        
        input M: a matrix
        input row: any number(int)
        input scalar: any number(int or float)
    """
    # validate the row index
    if not 0 <= row < len(M):
        raise ValueError("Row index must be valid and in-bounds for this matrix.")
    # multiply the row by the scalar
    M[row] = [scalar * element for element in M[row]]
    
# function mult_row_scalar(M, row, scalar)
def add_row_into(M, src, dest):
    """ this function  performs the elementary-row operation to add the src row
        into the dest row. That is, each element of row src is to be added into 
        the corresponding element of row dest.
        
        input M: a matrix
        input src: any number(int)
        input dest: any number(int)
    """
    # validate the row indices
    if not (0 <= src < len(M) and 0 <= dest < len(M)):
        raise ValueError("Both src and dest must be valid row indices.")
    # add the src row into the dest row
    M[dest] = [sum(x) for x in zip(M[dest], M[src])]
    
if __name__ == '__main__':

    # sample test call for function print_matrix(m, label)
    A = [[3,0,2,1],[2,0,-2,3]]
    print_matrix(A) # no label provided, so don't show a label
    print_matrix(A, 'A') # label of 'A' is provided, so the printout will show 'A = '
    
    # sample test call for zeros(n, m)
    print('print_matrix(zeros(3,2)) returns', print_matrix(zeros(3,2)))
    print('print_matrix(zeros(2,2)) returns', print_matrix(zeros(2,2)))
    print('print_matrix(zeros(3,5)) returns', print_matrix(zeros(3,5)))
    print('print_matrix(zeros(3)) returns', print_matrix(zeros(3)))


    # sample test call for identity_matrix(n)
    I = identity_matrix(3)
    print("print_matrix(I, 'I') returns", print_matrix(I, 'I'))
    
    # sample test call for transpose(M)
    A = [[1,2,3],[4,5,6]]
    print_matrix(A)
    AT = transpose(A)
    print_matrix(AT, 'AT')
    
    # sample test call for function swap_rows(M, src, dest)
    A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    print_matrix(A)
    swap_rows(A, 1, 2) # swap rows 1 and 2
    print_matrix(A)
    swap_rows(A, 0, 2)
    print_matrix(A)

    
    # sample test call for function mult_row_scalar(M, row, scalar)
    A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    print_matrix(A)
    mult_row_scalar(A, 1, -1) # multiply row 1 by -1
    print_matrix(A)
    mult_row_scalar(A, 1, 0.5) # multiply row 1 by 0.5
    print_matrix(A)

    # sample test call for mult_row_scalar(M, row, scalar)
    A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    print_matrix(A)
    add_row_into(A, 2, 1) # add row 2 into row 1
    print_matrix(A)
    add_row_into(A, 2, 1) # add row 2 into row 1
    print_matrix(A)
