import numpy as np

print("\n=== 1 可重复性 ===")
a = np.random.RandomState(42).random_sample(5)
b = np.random.RandomState(42).random_sample(5)
c = np.random.RandomState(7).random_sample(5)
print(a, np.array_equal(a, b), np.array_equal(a, c))

print("\n=== 2 分布 ===")
rng = np.random.RandomState(0)
returns = rng.normal(0, 0.01, 1000)
print(rng.randint(0, 100, size=10), round(np.mean(rng4), 4), round(np.std(rng4), 4))

print("\n=== 3 抽样 ===")
rng = np.random.RandomState(0)
print(rng.choice(["A", "B", "C", "D"], size=3, replace=False))
print(rng.permutation(10))

print("\n=== 4 蒙特卡洛估 π ===")
rng = np.random.RandomState(0)
x, y = rng.random_sample((2, 100_000))
inside = (x**2 + y**2) < 1
print(round(4 * inside.mean(), 5), round(abs(4 * inside.mean() - np.pi), 5))
