s = "shashikanth is my name"

for ch in s:

    if s.count(ch)==1:
        print(ch)


##another method

s ="shashikanth is my name"

ans = ""

for ch in s:
    if ch not in ans:
        ans+=ch

print(ans)

