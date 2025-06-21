"""
geo_utils.py

Geospatial utility functions to support the FindMyRoute project.

Author: Amna Azeem
"""

import osmnx as ox
import geopandas as gpd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from shapely.geometry import Point  # imported here since used below

def load_city_road_network(city_name):
    """
    Download road network of a city using OSMnx.

    Args:
        city_name (str): Name of the city (e.g. 'Salzburg, Austria')

    Returns:
        networkx.MultiDiGraph: Road network graph of the city
    """
    graph = ox.graph_from_place(city_name, network_type='drive')
    return graph

def get_tourist_locations(place_names):
    """
    Convert a list of tourist attraction names to coordinates.

    Args:
        place_names (list): List of strings like ['Mirabell Palace, Salzburg']

    Returns:
        list: List of (name, latitude, longitude)
    """
    geolocator = Nominatim(user_agent="findmyroute")
    results = []

    for name in place_names:
        location = geolocator.geocode(name)
        if location:
            results.append((name, location.latitude, location.longitude))
        else:
            results.append((name, None, None))
    return results

def calculate_pairwise_distances(loc_list):
    """
    Calculate pairwise geodesic distances between locations.
    
    Args:
        loc_list (list): List of tuples (place_name, latitude, longitude)
        
    Returns:
        list of tuples: (place1, place2, distance_in_km)
        
    Notes:
        Locations with missing latitude or longitude are skipped.
    """
    distances = []
    for i in range(len(loc_list)):
        for j in range(i + 1, len(loc_list)):
            place1, lat1, lon1 = loc_list[i]
            place2, lat2, lon2 = loc_list[j]
            
            # Skip if any coordinate is None or missing
            if None in (lat1, lon1, lat2, lon2):
                continue
            
            dist = geodesic((lat1, lon1), (lat2, lon2)).km
            distances.append((place1, place2, dist))
    return distances

from statistics import mean

def calculate_geographic_centroid(locations):
    """
    Calculate the geographic center (centroid) of a list of coordinates.

    Args:
        locations (list): List of tuples (name, latitude, longitude)

    Returns:
        tuple: (centroid_latitude, centroid_longitude)
    """
    latitudes = []
    longitudes = []

    for name, lat, lon in locations:
        if lat is not None and lon is not None:
            latitudes.append(lat)
            longitudes.append(lon)

    if not latitudes or not longitudes:
        return None, None

    return mean(latitudes), mean(longitudes)

def filter_valid_locations(loc_list):
    """Remove locations with missing lat/lon values."""
    return [loc for loc in loc_list if None not in (loc[1], loc[2])]












