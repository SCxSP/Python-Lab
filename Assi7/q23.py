fn = input("Enter filename (default student.txt): ")
if not fn:
    fn = "student.txt"

try:
    with open(fn, "r") as f:
        lines = f.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)
    print("Lines:", line_count, "Words:", word_count, "Chars:", char_count)
except FileNotFoundError:
    print("File not found")
