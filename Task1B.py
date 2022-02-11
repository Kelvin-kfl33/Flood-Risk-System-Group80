from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
import haversine
def run():
    """Function to produce two lists, one for the 10 closest stations, the other one for the 10 furthest stations"""
    stations = build_station_list()
    p = (52.2053, 0.1218)
    x = stations_by_distance(stations, p)
    A = x[:10]
    B = x[-10:]
    print("\nThe 10 closest stations from Cambridge are {}".format(x[:10]))
    print("\nThe 10 furthest stations from Cambridge are {}".format(x[-10:]))
    """Test the length of the lists"""
    assert len(A) == 10
    assert len(B) == 10
    return A,B

if __name__ == "__main__":
    print("Task1B")
    run()