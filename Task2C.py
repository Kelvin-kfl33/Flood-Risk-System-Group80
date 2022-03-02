from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_station_data
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():

    stations = build_station_list()   
    update_water_levels(stations)
    ans = stations_highest_rel_level(stations, 10)
    for val in ans:
        print(val[0].name, val[1])

if __name__ == "__main__":
    print("***Task 2C: CUED Part 1A Flood Warning System")
    run()