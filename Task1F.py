from unicodedata import name
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    print(inconsistent_stations)
    length = len(inconsistent_stations)
    return length

if __name__ == "__main__":
    print(" Task1F")
    run()