def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    upper = sum(1 for c in content if c.isupper())
    lower = sum(1 for c in content if c.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

    with open(filename, 'r') as f:
        lines = f.readlines()

    line_no = int(input("Enter line number to search word in: "))
    word = input("Enter word to search: ")
    if 0 < line_no <= len(lines) and word in lines[line_no - 1]:
        print("Word found in line", line_no)
    else:
        print("Word not found")

    start = int(input("Enter start line: "))
    end = int(input("Enter end line: "))
    for i in range(start - 1, end):
        if word in lines[i]:
            print(f"'{word}' found in line {i + 1}: {lines[i].strip()}")

    to_replace = input("Enter word to replace: ")
    replacement = input("Enter replacement word: ")
    content = content.replace(to_replace, replacement)
    with open(filename, 'w') as f:
        f.write(content)

