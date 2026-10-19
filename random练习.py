import random

for i in range(11):
    print(random.randint(0, 100))
print(random.randrange(0, 101, 2))
for i in range(5):
    print(random.choice("abcdefjhi"))
print(random.choice(["apple", "pear", "peach", "orange"]))
