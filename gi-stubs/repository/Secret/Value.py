# encoding: utf-8
# module gi.repository.Secret
# from /usr/lib64/girepository-1.0/Secret-1.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gobject as __gobject


class Value(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(secret:str, length:int, content_type:str) -> Secret.Value
        new_full(secret:str, length:int, content_type:str, destroy:GLib.DestroyNotify) -> Secret.Value
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get(self): # real signature unknown; restored from __doc__
        """ get(self) -> list, length:int """
        return []

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> str """
        return ""

    def get_text(self): # real signature unknown; restored from __doc__
        """ get_text(self) -> str or None """
        return ""

    def new(self, secret, length, content_type): # real signature unknown; restored from __doc__
        """ new(secret:str, length:int, content_type:str) -> Secret.Value """
        pass

    def new_full(self, secret, length, content_type, destroy): # real signature unknown; restored from __doc__
        """ new_full(secret:str, length:int, content_type:str, destroy:GLib.DestroyNotify) -> Secret.Value """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Secret.Value """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def unref_to_password(self, length): # real signature unknown; restored from __doc__
        """ unref_to_password(self, length:int) -> str """
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
        """ new(secret:str, length:int, content_type:str) -> Secret.Value """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Value), '__module__': 'gi.repository.Secret', '__gtype__': <GType SecretValue (93972239851360)>, '__dict__': <attribute '__dict__' of 'Value' objects>, '__weakref__': <attribute '__weakref__' of 'Value' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_full': gi.FunctionInfo(new_full), 'get': gi.FunctionInfo(get), 'get_content_type': gi.FunctionInfo(get_content_type), 'get_text': gi.FunctionInfo(get_text), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), 'unref_to_password': gi.FunctionInfo(unref_to_password), '__new__': <staticmethod object at 0x7fa0c5986070>, '__init__': <function nothing at 0x7fa0c5bb5ee0>})"
    __gtype__ = None # (!) real value is '<GType SecretValue (93972239851360)>'
    __info__ = StructInfo(Value)


