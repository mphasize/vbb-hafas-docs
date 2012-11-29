# VBB HAFAS API Documentation

Basiert auf den XML Schema Spezifikationen verfügbar unter http://demo.hafas.de/xml/vbb/se/hafasXMLInterface.xsd und http://demo.hafas.de/xml/vbb/std/hafasXMLInterface.xsd sowie persönlichen Informationen.

Stand: 29. November 2012



## ReqC - Request to the HAFAS System

> The element ReqC is the root element for requests to the HAFAS system. It must contain either a location validation request, a connection request or a connection scroll request. (See the corresponding elements for more details).

Alle Anfragen an das HAFAS API müssen in ein ReqC Element gepackt werden, dass auch im Attribut "accessId" die Authentifizierung am System herstellt.

Die ReqC-Element müssen einen der folgenden inhaltlichen Requests enthalten:

* ConReq - Connection Request (Verbindungsanfrage)
* ConScrReq - Connection Scroll Request (Weiterführung einer Verbindungsanfrage aus einem bestehenden ConReq-Kontext heraus)
* LocValReq - Location Validation Request 
* STBReq - Station Board Request
* MLCReq - 


### ReqC Parameter

* accessId: The id may contain any string for identification of the user





## ConBasicReq - Connection Basic Request



## ConReq - Connection Request

> The element ConReq specifies an initial connection request (opposed to the element ConScrReq, that specifies a subsequent scroll request based on this initial request).



## ConScrReq - Connection Scroll Request

> ConScrReq specifies a connection scroll request based on a previously performed ConReq. It takes a ConResCtxt supplied by the ConRes (as the answer to this previously performed ConReq)


## LocValReq - Location Validation Request

Location Validation Request können genutzt werden, um über eine Stationsbezeichnung die entsprechende ID der Station abzufragen.


## MLCReq




## ResC

	