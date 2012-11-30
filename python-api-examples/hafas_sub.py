#!/usr/bin/env python

#
# Generated Thu Nov 29 22:00:29 2012 by generateDS.py version 2.7c.
#

import sys

import hafas_api as supermod

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#

class ReqCSub(supermod.ReqC):
    def __init__(self, accessId=None, STBReq=None, ConReq=None, ConScrReq=None):
        super(ReqCSub, self).__init__(accessId, STBReq, ConReq, ConScrReq, )
supermod.ReqC.subclass = ReqCSub
# end class ReqCSub


class ErrSub(supermod.Err):
    def __init__(self, text=None, code=None, level='E'):
        super(ErrSub, self).__init__(text, code, level, )
supermod.Err.subclass = ErrSub
# end class ErrSub


class ConBasicReqSub(supermod.ConBasicReq):
    def __init__(self, ivCons='no', oevCons='yes', Start=None, Dest=None, Via=None, extensiontype_=None):
        super(ConBasicReqSub, self).__init__(ivCons, oevCons, Start, Dest, Via, extensiontype_, )
supermod.ConBasicReq.subclass = ConBasicReqSub
# end class ConBasicReqSub


class ConReqSub(supermod.ConReq):
    def __init__(self, ivCons='no', oevCons='yes', Start=None, Dest=None, Via=None, ReqT=None, RFlags=None, GISParameters=None):
        super(ConReqSub, self).__init__(ivCons, oevCons, Start, Dest, Via, ReqT, RFlags, GISParameters, )
supermod.ConReq.subclass = ConReqSub
# end class ConReqSub


class GISParametersSub(supermod.GISParameters):
    def __init__(self, Front=None, Back=None, Total=None):
        super(GISParametersSub, self).__init__(Front, Back, Total, )
supermod.GISParameters.subclass = GISParametersSub
# end class GISParametersSub


class FrontSub(supermod.Front):
    def __init__(self, IndividualTransport=None):
        super(FrontSub, self).__init__(IndividualTransport, )
supermod.Front.subclass = FrontSub
# end class FrontSub


class BackSub(supermod.Back):
    def __init__(self, IndividualTransport=None):
        super(BackSub, self).__init__(IndividualTransport, )
supermod.Back.subclass = BackSub
# end class BackSub


class IndividualTransportSub(supermod.IndividualTransport):
    def __init__(self, maxDist=None, type_=None, cost=None, minDist=None, maxTime=None, speed=None):
        super(IndividualTransportSub, self).__init__(maxDist, type_, cost, minDist, maxTime, speed, )
supermod.IndividualTransport.subclass = IndividualTransportSub
# end class IndividualTransportSub


class TotalSub(supermod.Total):
    def __init__(self, IndividualTransport=None):
        super(TotalSub, self).__init__(IndividualTransport, )
supermod.Total.subclass = TotalSub
# end class TotalSub


class ConScrReqSub(supermod.ConScrReq):
    def __init__(self, nrCons=3, scrDir='F', ConResCtxt=None):
        super(ConScrReqSub, self).__init__(nrCons, scrDir, ConResCtxt, )
supermod.ConScrReq.subclass = ConScrReqSub
# end class ConScrReqSub


class ViaTypeSub(supermod.ViaType):
    def __init__(self, min=None, Station=None, Prod=None):
        super(ViaTypeSub, self).__init__(min, Station, Prod, )
supermod.ViaType.subclass = ViaTypeSub
# end class ViaTypeSub


class RequestLocationTypeSub(supermod.RequestLocationType):
    def __init__(self, min=None, Address=None, Poi=None, Station=None, Coord=None, extensiontype_=None):
        super(RequestLocationTypeSub, self).__init__(min, Address, Poi, Station, Coord, extensiontype_, )
supermod.RequestLocationType.subclass = RequestLocationTypeSub
# end class RequestLocationTypeSub


class ProdSub(supermod.Prod):
    def __init__(self, direct='0', sleeper='0', bike='0', couchette='0', prod=None):
        super(ProdSub, self).__init__(direct, sleeper, bike, couchette, prod, )
supermod.Prod.subclass = ProdSub
# end class ProdSub


class ReqTTypeSub(supermod.ReqTType):
    def __init__(self, date=None, a='0', time=None):
        super(ReqTTypeSub, self).__init__(date, a, time, )
