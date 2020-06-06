# encoding: utf-8
# module gi.repository.WebKit2
# from /usr/lib64/girepository-1.0/WebKit2-4.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class NavigationAction(__gi.Boxed):
    # no doc
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> WebKit2.NavigationAction """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_modifiers(self): # real signature unknown; restored from __doc__
        """ get_modifiers(self) -> int """
        return 0

    def get_mouse_button(self): # real signature unknown; restored from __doc__
        """ get_mouse_button(self) -> int """
        return 0

    def get_navigation_type(self): # real signature unknown; restored from __doc__
        """ get_navigation_type(self) -> WebKit2.NavigationType """
        pass

    def get_request(self): # real signature unknown; restored from __doc__
        """ get_request(self) -> WebKit2.URIRequest """
        pass

    def is_redirect(self): # real signature unknown; restored from __doc__
        """ is_redirect(self) -> bool """
        return False

    def is_user_gesture(self): # real signature unknown; restored from __doc__
        """ is_user_gesture(self) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NavigationAction), '__module__': 'gi.repository.WebKit2', '__gtype__': <GType WebKitNavigationAction (94869774788464)>, '__dict__': <attribute '__dict__' of 'NavigationAction' objects>, '__weakref__': <attribute '__weakref__' of 'NavigationAction' objects>, '__doc__': None, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_modifiers': gi.FunctionInfo(get_modifiers), 'get_mouse_button': gi.FunctionInfo(get_mouse_button), 'get_navigation_type': gi.FunctionInfo(get_navigation_type), 'get_request': gi.FunctionInfo(get_request), 'is_redirect': gi.FunctionInfo(is_redirect), 'is_user_gesture': gi.FunctionInfo(is_user_gesture)})"
    __gtype__ = None # (!) real value is '<GType WebKitNavigationAction (94869774788464)>'
    __info__ = StructInfo(NavigationAction)


