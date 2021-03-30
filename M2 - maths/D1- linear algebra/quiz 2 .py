#quiz 2
#Q1

import sympy
import numpy as np
matrix = np.array([
    [1, 2, 3],
    [2, 2, 2],
    [8, 8, 8]
])

_, indexes = sympy.Matrix(matrix).T.rref()
print(indexes)

print(matrix[indexes,:])

if len(indexes) == 2:
    print("linearly independant")
else:
    print("linearly dependant")


#Q2

# since 2a+3b = -1 and 10a+15b = -5 they are on the same plane and linearly dependent. this means that there are an  infinite amount of numbers you could put intot his and will give the correct answer. If they were linearly independent and crossed at one point then we could solve for a and b

#Q3
# -a +3b = 1
# -a +3b = 5
# This is the opposite of the previous question as there is no way that these two lines ever cross so there is no solution at all.

