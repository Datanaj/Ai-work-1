#Quiz 1

#Q1
import numpy as np

def magnitude_complete(a,b,c,d,e):
    return np.linalg.norm([a,b,c,d,e])



#print (magnitude_complete(1,2,3,4,5))

#Q2

def magnitude_vectors(a,b):
    v = a+b
    return np.linalg.norm(v)


a = np.array([5, 1])
b = np.array([-4,-1])

#print (magnitude_vectors(a, b))

#Q3

def alpha_magnitude(alpha, b):
    #returns the resulting magnitude, if the direction has changed and what has happened to the vector
    b = np.array(b)
    vector = alpha * b
    if np.sign(b[0]) == np.sign(vector[0]):
        print('No directional change')
    else:
        print('The direction has changed 180 degrees')
    return (vector, np.linalg.norm(vector))