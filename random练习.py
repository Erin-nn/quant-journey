import random

for i in range(10):
    print(random.randint(0, 100))
print(random.randrange(1, 101, 2))
for i in range(4):
    print(random.choice("abcdefjhi"))
print(random.choice(["apple", "pear", "peach", "orange"]))
