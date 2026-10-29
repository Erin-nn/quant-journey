import csv

with open("grades.csv", "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))

header = rows[0]
data = rows[1:]
result = []
for r in data:
    name = r[0]
    scores = [float(x) for x in r[1:]]
    total = sum(scores)
    avg = round(total / len(scores), 2)
    result.append([name] + scores + [total, avg])
result.sort(key=lambda x: x[-1], reverse=True)

out_header = ["排名"] + header + ["总分", "平均分"]
out_rows = [[i] + row for i, row in enumerate(result, 1)]

with open("grades_result.csv", "w", encoding="utf-8", newline="") as f:
    write = csv.writer(f)
    write.writerow(out_header)
    write.writerows(out_rows)
