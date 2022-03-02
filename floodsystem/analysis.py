import numpy as np
import matplotlib

def polyfit(dates, levels, p):
   
    dates_1 = matplotlib.dates.date2num(dates)
    
    poly_1 = np.polyfit(dates_1 - dates_1[0], levels, 1)

    poly = np.poly1d(poly_1)
    
    return poly, dates_1[0]