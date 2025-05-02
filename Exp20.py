with open("output.txt", "w") as f:
    while True:
        line = input()
        if line.lower() == "end":
            break
        f.write(line + "\n")
