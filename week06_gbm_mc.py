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
rng4 = np.random.RandomState(seed=0)
#  help(np.exp) : 确认它和 np.log 互为反函数,参数可以是数组
#  help(rng4.normal) : normal(loc=0.0, scale=1.0, size=None),前两个都是默认值,size 直接给 252
s0 = 100
mu = 0.10
sigma = 0.20
t = 1.0
nsteps2 = 252
dt = t / nsteps2
steps4 = rng4.normal(size=nsteps2)
gbm = (mu - 0.5 * sigma**2) * dt + sigma * (dt ** (1 / 2)) * steps4
price = np.exp(np.cumsum(gbm)) * s0
print(
    np.shape(price), round(price[0], 4), round(price[-1], 4), round(np.min(price), 4)
)  #  exp 永远 > 0，价格不会变负,最小值必须是正数
