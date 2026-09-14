def display_table(n,times=10):
    for i in range(times):
        print(f"{n} x   {i+1}   = {n*(i+1)}")

display_table(int(input("Multiplication Table of: ")))