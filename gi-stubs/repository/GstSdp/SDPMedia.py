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


class SDPMedia(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        SDPMedia()
    """
    def add_attribute(self, key, value=None): # real signature unknown; restored from __doc__
        """ add_attribute(self, key:str, value:str=None) -> GstSdp.SDPResult """
        pass

    def add_bandwidth(self, bwtype, bandwidth): # real signature unknown; restored from __doc__
        """ add_bandwidth(self, bwtype:str, bandwidth:int) -> GstSdp.SDPResult """
        pass

    def add_connection(self, nettype, addrtype, address, ttl, addr_number): # real signature unknown; restored from __doc__
        """ add_connection(self, nettype:str, addrtype:str, address:str, ttl:int, addr_number:int) -> GstSdp.SDPResult """
        pass

    def add_format(self, format): # real signature unknown; restored from __doc__
        """ add_format(self, format:str) -> GstSdp.SDPResult """
        pass

    def as_text(self): # real signature unknown; restored from __doc__
        """ as_text(self) -> str """
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

    def connections_len(self): # real signature unknown; restored from __doc__
        """ connections_len(self) -> int """
        return 0

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstSdp.SDPResult, copy:GstSdp.SDPMedia """
        pass

    def formats_len(self): # real signature unknown; restored from __doc__
        """ formats_len(self) -> int """
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

    def get_caps_from_media(self, pt): # real signature unknown; restored from __doc__
        """ get_caps_from_media(self, pt:int) -> Gst.Caps """
        pass

    def get_connection(self, idx): # real signature unknown; restored from __doc__
        """ get_connection(self, idx:int) -> GstSdp.SDPConnection """
        pass

    def get_format(self, idx): # real signature unknown; restored from __doc__
        """ get_format(self, idx:int) -> str """
        return ""

    def get_information(self): # real signature unknown; restored from __doc__
        """ get_information(self) -> str """
        return ""

    def get_key(self): # real signature unknown; restored from __doc__
        """ get_key(self) -> GstSdp.SDPKey """
        pass

    def get_media(self): # real signature unknown; restored from __doc__
        """ get_media(self) -> str """
        return ""

    def get_num_ports(self): # real signature unknown; restored from __doc__
        """ get_num_ports(self) -> int """
        return 0

    def get_port(self): # real signature unknown; restored from __doc__
        """ get_port(self) -> int """
        return 0

    def get_proto(self): # real signature unknown; restored from __doc__
        """ get_proto(self) -> str """
        return ""

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) -> GstSdp.SDPResult """
        pass

    def insert_attribute(self, idx, attr): # real signature unknown; restored from __doc__
        """ insert_attribute(self, idx:int, attr:GstSdp.SDPAttribute) -> GstSdp.SDPResult """
        pass

    def insert_bandwidth(self, idx, bw): # real signature unknown; restored from __doc__
        """ insert_bandwidth(self, idx:int, bw:GstSdp.SDPBandwidth) -> GstSdp.SDPResult """
        pass

    def insert_connection(self, idx, conn): # real signature unknown; restored from __doc__
        """ insert_connection(self, idx:int, conn:GstSdp.SDPConnection) -> GstSdp.SDPResult """
        pass

    def insert_format(self, idx, format): # real signature unknown; restored from __doc__
        """ insert_format(self, idx:int, format:str) -> GstSdp.SDPResult """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GstSdp.SDPResult, media:GstSdp.SDPMedia """
        pass

    def parse_keymgmt(self): # real signature unknown; restored from __doc__
        """ parse_keymgmt(self) -> GstSdp.SDPResult, mikey:GstSdp.MIKEYMessage """
        pass

    def remove_attribute(self, idx): # real signature unknown; restored from __doc__
        """ remove_attribute(self, idx:int) -> GstSdp.SDPResult """
        pass

    def remove_bandwidth(self, idx): # real signature unknown; restored from __doc__
        """ remove_bandwidth(self, idx:int) -> GstSdp.SDPResult """
        pass

    def remove_connection(self, idx): # real signature unknown; restored from __doc__
        """ remove_connection(self, idx:int) -> GstSdp.SDPResult """
        pass

    def remove_format(self, idx): # real signature unknown; restored from __doc__
        """ remove_format(self, idx:int) -> GstSdp.SDPResult """
        pass

    def replace_attribute(self, idx, attr): # real signature unknown; restored from __doc__
        """ replace_attribute(self, idx:int, attr:GstSdp.SDPAttribute) -> GstSdp.SDPResult """
        pass

    def replace_bandwidth(self, idx, bw): # real signature unknown; restored from __doc__
        """ replace_bandwidth(self, idx:int, bw:GstSdp.SDPBandwidth) -> GstSdp.SDPResult """
        pass

    def replace_connection(self, idx, conn): # real signature unknown; restored from __doc__
        """ replace_connection(self, idx:int, conn:GstSdp.SDPConnection) -> GstSdp.SDPResult """
        pass

    def replace_format(self, idx, format): # real signature unknown; restored from __doc__
        """ replace_format(self, idx:int, format:str) -> GstSdp.SDPResult """
        pass

    def set_information(self, information): # real signature unknown; restored from __doc__
        """ set_information(self, information:str) -> GstSdp.SDPResult """
        pass

    def set_key(self, type, data): # real signature unknown; restored from __doc__
        """ set_key(self, type:str, data:str) -> GstSdp.SDPResult """
        pass

    def set_media(self, med): # real signature unknown; restored from __doc__
        """ set_media(self, med:str) -> GstSdp.SDPResult """
        pass

    def set_media_from_caps(self, caps, media): # real signature unknown; restored from __doc__
        """ set_media_from_caps(caps:Gst.Caps, media:GstSdp.SDPMedia) -> GstSdp.SDPResult """
        pass

    def set_port_info(self, port, num_ports): # real signature unknown; restored from __doc__
        """ set_port_info(self, port:int, num_ports:int) -> GstSdp.SDPResult """
        pass

    def set_proto(self, proto): # real signature unknown; restored from __doc__
        """ set_proto(self, proto:str) -> GstSdp.SDPResult """
        pass

    def uninit(self): # real signature unknown; restored from __doc__
        """ uninit(self) -> GstSdp.SDPResult """
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

    connections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fmts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    information = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    media = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_ports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SDPMedia), '__module__': 'gi.repository.GstSdp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'SDPMedia' objects>, '__weakref__': <attribute '__weakref__' of 'SDPMedia' objects>, '__doc__': None, 'media': <property object at 0x7f89a60353b0>, 'port': <property object at 0x7f89a60354a0>, 'num_ports': <property object at 0x7f89a6035590>, 'proto': <property object at 0x7f89a6035680>, 'fmts': <property object at 0x7f89a6035770>, 'information': <property object at 0x7f89a6035860>, 'connections': <property object at 0x7f89a6035950>, 'bandwidths': <property object at 0x7f89a6035a40>, 'key': <property object at 0x7f89a6035b30>, 'attributes': <property object at 0x7f89a6035c20>, 'add_attribute': gi.FunctionInfo(add_attribute), 'add_bandwidth': gi.FunctionInfo(add_bandwidth), 'add_connection': gi.FunctionInfo(add_connection), 'add_format': gi.FunctionInfo(add_format), 'as_text': gi.FunctionInfo(as_text), 'attributes_len': gi.FunctionInfo(attributes_len), 'attributes_to_caps': gi.FunctionInfo(attributes_to_caps), 'bandwidths_len': gi.FunctionInfo(bandwidths_len), 'connections_len': gi.FunctionInfo(connections_len), 'copy': gi.FunctionInfo(copy), 'formats_len': gi.FunctionInfo(formats_len), 'free': gi.FunctionInfo(free), 'get_attribute': gi.FunctionInfo(get_attribute), 'get_attribute_val': gi.FunctionInfo(get_attribute_val), 'get_attribute_val_n': gi.FunctionInfo(get_attribute_val_n), 'get_bandwidth': gi.FunctionInfo(get_bandwidth), 'get_caps_from_media': gi.FunctionInfo(get_caps_from_media), 'get_connection': gi.FunctionInfo(get_connection), 'get_format': gi.FunctionInfo(get_format), 'get_information': gi.FunctionInfo(get_information), 'get_key': gi.FunctionInfo(get_key), 'get_media': gi.FunctionInfo(get_media), 'get_num_ports': gi.FunctionInfo(get_num_ports), 'get_port': gi.FunctionInfo(get_port), 'get_proto': gi.FunctionInfo(get_proto), 'init': gi.FunctionInfo(init), 'insert_attribute': gi.FunctionInfo(insert_attribute), 'insert_bandwidth': gi.FunctionInfo(insert_bandwidth), 'insert_connection': gi.FunctionInfo(insert_connection), 'insert_format': gi.FunctionInfo(insert_format), 'parse_keymgmt': gi.FunctionInfo(parse_keymgmt), 'remove_attribute': gi.FunctionInfo(remove_attribute), 'remove_bandwidth': gi.FunctionInfo(remove_bandwidth), 'remove_connection': gi.FunctionInfo(remove_connection), 'remove_format': gi.FunctionInfo(remove_format), 'replace_attribute': gi.FunctionInfo(replace_attribute), 'replace_bandwidth': gi.FunctionInfo(replace_bandwidth), 'replace_connection': gi.FunctionInfo(replace_connection), 'replace_format': gi.FunctionInfo(replace_format), 'set_information': gi.FunctionInfo(set_information), 'set_key': gi.FunctionInfo(set_key), 'set_media': gi.FunctionInfo(set_media), 'set_port_info': gi.FunctionInfo(set_port_info), 'set_proto': gi.FunctionInfo(set_proto), 'uninit': gi.FunctionInfo(uninit), 'new': gi.FunctionInfo(new), 'set_media_from_caps': gi.FunctionInfo(set_media_from_caps)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(SDPMedia)


