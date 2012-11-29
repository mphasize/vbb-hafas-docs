# Open VBB HAFAS API Dokumentation

Basiert auf den XML Schema Spezifikationen verfügbar unter
http://demo.hafas.de/xml/vbb/se/hafasXMLInterface.xsd und
http://demo.hafas.de/xml/vbb/std/hafasXMLInterface.xsd sowie persönlichen
Informationen (s.a. http://stefanwehrmeyer.com/projects/vbbxsd/).

Stand: 29. November 2012

Die Modellierung der API orientiert sich an einer klassischen
Verbindungsauskunft und Abfahrtstafeln.

Anfragen an eher statische Daten wie Stationslisten, Linien etc. sollten eher
über die GTFS-Daten bezogen werden.

(Alle nicht als optional gekennzeichneten Parameter sind notwendig.)


## ReqC - Request to the HAFAS System

> The element ReqC is the root element for requests to the HAFAS
> system. It must contain either a location validation request,
> a connection request or a connection scroll request. (See the
> corresponding elements for more details).

Alle Anfragen an das HAFAS API müssen in ein ReqC Element gepackt werden, dass
auch im Attribut "accessId" die Authentifizierung am System herstellt.

Die ReqC-Element müssen einen der folgenden inhaltlichen Requests enthalten:

* ConReq - Connection Request (Verbindungsanfrage)
* ConScrReq - Connection Scroll Request (Weiterführung einer Verbindungsanfrage
  aus einem bestehenden ConReq-Kontext heraus)
* LocValReq - Location Validation Request 
* STBReq - Station Board Request
* MLCReq - unbekannt, vielleicht "Map Location Request"?


### Request Parameter:

Attribute:

- accessId: The id may contain any string for identification of the user



## ConBasicReq - Connection Basic Request

Nicht direkt zu benutzen, wird von ConReq erweitert.


## ConReq - Connection Request

> The element ConReq specifies an initial connection request (opposed to the
element ConScrReq, that specifies a subsequent scroll request based on this
initial request).

### Connection Request Parameter:

- Start: 
- Dest:
- Via (0 bis 3 Viapunkte): 

- ReqT: ReqT contains the request time for the current request.

- RFlags: RFlags specifies some essential request flags passed to the Hafas
  kernel.

  Attribute:
  - b (Integer, 0-6): The attribute b specifies the number of connections to
    find in searchdirection backward. This means connections starting/ending
    (depends on the value of the attribute a) before the time specified in ReqT.
    The number must not be below zero and must not exceed 6.
  - f (Integer, 0-6): The attribute f specifies the number of connections to
    find in searchdirection forward. This means connections starting/ending
    (depends on the value of the attribute a) after the time specified in ReqT.
    The number must not be below zero and must not exceed 6.
  - weitere optionale Paramter unter attlist.BasicRFlags

- HandicapProfile (optional)
- GISParameters (optional)



## ConScrReq - Connection Scroll Request

> ConScrReq specifies a connection scroll request based on a previously
performed ConReq. It takes a ConResCtxt supplied by the ConRes (as the answer to
this previously performed ConReq)

### Connection Scroll Request Parameter:

- ConResCtxt: Kontext wie zurückgegeben von einem Connection Request

Attribute:

- scrDir (optional, Werte "F" (default), "B", "I"): The attribute scrDir specifies the scroll
  direction relative to the previously received ConRes. A value of B will
  retrieve the connections preceeding the connections of this ConRes. A value of
  F will retrieve the connection following the connections in this ConRes. A
  value of I will retrieve the same connections once again. The option I is for
  future use and will not work in this version of the interface. If supplied, an
  error message will be returned.
- nrCons (optional, integer, default 3): nrCons specifies the number of
  connections to be returned in the ConRes containing the answer of the current
  ConScrReq. Please keep in mind that there can be returned fewer connections
  (in which case the result will contain an Err element specifying the reason
  for this behaviour). In some cases the Hafas algorithm will calculate more tan
  the requested number of connections. This is due to te fact, that the HAFAS
  algorithm apart from returning the best connections additionally calculates
  more comfortable connections, which will be returned as well. This is a basic
  feature of the Hafas algorithm.


## LocValReq - Location Validation Request

Location Validation Request können genutzt werden, um über eine
Stationsbezeichnung die entsprechende ID der Station abzufragen.

Der grundlegende Ansatz des HAFAS-System ist, dass Stationen zuerst immer über
eine allgemeine Bezeichnungssuche bzw. Geokoordinaten identifiziert werden
sollte, da die im System liegenden Namen oder IDs nicht dauerhaft garantiert
sind.


  <LocValReq id="001" maxNr="20" sMode="1"> 
    <ReqLoc type="ST" match="Hauptbahnhof, Berlin" /> 
  </LocValReq> 
  
  <LocValRes flag="FINAL" id="001"> 
    <Station name="Berlin Hbf" externalId="008011160#81" externalStationNr="008011160" type="WGS84" x="13369548" y="52525589"/> 
    [...] 
  </LocValRes> 


## STBReq - Station Board Request

Ein Station Board Request liefert Abfahrts- bzw. Ankunftstafeln für eine
angegebene Station bzw. Stationsbezeichnung.

### Station Board Request Parameter:

- Zeitpunkt, entweder 1., 2. oder 3.:
  1. Sequenz aus:
    - Time: The format of the Time element is [xxd]hh:mm:ss. xx represents a day
      offset. All offsets are relative to the base date of the connection. For
      example a time 01d12:30:00 means 12:30 at the first day following the day
      specified as the base date in the Date element in the Overview section of
      the connection.
    - Period oder Today

      Period: A period is requested. If DateBegin and DateEnd are ommitted, a
      table for the whole timetableperiod is generated. If DateBegin is ommitted,
      the current date is taken as the begin of the period. If DateEnd is
      ommitted, the end of the timetable period is taken as the end of the
      requested period.
      - DateBegin: 
      - DateEnd:
        
      Today: Stationboardrequest for the current day.
  
  2. Now: The element Now stands for current time and current date
  
  3. Timetable: The element Timetable stands for the timetable period beginning from now.
	
- TableStation: The requested Station. This element must be filled with the
  results from a previously performed location validation request. Only stations
  are allowed as input here.

- DirectionFilter (optional)
- TrainFilter (optional)
- ProductFilter (optional)
		
Attribute: 

- boardType (Werte: "ARR" oder "DEP"): Type of StationBoard: ARR = Arrivalboard, DEP = DepartureBoard
- maxStops: The attribute maxStops describes the number of stopovers in the
  passlist plus 2 (for departure and arrival stops). If maxStops equals to zero,
  only 2 stops - departure and arrival are displayed in the passList. If the
  attribute is absent, all available stops are displayed.


## MLCReq

Zur Zeit nicht dokumentiert.




## ResC - Result

> ResC is the container for any type of results, calculated by the Hafas server.


## ConRes - Connection Result

> A ConRes is the connection result. This Type of result is returned as a resonse to a connection request (ConReq) or a connection scroll request (ConScrReq).

