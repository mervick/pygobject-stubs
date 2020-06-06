# encoding: utf-8
# module gi.repository.Gladeui
# from /usr/lib64/girepository-1.0/Gladeui-2.0.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class WidgetActionDef(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        WidgetActionDef()
        new(path:str) -> Gladeui.WidgetActionDef
    """
    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> Gladeui.WidgetActionDef """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def new(self, path): # real signature unknown; restored from __doc__
        """ new(path:str) -> Gladeui.WidgetActionDef """
        pass

    def set_important(self, important): # real signature unknown; restored from __doc__
        """ set_important(self, important:bool) """
        pass

    def set_label(self, label): # real signature unknown; restored from __doc__
        """ set_label(self, label:str) """
        pass

    def set_stock(self, stock): # real signature unknown; restored from __doc__
        """ set_stock(self, stock:str) """
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

    actions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    important = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WidgetActionDef), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType GladeWidgetActionDef (94653531291056)>, '__dict__': <attribute '__dict__' of 'WidgetActionDef' objects>, '__weakref__': <attribute '__weakref__' of 'WidgetActionDef' objects>, '__doc__': None, 'id': <property object at 0x7f1341772ef0>, 'path': <property object at 0x7f1341773040>, 'label': <property object at 0x7f1341773130>, 'stock': <property object at 0x7f1341773220>, 'important': <property object at 0x7f1341773310>, 'actions': <property object at 0x7f1341773400>, 'new': gi.FunctionInfo(new), 'clone': gi.FunctionInfo(clone), 'free': gi.FunctionInfo(free), 'set_important': gi.FunctionInfo(set_important), 'set_label': gi.FunctionInfo(set_label), 'set_stock': gi.FunctionInfo(set_stock)})"
    __gtype__ = None # (!) real value is '<GType GladeWidgetActionDef (94653531291056)>'
    __info__ = StructInfo(WidgetActionDef)


