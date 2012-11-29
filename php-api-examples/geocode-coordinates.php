<?php

$url = "http://maps.googleapis.com/maps/api/geocode/";

$x = trim(urldecode($_GET['lat']));
$y = trim(urldecode($_GET['lng']));

$response = array();

if ($x != "" && $y != "") {

	$session = curl_init($url .'json?latlng=' . $x . ',' . $y . '&sensor=false');
	curl_setopt_array($session, array(CURLOPT_RETURNTRANSFER => true));
	$response = curl_exec($session);
	curl_close($session);

	echo $response;
}
?>