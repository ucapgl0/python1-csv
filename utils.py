import math
import heapq

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

def n_min(list1, n):
    
    max_num_index_list = map(list1.index, heapq.nsmallest(n, list1))

    return list(max_num_index_list)


def n_max(list1, n):

    max_num_index_list = map(list1.index, heapq.nlargest(n, list1))

    return list(max_num_index_list)

def find_key(dictionary,value1):
    for key in dictionary:
        if dictionary[key] == value1:
            return key

def return_object(Object_name, glacier_id, name, unit, lat, lon, code):
    for i in range(len(name)):
        if name[i] == Object_name:
            return [glacier_id[i], name[i], unit[i], lat[i], lon[i], code[i]]


          