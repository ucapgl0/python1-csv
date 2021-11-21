import math
import heapq
import matplotlib.pyplot as plt


def haversine_distance(lat1, lon1, lat2, lon2): # Use in calculating nearest glaciers
    """Return the distance in km between two points around the Earth.
    
    Latitude and longitude for each point are given in degrees.
    """
    if lat2 < -90 or lat2 > 90 or lon2 < -180 or lon2 > 180:
        raise NotImplementedError('the latitude should be between -90 and 90, the longitude between -180 and 180')
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
    
    raise NotImplementedError


def n_min(list1, n): 
    # Use in find_nearest() and reverse condition of sort_by_latest_mass_balance() and plot_extremes()
    
    min_num_index_list = map(list1.index, heapq.nsmallest(n, list1))

    return list(min_num_index_list)


def n_max(list1, n): 
    # Use in sort_by_latest_mass_balance() and plot_extremes()

    max_num_index_list = map(list1.index, heapq.nlargest(n, list1))

    return list(max_num_index_list)




def calculate_shunk_rate(list1):
    # Use for summary()
    a = 0
    for i in range(len(list1)):
        if list1[i] < 0:
            a += 1
    b = a / len(list1)
    c = int(round(b,2) * 100)
    return c


def mass_change(Object_name, name, year, value):
    
    a = []
    d = {}
    for i in range(len(name)):
        if name[i] == Object_name:
            a.append(i)  
    a1 = a[0]
    a2 = a[-1]
    for i1 in range(a1, a2+1):
        if value[i1] == '':
            value[i1] = 0
    c = -1
    boolean = []
    mass_balance = []
    if a1 == a2:
        boolean.append(False)        
        d[int(year[a1])] = float(value[a1])

    else:
        for i2 in range(a1, a2 + 1):
            if i2 < a2:
                c += 1
                if year[i2] != year[i2+1]:
                    k = i2 + 1            
                    if c >= 1:
                        for j in range(i2-c, i2+1):
                            mass_balance.append(float(value[j])) 
                        boolean.append(True)   
                        d[int(year[i2])] = mass_balance
                        c = -1
                        mass_balance = []
                    else:
                        boolean.append(False)
                        d[int(year[i2])] = float(value[i2]) 
                        c = -1
            else:
                if year[i2] != year[i2-1]:
                    boolean.append(False)
                    d[int(year[i2])] = float(value[i2])
                else:
                    for i3 in range(k, a2 + 1):
                        mass_balance.append(float(value[i3]))
                    boolean.append(True)
                    d[int(year[i2])] = mass_balance
      
    return d, boolean


def plot(dictionary):
        
    return plt.show()

        

    