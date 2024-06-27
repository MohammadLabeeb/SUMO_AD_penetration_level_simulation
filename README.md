# SUMO_AD_penetration_level_simulation

The research question addressed in this simulation study is: "How does the existence of autonomous vehicles influence the safety of heterogeneous traffic? Do different penetration rates bring different results?" The objectives of the simulation are to assess the impact of autonomous vehicles on traffic safety, considering varying penetration rates.

## Description

The 'demand_generation_script.py' script generates a traffic flow file(xml format) containing a specified number of vehicles with various characteristics. The vehicles are divided into autonomous and human-operated types, with different probabilities for cars and trucks. The script also includes parameters for tracking conflicts using SSM (Surrogate Safety Measures).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/traffic-flow-generator.git
   ```
2. Navigate to the project directory
   ```bash
   cd traffic-flow-generator
   ```

## Usage

1. Navigate to the project directory
   ```bash
   python traffic_flow_generator.py
   ```
   This will generate the generated_traffic_3.rou.xml file in the project directory.

## Features
- Generates a specified number of vehicles with unique IDs.
- Randomly assigns vehicle types based on penetration rate(penetration rate can be set in the script).
- Randomly generates initial speeds for each vehicle.
- Randomly assigns edges and lanes for vehicle departure.
- Includes SSM parameters for tracking conflicts.
