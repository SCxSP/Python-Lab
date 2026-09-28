fn = input("Enter filename: ")
try:
    with open(fn, "r") as f:
        print("File content:")
        print(f.read())
except FileNotFoundError:
    print("Error: File not found")
except PermissionError:
    print("Error: Permission denied")
except Exception as e:
    print("Error:", e)
finally:
    print("File operation completed")
