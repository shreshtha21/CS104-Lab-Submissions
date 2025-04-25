'''
    NumPy and The Matrix
'''

import numpy as np

def task1(matrix):
    '''return the upper diagonal matrix in column-wise fashion'''
    matrix2 = matrix.copy()
    matrix2 = matrix2.transpose()
    for i in range(0,5):
        for j in range(i+1,5):
            matrix2[i,j]=0
    return matrix2

def task2(matrix):
    '''return mean, median, std (precision 2), all along x, determinant, inverse, pseudo-inverse'''
    mean = np.round(np.mean(matrix, axis=0), 2)
    median = np.round(np.median(matrix, axis=0), 2)
    std = np.round(np.std(matrix, axis=0), 2)
    det = round(np.linalg.det(matrix), 2)
    if det != 0:
        inv = np.round(np.linalg.inv(matrix), 2)
    else:
        inv = None
    pseudoinv = np.round(np.linalg.pinv(matrix), 2)
    return mean, median, std, det, inv, pseudoinv

def task3(matrix, num = 0, padding = 3):
    '''return the padded matrix'''
    matrix3 = matrix.copy()
#ye na bhi likhe toh chlega, koi kaam ka ni h
    for i in range(0,padding):
        for j in range(0,matrix3.shape[0]):
            matrix3[i,j] = num
    for i in range(matrix3.shape[1]-padding, matrix3.shape[1]):
        for j in range(0,matrix3.shape[0]):
            matrix3[i,j] = num
    for i in range(padding, matrix3.shape[1]-padding):
        for j in range(0,padding):
            matrix3[i,j] = num
        for j in range(matrix3.shape[0]-padding, matrix3.shape[0]):
            matrix3[i,j] = num
#yaha tk
    return np.pad(matrix, pad_width=padding, mode='constant', constant_values=num)

if __name__ == '__main__':

    matrix = np.array([
        [5,5,84,3,9],
        [6,11,1,55,58],
        [1,20,48,12,36],
        [8,4,41,93,98],
        [6,17,64,0,13]
    ])

    # you can call the functions here
    # Uncomment the following lines to test your code

    # TASK 1
print(task1(matrix))
    # TASK 2
mean, median, std, det, inv, pseudoinv = task2(matrix)
print("Mean: ", mean)
print("Median: ", median)
print("Standard Deviation: ", std)
print("Determinant: ", det)
print("Inverse: ", inv)
print("Pseudo-Inverse: ", pseudoinv)
    # TASK 3
print(task3(matrix)) # default padding