# Python API binding

This is a first try of building a nice Python binding for the interface
provided by the VBB.

## Used tools

### [generateDS](http://cutter.rexx.com/~dkuhlman/generateDS.html)

I generated the Python classes from the API XMLSchema with this.

### [Requests](http://docs.python-requests.org/en/latest/) *(optional)*

I highly recommend it to query the API though. (And you need it to run the
test script `main.py`.)

## Generating the Python classes

Basically all I did was running this command:

    generateDS.py -o hafas_api.py -s hafas_sub.py --super=hafas_api hafasXMLInterface.xsd

It's straight from their docs. So don't ask me what they do ;)

`hafasXMLInterface.xsd` was given to me at the Apps & the City developer day.
If you have a newer one, feel free to try that and maybe contribute.

## Using the classes

I provided a test script which builds a `ConReq` request step by step and
sends it using the Requests library.

Other requests are build similarly.

## TODO

I guess a simpler and more *pythonic* wrapper would be nice to have.