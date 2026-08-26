infos = []
for i in range(3):
    name = input("Enter name: ")
    roll = input("Enter roll: ")
    m1, m2, m3 = input("Enter 3 marks: ").split()
    infos.append((name, roll, m1, m2, m3))
infos = tuple(infos)
for i in range(3):
    print(f"Name: {infos[i][0]}, Roll: {infos[i][1]}, Marks: {infos[i][2]} {infos[i][3]} {infos[i][4]}")
