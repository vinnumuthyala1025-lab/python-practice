s1 = "shashikanth is actually my name"
s2 = "my name is shashikanthh"

if len(s1) == len(s2) and s2 in s1 + s1:
    print("Rotation")
else:
    print("Not rotation")