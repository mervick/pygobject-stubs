# encoding: utf-8
# module gi.repository.GstRtsp
# from /usr/lib64/girepository-1.0/GstRtsp-1.0.typelib
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


class RTSPMessage(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        RTSPMessage()
    """
    def add_header(self, field, value): # real signature unknown; restored from __doc__
        """ add_header(self, field:GstRtsp.RTSPHeaderField, value:str) -> GstRtsp.RTSPResult """
        pass

    def add_header_by_name(self, header, value): # real signature unknown; restored from __doc__
        """ add_header_by_name(self, header:str, value:str) -> GstRtsp.RTSPResult """
        pass

    def append_headers(self, p_str): # real signature unknown; restored from __doc__
        """ append_headers(self, str:GLib.String) -> GstRtsp.RTSPResult """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstRtsp.RTSPResult, copy:GstRtsp.RTSPMessage """
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """ dump(self) -> GstRtsp.RTSPResult """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) -> GstRtsp.RTSPResult """
        pass

    def get_body(self): # real signature unknown; restored from __doc__
        """ get_body(self) -> GstRtsp.RTSPResult, data:list """
        pass

    def get_body_buffer(self): # real signature unknown; restored from __doc__
        """ get_body_buffer(self) -> GstRtsp.RTSPResult, buffer:Gst.Buffer """
        pass

    def get_header(self, field, indx): # real signature unknown; restored from __doc__
        """ get_header(self, field:GstRtsp.RTSPHeaderField, indx:int) -> GstRtsp.RTSPResult, value:str """
        pass

    def get_header_by_name(self, header, index): # real signature unknown; restored from __doc__
        """ get_header_by_name(self, header:str, index:int) -> GstRtsp.RTSPResult, value:str """
        pass

    def get_type(self): # real signature unknown; restored from __doc__
        """ get_type(self) -> GstRtsp.RTSPMsgType """
        pass

    def has_body_buffer(self): # real signature unknown; restored from __doc__
        """ has_body_buffer(self) -> bool """
        return False

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) -> GstRtsp.RTSPResult """
        pass

    def init_data(self, channel): # real signature unknown; restored from __doc__
        """ init_data(self, channel:int) -> GstRtsp.RTSPResult """
        pass

    def init_request(self, method, uri): # real signature unknown; restored from __doc__
        """ init_request(self, method:GstRtsp.RTSPMethod, uri:str) -> GstRtsp.RTSPResult """
        pass

    def init_response(self, code, reason=None, request=None): # real signature unknown; restored from __doc__
        """ init_response(self, code:GstRtsp.RTSPStatusCode, reason:str=None, request:GstRtsp.RTSPMessage=None) -> GstRtsp.RTSPResult """
        pass

    def parse_auth_credentials(self, field): # real signature unknown; restored from __doc__
        """ parse_auth_credentials(self, field:GstRtsp.RTSPHeaderField) -> list """
        return []

    def parse_data(self): # real signature unknown; restored from __doc__
        """ parse_data(self) -> GstRtsp.RTSPResult, channel:int """
        pass

    def parse_request(self): # real signature unknown; restored from __doc__
        """ parse_request(self) -> GstRtsp.RTSPResult, method:GstRtsp.RTSPMethod, uri:str, version:GstRtsp.RTSPVersion """
        pass

    def parse_response(self): # real signature unknown; restored from __doc__
        """ parse_response(self) -> GstRtsp.RTSPResult, code:GstRtsp.RTSPStatusCode, reason:str, version:GstRtsp.RTSPVersion """
        pass

    def remove_header(self, field, indx): # real signature unknown; restored from __doc__
        """ remove_header(self, field:GstRtsp.RTSPHeaderField, indx:int) -> GstRtsp.RTSPResult """
        pass

    def remove_header_by_name(self, header, index): # real signature unknown; restored from __doc__
        """ remove_header_by_name(self, header:str, index:int) -> GstRtsp.RTSPResult """
        pass

    def set_body(self, data): # real signature unknown; restored from __doc__
        """ set_body(self, data:list) -> GstRtsp.RTSPResult """
        pass

    def set_body_buffer(self, buffer): # real signature unknown; restored from __doc__
        """ set_body_buffer(self, buffer:Gst.Buffer) -> GstRtsp.RTSPResult """
        pass

    def steal_body(self): # real signature unknown; restored from __doc__
        """ steal_body(self) -> GstRtsp.RTSPResult, data:list """
        pass

    def steal_body_buffer(self): # real signature unknown; restored from __doc__
        """ steal_body_buffer(self) -> GstRtsp.RTSPResult, buffer:Gst.Buffer """
        pass

    def take_body(self, data): # real signature unknown; restored from __doc__
        """ take_body(self, data:list) -> GstRtsp.RTSPResult """
        pass

    def take_body_buffer(self, buffer): # real signature unknown; restored from __doc__
        """ take_body_buffer(self, buffer:Gst.Buffer) -> GstRtsp.RTSPResult """
        pass

    def take_header(self, field, value): # real signature unknown; restored from __doc__
        """ take_header(self, field:GstRtsp.RTSPHeaderField, value:str) -> GstRtsp.RTSPResult """
        pass

    def take_header_by_name(self, header, value): # real signature unknown; restored from __doc__
        """ take_header_by_name(self, header:str, value:str) -> GstRtsp.RTSPResult """
        pass

    def unset(self): # real signature unknown; restored from __doc__
        """ unset(self) -> GstRtsp.RTSPResult """
        pass

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

    body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hdr_fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RTSPMessage), '__module__': 'gi.repository.GstRtsp', '__gtype__': <GType GstRTSPMessage (93854382879936)>, '__dict__': <attribute '__dict__' of 'RTSPMessage' objects>, '__weakref__': <attribute '__weakref__' of 'RTSPMessage' objects>, '__doc__': None, 'type': <property object at 0x7ff1b34d2ae0>, 'hdr_fields': <property object at 0x7ff1b34d2bd0>, 'body': <property object at 0x7ff1b34d2cc0>, 'body_size': <property object at 0x7ff1b34d2db0>, 'body_buffer': <property object at 0x7ff1b34d2ea0>, '_gst_reserved': <property object at 0x7ff1b34d2f90>, 'add_header': gi.FunctionInfo(add_header), 'add_header_by_name': gi.FunctionInfo(add_header_by_name), 'append_headers': gi.FunctionInfo(append_headers), 'copy': gi.FunctionInfo(copy), 'dump': gi.FunctionInfo(dump), 'free': gi.FunctionInfo(free), 'get_body': gi.FunctionInfo(get_body), 'get_body_buffer': gi.FunctionInfo(get_body_buffer), 'get_header': gi.FunctionInfo(get_header), 'get_header_by_name': gi.FunctionInfo(get_header_by_name), 'get_type': gi.FunctionInfo(get_type), 'has_body_buffer': gi.FunctionInfo(has_body_buffer), 'init': gi.FunctionInfo(init), 'init_data': gi.FunctionInfo(init_data), 'init_request': gi.FunctionInfo(init_request), 'init_response': gi.FunctionInfo(init_response), 'parse_auth_credentials': gi.FunctionInfo(parse_auth_credentials), 'parse_data': gi.FunctionInfo(parse_data), 'parse_request': gi.FunctionInfo(parse_request), 'parse_response': gi.FunctionInfo(parse_response), 'remove_header': gi.FunctionInfo(remove_header), 'remove_header_by_name': gi.FunctionInfo(remove_header_by_name), 'set_body': gi.FunctionInfo(set_body), 'set_body_buffer': gi.FunctionInfo(set_body_buffer), 'steal_body': gi.FunctionInfo(steal_body), 'steal_body_buffer': gi.FunctionInfo(steal_body_buffer), 'take_body': gi.FunctionInfo(take_body), 'take_body_buffer': gi.FunctionInfo(take_body_buffer), 'take_header': gi.FunctionInfo(take_header), 'take_header_by_name': gi.FunctionInfo(take_header_by_name), 'unset': gi.FunctionInfo(unset)})"
    __gtype__ = None # (!) real value is '<GType GstRTSPMessage (93854382879936)>'
    __info__ = StructInfo(RTSPMessage)


