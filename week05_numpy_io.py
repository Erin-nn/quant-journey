import numpy as np

print("=== 1 cumsum 与 cumprod ===")
r = np.array([0.02, -0.03, 0.05, -0.02, 0.01])  # 5 天日收益率
print(
    np.cumsum(r),
    np.cumprod(r + 1),
    round(np.cumsum(r)[-1], 6),
    round(np.cumprod(r + 1)[-1], 6),
)
# # cumprod(1+r) 末值是净值 1.028274，减 1 得真实累计收益 2.83%；cumsum 末值 3.00% 是线性加总的近似

print("\n=== 2 axis 方向 ===")
b = np.array([[0, 1, 2], [3, 4, 5]])
print(b.cumsum(axis=0), "\n", b.cumsum(axis=1))
# axis=0 消掉行，每列得一个值（[0+3, 1+4, 2+5]）；axis=1 消掉列，每行得一个值