supermod.ReqTType.subclass = ReqTTypeSub
# end class ReqTTypeSub


class RFlagsSub(supermod.RFlags):
    def __init__(self, b=None, f=None, nrChanges=None, chExtension=0, sMode='N', getPrice='0'):
        super(RFlagsSub, self).__init__(b, f, nrChanges, chExtension, sMode, getPrice, )
supermod.RFlags.subclass = RFlagsSub
# end class RFlagsSub


class ResCSub(supermod.ResC):
    def __init__(self, rt='yes', lang=None, ld=None, ver=None, host=None, prod=None, Err=None, ConRes=None, STBRes=None):
        super(ResCSub, self).__init__(rt, lang, ld, ver, host, prod, Err, ConRes, STBRes, )
supermod.ResC.subclass = ResCSub
# end class ResCSub


class ConResSub(supermod.ConRes):
    def __init__(self, dir=None, Err=None, ConResCtxt=None, ConnectionList=None, PricingResult=None):
        super(ConResSub, self).__init__(dir, Err, ConResCtxt, ConnectionList, PricingResult, )
supermod.ConRes.subclass = ConResSub
# end class ConResSub


class NowSub(supermod.Now):
    def __init__(self):
        super(NowSub, self).__init__()
supermod.Now.subclass = NowSub
# end class NowSub


class TimetableSub(supermod.Timetable):
    def __init__(self):
        super(TimetableSub, self).__init__()
supermod.Timetable.subclass = TimetableSub
# end class TimetableSub


class STBReqSub(supermod.STBReq):
    def __init__(self, boardType=None, maxStops=None, Time=None, Period=None, Today=None, Now=None, Timetable=None, TableStation=None, DirectionFilter=None, TrainFilter=None, ProductFilter=None):
        super(STBReqSub, self).__init__(boardType, maxStops, Time, Period, Today, Now, Timetable, TableStation, DirectionFilter, TrainFilter, ProductFilter, )
supermod.STBReq.subclass = STBReqSub
# end class STBReqSub


class TodaySub(supermod.Today):
    def __init__(self):
        super(TodaySub, self).__init__()
supermod.Today.subclass = TodaySub
# end class TodaySub


class PeriodSub(supermod.Period):
    def __init__(self, DateBegin=None, DateEnd=None):
        super(PeriodSub, self).__init__(DateBegin, DateEnd, )
supermod.Period.subclass = PeriodSub
# end class PeriodSub


class TrainFilterSub(supermod.TrainFilter):
    def __init__(self):
        super(TrainFilterSub, self).__init__()
supermod.TrainFilter.subclass = TrainFilterSub
# end class TrainFilterSub


class ProductFilterSub(supermod.ProductFilter):
    def __init__(self):
        super(ProductFilterSub, self).__init__()
supermod.ProductFilter.subclass = ProductFilterSub
# end class ProductFilterSub


class STBResSub(supermod.STBRes):
    def __init__(self, Err=None, JourneyList=None, IList=None):
        super(STBResSub, self).__init__(Err, JourneyList, IList, )
supermod.STBRes.subclass = STBResSub
# end class STBResSub


class JourneyListSub(supermod.JourneyList):
    def __init__(self, STBJourney=None):
        super(JourneyListSub, self).__init__(STBJourney, )
supermod.JourneyList.subclass = JourneyListSub
# end class JourneyListSub


class STBJourneySub(supermod.STBJourney):
    def __init__(self, journeyId=None, trainId=None, MainStop=None, JourneyAttributeList=None, ServiceDaysList=None, IList=None, JProg=None):
        super(STBJourneySub, self).__init__(journeyId, trainId, MainStop, JourneyAttributeList, ServiceDaysList, IList, JProg, )
supermod.STBJourney.subclass = STBJourneySub
# end class STBJourneySub


class MainStopSub(supermod.MainStop):
    def __init__(self, BasicStop=None):
        super(MainStopSub, self).__init__(BasicStop, )
supermod.MainStop.subclass = MainStopSub
# end class MainStopSub


class PricingResultSub(supermod.PricingResult):
    def __init__(self, PricingList=None):
        super(PricingResultSub, self).__init__(PricingList, )
supermod.PricingResult.subclass = PricingResultSub
# end class PricingResultSub


