<?php
require_once 'func.php';

$xml = '<?xml version="1.0" encoding="utf-8"?>
<ReqC lang="DE" prod="testsystem" ver="1.1" accessId="'. XML_ACCESS_ID .'">
    <ConReq>
        <Start>
            <Station externalId="9470098" />
            <Prod prod="1111000000000000" direct="0" />
        </Start>
        <Dest>
            <Station externalId="9470101" />
        </Dest>
        <ReqT a="0" date="20121207" time="11:57" />
        <RFlags b="0" f="6" sMode="N" />
    </ConReq>
</ReqC>';

$response = query($xml);

echo var_dump($response);
exit();
?>