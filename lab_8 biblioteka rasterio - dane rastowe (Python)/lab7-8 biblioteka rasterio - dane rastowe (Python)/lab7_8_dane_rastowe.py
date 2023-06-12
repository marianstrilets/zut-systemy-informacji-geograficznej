import rasterio
from rasterio.plot import show
# import rasterio.features
# import rasterio.warp
# from rasterio.transform import Affine
# from rasterio.plot import show_hist
from rasterio.transform import from_origin
from rasterio.warp import transform_bounds

import numpy as np
from matplotlib import pyplot as plt
# =======================================================================================================
# 1.  Pobierz ze strony https://mapy.geoportal.gov.pl/imap/Imgp_2.html?gpmap=gp0 
#   dowolny numeryczny model terenu. Dokonaj jego wizualizacji wykorzystując parametry cieniowania i 
#   przykład w z wykładu. Zapisz plik w formacie geotiff i układzie współrzędnych PL1992(EPS:2180)#   
# =======================================================================================================

# Otwarcie obrazu
input_file = './szczecin.tif'
output_file = './szczecin_cieniowanie.tif'

# Wczytanie danych
image = rasterio.open(input_file)
raster = image.read(1) # Wczytanie danych z pierwszej warstwy obrazu

# Wyswietlania informacji o wczytanym pliku
print('\n\tnazwa:    ', image.name)
print('\tszerokość:', image.width) 
print('\twysokosc: ', image.height) 

# Wizualizacja
plt.figure('Numeryczny model terenu (Szczecin)')
plt.imshow(raster)
plt.colorbar()
plt.title('Numeryczny model terenu (Szczecin)')
plt.savefig('./_szczecin.png')
plt.show()

# -------- Tworzenie cieniowania ----------
# Kierunek oświetlenia
azimuth = 315                       
azimuth_rad = np.radians(azimuth)   
# Wzniesienia słońca nad horyzontem
angle_altitude = 45                        
altitude = np.radians(90 - angle_altitude)

dx, dy = np.gradient(raster)                    # Obliczenie gradientów w kierunkach x i y
slope = np.pi/2 - np.arctan(np.hypot(dx, dy))   # Obliczenie nachylenia terenu
aspect = np.arctan2(dx, dy)                     # Obliczenie aspektu terenu

shaded_data = np.sin(altitude) * np.sin(slope) + np.cos(altitude) * np.cos(slope) * np.cos(azimuth_rad - aspect)
shaded_data = (shaded_data + 1) / 2  # Skalowanie do zakresu 0-1

# Zapisanie do nowego pliku geotiff
profile = image.profile                         # Pobranie metadanych obrazu wejściowego
profile.update(dtype=rasterio.float32, count=1)  # Zaktualizowanie typu danych i liczby warstw obrazu

with rasterio.open(output_file, 'w', **profile) as dst:     # Otwarcie pliku
    dst.write(shaded_data.astype(rasterio.float32), 1)      # Zapisanie danych cieniowania do warstwy 1
    dst.crs = rasterio.crs.CRS.from_epsg(2180)              # Ustawienie układu współrzędnych na PL1992 (EPSG:2180)
    dst.transform = image.transform                         # Przypisanie transformacji przestrzennej z obrazu wejściowego

# Wizualizacja z parametrami cieniowania
plt.figure('Numeryczny model terenu z cieniowaniem (Szczecin)')
plt.imshow(shaded_data, cmap='gray')  
plt.title('Numeryczny model terenu z cieniowaniem (Szczecin)')  
plt.colorbar()  
plt.savefig('./_szczecin_cieniowanie.png')
plt.show()  
