infos = []
for i in range(3):
    name = input("Enter name: ")
    m1, m2, m3 = map(int, input("Enter 3 marks: ").split())
    infos.append((name, m1, m2, m3))
infos = tuple(infos)
for info in infos:
    print(info[0], info[1], info[2], info[3])
