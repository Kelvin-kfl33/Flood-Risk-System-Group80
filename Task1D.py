from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """The function gives how many rivers have at least one monitoring station"""
    """Also, it gives the  names of the stations located on the specific rivers"""
    x = build_station_list()
    y = rivers_with_station(x)
    z = stations_by_river(x)
    ans1 = z['River Aire']
    ans2 = z['River Cam']
    ans3 = z['River Thames']

    print(y)
    print(ans1)
    print(ans2)
    print(ans3)
    return y, ans1, ans2 ,ans3

if __name__ == "__main__":
    print(" Task1C")
    run()