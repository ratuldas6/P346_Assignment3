def integerRound(x):
    from math import floor, ceil
    a = floor(x)
    b = ceil(x)
    if x-a<=.1:
        result = a
    elif b-x<=.1:
        result = b
    else:
        print("Please apply the function to a smaller difference")
    return result

def dec2Round(x):
    y = 100*x
    remainder = y%1
    y = y - remainder
    if remainder > 0.5:
        modified_digit = 1
    else:
        modified_digit = 0
    y = y + modified_digit
    y = y/100
    return y

def displayMatrix(matrix): #display given matrix
    for row in matrix:
        print(row)

def applyGJ(A,B): #function to apply GJ elim
    for k in range(len(B)): #rows are pivotted
        if abs(A[k][k]) < 1.0e-6: #defining upper limit for element = 0
            for i in range(k+1, len(B)): 
                if abs(A[i][k]) > abs(A[k][k]):     #swap check
                    for j in range(k, len(B)): 
                        A[k][j], A[i][j] = A[i][j], A[k][j] #obtaining swapped rows
                    B[k], B[i] = B[i], B[k] 
                    break
        A_kk = A[k][k]
        if A_kk == 0:        
            print("No distinct solution was found for this system of equations")
            return
        for j in range(k, len(B)): #column index of row is pivotted
            A[k][j] /= A_kk         #pivot row division for row ech form
        B[k] /= A_kk
        for i in range(len(B)):    #changed rows assigned new indices
            if i == k or A[i][k] == 0: continue
            factor = A[i][k]
            for j in range(k, len(B)): 
                #columns for subtraction assigned indices
                A[i][j] -= factor*A[k][j]
            B[i] -= factor * B[k]
    return B

def productMatrix(B,A): #finds product of two matrices
    try:               
        if  len(A) != len(B[0]): 
            print("Multiplication is undefined for given matrices!") 
        else:
            C = [[0 for i in range(len(A[0]))] for j in range(len(B))]
            for i in range(len(B)):       #rows of the matrix product.
                for j in range(len(A[0])):#columns of the matrix product.
                    for k in range(len(A)):
                        elem = dec2Round(B[i][k]*A[k][j])
                        C[i][j] += elem
            displayMatrix(C)
    except TypeError:
        print("Invalid entries found in matrix!")

def findDeterminant(A):     #determinant function for use in applyGJ()
    if len(A) != len(A[0]): #square matrix check
        print("Determinant is undefined for square matrices")
    else:
        count = 0
        for i in range(len(A) - 1): 
            if abs(A[i][i]) < 1.0e-6:
                for j in range(i+1 , len(A)): 
                    if  abs(A[i][i]) < abs(A[j][i]): 
                        for k in range(i , len(A)):
                            A[i][k], A[j][k] = A[j][k], A[i][k] #swapping the rows of the matrix.
                            count += 1
            for j in range(i+1 , len(A)):
                if A[j][i] == 0: continue 
                result = A[j][i]/A[i][i] #dividing the rows.
                for k in range(i , len(A)):
                    A[j][k] -= result*A[i][k]
        initial = 1
        for j in range(len(A)):
            initial *= A[j][j] #product of diagonal elements of matrix
        initial *= (-1)**count
        print(initial) 
'''
def inverseMatrix(A): #function for inverse matrix (3x3)
    M = [[ 0.00 for i in range(len(A))] for j in range(len(A))] 
    for i in range(3):
        for j in range(3):
            M[j][j] = 1.00
    for i in range(len(A)):
        A[i].extend(M[i])
    for k in range(len(A)):
        if abs(A[k][k]) < 1.0e-6: #GJ elim segment
            for i in range(k+1, len(A)):
                if abs(A[i][k]) > abs(A[k][k]):
                    for j in range(k,2*len(A)):
                        A[k][j], A[i][j] = A[i][j], A[k][j] #swap rows
                    break
        count = A[k][k] #element is pivotted
        if count == 0:  #checking if pivot = 0
            print("The matrix does not have a defined inverse")
            return
        else:
            for j in range(k, 2*len(A)): #pivotted row columns
                A[k][j] /= count
            for i in range(len(A)):      #substracted rows indiced
                if i == k or A[i][k] == 0: continue
                result = A[i][k] 
                for j in range(k, 2*len(A)): #columns for subtraction indiced
                    A[i][j] -= result*A[k][j]
    for i in range(len(A)):                     
        for j in range(len(A),len(A[0])):
            print("{:.2f}".format(A[i][j]), end = " ") 
            #to print upto 2 decimal places
        print()
'''
def inverseMatrix(A): #function for inverse matrix (3x3)
    M = [[ 0.00 for i in range(len(A))] for j in range(len(A))] 
    for i in range(3):
        for j in range(3):
            M[j][j] = 1.00
    for i in range(len(A)):
        A[i].extend(M[i])
    for k in range(len(A)):
        if abs(A[k][k]) < 1.0e-6: #GJ elim segment
            for i in range(k+1, len(A)):
                if abs(A[i][k]) > abs(A[k][k]):
                    for j in range(k,2*len(A)):
                        A[k][j], A[i][j] = A[i][j], A[k][j] #swap rows
                    break
        count = A[k][k] #element is pivotted
        if count == 0:  #checking if pivot = 0
            print("The matrix does not have a defined inverse")
            return
        else:
            for j in range(k, 2*len(A)): #pivotted row columns
                A[k][j] /= count
            for i in range(len(A)):      #substracted rows indiced
                if i == k or A[i][k] == 0: continue
                result = A[i][k] 
                for j in range(k, 2*len(A)): #columns for subtraction indiced
                    A[i][j] -= result*A[k][j]
                    
    A_inv = []
    
    for i in range(len(A)):
        blank_row = []
        for j in range(len(A),len(A[0])):
            blank_row.append(dec2Round(A[i][j]))
        A_inv.append(blank_row)
    return A_inv