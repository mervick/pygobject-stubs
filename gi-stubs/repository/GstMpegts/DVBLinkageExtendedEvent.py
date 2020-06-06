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


class DVBLinkageExtendedEvent(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        DVBLinkageExtendedEvent()
    """
    def copy(self, *args, **kwargs): # real signature unknown
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

    event_simulcast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    link_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    original_network_id_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    service_id_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_event_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_id_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_listed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_original_network_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_service_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_transport_stream_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_defined_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DVBLinkageExtendedEvent), '__module__': 'gi.repository.GstMpegts', '__gtype__': <GType GstMpegtsDVBLinkageExtendedEvent (94624018569792)>, '__dict__': <attribute '__dict__' of 'DVBLinkageExtendedEvent' objects>, '__weakref__': <attribute '__weakref__' of 'DVBLinkageExtendedEvent' objects>, '__doc__': None, 'target_event_id': <property object at 0x7faa5f940ae0>, 'target_listed': <property object at 0x7faa5f940bd0>, 'event_simulcast': <property object at 0x7faa5f940cc0>, 'link_type': <property object at 0x7faa5f940db0>, 'target_id_type': <property object at 0x7faa5f940ea0>, 'original_network_id_flag': <property object at 0x7faa5f942040>, 'service_id_flag': <property object at 0x7faa5f942130>, 'user_defined_id': <property object at 0x7faa5f942220>, 'target_transport_stream_id': <property object at 0x7faa5f942360>, 'target_original_network_id': <property object at 0x7faa5f9424a0>, 'target_service_id': <property object at 0x7faa5f9425e0>})"
    __gtype__ = None # (!) real value is '<GType GstMpegtsDVBLinkageExtendedEvent (94624018569792)>'
    __info__ = StructInfo(DVBLinkageExtendedEvent)


