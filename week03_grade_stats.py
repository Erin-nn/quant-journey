import csv

with open("grades.csv", "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))
print(rows[1][0])
print(rows[2][1:4])
for r in rows[1:]:
    print(r[0])
print("任务1如上")
print(len(rows) - 1)
print(len(rows[1]) - 1)
print("任务2如上")
names = []
for r in rows[1:]:
    names.append(r[0])
print(names)
names2 = [r[0] for r in rows[1:]]
print(names2)
print("任务3如上")
print(sum(int(x) for x in rows[1][1:]), "\n", "任务4如上")
zs = rows[1][1:]
total1 = sum(int(m) for m in zs)
avg1 = round(total1 / len(zs), 2)
print(avg1, "\n", "任务5如上")
scored = []
for r in rows[1:]:
    scores = r[1:]
    total = sum(int(s) for s in scores)
    avg = round(total / len(scores), 2)
    scored.append((avg, r[0]))
scored.sort(reverse=True)
print(scored)
print("任务6如上")
print(sorted(["92", "88", "100"]))
print(sorted(int(x) for x in ["92", "88", "100"]))
print("任务7如上")
