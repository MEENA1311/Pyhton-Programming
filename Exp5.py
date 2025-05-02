lst = list(map(int, input("Enter numbers separated by space: ").split()))
unique = list(set(lst))
if len(unique) < 2:
    print("Not enough unique elements.")
else:
    unique.sort()
    print("Second Smallest:", unique[1])
    print("Second Largest:", unique[-2])
