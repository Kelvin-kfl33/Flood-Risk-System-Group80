from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    
    # Alternative implementation
    # for station in [s for s in stations if s.name in names]:
    #     print("Station name and current level: {}, {}".format(station.name,
    #                                                           station.latest_level))
    def relative_water_details(stations, tol=0.8):
        relative_water_stations = stations_level_over_threshold(stations, tol)
        for station in relative_water_stations:
            print(station[0].name, station[1])

    relative_water_details(stations, 0.95)


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()