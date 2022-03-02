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