import numpy as np

print("\n=== 1 单条随机漫步,1000 步 ===")
# help(np.cumsum) : 一维数组能省，省了之后默认axis=None，含义是“把数组摊平后累加”
rng1 = np.random.RandomState(seed=0)
steps1 = rng1.choice([-1, 1], size=1000)
path = np.cumsum(steps1)
print(
    steps1[:10], "\n", path[:10], "\n", path[-1]
)  # cumsum 结果的第 k 项，在物理上对应所在位置

print("\n=== 2 多条路径 + √N 验证 ===")
# help(np.cumsum):每条路径在自己的行内沿时间累积，不跨行--对应 axis =1
nwalks = 5
nsteps = 1000
rng2 = np.random.RandomState(seed=0)
steps2 = rng2.choice([-1, 1], size=(nwalks, nsteps))
path1 = np.cumsum(steps2, axis=1)
print(np.shape(path1), "\n", path1[:, -1])

finals = path1[:, -1]  # 每条路径的终值：作用在 path1 上，取最后一列
rowsum = np.sum(steps2, axis=1)  # 每条路径的总位移：作用在 steps2 上，每行求和
print(finals, rowsum, np.array_equal(finals, rowsum))  # 判等，用 np.array_equal

nwalks2 = 1000
rng3 = np.random.RandomState(seed=0)
steps3 = rng3.choice([-1, 1], size=(nwalks2, nsteps))
path3 = np.cumsum(steps3, axis=1)
finals3 = path3[:, -1]
print(
    round(np.mean(finals3), 2), round(np.std(finals3), 2), round(np.sqrt(1000), 2)
)  # std ≈ √1000 = 31.62：每条路径终值是 1000 个 ±1 之和，方差累加成 1000，标准差开根号

print("\n=== 3 GBM 单条路径 ===")
# 几何布朗运动（GBM）描述股价的连续随机过程，离散到每一天是：每期对数收益 = (μ − 0.5σ²)·dt  +  σ·√dt·z
#                                                                 └─ 漂移 ─┘      └─ 波动 ─┘
rng_gbm = np.random.RandomState(seed=0)
#  help(np.exp) : 确认它和 np.log 互为反函数,参数可以是数组
#  help(rng_gbm.normal) : normal(loc=0.0, scale=1.0, size=None),前两个都是默认值,size 直接给 252
s0 = 100
mu = 0.10
sigma = 0.20
t = 1.0
n_steps = 252
dt = t / n_steps
z3 = rng_gbm.normal(size=n_steps)
logret3 = (mu - 0.5 * sigma**2) * dt + sigma * (dt ** (1 / 2)) * z3
price3 = np.exp(np.cumsum(logret3)) * s0
print(
    np.shape(price3),
    round(price3[0], 4),
    round(price3[-1], 4),
    round(np.min(price3), 4),
)  #  exp 永远 > 0，价格不会变负,最小值必须是正数

print("\n=== 4 GBM 多路径 GBM + 0.5σ² 对照实验 ===")
rng4 = np.random.RandomState(seed=0)
# ① 先 help(np.cumsum)，确认二维下要的是「每行内部沿时间累积」
#    对应 axis = ?（昨天 ±1 漫步里用过同一个判断，结论照搬）
n_paths = 10000
z4 = rng4.normal(size=(n_paths, n_steps))
logret4 = (mu - 0.5 * sigma**2) * dt + sigma * (dt ** (1 / 2)) * z4
price4 = np.exp(np.cumsum(logret4, axis=1)) * s0
theory = s0 * np.exp(mu * t)  # 理论均值，别硬编码 110.5171
err = price4[:, -1].mean() / theory - 1  # 相对误差，是个小数

print(
    round(price4[:, -1].mean(), 3),
    f"{err:+.2%}",
    round(np.std(price4[:, -1]), 3),
    round(np.min(price4), 3),
)
logret_wrong = mu * dt + sigma * (dt ** (1 / 2)) * z4
price_wrong = np.exp(np.cumsum(logret_wrong, axis=1)) * s0
err_wrong = price_wrong[:, -1].mean() / theory - 1
print(
    "漂移项改成不带 0.5σ² 的版本:",
    round(price_wrong[:, -1].mean(), 3),
    f"{err_wrong:+.2%}",
    round(np.std(price_wrong[:, -1]), 3),
    round(np.min(price_wrong), 3),
)  #  两个均值差2.234
# 两次都用同一个 z4（控制变量）：唯一差异是漂移项，因此 2.234 的差可归因于 0.5σ²
