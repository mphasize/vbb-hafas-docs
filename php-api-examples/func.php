<?php

/**
 * Define POST URL and also payload
 */
require_once 'config.php';
define('XML_POST_URL', 'http://demo.hafas.de/bin/pub/vbb-fahrinfo/relaunch2011/extxml.exe/');
define('XML_ACCESS_ID', $accessID);

function query($xml) {
	/**
	 * Initialize handle and set options
	 */
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, XML_POST_URL);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_TIMEOUT, 4);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $xml);
//curl_setopt($ch, CURLOPT_VERBOSE, true);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Connection: close', 'Content-Type: text/xml'));

	/**
	 * Execute the request and also time the transaction
	 */
	$start = array_sum(explode(' ', microtime()));
	$result = curl_exec($ch);
	$stop = array_sum(explode(' ', microtime()));
	$totalTime = $stop - $start;

	/**
	 * Check for errors
	 */
	if (curl_errno($ch)) {
		$result = 'ERROR -> ' . curl_errno($ch) . ': ' . curl_error($ch);
	} else {
		$returnCode = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
		switch ($returnCode) {
			case 404:
				$result = 'ERROR -> 404 Not Found';
				break;
			default:
				break;
		}
	}

	/**
	 * Close the handle
	 */
	curl_close($ch);

	/**
	 * Output the results and time
	 */
	$out = new stdClass();
	$out->timer = $totalTime;
	$out->xml = $result;
	
	//echo var_dump($result);

	$res = new SimpleXMLElement($result);
	$resname = "" . $res->getName();

	$out->$resname = $res;

	return $out;
}

?>
