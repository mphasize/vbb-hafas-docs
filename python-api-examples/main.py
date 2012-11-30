#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-

from hafas_api import ReqC, ConReq, StartViaType, LocationType, Prod
from hafas_api import RequestLocationType, ReqTType, RFlags

import requests

from StringIO import StringIO

# <Coord ... />, lat and lon need to be multiplied by 1.000.000
start_coord = LocationType(x=52559480, y=13413212)
# <Prod ... />, what kind of connections and trains to use
start_prod = Prod(prod="1111111111111111")

# see start_coord
dest_coord = LocationType(x=52567380, y=13412250)

# <Start ... />
start = StartViaType(Coord=start_coord, Prod=start_prod)
# <Dest ... />
dest = RequestLocationType(Coord=dest_coord)

# <ReqT ... />, time of either arrival or departure
reqt = ReqTType(time="19:47", date="20121126")
# <RFlags ... />, search specific flags
rflags = RFlags(b="0", chExtension="20", f="1", sMode="N", nrChanges="2",
                getPrice="1")

# <ConReq ... />, putting it all together
cr = ConReq(Start=start, Dest=dest, ReqT=reqt, RFlags=rflags)
# <ReqC ... />, wrap it all up nicely
reqc = ReqC(ConReq=cr, accessId="dfe2a3638d4ee0ea051e7f9dccf842df")

# oh man, I need a file-like object here because the export function can only
# write into one of those -.-"
xml = StringIO()
# giving it a nice XML declaration
xml.write('<?xml version="1.0" encoding="iso-8859-1"?>\n')
# export the XML and append it to the file-like object
reqc.export(xml, 0)
# get the XML from the file-like object
data = xml.getvalue()
# close the file-like object
xml.close()

# setting up a request using the fabulous requests library
URL = "http://demo.hafas.de/bin/pub/vbb-fahrinfo/relaunch2011/extxml.exe/"
headers = {'content-type': 'text/xml'}
# fire the request
response = requests.post(URL, data=data, headers=headers)
# having a look at the raw response body
print response.content
