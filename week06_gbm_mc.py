import numpy as np

# 第 1 段：单条随机漫步，1000 步
# help(np.cumsum) : 一维数组能省，省了之后默认axis=None，含义是“把数组摊平后累加”
rng = np.random.RandomState(seed=0)
steps = rng.choice([-1, 1], size=1000)
path = np.cumsum(steps)
print(
    steps[:10], "\n", path[:10], "\n", path[-1]
)  # cumsum 结果的第 k 项，在物理上对应所在位置
