s = "shashikanth is my name"

words = s.split()

largest = ""

for word in words:

    if len(word)>len(largest):
        largest = word

print(largest)
