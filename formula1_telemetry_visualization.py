import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import random  

plotting.setup_mpl()
ff1.Cache.enable_cache('cache')

print('Enter race data ')
year = input('Enter year: ')
circuit = input('Enter circuit: ')
session = input('Enter session: \nSessions: FP1, FP2, FP3, Q, SQ(Sprint Qualifying), R(Race)')
num_drivers = int(input('Enter the number of drivers to analyze: '))

drivers = []
for i in range(num_drivers):
    driver = input('Enter 3-letter code of Driver {}: '.format(i+1))
    drivers.append(driver)

driver_colors = {
    driver: '#{:06x}'.format(random.randint(0, 0xFFFFFF))  
    for driver in drivers
}

year = int(year)

race = ff1.get_session(year, '{}'.format(circuit), '{}'.format(session))
race.load()
laps = race.laps

if laps is not None and not laps.empty:
    telemetry_data = []

    for driver in drivers:
        laps_driver = race.laps.pick_driver(driver)
        fastest_driver = laps_driver.pick_fastest().get_telemetry().add_distance()
        fastest_driver['Driver'] = driver
        telemetry_data.append(fastest_driver)
        
    telemetry = pd.concat(telemetry_data)
    cmap = cm.colors.ListedColormap(list(driver_colors.values()))
    num_minisectors = 25

    total_distance = max(telemetry['Distance'])

    minisector_length = total_distance / num_minisectors

    minisectors = [0]

    for i in range(0, (num_minisectors - 1)):
        minisectors.append(minisector_length * (i + 1))

    telemetry['Minisector'] = telemetry['Distance'].apply(
        lambda dist: (
            int((dist // minisector_length) + 1)
        )
    )
    average_speed = telemetry.groupby(['Minisector', 'Driver'])['Speed'].mean().reset_index()

    fastest_driver = average_speed.loc[average_speed.groupby(['Minisector'])['Speed'].idxmax()]

    fastest_driver = fastest_driver[['Minisector', 'Driver']].rename(columns={'Driver': 'Fastest_driver'})

    telemetry = telemetry.merge(fastest_driver, on=['Minisector'])

    telemetry = telemetry.sort_values(by=['Distance'])

    for i, driver in enumerate(drivers):
        telemetry.loc[telemetry['Fastest_driver'] == driver, 'Fastest_driver_int'] = i + 1

    x = np.array(telemetry['X'].values)
    y = np.array(telemetry['Y'].values)

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    fastest_driver_array = telemetry['Fastest_driver'].map(driver_colors).to_numpy()

    lc_comp = LineCollection(segments, colors=fastest_driver_array, linewidths=5)
    c_cmap = mcolors.ListedColormap(list(driver_colors.values()))   
    plt.rcParams['figure.figsize'] = [18, 10]
    plt.gca().add_collection(lc_comp)
    plt.axis('equal')
    plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=driver, 
                               markerfacecolor=driver_colors[driver], markersize=10) 
                   for driver in drivers]
    plt.legend(handles=legend_elements, loc='lower center')

    legend_elements = [Line2D([0], [0], color=color, label=driver) for driver, color in driver_colors.items()]
    plt.gca().add_collection(lc_comp)
    plt.axis('equal')
    plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
    plt.legend(handles=legend_elements, loc='upper left')  # You can change the location as needed

    drivers = telemetry['Driver'].unique()
    
    plt.figure(figsize=(12, 8))
    for driver in drivers:
        driver_data = telemetry[telemetry['Driver'] == driver]
        plt.plot(driver_data['Distance'], driver_data['Speed'], label=driver, color=driver_colors[driver])

    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=driver, 
                               markerfacecolor=driver_colors[driver], markersize=10) 
                   for driver in drivers]
    plt.legend(handles=legend_elements, loc='upper left')
    
    plt.xlabel('Distance')
    plt.ylabel('Speed')
    plt.grid(True)
    plt.savefig('circuit_plot.png', dpi=300)
    plt.show()


else:
    print("Failed to load session data.")
