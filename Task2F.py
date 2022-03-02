import datetime
from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_measure_levels, fetch_station_data
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
from floodsystem.station import MonitoringStation


def run():

    stations = build_station_list()   
    update_water_levels(stations)

    top_5 = stations_highest_rel_level(stations, 5)
    
    top_55 = []
    print(top_5)
    
    for val in top_5:
        dates, level = fetch_measure_levels(val[0].measure_id, datetime.timedelta(days = 2))

        plot_water_level_with_fit(val[0], dates, level, 4)
    
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()

