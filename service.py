from vincenty import vincenty
from time import sleep

cache = {}

def distance_from(origin, point):
    if cache.get((origin,point)) != None:
        return cache.get((origin,point))
    else:
        distance = vincenty(origin,point)
        cache[(origin,point)] = distance
        sleep(10)
    return distance
