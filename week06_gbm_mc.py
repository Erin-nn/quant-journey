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
