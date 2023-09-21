from sympy import var
var('filename mdict do_compression')


import numpy as np
from scipy import io

# Exporting Data in Matlab Format

filename # - the file name for saving data.
mdict # - a dictionary containing the data.
do_compression # - a boolean value that specifies whether to compress the result or not. Default False.

arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})

# Import Data from Matlab Format

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])


io.savemat('arr.mat', {"vec": arr}) # Export:

mydata = io.loadmat('arr.mat') # Import:

print(mydata)

# Another example

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

io.savemat('arr.mat', {"vec": arr}) # Export:

mydata = io.loadmat('arr.mat') # Import:

print(mydata['vec'])

# Another example

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])


io.savemat('arr.mat', {"vec": arr}) # Export:


mydata = io.loadmat('arr.mat', squeeze_me=True) # Import:

print(mydata['vec'])