class PricingListSub(supermod.PricingList):
    def __init__(self, id=None, ParameterList=None, PricingSet=None, Pricing=None):
        super(PricingListSub, self).__init__(id, ParameterList, PricingSet, Pricing, )
supermod.PricingList.subclass = PricingListSub
# end class PricingListSub


class ParameterListSub(supermod.ParameterList):
    def __init__(self):
        super(ParameterListSub, self).__init__()
supermod.ParameterList.subclass = ParameterListSub
# end class ParameterListSub


class PricingSetSub(supermod.PricingSet):
    def __init__(self, ParameterList=None, Pricing=None):
        super(PricingSetSub, self).__init__(ParameterList, Pricing, )
supermod.PricingSet.subclass = PricingSetSub
# end class PricingSetSub


class PricingSub(supermod.Pricing):
    def __init__(self, type_=None, Ticket=None, ParameterList=None):
        super(PricingSub, self).__init__(type_, Ticket, ParameterList, )
supermod.Pricing.subclass = PricingSub
# end class PricingSub


class TicketSub(supermod.Ticket):
    def __init__(self, Tariff=None, Traveller=None, FromText=None, ToText=None, Price=None, ParameterList=None):
        super(TicketSub, self).__init__(Tariff, Traveller, FromText, ToText, Price, ParameterList, )
supermod.Ticket.subclass = TicketSub
# end class TicketSub


class TariffSub(supermod.Tariff):
    def __init__(self, code=None, Text=None):
        super(TariffSub, self).__init__(code, Text, )
supermod.Tariff.subclass = TariffSub
# end class TariffSub


class TravellerSub(supermod.Traveller):
    def __init__(self, TravellerCategory=None, Text=None):
        super(TravellerSub, self).__init__(TravellerCategory, Text, )
supermod.Traveller.subclass = TravellerSub
# end class TravellerSub


class TravellerCategorySub(supermod.TravellerCategory):
    def __init__(self, category=None, amount=None):
        super(TravellerCategorySub, self).__init__(category, amount, )
supermod.TravellerCategory.subclass = TravellerCategorySub
# end class TravellerCategorySub


class FromTextSub(supermod.FromText):
    def __init__(self, Text=None):
        super(FromTextSub, self).__init__(Text, )
supermod.FromText.subclass = FromTextSub
# end class FromTextSub


class ToTextSub(supermod.ToText):
    def __init__(self, Text=None):
        super(ToTextSub, self).__init__(Text, )
supermod.ToText.subclass = ToTextSub
# end class ToTextSub


class PriceSub(supermod.Price):
    def __init__(self, currency=None, price=None):
        super(PriceSub, self).__init__(currency, price, )
supermod.Price.subclass = PriceSub
# end class PriceSub


class ConnectionListSub(supermod.ConnectionList):
    def __init__(self, type_=None, Err=None, Connection=None):
        super(ConnectionListSub, self).__init__(type_, Err, Connection, )
supermod.ConnectionList.subclass = ConnectionListSub
# end class ConnectionListSub


class ConResCtxtSub(supermod.ConResCtxt):
    def __init__(self, b='1', f='1', valueOf_=None, mixedclass_=None, content_=None):
        super(ConResCtxtSub, self).__init__(b, f, valueOf_, mixedclass_, content_, )
supermod.ConResCtxt.subclass = ConResCtxtSub
# end class ConResCtxtSub


class TimeTypeSub(supermod.TimeType):
    def __init__(self, Time=None, extensiontype_=None):
        super(TimeTypeSub, self).__init__(Time, extensiontype_, )
supermod.TimeType.subclass = TimeTypeSub
# end class TimeTypeSub


class TimeSub(supermod.Time):
    def __init__(self, valueOf_=None, mixedclass_=None, content_=None):
        super(TimeSub, self).__init__(valueOf_, mixedclass_, content_, )
supermod.Time.subclass = TimeSub
# end class TimeSub


class LocationTypeSub(supermod.LocationType):
    def __init__(self, y=None, x=None, z=None, type_='WGS84', name=None, extensiontype_=None):
        super(LocationTypeSub, self).__init__(y, x, z, type_, name, extensiontype_, )
supermod.LocationType.subclass = LocationTypeSub
# end class LocationTypeSub


