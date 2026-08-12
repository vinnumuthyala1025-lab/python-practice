s = "shashikanth is my name"

words = s.split()

max_count = 0
max_word=""

for word in words:
    if words.count(word)>max_count:
        max_count = words.count(word)
        max_word = word

print("most frquent word=",max_word)

