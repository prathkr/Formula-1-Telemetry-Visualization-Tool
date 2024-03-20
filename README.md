# F1 Telemetry Visualization Tool
This python script is designed to visualize and compare telemetry data from Formula 1 races using the fastf1 library. 

# Overview
The script prompts the user to input race details such as year, circuit, session type, and the number of drivers to analyze. It then fetches telemetry data for the specified race session and drivers, allowing for detailed analysis. The analysis includes generating a plot that provides a visual representation of how each driver performs in terms of speed during their fastest lap, as well as plotting speed, throttle, and brake data for each driver along the race distance.

# Setup Instructions
### 1. Clone the repository
First, clone the repository or download the repository
### 2. Install dependencies
Navigate to the project directory and install the required dependencies using pip. Ensure that you have Python installed on your system

```
pip install -r requirements.txt
```

### 3. Caching configuration
To enable caching and speed up data loading, update 'path' with your cache directory in the script

```python
ff1.Cache.enable_cache('path')
```

# Usage
### 1. Run the project
Run the script in a python environment.

```
python f1_viz.py
```
### 2. Input race data
Follow the on-screen prompts to enter the required race data

<img src="https://github.com/prathkr/Formula1-Telemetry-Visualization-Tool/assets/130935483/c5668d40-a060-4d2b-9c7e-469caab0282f" alt="image" width="406" height="203" style="float:left;">


