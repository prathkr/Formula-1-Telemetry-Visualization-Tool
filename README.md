# F1 Telemetry Visualization Tool
This python script is designed to visualize and compare telemetry data from Formula 1 races using the fastf1 library. 

<img src= "https://github.com/prathkr/Formula1-Telemetry-Visualization-Tool/assets/130935483/e2f07a5d-a683-431a-8e01-19f34b6c4bfe" alt="image" width="444" height="222" style="float:left;">

<img src= "https://github.com/prathkr/Formula1-Telemetry-Visualization-Tool/assets/130935483/18ae869b-65f6-4e6a-ad5a-ed9d7538b0bd" alt="image" width="444" height="222" style="float:left;">

<img src= "https://github.com/prathkr/Formula1-Telemetry-Visualization-Tool/assets/130935483/2cc75bb4-73f8-49cf-8946-65a5ade1d0f8" alt="image" width="444" height="222" style="float:left;">

<img src= "https://github.com/prathkr/Formula1-Telemetry-Visualization-Tool/assets/130935483/8c7eaeb8-0c83-4a27-aea0-10a7a539664e" alt="image" width="444" height="222" style="float:left;">

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




