from cProfile import label
import matplotlib.pyplot as plt
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list, update_water_levels

def plot_water_levels(station, dates, levels):
    stations = build_station_list()
    update_water_levels(stations)

    highest_rel = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            highest_rel.append((station.name, station.relative_water_level()))
    new = sorted_by_key(highest_rel, 1, reverse = True)

    
    station_name1 = new[1][0]
    station_1 = None
    for station in stations:
        if station.name == station_name1:
            station_1 = station
            break

    if not station_1:
        print("Station {} could not be found".format(station_name1))
        return

    dt = 10
    dates, levels = fetch_measure_levels(
        station_1.measure_id, dt=datetime.timedelta(days=dt))


    station_name2 = new[2][0]
    station_2 = None
    for station in stations:
        if station.name == station_name2:
            station_2 = station
            break

    if not station_2:
        print("Station {} could not be found".format(station_name2))
        return

    dates2, levels2 = fetch_measure_levels(
        station_2.measure_id, dt=datetime.timedelta(days=dt))

    station_name3 = new[3][0]
    station_3 = None
    for station in stations:
        if station.name == station_name3:
            station_3 = station
            break

    if not station_3:
        print("Station {} could not be found".format(station_name3))
        return

    dates3, levels3 = fetch_measure_levels(
        station_3.measure_id, dt=datetime.timedelta(days=dt))
    
    station_name4 = new[4][0]
    station_4 = None
    for station in stations:
        if station.name == station_name4:
            station_4 = station
            break

    if not station_4:
        print("Station {} could not be found".format(station_name4))
        return

    dates4, levels4 = fetch_measure_levels(
        station_4.measure_id, dt=datetime.timedelta(days=dt))

    station_name5 = new[5][0]
    station_5 = None
    for station in stations:
        if station.name == station_name5:
            station_5 = station
            break

    if not station_5:
        print("Station {} could not be found".format(station_name5))
        return

    dates5, levels5 = fetch_measure_levels(
        station_5.measure_id, dt=datetime.timedelta(days=dt))
    
    plt.plot( dates5, levels5, '-c')
    plt.plot( dates4, levels4, '-y')
    plt.plot( dates3, levels3, '-b')
    plt.plot( dates2, levels2, '-g')
    plt.plot( dates, levels, '-r')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title('Water level over the past 10 days for the 5 stations with current greatest relative water level')
    plt.show()

