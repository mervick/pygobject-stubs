# encoding: utf-8
# module gi.repository.GstMpegts
# from /usr/lib64/girepository-1.0/GstMpegts-1.0.typelib
# by generator 1.147
"""
An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
"""

# imports
import gi as __gi
import gobject as __gobject


# Variables with simple values

_namespace = 'GstMpegts'

_version = '1.0'

__weakref__ = None

# functions

def descriptor_from_custom(tag, data): # real signature unknown; restored from __doc__
    """ descriptor_from_custom(tag:int, data:list) -> GstMpegts.Descriptor """
    pass

def descriptor_from_custom_with_extension(tag, tag_extension, data): # real signature unknown; restored from __doc__
    """ descriptor_from_custom_with_extension(tag:int, tag_extension:int, data:list) -> GstMpegts.Descriptor """
    pass

def descriptor_from_dvb_network_name(name): # real signature unknown; restored from __doc__
    """ descriptor_from_dvb_network_name(name:str) -> GstMpegts.Descriptor """
    pass

def descriptor_from_dvb_service(service_type, service_name=None, service_provider=None): # real signature unknown; restored from __doc__
    """ descriptor_from_dvb_service(service_type:GstMpegts.DVBServiceType, service_name:str=None, service_provider:str=None) -> GstMpegts.Descriptor """
    pass

def descriptor_from_dvb_subtitling(lang, type, composition, ancillary): # real signature unknown; restored from __doc__
    """ descriptor_from_dvb_subtitling(lang:str, type:int, composition:int, ancillary:int) -> GstMpegts.Descriptor """
    pass

def descriptor_from_iso_639_language(language): # real signature unknown; restored from __doc__
    """ descriptor_from_iso_639_language(language:str) -> GstMpegts.Descriptor """
    pass

def descriptor_from_registration(format_identifier, additional_info=None): # real signature unknown; restored from __doc__
    """ descriptor_from_registration(format_identifier:str, additional_info:list=None) -> GstMpegts.Descriptor """
    pass

def dvb_component_descriptor_free(source): # real signature unknown; restored from __doc__
    """ dvb_component_descriptor_free(source:GstMpegts.ComponentDescriptor) """
    pass

def event_parse_mpegts_section(event): # real signature unknown; restored from __doc__
    """ event_parse_mpegts_section(event:Gst.Event) -> GstMpegts.Section """
    pass

def find_descriptor(descriptors, tag): # real signature unknown; restored from __doc__
    """ find_descriptor(descriptors:list, tag:int) -> GstMpegts.Descriptor """
    pass

def initialize(): # real signature unknown; restored from __doc__
    """ initialize() """
    pass

def message_new_mpegts_section(parent, section): # real signature unknown; restored from __doc__
    """ message_new_mpegts_section(parent:Gst.Object, section:GstMpegts.Section) -> Gst.Message """
    pass

def message_parse_mpegts_section(message): # real signature unknown; restored from __doc__
    """ message_parse_mpegts_section(message:Gst.Message) -> GstMpegts.Section """
    pass

def parse_descriptors(buffer, buf_len): # real signature unknown; restored from __doc__
    """ parse_descriptors(buffer:int, buf_len:int) -> list """
    return []

def pat_new(): # real signature unknown; restored from __doc__
    """ pat_new() -> list """
    return []

def section_from_nit(nit): # real signature unknown; restored from __doc__
    """ section_from_nit(nit:GstMpegts.NIT) -> GstMpegts.Section """
    pass

def section_from_pat(programs, ts_id): # real signature unknown; restored from __doc__
    """ section_from_pat(programs:list, ts_id:int) -> GstMpegts.Section """
    pass

def section_from_pmt(pmt, pid): # real signature unknown; restored from __doc__
    """ section_from_pmt(pmt:GstMpegts.PMT, pid:int) -> GstMpegts.Section """
    pass

def section_from_sdt(sdt): # real signature unknown; restored from __doc__
    """ section_from_sdt(sdt:GstMpegts.SDT) -> GstMpegts.Section """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .ATSCDescriptorType import ATSCDescriptorType
