# F1 Telemetry Visualization Tool
This python script is designed to visualize and compare telemetry data from Formula 1 races using the fastf1 library. 

# Overview
The script prompts the user to input race details such as year, circuit, session type, and the number of drivers to analyze. It then fetches telemetry data for the specified race session and drivers, allowing for detailed analysis. The analysis includes generating a plot that provides a visual representation of how each driver performs in terms of speed during their fastest lap, as well as plotting speed, throttle, and brake data for each driver along the race distance.

# Setup Instructions
## Clone the repository
First, clone the repository or download the repository
## Install Dependencies
Navigate to the project directory and install the required dependencies using pip. Ensure that you have Python installed on your system

```
pip install -r requirements.txt
```

## Caching configuration
To enable caching and speed up data loading, Replace 'path' with your cache directory in the script

```
ff1.Cache.enable_cache('path') 
```

# Usage
## Run the project
Run the script in a python environment.

```
python f1_viz.py
```
## Input race data
follow the on-screen instructions to input race details
example : 

