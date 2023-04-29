## Lab. 1 Wykorzystanie formatu bazodanowego GeoPackage do wykonania mapy powiatu szczecińskiego

### Wstęp:
W  systemach  informacji  przestrzennej  bardzo  ważne  jest  sprawne  operowanie  warstwami, a szczególnie treścią w oparciu o zapytania SQL. Najbardziej wygodne jest więc wykorzystanie baz danych w postaci systemów sieciowych jak i lokalnych. Jednym z tego typu rozwiązań dla systemów lokalnych zyskującym na popularności jest format GeoPackage (*.gpkg), będący rozszerzeniem bazy SQLite3. Umożliwia on zachowanie wielu warstw w jednym pliku wraz z ich stylizacją oraz relacjami przestrzennymi. Daje on namdo dyspozycji zaawansowane funkcje SQL (m.in. indeksowanie, funkcje geometryczne:  grupowanie,  wybieranie  po  położeniu,  analizy  sąsiedztwaitp.),  jak  i  możliwość przechowywania  danych  wektorowych  i  rastrowych  w  jednym  miejscu,  który  można  później udostępnić np. w systemach chmurowych. 

### Cel:

Celem ćwiczenia jest zapoznanie się z podstawowymi funkcjamibazy  danych  GeoPackage  oraz stylizacja mapy z odpowiednimi ustawieniami dotyczącymi zakresów widoczności warstw po skali, wybierania danych i stylizacji z wykorzystaniem funkcji SQL.