class StationTypeSub(supermod.StationType):
    def __init__(self, y=None, x=None, z=None, type_='WGS84', name=None, externalStationNr=None, externalId=None):
        super(StationTypeSub, self).__init__(y, x, z, type_, name, externalStationNr, externalId, )
supermod.StationType.subclass = StationTypeSub
# end class StationTypeSub


class TextSub(supermod.Text):
    def __init__(self, lang=None, valueOf_=None, mixedclass_=None, content_=None):
        super(TextSub, self).__init__(lang, valueOf_, mixedclass_, content_, )
supermod.Text.subclass = TextSub
# end class TextSub


class NamedValueSub(supermod.NamedValue):
    def __init__(self, name=None, value=None):
        super(NamedValueSub, self).__init__(name, value, )
supermod.NamedValue.subclass = NamedValueSub
# end class NamedValueSub


class ServiceDaysSub(supermod.ServiceDays):
    def __init__(self, ServiceBits=None, RegularServiceText=None, IrregularServiceText=None):
        super(ServiceDaysSub, self).__init__(ServiceBits, RegularServiceText, IrregularServiceText, )
supermod.ServiceDays.subclass = ServiceDaysSub
# end class ServiceDaysSub


class RegularServiceTextSub(supermod.RegularServiceText):
    def __init__(self, Text=None):
        super(RegularServiceTextSub, self).__init__(Text, )
supermod.RegularServiceText.subclass = RegularServiceTextSub
# end class RegularServiceTextSub


class IrregularServiceTextSub(supermod.IrregularServiceText):
    def __init__(self, Text=None):
        super(IrregularServiceTextSub, self).__init__(Text, )
supermod.IrregularServiceText.subclass = IrregularServiceTextSub
# end class IrregularServiceTextSub


class ConnectionSub(supermod.Connection):
    def __init__(self, id=None, RtStateList=None, Overview=None, ConSectionList=None, IList=None, CommentList=None, AltConList=None):
        super(ConnectionSub, self).__init__(id, RtStateList, Overview, ConSectionList, IList, CommentList, AltConList, )
supermod.Connection.subclass = ConnectionSub
# end class ConnectionSub


class OverviewSub(supermod.Overview):
    def __init__(self, Date=None, Departure=None, Arrival=None, Transfers=None, Duration=None, ServiceDays=None, Products=None, ContextURL=None):
        super(OverviewSub, self).__init__(Date, Departure, Arrival, Transfers, Duration, ServiceDays, Products, ContextURL, )
supermod.Overview.subclass = OverviewSub
# end class OverviewSub


class ProductsSub(supermod.Products):
    def __init__(self, Product=None):
        super(ProductsSub, self).__init__(Product, )
supermod.Products.subclass = ProductsSub
# end class ProductsSub


class ProductSub(supermod.Product):
    def __init__(self, cat=None):
        super(ProductSub, self).__init__(cat, )
supermod.Product.subclass = ProductSub
# end class ProductSub


class ContextURLSub(supermod.ContextURL):
    def __init__(self, url=None):
        super(ContextURLSub, self).__init__(url, )
supermod.ContextURL.subclass = ContextURLSub
# end class ContextURLSub


class ConSectionListSub(supermod.ConSectionList):
    def __init__(self, ConSection=None):
        super(ConSectionListSub, self).__init__(ConSection, )
supermod.ConSectionList.subclass = ConSectionListSub
# end class ConSectionListSub


class ConSectionSub(supermod.ConSection):
    def __init__(self, Departure=None, Journey=None, Walk=None, Transfer=None, GisRoute=None, Arrival=None):
        super(ConSectionSub, self).__init__(Departure, Journey, Walk, Transfer, GisRoute, Arrival, )
supermod.ConSection.subclass = ConSectionSub
# end class ConSectionSub


class DepartureSub(supermod.Departure):
    def __init__(self, BasicStop=None):
        super(DepartureSub, self).__init__(BasicStop, )
supermod.Departure.subclass = DepartureSub
# end class DepartureSub


class ArrivalSub(supermod.Arrival):
    def __init__(self, BasicStop=None):
        super(ArrivalSub, self).__init__(BasicStop, )
supermod.Arrival.subclass = ArrivalSub
# end class ArrivalSub


