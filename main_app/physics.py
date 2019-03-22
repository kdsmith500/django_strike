import math

g = -9.81
theta = math.pi / 3

lat1 = 33.729759
lon1 = -111.431221 
lat2 = 36.116203
lon2 = -119.681564


# obtain great circle distance between 2 points:

def R(origin, target):
    lat1, lon1 = origin
    lat2, lon2 = target
    radius = 6371e3 #in meters

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d


print(R((lat1, lon1), (lat2, lon2)))