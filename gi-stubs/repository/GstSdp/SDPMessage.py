# encoding: utf-8
# module gi.repository.GstSdp
# from /usr/lib64/girepository-1.0/GstSdp-1.0.typelib
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


class SDPMessage(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        SDPMessage()
    """
    def add_attribute(self, key, value=None): # real signature unknown; restored from __doc__
        """ add_attribute(self, key:str, value:str=None) -> GstSdp.SDPResult """
        pass

    def add_bandwidth(self, bwtype, bandwidth): # real signature unknown; restored from __doc__
        """ add_bandwidth(self, bwtype:str, bandwidth:int) -> GstSdp.SDPResult """
        pass

    def add_email(self, email): # real signature unknown; restored from __doc__
        """ add_email(self, email:str) -> GstSdp.SDPResult """
        pass

    def add_media(self, media): # real signature unknown; restored from __doc__
        """ add_media(self, media:GstSdp.SDPMedia) -> GstSdp.SDPResult """
        pass

    def add_phone(self, phone): # real signature unknown; restored from __doc__
        """ add_phone(self, phone:str) -> GstSdp.SDPResult """
        pass

    def add_time(self, start, stop, repeat): # real signature unknown; restored from __doc__
        """ add_time(self, start:str, stop:str, repeat:list) -> GstSdp.SDPResult """
        pass

    def add_zone(self, adj_time, typed_time): # real signature unknown; restored from __doc__
        """ add_zone(self, adj_time:str, typed_time:str) -> GstSdp.SDPResult """
        pass

    def as_text(self): # real signature unknown; restored from __doc__
        """ as_text(self) -> str """
        return ""

    def as_uri(self, scheme, msg): # real signature unknown; restored from __doc__
        """ as_uri(scheme:str, msg:GstSdp.SDPMessage) -> str """
        return ""

    def attributes_len(self): # real signature unknown; restored from __doc__
        """ attributes_len(self) -> int """
        return 0

    def attributes_to_caps(self, caps): # real signature unknown; restored from __doc__
        """ attributes_to_caps(self, caps:Gst.Caps) -> GstSdp.SDPResult """
        pass

    def bandwidths_len(self): # real signature unknown; restored from __doc__
        """ bandwidths_len(self) -> int """
        return 0

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstSdp.SDPResult, copy:GstSdp.SDPMessage """
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """ dump(self) -> GstSdp.SDPResult """
        pass

    def emails_len(self): # real signature unknown; restored from __doc__
        """ emails_len(self) -> int """
        return 0

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) -> GstSdp.SDPResult """
        pass

    def get_attribute(self, idx): # real signature unknown; restored from __doc__
        """ get_attribute(self, idx:int) -> GstSdp.SDPAttribute """
        pass

    def get_attribute_val(self, key): # real signature unknown; restored from __doc__
        """ get_attribute_val(self, key:str) -> str """
        return ""

    def get_attribute_val_n(self, key, nth): # real signature unknown; restored from __doc__
        """ get_attribute_val_n(self, key:str, nth:int) -> str """
        return ""

    def get_bandwidth(self, idx): # real signature unknown; restored from __doc__
        """ get_bandwidth(self, idx:int) -> GstSdp.SDPBandwidth """
        pass

    def get_connection(self): # real signature unknown; restored from __doc__
        """ get_connection(self) -> GstSdp.SDPConnection """
        pass

    def get_email(self, idx): # real signature unknown; restored from __doc__
        """ get_email(self, idx:int) -> str """
        return ""

    def get_information(self): # real signature unknown; restored from __doc__
        """ get_information(self) -> str """
        return ""

    def get_key(self): # real signature unknown; restored from __doc__
        """ get_key(self) -> GstSdp.SDPKey """
        pass

    def get_media(self, idx): # real signature unknown; restored from __doc__
        """ get_media(self, idx:int) -> GstSdp.SDPMedia """
        pass

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> GstSdp.SDPOrigin """
        pass

    def get_phone(self, idx): # real signature unknown; restored from __doc__
        """ get_phone(self, idx:int) -> str """
        return ""

    def get_session_name(self): # real signature unknown; restored from __doc__
        """ get_session_name(self) -> str """
        return ""

    def get_time(self, idx): # real signature unknown; restored from __doc__
        """ get_time(self, idx:int) -> GstSdp.SDPTime """
        pass

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> str """
        return ""

    def get_zone(self, idx): # real signature unknown; restored from __doc__
        """ get_zone(self, idx:int) -> GstSdp.SDPZone """
        pass

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) -> GstSdp.SDPResult """
        pass

    def insert_attribute(self, idx, attr): # real signature unknown; restored from __doc__
        """ insert_attribute(self, idx:int, attr:GstSdp.SDPAttribute) -> GstSdp.SDPResult """
        pass

    def insert_bandwidth(self, idx, bw): # real signature unknown; restored from __doc__
        """ insert_bandwidth(self, idx:int, bw:GstSdp.SDPBandwidth) -> GstSdp.SDPResult """
        pass

    def insert_email(self, idx, email): # real signature unknown; restored from __doc__
        """ insert_email(self, idx:int, email:str) -> GstSdp.SDPResult """
        pass

    def insert_phone(self, idx, phone): # real signature unknown; restored from __doc__
        """ insert_phone(self, idx:int, phone:str) -> GstSdp.SDPResult """
        pass

    def insert_time(self, idx, t): # real signature unknown; restored from __doc__
        """ insert_time(self, idx:int, t:GstSdp.SDPTime) -> GstSdp.SDPResult """
        pass

    def insert_zone(self, idx, zone): # real signature unknown; restored from __doc__
        """ insert_zone(self, idx:int, zone:GstSdp.SDPZone) -> GstSdp.SDPResult """
        pass

    def medias_len(self): # real signature unknown; restored from __doc__
        """ medias_len(self) -> int """
        return 0

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GstSdp.SDPResult, msg:GstSdp.SDPMessage """
        pass

    def new_from_text(self, text): # real signature unknown; restored from __doc__
        """ new_from_text(text:str) -> GstSdp.SDPResult, msg:GstSdp.SDPMessage """
        pass

    def parse_buffer(self, data, msg): # real signature unknown; restored from __doc__
        """ parse_buffer(data:list, msg:GstSdp.SDPMessage) -> GstSdp.SDPResult """
        pass

    def parse_keymgmt(self): # real signature unknown; restored from __doc__
        """ parse_keymgmt(self) -> GstSdp.SDPResult, mikey:GstSdp.MIKEYMessage """
        pass

    def parse_uri(self, uri, msg): # real signature unknown; restored from __doc__
        """ parse_uri(uri:str, msg:GstSdp.SDPMessage) -> GstSdp.SDPResult """
        pass

    def phones_len(self): # real signature unknown; restored from __doc__
        """ phones_len(self) -> int """
        return 0

    def remove_attribute(self, idx): # real signature unknown; restored from __doc__
        """ remove_attribute(self, idx:int) -> GstSdp.SDPResult """
        pass

    def remove_bandwidth(self, idx): # real signature unknown; restored from __doc__
        """ remove_bandwidth(self, idx:int) -> GstSdp.SDPResult """
        pass

    def remove_email(self, idx): # real signature unknown; restored from __doc__
        """ remove_email(self, idx:int) -> GstSdp.SDPResult """
        pass

    def remove_phone(self, idx): # real signature unknown; restored from __doc__
        """ remove_phone(self, idx:int) -> GstSdp.SDPResult """
        pass

    def remove_time(self, idx): # real signature unknown; restored from __doc__
        """ remove_time(self, idx:int) -> GstSdp.SDPResult """
        pass

    def remove_zone(self, idx): # real signature unknown; restored from __doc__
        """ remove_zone(self, idx:int) -> GstSdp.SDPResult """
        pass

    def replace_attribute(self, idx, attr): # real signature unknown; restored from __doc__
        """ replace_attribute(self, idx:int, attr:GstSdp.SDPAttribute) -> GstSdp.SDPResult """
        pass

    def replace_bandwidth(self, idx, bw): # real signature unknown; restored from __doc__
        """ replace_bandwidth(self, idx:int, bw:GstSdp.SDPBandwidth) -> GstSdp.SDPResult """
        pass

    def replace_email(self, idx, email): # real signature unknown; restored from __doc__
        """ replace_email(self, idx:int, email:str) -> GstSdp.SDPResult """
        pass

    def replace_phone(self, idx, phone): # real signature unknown; restored from __doc__
        """ replace_phone(self, idx:int, phone:str) -> GstSdp.SDPResult """
        pass

    def replace_time(self, idx, t): # real signature unknown; restored from __doc__
        """ replace_time(self, idx:int, t:GstSdp.SDPTime) -> GstSdp.SDPResult """
        pass

    def replace_zone(self, idx, zone): # real signature unknown; restored from __doc__
        """ replace_zone(self, idx:int, zone:GstSdp.SDPZone) -> GstSdp.SDPResult """
        pass

    def set_connection(self, nettype, addrtype, address, ttl, addr_number): # real signature unknown; restored from __doc__
        """ set_connection(self, nettype:str, addrtype:str, address:str, ttl:int, addr_number:int) -> GstSdp.SDPResult """
        pass

    def set_information(self, information): # real signature unknown; restored from __doc__
        """ set_information(self, information:str) -> GstSdp.SDPResult """
        pass

    def set_key(self, type, data): # real signature unknown; restored from __doc__
        """ set_key(self, type:str, data:str) -> GstSdp.SDPResult """
        pass

    def set_origin(self, username, sess_id, sess_version, nettype, addrtype, addr): # real signature unknown; restored from __doc__
        """ set_origin(self, username:str, sess_id:str, sess_version:str, nettype:str, addrtype:str, addr:str) -> GstSdp.SDPResult """
        pass

    def set_session_name(self, session_name): # real signature unknown; restored from __doc__
        """ set_session_name(self, session_name:str) -> GstSdp.SDPResult """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:str) -> GstSdp.SDPResult """
        pass

    def set_version(self, version): # real signature unknown; restored from __doc__
        """ set_version(self, version:str) -> GstSdp.SDPResult """
        pass

    def times_len(self): # real signature unknown; restored from __doc__
        """ times_len(self) -> int """
        return 0

    def uninit(self): # real signature unknown; restored from __doc__
        """ uninit(self) -> GstSdp.SDPResult """
        pass

    def zones_len(self): # real signature unknown; restored from __doc__
        """ zones_len(self) -> int """
        return 0

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

    attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bandwidths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    emails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    information = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    medias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    phones = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    session_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    times = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    zones = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SDPMessage), '__module__': 'gi.repository.GstSdp', '__gtype__': <GType GstSDPMessage (94778371633888)>, '__dict__': <attribute '__dict__' of 'SDPMessage' objects>, '__weakref__': <attribute '__weakref__' of 'SDPMessage' objects>, '__doc__': None, 'version': <property object at 0x7f89a60372c0>, 'origin': <property object at 0x7f89a60373b0>, 'session_name': <property object at 0x7f89a60374a0>, 'information': <property object at 0x7f89a6037590>, 'uri': <property object at 0x7f89a6037680>, 'emails': <property object at 0x7f89a6037770>, 'phones': <property object at 0x7f89a6037860>, 'connection': <property object at 0x7f89a6037950>, 'bandwidths': <property object at 0x7f89a6037a40>, 'times': <property object at 0x7f89a6037b30>, 'zones': <property object at 0x7f89a6037c20>, 'key': <property object at 0x7f89a6037d10>, 'attributes': <property object at 0x7f89a6037e00>, 'medias': <property object at 0x7f89a6037ef0>, 'add_attribute': gi.FunctionInfo(add_attribute), 'add_bandwidth': gi.FunctionInfo(add_bandwidth), 'add_email': gi.FunctionInfo(add_email), 'add_media': gi.FunctionInfo(add_media), 'add_phone': gi.FunctionInfo(add_phone), 'add_time': gi.FunctionInfo(add_time), 'add_zone': gi.FunctionInfo(add_zone), 'as_text': gi.FunctionInfo(as_text), 'attributes_len': gi.FunctionInfo(attributes_len), 'attributes_to_caps': gi.FunctionInfo(attributes_to_caps), 'bandwidths_len': gi.FunctionInfo(bandwidths_len), 'copy': gi.FunctionInfo(copy), 'dump': gi.FunctionInfo(dump), 'emails_len': gi.FunctionInfo(emails_len), 'free': gi.FunctionInfo(free), 'get_attribute': gi.FunctionInfo(get_attribute), 'get_attribute_val': gi.FunctionInfo(get_attribute_val), 'get_attribute_val_n': gi.FunctionInfo(get_attribute_val_n), 'get_bandwidth': gi.FunctionInfo(get_bandwidth), 'get_connection': gi.FunctionInfo(get_connection), 'get_email': gi.FunctionInfo(get_email), 'get_information': gi.FunctionInfo(get_information), 'get_key': gi.FunctionInfo(get_key), 'get_media': gi.FunctionInfo(get_media), 'get_origin': gi.FunctionInfo(get_origin), 'get_phone': gi.FunctionInfo(get_phone), 'get_session_name': gi.FunctionInfo(get_session_name), 'get_time': gi.FunctionInfo(get_time), 'get_uri': gi.FunctionInfo(get_uri), 'get_version': gi.FunctionInfo(get_version), 'get_zone': gi.FunctionInfo(get_zone), 'init': gi.FunctionInfo(init), 'insert_attribute': gi.FunctionInfo(insert_attribute), 'insert_bandwidth': gi.FunctionInfo(insert_bandwidth), 'insert_email': gi.FunctionInfo(insert_email), 'insert_phone': gi.FunctionInfo(insert_phone), 'insert_time': gi.FunctionInfo(insert_time), 'insert_zone': gi.FunctionInfo(insert_zone), 'medias_len': gi.FunctionInfo(medias_len), 'parse_keymgmt': gi.FunctionInfo(parse_keymgmt), 'phones_len': gi.FunctionInfo(phones_len), 'remove_attribute': gi.FunctionInfo(remove_attribute), 'remove_bandwidth': gi.FunctionInfo(remove_bandwidth), 'remove_email': gi.FunctionInfo(remove_email), 'remove_phone': gi.FunctionInfo(remove_phone), 'remove_time': gi.FunctionInfo(remove_time), 'remove_zone': gi.FunctionInfo(remove_zone), 'replace_attribute': gi.FunctionInfo(replace_attribute), 'replace_bandwidth': gi.FunctionInfo(replace_bandwidth), 'replace_email': gi.FunctionInfo(replace_email), 'replace_phone': gi.FunctionInfo(replace_phone), 'replace_time': gi.FunctionInfo(replace_time), 'replace_zone': gi.FunctionInfo(replace_zone), 'set_connection': gi.FunctionInfo(set_connection), 'set_information': gi.FunctionInfo(set_information), 'set_key': gi.FunctionInfo(set_key), 'set_origin': gi.FunctionInfo(set_origin), 'set_session_name': gi.FunctionInfo(set_session_name), 'set_uri': gi.FunctionInfo(set_uri), 'set_version': gi.FunctionInfo(set_version), 'times_len': gi.FunctionInfo(times_len), 'uninit': gi.FunctionInfo(uninit), 'zones_len': gi.FunctionInfo(zones_len), 'as_uri': gi.FunctionInfo(as_uri), 'new': gi.FunctionInfo(new), 'new_from_text': gi.FunctionInfo(new_from_text), 'parse_buffer': gi.FunctionInfo(parse_buffer), 'parse_uri': gi.FunctionInfo(parse_uri)})"
    __gtype__ = None # (!) real value is '<GType GstSDPMessage (94778371633888)>'
    __info__ = StructInfo(SDPMessage)


