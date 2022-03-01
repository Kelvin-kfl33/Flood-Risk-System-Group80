from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
import operator
def run():
    stations = build_station_list()
    update_water_levels(stations)
    station_list = []
    for station in stations:
        if station.latest_level != None:
            station_list.append(station.name)
        elif station.latest_level == None:
            pass
    fraction_list = []
    station_profile = []
    for element in stations:
        if element.latest_level != None and element.typical_range != None:
            fraction = ( element.latest_level - element.typical_range[0] ) / (element.typical_range[1] - element.typical_range[0])       
            station_profile.append(element.name)
            fraction_list.append(fraction)
        else:
            pass
    station_dict = dict(zip(station_profile, fraction_list))
    station_dict2 = dict(sorted(station_dict.items(), key = operator.itemgetter(1), reverse = True))
    for i in station_dict2.items():
        if i[1] > 0.8 and i[1] <600 :
            print(i)
        else:
            pass

if __name__ == "__main__":
    print(" Task2B")
    run()