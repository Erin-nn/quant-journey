def constellation(sid):
    bm = int(sid[-8:-6])
    bd = int(sid[-6:-4])
    if (bm == 3 and bd >= 21) or (bm == 4 and bd <= 19):
        con = "Aries"
    elif (bm == 4 and bd >= 20) or (bm == 5 and bd <= 20):
        con = "Taurus"
    elif (bm == 5 and bd >= 21) or (bm == 6 and bd <= 21):
        con = "Gemini"
    elif (bm == 6 and bd >= 22) or (bm == 7 and bd <= 22):
        con = "Cancer"
    elif (bm == 7 and bd >= 23) or (bm == 8 and bd <= 22):
        con = "Leo"
    elif (bm == 8 and bd >= 23) or (bm == 9 and bd <= 22):
        con = "Virgo"
    elif (bm == 9 and bd >= 23) or (bm == 10 and bd <= 23):
        con = "Libra"
    elif (bm == 10 and bd >= 24) or (bm == 11 and bd <= 22):
        con = "Scorpio"
    elif (bm == 11 and bd >= 23) or (bm == 12 and bd <= 21):
        con = "Sagittarius"
    elif (bm == 12 and bd >= 22) or (bm == 1 and bd <= 19):
        con = "Capricorn"
    elif (bm == 1 and bd >= 20) or (bm == 2 and bd <= 18):
        con = "Aquarius"
    else:
        con = "Pisces"
    return con  # TODO: week3 用异常处理拦截非法日期


sid = input("input a Chinese national ID number:")

print("your constellation is:", constellation(sid))
