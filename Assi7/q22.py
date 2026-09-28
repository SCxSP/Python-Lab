fn = input("Enter filename (default student.txt): ")
if not fn:
    fn = "student.txt"

try:
    with open(fn, "r") as f:
        print("--- Using read() ---")
        print(f.read())

    with open(fn, "r") as f:
        print("--- Using readline() ---")
        line = f.readline()
        while line:
            print(line.strip())
            line = f.readline()
except FileNotFoundError:
    print("File not found")
