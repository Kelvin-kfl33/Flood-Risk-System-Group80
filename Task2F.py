<<<<<<< HEAD
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
=======
import datetime
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_measure_levels, fetch_station_data
>>>>>>> 56538b438530e0866f0e21d22d6309e856d96054
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
<<<<<<< HEAD
import datetime
=======
from floodsystem.station import MonitoringStation

>>>>>>> 56538b438530e0866f0e21d22d6309e856d96054

def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest_stations = stations_highest_rel_level(stations, 5)
    for station in highest_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        plot_water_level_with_fit(station, dates, levels, 4)

<<<<<<< HEAD
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
=======
    top_5 = stations_highest_rel_level(stations, 5)
    
    top_55 = []
    print(top_5)
    
    for val in top_5:
        dates, level = fetch_measure_levels(val[0].measure_id, datetime.timedelta(days = 2))

        plot_water_level_with_fit(val[0], dates, level, 4)
    
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()

>>>>>>> 56538b438530e0866f0e21d22d6309e856d96054
