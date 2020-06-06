# encoding: utf-8
# module gi.repository.GstBase
# from /usr/lib64/girepository-1.0/GstBase-1.0.typelib
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
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gst as __gi_repository_Gst
import gobject as __gobject


class BitWriter(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BitWriter()
    """
    def align_bytes(self, trailing_bit): # real signature unknown; restored from __doc__
        """ align_bytes(self, trailing_bit:int) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def free_and_get_buffer(self): # real signature unknown; restored from __doc__
        """ free_and_get_buffer(self) -> Gst.Buffer """
        pass

    def free_and_get_data(self): # real signature unknown; restored from __doc__
        """ free_and_get_data(self) -> list """
        return []

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> int """
        return 0

    def get_remaining(self): # real signature unknown; restored from __doc__
        """ get_remaining(self) -> int """
        return 0

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def put_bits_uint16(self, value, nbits): # real signature unknown; restored from __doc__
        """ put_bits_uint16(self, value:int, nbits:int) -> bool """
        return False

    def put_bits_uint32(self, value, nbits): # real signature unknown; restored from __doc__
        """ put_bits_uint32(self, value:int, nbits:int) -> bool """
        return False

    def put_bits_uint64(self, value, nbits): # real signature unknown; restored from __doc__
        """ put_bits_uint64(self, value:int, nbits:int) -> bool """
        return False

    def put_bits_uint8(self, value, nbits): # real signature unknown; restored from __doc__
        """ put_bits_uint8(self, value:int, nbits:int) -> bool """
        return False

    def put_bytes(self, data, nbytes): # real signature unknown; restored from __doc__
        """ put_bytes(self, data:int, nbytes:int) -> bool """
        return False

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def reset_and_get_buffer(self): # real signature unknown; restored from __doc__
        """ reset_and_get_buffer(self) -> Gst.Buffer """
        pass

    def reset_and_get_data(self): # real signature unknown; restored from __doc__
        """ reset_and_get_data(self) -> list """
        return []

    def set_pos(self, pos): # real signature unknown; restored from __doc__
        """ set_pos(self, pos:int) -> bool """
        return False

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

    auto_grow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bit_capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bit_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    owned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BitWriter), '__module__': 'gi.repository.GstBase', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BitWriter' objects>, '__weakref__': <attribute '__weakref__' of 'BitWriter' objects>, '__doc__': None, 'data': <property object at 0x7f9fb7bcb450>, 'bit_size': <property object at 0x7f9fb7bcb540>, 'bit_capacity': <property object at 0x7f9fb7bcb630>, 'auto_grow': <property object at 0x7f9fb7bcb720>, 'owned': <property object at 0x7f9fb7bcb810>, '_gst_reserved': <property object at 0x7f9fb7bcb900>, 'align_bytes': gi.FunctionInfo(align_bytes), 'free': gi.FunctionInfo(free), 'free_and_get_buffer': gi.FunctionInfo(free_and_get_buffer), 'free_and_get_data': gi.FunctionInfo(free_and_get_data), 'get_data': gi.FunctionInfo(get_data), 'get_remaining': gi.FunctionInfo(get_remaining), 'get_size': gi.FunctionInfo(get_size), 'put_bits_uint16': gi.FunctionInfo(put_bits_uint16), 'put_bits_uint32': gi.FunctionInfo(put_bits_uint32), 'put_bits_uint64': gi.FunctionInfo(put_bits_uint64), 'put_bits_uint8': gi.FunctionInfo(put_bits_uint8), 'put_bytes': gi.FunctionInfo(put_bytes), 'reset': gi.FunctionInfo(reset), 'reset_and_get_buffer': gi.FunctionInfo(reset_and_get_buffer), 'reset_and_get_data': gi.FunctionInfo(reset_and_get_data), 'set_pos': gi.FunctionInfo(set_pos)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BitWriter)


