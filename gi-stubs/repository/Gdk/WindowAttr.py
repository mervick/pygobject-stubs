# encoding: utf-8
# module gi.repository.Gdk
# from /usr/lib64/girepository-1.0/Gdk-3.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class WindowAttr(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        WindowAttr()
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

    cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    event_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    override_redirect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    visual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wclass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wmclass_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wmclass_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WindowAttr), '__module__': 'gi.repository.Gdk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'WindowAttr' objects>, '__weakref__': <attribute '__weakref__' of 'WindowAttr' objects>, '__doc__': None, 'title': <property object at 0x7f1e11c34bd0>, 'event_mask': <property object at 0x7f1e11c34cc0>, 'x': <property object at 0x7f1e11c34db0>, 'y': <property object at 0x7f1e11c34ea0>, 'width': <property object at 0x7f1e11c34f90>, 'height': <property object at 0x7f1e11c370e0>, 'wclass': <property object at 0x7f1e11c371d0>, 'visual': <property object at 0x7f1e11c372c0>, 'window_type': <property object at 0x7f1e11c373b0>, 'cursor': <property object at 0x7f1e11c374a0>, 'wmclass_name': <property object at 0x7f1e11c37590>, 'wmclass_class': <property object at 0x7f1e11c37680>, 'override_redirect': <property object at 0x7f1e11c377c0>, 'type_hint': <property object at 0x7f1e11c378b0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(WindowAttr)


