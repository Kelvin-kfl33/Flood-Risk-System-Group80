<<<<<<< HEAD
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import floodrisk
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
import datetime
import matplotlib.dates

def run():
    stations = build_station_list()
    update_water_levels(stations)
    low = []
    moderate = []
    high = []
    severe = []
    counter = 0
    for station in stations:
        counter += 1
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        risk = floodrisk(station, dates, levels)
        print(risk)
        if station.town == None:
            pass
        else:
            if risk == 'severe':
                severe.append(station.town)
            elif risk == 'high':
                high.append(station.town)
            elif risk == 'moderate':
                moderate.append(station.town)
            elif risk == 'low':
                low.append(station.town)
            if counter == 50:
                break
    print('severe:')
    print(severe)
    print('high:')
    print(high)
    print('moderate:')
    print(moderate)
    print('low:')
    print(low)
    print(counter)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
=======

from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list


def risk():
    stations = build_station_list()
    risk = []
    severe_stations = []
    stations_1 = stations_highest_rel_level(stations, 10)
    for val in stations_1:
        severe_stations.append(val[0].name)
   
    for val in stations:

        if val in severe_stations:
            risk.append((val.name, 'Severe'))

    print(risk)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    risk()
>>>>>>> d9d126ae9fa14c8e1477dd1107664be44dfe06a6
