import numpy as np

l0 = np.array([10, 20, 30])
print(l0, type(l0))
l1 = np.array([[1, 2, 3], [4, 5, 6]])
print(l1.shape, l1.ndim, l1.size, l1.dtype)
l2 = np.array([6, 7.5, 8, 0, 1])
print(l2.dtype)  # 数组里有一个 7.5 是浮点，numpy 统一向上取 dtype，整个数组升为 float64
l3 = np.arange(6)
print(l3.reshape(2, 3), l3.reshape(3, 2))
# l3.reshape(4, 2)   ValueError: cannot reshape array of size 6 into shape (4,2)
# --- 索引与切片 ---
a = np.arange(10)
print(a[1:4], a[::-1], a[::2])

b = np.arange(12).reshape(3, 4)
print(b[1], b[:, 1], b[0:2, 1:3])  # b[:,1] 的形状是1维，取整列会降维

s = a[2:5]
s[0] = 99
print(a)
a = np.arange(10)
s = a[2:5].copy()
s[0] = 99
print(a)

r = np.array([0.02, -0.03, 0.0, 0.05, -0.01])
print(r[r > 0])
m = r.copy()
m[m < 0] = 0
print(m)
# --- 花式索引与转置 ---
a = np.arange(10)
print(
    a[[0, 2]], a[[2, 0, 1]], a[[0, 0, 0]], np.shares_memory(a, a[[0, 2]])
)  # 花式索引返回的是拷贝
b = np.arange(12).reshape(3, 4)
print(b[[0, 2]])
c = np.arange(6).reshape(2, 3)
print(c, c.T, c.T.shape)
c.T[0, 1] = 99
print(c)
print(np.arange(3).T.shape)
