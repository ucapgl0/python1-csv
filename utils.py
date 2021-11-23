import math
import heapq



def haversine_distance(lat1, lon1, lat2, lon2): # Use in calculating nearest glaciers

    if lat2 < -90 or lat2 > 90 or lon2 < -180 or lon2 > 180:
        raise ValueError('the latitude should be between -90 and 90, the longitude between -180 and 180')
    R = 6371
    arcs = math.asin
    s = math.sin
    c = math.cos
    lat1_r = math.radians(lat1)
    lat2_r = math.radians(lat2)
    lon1_r = math.radians(lon1)
    lon2_r = math.radians(lon2)
    d = 2*R*arcs(math.sqrt(s((lat2_r-lat1_r)/2)**2 + c(lat1_r)*c(lat2_r)*(s((lon2_r-lon1_r)/2)**2)))
    return d
    
    

def n_min(list1, n): 
    # Use in find_nearest() and reverse condition of sort_by_latest_mass_balance() and plot_extremes()
    # return the index of n smallest values in list 
    min_num_index_list = map(list1.index, heapq.nsmallest(n, list1))

    return list(min_num_index_list)


def n_max(list1, n): 
    # Use in sort_by_latest_mass_balance() and plot_extremes()
    #return the index of n largest values in list
    max_num_index_list = map(list1.index, heapq.nlargest(n, list1))

    return list(max_num_index_list)







        

    