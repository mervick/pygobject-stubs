# encoding: utf-8
# module gi.repository.Soup
# from /usr/lib64/girepository-1.0/Soup-2.4.typelib
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


class MessageHeaders(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(type:Soup.MessageHeadersType) -> Soup.MessageHeaders
    """
    def append(self, name, value): # real signature unknown; restored from __doc__
        """ append(self, name:str, value:str) """
        pass

    def clean_connection_headers(self): # real signature unknown; restored from __doc__
        """ clean_connection_headers(self) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:Soup.MessageHeadersForeachFunc, user_data=None) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def free_ranges(self, ranges): # real signature unknown; restored from __doc__
        """ free_ranges(self, ranges:Soup.Range) """
        pass

    def get(self, name): # real signature unknown; restored from __doc__
        """ get(self, name:str) -> str or None """
        return ""

    def get_content_disposition(self): # real signature unknown; restored from __doc__
        """ get_content_disposition(self) -> bool, disposition:str, params:dict """
        return False

    def get_content_length(self): # real signature unknown; restored from __doc__
        """ get_content_length(self) -> int """
        return 0

    def get_content_range(self): # real signature unknown; restored from __doc__
        """ get_content_range(self) -> bool, start:int, end:int, total_length:int """
        return False

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> str or None, params:dict """
        return ""

    def get_encoding(self): # real signature unknown; restored from __doc__
        """ get_encoding(self) -> Soup.Encoding """
        pass

    def get_expectations(self): # real signature unknown; restored from __doc__
        """ get_expectations(self) -> Soup.Expectation """
        pass

    def get_headers_type(self): # real signature unknown; restored from __doc__
        """ get_headers_type(self) -> Soup.MessageHeadersType """
        pass

    def get_list(self, name): # real signature unknown; restored from __doc__
        """ get_list(self, name:str) -> str or None """
        return ""

    def get_one(self, name): # real signature unknown; restored from __doc__
        """ get_one(self, name:str) -> str or None """
        return ""

    def get_ranges(self, total_length): # real signature unknown; restored from __doc__
        """ get_ranges(self, total_length:int) -> bool, ranges:list """
        return False

    def header_contains(self, name, token): # real signature unknown; restored from __doc__
        """ header_contains(self, name:str, token:str) -> bool """
        return False

    def header_equals(self, name, value): # real signature unknown; restored from __doc__
        """ header_equals(self, name:str, value:str) -> bool """
        return False

    def new(self, type): # real signature unknown; restored from __doc__
        """ new(type:Soup.MessageHeadersType) -> Soup.MessageHeaders """
        pass

    def remove(self, name): # real signature unknown; restored from __doc__
        """ remove(self, name:str) """
        pass

    def replace(self, name, value): # real signature unknown; restored from __doc__
        """ replace(self, name:str, value:str) """
        pass

    def set_content_disposition(self, disposition, params=None): # real signature unknown; restored from __doc__
        """ set_content_disposition(self, disposition:str, params:dict=None) """
        pass

    def set_content_length(self, content_length): # real signature unknown; restored from __doc__
        """ set_content_length(self, content_length:int) """
        pass

    def set_content_range(self, start, end, total_length): # real signature unknown; restored from __doc__
        """ set_content_range(self, start:int, end:int, total_length:int) """
        pass

    def set_content_type(self, content_type, params=None): # real signature unknown; restored from __doc__
        """ set_content_type(self, content_type:str, params:dict=None) """
        pass

    def set_encoding(self, encoding): # real signature unknown; restored from __doc__
        """ set_encoding(self, encoding:Soup.Encoding) """
        pass

    def set_expectations(self, expectations): # real signature unknown; restored from __doc__
        """ set_expectations(self, expectations:Soup.Expectation) """
        pass

    def set_range(self, start, end): # real signature unknown; restored from __doc__
        """ set_range(self, start:int, end:int) """
        pass

    def set_ranges(self, ranges, length): # real signature unknown; restored from __doc__
        """ set_ranges(self, ranges:Soup.Range, length:int) """
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
        """ new(type:Soup.MessageHeadersType) -> Soup.MessageHeaders """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MessageHeaders), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupMessageHeaders (94750594805168)>, '__dict__': <attribute '__dict__' of 'MessageHeaders' objects>, '__weakref__': <attribute '__weakref__' of 'MessageHeaders' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'append': gi.FunctionInfo(append), 'clean_connection_headers': gi.FunctionInfo(clean_connection_headers), 'clear': gi.FunctionInfo(clear), 'foreach': gi.FunctionInfo(foreach), 'free': gi.FunctionInfo(free), 'free_ranges': gi.FunctionInfo(free_ranges), 'get': gi.FunctionInfo(get), 'get_content_disposition': gi.FunctionInfo(get_content_disposition), 'get_content_length': gi.FunctionInfo(get_content_length), 'get_content_range': gi.FunctionInfo(get_content_range), 'get_content_type': gi.FunctionInfo(get_content_type), 'get_encoding': gi.FunctionInfo(get_encoding), 'get_expectations': gi.FunctionInfo(get_expectations), 'get_headers_type': gi.FunctionInfo(get_headers_type), 'get_list': gi.FunctionInfo(get_list), 'get_one': gi.FunctionInfo(get_one), 'get_ranges': gi.FunctionInfo(get_ranges), 'header_contains': gi.FunctionInfo(header_contains), 'header_equals': gi.FunctionInfo(header_equals), 'remove': gi.FunctionInfo(remove), 'replace': gi.FunctionInfo(replace), 'set_content_disposition': gi.FunctionInfo(set_content_disposition), 'set_content_length': gi.FunctionInfo(set_content_length), 'set_content_range': gi.FunctionInfo(set_content_range), 'set_content_type': gi.FunctionInfo(set_content_type), 'set_encoding': gi.FunctionInfo(set_encoding), 'set_expectations': gi.FunctionInfo(set_expectations), 'set_range': gi.FunctionInfo(set_range), 'set_ranges': gi.FunctionInfo(set_ranges), '__new__': <staticmethod object at 0x7f8e47ee31c0>, '__init__': <function nothing at 0x7f8e4884dee0>})"
    __gtype__ = None # (!) real value is '<GType SoupMessageHeaders (94750594805168)>'
    __info__ = StructInfo(MessageHeaders)


