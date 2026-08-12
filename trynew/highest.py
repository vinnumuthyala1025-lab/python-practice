s = "shashikanth is my name"

max_count = 0
max_ch =""

for ch in s:
    if s.count(ch)>max_count:
        max_count = s.count(ch)
        max_ch=ch

print(max_ch)

