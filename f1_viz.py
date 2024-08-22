import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import fastf1 as ff1
from fastf1 import plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib import cm, colors as mcolors
from matplotlib.lines import Line2D

plotting.setup_mpl()
ff1.Cache.enable_cache('cache')

root = tk.Tk()
root.title("F1 Telemetry Visualization Tool")


def submit():
    try:
        year = int(year_entry.get())
        circuit = circuit_entry.get()
        session = session_entry.get().upper()
        num_drivers = int(drivers_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid data.")
        return

    drivers = []
    for i in range(num_drivers):
        driver = simpledialog.askstring("Driver", f"Enter 3-letter code of Driver {i + 1}:")
        if driver:
            drivers.append(driver.upper())

    if not drivers:
        messagebox.showerror("Input Error", "No drivers entered.")
        return

    driver_colors = {
        driver: '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        for driver in drivers
    }

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
        num_minisectors = 25

        total_distance = max(telemetry['Distance'])
        minisector_length = total_distance / num_minisectors

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

        plt.title('{} - {} - {}'.format(circuit, year, session))
        legend_elements = [Line2D([0], [0], color=color, label=driver) for driver, color in driver_colors.items()]
        plt.gca().add_collection(lc_comp)
        plt.axis('equal')
        plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
        plt.legend(handles=legend_elements, loc='upper left')
        drivers = telemetry['Driver'].unique()

        plt.figure(figsize=(12, 8))
        for driver in drivers:
            driver_data = telemetry[telemetry['Driver'] == driver]
            plt.plot(driver_data['Distance'], driver_data['Speed'], label=driver, color=driver_colors[driver])

        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=driver,
                                      markerfacecolor=driver_colors[driver], markersize=10)
                           for driver in drivers]
        plt.legend(handles=legend_elements, loc='upper left')
        plt.title('{} - {} - {}'.format(circuit, year, session))
        plt.xlabel('Distance')
        plt.ylabel('Speed')
        plt.grid(True)
        plt.savefig('driver_speed_graph.png', dpi=300)
        plt.show()

        plt.figure(figsize=(12, 8))
        for driver in drivers:
            driver_data = telemetry[telemetry['Driver'] == driver]
            plt.plot(driver_data['Distance'], driver_data['Throttle'], label=driver, color=driver_colors[driver])
        plt.title('{} - {} - {}'.format(circuit, year, session))
        plt.xlabel('Distance')
        plt.ylabel('Throttle')
        plt.grid(True)
        plt.legend(loc='upper left')
        plt.savefig('driver_throttle_graph.png', dpi=300)
        plt.show()

        plt.figure(figsize=(12, 8))
        for driver in drivers:
            driver_data = telemetry[telemetry['Driver'] == driver]
            plt.plot(driver_data['Distance'], driver_data['Brake'], label=driver, color=driver_colors[driver])
        plt.title('{} - {} - {}'.format(circuit, year, session))
        plt.xlabel('Distance')
        plt.ylabel('Brake')
        plt.grid(True)
        plt.legend(loc='upper left')
        plt.savefig('driver_brake_graph.png', dpi=300)
        plt.show()

    else:
        print("Failed to load session data.")


ttk.Label(root, text="Enter year:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
year_entry = ttk.Entry(root)
year_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Enter circuit:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
circuit_entry = ttk.Entry(root)
circuit_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Enter session (FP1, FP2, FP3, Q, SQ, R):").grid(row=2, column=0, padx=10, pady=5, sticky='e')
session_entry = ttk.Entry(root)
session_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Enter the number of drivers to analyze:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
drivers_entry = ttk.Entry(root)
drivers_entry.grid(row=3, column=1, padx=10, pady=5)

submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
