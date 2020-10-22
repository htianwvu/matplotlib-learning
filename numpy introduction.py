import numpy as np

array = np.array([1,2,3])
print(array)
print(type(array))

#shape
print(array.shape)
print(array[0],array[1])
arry[0] = -1
print(array)



# muti-array

mult_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mult_array)
print(mult_array.shape)

# create a ew array with 0 or 1
zeros_array = np.zeros((3,4))
one_array = np.ones((5,6))
print(zeros_array)
print(one_array)


# extract a element from array

print("extract element", mult_array[0][2])
print('extract element from first row', mult_array[0,:])
print('extract element from the third column', mult_array[:,2])

## array operation

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array2 = np.array([[7,8,9],[10,11,12],[13,14,15]])

# operations

print("addition", array1+array2)
print('substraction', array1-array2)
print('multification', array1*array2)
print('division', array1/array2)

# array operations

print("dot multification", array1.dot(array2) )

