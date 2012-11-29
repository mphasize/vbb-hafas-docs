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
	</xml>



## Location Validation Request

Mit dem Location-Validation-Request kann man für einen beliebigen Suchstring eine passende Haltestelle finden. Üblicherweise kann man diese Funktion benutzen, wenn der Benutzer einen Haltestellen-Namen in ein Freitext-Suchfeld eingibt. Die API liefert dann zu dem Suchtext passende Ergebnisse mit eindeutigen Stations-IDs, welche dann in weiteren Anfragen an die API, z.B. für die Verbindungssuche benutzt werden können.

    <?xml version="1.0" encoding="iso-8859-1"?>
		<ReqC ver="1.1" prod="String" rt="yes" lang="DE" accessId="[Access-ID]">
			<LocValReq id="001" maxNr="20" sMode="1"> 
				<ReqLoc type="ST" match="[Suchstring]" /> 
			</LocValReq>
		</ReqC>
	</xml>