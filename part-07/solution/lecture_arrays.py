# TODO: Create a 3-dimensional tensor with filled with zeros
# Choose the shape of the tensor, but it should have 200 elements
# Add the number 5 to all values of the tensor

# Your code here
import numpy as np

tensor = np.zeros((2,2,50))
tensor += 5
shape = tensor.shape()
dtype = tensor.dtype()
size = tensor.size()

print("Sum of tensor:", np.sum(tensor))

assert np.sum(tensor) == 1000

# TODO: Print the shape of the tensor using the method shape()
print(shape)

# TODO: Print the dtype of the tensor using the method dtype()
print(dtype)

# TODO: Print the size of the tensor using the method size()
print(size)