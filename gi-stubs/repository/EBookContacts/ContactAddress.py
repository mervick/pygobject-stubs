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


class ContactAddress(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        ContactAddress()
        new() -> EBookContacts.ContactAddress
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> EBookContacts.ContactAddress """
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
        """ new() -> EBookContacts.ContactAddress """
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

    address_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    country = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    locality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    po = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    region = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    street = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ContactAddress), '__module__': 'gi.repository.EBookContacts', '__gtype__': <GType EContactAddress (94769385553696)>, '__dict__': <attribute '__dict__' of 'ContactAddress' objects>, '__weakref__': <attribute '__weakref__' of 'ContactAddress' objects>, '__doc__': None, 'address_format': <property object at 0x7f714bb37a90>, 'po': <property object at 0x7f714bb37b80>, 'ext': <property object at 0x7f714bb37c70>, 'street': <property object at 0x7f714bb37d60>, 'locality': <property object at 0x7f714bb37e50>, 'region': <property object at 0x7f714bb37f40>, 'code': <property object at 0x7f714bb39090>, 'country': <property object at 0x7f714bb39180>, 'new': gi.FunctionInfo(new), 'free': gi.FunctionInfo(free), '__new__': <staticmethod object at 0x7f714bb2f760>, '__init__': <function nothing at 0x7f714bde4ee0>})"
    __gtype__ = None # (!) real value is '<GType EContactAddress (94769385553696)>'
    __info__ = StructInfo(ContactAddress)


