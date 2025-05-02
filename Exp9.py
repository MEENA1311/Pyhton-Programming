s1 = "welcome"
s2 = "good"
if s1 and s2:
    new_s1 = s2[0] + s1[1:]
    new_s2 = s1[0] + s2[1:]
    result = new_s1 + " " + new_s2
    print(result)
else:
    print("Invalid input")
