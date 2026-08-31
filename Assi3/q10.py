#sqrt((x2 - x1)^2 + (y2 - y1)^2)
x1, y1 = map(float, input("Enter x1 y1: ").split())
x2, y2 = map(float, input("Enter x2 y2: ").split())
p1, p2 = (x1, y1), (x2, y2)
d = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5
print("Distance:", d)
