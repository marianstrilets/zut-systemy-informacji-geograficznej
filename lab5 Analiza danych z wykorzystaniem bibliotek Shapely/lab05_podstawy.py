# os - modul umożliwia interakcję z systemem operacyjnym
import os
# fiona - moduł do odczytu i zapisu danych wektorowych GIS, takich jak pliki shapefile, GeoJSON czy GML.
import fiona
#numpy - moduł wykorzystywany do obliczeń numerycznych, analizy danych i naukowych obliczeń.
import numpy as np
# pyplot - moduł służącej do tworzenia wykresów i wizualizacji danych w sposób podobny do MATLAB-a.
import matplotlib.pyplot as plt
# Polygon - moduł zawiera klasy do rysowania figur geometrycznych takich jak prostokąty, koła, wielokąty itp.
from matplotlib.patches import Polygon
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.collections import PatchCollection
# geopandas - rozszerzenie Pandas, umożliwia wczytywanie i zapisywanie danych przestrzennych,
#             takich jak pliki Shapefile, GeoJSON czy PostGIS,
import geopandas as gpd
# pandas - biblioteka do manipulacji i analizy danych, wczytywanie danych z plików CSV, Excel, SQL
import pandas as pd
# json - moduł który umożliwia kodowanie i dekodowanie danych w formacie JSON (JavaScript Object Notation).
import json
# pyproj - moduł który umożliwia łatwe przeliczanie współrzędnych takich jak szerokość geograficzna,
#          długość geograficzna, współrzędne UTM
import pyproj

# shapely          - biblioteka Pythona do manipulacji geometrią
# shapely.geometry - biblioteką służącą do pracy z geometrią przestrzenną i umożliwia tworzenie,
#                    manipulowanie i analizowanie obiektów geometrycznych
import shapely.geometry as sg
import shapely.ops as sh_ops
from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry import Polygon
from shapely.geometry import MultiPoint
#   # wkt - funkcja wkt służy do parsowania tekstowej reprezentacji geometrii w formacie WKT
#   #       i tworzenia z niej obiektu geometrycznego
#   from shapely import wkt
#   # shapely.ops - zawiera wiele funkcji do przekształcania i analizowania tych obiektów.
#   # transform - służy do transformacji geometrycznych obiektów przy użyciu dostępnych transformacji
#   from shapely.ops import transform
# --------------------------------------------------------------------------------------------------------------------
# ------------------------ Tworzenie obiektów wektorowych za pomocą biblioteki shapely --------------------------------

# współrzędne pojedynczego punktu w układzie współrzędnych 1992 EPSG:2180
punkt1 = (204376, 627861)
# współrzędne pojedynczego punktu w układzie współrzędnych wgs84 EPSG:4326 (GPS)
punkt2 = (14.54771042, 53.43268351)
# współrzędna kartezjańska np. współrzędne piksela
punkt3 = (1, 1)

print('------------------------ Tworzenie obiektów wektorowych za pomocą biblioteki shapely --------------------------------\n')
print("punkt 1: \n\t" + str(punkt1))
print("punkt 2: \n\t" + str(punkt2))
print("punkt 3: \n\t" + str(punkt3))
# --------------------------------------------------------------------------------------------------------------------
# ------------------------------ Generowanie geometrii WKT za pomocą shapely ------------------------------------------

print('------------------------------ Generowanie geometrii WKT za pomocą shapely ------------------------------------------\n')
punktA = Point(punkt1)
print("Point  : \n\t" + str(punktA))

# sprawdzenie czy jest wartość z
print("Sprawdzenie czy jest wartość z punktA\n\t" + str(punktA.has_z))

print('----------------------------------------\n')
# wysokość punktu 14.7
punkt3D = Point(14.54771042, 53.43268351, 14.7)
print("Point3D: \n\t" + str(punkt3D))

# sprawdzenie czy jest wartość z
print("Sprawdzenie czy jest wartość z punkt3D\n\t" + str(punkt3D.has_z))
print('----------------------------------------\n')
# (tuple) w odróżnieniu od listy nie jesteśmy w stanie uzupełnić danymi ani jej zmienić przy wykonaniu wyskoczy błąd
punkt1 = (204376, 627861)
print(type(punkt1))  # typ obiektu - niezmienialny

punkt1 = [[204376, 627861]]
print(punkt1)
print(type(punkt1))  # typ obiektu

