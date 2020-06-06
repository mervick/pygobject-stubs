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


class Descriptor(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Descriptor()
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_custom(self, tag, data): # real signature unknown; restored from __doc__
        """ from_custom(tag:int, data:list) -> GstMpegts.Descriptor """
        pass

    def from_custom_with_extension(self, tag, tag_extension, data): # real signature unknown; restored from __doc__
        """ from_custom_with_extension(tag:int, tag_extension:int, data:list) -> GstMpegts.Descriptor """
        pass

    def from_dvb_network_name(self, name): # real signature unknown; restored from __doc__
        """ from_dvb_network_name(name:str) -> GstMpegts.Descriptor """
        pass

    def from_dvb_service(self, service_type, service_name=None, service_provider=None): # real signature unknown; restored from __doc__
        """ from_dvb_service(service_type:GstMpegts.DVBServiceType, service_name:str=None, service_provider:str=None) -> GstMpegts.Descriptor """
        pass

    def from_dvb_subtitling(self, lang, type, composition, ancillary): # real signature unknown; restored from __doc__
        """ from_dvb_subtitling(lang:str, type:int, composition:int, ancillary:int) -> GstMpegts.Descriptor """
        pass

    def from_iso_639_language(self, language): # real signature unknown; restored from __doc__
        """ from_iso_639_language(language:str) -> GstMpegts.Descriptor """
        pass

    def from_registration(self, format_identifier, additional_info=None): # real signature unknown; restored from __doc__
        """ from_registration(format_identifier:str, additional_info:list=None) -> GstMpegts.Descriptor """
        pass

    def parse_ca(self): # real signature unknown; restored from __doc__
        """ parse_ca(self) -> bool, ca_system_id:int, ca_pid:int, private_data:list """
        return False

    def parse_cable_delivery_system(self): # real signature unknown; restored from __doc__
        """ parse_cable_delivery_system(self) -> bool, res:GstMpegts.CableDeliverySystemDescriptor """
        return False

    def parse_dvb_bouquet_name(self): # real signature unknown; restored from __doc__
        """ parse_dvb_bouquet_name(self) -> bool, bouquet_name:str """
        return False

    def parse_dvb_ca_identifier(self): # real signature unknown; restored from __doc__
        """ parse_dvb_ca_identifier(self) -> bool, list:list """
        return False

    def parse_dvb_component(self): # real signature unknown; restored from __doc__
        """ parse_dvb_component(self) -> bool, res:GstMpegts.ComponentDescriptor """
        return False

    def parse_dvb_content(self): # real signature unknown; restored from __doc__
        """ parse_dvb_content(self) -> bool, content:list """
        return False

    def parse_dvb_data_broadcast(self): # real signature unknown; restored from __doc__
        """ parse_dvb_data_broadcast(self) -> bool, res:GstMpegts.DataBroadcastDescriptor """
        return False

    def parse_dvb_data_broadcast_id(self): # real signature unknown; restored from __doc__
        """ parse_dvb_data_broadcast_id(self) -> bool, data_broadcast_id:int, id_selector_bytes:list """
        return False

    def parse_dvb_extended_event(self): # real signature unknown; restored from __doc__
        """ parse_dvb_extended_event(self) -> bool, res:GstMpegts.ExtendedEventDescriptor """
        return False

    def parse_dvb_frequency_list(self): # real signature unknown; restored from __doc__
        """ parse_dvb_frequency_list(self) -> bool, offset:bool, list:list """
        return False

    def parse_dvb_linkage(self): # real signature unknown; restored from __doc__
        """ parse_dvb_linkage(self) -> bool, res:GstMpegts.DVBLinkageDescriptor """
        return False

    def parse_dvb_multilingual_bouquet_name(self): # real signature unknown; restored from __doc__
        """ parse_dvb_multilingual_bouquet_name(self) -> bool, bouquet_name_items:list """
        return False

    def parse_dvb_multilingual_component(self): # real signature unknown; restored from __doc__
        """ parse_dvb_multilingual_component(self) -> bool, component_tag:int, component_description_items:list """
        return False

    def parse_dvb_multilingual_network_name(self): # real signature unknown; restored from __doc__
        """ parse_dvb_multilingual_network_name(self) -> bool, network_name_items:list """
        return False

    def parse_dvb_multilingual_service_name(self): # real signature unknown; restored from __doc__
        """ parse_dvb_multilingual_service_name(self) -> bool, service_name_items:list """
        return False

    def parse_dvb_network_name(self): # real signature unknown; restored from __doc__
        """ parse_dvb_network_name(self) -> bool, name:str """
        return False

    def parse_dvb_parental_rating(self): # real signature unknown; restored from __doc__
        """ parse_dvb_parental_rating(self) -> bool, rating:list """
        return False

    def parse_dvb_private_data_specifier(self): # real signature unknown; restored from __doc__
        """ parse_dvb_private_data_specifier(self) -> bool, private_data_specifier:int, private_data:list """
        return False

    def parse_dvb_scrambling(self): # real signature unknown; restored from __doc__
        """ parse_dvb_scrambling(self) -> bool, scrambling_mode:GstMpegts.DVBScramblingModeType """
        return False

    def parse_dvb_service(self): # real signature unknown; restored from __doc__
        """ parse_dvb_service(self) -> bool, service_type:GstMpegts.DVBServiceType, service_name:str, provider_name:str """
        return False

    def parse_dvb_service_list(self): # real signature unknown; restored from __doc__
        """ parse_dvb_service_list(self) -> bool, list:list """
        return False

    def parse_dvb_short_event(self): # real signature unknown; restored from __doc__
        """ parse_dvb_short_event(self) -> bool, language_code:str, event_name:str, text:str """
        return False

    def parse_dvb_stream_identifier(self): # real signature unknown; restored from __doc__
        """ parse_dvb_stream_identifier(self) -> bool, component_tag:int """
        return False

    def parse_dvb_stuffing(self): # real signature unknown; restored from __doc__
        """ parse_dvb_stuffing(self) -> bool, stuffing_bytes:int """
        return False

    def parse_dvb_subtitling_idx(self, idx): # real signature unknown; restored from __doc__
        """ parse_dvb_subtitling_idx(self, idx:int) -> bool, lang:str, type:int, composition_page_id:int, ancillary_page_id:int """
        return False

    def parse_dvb_subtitling_nb(self): # real signature unknown; restored from __doc__
        """ parse_dvb_subtitling_nb(self) -> int """
        return 0

    def parse_dvb_t2_delivery_system(self): # real signature unknown; restored from __doc__
        """ parse_dvb_t2_delivery_system(self) -> bool, res:GstMpegts.T2DeliverySystemDescriptor """
        return False

    def parse_dvb_teletext_idx(self, idx): # real signature unknown; restored from __doc__
        """ parse_dvb_teletext_idx(self, idx:int) -> bool, language_code:str, teletext_type:GstMpegts.DVBTeletextType, magazine_number:int, page_number:int """
        return False

    def parse_dvb_teletext_nb(self): # real signature unknown; restored from __doc__
        """ parse_dvb_teletext_nb(self) -> int """
        return 0

    def parse_iso_639_language(self): # real signature unknown; restored from __doc__
        """ parse_iso_639_language(self) -> bool, res:GstMpegts.ISO639LanguageDescriptor """
        return False

    def parse_iso_639_language_idx(self, idx): # real signature unknown; restored from __doc__
        """ parse_iso_639_language_idx(self, idx:int) -> bool, lang:str, audio_type:GstMpegts.Iso639AudioType """
        return False

    def parse_iso_639_language_nb(self): # real signature unknown; restored from __doc__
        """ parse_iso_639_language_nb(self) -> int """
        return 0

    def parse_logical_channel(self): # real signature unknown; restored from __doc__
        """ parse_logical_channel(self) -> bool, res:GstMpegts.LogicalChannelDescriptor """
        return False

    def parse_satellite_delivery_system(self): # real signature unknown; restored from __doc__
        """ parse_satellite_delivery_system(self) -> bool, res:GstMpegts.SatelliteDeliverySystemDescriptor """
        return False

    def parse_terrestrial_delivery_system(self): # real signature unknown; restored from __doc__
        """ parse_terrestrial_delivery_system(self) -> bool, res:GstMpegts.TerrestrialDeliverySystemDescriptor """
        return False

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tag_extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Descriptor), '__module__': 'gi.repository.GstMpegts', '__gtype__': <GType GstMpegtsDescriptor (94624018595216)>, '__dict__': <attribute '__dict__' of 'Descriptor' objects>, '__weakref__': <attribute '__weakref__' of 'Descriptor' objects>, '__doc__': None, 'tag': <property object at 0x7faa5f947860>, 'tag_extension': <property object at 0x7faa5f947950>, 'length': <property object at 0x7faa5f947a40>, 'data': <property object at 0x7faa5f947b30>, '_gst_reserved': <property object at 0x7faa5f947c20>, 'free': gi.FunctionInfo(free), 'parse_ca': gi.FunctionInfo(parse_ca), 'parse_cable_delivery_system': gi.FunctionInfo(parse_cable_delivery_system), 'parse_dvb_bouquet_name': gi.FunctionInfo(parse_dvb_bouquet_name), 'parse_dvb_ca_identifier': gi.FunctionInfo(parse_dvb_ca_identifier), 'parse_dvb_component': gi.FunctionInfo(parse_dvb_component), 'parse_dvb_content': gi.FunctionInfo(parse_dvb_content), 'parse_dvb_data_broadcast': gi.FunctionInfo(parse_dvb_data_broadcast), 'parse_dvb_data_broadcast_id': gi.FunctionInfo(parse_dvb_data_broadcast_id), 'parse_dvb_extended_event': gi.FunctionInfo(parse_dvb_extended_event), 'parse_dvb_frequency_list': gi.FunctionInfo(parse_dvb_frequency_list), 'parse_dvb_linkage': gi.FunctionInfo(parse_dvb_linkage), 'parse_dvb_multilingual_bouquet_name': gi.FunctionInfo(parse_dvb_multilingual_bouquet_name), 'parse_dvb_multilingual_component': gi.FunctionInfo(parse_dvb_multilingual_component), 'parse_dvb_multilingual_network_name': gi.FunctionInfo(parse_dvb_multilingual_network_name), 'parse_dvb_multilingual_service_name': gi.FunctionInfo(parse_dvb_multilingual_service_name), 'parse_dvb_network_name': gi.FunctionInfo(parse_dvb_network_name), 'parse_dvb_parental_rating': gi.FunctionInfo(parse_dvb_parental_rating), 'parse_dvb_private_data_specifier': gi.FunctionInfo(parse_dvb_private_data_specifier), 'parse_dvb_scrambling': gi.FunctionInfo(parse_dvb_scrambling), 'parse_dvb_service': gi.FunctionInfo(parse_dvb_service), 'parse_dvb_service_list': gi.FunctionInfo(parse_dvb_service_list), 'parse_dvb_short_event': gi.FunctionInfo(parse_dvb_short_event), 'parse_dvb_stream_identifier': gi.FunctionInfo(parse_dvb_stream_identifier), 'parse_dvb_stuffing': gi.FunctionInfo(parse_dvb_stuffing), 'parse_dvb_subtitling_idx': gi.FunctionInfo(parse_dvb_subtitling_idx), 'parse_dvb_subtitling_nb': gi.FunctionInfo(parse_dvb_subtitling_nb), 'parse_dvb_t2_delivery_system': gi.FunctionInfo(parse_dvb_t2_delivery_system), 'parse_dvb_teletext_idx': gi.FunctionInfo(parse_dvb_teletext_idx), 'parse_dvb_teletext_nb': gi.FunctionInfo(parse_dvb_teletext_nb), 'parse_iso_639_language': gi.FunctionInfo(parse_iso_639_language), 'parse_iso_639_language_idx': gi.FunctionInfo(parse_iso_639_language_idx), 'parse_iso_639_language_nb': gi.FunctionInfo(parse_iso_639_language_nb), 'parse_logical_channel': gi.FunctionInfo(parse_logical_channel), 'parse_satellite_delivery_system': gi.FunctionInfo(parse_satellite_delivery_system), 'parse_terrestrial_delivery_system': gi.FunctionInfo(parse_terrestrial_delivery_system), 'from_custom': gi.FunctionInfo(from_custom), 'from_custom_with_extension': gi.FunctionInfo(from_custom_with_extension), 'from_dvb_network_name': gi.FunctionInfo(from_dvb_network_name), 'from_dvb_service': gi.FunctionInfo(from_dvb_service), 'from_dvb_subtitling': gi.FunctionInfo(from_dvb_subtitling), 'from_iso_639_language': gi.FunctionInfo(from_iso_639_language), 'from_registration': gi.FunctionInfo(from_registration)})"
    __gtype__ = None # (!) real value is '<GType GstMpegtsDescriptor (94624018595216)>'
    __info__ = StructInfo(Descriptor)


