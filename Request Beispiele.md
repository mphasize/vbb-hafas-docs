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

