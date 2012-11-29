
ReqC

The element ReqC is the root element for requests to the HAFAS system. It must contain either a location validation request, a connection request or a connection scroll request. (See the corresponding elements for more details).


ResC
	

ReqC
	accessId	The id may contain any string for identification of the user


Location Validation Request


ConBasicReq


ConReq - Connection Request

The element ConReq specifies an initial connection request (opposed to the element ConScrReq, that specifies a subsequent scroll request based on this initial request).


ConScrReq - Connection Scroll Request

ConScrReq specifies a connection scroll request based on a previously performed ConReq. It takes a ConResCtxt supplied by the ConRes (as the answer to this previously performed ConReq)