class BasicStopSub(supermod.BasicStop):
    def __init__(self, index=None, type_='NORMAL', Address=None, Poi=None, Station=None, Arr=None, Dep=None, StopPrognosis=None):
        super(BasicStopSub, self).__init__(index, type_, Address, Poi, Station, Arr, Dep, StopPrognosis, )
supermod.BasicStop.subclass = BasicStopSub
# end class BasicStopSub


class PlatformSub(supermod.Platform):
    def __init__(self, Text=None):
        super(PlatformSub, self).__init__(Text, )
supermod.Platform.subclass = PlatformSub
# end class PlatformSub


class ArrDepTypeSub(supermod.ArrDepType):
    def __init__(self, Time=None, getIn='YES', getOut='YES', Platform=None):
        super(ArrDepTypeSub, self).__init__(Time, getIn, getOut, Platform, )
supermod.ArrDepType.subclass = ArrDepTypeSub
# end class ArrDepTypeSub


class JourneySub(supermod.Journey):
    def __init__(self, JHandle=None, JourneyAttributeList=None, PassList=None, JProg=None):
        super(JourneySub, self).__init__(JHandle, JourneyAttributeList, PassList, JProg, )
supermod.Journey.subclass = JourneySub
# end class JourneySub


class WalkSub(supermod.Walk):
    def __init__(self, length=None, Duration=None, Distance=None, JourneyAttributeList=None):
        super(WalkSub, self).__init__(length, Duration, Distance, JourneyAttributeList, )
supermod.Walk.subclass = WalkSub
# end class WalkSub


class DistanceSub(supermod.Distance):
    def __init__(self):
        super(DistanceSub, self).__init__()
supermod.Distance.subclass = DistanceSub
# end class DistanceSub


class TransferSub(supermod.Transfer):
    def __init__(self, length=None, Duration=None, JourneyAttributeList=None):
        super(TransferSub, self).__init__(length, Duration, JourneyAttributeList, )
supermod.Transfer.subclass = TransferSub
# end class TransferSub


class GisRouteSub(supermod.GisRoute):
    def __init__(self, type_=None, Duration=None, Distance=None, JourneyAttributeList=None):
        super(GisRouteSub, self).__init__(type_, Duration, Distance, JourneyAttributeList, )
supermod.GisRoute.subclass = GisRouteSub
# end class GisRouteSub


class PassListSub(supermod.PassList):
    def __init__(self, BasicStop=None):
        super(PassListSub, self).__init__(BasicStop, )
supermod.PassList.subclass = PassListSub
# end class PassListSub


class CommentListSub(supermod.CommentList):
    def __init__(self, Comment=None):
        super(CommentListSub, self).__init__(Comment, )
supermod.CommentList.subclass = CommentListSub
# end class CommentListSub


class CommentSub(supermod.Comment):
    def __init__(self, id=None, Text=None):
        super(CommentSub, self).__init__(id, Text, )
supermod.Comment.subclass = CommentSub
# end class CommentSub


class JHandleSub(supermod.JHandle):
    def __init__(self, cycle=None, puic=None, tNr=None):
        super(JHandleSub, self).__init__(cycle, puic, tNr, )
supermod.JHandle.subclass = JHandleSub
# end class JHandleSub


class AltConListSub(supermod.AltConList):
    def __init__(self, id=None):
        super(AltConListSub, self).__init__(id, )
supermod.AltConList.subclass = AltConListSub
# end class AltConListSub


class RtStateListSub(supermod.RtStateList):
    def __init__(self, RtState=None):
        super(RtStateListSub, self).__init__(RtState, )
supermod.RtStateList.subclass = RtStateListSub
# end class RtStateListSub


class RtStateSub(supermod.RtState):
    def __init__(self, value=None):
        super(RtStateSub, self).__init__(value, )
supermod.RtState.subclass = RtStateSub
# end class RtStateSub


class JProgSub(supermod.JProg):
    def __init__(self, JStatus=None):
        super(JProgSub, self).__init__(JStatus, )
supermod.JProg.subclass = JProgSub
# end class JProgSub


class AnnoTextSub(supermod.AnnoText):
    def __init__(self):
        super(AnnoTextSub, self).__init__()
supermod.AnnoText.subclass = AnnoTextSub
# end class AnnoTextSub


class AttributeSub(supermod.Attribute):
    def __init__(self, priority=None, code=None, type_='NORMAL', AttributeVariant=None):
        super(AttributeSub, self).__init__(priority, code, type_, AttributeVariant, )
