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


class SatelliteDeliverySystemDescriptor(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        SatelliteDeliverySystemDescriptor()
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

    fec_inner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modulation_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modulation_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orbital_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    polarization = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    roll_off = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    symbol_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    west_east = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SatelliteDeliverySystemDescriptor), '__module__': 'gi.repository.GstMpegts', '__gtype__': <GType GstMpegtsSatelliteDeliverySystemDescriptor (94624018697264)>, '__dict__': <attribute '__dict__' of 'SatelliteDeliverySystemDescriptor' objects>, '__weakref__': <attribute '__weakref__' of 'SatelliteDeliverySystemDescriptor' objects>, '__doc__': None, 'frequency': <property object at 0x7faa5f6be0e0>, 'orbital_position': <property object at 0x7faa5f6be220>, 'west_east': <property object at 0x7faa5f6be310>, 'polarization': <property object at 0x7faa5f6be400>, 'roll_off': <property object at 0x7faa5f6be4f0>, 'modulation_system': <property object at 0x7faa5f6be630>, 'modulation_type': <property object at 0x7faa5f6be720>, 'symbol_rate': <property object at 0x7faa5f6be810>, 'fec_inner': <property object at 0x7faa5f6be900>})"
    __gtype__ = None # (!) real value is '<GType GstMpegtsSatelliteDeliverySystemDescriptor (94624018697264)>'
    __info__ = StructInfo(SatelliteDeliverySystemDescriptor)


