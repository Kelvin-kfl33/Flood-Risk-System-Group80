class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """This method looks at the typical range value for each monitoring station and if
        it is None (i.e no data) or the low range is greater than the high range we return
        a boolean value to mark/demonstrate that it contains inconsistent data. Therefore
        we do not want to include it in our data."""
        #Test first for no data available
        if self.typical_range == None:
            return False
        #Test if first tuple value is larger than the second tuple value
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        #If both these tests are passed we can mark the monitoring station as containing consistent data
        else:
            return True

    def relative_water_level(self):
        """This method looks at the lastest update for river level and returns it as a fraction of the typical range."""
        if self.typical_range_consistent() == False:
            return None
        elif self.latest_level == None:
            return None
        else:
            relative_level = (self.latest_level - self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
            return (relative_level)
            


def inconsistent_typical_range_stations(stations):
    """This function calls the typical range data method and if the monitoring station is marked
    to be inconsistent it is appended to a list of stations (MonitoringStation) which have
    inconsistent range data. This list is returned without being sorted"""
    inconsistent_stations = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent_stations.append(station)
    return inconsistent_stations
