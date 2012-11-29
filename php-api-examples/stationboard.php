<?php

require_once 'func.php';

$xml = '<?xml version="1.0" encoding="iso-8859-1"?>
<ReqC ver="1.1" prod="String" rt="no" lang="DE" accessId="' . XML_ACCESS_ID . '">
	<STBReq boardType="DEP"> 
		<Time>16:00:00</Time> 
		<Today /> 
		<TableStation externalId="009058101#86"/> 
		<ProductFilter>1111111111111111</ProductFilter> 
	</STBReq>
</ReqC>';

$response = query($xml);

echo json_encode($response);
exit();
?>
