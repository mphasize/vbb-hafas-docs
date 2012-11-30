# Request Beispiele


## Station Board Request

Der Station Board Request liefert Fahrplan-Informationen für einzelne Haltestellen zurück.

	<?xml version="1.0" encoding="iso-8859-1"?>
	<ReqC ver="1.1" prod="String" rt="no" lang="DE" accessId="[Access-ID]">
		<STBReq boardType="DEP"> 
			<Time>16:00:00</Time> 
			<Today /> 
			<TableStation externalId="009058101#86"/> 
			<ProductFilter>1111111111111111</ProductFilter> 
		</STBReq>
	</ReqC>
	



## Location Validation Request

Mit dem Location-Validation-Request kann man für einen beliebigen Suchstring eine passende Haltestelle finden. Üblicherweise kann man diese Funktion benutzen, wenn der Benutzer einen Haltestellen-Namen in ein Freitext-Suchfeld eingibt. Die API liefert dann zu dem Suchtext passende Ergebnisse mit eindeutigen Stations-IDs, welche dann in weiteren Anfragen an die API, z.B. für die Verbindungssuche benutzt werden können.

    <?xml version="1.0" encoding="iso-8859-1"?>
	<ReqC ver="1.1" prod="String" rt="yes" lang="DE" accessId="[Access-ID]">
		<LocValReq id="001" maxNr="20" sMode="1"> 
			<ReqLoc type="ST" match="[Suchstring]" /> 
		</LocValReq>
	</ReqC>

## Connection Request

Mit dem Connection-Request kann man eine Verbindungssuche starten.
Beispiel #1: Vorher wurden über den Location-Validation-Request zwei Stations-IDs bestimmt, die jetzt hier im ConReq verwendet werden um den Start- und den Endpunkt zu bestimmten.

	<?xml version="1.0" encoding="iso-8859-1"?>
	<ReqC ver="1.1" prod="String" rt="yes" lang="DE" accessId="[Access-ID]">
		<ConReq deliverPolyline="1">
			<Start>
				<Station externalId="009230999#86" />
				<Prod prod="1111111111111111" bike="0" couchette="0" direct="0" sleeper="0" />
			</Start>
			<Dest>						
				<Station externalId="009024101#86" />
			</Dest>
			<ReqT a="0"  time="19:47" date="20121126" />
			<RFlags b="1" f="5" chExtension="0" sMode="N" nrChanges="2" getPrice="1" />
		</ConReq>
	</ReqC>

Beispiel #2: Statt festen Stationen, können z.B. auch Geo-Koordination im Latitude-Longitude-Format für einen Request verwendet werden.
Da das HAFAS System die Koordination als Integer (also Ganzzahlen) erwartet, muss man die klassischen Koordinaten mit dem Faktor 1.000.000 multiplizieren.


	<?xml version="1.0" encoding="iso-8859-1"?>
	<ReqC ver="1.1" prod="String" rt="no" lang="DE" accessId="[Access-ID]">
		<ConReq deliverPolyline="0">
			<Start>
				<Coord x="Longitude(*1000000)" y="Latitude(*1000000)" type="WGS84" />
				<Prod prod="1111111111111111" bike="0" couchette="0" direct="0" sleeper="0" />
			</Start>
			<Dest>						
				<Coord x="Longitude(*1000000)" y="Latitude(*1000000)" type="WGS84" />
			</Dest>
			<ReqT a="0"  time="19:47" date="20121126" />
			<RFlags b="1" f="5" chExtension="0" sMode="N" nrChanges="2" getPrice="1" />
		</ConReq>
	</ReqC>	

