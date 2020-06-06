# encoding: utf-8
# module gi.repository.Clutter
# from /usr/lib64/girepository-1.0/Clutter-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Container(__gobject.GInterface):
    # no doc
    def add_actor(self, actor): # real signature unknown; restored from __doc__
        """ add_actor(self, actor:Clutter.Actor) """
        pass

    def child_get_property(self, child, property, value): # real signature unknown; restored from __doc__
        """ child_get_property(self, child:Clutter.Actor, property:str, value:GObject.Value) """
        pass

    def child_notify(self, child, pspec): # real signature unknown; restored from __doc__
        """ child_notify(self, child:Clutter.Actor, pspec:GObject.ParamSpec) """
        pass

    def child_set_property(self, child, property, value): # real signature unknown; restored from __doc__
        """ child_set_property(self, child:Clutter.Actor, property:str, value:GObject.Value) """
        pass

    def class_find_child_property(self, klass, property_name): # real signature unknown; restored from __doc__
        """ class_find_child_property(klass:GObject.ObjectClass, property_name:str) -> GObject.ParamSpec """
        pass

    def class_list_child_properties(self, klass): # real signature unknown; restored from __doc__
        """ class_list_child_properties(klass:GObject.ObjectClass) -> list, n_properties:int """
        return []

    def create_child_meta(self, actor): # real signature unknown; restored from __doc__
        """ create_child_meta(self, actor:Clutter.Actor) """
        pass

    def destroy_child_meta(self, actor): # real signature unknown; restored from __doc__
        """ destroy_child_meta(self, actor:Clutter.Actor) """
        pass

    def find_child_by_name(self, child_name): # real signature unknown; restored from __doc__
        """ find_child_by_name(self, child_name:str) -> Clutter.Actor """
        pass

    def foreach(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, callback:Clutter.Callback, user_data=None) """
        pass

    def foreach_with_internals(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_with_internals(self, callback:Clutter.Callback, user_data=None) """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_child_meta(self, actor): # real signature unknown; restored from __doc__
        """ get_child_meta(self, actor:Clutter.Actor) -> Clutter.ChildMeta """
        pass

    def lower_child(self, actor, sibling=None): # real signature unknown; restored from __doc__
        """ lower_child(self, actor:Clutter.Actor, sibling:Clutter.Actor=None) """
        pass

    def raise_child(self, actor, sibling=None): # real signature unknown; restored from __doc__
        """ raise_child(self, actor:Clutter.Actor, sibling:Clutter.Actor=None) """
        pass

    def remove_actor(self, actor): # real signature unknown; restored from __doc__
        """ remove_actor(self, actor:Clutter.Actor) """
        pass

    def sort_depth_order(self): # real signature unknown; restored from __doc__
        """ sort_depth_order(self) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Container), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterContainer (94911695362208)>, '__dict__': <attribute '__dict__' of 'Container' objects>, '__weakref__': <attribute '__weakref__' of 'Container' objects>, '__doc__': None, '__gsignals__': {}, 'class_find_child_property': gi.FunctionInfo(class_find_child_property), 'class_list_child_properties': gi.FunctionInfo(class_list_child_properties), 'add_actor': gi.FunctionInfo(add_actor), 'child_get_property': gi.FunctionInfo(child_get_property), 'child_notify': gi.FunctionInfo(child_notify), 'child_set_property': gi.FunctionInfo(child_set_property), 'create_child_meta': gi.FunctionInfo(create_child_meta), 'destroy_child_meta': gi.FunctionInfo(destroy_child_meta), 'find_child_by_name': gi.FunctionInfo(find_child_by_name), 'foreach': gi.FunctionInfo(foreach), 'foreach_with_internals': gi.FunctionInfo(foreach_with_internals), 'get_child_meta': gi.FunctionInfo(get_child_meta), 'get_children': gi.FunctionInfo(get_children), 'lower_child': gi.FunctionInfo(lower_child), 'raise_child': gi.FunctionInfo(raise_child), 'remove_actor': gi.FunctionInfo(remove_actor), 'sort_depth_order': gi.FunctionInfo(sort_depth_order)})"
    __gdoc__ = 'Interface ClutterContainer\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ClutterContainer (94911695362208)>'
    __info__ = InterfaceInfo(Container)


