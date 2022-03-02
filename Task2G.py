
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list


def risk():
    stations = build_station_list()
    risk = []
    severe_stations = []
    stations_1 = stations_highest_rel_level(stations, 10)
    for val in stations_1:
        severe_stations.append(val[0].name)
   
    for val in stations:

        if val in severe_stations:
            risk.append((val.name, 'Severe'))

    print(risk)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    risk()