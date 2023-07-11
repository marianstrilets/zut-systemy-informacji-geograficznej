--===============================================================================================================================
-- Napisz formuły SQL generujące mapy lub zwracające dane z bazy danych GeoPackage: 
--===============================================================================================================================
-- 1.  Proszę napisać formułę SQL obliczającą całkowitą powierzchnię budynków 
-- mieszkalnych [m2] z podziałem na klasy: BUBD-01 -> BUBD04 w poszczególnych 
-- dzielnicach Szczecina. Powierzchnia mieszkalna = „podstawa*liczba pięter”.
-- Wartość proszę zaokrąglić do dwóch miejsc po przecinku. 
--    1.  W jakiej dzielnicy Szczecina sumaryczna powierzchnia mieszkalna [ha] jest 
--     największa a w jakiej najmniejsza? 

select round(sum(budynki.powierzchnia)/10000,2) as powierzchnia,
dzielnice.nazwa
from
(select *, area(geom)*liczbakond AS powierzchnia from OT_BUBD_A where x_kod in('BUBD01', 'BUBD02', 'BUBD03', 'BUBD04'))budynki,
(select * from dzielnice_osiedla_szczecin)dzielnice
where st_contains(dzielnice.geom, budynki.geom)
group by dzielnice.nazwa
order by sum(budynki.powierzchnia) desc

---------------------------------------------------------------------------------------------------------------------------------
--    2.  Policz budynki w dzielnicach. W których najwięcej jest budynków: 
--     jednorodzinnych (BUBD01), o dwóch mieszkaniach (BUBD02), trzech i więcej 
--     mieszkań (BUBD03) oraz zabudowy zbiorowej (BUBD04)? 

select COUNT(OT_BUBD_A.x_kod) as "count",dzielnice_osiedla_szczecin.nazwa, OT_BUBD_A.x_kod from OT_BUBD_A, dzielnice_osiedla_szczecin
where OT_BUBD_A.x_kod in('BUBD01', 'BUBD02', 'BUBD03', 'BUBD04') and st_contains(dzielnice_osiedla_szczecin.geom, OT_BUBD_A.geom) 
group by OT_BUBD_A.x_kod, dzielnice_osiedla_szczecin.nazwa
order by dzielnice_osiedla_szczecin.nazwa

--===============================================================================================================================
-- 2.  Proszę za pomocą formuły SQL, odnaleźć wszystkie sklepy biedronka (warstwa 
-- planet_osm_point; "name" = 'Biedronka') w Szczecinie i obliczyć powierzchnię 
-- budynków mieszkalnych w promieniu 500 metrów wokół (liczba pięter x podstawa).  
-- Dane proszę zwizualizować w postaci mapy tematycznej. 
-- Proszę wskazać lokalizację sklepu z największą powierzchnią mieszkalną  promieniu 500 m.

select round(sum(area(budynki.geom)*budynki.liczbakond),2) as pow, biedronka.fid
from
(select *, area(geom)*liczbakond AS powierzchnia from OT_BUBD_A where x_kod in('BUBD01', 'BUBD02', 'BUBD03', 'BUBD04'))budynki,
(select * from planet_osm_point where name = "Biedronka")biedronka
where st_contains(st_buffer(biedronka.geom,500), budynki.geom)
group by biedronka.fid
order by pow desc

--===============================================================================================================================
-- 3.  Budowana jest nowa linia energetyczna. Znajdź wszystkie działki geodezyjne, które 
-- będzie przecinać (warstwa „linia_energetyczna” oraz „kataster”). Wyświetl znalezione 
-- działki na mapie. Zwróć uwagę, ze warstwy mają różne układy współrzędnych. Użyj 
-- funkcji st_transform do konwersji jednej z nich do wspólnego formatu.

select * from kataster, linia_energetyczna 
where st_intersects(st_transform(kataster.geom,2180), linia_energetyczna.geom)

--===============================================================================================================================
-- 4.  Napisz kwerendę zwracającą wszystkie budynki w odległości 100 m od linii 
-- energetycznej. Pokaż budynki na mapie.

select OT_BUBD_A.fid, OT_BUBD_A.geom
from OT_BUBD_A,
(select st_buffer(geom,100) as geom from linia_energetyczna)
where st_contains(b.geom,OT_BUBD_A.geom) 
--===============================================================================================================================
--===============================================================================================================================
