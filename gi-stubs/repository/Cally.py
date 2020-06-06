# encoding: utf-8
# module gi.repository.Cally
# from /usr/lib64/girepository-1.0/Cally-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk


# Variables with simple values

_namespace = 'Cally'

_version = '1.0'

__weakref__ = None

# functions

def accessibility_init(): # real signature unknown; restored from __doc__
    """ accessibility_init() -> bool """
    return False

def get_cally_initialized(): # real signature unknown; restored from __doc__
    """ get_cally_initialized() -> bool """
    return False

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

class Actor(__gi_repository_Atk.GObjectAccessible, __gi_repository_Atk.Action, __gi_repository_Atk.Component):
    """
    :Constructors:
    
    ::
    
        Actor(**properties)
        new(actor:Clutter.Actor) -> Atk.Object
    """
    def add_action(self, action_name, action_description, action_keybinding, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_action(self, action_name:str, action_description:str, action_keybinding:str, callback:Cally.ActionCallback, user_data=None) -> int """
        return 0

    def add_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ add_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_action(self, i): # real signature unknown; restored from __doc__
        """ do_action(self, i:int) -> bool """
        return False

    def do_active_descendant_changed(self, *args, **kwargs): # real signature unknown
        """ active_descendant_changed(self, child=None) """
        pass

    def do_children_changed(self, *args, **kwargs): # real signature unknown
        """ children_changed(self, change_index:int, changed_child=None) """
        pass

    def do_focus_event(self, *args, **kwargs): # real signature unknown
        """ focus_event(self, focus_in:bool) """
        pass

    def do_get_attributes(self, *args, **kwargs): # real signature unknown
        """ get_attributes(self) -> list """
        pass

    def do_get_description(self, *args, **kwargs): # real signature unknown
        """ get_description(self) -> str """
        pass

    def do_get_index_in_parent(self, *args, **kwargs): # real signature unknown
        """ get_index_in_parent(self) -> int """
        pass

    def do_get_layer(self, *args, **kwargs): # real signature unknown
        """ get_layer(self) -> Atk.Layer """
        pass

    def do_get_mdi_zorder(self, *args, **kwargs): # real signature unknown
        """ get_mdi_zorder(self) -> int """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_get_n_children(self, *args, **kwargs): # real signature unknown
        """ get_n_children(self) -> int """
        pass

    def do_get_object_locale(self, *args, **kwargs): # real signature unknown
        """ get_object_locale(self) -> str """
        pass

    def do_get_parent(self, *args, **kwargs): # real signature unknown
        """ get_parent(self) -> Atk.Object """
        pass

    def do_get_role(self, *args, **kwargs): # real signature unknown
        """ get_role(self) -> Atk.Role """
        pass

    def do_initialize(self, *args, **kwargs): # real signature unknown
        """ initialize(self, data=None) """
        pass

    def do_property_change(self, *args, **kwargs): # real signature unknown
        """ property_change(self, values:Atk.PropertyValues) """
        pass

    def do_ref_relation_set(self, *args, **kwargs): # real signature unknown
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def do_ref_state_set(self, *args, **kwargs): # real signature unknown
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def do_remove_property_change_handler(self, *args, **kwargs): # real signature unknown
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def do_set_description(self, *args, **kwargs): # real signature unknown
        """ set_description(self, description:str) """
        pass

    def do_set_name(self, *args, **kwargs): # real signature unknown
        """ set_name(self, name:str) """
        pass

    def do_set_parent(self, *args, **kwargs): # real signature unknown
        """ set_parent(self, parent:Atk.Object) """
        pass

    def do_set_role(self, *args, **kwargs): # real signature unknown
        """ set_role(self, role:Atk.Role) """
        pass

    def do_state_change(self, *args, **kwargs): # real signature unknown
        """ state_change(self, name:str, state_set:bool) """
        pass

    def do_visible_data_changed(self, *args, **kwargs): # real signature unknown
        """ visible_data_changed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def for_object(self, obj): # real signature unknown; restored from __doc__
        """ for_object(obj:GObject.Object) -> Atk.Object """
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accessible_id(self): # real signature unknown; restored from __doc__
        """ get_accessible_id(self) -> str """
        return ""

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_extents(self, coord_type): # real signature unknown; restored from __doc__
        """ get_extents(self, coord_type:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_index_in_parent(self): # real signature unknown; restored from __doc__
        """ get_index_in_parent(self) -> int """
        return 0

    def get_keybinding(self, i): # real signature unknown; restored from __doc__
        """ get_keybinding(self, i:int) -> str or None """
        return ""

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atk.Layer """
        pass

    def get_localized_name(self, i): # real signature unknown; restored from __doc__
        """ get_localized_name(self, i:int) -> str or None """
        return ""

    def get_mdi_zorder(self): # real signature unknown; restored from __doc__
        """ get_mdi_zorder(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_accessible_children(self): # real signature unknown; restored from __doc__
        """ get_n_accessible_children(self) -> int """
        return 0

    def get_n_actions(self): # real signature unknown; restored from __doc__
        """ get_n_actions(self) -> int """
        return 0

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GObject.Object """
        pass

    def get_object_locale(self): # real signature unknown; restored from __doc__
        """ get_object_locale(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Atk.Object """
        pass

    def get_position(self, coord_type): # real signature unknown; restored from __doc__
        """ get_position(self, coord_type:Atk.CoordType) -> x:int, y:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> Atk.Role """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:int, height:int """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
        return False

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, data=None): # real signature unknown; restored from __doc__
        """ initialize(self, data=None) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, actor): # real signature unknown; restored from __doc__
        """ new(actor:Clutter.Actor) -> Atk.Object """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_state_change(self, state, value): # real signature unknown; restored from __doc__
        """ notify_state_change(self, state:int, value:bool) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_parent(self): # real signature unknown; restored from __doc__
        """ peek_parent(self) -> Atk.Object """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_accessible_at_point(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ ref_accessible_at_point(self, x:int, y:int, coord_type:Atk.CoordType) -> Atk.Object or None """
        pass

    def ref_accessible_child(self, i): # real signature unknown; restored from __doc__
        """ ref_accessible_child(self, i:int) -> Atk.Object """
        pass

    def ref_relation_set(self): # real signature unknown; restored from __doc__
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_state_set(self): # real signature unknown; restored from __doc__
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def remove_action(self, action_id): # real signature unknown; restored from __doc__
        """ remove_action(self, action_id:int) -> bool """
        return False

    def remove_action_by_name(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action_by_name(self, action_name:str) -> bool """
        return False

    def remove_focus_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_focus_handler(self, handler_id:int) """
        pass

    def remove_property_change_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def remove_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ remove_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atk.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def set_accessible_id(self, name): # real signature unknown; restored from __doc__
        """ set_accessible_id(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_extents(self, x, y, width, height, coord_type): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Atk.Object) """
        pass

    def set_position(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:Atk.Role) """
        pass

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    accessible_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    relation_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffaba7e45b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Actor), '__module__': 'gi.repository.Cally', '__gtype__': <GType CallyActor (94729765932640)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_action': gi.FunctionInfo(add_action), 'remove_action': gi.FunctionInfo(remove_action), 'remove_action_by_name': gi.FunctionInfo(remove_action_by_name), 'parent': <property object at 0x7ffaba7f5130>, 'priv': <property object at 0x7ffaba7f5220>})"
    __gdoc__ = 'Object CallyActor\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkObject:\n  children-changed (guint, gpointer)\n  focus-event (gboolean)\n  property-change (gpointer)\n  state-change (gchararray, gboolean)\n  visible-data-changed ()\n  active-descendant-changed (gpointer)\n\nProperties from AtkObject:\n  accessible-name -> gchararray: Accessible Name\n    Object instance’s name formatted for assistive technology access\n  accessible-description -> gchararray: Accessible Description\n    Description of an object, formatted for assistive technology access\n  accessible-parent -> AtkObject: Accessible Parent\n    Parent of the current accessible as returned by atk_object_get_parent()\n  accessible-value -> gdouble: Accessible Value\n    Is used to notify that the value has changed\n  accessible-role -> AtkRole: Accessible Role\n    The accessible role of this object\n  accessible-component-layer -> gint: Accessible Layer\n    The accessible layer of this object\n  accessible-component-mdi-zorder -> gint: Accessible MDI Value\n    The accessible MDI value of this object\n  accessible-table-caption -> gchararray: Accessible Table Caption\n    Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead\n  accessible-table-column-description -> gchararray: Accessible Table Column Description\n    Is used to notify that the table column description has changed\n  accessible-table-column-header -> AtkObject: Accessible Table Column Header\n    Is used to notify that the table column header has changed\n  accessible-table-row-description -> gchararray: Accessible Table Row Description\n    Is used to notify that the table row description has changed\n  accessible-table-row-header -> AtkObject: Accessible Table Row Header\n    Is used to notify that the table row header has changed\n  accessible-table-summary -> AtkObject: Accessible Table Summary\n    Is used to notify that the table summary has changed\n  accessible-table-caption-object -> AtkObject: Accessible Table Caption Object\n    Is used to notify that the table caption has changed\n  accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links\n    The number of links which the current AtkHypertext has\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CallyActor (94729765932640)>'
    __info__ = ObjectInfo(Actor)


class ActorClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ActorClass()
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

    add_actor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_clutter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notify_clutter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_actor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ActorClass), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ActorClass' objects>, '__weakref__': <attribute '__weakref__' of 'ActorClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ffaba7f53b0>, 'notify_clutter': <property object at 0x7ffaba7f54a0>, 'focus_clutter': <property object at 0x7ffaba7f5590>, 'add_actor': <property object at 0x7ffaba7f5680>, 'remove_actor': <property object at 0x7ffaba7f5770>, '_padding_dummy': <property object at 0x7ffaba7f5860>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ActorClass)


class ActorPrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ActorPrivate), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ActorPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'ActorPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ActorPrivate)


class Clone(Actor):
    """
    :Constructors:
    
    ::
    
        Clone(**properties)
        new(actor:Clutter.Actor) -> Atk.Object
    """
    def add_action(self, action_name, action_description, action_keybinding, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_action(self, action_name:str, action_description:str, action_keybinding:str, callback:Cally.ActionCallback, user_data=None) -> int """
        return 0

    def add_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ add_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_action(self, i): # real signature unknown; restored from __doc__
        """ do_action(self, i:int) -> bool """
        return False

    def do_active_descendant_changed(self, *args, **kwargs): # real signature unknown
        """ active_descendant_changed(self, child=None) """
        pass

    def do_children_changed(self, *args, **kwargs): # real signature unknown
        """ children_changed(self, change_index:int, changed_child=None) """
        pass

    def do_focus_event(self, *args, **kwargs): # real signature unknown
        """ focus_event(self, focus_in:bool) """
        pass

    def do_get_attributes(self, *args, **kwargs): # real signature unknown
        """ get_attributes(self) -> list """
        pass

    def do_get_description(self, *args, **kwargs): # real signature unknown
        """ get_description(self) -> str """
        pass

    def do_get_index_in_parent(self, *args, **kwargs): # real signature unknown
        """ get_index_in_parent(self) -> int """
        pass

    def do_get_layer(self, *args, **kwargs): # real signature unknown
        """ get_layer(self) -> Atk.Layer """
        pass

    def do_get_mdi_zorder(self, *args, **kwargs): # real signature unknown
        """ get_mdi_zorder(self) -> int """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_get_n_children(self, *args, **kwargs): # real signature unknown
        """ get_n_children(self) -> int """
        pass

    def do_get_object_locale(self, *args, **kwargs): # real signature unknown
        """ get_object_locale(self) -> str """
        pass

    def do_get_parent(self, *args, **kwargs): # real signature unknown
        """ get_parent(self) -> Atk.Object """
        pass

    def do_get_role(self, *args, **kwargs): # real signature unknown
        """ get_role(self) -> Atk.Role """
        pass

    def do_initialize(self, *args, **kwargs): # real signature unknown
        """ initialize(self, data=None) """
        pass

    def do_property_change(self, *args, **kwargs): # real signature unknown
        """ property_change(self, values:Atk.PropertyValues) """
        pass

    def do_ref_relation_set(self, *args, **kwargs): # real signature unknown
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def do_ref_state_set(self, *args, **kwargs): # real signature unknown
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def do_remove_property_change_handler(self, *args, **kwargs): # real signature unknown
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def do_set_description(self, *args, **kwargs): # real signature unknown
        """ set_description(self, description:str) """
        pass

    def do_set_name(self, *args, **kwargs): # real signature unknown
        """ set_name(self, name:str) """
        pass

    def do_set_parent(self, *args, **kwargs): # real signature unknown
        """ set_parent(self, parent:Atk.Object) """
        pass

    def do_set_role(self, *args, **kwargs): # real signature unknown
        """ set_role(self, role:Atk.Role) """
        pass

    def do_state_change(self, *args, **kwargs): # real signature unknown
        """ state_change(self, name:str, state_set:bool) """
        pass

    def do_visible_data_changed(self, *args, **kwargs): # real signature unknown
        """ visible_data_changed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def for_object(self, obj): # real signature unknown; restored from __doc__
        """ for_object(obj:GObject.Object) -> Atk.Object """
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accessible_id(self): # real signature unknown; restored from __doc__
        """ get_accessible_id(self) -> str """
        return ""

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_extents(self, coord_type): # real signature unknown; restored from __doc__
        """ get_extents(self, coord_type:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_index_in_parent(self): # real signature unknown; restored from __doc__
        """ get_index_in_parent(self) -> int """
        return 0

    def get_keybinding(self, i): # real signature unknown; restored from __doc__
        """ get_keybinding(self, i:int) -> str or None """
        return ""

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atk.Layer """
        pass

    def get_localized_name(self, i): # real signature unknown; restored from __doc__
        """ get_localized_name(self, i:int) -> str or None """
        return ""

    def get_mdi_zorder(self): # real signature unknown; restored from __doc__
        """ get_mdi_zorder(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_accessible_children(self): # real signature unknown; restored from __doc__
        """ get_n_accessible_children(self) -> int """
        return 0

    def get_n_actions(self): # real signature unknown; restored from __doc__
        """ get_n_actions(self) -> int """
        return 0

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GObject.Object """
        pass

    def get_object_locale(self): # real signature unknown; restored from __doc__
        """ get_object_locale(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Atk.Object """
        pass

    def get_position(self, coord_type): # real signature unknown; restored from __doc__
        """ get_position(self, coord_type:Atk.CoordType) -> x:int, y:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> Atk.Role """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:int, height:int """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
        return False

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, data=None): # real signature unknown; restored from __doc__
        """ initialize(self, data=None) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, actor): # real signature unknown; restored from __doc__
        """ new(actor:Clutter.Actor) -> Atk.Object """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_state_change(self, state, value): # real signature unknown; restored from __doc__
        """ notify_state_change(self, state:int, value:bool) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_parent(self): # real signature unknown; restored from __doc__
        """ peek_parent(self) -> Atk.Object """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_accessible_at_point(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ ref_accessible_at_point(self, x:int, y:int, coord_type:Atk.CoordType) -> Atk.Object or None """
        pass

    def ref_accessible_child(self, i): # real signature unknown; restored from __doc__
        """ ref_accessible_child(self, i:int) -> Atk.Object """
        pass

    def ref_relation_set(self): # real signature unknown; restored from __doc__
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_state_set(self): # real signature unknown; restored from __doc__
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def remove_action(self, action_id): # real signature unknown; restored from __doc__
        """ remove_action(self, action_id:int) -> bool """
        return False

    def remove_action_by_name(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action_by_name(self, action_name:str) -> bool """
        return False

    def remove_focus_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_focus_handler(self, handler_id:int) """
        pass

    def remove_property_change_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def remove_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ remove_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atk.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def set_accessible_id(self, name): # real signature unknown; restored from __doc__
        """ set_accessible_id(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_extents(self, x, y, width, height, coord_type): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Atk.Object) """
        pass

    def set_position(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:Atk.Role) """
        pass

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    accessible_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    relation_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffab9fcd5b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Clone), '__module__': 'gi.repository.Cally', '__gtype__': <GType CallyClone (94729765957872)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent': <property object at 0x7ffaba7f5a40>, 'priv': <property object at 0x7ffaba7f5b80>})"
    __gdoc__ = 'Object CallyClone\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkObject:\n  children-changed (guint, gpointer)\n  focus-event (gboolean)\n  property-change (gpointer)\n  state-change (gchararray, gboolean)\n  visible-data-changed ()\n  active-descendant-changed (gpointer)\n\nProperties from AtkObject:\n  accessible-name -> gchararray: Accessible Name\n    Object instance’s name formatted for assistive technology access\n  accessible-description -> gchararray: Accessible Description\n    Description of an object, formatted for assistive technology access\n  accessible-parent -> AtkObject: Accessible Parent\n    Parent of the current accessible as returned by atk_object_get_parent()\n  accessible-value -> gdouble: Accessible Value\n    Is used to notify that the value has changed\n  accessible-role -> AtkRole: Accessible Role\n    The accessible role of this object\n  accessible-component-layer -> gint: Accessible Layer\n    The accessible layer of this object\n  accessible-component-mdi-zorder -> gint: Accessible MDI Value\n    The accessible MDI value of this object\n  accessible-table-caption -> gchararray: Accessible Table Caption\n    Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead\n  accessible-table-column-description -> gchararray: Accessible Table Column Description\n    Is used to notify that the table column description has changed\n  accessible-table-column-header -> AtkObject: Accessible Table Column Header\n    Is used to notify that the table column header has changed\n  accessible-table-row-description -> gchararray: Accessible Table Row Description\n    Is used to notify that the table row description has changed\n  accessible-table-row-header -> AtkObject: Accessible Table Row Header\n    Is used to notify that the table row header has changed\n  accessible-table-summary -> AtkObject: Accessible Table Summary\n    Is used to notify that the table summary has changed\n  accessible-table-caption-object -> AtkObject: Accessible Table Caption Object\n    Is used to notify that the table caption has changed\n  accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links\n    The number of links which the current AtkHypertext has\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CallyClone (94729765957872)>'
    __info__ = ObjectInfo(Clone)


class CloneClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        CloneClass()
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CloneClass), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'CloneClass' objects>, '__weakref__': <attribute '__weakref__' of 'CloneClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ffaba7f5d10>, '_padding_dummy': <property object at 0x7ffaba7f5e00>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(CloneClass)


class ClonePrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ClonePrivate), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ClonePrivate' objects>, '__weakref__': <attribute '__weakref__' of 'ClonePrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ClonePrivate)


