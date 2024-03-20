# F1 Telemetry Visualization Tool
This python script is designed to visualize and compare telemetry data from Formula 1 races using the fastf1 library. 

<img src= "https://github.com/prathkr/Formula1-Telemetry-Visualization-Tool/assets/130935483/8e39f06f-58a8-4e22-b4ee-8c003a7ee3cb" alt="image" width="495" height="278" style="float:left;">

<img src= "https://github.com/prathkr/Formula1-Telemetry-Visualization-Tool/assets/130935483/adc62932-dea2-4886-9f30-d584c826416b" alt="image" width="495" height="278" style="float:left;">

<img src= "https://github.com/prathkr/Formula1-Telemetry-Visualization-Tool/assets/130935483/dc17f7d7-539e-4845-9eb3-9f8df40d77df" alt="image" width="495" height="278" style="float:left;">

<img src= "https://github.com/prathkr/Formula1-Telemetry-Visualization-Tool/assets/130935483/4125f3cc-3bcf-4c4f-91f3-e4c26b70e52a" alt="image" width="495" height="278" style="float:left;">

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

<img src="https://github.com/prathkr/Formula1-Telemetry-Visualization-Tool/assets/130935483/c5668d40-a060-4d2b-9c7e-469caab0282f" alt="image" width="444" height="133" style="float:left;">

### 3. Plot generation and sharing
* The script generates multiple plots to visualize different aspects of driver performance, including speed, throttle, and brake inputs.
* Each plot is customized with appropriate labels, legends, and gridlines for clarity and interpretation.
* The generated plots are saved as PNG images, facilitating further analysis, documentation, or presentation of the data.




