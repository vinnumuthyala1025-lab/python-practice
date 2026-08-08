d = {
    "a": 10,
    "b": 15,
    "c": 20,
    "d": 25,
    "e": 30
}

count = 0

for value in d.values():
    if value%2==0:
        count+=1


print(count)