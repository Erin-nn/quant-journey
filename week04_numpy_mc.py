import numpy as np

l0 = np.array([10, 20, 30])
print(l0, type(l0))
l1 = np.array([[1, 2, 3], [4, 5, 6]])
print(l1.shape, l1.ndim, l1.size, l1.dtype)
l2 = np.array([6, 7.5, 8, 0, 1])
print(l2.dtype)  # 数组里有一个 7.5 是浮点，numpy 统一向上取 dtype，整个数组升为 float64
l3 = np.arange(6)
print(l3.reshape(2, 3), l3.reshape(3, 2))
l3.reshape(4, 2)  # ValueError: cannot reshape array of size 6 into shape (4,2)
