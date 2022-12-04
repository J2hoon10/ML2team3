import random

script = []

f = open(r"KSS_대사정보.txt", 'rt', encoding='UTF8')
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    script.append(line)
f.close()

f = open('all.txt', 'w')

filepath = (r"kss_temp")
for i in range(1, 4+1):
    if i == 1:
        for j in range(0, 1040+1):
            f.write(filepath)
            f.write("/")
            if j<10:
                f.write("1_000")
                f.write(str(j))
                f.write(".wav")
            elif j>=10 and j<100:
                f.write("1_00")
                f.write(str(j))
                f.write(".wav")
            elif j==846:
                continue
            elif j>=100 and j<1000:
                f.write("1_0")
                f.write(str(j))
                f.write(".wav")
            elif j>=1000:
                f.write("1_")
                f.write(str(j))
                f.write(".wav")
            f.write("|")
            f.write(script[j])
            f.write("\n")
    elif i == 2:
        for j in range(0, 1156+1):
            f.write(filepath)
            f.write("/")
            if j<10:
                f.write("2_000")
                f.write(str(j))
                f.write(".wav")
            elif j>=10 and j<100:
                f.write("2_00")
                f.write(str(j))
                f.write(".wav")
            elif j>=100 and j<1000:
                f.write("2_0")
                f.write(str(j))
                f.write(".wav")
            elif j>=1000:
                f.write("2_")
                f.write(str(j))
                f.write(".wav")
            f.write("|")
            f.write(script[j])
            f.write("\n")
    elif i == 3:
        for j in range(0, 5024+1):
            f.write(filepath)
            f.write("/")
            if j<10:
                f.write("3_000")
                f.write(str(j))
                f.write(".wav")
            elif j>=10 and j<100:
                f.write("3_00")
                f.write(str(j))
                f.write(".wav")
            elif j>=100 and j<1000:
                f.write("3_0")
                f.write(str(j))
                f.write(".wav")
            elif j>=1000:
                f.write("3_")
                f.write(str(j))
                f.write(".wav")
            f.write("|")
            f.write(script[j])
            f.write("\n")
    elif i == 4:
        for j in range(0, 5631+1):
            f.write(filepath)
            f.write("/")
            if j<10:
                f.write("4_000")
                f.write(str(j))
                f.write(".wav")
            elif j>=10 and j<100:
                f.write("4_00")
                f.write(str(j))
                f.write(".wav")
            elif j>=100 and j<1000:
                f.write("4_0")
                f.write(str(j))
                f.write(".wav")
            elif j>=1000:
                f.write("4_")
                f.write(str(j))
                f.write(".wav")
            f.write("|")
            f.write(script[j])
            f.write("\n")
    

f.close()

with open(r"all.txt", 'rt', encoding='cp949') as f:
    lines = f.readlines()

random.shuffle(lines)

with open(r"train.txt",'w',encoding='UTF-8') as f:
    for data in lines[:10283]:
        f.write(data)

with open(r"dev.txt",'w',encoding='UTF-8') as f:
    for data in lines[10283:]:
        f.write(data)
