from week01_def_practice import constellation

with (
    open("ids.txt", "r", encoding="utf-8") as ids,
    open("result.txt", "w", encoding="utf-8") as out,
):
    for sid in ids:
        sid = sid.strip()
        if not sid:
            continue
        if len(sid) != 18:
            out.write(f"{sid} 格式非法\n")
            continue
        try:
            con = constellation(sid)
        except ValueError:
            out.write(sid + " 格式非法\n")
        else:
            out.write(sid + " -> " + con + "\n")
