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


class DVBLinkageDescriptor(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        DVBLinkageDescriptor()
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_event(self): # real signature unknown; restored from __doc__
        """ get_event(self) -> GstMpegts.DVBLinkageEvent """
        pass

    def get_extended_event(self): # real signature unknown; restored from __doc__
        """ get_extended_event(self) -> list """
        return []

    def get_mobile_hand_over(self): # real signature unknown; restored from __doc__
        """ get_mobile_hand_over(self) -> GstMpegts.DVBLinkageMobileHandOver """
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

    linkage_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linkage_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    original_network_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_data_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_data_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    service_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transport_stream_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DVBLinkageDescriptor), '__module__': 'gi.repository.GstMpegts', '__gtype__': <GType GstMpegtsDVBLinkageDescriptor (94624018569184)>, '__dict__': <attribute '__dict__' of 'DVBLinkageDescriptor' objects>, '__weakref__': <attribute '__weakref__' of 'DVBLinkageDescriptor' objects>, '__doc__': None, 'transport_stream_id': <property object at 0x7faa5f93ee50>, 'original_network_id': <property object at 0x7faa5f93ef40>, 'service_id': <property object at 0x7faa5f940040>, 'linkage_type': <property object at 0x7faa5f940130>, 'linkage_data': <property object at 0x7faa5f940220>, 'private_data_length': <property object at 0x7faa5f940360>, 'private_data_bytes': <property object at 0x7faa5f9404a0>, 'free': gi.FunctionInfo(free), 'get_event': gi.FunctionInfo(get_event), 'get_extended_event': gi.FunctionInfo(get_extended_event), 'get_mobile_hand_over': gi.FunctionInfo(get_mobile_hand_over)})"
    __gtype__ = None # (!) real value is '<GType GstMpegtsDVBLinkageDescriptor (94624018569184)>'
    __info__ = StructInfo(DVBLinkageDescriptor)


