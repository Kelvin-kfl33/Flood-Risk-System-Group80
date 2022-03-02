from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def run():

    stations = build_station_list()
    stations_level_over_threshold(stations , tol = 1.5)
    
if __name__ == "__main__":
    print(" Task2B")
    run()