# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine
from .utils import sorted_by_key  # noqa



def stations_by_distance(stations, p):
    """Give a list with the readings of stations names, stations towns, stations distance from a given coordinate"""
    stations_name = []
    stations_towns = []
    stations_distance = []
    for station in stations:
        distance = haversine(p, station.coord)
        if station is not stations:
            stations_name.append(station.name)
            stations_towns.append(station.town)
            stations_distance.append(distance)
        else:
            pass
    tuples = list(zip(stations_name, stations_towns, stations_distance))
    tuples = sorted_by_key(tuples, 2)
    assert len(stations_name) <5000
    return tuples

def stations_within_radius(stations, centre, r):
    """Give stations within a given radius with respect to the city centre"""
    station_list = []
    for i in stations:
        distance = haversine(centre, i.coord)
        if distance <= r:
            station_list.append(i.name)
        elif distance > r:
            pass
    station_list = sorted(station_list)
    assert len(station_list) < 3000
    return station_list

def rivers_with_station(stations):
    """Give rivers and their corresponding stations number"""
    rivers_name = []
    stations_number = []
    for station in stations:
        if station.river not in rivers_name:
            rivers_name.append(station.river)
        else:
             pass
    for i in rivers_name:  ## start looping through the river_name list
        a = 0  ## counting 
        for n in stations: ## double loop, to loop through the big stations list
            if i == n.river:
                a += 1
            else:
                pass
        stations_number.append(a)
    tuples = list(zip(rivers_name, stations_number))
    tuples = sorted_by_key(tuples, 1)
    Low_bound_station = 1
    river_list = []
    for i in tuples:  ## start looping through the list of tuples
        if i[1] >= Low_bound_station:
            river_list.append(i[0])
        if i[1] < Low_bound_station:
            continue
    river_list = sorted(river_list)
    assert len(river_list) == 950
    return river_list[:10]

def stations_by_river(stations):
    """Give a dictionary to hold the rivers name as keys and their corresponding stations' name as values"""
    rivers_name = []
    for i in stations:
        if i.river not in rivers_name:
            rivers_name.append(i.river)
        elif i.river in rivers_name:
            continue
    big_list = []
    for n in rivers_name:
        lists = []
        for y in stations:
            if n == y.river:
                lists.append(y.name)
            elif n != y.river:
                continue
        lists = sorted(lists)
        big_list.append(lists)
    dictionary = dict(zip(rivers_name, big_list))
    dicti = {}
    for key in sorted(dictionary):
        dicti.update({key : dictionary[key]})
    assert dicti != {}
    return dicti

def rivers_by_station_number(stations, N):
    """Give ranked rivers name, according to their number of stations"""
    rivers_name = []
    stations_number = []
    for station in stations:
        if station.river not in rivers_name:
            rivers_name.append(station.river)
        else:
             pass
    for i in rivers_name:  ## start looping through the river_name list
        a = 0  ## counting 
        for n in stations: ## double loop, to loop through the big stations list
            if i == n.river:
                a += 1
            else:
                pass
        stations_number.append(a)
    tuples = list(zip(rivers_name, stations_number))
    tuples = sorted_by_key(tuples, 1)
    tuples = tuples[::-1]
    """To set the number of outputs based on the number ranking of stations (intead of pre positions of river in rivers_name list) """
    """Assuming we start counting at 1, i.e 1,2,3.... Hence the N-1 is shown below"""
    Low_bound_station = tuples[N-1][1]
    count = 0
    for i in tuples:  ## start looping through the list of tuples
        if i[1] >= Low_bound_station:
            count += 1
        if i[1] < Low_bound_station:
            break
    assert tuples != None
    return tuples[:count]