class Group(Actor):
    """
    :Constructors:
    
    ::
    
        Group(**properties)
        new(actor:Clutter.Actor) -> Atk.Object
    """
    def add_action(self, action_name, action_description, action_keybinding, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_action(self, action_name:str, action_description:str, action_keybinding:str, callback:Cally.ActionCallback, user_data=None) -> int """
        return 0

    def add_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ add_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_action(self, i): # real signature unknown; restored from __doc__
        """ do_action(self, i:int) -> bool """
        return False

    def do_active_descendant_changed(self, *args, **kwargs): # real signature unknown
        """ active_descendant_changed(self, child=None) """
        pass

    def do_children_changed(self, *args, **kwargs): # real signature unknown
        """ children_changed(self, change_index:int, changed_child=None) """
        pass

    def do_focus_event(self, *args, **kwargs): # real signature unknown
        """ focus_event(self, focus_in:bool) """
        pass

    def do_get_attributes(self, *args, **kwargs): # real signature unknown
        """ get_attributes(self) -> list """
        pass

    def do_get_description(self, *args, **kwargs): # real signature unknown
        """ get_description(self) -> str """
        pass

    def do_get_index_in_parent(self, *args, **kwargs): # real signature unknown
        """ get_index_in_parent(self) -> int """
        pass

    def do_get_layer(self, *args, **kwargs): # real signature unknown
        """ get_layer(self) -> Atk.Layer """
        pass

    def do_get_mdi_zorder(self, *args, **kwargs): # real signature unknown
        """ get_mdi_zorder(self) -> int """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_get_n_children(self, *args, **kwargs): # real signature unknown
        """ get_n_children(self) -> int """
        pass

    def do_get_object_locale(self, *args, **kwargs): # real signature unknown
        """ get_object_locale(self) -> str """
        pass

    def do_get_parent(self, *args, **kwargs): # real signature unknown
        """ get_parent(self) -> Atk.Object """
        pass

    def do_get_role(self, *args, **kwargs): # real signature unknown
        """ get_role(self) -> Atk.Role """
        pass

    def do_initialize(self, *args, **kwargs): # real signature unknown
        """ initialize(self, data=None) """
        pass

    def do_property_change(self, *args, **kwargs): # real signature unknown
        """ property_change(self, values:Atk.PropertyValues) """
        pass

    def do_ref_relation_set(self, *args, **kwargs): # real signature unknown
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def do_ref_state_set(self, *args, **kwargs): # real signature unknown
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def do_remove_property_change_handler(self, *args, **kwargs): # real signature unknown
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def do_set_description(self, *args, **kwargs): # real signature unknown
        """ set_description(self, description:str) """
        pass

    def do_set_name(self, *args, **kwargs): # real signature unknown
        """ set_name(self, name:str) """
        pass

    def do_set_parent(self, *args, **kwargs): # real signature unknown
        """ set_parent(self, parent:Atk.Object) """
        pass

    def do_set_role(self, *args, **kwargs): # real signature unknown
        """ set_role(self, role:Atk.Role) """
        pass

    def do_state_change(self, *args, **kwargs): # real signature unknown
        """ state_change(self, name:str, state_set:bool) """
        pass

    def do_visible_data_changed(self, *args, **kwargs): # real signature unknown
        """ visible_data_changed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def for_object(self, obj): # real signature unknown; restored from __doc__
        """ for_object(obj:GObject.Object) -> Atk.Object """
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accessible_id(self): # real signature unknown; restored from __doc__
        """ get_accessible_id(self) -> str """
        return ""

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_extents(self, coord_type): # real signature unknown; restored from __doc__
        """ get_extents(self, coord_type:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_index_in_parent(self): # real signature unknown; restored from __doc__
        """ get_index_in_parent(self) -> int """
        return 0

    def get_keybinding(self, i): # real signature unknown; restored from __doc__
        """ get_keybinding(self, i:int) -> str or None """
        return ""

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atk.Layer """
        pass

    def get_localized_name(self, i): # real signature unknown; restored from __doc__
        """ get_localized_name(self, i:int) -> str or None """
        return ""

    def get_mdi_zorder(self): # real signature unknown; restored from __doc__
        """ get_mdi_zorder(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_accessible_children(self): # real signature unknown; restored from __doc__
        """ get_n_accessible_children(self) -> int """
        return 0

    def get_n_actions(self): # real signature unknown; restored from __doc__
        """ get_n_actions(self) -> int """
        return 0

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GObject.Object """
        pass

    def get_object_locale(self): # real signature unknown; restored from __doc__
        """ get_object_locale(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Atk.Object """
        pass

    def get_position(self, coord_type): # real signature unknown; restored from __doc__
        """ get_position(self, coord_type:Atk.CoordType) -> x:int, y:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> Atk.Role """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:int, height:int """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
        return False

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, data=None): # real signature unknown; restored from __doc__
        """ initialize(self, data=None) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, actor): # real signature unknown; restored from __doc__
        """ new(actor:Clutter.Actor) -> Atk.Object """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_state_change(self, state, value): # real signature unknown; restored from __doc__
        """ notify_state_change(self, state:int, value:bool) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_parent(self): # real signature unknown; restored from __doc__
        """ peek_parent(self) -> Atk.Object """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_accessible_at_point(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ ref_accessible_at_point(self, x:int, y:int, coord_type:Atk.CoordType) -> Atk.Object or None """
        pass

    def ref_accessible_child(self, i): # real signature unknown; restored from __doc__
        """ ref_accessible_child(self, i:int) -> Atk.Object """
        pass

    def ref_relation_set(self): # real signature unknown; restored from __doc__
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_state_set(self): # real signature unknown; restored from __doc__
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def remove_action(self, action_id): # real signature unknown; restored from __doc__
        """ remove_action(self, action_id:int) -> bool """
        return False

    def remove_action_by_name(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action_by_name(self, action_name:str) -> bool """
        return False

    def remove_focus_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_focus_handler(self, handler_id:int) """
        pass

    def remove_property_change_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def remove_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ remove_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atk.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def set_accessible_id(self, name): # real signature unknown; restored from __doc__
        """ set_accessible_id(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_extents(self, x, y, width, height, coord_type): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Atk.Object) """
        pass

    def set_position(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:Atk.Role) """
        pass

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    accessible_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    relation_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffaba84ed30>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Group), '__module__': 'gi.repository.Cally', '__gtype__': <GType CallyGroup (94729765963104)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent': <property object at 0x7ffaba7f6040>, 'priv': <property object at 0x7ffaba7f6180>})"
    __gdoc__ = 'Object CallyGroup\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkObject:\n  children-changed (guint, gpointer)\n  focus-event (gboolean)\n  property-change (gpointer)\n  state-change (gchararray, gboolean)\n  visible-data-changed ()\n  active-descendant-changed (gpointer)\n\nProperties from AtkObject:\n  accessible-name -> gchararray: Accessible Name\n    Object instance’s name formatted for assistive technology access\n  accessible-description -> gchararray: Accessible Description\n    Description of an object, formatted for assistive technology access\n  accessible-parent -> AtkObject: Accessible Parent\n    Parent of the current accessible as returned by atk_object_get_parent()\n  accessible-value -> gdouble: Accessible Value\n    Is used to notify that the value has changed\n  accessible-role -> AtkRole: Accessible Role\n    The accessible role of this object\n  accessible-component-layer -> gint: Accessible Layer\n    The accessible layer of this object\n  accessible-component-mdi-zorder -> gint: Accessible MDI Value\n    The accessible MDI value of this object\n  accessible-table-caption -> gchararray: Accessible Table Caption\n    Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead\n  accessible-table-column-description -> gchararray: Accessible Table Column Description\n    Is used to notify that the table column description has changed\n  accessible-table-column-header -> AtkObject: Accessible Table Column Header\n    Is used to notify that the table column header has changed\n  accessible-table-row-description -> gchararray: Accessible Table Row Description\n    Is used to notify that the table row description has changed\n  accessible-table-row-header -> AtkObject: Accessible Table Row Header\n    Is used to notify that the table row header has changed\n  accessible-table-summary -> AtkObject: Accessible Table Summary\n    Is used to notify that the table summary has changed\n  accessible-table-caption-object -> AtkObject: Accessible Table Caption Object\n    Is used to notify that the table caption has changed\n  accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links\n    The number of links which the current AtkHypertext has\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CallyGroup (94729765963104)>'
    __info__ = ObjectInfo(Group)


class GroupClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GroupClass()
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GroupClass), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GroupClass' objects>, '__weakref__': <attribute '__weakref__' of 'GroupClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ffaba7f62c0>, '_padding_dummy': <property object at 0x7ffaba7f63b0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GroupClass)


class GroupPrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GroupPrivate), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GroupPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'GroupPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GroupPrivate)


class Rectangle(Actor):
    """
    :Constructors:
    
    ::
    
        Rectangle(**properties)
        new(actor:Clutter.Actor) -> Atk.Object
    """
    def add_action(self, action_name, action_description, action_keybinding, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_action(self, action_name:str, action_description:str, action_keybinding:str, callback:Cally.ActionCallback, user_data=None) -> int """
        return 0

    def add_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ add_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_action(self, i): # real signature unknown; restored from __doc__
        """ do_action(self, i:int) -> bool """
        return False

    def do_active_descendant_changed(self, *args, **kwargs): # real signature unknown
        """ active_descendant_changed(self, child=None) """
        pass

    def do_children_changed(self, *args, **kwargs): # real signature unknown
        """ children_changed(self, change_index:int, changed_child=None) """
        pass

    def do_focus_event(self, *args, **kwargs): # real signature unknown
        """ focus_event(self, focus_in:bool) """
        pass

    def do_get_attributes(self, *args, **kwargs): # real signature unknown
        """ get_attributes(self) -> list """
        pass

    def do_get_description(self, *args, **kwargs): # real signature unknown
        """ get_description(self) -> str """
        pass

    def do_get_index_in_parent(self, *args, **kwargs): # real signature unknown
        """ get_index_in_parent(self) -> int """
        pass

    def do_get_layer(self, *args, **kwargs): # real signature unknown
        """ get_layer(self) -> Atk.Layer """
        pass

    def do_get_mdi_zorder(self, *args, **kwargs): # real signature unknown
        """ get_mdi_zorder(self) -> int """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_get_n_children(self, *args, **kwargs): # real signature unknown
        """ get_n_children(self) -> int """
        pass

    def do_get_object_locale(self, *args, **kwargs): # real signature unknown
        """ get_object_locale(self) -> str """
        pass

    def do_get_parent(self, *args, **kwargs): # real signature unknown
        """ get_parent(self) -> Atk.Object """
        pass

    def do_get_role(self, *args, **kwargs): # real signature unknown
        """ get_role(self) -> Atk.Role """
        pass

    def do_initialize(self, *args, **kwargs): # real signature unknown
        """ initialize(self, data=None) """
        pass

    def do_property_change(self, *args, **kwargs): # real signature unknown
        """ property_change(self, values:Atk.PropertyValues) """
        pass

    def do_ref_relation_set(self, *args, **kwargs): # real signature unknown
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def do_ref_state_set(self, *args, **kwargs): # real signature unknown
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def do_remove_property_change_handler(self, *args, **kwargs): # real signature unknown
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def do_set_description(self, *args, **kwargs): # real signature unknown
        """ set_description(self, description:str) """
        pass

    def do_set_name(self, *args, **kwargs): # real signature unknown
        """ set_name(self, name:str) """
        pass

    def do_set_parent(self, *args, **kwargs): # real signature unknown
        """ set_parent(self, parent:Atk.Object) """
        pass

    def do_set_role(self, *args, **kwargs): # real signature unknown
        """ set_role(self, role:Atk.Role) """
        pass

    def do_state_change(self, *args, **kwargs): # real signature unknown
        """ state_change(self, name:str, state_set:bool) """
        pass

    def do_visible_data_changed(self, *args, **kwargs): # real signature unknown
        """ visible_data_changed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def for_object(self, obj): # real signature unknown; restored from __doc__
        """ for_object(obj:GObject.Object) -> Atk.Object """
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accessible_id(self): # real signature unknown; restored from __doc__
        """ get_accessible_id(self) -> str """
        return ""

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_extents(self, coord_type): # real signature unknown; restored from __doc__
        """ get_extents(self, coord_type:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_index_in_parent(self): # real signature unknown; restored from __doc__
        """ get_index_in_parent(self) -> int """
        return 0

    def get_keybinding(self, i): # real signature unknown; restored from __doc__
        """ get_keybinding(self, i:int) -> str or None """
        return ""

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atk.Layer """
        pass

    def get_localized_name(self, i): # real signature unknown; restored from __doc__
        """ get_localized_name(self, i:int) -> str or None """
        return ""

    def get_mdi_zorder(self): # real signature unknown; restored from __doc__
        """ get_mdi_zorder(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_accessible_children(self): # real signature unknown; restored from __doc__
        """ get_n_accessible_children(self) -> int """
        return 0

    def get_n_actions(self): # real signature unknown; restored from __doc__
        """ get_n_actions(self) -> int """
        return 0

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GObject.Object """
        pass

    def get_object_locale(self): # real signature unknown; restored from __doc__
        """ get_object_locale(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Atk.Object """
        pass

    def get_position(self, coord_type): # real signature unknown; restored from __doc__
        """ get_position(self, coord_type:Atk.CoordType) -> x:int, y:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> Atk.Role """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:int, height:int """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
        return False

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, data=None): # real signature unknown; restored from __doc__
        """ initialize(self, data=None) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, actor): # real signature unknown; restored from __doc__
        """ new(actor:Clutter.Actor) -> Atk.Object """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_state_change(self, state, value): # real signature unknown; restored from __doc__
        """ notify_state_change(self, state:int, value:bool) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_parent(self): # real signature unknown; restored from __doc__
        """ peek_parent(self) -> Atk.Object """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_accessible_at_point(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ ref_accessible_at_point(self, x:int, y:int, coord_type:Atk.CoordType) -> Atk.Object or None """
        pass

    def ref_accessible_child(self, i): # real signature unknown; restored from __doc__
        """ ref_accessible_child(self, i:int) -> Atk.Object """
        pass

    def ref_relation_set(self): # real signature unknown; restored from __doc__
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_state_set(self): # real signature unknown; restored from __doc__
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def remove_action(self, action_id): # real signature unknown; restored from __doc__
        """ remove_action(self, action_id:int) -> bool """
        return False

    def remove_action_by_name(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action_by_name(self, action_name:str) -> bool """
        return False

    def remove_focus_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_focus_handler(self, handler_id:int) """
        pass

    def remove_property_change_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def remove_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ remove_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atk.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def set_accessible_id(self, name): # real signature unknown; restored from __doc__
        """ set_accessible_id(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_extents(self, x, y, width, height, coord_type): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Atk.Object) """
        pass

    def set_position(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:Atk.Role) """
        pass

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    accessible_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    relation_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffaba7d0640>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Rectangle), '__module__': 'gi.repository.Cally', '__gtype__': <GType CallyRectangle (94729765966240)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent': <property object at 0x7ffaba7f6590>, 'priv': <property object at 0x7ffaba7f66d0>})"
    __gdoc__ = 'Object CallyRectangle\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkObject:\n  children-changed (guint, gpointer)\n  focus-event (gboolean)\n  property-change (gpointer)\n  state-change (gchararray, gboolean)\n  visible-data-changed ()\n  active-descendant-changed (gpointer)\n\nProperties from AtkObject:\n  accessible-name -> gchararray: Accessible Name\n    Object instance’s name formatted for assistive technology access\n  accessible-description -> gchararray: Accessible Description\n    Description of an object, formatted for assistive technology access\n  accessible-parent -> AtkObject: Accessible Parent\n    Parent of the current accessible as returned by atk_object_get_parent()\n  accessible-value -> gdouble: Accessible Value\n    Is used to notify that the value has changed\n  accessible-role -> AtkRole: Accessible Role\n    The accessible role of this object\n  accessible-component-layer -> gint: Accessible Layer\n    The accessible layer of this object\n  accessible-component-mdi-zorder -> gint: Accessible MDI Value\n    The accessible MDI value of this object\n  accessible-table-caption -> gchararray: Accessible Table Caption\n    Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead\n  accessible-table-column-description -> gchararray: Accessible Table Column Description\n    Is used to notify that the table column description has changed\n  accessible-table-column-header -> AtkObject: Accessible Table Column Header\n    Is used to notify that the table column header has changed\n  accessible-table-row-description -> gchararray: Accessible Table Row Description\n    Is used to notify that the table row description has changed\n  accessible-table-row-header -> AtkObject: Accessible Table Row Header\n    Is used to notify that the table row header has changed\n  accessible-table-summary -> AtkObject: Accessible Table Summary\n    Is used to notify that the table summary has changed\n  accessible-table-caption-object -> AtkObject: Accessible Table Caption Object\n    Is used to notify that the table caption has changed\n  accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links\n    The number of links which the current AtkHypertext has\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CallyRectangle (94729765966240)>'
    __info__ = ObjectInfo(Rectangle)


class RectangleClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        RectangleClass()
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RectangleClass), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RectangleClass' objects>, '__weakref__': <attribute '__weakref__' of 'RectangleClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ffaba7f6860>, '_padding_dummy': <property object at 0x7ffaba7f6950>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RectangleClass)


class RectanglePrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RectanglePrivate), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RectanglePrivate' objects>, '__weakref__': <attribute '__weakref__' of 'RectanglePrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RectanglePrivate)