punkt1.append([205378, 628862])  # typ list możemy zmieniać i uzupełniać danymi
print(punkt1)
print(type(punkt1))  # typ obiektu

print('----------------------------------------\n')

punktC = Point(punkt1[0])
print(type(punktC))  # typ obiektu

points = [Point(punkt1[0]), Point(punkt1[1])]
print(type(points))
print(points)

xs = [point.x for point in points]
ys = [point.y for point in points]
print(xs)
print(ys)

plt.scatter(xs, ys)
plt.show()

multiPoints = MultiPoint(points)
print(multiPoints)
print(list(punktC.coords))

# współrzędne pojedynczego punktu w układzie współrzędnych 1992 EPSG:2180
punkt1 = Point(204376, 627861)
punkt2 = Point(204396, 627811)
# współrzędne pojedynczego punktu w układzie współrzędnych WGS84 EPSG:4326
punkt3 = Point(14.54771042, 53.43268351)
# odległość pomiędzy punktami Musi być ten sam układ współrzędnych
print(round(punkt1.distance(punkt2), 2), 'm')

# --------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Generowanie linii ---------------------------------------------------

print('----------------------------------------------- Generowanie linii ---------------------------------------------------\n')

linia = LineString([punkt1, punkt2])
print(linia)
print(type(linia))
print(linia.coords)

xcoords = list(linia.xy[0])
ycoords = list(linia.xy[1])
print(xcoords, ycoords)

# linia posiada długość jako atrybut geometrii
print(round(linia.length, 2), "m")


# --------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Generowanie polygonu ------------------------------------------------
print('----------------------------------------------- Generowanie polygonu ------------------------------------------------')
# współrzędne pojedynczego punktu w układzie współrzędnych 1992 EPSG:2180
punkt1 = Point(204376, 627861)
punkt2 = Point(204376, 627861)
punkt3 = Point(204376, 627861)
punkt4 = Point(204376, 627861)

polygon = Polygon([punkt1, punkt2, punkt3, punkt4])
print(polygon)

# tworzenie polygonu metodą iteracji
polygon = Polygon([[p.x, p.y] for p in [punkt1, punkt2, punkt3, punkt4]])
print(polygon)

# --------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Gotowa definicja WKT ------------------------------------------------
print('----------------------------------------------- Gotowa definicja WKT ------------------------------------------------')
polygon1 = wkt.loads('Polygon ((204525.05 626993.47, 204219.86 627046.75, 204225.19 627131.91, 203898.25 627918.83, 203932.8 627936.68, 204146.52 628156.93, 204289.82 628256.23, 204491.43 628283.51, 204809.01 628064.23, 205238.93 628088.68, 205056.98 627644.16, 204911.95 627334.07, 204738.38 627390.5, 204669.03 627377.73, 204525.05 626993.47))')
polygon2 = wkt.loads(
    'Polygon ((204371.52 628148.42, 204170.55 628003.35, 203981.56 627433.7, 204198.5 627171.5, 204760.16 627517.55, 204706.92 627988.71, 204371.52 628148.42))')

print(polygon1)
print(polygon2)
# --------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Operacje geometrii --------------------------------------------------
print('----------------------------------------------- Operacje geometrii --------------------------------------------------')
unionpolygon = polygon1.union(polygon2).boundary        # złączenie
print(unionpolygon)

symdifpolygon = polygon1.symmetric_difference(polygon2)  # różnica
print(symdifpolygon)

difpolygon = polygon1.difference(polygon2)              # różnica
print(difpolygon)

intersecpolygon = polygon1.intersection(polygon2)       # przecięcie
print(intersecpolygon)

# Zwraca True jeśli geometrie mają więcej niż jeden, ale nie wszystkie punkty wspólne
overlapspolygon = polygon1.overlaps(polygon2)
print(overlapspolygon)

# Zwraca True, jeśli obiekty mają przynajmniej jeden punkt wspólny, a ich wnętrza nie przecinają się z żadną częścią drugiego obiektu.
touchespolygon = polygon1.touches(punkt1)
print(touchespolygon)

# Zwraca True jeśli granica i wnętrze obiektu przecinają się tylko z wnętrzem drugiego obiektu
punkt1 = wkt.loads('Point (204376.84 627862.61)')
withinpolygon = punkt1.within(polygon1)
print(withinpolygon)

