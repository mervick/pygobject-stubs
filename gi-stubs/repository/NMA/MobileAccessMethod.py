# encoding: utf-8
# module gi.repository.NMA
# from /usr/lib64/girepository-1.0/NMA-1.0.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class MobileAccessMethod(__gi.Boxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_3gpp_apn(self): # real signature unknown; restored from __doc__
        """ get_3gpp_apn(self) -> str """
        return ""

    def get_dns(self): # real signature unknown; restored from __doc__
        """ get_dns(self) -> list """
        return []

    def get_family(self): # real signature unknown; restored from __doc__
        """ get_family(self) -> NMA.MobileFamily """
        pass

    def get_gateway(self): # real signature unknown; restored from __doc__
        """ get_gateway(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_password(self): # real signature unknown; restored from __doc__
        """ get_password(self) -> str """
        return ""

    def get_username(self): # real signature unknown; restored from __doc__
        """ get_username(self) -> str """
        return ""

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> NMA.MobileAccessMethod """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MobileAccessMethod), '__module__': 'gi.repository.NMA', '__gtype__': <GType NMAMobileAccessMethod (94779697273616)>, '__dict__': <attribute '__dict__' of 'MobileAccessMethod' objects>, '__weakref__': <attribute '__weakref__' of 'MobileAccessMethod' objects>, '__doc__': None, 'get_3gpp_apn': gi.FunctionInfo(get_3gpp_apn), 'get_dns': gi.FunctionInfo(get_dns), 'get_family': gi.FunctionInfo(get_family), 'get_gateway': gi.FunctionInfo(get_gateway), 'get_name': gi.FunctionInfo(get_name), 'get_password': gi.FunctionInfo(get_password), 'get_username': gi.FunctionInfo(get_username), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType NMAMobileAccessMethod (94779697273616)>'
    __info__ = StructInfo(MobileAccessMethod)