supermod.Attribute.subclass = AttributeSub
# end class AttributeSub


class AttributeVariantSub(supermod.AttributeVariant):
    def __init__(self, type_='NORMAL', Text=None):
        super(AttributeVariantSub, self).__init__(type_, Text, )
supermod.AttributeVariant.subclass = AttributeVariantSub
# end class AttributeVariantSub


class JourneyAttributeListSub(supermod.JourneyAttributeList):
    def __init__(self, JourneyAttribute=None):
        super(JourneyAttributeListSub, self).__init__(JourneyAttribute, )
supermod.JourneyAttributeList.subclass = JourneyAttributeListSub
# end class JourneyAttributeListSub


class JourneyAttributeSub(supermod.JourneyAttribute):
    def __init__(self, to=None, fromxx=None, Attribute=None, ServiceDays=None):
        super(JourneyAttributeSub, self).__init__(to, fromxx, Attribute, ServiceDays, )
supermod.JourneyAttribute.subclass = JourneyAttributeSub
# end class JourneyAttributeSub


class IListSub(supermod.IList):
    def __init__(self, I=None):
        super(IListSub, self).__init__(I, )
supermod.IList.subclass = IListSub
# end class IListSub


class ISub(supermod.I):
    def __init__(self, arr=None, lead=None, header=None, dep=None, text=None, symbol=None, altRouteStart=None, uriCustom=None, altRouteEnd=None, locType=None, type_=0, section=None, channel=None):
        super(ISub, self).__init__(arr, lead, header, dep, text, symbol, altRouteStart, uriCustom, altRouteEnd, locType, type_, section, channel, )
supermod.I.subclass = ISub
# end class ISub


class DateBeginTypeSub(supermod.DateBeginType):
    def __init__(self, Date=None):
        super(DateBeginTypeSub, self).__init__(Date, )
supermod.DateBeginType.subclass = DateBeginTypeSub
# end class DateBeginTypeSub


class DateEndTypeSub(supermod.DateEndType):
    def __init__(self, Date=None):
        super(DateEndTypeSub, self).__init__(Date, )
supermod.DateEndType.subclass = DateEndTypeSub
# end class DateEndTypeSub


class ServiceDaysListTypeSub(supermod.ServiceDaysListType):
    def __init__(self, ServiceDays=None):
        super(ServiceDaysListTypeSub, self).__init__(ServiceDays, )
supermod.ServiceDaysListType.subclass = ServiceDaysListTypeSub
# end class ServiceDaysListTypeSub


class StopPrognosisTypeSub(supermod.StopPrognosisType):
    def __init__(self, Arr=None, Dep=None, Status=None, FreeTextL=None):
        super(StopPrognosisTypeSub, self).__init__(Arr, Dep, Status, FreeTextL, )
supermod.StopPrognosisType.subclass = StopPrognosisTypeSub
# end class StopPrognosisTypeSub


class FreeTextLTypeSub(supermod.FreeTextLType):
    def __init__(self, Freetext=None):
        super(FreeTextLTypeSub, self).__init__(Freetext, )
supermod.FreeTextLType.subclass = FreeTextLTypeSub
# end class FreeTextLTypeSub


class FreetextTypeSub(supermod.FreetextType):
    def __init__(self, validFor=None, Text=None, Code=None):
        super(FreetextTypeSub, self).__init__(validFor, Text, Code, )
supermod.FreetextType.subclass = FreetextTypeSub
# end class FreetextTypeSub


class StartViaTypeSub(supermod.StartViaType):
    def __init__(self, min=None, Address=None, Poi=None, Station=None, Coord=None, Prod=None):
        super(StartViaTypeSub, self).__init__(min, Address, Poi, Station, Coord, Prod, )
supermod.StartViaType.subclass = StartViaTypeSub
# end class StartViaTypeSub



def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    if hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ReqC'
        rootClass = supermod.ReqC
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    doc = None
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ReqC'
        rootClass = supermod.ReqC
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ReqC'
        rootClass = supermod.ReqC
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from hafas_api import *\n\n')
    sys.stdout.write('import hafas_api as model_\n\n')
    sys.stdout.write('rootObj = model_.ReqC(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="ReqC")
    sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


