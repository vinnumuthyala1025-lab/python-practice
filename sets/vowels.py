t="Education"
vowels ={'a','e','i','o','u'}
result=set()
for ch in t.lower():
    if ch in vowels:
        result.add(ch)
print(result)


