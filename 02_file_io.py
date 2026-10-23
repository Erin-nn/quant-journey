from week01_def_practice import constellation

with open("ids.txt", "r", encoding="utf-8") as ids:
    try:
        for sid in ids:
            sid=sid.strip()
            print(sid, "->", constellation(sid))

    except NameError:
        print("输入错误！")