bufferpolygon = punkt1.buffer(
    50, resolution=20, cap_style=3, join_style=1, mitre_limit=5.0, single_sided=False)
print(bufferpolygon)

#   cap_style:
#       1-koło
#       2-płaski
#       3-kwadrat
#   join_style:
#       1-okrągłe
#       2-ukośnie
#       3-skośnie

linia = wkt.loads(
    'LineString (-0.67603306 0.78842975, -0.78181818 -0.13553719, -0.2661157 -0.52066116, 0.59338843 0.03305785, -1.06942149 0.47107438)')
print(linia)

bufor = linia.buffer(0.2, resolution=4, cap_style=2, join_style=1)
print(bufor)

bufor2 = bufor.buffer(-0.1)
print(bufor2)

lewy = linia.buffer(-0.2, single_sided=True)
print(lewy)

# wpasowanie obiektu w prostokąt
linia.minimum_rotated_rectangle

# Zwraca reprezentację punktu lub najmniejszego wielokąta prostokątnego (o bokach równoległych do osi współrzędnych), który zawiera obiekt.
linia.envelope

# Zwraca reprezentację najmniejszego wielokąta zawierającego wszystkie punkty w obiekcie,
# chyba że liczba punktów w obiekcie jest mniejsza niż trzy
linia.convex_hull

linia_source = wkt.loads(
    'LineString (-0.67603306 0.78842975, -0.78181818 -0.13553719, -0.2661157 -0.52066116, 0.59338843 0.03305785, -1.06942149 0.47107438)')
linia_offset = linia_source.parallel_offset(
    0.8, resolution=16, join_style=1, mitre_limit=1)  # oodsunięcie linii
x, y = linia_offset.xy
plt.plot(x, y)
x, y = linia_source.xy
plt.plot(x, y)
plt.show()

bufor = punkt1.buffer(100, resolution=100, cap_style=1,
                      join_style=1, mitre_limit=5.0, single_sided=False)  # bufor
bufor_simplify = bufor.simplify(20, preserve_topology=False)

plt.rcParams["figure.figsize"] = [7, 7]
plt.rcParams["figure.autolayout"] = True
x, y = bufor.exterior.xy
plt.plot(x, y, c="red")
x, y = bufor_simplify.exterior.xy
plt.plot(x, y, c="black")
plt.show()

# --------------------------------------------------------------------------------------------------------------------
# ---------------------------------------- Konwersja typów struktur danych -------------------------------------------
print('---------------------------------------- Konwersja typów struktur danych -------------------------------------------')

df = pd.read_csv('budynki_multi.csv', sep='\t')
results = []
for index, row in df.iterrows():
    budynek = wkt.loads(row['wkt_geom'])
    print(row['wkt_geom'])
    results.append(wkt.loads(row['wkt_geom']))

dfhead = df.head()
print(dfhead)

budynek = (results[7])
print(round(budynek.area, 2), 'sq m')

polyout = sh_ops.unary_union(results)  # grupowanie geometrii
print(polyout)
print(type(polyout))

polygon = list(polyout.geoms)
print(polygon)

lista = [poly.exterior.coords for poly in list(
    polyout.geoms)]  # rozgrupowanie geometrii
print(lista)
print(type(lista))

budynek = Polygon(lista[0])  # linia do polygon
print(budynek)
print(type(budynek))

print(type(budynek.exterior.xy))  # linie zewnętrzne budynków

lista = [poly.exterior.coords for poly in list(polyout.geoms)]
plt.rcParams["figure.figsize"] = [7, 7]
plt.rcParams["figure.autolayout"] = True
i = 0
for x in lista:
    budynek = Polygon(lista[i])
    x, y = budynek.exterior.xy
    plt.plot(x, y)
    i += 1
plt.show()

lista = [poly.exterior.coords for poly in list(polyout.geoms)]
i=0
export_wkt = []
for x in lista:
    budynek=Polygon(lista[i]) #linia do polygonu
    export_wkt.append(budynek)
    i+=1
print(export_wkt[0])

df = pd.DataFrame(export_wkt) #shapely do pandas dataframe
df.columns=['geometria']
print(df.head())

gdf = gpd.GeoDataFrame(df, geometry='geometria') #pandas dataframe do geopandas
gdf.plot()
plt.show()

