class SemanticNetwork:
    def __init__(self):
        self.network = {}

    def add_relation(self, subject, relation, obj):
        self.network.setdefault(subject, []).append((relation, obj))

    def query(self, subject):
        return self.network.get(subject, [])

sn = SemanticNetwork()
sn.add_relation("Car", "IS-A", "Vehicle")
sn.add_relation("Car", "HAS-A", "Engine")
sn.add_relation("Car", "CAN", "Drive")
sn.add_relation("ElectricCar", "IS-A", "Car")
sn.add_relation("ElectricCar", "HAS-A", "Battery")

item = input("Query vehicle (Car/ElectricCar): ")
results = sn.query(item)
print(f"Relations for {item}:")
for rel, obj in results:
    print(f"  {item} {rel} {obj}")
