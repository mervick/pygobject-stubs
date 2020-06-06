# encoding: utf-8
# module gi.repository.GData
# from /usr/lib64/girepository-1.0/GData-0.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class FreebaseTopicValue(__gi.Boxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def copy_value(self): # real signature unknown; restored from __doc__
        """ copy_value(self) -> gvalue:GObject.Value """
        pass

    def get_creator(self): # real signature unknown; restored from __doc__
        """ get_creator(self) -> str """
        return ""

    def get_double(self): # real signature unknown; restored from __doc__
        """ get_double(self) -> float """
        return 0.0

    def get_int(self): # real signature unknown; restored from __doc__
        """ get_int(self) -> int """
        return 0

    def get_language(self): # real signature unknown; restored from __doc__
        """ get_language(self) -> str """
        return ""

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GData.FreebaseTopicObject """
        pass

    def get_property(self): # real signature unknown; restored from __doc__
        """ get_property(self) -> str """
        return ""

    def get_string(self): # real signature unknown; restored from __doc__
        """ get_string(self) -> str """
        return ""

    def get_text(self): # real signature unknown; restored from __doc__
        """ get_text(self) -> str """
        return ""

    def get_timestamp(self): # real signature unknown; restored from __doc__
        """ get_timestamp(self) -> int """
        return 0

    def get_value_type(self): # real signature unknown; restored from __doc__
        """ get_value_type(self) -> GType """
        pass

    def is_image(self): # real signature unknown; restored from __doc__
        """ is_image(self) -> bool """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GData.FreebaseTopicValue """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FreebaseTopicValue), '__module__': 'gi.repository.GData', '__gtype__': <GType GDataFreebaseTopicValue (94233464593024)>, '__dict__': <attribute '__dict__' of 'FreebaseTopicValue' objects>, '__weakref__': <attribute '__weakref__' of 'FreebaseTopicValue' objects>, '__doc__': None, 'copy_value': gi.FunctionInfo(copy_value), 'get_creator': gi.FunctionInfo(get_creator), 'get_double': gi.FunctionInfo(get_double), 'get_int': gi.FunctionInfo(get_int), 'get_language': gi.FunctionInfo(get_language), 'get_object': gi.FunctionInfo(get_object), 'get_property': gi.FunctionInfo(get_property), 'get_string': gi.FunctionInfo(get_string), 'get_text': gi.FunctionInfo(get_text), 'get_timestamp': gi.FunctionInfo(get_timestamp), 'get_value_type': gi.FunctionInfo(get_value_type), 'is_image': gi.FunctionInfo(is_image), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GDataFreebaseTopicValue (94233464593024)>'
    __info__ = StructInfo(FreebaseTopicValue)


