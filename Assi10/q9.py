def get_peas(agent_name):
    peas_dict = {
        "vacuum": {
            "P": "Cleanliness, Energy efficiency, Time",
            "E": "Room floor, Obstacles, Dirt",
            "A": "Wheels, Brushes, Suction motor",
            "S": "Dirt sensor, Bump sensor, Camera"
        },
        "self-driving car": {
            "P": "Safety, Speed, Destination reach, Fuel efficiency",
            "E": "Roads, Traffic, Pedestrians, Weather",
            "A": "Steering, Accelerator, Brakes, Signals",
            "S": "Cameras, LiDAR, Radar, GPS, Speedometer"
        },
        "medical diagnosis": {
            "P": "Healthy patient, Correct diagnosis, Reduced costs",
            "E": "Patient, Hospital, Lab results",
            "A": "Display questions, Tests, Treatments",
            "S": "Symptoms, Lab measurements, Patient responses"
        }
    }
    key = "vacuum" if "vacuum" in agent_name.lower() else ("self-driving car" if "car" in agent_name.lower() else "medical diagnosis")
    return peas_dict[key]

agent = input("Enter AI Agent (vacuum/car/medical): ")
peas = get_peas(agent)
print("Performance Measure:", peas['P'])
print("Environment:", peas['E'])
print("Actuators:", peas['A'])
print("Sensors:", peas['S'])
