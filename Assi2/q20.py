name = input("Enter your name: ")
marks=[]
q1,q2,q3 = input("Enter your Marks: ").split()
q1,q2,q3=int(q1),int(q2),int(q3)
print(f"Your name is {name}!")
print(f"You Total is: {sum(q1,q2,q3)}")
print(f"Your Avg is: {sum(q1,q2,q3)/3}")
