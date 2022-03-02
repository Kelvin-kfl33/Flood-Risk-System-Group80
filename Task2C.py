from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    
    def most_risk_stations_details(stations):
        """This function takes the 10 most at risk Monitoring Stations and prints their name and relative water level."""
        stations_most_risk = stations_highest_rel_level(stations, 10)
        for station in stations_most_risk:
            print(station.name, station.relative_water_level())

    most_risk_stations_details(stations)
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()