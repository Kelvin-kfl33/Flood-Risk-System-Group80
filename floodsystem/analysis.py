from this import d
import matplotlib.dates
import numpy as np
from floodsystem.station import MonitoringStation

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    x0 = x[0]
    y = levels
    p_coeff = np.polyfit(x - x0, y, p)
    poly = np.poly1d(p_coeff)
    return poly, x0

def floodrisk(station, dates, levels):
    risk = 0
    #determine risk with relative water level
    global relative_level
    if station.typical_range_consistent() == False:
        pass
    elif station.latest_level == None:
        pass
    else:
        relative_level = relative_level = (station.latest_level - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])

    if relative_level > 1.5:
        risk += 5
    elif relative_level > 1:
        risk += 3
    elif relative_level > 0.5:
        risk += 1
    else:
        risk += 0

    #determine risk with tendency of change of water level
    global gradient
    x = matplotlib.dates.date2num(dates)
    if len(x) == 0:
        pass
    else:
        x1 = np.linspace(x[0], x[-1], 100)
        if len(x - x[0]) != len(levels):
            pass
        elif len(x - x[0]) != len(levels):
            pass
        else:
            try: 
                p_coeff = np.polyfit(x - x[0], levels, 4)
                poly = np.poly1d(p_coeff)
                gradient = (poly(x1[-1] - x[0]) - poly(x1[0] - x[0]))
            except TypeError:
                pass

    if gradient > 1:
        risk += 3
    elif gradient > 0.5:
        risk += 1
    elif gradient < 0:
        risk -= 1
    else:
        risk += 0
    
    if risk <= 1:
        return 'low'
    elif risk == 2:
        return 'moderate'
    elif risk == 3:
        return 'high'
    else: 
        return 'severe'