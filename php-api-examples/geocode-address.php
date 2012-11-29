<?php

$url = "http://maps.googleapis.com/maps/api/geocode/";

$address = urldecode($_GET['address']);

$response = array();

if ($address != null && $address != "") {

	$session = curl_init($this->url . $output . '?address=' . urlencode($address) . '&sensor=false');
	curl_setopt_array($session, array(CURLOPT_RETURNTRANSFER => true));
	$response = curl_exec($session);
	curl_close($session);

	echo $response;
}
?>
