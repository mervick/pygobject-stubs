# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Uri(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(scheme:str=None, userinfo:str=None, host:str=None, port:int, path:str=None, query:str=None, fragment:str=None) -> Gst.Uri
    """
    def append_path(self, relative_path): # real signature unknown; restored from __doc__
        """ append_path(self, relative_path:str) -> bool """
        return False

    def append_path_segment(self, path_segment): # real signature unknown; restored from __doc__
        """ append_path_segment(self, path_segment:str) -> bool """
        return False

    def construct(self, protocol, location): # real signature unknown; restored from __doc__
        """ construct(protocol:str, location:str) -> str """
        return ""

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, second): # real signature unknown; restored from __doc__
        """ equal(self, second:Gst.Uri) -> bool """
        return False

    def from_string(self, uri): # real signature unknown; restored from __doc__
        """ from_string(uri:str) -> Gst.Uri or None """
        pass

    def from_string_with_base(self, uri): # real signature unknown; restored from __doc__
        """ from_string_with_base(self, uri:str) -> Gst.Uri """
        pass

    def get_fragment(self): # real signature unknown; restored from __doc__
        """ get_fragment(self) -> str or None """
        return ""

    def get_host(self): # real signature unknown; restored from __doc__
        """ get_host(self) -> str or None """
        return ""

    def get_location(self, uri): # real signature unknown; restored from __doc__
        """ get_location(uri:str) -> str or None """
        return ""

    def get_media_fragment_table(self): # real signature unknown; restored from __doc__
        """ get_media_fragment_table(self) -> dict or None """
        return {}

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str or None """
        return ""

    def get_path_segments(self): # real signature unknown; restored from __doc__
        """ get_path_segments(self) -> list """
        return []

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str or None """
        return ""

    def get_port(self): # real signature unknown; restored from __doc__
        """ get_port(self) -> int """
        return 0

    def get_protocol(self, uri): # real signature unknown; restored from __doc__
        """ get_protocol(uri:str) -> str or None """
        return ""

    def get_query_keys(self): # real signature unknown; restored from __doc__
        """ get_query_keys(self) -> list """
        return []

    def get_query_string(self): # real signature unknown; restored from __doc__
        """ get_query_string(self) -> str or None """
        return ""

    def get_query_table(self): # real signature unknown; restored from __doc__
        """ get_query_table(self) -> dict or None """
        return {}

    def get_query_value(self, query_key): # real signature unknown; restored from __doc__
        """ get_query_value(self, query_key:str) -> str or None """
        return ""

    def get_scheme(self): # real signature unknown; restored from __doc__
        """ get_scheme(self) -> str or None """
        return ""

    def get_userinfo(self): # real signature unknown; restored from __doc__
        """ get_userinfo(self) -> str or None """
        return ""

    def has_protocol(self, uri, protocol): # real signature unknown; restored from __doc__
        """ has_protocol(uri:str, protocol:str) -> bool """
        return False

    def is_normalized(self): # real signature unknown; restored from __doc__
        """ is_normalized(self) -> bool """
        return False

    def is_valid(self, uri): # real signature unknown; restored from __doc__
        """ is_valid(uri:str) -> bool """
        return False

    def is_writable(self): # real signature unknown; restored from __doc__
        """ is_writable(self) -> bool """
        return False

    def join(self, ref_uri=None): # real signature unknown; restored from __doc__
        """ join(self, ref_uri:Gst.Uri=None) -> Gst.Uri or None """
        pass

    def join_strings(self, base_uri, ref_uri): # real signature unknown; restored from __doc__
        """ join_strings(base_uri:str, ref_uri:str) -> str """
        return ""

    def make_writable(self): # real signature unknown; restored from __doc__
        """ make_writable(self) -> Gst.Uri """
        pass

    def new(self, scheme=None, userinfo=None, host=None, port, path=None, query=None, fragment=None): # real signature unknown; restored from __doc__
        """ new(scheme:str=None, userinfo:str=None, host:str=None, port:int, path:str=None, query:str=None, fragment:str=None) -> Gst.Uri """
        pass

    def new_with_base(self, scheme=None, userinfo=None, host=None, port, path=None, query=None, fragment=None): # real signature unknown; restored from __doc__
        """ new_with_base(self, scheme:str=None, userinfo:str=None, host:str=None, port:int, path:str=None, query:str=None, fragment:str=None) -> Gst.Uri """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> bool """
        return False

    def protocol_is_supported(self, type, protocol): # real signature unknown; restored from __doc__
        """ protocol_is_supported(type:Gst.URIType, protocol:str) -> bool """
        return False

    def protocol_is_valid(self, protocol): # real signature unknown; restored from __doc__
        """ protocol_is_valid(protocol:str) -> bool """
        return False

    def query_has_key(self, query_key): # real signature unknown; restored from __doc__
        """ query_has_key(self, query_key:str) -> bool """
        return False

    def remove_query_key(self, query_key): # real signature unknown; restored from __doc__
        """ remove_query_key(self, query_key:str) -> bool """
        return False

    def set_fragment(self, fragment=None): # real signature unknown; restored from __doc__
        """ set_fragment(self, fragment:str=None) -> bool """
        return False

    def set_host(self, host): # real signature unknown; restored from __doc__
        """ set_host(self, host:str) -> bool """
        return False

    def set_path(self, path): # real signature unknown; restored from __doc__
        """ set_path(self, path:str) -> bool """
        return False

    def set_path_segments(self, path_segments=None): # real signature unknown; restored from __doc__
        """ set_path_segments(self, path_segments:list=None) -> bool """
        return False

    def set_path_string(self, path): # real signature unknown; restored from __doc__
        """ set_path_string(self, path:str) -> bool """
        return False

    def set_port(self, port): # real signature unknown; restored from __doc__
        """ set_port(self, port:int) -> bool """
        return False

    def set_query_string(self, query): # real signature unknown; restored from __doc__
        """ set_query_string(self, query:str) -> bool """
        return False

    def set_query_table(self, query_table=None): # real signature unknown; restored from __doc__
        """ set_query_table(self, query_table:dict=None) -> bool """
        return False

    def set_query_value(self, query_key, query_value=None): # real signature unknown; restored from __doc__
        """ set_query_value(self, query_key:str, query_value:str=None) -> bool """
        return False

    def set_scheme(self, scheme): # real signature unknown; restored from __doc__
        """ set_scheme(self, scheme:str) -> bool """
        return False

    def set_userinfo(self, userinfo): # real signature unknown; restored from __doc__
        """ set_userinfo(self, userinfo:str) -> bool """
        return False

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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
        """ new(scheme:str=None, userinfo:str=None, host:str=None, port:int, path:str=None, query:str=None, fragment:str=None) -> Gst.Uri """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Uri), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstUri (94058978111728)>, '__dict__': <attribute '__dict__' of 'Uri' objects>, '__weakref__': <attribute '__weakref__' of 'Uri' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'append_path': gi.FunctionInfo(append_path), 'append_path_segment': gi.FunctionInfo(append_path_segment), 'equal': gi.FunctionInfo(equal), 'from_string_with_base': gi.FunctionInfo(from_string_with_base), 'get_fragment': gi.FunctionInfo(get_fragment), 'get_host': gi.FunctionInfo(get_host), 'get_media_fragment_table': gi.FunctionInfo(get_media_fragment_table), 'get_path': gi.FunctionInfo(get_path), 'get_path_segments': gi.FunctionInfo(get_path_segments), 'get_path_string': gi.FunctionInfo(get_path_string), 'get_port': gi.FunctionInfo(get_port), 'get_query_keys': gi.FunctionInfo(get_query_keys), 'get_query_string': gi.FunctionInfo(get_query_string), 'get_query_table': gi.FunctionInfo(get_query_table), 'get_query_value': gi.FunctionInfo(get_query_value), 'get_scheme': gi.FunctionInfo(get_scheme), 'get_userinfo': gi.FunctionInfo(get_userinfo), 'is_normalized': gi.FunctionInfo(is_normalized), 'is_writable': gi.FunctionInfo(is_writable), 'join': gi.FunctionInfo(join), 'make_writable': gi.FunctionInfo(make_writable), 'new_with_base': gi.FunctionInfo(new_with_base), 'normalize': gi.FunctionInfo(normalize), 'query_has_key': gi.FunctionInfo(query_has_key), 'remove_query_key': gi.FunctionInfo(remove_query_key), 'set_fragment': gi.FunctionInfo(set_fragment), 'set_host': gi.FunctionInfo(set_host), 'set_path': gi.FunctionInfo(set_path), 'set_path_segments': gi.FunctionInfo(set_path_segments), 'set_path_string': gi.FunctionInfo(set_path_string), 'set_port': gi.FunctionInfo(set_port), 'set_query_string': gi.FunctionInfo(set_query_string), 'set_query_table': gi.FunctionInfo(set_query_table), 'set_query_value': gi.FunctionInfo(set_query_value), 'set_scheme': gi.FunctionInfo(set_scheme), 'set_userinfo': gi.FunctionInfo(set_userinfo), 'to_string': gi.FunctionInfo(to_string), 'construct': gi.FunctionInfo(construct), 'from_string': gi.FunctionInfo(from_string), 'get_location': gi.FunctionInfo(get_location), 'get_protocol': gi.FunctionInfo(get_protocol), 'has_protocol': gi.FunctionInfo(has_protocol), 'is_valid': gi.FunctionInfo(is_valid), 'join_strings': gi.FunctionInfo(join_strings), 'protocol_is_supported': gi.FunctionInfo(protocol_is_supported), 'protocol_is_valid': gi.FunctionInfo(protocol_is_valid), '__new__': <staticmethod object at 0x7f42605355e0>, '__init__': <function nothing at 0x7f4260937ee0>})"
    __gtype__ = None # (!) real value is '<GType GstUri (94058978111728)>'
    __info__ = StructInfo(Uri)


