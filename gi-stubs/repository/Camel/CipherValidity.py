# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


class CipherValidity(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        CipherValidity()
        new() -> Camel.CipherValidity
    """
    def add_certinfo(self, mode, name, email): # real signature unknown; restored from __doc__
        """ add_certinfo(self, mode:Camel.CipherValidityMode, name:str, email:str) -> int """
        return 0

    def add_certinfo_ex(self, mode, name, email, cert_data=None, cert_data_clone=None): # real signature unknown; restored from __doc__
        """ add_certinfo_ex(self, mode:Camel.CipherValidityMode, name:str, email:str, cert_data=None, cert_data_clone:Camel.CipherCloneFunc=None) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> Camel.CipherValidity """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def envelope(self, valid): # real signature unknown; restored from __doc__
        """ envelope(self, valid:Camel.CipherValidity) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_certinfo_property(self, mode, info_index, name): # real signature unknown; restored from __doc__
        """ get_certinfo_property(self, mode:Camel.CipherValidityMode, info_index:int, name:str) """
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_valid(self): # real signature unknown; restored from __doc__
        """ get_valid(self) -> bool """
        return False

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Camel.CipherValidity """
        pass

    def set_certinfo_property(self, mode, info_index, name, value=None, value_clone=None): # real signature unknown; restored from __doc__
        """ set_certinfo_property(self, mode:Camel.CipherValidityMode, info_index:int, name:str, value=None, value_clone:Camel.CipherCloneFunc=None) """
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_valid(self, valid): # real signature unknown; restored from __doc__
        """ set_valid(self, valid:bool) """
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
        """ new() -> Camel.CipherValidity """
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

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encrypt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CipherValidity), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelCipherValidity (94124523573424)>, '__dict__': <attribute '__dict__' of 'CipherValidity' objects>, '__weakref__': <attribute '__weakref__' of 'CipherValidity' objects>, '__doc__': None, 'children': <property object at 0x7f7b37536e00>, 'sign': <property object at 0x7f7b37536ef0>, 'encrypt': <property object at 0x7f7b34fac040>, 'new': gi.FunctionInfo(new), 'add_certinfo': gi.FunctionInfo(add_certinfo), 'add_certinfo_ex': gi.FunctionInfo(add_certinfo_ex), 'clear': gi.FunctionInfo(clear), 'clone': gi.FunctionInfo(clone), 'envelope': gi.FunctionInfo(envelope), 'free': gi.FunctionInfo(free), 'get_certinfo_property': gi.FunctionInfo(get_certinfo_property), 'get_description': gi.FunctionInfo(get_description), 'get_valid': gi.FunctionInfo(get_valid), 'init': gi.FunctionInfo(init), 'set_certinfo_property': gi.FunctionInfo(set_certinfo_property), 'set_description': gi.FunctionInfo(set_description), 'set_valid': gi.FunctionInfo(set_valid), '__new__': <staticmethod object at 0x7f7b375353a0>, '__init__': <function nothing at 0x7f7b37797ee0>})"
    __gtype__ = None # (!) real value is '<GType CamelCipherValidity (94124523573424)>'
    __info__ = StructInfo(CipherValidity)


