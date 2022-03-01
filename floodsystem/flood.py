
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
import operator

# def stations_highest_rel_level(stations, N):
#     highest_rel = []
#     for station in stations:
#         if station.relative_water_level() == None:
#             continue
#         else:
#             highest_rel.append((station, station.relative_water_level()))
#     return (sorted_by_key(highest_rel, 1, False)) [:N]
    
def stations_level_over_threshold(stations, tol):

    update_water_levels(stations)

    fraction_list = []
    station_profile = []

    for i in stations:
        if i.relative_water_level() != None:
            fraction_list.append(i.relative_water_level())
            station_profile.append(i.name)
        else:
            pass
    
    station_dict = dict(zip(station_profile, fraction_list))
    station_dict2 = dict(sorted(station_dict.items(), key = operator.itemgetter(1), reverse = True))
    
    for i in station_dict2.items():
        if i[1] > tol and i[1] <660 :
            print(i)
        else:
            pass