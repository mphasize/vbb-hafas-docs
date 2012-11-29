<?php

require_once 'func.php';

$name = urldecode(isset($_GET['name']) ? $_GET['name'] : 'Rathaus');

$xml = '<?xml version="1.0" encoding="iso-8859-1"?>
<ReqC ver="1.1" prod="String" rt="yes" lang="DE" accessId="'. XML_ACCESS_ID .'">
	<LocValReq id="001" maxNr="20" sMode="1"> 
		<ReqLoc type="ST" match="' . $name . '" /> 
	</LocValReq>
</ReqC>';


$response = query($xml);

echo json_encode($response);
exit();
?>