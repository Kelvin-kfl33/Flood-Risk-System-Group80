from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels

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
            station.append
            fraction_list.append(fraction)


        else:
            pass
    ans = sorted(fraction_list)
    for i in ans:
        if i > 0.8:
            print(i)
        else:
            pass
        # if element.fraction >= 0.8:
        #     target_list.append(element)

run()