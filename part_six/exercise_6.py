'''
In this exercise we will write some functions for working on a 
file containing location data from the stations for city bikes in Helsinki.

First, write a function named get_station_data(filename: str). 
This function should read the names and locations of all the stations in the file, 
and return them in a dictionary.

Dictionary keys are the names of the stations, 
and the value attached is a tuple containing the location coordinates of the station. 
The first element in the tuple is the Longitude field, and the second is the Latitude field.

Next, write a function named distance(stations: dict, station1: str, station2: str), 
which returns the distance between the two stations given as arguments.

The distance is calculated using the Pythagorean theorem. 
The multiplication factors below are approximate values for converting 
latitudes and longitudes to distances in kilometres in the Helsinki region.


Please write a function named greatest_distance(stations: dict), 
which works out the two stations on the list with the greatest distance from each other. 
The function should return a tuple, 
where the first two elements are the names of the two stations, 
and the third element is the distance between the two.
'''

def get_station_data(filename: str):
    station_data = {}
    with open(filename) as f:
        for line in f:
            parts = line.split(';')
            
            if parts[0] == 'Longitude':
                continue
            
            station_data[parts[3]] = float(parts[0]), float(parts[1])


    return station_data


def distance(stations: dict, station1: str, station2: str):
    import math

    for station in stations:
        longitude1 = stations[station1][0]
        latitude1 = stations[station1][1]
        longitude2 = stations[station2][0]
        latitude2 = stations[station2][1]


    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations):
    import math

    greatest_distance = 0
    station1_name, station2_name = None, None
    for station1 in stations:
        for station2 in stations:
            if station1 != station2:
                x_km = (stations[station1][0] - stations[station2][0]) * 55.26
                y_km = (stations[station1][1] - stations[station2][1]) * 111.2
                distance_km = math.sqrt(x_km**2 + y_km**2)
                if distance_km > greatest_distance:
                    greatest_distance = distance_km
                    station1_name, station2_name = station1, station2
    return (station1_name, station2_name, greatest_distance)
