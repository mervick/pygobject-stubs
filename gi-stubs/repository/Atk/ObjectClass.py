# encoding: utf-8
# module gi.repository.Atk
# from /usr/lib64/girepository-1.0/Atk-1.0.typelib
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
import gobject as __gobject


class ObjectClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ObjectClass()
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

    active_descendant_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    children_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connect_property_change_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_index_in_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mdi_zorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_object_locale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initialize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    property_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_relation_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_state_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_property_change_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    visible_data_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ObjectClass), '__module__': 'gi.repository.Atk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ObjectClass' objects>, '__weakref__': <attribute '__weakref__' of 'ObjectClass' objects>, '__doc__': None, 'parent': <property object at 0x7f44c6dba4f0>, 'get_name': <property object at 0x7f44c6dba5e0>, 'get_description': <property object at 0x7f44c6dba6d0>, 'get_parent': <property object at 0x7f44c6dba7c0>, 'get_n_children': <property object at 0x7f44c6dba8b0>, 'ref_child': <property object at 0x7f44c6dba9a0>, 'get_index_in_parent': <property object at 0x7f44c6dbaae0>, 'ref_relation_set': <property object at 0x7f44c6dbabd0>, 'get_role': <property object at 0x7f44c6dbac70>, 'get_layer': <property object at 0x7f44c6dbad60>, 'get_mdi_zorder': <property object at 0x7f44c6dbae50>, 'ref_state_set': <property object at 0x7f44c6dbaf40>, 'set_name': <property object at 0x7f44c6dbd090>, 'set_description': <property object at 0x7f44c6dbd180>, 'set_parent': <property object at 0x7f44c6dbd270>, 'set_role': <property object at 0x7f44c6dbd360>, 'connect_property_change_handler': <property object at 0x7f44c6dbd4a0>, 'remove_property_change_handler': <property object at 0x7f44c6dbd5e0>, 'initialize': <property object at 0x7f44c6dbd680>, 'children_changed': <property object at 0x7f44c6dbd7c0>, 'focus_event': <property object at 0x7f44c6dbd8b0>, 'property_change': <property object at 0x7f44c6dbd9a0>, 'state_change': <property object at 0x7f44c6dbda90>, 'visible_data_changed': <property object at 0x7f44c6dbdbd0>, 'active_descendant_changed': <property object at 0x7f44c6dbdd10>, 'get_attributes': <property object at 0x7f44c6dbde00>, 'get_object_locale': <property object at 0x7f44c6dbdf40>, 'pad1': <property object at 0x7f44c6dbe040>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ObjectClass)


