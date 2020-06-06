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


class XmlDoc(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> Gladeui.XmlDoc
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_root(self): # real signature unknown; restored from __doc__
        """ get_root(self) -> Gladeui.XmlNode """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gladeui.XmlDoc """
        pass

    def new_comment(self, comment): # real signature unknown; restored from __doc__
        """ new_comment(self, comment:str) -> Gladeui.XmlNode """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gladeui.XmlDoc """
        pass

    def save(self, full_path): # real signature unknown; restored from __doc__
        """ save(self, full_path:str) -> int """
        return 0

    def set_root(self, node): # real signature unknown; restored from __doc__
        """ set_root(self, node:Gladeui.XmlNode) """
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
        """ new() -> Gladeui.XmlDoc """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(XmlDoc), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType GladeXmlDoc (94653531289136)>, '__dict__': <attribute '__dict__' of 'XmlDoc' objects>, '__weakref__': <attribute '__weakref__' of 'XmlDoc' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'get_root': gi.FunctionInfo(get_root), 'new_comment': gi.FunctionInfo(new_comment), 'ref': gi.FunctionInfo(ref), 'save': gi.FunctionInfo(save), 'set_root': gi.FunctionInfo(set_root), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod object at 0x7f13417795b0>, '__init__': <function nothing at 0x7f1342e6cee0>})"
    __gtype__ = None # (!) real value is '<GType GladeXmlDoc (94653531289136)>'
    __info__ = StructInfo(XmlDoc)


