# encoding: utf-8
# module gi.repository.EBookContacts
# from /usr/lib64/girepository-1.0/EBookContacts-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gobject as __gobject


class ContactPhoto(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        ContactPhoto()
        new() -> EBookContacts.ContactPhoto
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EBookContacts.ContactPhoto """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_inlined(self): # real signature unknown; restored from __doc__
        """ get_inlined(self) -> list or None, len:int """
        return []

    def get_mime_type(self): # real signature unknown; restored from __doc__
        """ get_mime_type(self) -> str or None """
        return ""

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str or None """
        return ""

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> EBookContacts.ContactPhoto """
        pass

    def set_inlined(self, data): # real signature unknown; restored from __doc__
        """ set_inlined(self, data:list) """
        pass

    def set_mime_type(self, mime_type): # real signature unknown; restored from __doc__
        """ set_mime_type(self, mime_type:str) """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:str) """
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
        """ new() -> EBookContacts.ContactPhoto """
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

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ContactPhoto), '__module__': 'gi.repository.EBookContacts', '__gtype__': <GType EContactPhoto (94769385598048)>, '__dict__': <attribute '__dict__' of 'ContactPhoto' objects>, '__weakref__': <attribute '__weakref__' of 'ContactPhoto' objects>, '__doc__': None, 'type': <property object at 0x7f714bb3e4f0>, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_inlined': gi.FunctionInfo(get_inlined), 'get_mime_type': gi.FunctionInfo(get_mime_type), 'get_uri': gi.FunctionInfo(get_uri), 'set_inlined': gi.FunctionInfo(set_inlined), 'set_mime_type': gi.FunctionInfo(set_mime_type), 'set_uri': gi.FunctionInfo(set_uri), '__new__': <staticmethod object at 0x7f714bb2fee0>, '__init__': <function nothing at 0x7f714bde4ee0>})"
    __gtype__ = None # (!) real value is '<GType EContactPhoto (94769385598048)>'
    __info__ = StructInfo(ContactPhoto)


