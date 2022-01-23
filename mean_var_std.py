
'''
Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean,
variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits.
The function should convert the list into a 3 x 3 Numpy array,
and then return a dictionary containing the mean, variance, standard deviation, max, min,
and sum along both axes and for the flattened matrix.

If a list containing less than 9 elements is passed into the function,
it should raise a ValueError exception with the message: "List must contain nine numbers."

The values in the returned dictionary should be lists and not Numpy arrays.
'''

import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    A = np.array([list[0:3],
                      list[3: 6],
                      list[6:9]])

    mean = [A.mean(axis=0), A.mean(axis=1), A.mean()]
    var = [A.var(axis=0), A.var(axis=1), A.var()]
    s_d = [A.std(axis=0), A.std(axis=1), A.std()]
    max = [A.max(axis=0), A.max(axis=1), A.max()]
    min = [A.min(axis=0), A.min(axis=1), A.min()]
    sum = [A.sum(axis=0), A.sum(axis=1), A.sum()]



    calculations = {
          'mean': mean,
          'variance': var,
          'standard deviation': s_d,
          'max': max,
          'min': min,
          'sum': sum
        }
    for key in calculations.keys():
        for i in range(2):
            calculations[key][i] = calculations.get(key)[i].tolist()



    print(calculations)

list = [i for i in range(9)]
calculate(list)

