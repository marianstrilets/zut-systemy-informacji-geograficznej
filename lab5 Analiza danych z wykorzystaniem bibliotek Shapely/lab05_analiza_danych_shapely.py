import pandas as pd
import geopandas as gpd
from shapely.geometry import MultiPolygon, Point
import pyproj
from shapely.ops import transform
from shapely import wkt
import matplotlib.pyplot as plt

#================================================================================================================
#---------------------------------------- Zadania: --------------------------------------------------------------
#   1.  Zmień odwzorowanie warstwy budynki z EPSG:2180 do EPSG:4326
print('\n\t=================== Zadanie 1 ====================\n')
#----------------------------------------------------------------------------------------------------------------
## Definiowanie systemów odwzorowań
crs_2180 = pyproj.CRS.from_epsg(2180)  # EPSG:2180 - układ współrzędnych dla Polski (PUWG 1992)
crs_4326 = pyproj.CRS.from_epsg(4326)  # EPSG:4326 - WGS84 (geograficzny układ współrzędnych)

# Odczyt pliku CSV do geopandas.DataFrame
gdf = gpd.read_file('budynki_multi.csv', GEOM_POSSIBLE_NAMES="wkt_geom", KEEP_GEOM_COLUMNS="NO", crs=crs_2180)

# Tworzenie transformacji
project = pyproj.Transformer.from_crs(crs_2180, crs_4326, always_xy=True)
point_crs2180 = []
point_crs4326 = []

for geometry in gdf.geometry:
    if geometry.geom_type == 'MultiPolygon':
        for polygon in geometry:
            for point in polygon.exterior.coords:
                lon, lat = point
                point_crs2180 = Point(lon, lat)
                point_crs4326 = transform(project.transform, point_crs2180) 
                print(f"\nWspółrzędne (lon, lat) w układzie 2180: {point_crs2180.x}, {point_crs2180.y}")
                point_crs4326 = transform(project.transform, point_crs2180)
                print(f"Współrzędne (lon, lat) w układzie 4326: {point_crs4326.x}, {point_crs4326.y}")
#================================================================================================================
#   2.  Oblicz sumaryczną powierzchnię budynków z pliku csv w klasach. (ocena dostateczna)
print('\n\t=================== Zadanie 2 ====================\n')
#================================================================================================================
df=pd.read_csv('budynki_multi.csv', sep='\t')
results = []
suma=0
for index, row in df.iterrows():
    budynek=wkt.loads(row['wkt_geom'])
    results.append(wkt.loads(row['wkt_geom']))
    p2 = transform(project.transform, budynek)
    suma+= budynek.area
print("Suma powierzchni budynków wynosi:", suma)
#================================================================================================================