class Root(__gi_repository_Atk.GObjectAccessible):
    """
    :Constructors:
    
    ::
    
        Root(**properties)
        new() -> Atk.Object
    """
    def add_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ add_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_active_descendant_changed(self, *args, **kwargs): # real signature unknown
        """ active_descendant_changed(self, child=None) """
        pass

    def do_children_changed(self, *args, **kwargs): # real signature unknown
        """ children_changed(self, change_index:int, changed_child=None) """
        pass

    def do_focus_event(self, *args, **kwargs): # real signature unknown
        """ focus_event(self, focus_in:bool) """
        pass

    def do_get_attributes(self, *args, **kwargs): # real signature unknown
        """ get_attributes(self) -> list """
        pass

    def do_get_description(self, *args, **kwargs): # real signature unknown
        """ get_description(self) -> str """
        pass

    def do_get_index_in_parent(self, *args, **kwargs): # real signature unknown
        """ get_index_in_parent(self) -> int """
        pass

    def do_get_layer(self, *args, **kwargs): # real signature unknown
        """ get_layer(self) -> Atk.Layer """
        pass

    def do_get_mdi_zorder(self, *args, **kwargs): # real signature unknown
        """ get_mdi_zorder(self) -> int """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_get_n_children(self, *args, **kwargs): # real signature unknown
        """ get_n_children(self) -> int """
        pass

    def do_get_object_locale(self, *args, **kwargs): # real signature unknown
        """ get_object_locale(self) -> str """
        pass

    def do_get_parent(self, *args, **kwargs): # real signature unknown
        """ get_parent(self) -> Atk.Object """
        pass

    def do_get_role(self, *args, **kwargs): # real signature unknown
        """ get_role(self) -> Atk.Role """
        pass

    def do_initialize(self, *args, **kwargs): # real signature unknown
        """ initialize(self, data=None) """
        pass

    def do_property_change(self, *args, **kwargs): # real signature unknown
        """ property_change(self, values:Atk.PropertyValues) """
        pass

    def do_ref_relation_set(self, *args, **kwargs): # real signature unknown
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def do_ref_state_set(self, *args, **kwargs): # real signature unknown
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def do_remove_property_change_handler(self, *args, **kwargs): # real signature unknown
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def do_set_description(self, *args, **kwargs): # real signature unknown
        """ set_description(self, description:str) """
        pass

    def do_set_name(self, *args, **kwargs): # real signature unknown
        """ set_name(self, name:str) """
        pass

    def do_set_parent(self, *args, **kwargs): # real signature unknown
        """ set_parent(self, parent:Atk.Object) """
        pass

    def do_set_role(self, *args, **kwargs): # real signature unknown
        """ set_role(self, role:Atk.Role) """
        pass

    def do_state_change(self, *args, **kwargs): # real signature unknown
        """ state_change(self, name:str, state_set:bool) """
        pass

    def do_visible_data_changed(self, *args, **kwargs): # real signature unknown
        """ visible_data_changed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def for_object(self, obj): # real signature unknown; restored from __doc__
        """ for_object(obj:GObject.Object) -> Atk.Object """
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accessible_id(self): # real signature unknown; restored from __doc__
        """ get_accessible_id(self) -> str """
        return ""

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_index_in_parent(self): # real signature unknown; restored from __doc__
        """ get_index_in_parent(self) -> int """
        return 0

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atk.Layer """
        pass

    def get_mdi_zorder(self): # real signature unknown; restored from __doc__
        """ get_mdi_zorder(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_accessible_children(self): # real signature unknown; restored from __doc__
        """ get_n_accessible_children(self) -> int """
        return 0

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GObject.Object """
        pass

    def get_object_locale(self): # real signature unknown; restored from __doc__
        """ get_object_locale(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Atk.Object """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> Atk.Role """
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, data=None): # real signature unknown; restored from __doc__
        """ initialize(self, data=None) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Atk.Object """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_state_change(self, state, value): # real signature unknown; restored from __doc__
        """ notify_state_change(self, state:int, value:bool) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_parent(self): # real signature unknown; restored from __doc__
        """ peek_parent(self) -> Atk.Object """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_accessible_child(self, i): # real signature unknown; restored from __doc__
        """ ref_accessible_child(self, i:int) -> Atk.Object """
        pass

    def ref_relation_set(self): # real signature unknown; restored from __doc__
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_state_set(self): # real signature unknown; restored from __doc__
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def remove_property_change_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def remove_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ remove_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_accessible_id(self, name): # real signature unknown; restored from __doc__
        """ set_accessible_id(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Atk.Object) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:Atk.Role) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    accessible_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    relation_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffab9fcd310>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Root), '__module__': 'gi.repository.Cally', '__gtype__': <GType CallyRoot (94729765974160)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent': <property object at 0x7ffaba7f6b80>, 'priv': <property object at 0x7ffaba7f6cc0>})"
    __gdoc__ = 'Object CallyRoot\n\nSignals from AtkObject:\n  children-changed (guint, gpointer)\n  focus-event (gboolean)\n  property-change (gpointer)\n  state-change (gchararray, gboolean)\n  visible-data-changed ()\n  active-descendant-changed (gpointer)\n\nProperties from AtkObject:\n  accessible-name -> gchararray: Accessible Name\n    Object instance’s name formatted for assistive technology access\n  accessible-description -> gchararray: Accessible Description\n    Description of an object, formatted for assistive technology access\n  accessible-parent -> AtkObject: Accessible Parent\n    Parent of the current accessible as returned by atk_object_get_parent()\n  accessible-value -> gdouble: Accessible Value\n    Is used to notify that the value has changed\n  accessible-role -> AtkRole: Accessible Role\n    The accessible role of this object\n  accessible-component-layer -> gint: Accessible Layer\n    The accessible layer of this object\n  accessible-component-mdi-zorder -> gint: Accessible MDI Value\n    The accessible MDI value of this object\n  accessible-table-caption -> gchararray: Accessible Table Caption\n    Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead\n  accessible-table-column-description -> gchararray: Accessible Table Column Description\n    Is used to notify that the table column description has changed\n  accessible-table-column-header -> AtkObject: Accessible Table Column Header\n    Is used to notify that the table column header has changed\n  accessible-table-row-description -> gchararray: Accessible Table Row Description\n    Is used to notify that the table row description has changed\n  accessible-table-row-header -> AtkObject: Accessible Table Row Header\n    Is used to notify that the table row header has changed\n  accessible-table-summary -> AtkObject: Accessible Table Summary\n    Is used to notify that the table summary has changed\n  accessible-table-caption-object -> AtkObject: Accessible Table Caption Object\n    Is used to notify that the table caption has changed\n  accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links\n    The number of links which the current AtkHypertext has\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CallyRoot (94729765974160)>'
    __info__ = ObjectInfo(Root)


class RootClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        RootClass()
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RootClass), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RootClass' objects>, '__weakref__': <attribute '__weakref__' of 'RootClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ffaba7f6e50>, '_padding_dummy': <property object at 0x7ffaba7f6f40>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RootClass)


class RootPrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RootPrivate), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RootPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'RootPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RootPrivate)


class Stage(Group, __gi_repository_Atk.Window):
    """
    :Constructors:
    
    ::
    
        Stage(**properties)
        new(actor:Clutter.Actor) -> Atk.Object
    """
    def add_action(self, action_name, action_description, action_keybinding, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_action(self, action_name:str, action_description:str, action_keybinding:str, callback:Cally.ActionCallback, user_data=None) -> int """
        return 0

    def add_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ add_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_action(self, i): # real signature unknown; restored from __doc__
        """ do_action(self, i:int) -> bool """
        return False

    def do_active_descendant_changed(self, *args, **kwargs): # real signature unknown
        """ active_descendant_changed(self, child=None) """
        pass

    def do_children_changed(self, *args, **kwargs): # real signature unknown
        """ children_changed(self, change_index:int, changed_child=None) """
        pass

    def do_focus_event(self, *args, **kwargs): # real signature unknown
        """ focus_event(self, focus_in:bool) """
        pass

    def do_get_attributes(self, *args, **kwargs): # real signature unknown
        """ get_attributes(self) -> list """
        pass

    def do_get_description(self, *args, **kwargs): # real signature unknown
        """ get_description(self) -> str """
        pass

    def do_get_index_in_parent(self, *args, **kwargs): # real signature unknown
        """ get_index_in_parent(self) -> int """
        pass

    def do_get_layer(self, *args, **kwargs): # real signature unknown
        """ get_layer(self) -> Atk.Layer """
        pass

    def do_get_mdi_zorder(self, *args, **kwargs): # real signature unknown
        """ get_mdi_zorder(self) -> int """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_get_n_children(self, *args, **kwargs): # real signature unknown
        """ get_n_children(self) -> int """
        pass

    def do_get_object_locale(self, *args, **kwargs): # real signature unknown
        """ get_object_locale(self) -> str """
        pass

    def do_get_parent(self, *args, **kwargs): # real signature unknown
        """ get_parent(self) -> Atk.Object """
        pass

    def do_get_role(self, *args, **kwargs): # real signature unknown
        """ get_role(self) -> Atk.Role """
        pass

    def do_initialize(self, *args, **kwargs): # real signature unknown
        """ initialize(self, data=None) """
        pass

    def do_property_change(self, *args, **kwargs): # real signature unknown
        """ property_change(self, values:Atk.PropertyValues) """
        pass

    def do_ref_relation_set(self, *args, **kwargs): # real signature unknown
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def do_ref_state_set(self, *args, **kwargs): # real signature unknown
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def do_remove_property_change_handler(self, *args, **kwargs): # real signature unknown
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def do_set_description(self, *args, **kwargs): # real signature unknown
        """ set_description(self, description:str) """
        pass

    def do_set_name(self, *args, **kwargs): # real signature unknown
        """ set_name(self, name:str) """
        pass

    def do_set_parent(self, *args, **kwargs): # real signature unknown
        """ set_parent(self, parent:Atk.Object) """
        pass

    def do_set_role(self, *args, **kwargs): # real signature unknown
        """ set_role(self, role:Atk.Role) """
        pass

    def do_state_change(self, *args, **kwargs): # real signature unknown
        """ state_change(self, name:str, state_set:bool) """
        pass

    def do_visible_data_changed(self, *args, **kwargs): # real signature unknown
        """ visible_data_changed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def for_object(self, obj): # real signature unknown; restored from __doc__
        """ for_object(obj:GObject.Object) -> Atk.Object """
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accessible_id(self): # real signature unknown; restored from __doc__
        """ get_accessible_id(self) -> str """
        return ""

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_extents(self, coord_type): # real signature unknown; restored from __doc__
        """ get_extents(self, coord_type:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_index_in_parent(self): # real signature unknown; restored from __doc__
        """ get_index_in_parent(self) -> int """
        return 0

    def get_keybinding(self, i): # real signature unknown; restored from __doc__
        """ get_keybinding(self, i:int) -> str or None """
        return ""

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atk.Layer """
        pass

    def get_localized_name(self, i): # real signature unknown; restored from __doc__
        """ get_localized_name(self, i:int) -> str or None """
        return ""

    def get_mdi_zorder(self): # real signature unknown; restored from __doc__
        """ get_mdi_zorder(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_accessible_children(self): # real signature unknown; restored from __doc__
        """ get_n_accessible_children(self) -> int """
        return 0

    def get_n_actions(self): # real signature unknown; restored from __doc__
        """ get_n_actions(self) -> int """
        return 0

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GObject.Object """
        pass

    def get_object_locale(self): # real signature unknown; restored from __doc__
        """ get_object_locale(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Atk.Object """
        pass

    def get_position(self, coord_type): # real signature unknown; restored from __doc__
        """ get_position(self, coord_type:Atk.CoordType) -> x:int, y:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> Atk.Role """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:int, height:int """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
        return False

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, data=None): # real signature unknown; restored from __doc__
        """ initialize(self, data=None) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, actor): # real signature unknown; restored from __doc__
        """ new(actor:Clutter.Actor) -> Atk.Object """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_state_change(self, state, value): # real signature unknown; restored from __doc__
        """ notify_state_change(self, state:int, value:bool) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_parent(self): # real signature unknown; restored from __doc__
        """ peek_parent(self) -> Atk.Object """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_accessible_at_point(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ ref_accessible_at_point(self, x:int, y:int, coord_type:Atk.CoordType) -> Atk.Object or None """
        pass

    def ref_accessible_child(self, i): # real signature unknown; restored from __doc__
        """ ref_accessible_child(self, i:int) -> Atk.Object """
        pass

    def ref_relation_set(self): # real signature unknown; restored from __doc__
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_state_set(self): # real signature unknown; restored from __doc__
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def remove_action(self, action_id): # real signature unknown; restored from __doc__
        """ remove_action(self, action_id:int) -> bool """
        return False

    def remove_action_by_name(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action_by_name(self, action_name:str) -> bool """
        return False

    def remove_focus_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_focus_handler(self, handler_id:int) """
        pass

    def remove_property_change_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def remove_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ remove_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atk.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def set_accessible_id(self, name): # real signature unknown; restored from __doc__
        """ set_accessible_id(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_extents(self, x, y, width, height, coord_type): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Atk.Object) """
        pass

    def set_position(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:Atk.Role) """
        pass

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    accessible_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    relation_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffaba7d07f0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Stage), '__module__': 'gi.repository.Cally', '__gtype__': <GType CallyStage (94729765978416)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent': <property object at 0x7ffaba7fb270>, 'priv': <property object at 0x7ffaba7fb360>})"
    __gdoc__ = 'Object CallyStage\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkWindow:\n  activate ()\n  create ()\n  deactivate ()\n  destroy ()\n  maximize ()\n  minimize ()\n  move ()\n  resize ()\n  restore ()\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkObject:\n  children-changed (guint, gpointer)\n  focus-event (gboolean)\n  property-change (gpointer)\n  state-change (gchararray, gboolean)\n  visible-data-changed ()\n  active-descendant-changed (gpointer)\n\nProperties from AtkObject:\n  accessible-name -> gchararray: Accessible Name\n    Object instance’s name formatted for assistive technology access\n  accessible-description -> gchararray: Accessible Description\n    Description of an object, formatted for assistive technology access\n  accessible-parent -> AtkObject: Accessible Parent\n    Parent of the current accessible as returned by atk_object_get_parent()\n  accessible-value -> gdouble: Accessible Value\n    Is used to notify that the value has changed\n  accessible-role -> AtkRole: Accessible Role\n    The accessible role of this object\n  accessible-component-layer -> gint: Accessible Layer\n    The accessible layer of this object\n  accessible-component-mdi-zorder -> gint: Accessible MDI Value\n    The accessible MDI value of this object\n  accessible-table-caption -> gchararray: Accessible Table Caption\n    Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead\n  accessible-table-column-description -> gchararray: Accessible Table Column Description\n    Is used to notify that the table column description has changed\n  accessible-table-column-header -> AtkObject: Accessible Table Column Header\n    Is used to notify that the table column header has changed\n  accessible-table-row-description -> gchararray: Accessible Table Row Description\n    Is used to notify that the table row description has changed\n  accessible-table-row-header -> AtkObject: Accessible Table Row Header\n    Is used to notify that the table row header has changed\n  accessible-table-summary -> AtkObject: Accessible Table Summary\n    Is used to notify that the table summary has changed\n  accessible-table-caption-object -> AtkObject: Accessible Table Caption Object\n    Is used to notify that the table caption has changed\n  accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links\n    The number of links which the current AtkHypertext has\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CallyStage (94729765978416)>'
    __info__ = ObjectInfo(Stage)


class StageClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        StageClass()
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(StageClass), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'StageClass' objects>, '__weakref__': <attribute '__weakref__' of 'StageClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ffaba7fb4f0>, '_padding_dummy': <property object at 0x7ffaba7fb5e0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(StageClass)


class StagePrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(StagePrivate), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'StagePrivate' objects>, '__weakref__': <attribute '__weakref__' of 'StagePrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(StagePrivate)


class Text(Actor, __gi_repository_Atk.EditableText, __gi_repository_Atk.Text):
    """
    :Constructors:
    
    ::
    
        Text(**properties)
        new(actor:Clutter.Actor) -> Atk.Object
    """
    def add_action(self, action_name, action_description, action_keybinding, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_action(self, action_name:str, action_description:str, action_keybinding:str, callback:Cally.ActionCallback, user_data=None) -> int """
        return 0

    def add_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ add_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def add_selection(self, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ add_selection(self, start_offset:int, end_offset:int) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def copy_text(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ copy_text(self, start_pos:int, end_pos:int) """
        pass

    def cut_text(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ cut_text(self, start_pos:int, end_pos:int) """
        pass

    def delete_text(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ delete_text(self, start_pos:int, end_pos:int) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_action(self, i): # real signature unknown; restored from __doc__
        """ do_action(self, i:int) -> bool """
        return False

    def do_active_descendant_changed(self, *args, **kwargs): # real signature unknown
        """ active_descendant_changed(self, child=None) """
        pass

    def do_children_changed(self, *args, **kwargs): # real signature unknown
        """ children_changed(self, change_index:int, changed_child=None) """
        pass

    def do_focus_event(self, *args, **kwargs): # real signature unknown
        """ focus_event(self, focus_in:bool) """
        pass

    def do_get_attributes(self, *args, **kwargs): # real signature unknown
        """ get_attributes(self) -> list """
        pass

    def do_get_description(self, *args, **kwargs): # real signature unknown
        """ get_description(self) -> str """
        pass

    def do_get_index_in_parent(self, *args, **kwargs): # real signature unknown
        """ get_index_in_parent(self) -> int """
        pass

    def do_get_layer(self, *args, **kwargs): # real signature unknown
        """ get_layer(self) -> Atk.Layer """
        pass

    def do_get_mdi_zorder(self, *args, **kwargs): # real signature unknown
        """ get_mdi_zorder(self) -> int """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_get_n_children(self, *args, **kwargs): # real signature unknown
        """ get_n_children(self) -> int """
        pass

    def do_get_object_locale(self, *args, **kwargs): # real signature unknown
        """ get_object_locale(self) -> str """
        pass

    def do_get_parent(self, *args, **kwargs): # real signature unknown
        """ get_parent(self) -> Atk.Object """
        pass

    def do_get_role(self, *args, **kwargs): # real signature unknown
        """ get_role(self) -> Atk.Role """
        pass

    def do_initialize(self, *args, **kwargs): # real signature unknown
        """ initialize(self, data=None) """
        pass

    def do_property_change(self, *args, **kwargs): # real signature unknown
        """ property_change(self, values:Atk.PropertyValues) """
        pass

    def do_ref_relation_set(self, *args, **kwargs): # real signature unknown
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def do_ref_state_set(self, *args, **kwargs): # real signature unknown
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def do_remove_property_change_handler(self, *args, **kwargs): # real signature unknown
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def do_set_description(self, *args, **kwargs): # real signature unknown
        """ set_description(self, description:str) """
        pass

    def do_set_name(self, *args, **kwargs): # real signature unknown
        """ set_name(self, name:str) """
        pass

    def do_set_parent(self, *args, **kwargs): # real signature unknown
        """ set_parent(self, parent:Atk.Object) """
        pass

    def do_set_role(self, *args, **kwargs): # real signature unknown
        """ set_role(self, role:Atk.Role) """
        pass

    def do_state_change(self, *args, **kwargs): # real signature unknown
        """ state_change(self, name:str, state_set:bool) """
        pass

    def do_visible_data_changed(self, *args, **kwargs): # real signature unknown
        """ visible_data_changed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def for_object(self, obj): # real signature unknown; restored from __doc__
        """ for_object(obj:GObject.Object) -> Atk.Object """
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def free_ranges(self, ranges): # real signature unknown; restored from __doc__
        """ free_ranges(ranges:list) """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accessible_id(self): # real signature unknown; restored from __doc__
        """ get_accessible_id(self) -> str """
        return ""

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_bounded_ranges(self, rect, coord_type, x_clip_type, y_clip_type): # real signature unknown; restored from __doc__
        """ get_bounded_ranges(self, rect:Atk.TextRectangle, coord_type:Atk.CoordType, x_clip_type:Atk.TextClipType, y_clip_type:Atk.TextClipType) -> list """
        return []

    def get_caret_offset(self): # real signature unknown; restored from __doc__
        """ get_caret_offset(self) -> int """
        return 0

    def get_character_at_offset(self, offset): # real signature unknown; restored from __doc__
        """ get_character_at_offset(self, offset:int) -> str """
        return ""

    def get_character_count(self): # real signature unknown; restored from __doc__
        """ get_character_count(self) -> int """
        return 0

    def get_character_extents(self, offset, coords): # real signature unknown; restored from __doc__
        """ get_character_extents(self, offset:int, coords:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_attributes(self): # real signature unknown; restored from __doc__
        """ get_default_attributes(self) -> list """
        return []

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_extents(self, coord_type): # real signature unknown; restored from __doc__
        """ get_extents(self, coord_type:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_index_in_parent(self): # real signature unknown; restored from __doc__
        """ get_index_in_parent(self) -> int """
        return 0

    def get_keybinding(self, i): # real signature unknown; restored from __doc__
        """ get_keybinding(self, i:int) -> str or None """
        return ""

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atk.Layer """
        pass

    def get_localized_name(self, i): # real signature unknown; restored from __doc__
        """ get_localized_name(self, i:int) -> str or None """
        return ""

    def get_mdi_zorder(self): # real signature unknown; restored from __doc__
        """ get_mdi_zorder(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_accessible_children(self): # real signature unknown; restored from __doc__
        """ get_n_accessible_children(self) -> int """
        return 0

    def get_n_actions(self): # real signature unknown; restored from __doc__
        """ get_n_actions(self) -> int """
        return 0

    def get_n_selections(self): # real signature unknown; restored from __doc__
        """ get_n_selections(self) -> int """
        return 0

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GObject.Object """
        pass

    def get_object_locale(self): # real signature unknown; restored from __doc__
        """ get_object_locale(self) -> str """
        return ""

    def get_offset_at_point(self, x, y, coords): # real signature unknown; restored from __doc__
        """ get_offset_at_point(self, x:int, y:int, coords:Atk.CoordType) -> int """
        return 0

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Atk.Object """
        pass

    def get_position(self, coord_type): # real signature unknown; restored from __doc__
        """ get_position(self, coord_type:Atk.CoordType) -> x:int, y:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_range_extents(self, start_offset, end_offset, coord_type): # real signature unknown; restored from __doc__
        """ get_range_extents(self, start_offset:int, end_offset:int, coord_type:Atk.CoordType) -> rect:Atk.TextRectangle """
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> Atk.Role """
        pass

    def get_run_attributes(self, offset): # real signature unknown; restored from __doc__
        """ get_run_attributes(self, offset:int) -> list, start_offset:int, end_offset:int """
        return []

    def get_selection(self, selection_num): # real signature unknown; restored from __doc__
        """ get_selection(self, selection_num:int) -> str, start_offset:int, end_offset:int """
        return ""

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:int, height:int """
        pass

    def get_string_at_offset(self, offset, granularity): # real signature unknown; restored from __doc__
        """ get_string_at_offset(self, offset:int, granularity:Atk.TextGranularity) -> str or None, start_offset:int, end_offset:int """
        return ""

    def get_text(self, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ get_text(self, start_offset:int, end_offset:int) -> str """
        return ""

    def get_text_after_offset(self, offset, boundary_type): # real signature unknown; restored from __doc__
        """ get_text_after_offset(self, offset:int, boundary_type:Atk.TextBoundary) -> str, start_offset:int, end_offset:int """
        return ""

    def get_text_at_offset(self, offset, boundary_type): # real signature unknown; restored from __doc__
        """ get_text_at_offset(self, offset:int, boundary_type:Atk.TextBoundary) -> str, start_offset:int, end_offset:int """
        return ""

    def get_text_before_offset(self, offset, boundary_type): # real signature unknown; restored from __doc__
        """ get_text_before_offset(self, offset:int, boundary_type:Atk.TextBoundary) -> str, start_offset:int, end_offset:int """
        return ""

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
        return False

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, data=None): # real signature unknown; restored from __doc__
        """ initialize(self, data=None) """
        pass

    def insert_text(self, string, length, position): # real signature unknown; restored from __doc__
        """ insert_text(self, string:str, length:int, position:int) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, actor): # real signature unknown; restored from __doc__
        """ new(actor:Clutter.Actor) -> Atk.Object """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_state_change(self, state, value): # real signature unknown; restored from __doc__
        """ notify_state_change(self, state:int, value:bool) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def paste_text(self, position): # real signature unknown; restored from __doc__
        """ paste_text(self, position:int) """
        pass

    def peek_parent(self): # real signature unknown; restored from __doc__
        """ peek_parent(self) -> Atk.Object """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_accessible_at_point(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ ref_accessible_at_point(self, x:int, y:int, coord_type:Atk.CoordType) -> Atk.Object or None """
        pass

    def ref_accessible_child(self, i): # real signature unknown; restored from __doc__
        """ ref_accessible_child(self, i:int) -> Atk.Object """
        pass

    def ref_relation_set(self): # real signature unknown; restored from __doc__
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_state_set(self): # real signature unknown; restored from __doc__
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def remove_action(self, action_id): # real signature unknown; restored from __doc__
        """ remove_action(self, action_id:int) -> bool """
        return False

    def remove_action_by_name(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action_by_name(self, action_name:str) -> bool """
        return False

    def remove_focus_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_focus_handler(self, handler_id:int) """
        pass

    def remove_property_change_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def remove_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ remove_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def remove_selection(self, selection_num): # real signature unknown; restored from __doc__
        """ remove_selection(self, selection_num:int) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scroll_substring_to(self, start_offset, end_offset, type): # real signature unknown; restored from __doc__
        """ scroll_substring_to(self, start_offset:int, end_offset:int, type:Atk.ScrollType) -> bool """
        return False

    def scroll_substring_to_point(self, start_offset, end_offset, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_substring_to_point(self, start_offset:int, end_offset:int, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atk.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def set_accessible_id(self, name): # real signature unknown; restored from __doc__
        """ set_accessible_id(self, name:str) """
        pass

    def set_caret_offset(self, offset): # real signature unknown; restored from __doc__
        """ set_caret_offset(self, offset:int) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_extents(self, x, y, width, height, coord_type): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Atk.Object) """
        pass

    def set_position(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:Atk.Role) """
        pass

    def set_run_attributes(self, attrib_set, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ set_run_attributes(self, attrib_set:list, start_offset:int, end_offset:int) -> bool """
        return False

    def set_selection(self, selection_num, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ set_selection(self, selection_num:int, start_offset:int, end_offset:int) -> bool """
        return False

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
        return False

    def set_text_contents(self, string): # real signature unknown; restored from __doc__
        """ set_text_contents(self, string:str) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    accessible_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    relation_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffaba7c6580>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Text), '__module__': 'gi.repository.Cally', '__gtype__': <GType CallyText (94729765982960)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent': <property object at 0x7ffaba7fbf40>, 'priv': <property object at 0x7ffaba7fd090>})"
    __gdoc__ = 'Object CallyText\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkText:\n  text-changed (gint, gint)\n  text-insert (gint, gint, gchararray)\n  text-remove (gint, gint, gchararray)\n  text-caret-moved (gint)\n  text-selection-changed ()\n  text-attributes-changed ()\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkObject:\n  children-changed (guint, gpointer)\n  focus-event (gboolean)\n  property-change (gpointer)\n  state-change (gchararray, gboolean)\n  visible-data-changed ()\n  active-descendant-changed (gpointer)\n\nProperties from AtkObject:\n  accessible-name -> gchararray: Accessible Name\n    Object instance’s name formatted for assistive technology access\n  accessible-description -> gchararray: Accessible Description\n    Description of an object, formatted for assistive technology access\n  accessible-parent -> AtkObject: Accessible Parent\n    Parent of the current accessible as returned by atk_object_get_parent()\n  accessible-value -> gdouble: Accessible Value\n    Is used to notify that the value has changed\n  accessible-role -> AtkRole: Accessible Role\n    The accessible role of this object\n  accessible-component-layer -> gint: Accessible Layer\n    The accessible layer of this object\n  accessible-component-mdi-zorder -> gint: Accessible MDI Value\n    The accessible MDI value of this object\n  accessible-table-caption -> gchararray: Accessible Table Caption\n    Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead\n  accessible-table-column-description -> gchararray: Accessible Table Column Description\n    Is used to notify that the table column description has changed\n  accessible-table-column-header -> AtkObject: Accessible Table Column Header\n    Is used to notify that the table column header has changed\n  accessible-table-row-description -> gchararray: Accessible Table Row Description\n    Is used to notify that the table row description has changed\n  accessible-table-row-header -> AtkObject: Accessible Table Row Header\n    Is used to notify that the table row header has changed\n  accessible-table-summary -> AtkObject: Accessible Table Summary\n    Is used to notify that the table summary has changed\n  accessible-table-caption-object -> AtkObject: Accessible Table Caption Object\n    Is used to notify that the table caption has changed\n  accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links\n    The number of links which the current AtkHypertext has\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CallyText (94729765982960)>'
    __info__ = ObjectInfo(Text)


class TextClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TextClass()
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TextClass), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TextClass' objects>, '__weakref__': <attribute '__weakref__' of 'TextClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ffaba7fd220>, '_padding_dummy': <property object at 0x7ffaba7fd310>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TextClass)


class TextPrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TextPrivate), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TextPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'TextPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TextPrivate)


class Texture(Actor):
    """
    :Constructors:
    
    ::
    
        Texture(**properties)
        new(actor:Clutter.Actor) -> Atk.Object
    """
    def add_action(self, action_name, action_description, action_keybinding, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_action(self, action_name:str, action_description:str, action_keybinding:str, callback:Cally.ActionCallback, user_data=None) -> int """
        return 0

    def add_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ add_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_action(self, i): # real signature unknown; restored from __doc__
        """ do_action(self, i:int) -> bool """
        return False

    def do_active_descendant_changed(self, *args, **kwargs): # real signature unknown
        """ active_descendant_changed(self, child=None) """
        pass

    def do_children_changed(self, *args, **kwargs): # real signature unknown
        """ children_changed(self, change_index:int, changed_child=None) """
        pass

    def do_focus_event(self, *args, **kwargs): # real signature unknown
        """ focus_event(self, focus_in:bool) """
        pass

    def do_get_attributes(self, *args, **kwargs): # real signature unknown
        """ get_attributes(self) -> list """
        pass

    def do_get_description(self, *args, **kwargs): # real signature unknown
        """ get_description(self) -> str """
        pass

    def do_get_index_in_parent(self, *args, **kwargs): # real signature unknown
        """ get_index_in_parent(self) -> int """
        pass

    def do_get_layer(self, *args, **kwargs): # real signature unknown
        """ get_layer(self) -> Atk.Layer """
        pass

    def do_get_mdi_zorder(self, *args, **kwargs): # real signature unknown
        """ get_mdi_zorder(self) -> int """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_get_n_children(self, *args, **kwargs): # real signature unknown
        """ get_n_children(self) -> int """
        pass

    def do_get_object_locale(self, *args, **kwargs): # real signature unknown
        """ get_object_locale(self) -> str """
        pass

    def do_get_parent(self, *args, **kwargs): # real signature unknown
        """ get_parent(self) -> Atk.Object """
        pass

    def do_get_role(self, *args, **kwargs): # real signature unknown
        """ get_role(self) -> Atk.Role """
        pass

    def do_initialize(self, *args, **kwargs): # real signature unknown
        """ initialize(self, data=None) """
        pass

    def do_property_change(self, *args, **kwargs): # real signature unknown
        """ property_change(self, values:Atk.PropertyValues) """
        pass

    def do_ref_relation_set(self, *args, **kwargs): # real signature unknown
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def do_ref_state_set(self, *args, **kwargs): # real signature unknown
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def do_remove_property_change_handler(self, *args, **kwargs): # real signature unknown
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def do_set_description(self, *args, **kwargs): # real signature unknown
        """ set_description(self, description:str) """
        pass

    def do_set_name(self, *args, **kwargs): # real signature unknown
        """ set_name(self, name:str) """
        pass

    def do_set_parent(self, *args, **kwargs): # real signature unknown
        """ set_parent(self, parent:Atk.Object) """
        pass

    def do_set_role(self, *args, **kwargs): # real signature unknown
        """ set_role(self, role:Atk.Role) """
        pass

    def do_state_change(self, *args, **kwargs): # real signature unknown
        """ state_change(self, name:str, state_set:bool) """
        pass

    def do_visible_data_changed(self, *args, **kwargs): # real signature unknown
        """ visible_data_changed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def for_object(self, obj): # real signature unknown; restored from __doc__
        """ for_object(obj:GObject.Object) -> Atk.Object """
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accessible_id(self): # real signature unknown; restored from __doc__
        """ get_accessible_id(self) -> str """
        return ""

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_extents(self, coord_type): # real signature unknown; restored from __doc__
        """ get_extents(self, coord_type:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_index_in_parent(self): # real signature unknown; restored from __doc__
        """ get_index_in_parent(self) -> int """
        return 0

    def get_keybinding(self, i): # real signature unknown; restored from __doc__
        """ get_keybinding(self, i:int) -> str or None """
        return ""

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atk.Layer """
        pass

    def get_localized_name(self, i): # real signature unknown; restored from __doc__
        """ get_localized_name(self, i:int) -> str or None """
        return ""

    def get_mdi_zorder(self): # real signature unknown; restored from __doc__
        """ get_mdi_zorder(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_accessible_children(self): # real signature unknown; restored from __doc__
        """ get_n_accessible_children(self) -> int """
        return 0

    def get_n_actions(self): # real signature unknown; restored from __doc__
        """ get_n_actions(self) -> int """
        return 0

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GObject.Object """
        pass

    def get_object_locale(self): # real signature unknown; restored from __doc__
        """ get_object_locale(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Atk.Object """
        pass

    def get_position(self, coord_type): # real signature unknown; restored from __doc__
        """ get_position(self, coord_type:Atk.CoordType) -> x:int, y:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> Atk.Role """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:int, height:int """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
        return False

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, data=None): # real signature unknown; restored from __doc__
        """ initialize(self, data=None) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, actor): # real signature unknown; restored from __doc__
        """ new(actor:Clutter.Actor) -> Atk.Object """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_state_change(self, state, value): # real signature unknown; restored from __doc__
        """ notify_state_change(self, state:int, value:bool) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_parent(self): # real signature unknown; restored from __doc__
        """ peek_parent(self) -> Atk.Object """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_accessible_at_point(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ ref_accessible_at_point(self, x:int, y:int, coord_type:Atk.CoordType) -> Atk.Object or None """
        pass

    def ref_accessible_child(self, i): # real signature unknown; restored from __doc__
        """ ref_accessible_child(self, i:int) -> Atk.Object """
        pass

    def ref_relation_set(self): # real signature unknown; restored from __doc__
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_state_set(self): # real signature unknown; restored from __doc__
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def remove_action(self, action_id): # real signature unknown; restored from __doc__
        """ remove_action(self, action_id:int) -> bool """
        return False

    def remove_action_by_name(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action_by_name(self, action_name:str) -> bool """
        return False

    def remove_focus_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_focus_handler(self, handler_id:int) """
        pass

    def remove_property_change_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def remove_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ remove_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atk.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def set_accessible_id(self, name): # real signature unknown; restored from __doc__
        """ set_accessible_id(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_extents(self, x, y, width, height, coord_type): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Atk.Object) """
        pass

    def set_position(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:Atk.Role) """
        pass

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    accessible_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    relation_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffab9fcd9d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Texture), '__module__': 'gi.repository.Cally', '__gtype__': <GType CallyTexture (94729766010384)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent': <property object at 0x7ffaba7fd4f0>, 'priv': <property object at 0x7ffaba7fd630>})"
    __gdoc__ = 'Object CallyTexture\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkObject:\n  children-changed (guint, gpointer)\n  focus-event (gboolean)\n  property-change (gpointer)\n  state-change (gchararray, gboolean)\n  visible-data-changed ()\n  active-descendant-changed (gpointer)\n\nProperties from AtkObject:\n  accessible-name -> gchararray: Accessible Name\n    Object instance’s name formatted for assistive technology access\n  accessible-description -> gchararray: Accessible Description\n    Description of an object, formatted for assistive technology access\n  accessible-parent -> AtkObject: Accessible Parent\n    Parent of the current accessible as returned by atk_object_get_parent()\n  accessible-value -> gdouble: Accessible Value\n    Is used to notify that the value has changed\n  accessible-role -> AtkRole: Accessible Role\n    The accessible role of this object\n  accessible-component-layer -> gint: Accessible Layer\n    The accessible layer of this object\n  accessible-component-mdi-zorder -> gint: Accessible MDI Value\n    The accessible MDI value of this object\n  accessible-table-caption -> gchararray: Accessible Table Caption\n    Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead\n  accessible-table-column-description -> gchararray: Accessible Table Column Description\n    Is used to notify that the table column description has changed\n  accessible-table-column-header -> AtkObject: Accessible Table Column Header\n    Is used to notify that the table column header has changed\n  accessible-table-row-description -> gchararray: Accessible Table Row Description\n    Is used to notify that the table row description has changed\n  accessible-table-row-header -> AtkObject: Accessible Table Row Header\n    Is used to notify that the table row header has changed\n  accessible-table-summary -> AtkObject: Accessible Table Summary\n    Is used to notify that the table summary has changed\n  accessible-table-caption-object -> AtkObject: Accessible Table Caption Object\n    Is used to notify that the table caption has changed\n  accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links\n    The number of links which the current AtkHypertext has\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CallyTexture (94729766010384)>'
    __info__ = ObjectInfo(Texture)


class TextureClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TextureClass()
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TextureClass), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TextureClass' objects>, '__weakref__': <attribute '__weakref__' of 'TextureClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ffaba7fd7c0>, '_padding_dummy': <property object at 0x7ffaba7fd8b0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TextureClass)


class TexturePrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TexturePrivate), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TexturePrivate' objects>, '__weakref__': <attribute '__weakref__' of 'TexturePrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TexturePrivate)


class Util(__gi_repository_Atk.Util):
    """
    :Constructors:
    
    ::
    
        Util(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffab9f81700>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Util), '__module__': 'gi.repository.Cally', '__gtype__': <GType CallyUtil (94729766014992)>, '__doc__': None, '__gsignals__': {}, 'parent': <property object at 0x7ffaba7fdc70>, 'priv': <property object at 0x7ffaba7fdd60>})"
    __gdoc__ = 'Object CallyUtil\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CallyUtil (94729766014992)>'
    __info__ = ObjectInfo(Util)


class UtilClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        UtilClass()
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(UtilClass), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'UtilClass' objects>, '__weakref__': <attribute '__weakref__' of 'UtilClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ffaba7fdef0>, '_padding_dummy': <property object at 0x7ffab9fbc040>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(UtilClass)


class UtilPrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(UtilPrivate), '__module__': 'gi.repository.Cally', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'UtilPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'UtilPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(UtilPrivate)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7ffabac791f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7ffabac79280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7ffabac79310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7ffabac793a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7ffabb8b5d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Cally-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Cally', loader=<gi.importer.DynamicImporter object at 0x7ffabb8b5d00>)"