from .AtscEIT import AtscEIT
from .AtscEITEvent import AtscEITEvent
from .AtscETT import AtscETT
from .AtscMGT import AtscMGT
from .AtscMGTTable import AtscMGTTable
from .AtscMGTTableType import AtscMGTTableType
from .AtscMultString import AtscMultString
from .AtscStringSegment import AtscStringSegment
from .AtscSTT import AtscSTT
from .AtscVCT import AtscVCT
from .AtscVCTSource import AtscVCTSource
from .BAT import BAT
from .BATStream import BATStream
from .CableDeliverySystemDescriptor import CableDeliverySystemDescriptor
from .CableOuterFECScheme import CableOuterFECScheme
from .ComponentDescriptor import ComponentDescriptor
from .ComponentStreamContent import ComponentStreamContent
from .Content import Content
from .ContentNibbleHi import ContentNibbleHi
from .DataBroadcastDescriptor import DataBroadcastDescriptor
from .Descriptor import Descriptor
from .DescriptorType import DescriptorType
from .DVBCodeRate import DVBCodeRate
from .DVBDescriptorType import DVBDescriptorType
from .DVBExtendedDescriptorType import DVBExtendedDescriptorType
from .DVBLinkageDescriptor import DVBLinkageDescriptor
from .DVBLinkageEvent import DVBLinkageEvent
from .DVBLinkageExtendedEvent import DVBLinkageExtendedEvent
from .DVBLinkageHandOverType import DVBLinkageHandOverType
from .DVBLinkageMobileHandOver import DVBLinkageMobileHandOver
from .DVBLinkageType import DVBLinkageType
from .DvbMultilingualBouquetNameItem import DvbMultilingualBouquetNameItem
from .DvbMultilingualComponentItem import DvbMultilingualComponentItem
from .DvbMultilingualNetworkNameItem import DvbMultilingualNetworkNameItem
from .DvbMultilingualServiceNameItem import DvbMultilingualServiceNameItem
from .DVBParentalRatingItem import DVBParentalRatingItem
from .DVBScramblingModeType import DVBScramblingModeType
from .DVBServiceListItem import DVBServiceListItem
from .DVBServiceType import DVBServiceType
from .DVBTeletextType import DVBTeletextType
from .EIT import EIT
from .EITEvent import EITEvent
from .ExtendedEventDescriptor import ExtendedEventDescriptor
from .ExtendedEventItem import ExtendedEventItem
from .ISDBDescriptorType import ISDBDescriptorType
from .Iso639AudioType import Iso639AudioType
from .ISO639LanguageDescriptor import ISO639LanguageDescriptor
from .LogicalChannel import LogicalChannel
from .LogicalChannelDescriptor import LogicalChannelDescriptor
from .MiscDescriptorType import MiscDescriptorType
from .ModulationType import ModulationType
from .NIT import NIT
from .NITStream import NITStream
from .PatProgram import PatProgram
from .PMT import PMT
from .PMTStream import PMTStream
from .RunningStatus import RunningStatus
from .SatelliteDeliverySystemDescriptor import SatelliteDeliverySystemDescriptor
from .SatellitePolarizationType import SatellitePolarizationType
from .SatelliteRolloff import SatelliteRolloff
from .ScteStreamType import ScteStreamType
from .SDT import SDT
from .SDTService import SDTService
from .Section import Section
from .SectionATSCTableID import SectionATSCTableID
from .SectionDVBTableID import SectionDVBTableID
from .SectionSCTETableID import SectionSCTETableID
from .SectionTableID import SectionTableID
from .SectionType import SectionType
from .StreamType import StreamType
from .T2DeliverySystemCell import T2DeliverySystemCell
from .T2DeliverySystemCellExtension import T2DeliverySystemCellExtension
from .T2DeliverySystemDescriptor import T2DeliverySystemDescriptor
from .TerrestrialDeliverySystemDescriptor import TerrestrialDeliverySystemDescriptor
from .TerrestrialGuardInterval import TerrestrialGuardInterval
from .TerrestrialHierarchy import TerrestrialHierarchy
from .TerrestrialTransmissionMode import TerrestrialTransmissionMode
from .TOT import TOT
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7faa607a0d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GstMpegts-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GstMpegts', loader=<gi.importer.DynamicImporter object at 0x7faa607a0d00>)"

