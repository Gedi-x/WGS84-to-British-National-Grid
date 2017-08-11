
# coding: utf-8

from pyproj import Proj, transform
import numpy as np

uk = '+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.9996012717 +x_0=400000 +y_0=-100000 +ellps=airy +towgs84=446.448,-125.157,542.06,0.15,0.247,0.842,-20.489 +units=m +no_defs'

# project wgs86  to british national grid
def proj_arr(points,proj_to):
    
    inproj = Proj(init='epsg:4326')
    outproj = Proj(proj_to)
    func = lambda x: transform(inproj,outproj,x[0],x[1])
    return np.array(list(map(func, points)))

def proj_arr_uk(points):
    
    inproj = Proj(init='epsg:4326')
    outproj = Proj(uk)
    func = lambda x: transform(inproj,outproj,x[0],x[1])
    return np.array(list(map(func, points)))

#example
#proj_arr_uk([[0.2,50]])





