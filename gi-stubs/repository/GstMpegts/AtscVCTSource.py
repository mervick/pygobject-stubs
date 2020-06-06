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


class AtscVCTSource(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        AtscVCTSource()
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

    access_controlled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    carrier_frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    channel_TSID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    descriptors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ETM_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hide_guide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    major_channel_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minor_channel_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modulation_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    out_of_band = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path_select = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    program_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    service_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    short_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AtscVCTSource), '__module__': 'gi.repository.GstMpegts', '__gtype__': <GType GstMpegtsAtscVCTSource (94624018019840)>, '__dict__': <attribute '__dict__' of 'AtscVCTSource' objects>, '__weakref__': <attribute '__weakref__' of 'AtscVCTSource' objects>, '__doc__': None, 'short_name': <property object at 0x7faa5f931e50>, 'major_channel_number': <property object at 0x7faa5f931f90>, 'minor_channel_number': <property object at 0x7faa5f932130>, 'modulation_mode': <property object at 0x7faa5f932220>, 'carrier_frequency': <property object at 0x7faa5f932360>, 'channel_TSID': <property object at 0x7faa5f932450>, 'program_number': <property object at 0x7faa5f932540>, 'ETM_location': <property object at 0x7faa5f932630>, 'access_controlled': <property object at 0x7faa5f932770>, 'hidden': <property object at 0x7faa5f932860>, 'path_select': <property object at 0x7faa5f932950>, 'out_of_band': <property object at 0x7faa5f932a40>, 'hide_guide': <property object at 0x7faa5f932b30>, 'service_type': <property object at 0x7faa5f932c20>, 'source_id': <property object at 0x7faa5f932d10>, 'descriptors': <property object at 0x7faa5f932e00>})"
    __gtype__ = None # (!) real value is '<GType GstMpegtsAtscVCTSource (94624018019840)>'
    __info__ = StructInfo(AtscVCTSource)


