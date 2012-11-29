<?php

require_once 'func.php';

$name = urldecode(isset($_GET['name']) ? $_GET['name'] : 'Rathaus');
$type = urldecode(isset($_GET['type']) ? $_GET['type'] : 'ALLTYPE');

$xml = '<?xml version="1.0" encoding="iso-8859-1"?>
<ReqC ver="1.1" prod="String" rt="yes" lang="DE" accessId="' . XML_ACCESS_ID . '">
	<MLcReq><MLc n="' . $name . '?" t="' . $type . '" /></MLcReq>
</ReqC>';


$response = query($xml);

echo json_encode($response);
exit();
?>