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


class TerrestrialDeliverySystemDescriptor(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        TerrestrialDeliverySystemDescriptor()
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

    bandwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    code_rate_hp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    code_rate_lp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    constellation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    guard_interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hierarchy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mpe_fec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    other_frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_slicing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transmission_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TerrestrialDeliverySystemDescriptor), '__module__': 'gi.repository.GstMpegts', '__gtype__': <GType GstMpegtsTerrestrialDeliverySystemDescriptor (94624018754048)>, '__dict__': <attribute '__dict__' of 'TerrestrialDeliverySystemDescriptor' objects>, '__weakref__': <attribute '__weakref__' of 'TerrestrialDeliverySystemDescriptor' objects>, '__doc__': None, 'frequency': <property object at 0x7faa5f6ccb30>, 'bandwidth': <property object at 0x7faa5f6ccc20>, 'priority': <property object at 0x7faa5f6ccd10>, 'time_slicing': <property object at 0x7faa5f6cce00>, 'mpe_fec': <property object at 0x7faa5f6ccef0>, 'constellation': <property object at 0x7faa5f6cd040>, 'hierarchy': <property object at 0x7faa5f6cd130>, 'code_rate_hp': <property object at 0x7faa5f6cd220>, 'code_rate_lp': <property object at 0x7faa5f6cd310>, 'guard_interval': <property object at 0x7faa5f6cd400>, 'transmission_mode': <property object at 0x7faa5f6cd540>, 'other_frequency': <property object at 0x7faa5f6cd5e0>})"
    __gtype__ = None # (!) real value is '<GType GstMpegtsTerrestrialDeliverySystemDescriptor (94624018754048)>'
    __info__ = StructInfo(TerrestrialDeliverySystemDescriptor)


