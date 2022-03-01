
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.station import MonitoringStation

def stations_highest_rel_level(stations, N):
    highest_rel = []
    for station in stations:
        if station.relative_water_level() == None:
            continue
        else:
            highest_rel.append((station, station.relative_water_level()))
    return (sorted_by_key(highest_rel, 1, False)) [:N]
    