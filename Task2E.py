import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level
from floodsystem.flood import stations_highest_rel_level


def run():

    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)
    #Find the 5 stations with highest relative water level
    
    def plot_highest_risk(stations, N, dt):
        """This function retrieves the N most at risk stations and then plots the relative water level from the last 10 days"""
        stations_to_plot = stations_highest_rel_level(stations, N)
        for station in stations_to_plot:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_level(station, dates, levels)
        return None
    
    plot_highest_risk(stations, 5, 10)



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()