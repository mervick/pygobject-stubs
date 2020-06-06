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


class RTSPTransport(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        RTSPTransport()
    """
    def as_text(self): # real signature unknown; restored from __doc__
        """ as_text(self) -> str """
        return ""

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) -> GstRtsp.RTSPResult """
        pass

    def get_manager(self, trans, option): # real signature unknown; restored from __doc__
        """ get_manager(trans:GstRtsp.RTSPTransMode, option:int) -> GstRtsp.RTSPResult, manager:str """
        pass

    def get_media_type(self): # real signature unknown; restored from __doc__
        """ get_media_type(self) -> GstRtsp.RTSPResult, media_type:str """
        pass

    def get_mime(self, trans, mime): # real signature unknown; restored from __doc__
        """ get_mime(trans:GstRtsp.RTSPTransMode, mime:str) -> GstRtsp.RTSPResult """
        pass

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) -> GstRtsp.RTSPResult """
        pass

    def new(self, transport): # real signature unknown; restored from __doc__
        """ new(transport:GstRtsp.RTSPTransport) -> GstRtsp.RTSPResult """
        pass

    def parse(self, p_str, transport): # real signature unknown; restored from __doc__
        """ parse(str:str, transport:GstRtsp.RTSPTransport) -> GstRtsp.RTSPResult """
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

    append = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    client_port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interleaved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lower_transport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode_play = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode_record = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ssrc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trans = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ttl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RTSPTransport), '__module__': 'gi.repository.GstRtsp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RTSPTransport' objects>, '__weakref__': <attribute '__weakref__' of 'RTSPTransport' objects>, '__doc__': None, 'trans': <property object at 0x7ff1b34dca90>, 'profile': <property object at 0x7ff1b34dcb80>, 'lower_transport': <property object at 0x7ff1b34dcc70>, 'destination': <property object at 0x7ff1b34dcd60>, 'source': <property object at 0x7ff1b34dce50>, 'layers': <property object at 0x7ff1b34dcf40>, 'mode_play': <property object at 0x7ff1b3249090>, 'mode_record': <property object at 0x7ff1b3249180>, 'append': <property object at 0x7ff1b3249270>, 'interleaved': <property object at 0x7ff1b3249360>, 'ttl': <property object at 0x7ff1b3249450>, 'port': <property object at 0x7ff1b3249540>, 'client_port': <property object at 0x7ff1b3249630>, 'server_port': <property object at 0x7ff1b3249720>, 'ssrc': <property object at 0x7ff1b3249810>, '_gst_reserved': <property object at 0x7ff1b3249900>, 'as_text': gi.FunctionInfo(as_text), 'free': gi.FunctionInfo(free), 'get_media_type': gi.FunctionInfo(get_media_type), 'init': gi.FunctionInfo(init), 'get_manager': gi.FunctionInfo(get_manager), 'get_mime': gi.FunctionInfo(get_mime), 'new': gi.FunctionInfo(new), 'parse': gi.FunctionInfo(parse)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RTSPTransport)


