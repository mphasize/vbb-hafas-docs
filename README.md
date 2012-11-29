Offene Schnittstellen Dokumentation für den VBB Entwicklertag
==============

Bisher gibt es außer der .XSD-Datei keine umfassende Dokumentation, wie man die Schnittstelle der VBB anfragen und entsprechende Antworten auswerten kann.
Wir wollen hier einen ersten Grundstein legen, eine umfassende Community-gestützte Dokumentation der HAFAS XML Schnittstelle zu starten.

Die ersten Beispiele werden wir ganz pragmatisch in einem Frage-Antwort Format behandeln, welche hoffentlich früher oder später die wichtigsten Anwendungsfälle für die API demonstrieren.


## Informationsquellen

http://appsandthecity.net/daten/
http://stefanwehrmeyer.com/projects/vbbxsd/

## Weitere Datenquellen

### CartoDB

Die georefenzierten Daten aus dem VBB-GTFS Datensatz in CartoDB eingeladen. (CartoDB selbst aktualisiert leider gerade die Server, in sofern Verfügbarkeit schwierig.)

https://maps-fhp.cartodb.com/tables/vbb_stops/embed_map
https://maps-fhp.cartodb.com/tables/vbb_shapes/embed_map

(Geo-)JSON API:

    http://maps-fhp.cartodb.com/api/v2/sql?q=SELECT * FROM vbb_stops&format=geojson
    http://maps-fhp.cartodb.com/api/v2/sql?q=SELECT * FROM vbb_shapes&format=geojson

Tiles API:

    http://maps-fhp.cartodb.com/tiles/vbb_stops/{z}/{x}/{y}.png
    http://maps-fhp.cartodb.com/tiles/vbb_shapes/{z}/{x}/{y}.png



