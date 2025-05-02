s = input("Enter a sentence: ")
words = s.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
if len(sorted_words) > 1:
    print("Second most repeated word:", sorted_words[1][0])
else:
    print("Not enough distinct words.")
