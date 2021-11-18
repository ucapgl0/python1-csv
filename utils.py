import math


def haversine_distance(lat1, lon1, lat2, lon2):
    """Return the distance in km between two points around the Earth.
    
    Latitude and longitude for each point are given in degrees.
    """
    R = 6371
    arcs = math.asin
    s = math.sin
    c = math.cos
    d = 2*R*arcs(math.sqrt(s((lat2-lat1)/2)**2 + c(lat1)*c(lat2)*(s((lon2-lon1)/2)**2)))
    return d

    raise NotImplementedError

def n_min(list, n):
    a = [] 
    b = {} # set an empty dictionary 
    for i, v in enumerate(list):
        # List all indexs and elements
        b[v] = i # set value v is key and index i is value 
    list.sort()
    for j in range(n):
        # According to jth min value to find related index
        x = list[j] 
        a.append(b[x])
    return a


def n_max(list, n):
    a = [] 
    b = {} # set an empty dictionary 
    for i, v in enumerate(list):
        # List all indexs and elements
        b[v] = i # set value v is key and index i is value 
    l = list.sort()
    l.reverse()
    for j in range(n):
        # According to jth max value to find related index
        x = l[j] 
        a.append(b[x])
    return a


          