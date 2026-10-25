rows = [
    ["张三", "85", "90", "78"],
    ["李四", "92", "88", "95"],
    ["王五", "70", "75", "80"],
]
print(rows[0][0])
print(rows[1][1:4])
for r in rows:
    print(r[0])
print("任务1如上")
print(len(rows))
print(len(rows[0]) - 1)
print("任务2如上")
names = []
for r in rows:
    names.append(r[0])
print(names)
names2 = [r[0] for r in rows]
print(names2)
print("任务3如上")
print(sum(int(x) for x in rows[0][1:]),"任务4如上")
zs = rows[0][1:]
total = sum(int(s) for s in zs)
print("张三平均分:", round(total / len(zs), 2))

sorted(int(x) for x in ["92", "88", "100"])
print("任务5如上")
