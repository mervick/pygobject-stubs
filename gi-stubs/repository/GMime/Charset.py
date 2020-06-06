# encoding: utf-8
# module gi.repository.GMime
# from /usr/lib64/girepository-1.0/GMime-3.0.typelib
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
import gobject as __gobject


class Charset(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Charset()
    """
    def best(self, inbuf, inlen): # real signature unknown; restored from __doc__
        """ best(inbuf:str, inlen:int) -> str or None """
        return ""

    def best_name(self): # real signature unknown; restored from __doc__
        """ best_name(self) -> str or None """
        return ""

    def canon_name(self, charset): # real signature unknown; restored from __doc__
        """ canon_name(charset:str) -> str """
        return ""

    def can_encode(self, charset, text, len): # real signature unknown; restored from __doc__
        """ can_encode(self, charset:str, text:str, len:int) -> bool """
        return False

    def iconv_name(self, charset): # real signature unknown; restored from __doc__
        """ iconv_name(charset:str) -> str """
        return ""

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def iso_to_windows(self, isocharset): # real signature unknown; restored from __doc__
        """ iso_to_windows(isocharset:str) -> str """
        return ""

    def language(self, charset): # real signature unknown; restored from __doc__
        """ language(charset:str) -> str or None """
        return ""

    def locale_name(self): # real signature unknown; restored from __doc__
        """ locale_name() -> str """
        return ""

    def map_init(self): # real signature unknown; restored from __doc__
        """ map_init() """
        pass

    def map_shutdown(self): # real signature unknown; restored from __doc__
        """ map_shutdown() """
        pass

    def name(self, charset): # real signature unknown; restored from __doc__
        """ name(charset:str) -> str """
        return ""

    def step(self, inbuf, inlen): # real signature unknown; restored from __doc__
        """ step(self, inbuf:str, inlen:int) """
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

    level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Charset), '__module__': 'gi.repository.GMime', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Charset' objects>, '__weakref__': <attribute '__weakref__' of 'Charset' objects>, '__doc__': None, 'mask': <property object at 0x7fc9708ca590>, 'level': <property object at 0x7fc9708ca680>, 'best_name': gi.FunctionInfo(best_name), 'can_encode': gi.FunctionInfo(can_encode), 'init': gi.FunctionInfo(init), 'step': gi.FunctionInfo(step), 'best': gi.FunctionInfo(best), 'canon_name': gi.FunctionInfo(canon_name), 'iconv_name': gi.FunctionInfo(iconv_name), 'iso_to_windows': gi.FunctionInfo(iso_to_windows), 'language': gi.FunctionInfo(language), 'locale_name': gi.FunctionInfo(locale_name), 'map_init': gi.FunctionInfo(map_init), 'map_shutdown': gi.FunctionInfo(map_shutdown), 'name': gi.FunctionInfo(name)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Charset)


