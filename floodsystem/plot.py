import matplotlib.pyplot as plt
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels


def plot_water_levels(station, dates, levels):
    
    stations = build_station_list()
    station_name = "Cam"
    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break

    if not station_cam:
        print("Station {} could not be found".format(station_name))
        return

    dt = 10
    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.show()

