import os
import random
import xml.etree.ElementTree as ET

# Define the number of vehicles and penetration rate
total_vehicles = 4000
penetration_rate = 0.1

# Define the output file path
output_file = "generated_traffic_3.rou.xml"

# Function to generate vehicle parameters
def generate_vehicle_params(vehicle_id, vehicle_type, initial_speed, edge, lane):
    vehicle = ET.Element("vehicle")
    vehicle.set("id", vehicle_id)
    vehicle.set("type", vehicle_type)
    vehicle.set("depart", "0")
    vehicle.set("departLane", lane)
    vehicle.set("departPos", "0")  # Set departPos to 0.00
    vehicle.set("departSpeed", initial_speed)
    route = ET.SubElement(vehicle, "route")
    route.set("edges", edge)

    # Add SSM parameters for tracking conflicts
    ssm_device = ET.SubElement(vehicle, "param")
    ssm_device.set("key", "has.ssm.device")
    ssm_device.set("value", "true")
    ssm_measures = ET.SubElement(vehicle, "param")
    ssm_measures.set("key", "device.ssm.measures")
    ssm_measures.set("value", "TTC DRAC")
    ssm_thresholds = ET.SubElement(vehicle, "param")
    ssm_thresholds.set("key", "device.ssm.thresholds")
    ssm_thresholds.set("value", "3.0 3.4")
    ssm_file = ET.SubElement(vehicle, "param")
    ssm_file.set("key", "device.ssm.file")
    ssm_file.set("value", "SSMs.xml")

    return vehicle

# Generate traffic flow
def generate_traffic():
    root = ET.Element("routes")
    for i in range(total_vehicles):
        vehicle_id = "vehicle_" + str(i)
        # Determine vehicle type based on penetration rate
        if random.random() < penetration_rate:
            # Autonomous vehicle
            if random.random() < 0.2:  # 20% probability of being a truck
                vehicle_type = "autonomous_truck_0"
            else:
                vehicle_type = "autonomous_car_0"
        else:
            # Human-operated vehicle
            if random.random() < 0.2:  # 20% probability of being a truck
                vehicle_type = "human_operated_truck_0"
            else:
                vehicle_type = "human_operated_car_0"
        # Generate random initial speed
        initial_speed = str(random.uniform(5, 25))
        # Determine edge and lane randomly
        edge = random.choice(["-gneE0", "gneE0"])
        lane = str(random.randint(0, 1))  # Randomly select a lane
        # Create vehicle element
        vehicle = generate_vehicle_params(vehicle_id, vehicle_type, initial_speed, edge, lane)
        root.append(vehicle)
    
    # Create XML tree and write to file
    tree = ET.ElementTree(root)
    tree.write(output_file)

# Main function
def main():
    generate_traffic()
    print("Generated traffic flow saved to", output_file)

if __name__ == "__main__":
    main()