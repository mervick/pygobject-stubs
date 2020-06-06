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


class ChildProxy(__gobject.GInterface):
    # no doc
    def child_added(self, child, name): # real signature unknown; restored from __doc__
        """ child_added(self, child:GObject.Object, name:str) """
        pass

    def child_removed(self, child, name): # real signature unknown; restored from __doc__
        """ child_removed(self, child:GObject.Object, name:str) """
        pass

    def get_children_count(self): # real signature unknown; restored from __doc__
        """ get_children_count(self) -> int """
        return 0

    def get_child_by_index(self, index): # real signature unknown; restored from __doc__
        """ get_child_by_index(self, index:int) -> GObject.Object or None """
        pass

    def get_child_by_name(self, name): # real signature unknown; restored from __doc__
        """ get_child_by_name(self, name:str) -> GObject.Object or None """
        pass

    def get_property(self, name): # real signature unknown; restored from __doc__
        """ get_property(self, name:str) -> value:GObject.Value """
        pass

    def lookup(self, name): # real signature unknown; restored from __doc__
        """ lookup(self, name:str) -> bool, target:GObject.Object, pspec:GObject.ParamSpec """
        return False

    def set_property(self, name, value): # real signature unknown; restored from __doc__
        """ set_property(self, name:str, value:GObject.Value) """
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(ChildProxy), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstChildProxy (94058976936640)>, '__dict__': <attribute '__dict__' of 'ChildProxy' objects>, '__weakref__': <attribute '__weakref__' of 'ChildProxy' objects>, '__doc__': None, '__gsignals__': {}, 'child_added': gi.FunctionInfo(child_added), 'child_removed': gi.FunctionInfo(child_removed), 'get_child_by_index': gi.FunctionInfo(get_child_by_index), 'get_child_by_name': gi.FunctionInfo(get_child_by_name), 'get_children_count': gi.FunctionInfo(get_children_count), 'get_property': gi.FunctionInfo(get_property), 'lookup': gi.FunctionInfo(lookup), 'set_property': gi.FunctionInfo(set_property)})"
    __gdoc__ = 'Interface GstChildProxy\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstChildProxy (94058976936640)>'
    __info__ = InterfaceInfo(ChildProxy)


