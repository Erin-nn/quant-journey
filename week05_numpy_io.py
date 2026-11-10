import numpy as np

print("=== 1 cumsum 与 cumprod ===")
r = np.array([0.02, -0.03, 0.05, -0.02, 0.01])  # 5 天日收益率
print(
    np.cumsum(r),
    np.cumprod(r + 1),
    round(np.cumsum(r)[-1], 6),
    round(np.cumprod(r + 1)[-1], 6),
)
# cumprod(1+r) 末值是净值 1.028274，减 1 得真实累计收益 2.83%；cumsum 末值 3.00% 是线性加总的近似

print("\n=== 2 axis 方向 ===")
b = np.array([[0, 1, 2], [3, 4, 5]])
print(b.cumsum(axis=0), "\n", b.cumsum(axis=1))
# axis=0 消掉行，每列得一个值（[0+3, 1+4, 2+5]）；axis=1 消掉列，每行得一个值

print("\n=== 3 数组文件 IO ===")
nav = np.cumprod(1 + np.array([0.02, -0.03, 0.05, -0.02, 0.01]))
np.save("nav", nav)  # 不写后缀
back = np.load("nav.npy")  # 读的时候必须写全
print(
    np.array_equal(nav, back), back.dtype, back.shape
)  # 读回来的和存进去的是否一模一样
# np.load("nav")      # 漏后缀 ，FileNotFoundError: [Errno 2] No such file or directory: 'nav'
arr = np.arange(10)
np.savez("array_archive.npz", a=arr, b=arr * 2)
arch = np.load("array_archive.npz")
print(type(arch).__name__)  # np.load 返回 NpzFile 对象，不是 ndarray，要按键取值
# __name__ 的正确定位是给人看的输出：打印、写日志、拼错误消息。
print(arch.files)  # ['a', 'b']
print(arch["b"])
np.savez_compressed("arrays_compressed.npz", a=arr, b=arr * 2)
# .npy 与 .npz 分别解决单数组和多数组打包；存时可以不加后缀，会自己补全，但读时必须加后缀。
