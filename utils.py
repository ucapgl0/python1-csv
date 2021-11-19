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


def create_name_LastMeasurement_dict(name, value):
    d = {}
    for i in range(len(name)):
        if value[i] == '':
            value[i] = 0
        if i < len(name) - 1:
            if name[i] != name[i+1]:
                d[name[i]] = float(value[i])
        else:
            d[name[i]] = float(value[i])
    return d
     

def find_key(dictionary,value1):
    for key in dictionary:
        if dictionary[key] == value1:
            return key


def return_object(Object_name, glacier_id, name, unit, lat, lon, code):
    for i in range(len(name)):
        if name[i] == Object_name:
            return [glacier_id[i], name[i], unit[i], lat[i], lon[i], code[i]]


def calculate_shunk_rate(list1):
    a = 0
    for i in range(len(list1)):
        if list1[i] < 0:
            a += 1
    b = a / len(list1)
    c = int(round(b,2) * 100)
    return c
          