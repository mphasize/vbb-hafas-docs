<?php

require_once 'func.php';

$fromX = urldecode($_GET['from_x']);
$fromY = urldecode($_GET['from_y']);
$toX = urldecode($_GET['to_x']);
$toY = urldecode($_GET['to_y']);

$xml = '<?xml version="1.0" encoding="iso-8859-1"?>
<ReqC ver="1.1" prod="String" rt="no" lang="DE" accessId="'. XML_ACCESS_ID .'">
	<ConReq deliverPolyline="0">
		<Start>
			<Coord x="'. $fromX .'" y="'. $fromY .'" type="WGS84" />
			<Prod prod="1111111111111111" bike="0" couchette="0" direct="0" sleeper="0" />
		</Start>
		<Dest>						
			<Coord x="'. $toX .'" y="'. $toY .'" type="WGS84" />
		</Dest>
		<ReqT a="0"  time="19:47" date="20121126" />
		<RFlags b="1" f="5" chExtension="0" sMode="N" nrChanges="2" getPrice="1" />
	</ConReq>
</ReqC>';

$response = query($xml);

echo json_encode($response);
exit();
?>