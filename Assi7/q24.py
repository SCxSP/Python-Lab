src = input("Enter source file (default student.txt): ") or "student.txt"
dest = input("Enter dest file (default destination.txt): ") or "destination.txt"

try:
    with open(src, "r") as f_src, open(dest, "w") as f_dest:
        f_dest.write(f_src.read())
    print("File copied successfully")
except FileNotFoundError:
    print("Source file not found")
