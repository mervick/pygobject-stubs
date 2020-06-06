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


class RTSPUrl(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        RTSPUrl()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstRtsp.RTSPUrl """
        pass

    def decode_path_components(self): # real signature unknown; restored from __doc__
        """ decode_path_components(self) -> list """
        return []

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_port(self): # real signature unknown; restored from __doc__
        """ get_port(self) -> GstRtsp.RTSPResult, port:int """
        pass

    def get_request_uri(self): # real signature unknown; restored from __doc__
        """ get_request_uri(self) -> str """
        return ""

    def parse(self, urlstr): # real signature unknown; restored from __doc__
        """ parse(urlstr:str) -> GstRtsp.RTSPResult, url:GstRtsp.RTSPUrl """
        pass

    def set_port(self, port): # real signature unknown; restored from __doc__
        """ set_port(self, port:int) -> GstRtsp.RTSPResult """
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

    abspath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    passwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RTSPUrl), '__module__': 'gi.repository.GstRtsp', '__gtype__': <GType GstRTSPUrl (93854382006448)>, '__dict__': <attribute '__dict__' of 'RTSPUrl' objects>, '__weakref__': <attribute '__weakref__' of 'RTSPUrl' objects>, '__doc__': None, 'transports': <property object at 0x7ff1b3249ae0>, 'family': <property object at 0x7ff1b3249bd0>, 'user': <property object at 0x7ff1b3249cc0>, 'passwd': <property object at 0x7ff1b3249db0>, 'host': <property object at 0x7ff1b3249ea0>, 'port': <property object at 0x7ff1b3249f90>, 'abspath': <property object at 0x7ff1b324a0e0>, 'query': <property object at 0x7ff1b324a1d0>, 'copy': gi.FunctionInfo(copy), 'decode_path_components': gi.FunctionInfo(decode_path_components), 'free': gi.FunctionInfo(free), 'get_port': gi.FunctionInfo(get_port), 'get_request_uri': gi.FunctionInfo(get_request_uri), 'set_port': gi.FunctionInfo(set_port), 'parse': gi.FunctionInfo(parse)})"
    __gtype__ = None # (!) real value is '<GType GstRTSPUrl (93854382006448)>'
    __info__ = StructInfo(RTSPUrl)


