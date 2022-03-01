import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from floodsystem.datafetcher import fetch_measure_levels

def dates_levels(station):
    dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
    return dates, levels 
    
def plot_water_levels(station, dates, levels):
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))

    level = []
    time = [datetime(2022, 2, 1 + dt) for dt in range(0,30)]

