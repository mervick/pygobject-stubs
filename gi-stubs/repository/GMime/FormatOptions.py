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


class FormatOptions(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> GMime.FormatOptions
    """
    def add_hidden_header(self, header): # real signature unknown; restored from __doc__
        """ add_hidden_header(self, header:str) """
        pass

    def clear_hidden_headers(self): # real signature unknown; restored from __doc__
        """ clear_hidden_headers(self) """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> GMime.FormatOptions """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def create_newline_filter(self, ensure_newline): # real signature unknown; restored from __doc__
        """ create_newline_filter(self, ensure_newline:bool) -> GMime.Filter """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> GMime.FormatOptions """
        pass

    def get_newline(self): # real signature unknown; restored from __doc__
        """ get_newline(self) -> str """
        return ""

    def get_newline_format(self): # real signature unknown; restored from __doc__
        """ get_newline_format(self) -> GMime.NewLineFormat """
        pass

    def get_param_encoding_method(self): # real signature unknown; restored from __doc__
        """ get_param_encoding_method(self) -> GMime.ParamEncodingMethod """
        pass

    def is_hidden_header(self, header): # real signature unknown; restored from __doc__
        """ is_hidden_header(self, header:str) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GMime.FormatOptions """
        pass

    def remove_hidden_header(self, header): # real signature unknown; restored from __doc__
        """ remove_hidden_header(self, header:str) """
        pass

    def set_newline_format(self, newline): # real signature unknown; restored from __doc__
        """ set_newline_format(self, newline:GMime.NewLineFormat) """
        pass

    def set_param_encoding_method(self, method): # real signature unknown; restored from __doc__
        """ set_param_encoding_method(self, method:GMime.ParamEncodingMethod) """
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> GMime.FormatOptions """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FormatOptions), '__module__': 'gi.repository.GMime', '__gtype__': <GType GMimeFormatOptions (94235496064912)>, '__dict__': <attribute '__dict__' of 'FormatOptions' objects>, '__weakref__': <attribute '__weakref__' of 'FormatOptions' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'add_hidden_header': gi.FunctionInfo(add_hidden_header), 'clear_hidden_headers': gi.FunctionInfo(clear_hidden_headers), 'clone': gi.FunctionInfo(clone), 'create_newline_filter': gi.FunctionInfo(create_newline_filter), 'free': gi.FunctionInfo(free), 'get_newline': gi.FunctionInfo(get_newline), 'get_newline_format': gi.FunctionInfo(get_newline_format), 'get_param_encoding_method': gi.FunctionInfo(get_param_encoding_method), 'is_hidden_header': gi.FunctionInfo(is_hidden_header), 'remove_hidden_header': gi.FunctionInfo(remove_hidden_header), 'set_newline_format': gi.FunctionInfo(set_newline_format), 'set_param_encoding_method': gi.FunctionInfo(set_param_encoding_method), 'get_default': gi.FunctionInfo(get_default), '__new__': <staticmethod object at 0x7fc97072e850>, '__init__': <function nothing at 0x7fc970afcee0>})"
    __gtype__ = None # (!) real value is '<GType GMimeFormatOptions (94235496064912)>'
    __info__ = StructInfo(FormatOptions)


