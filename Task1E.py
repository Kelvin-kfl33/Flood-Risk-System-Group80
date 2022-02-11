from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    x = rivers_by_station_number(stations, 9)  ## shows rivers with top 9 number of stations, not the top 9 position in the river list
    print(x)
    N = 1
    return x, N


if __name__ == "__main__":
    print(" Task1E")
    run()