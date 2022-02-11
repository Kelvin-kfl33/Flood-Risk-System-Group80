from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius
MonitoringStation

def run():
    stations = build_station_list()
    r = 10
    centre = (52.2053, 0.1218)
    x = stations_within_radius(stations, centre, r)
    print(x)
    """Test to make sure the number of station presented is reasonable"""
    assert len(x) <=950

if __name__ == "__main__":
    print(" Task1C")
    run()