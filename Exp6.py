lst = list(map(int, input("Enter numbers separated by space: ").split()))
freq = {}
for num in lst:
    freq[num] = freq.get(num, 0) + 1
print("Frequency of elements:", freq)
