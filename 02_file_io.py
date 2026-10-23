from week01_def_practice import constellation

ids = with open("ids.txt", "rt",encoding="utf-8")
try:
    for sid in ids:
        sid=sid.strip()
        print(sid, "->", constellation(sid))

except NameError:
    print("输入错误！")
