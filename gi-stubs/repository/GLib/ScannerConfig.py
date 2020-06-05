# encoding: utf-8
# module gi.repository.GLib
# from /usr/lib64/girepository-1.0/GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # /usr/lib64/python3.8/site-packages/gi/_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gobject as __gobject


class ScannerConfig(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ScannerConfig()
    """
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

    case_sensitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    char_2_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cpair_comment_single = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cset_identifier_first = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cset_identifier_nth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cset_skip_characters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    identifier_2_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    int_2_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numbers_2_int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_binary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_comment_multi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_hex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_hex_dollar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_identifier_1char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_identifier_NULL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_octal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_string_dq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_string_sq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_symbols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scope_0_fallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skip_comment_multi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skip_comment_single = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    store_int64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    symbol_2_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ScannerConfig), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ScannerConfig' objects>, '__weakref__': <attribute '__weakref__' of 'ScannerConfig' objects>, '__doc__': None, 'cset_skip_characters': <property object at 0x7f1d2b902c20>, 'cset_identifier_first': <property object at 0x7f1d2b902d60>, 'cset_identifier_nth': <property object at 0x7f1d2b902ea0>, 'cpair_comment_single': <property object at 0x7f1d2b904040>, 'case_sensitive': <property object at 0x7f1d2b904130>, 'skip_comment_multi': <property object at 0x7f1d2b904270>, 'skip_comment_single': <property object at 0x7f1d2b9043b0>, 'scan_comment_multi': <property object at 0x7f1d2b9044f0>, 'scan_identifier': <property object at 0x7f1d2b9045e0>, 'scan_identifier_1char': <property object at 0x7f1d2b904720>, 'scan_identifier_NULL': <property object at 0x7f1d2b904860>, 'scan_symbols': <property object at 0x7f1d2b904950>, 'scan_binary': <property object at 0x7f1d2b904a40>, 'scan_octal': <property object at 0x7f1d2b904b30>, 'scan_float': <property object at 0x7f1d2b904c20>, 'scan_hex': <property object at 0x7f1d2b904d10>, 'scan_hex_dollar': <property object at 0x7f1d2b904e00>, 'scan_string_sq': <property object at 0x7f1d2b904ef0>, 'scan_string_dq': <property object at 0x7f1d2b905040>, 'numbers_2_int': <property object at 0x7f1d2b905130>, 'int_2_float': <property object at 0x7f1d2b905220>, 'identifier_2_string': <property object at 0x7f1d2b905360>, 'char_2_token': <property object at 0x7f1d2b905450>, 'symbol_2_token': <property object at 0x7f1d2b905540>, 'scope_0_fallback': <property object at 0x7f1d2b905680>, 'store_int64': <property object at 0x7f1d2b905770>, 'padding_dummy': <property object at 0x7f1d2b905860>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ScannerConfig)


