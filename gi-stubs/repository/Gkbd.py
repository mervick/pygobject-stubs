# encoding: utf-8
# module gi.repository.Gkbd
# from /usr/lib64/girepository-1.0/Gkbd-3.0.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


# Variables with simple values

DESKTOP_SCHEMA = 'org.gnome.libgnomekbd.desktop'

KEYBOARD_DRAWING_H = 1

KEYBOARD_SCHEMA = 'org.gnome.libgnomekbd.keyboard'

_namespace = 'Gkbd'

_version = '3.0'

__weakref__ = None

# functions

def install_glib_log_appender(): # real signature unknown; restored from __doc__
    """ install_glib_log_appender() """
    pass

def keyboard_config_add_default_switch_option_if_necessary(layouts_list, options_list, was_appended): # real signature unknown; restored from __doc__
    """ keyboard_config_add_default_switch_option_if_necessary(layouts_list:str, options_list:str, was_appended:bool) -> list """
    return []

def keyboard_config_format_full_description(layout_descr, variant_descr): # real signature unknown; restored from __doc__
    """ keyboard_config_format_full_description(layout_descr:str, variant_descr:str) -> str """
    return ""

def keyboard_config_get_descriptions(config_registry, name, layout_short_descr, layout_descr, variant_short_descr, variant_descr): # real signature unknown; restored from __doc__
    """ keyboard_config_get_descriptions(config_registry:Xkl.ConfigRegistry, name:str, layout_short_descr:str, layout_descr:str, variant_short_descr:str, variant_descr:str) -> bool """
    return False

def keyboard_config_merge_items(parent, child): # real signature unknown; restored from __doc__
    """ keyboard_config_merge_items(parent:str, child:str) -> str """
    return ""

def keyboard_config_split_items(merged, parent, child): # real signature unknown; restored from __doc__
    """ keyboard_config_split_items(merged:str, parent:str, child:str) -> bool """
    return False

def preview_load_position(): # real signature unknown; restored from __doc__
    """ preview_load_position() -> Gdk.Rectangle """
    pass

def preview_save_position(rect): # real signature unknown; restored from __doc__
    """ preview_save_position(rect:Gdk.Rectangle) """
    pass

def strv_append(arr, element): # real signature unknown; restored from __doc__
    """ strv_append(arr:str, element:str) -> list """
    return []

def strv_behead(arr): # real signature unknown; restored from __doc__
    """ strv_behead(arr:str) """
    pass

def strv_remove(arr, element): # real signature unknown; restored from __doc__
    """ strv_remove(arr:str, element:str) -> bool """
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

class Configuration(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Configuration(**properties)
    """
    def append_object(self, obj): # real signature unknown; restored from __doc__
        """ append_object(self, obj:GObject.Object) """
        pass

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

    def create_label_title(self, group, ln2cnt_map, layout_name): # real signature unknown; restored from __doc__
        """ create_label_title(group:int, ln2cnt_map:dict, layout_name:str) -> str """
        return ""

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

    def extract_layout_name(self, group): # real signature unknown; restored from __doc__
        """ extract_layout_name(self, group:int) -> str """
        return ""

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

    def free_images(self, images): # real signature unknown; restored from __doc__
        """ free_images(self, images:list) """
        pass

    def get(self): # real signature unknown; restored from __doc__
        """ get() -> Gkbd.Configuration """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_all_objects(self): # real signature unknown; restored from __doc__
        """ get_all_objects(self) -> list """
        return []

    def get_caps_lock_state(self): # real signature unknown; restored from __doc__
        """ get_caps_lock_state(self) -> bool """
        return False

    def get_current_group(self): # real signature unknown; restored from __doc__
        """ get_current_group(self) -> int """
        return 0

    def get_current_tooltip(self): # real signature unknown; restored from __doc__
        """ get_current_tooltip(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_group_name(self, group): # real signature unknown; restored from __doc__
        """ get_group_name(self, group:int) -> str """
        return ""

    def get_group_names(self): # real signature unknown; restored from __doc__
        """ get_group_names(self) -> list """
        return []

    def get_image_filename(self, group): # real signature unknown; restored from __doc__
        """ get_image_filename(self, group:int) -> str """
        return ""

    def get_indicator_config(self): # real signature unknown; restored from __doc__
        """ get_indicator_config(self) -> Gkbd.IndicatorConfig """
        pass

    def get_keyboard_config(self): # real signature unknown; restored from __doc__
        """ get_keyboard_config(self) -> Gkbd.KeyboardConfig """
        pass

    def get_num_lock_state(self): # real signature unknown; restored from __doc__
        """ get_num_lock_state(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_scroll_lock_state(self): # real signature unknown; restored from __doc__
        """ get_scroll_lock_state(self) -> bool """
        return False

    def get_short_group_names(self): # real signature unknown; restored from __doc__
        """ get_short_group_names(self) -> list """
        return []

    def get_xkl_engine(self): # real signature unknown; restored from __doc__
        """ get_xkl_engine(self) -> Xkl.Engine """
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

    def if_any_object_exists(self): # real signature unknown; restored from __doc__
        """ if_any_object_exists(self) -> bool """
        return False

    def if_flags_shown(self): # real signature unknown; restored from __doc__
        """ if_flags_shown(self) -> bool """
        return False

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

    def load_images(self): # real signature unknown; restored from __doc__
        """ load_images(self) -> list """
        return []

    def lock_group(self, group): # real signature unknown; restored from __doc__
        """ lock_group(self, group:int) """
        pass

    def lock_next_group(self): # real signature unknown; restored from __doc__
        """ lock_next_group(self) """
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

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_object(self, obj): # real signature unknown; restored from __doc__
        """ remove_object(self, obj:GObject.Object) """
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

    def start_listen(self): # real signature unknown; restored from __doc__
        """ start_listen(self) """
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

    def stop_listen(self): # real signature unknown; restored from __doc__
        """ stop_listen(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb17320c190>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Configuration), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType GkbdConfiguration (94195347565584)>, '__doc__': None, '__gsignals__': {}, 'create_label_title': gi.FunctionInfo(create_label_title), 'get': gi.FunctionInfo(get), 'append_object': gi.FunctionInfo(append_object), 'extract_layout_name': gi.FunctionInfo(extract_layout_name), 'free_images': gi.FunctionInfo(free_images), 'get_all_objects': gi.FunctionInfo(get_all_objects), 'get_caps_lock_state': gi.FunctionInfo(get_caps_lock_state), 'get_current_group': gi.FunctionInfo(get_current_group), 'get_current_tooltip': gi.FunctionInfo(get_current_tooltip), 'get_group_name': gi.FunctionInfo(get_group_name), 'get_group_names': gi.FunctionInfo(get_group_names), 'get_image_filename': gi.FunctionInfo(get_image_filename), 'get_indicator_config': gi.FunctionInfo(get_indicator_config), 'get_keyboard_config': gi.FunctionInfo(get_keyboard_config), 'get_num_lock_state': gi.FunctionInfo(get_num_lock_state), 'get_scroll_lock_state': gi.FunctionInfo(get_scroll_lock_state), 'get_short_group_names': gi.FunctionInfo(get_short_group_names), 'get_xkl_engine': gi.FunctionInfo(get_xkl_engine), 'if_any_object_exists': gi.FunctionInfo(if_any_object_exists), 'if_flags_shown': gi.FunctionInfo(if_flags_shown), 'load_images': gi.FunctionInfo(load_images), 'lock_group': gi.FunctionInfo(lock_group), 'lock_next_group': gi.FunctionInfo(lock_next_group), 'remove_object': gi.FunctionInfo(remove_object), 'start_listen': gi.FunctionInfo(start_listen), 'stop_listen': gi.FunctionInfo(stop_listen), 'parent': <property object at 0x7fb173265860>, 'priv': <property object at 0x7fb1732658b0>})"
    __gdoc__ = 'Object GkbdConfiguration\n\nSignals from GkbdConfiguration:\n  changed ()\n  group-changed (gint)\n  indicators-changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GkbdConfiguration (94195347565584)>'
    __info__ = ObjectInfo(Configuration)


class ConfigurationClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ConfigurationClass()
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


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ConfigurationClass), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ConfigurationClass' objects>, '__weakref__': <attribute '__weakref__' of 'ConfigurationClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fb1732659a0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ConfigurationClass)


class ConfigurationPrivate(__gi.Struct):
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ConfigurationPrivate), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ConfigurationPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'ConfigurationPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ConfigurationPrivate)


class DesktopConfig(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DesktopConfig()
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def init(self, engine): # real signature unknown; restored from __doc__
        """ init(self, engine:Xkl.Engine) """
        pass

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) """
        pass

    def load_group_descriptions(self, registry, layout_ids, variant_ids, short_group_names, full_group_names): # real signature unknown; restored from __doc__
        """ load_group_descriptions(self, registry:Xkl.ConfigRegistry, layout_ids:str, variant_ids:str, short_group_names:str, full_group_names:str) -> bool """
        return False

    def lock_next_group(self): # real signature unknown; restored from __doc__
        """ lock_next_group(self) """
        pass

    def lock_prev_group(self): # real signature unknown; restored from __doc__
        """ lock_prev_group(self) """
        pass

    def restore_group(self): # real signature unknown; restored from __doc__
        """ restore_group(self) """
        pass

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) """
        pass

    def start_listen(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ start_listen(self, func:GObject.Callback, user_data=None) """
        pass

    def stop_listen(self): # real signature unknown; restored from __doc__
        """ stop_listen(self) """
        pass

    def term(self): # real signature unknown; restored from __doc__
        """ term(self) """
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

    config_listener_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    engine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    group_per_app = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_indicators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layout_names_as_group_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    load_extra_items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DesktopConfig), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DesktopConfig' objects>, '__weakref__': <attribute '__weakref__' of 'DesktopConfig' objects>, '__doc__': None, 'default_group': <property object at 0x7fb173265b80>, 'group_per_app': <property object at 0x7fb173265c70>, 'handle_indicators': <property object at 0x7fb173265db0>, 'layout_names_as_group_names': <property object at 0x7fb173265ef0>, 'load_extra_items': <property object at 0x7fb1731b5090>, 'settings': <property object at 0x7fb1731b5180>, 'config_listener_id': <property object at 0x7fb1731b52c0>, 'engine': <property object at 0x7fb1731b53b0>, 'activate': gi.FunctionInfo(activate), 'init': gi.FunctionInfo(init), 'load': gi.FunctionInfo(load), 'load_group_descriptions': gi.FunctionInfo(load_group_descriptions), 'lock_next_group': gi.FunctionInfo(lock_next_group), 'lock_prev_group': gi.FunctionInfo(lock_prev_group), 'restore_group': gi.FunctionInfo(restore_group), 'save': gi.FunctionInfo(save), 'start_listen': gi.FunctionInfo(start_listen), 'stop_listen': gi.FunctionInfo(stop_listen), 'term': gi.FunctionInfo(term)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DesktopConfig)


class Indicator(__gi_repository_Gtk.Notebook):
    """
    :Constructors:
    
    ::
    
        Indicator(**properties)
        new() -> Gtk.Widget
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def add(self, widget): # real signature unknown; restored from __doc__
        """ add(self, widget:Gtk.Widget) """
        pass

    def add_accelerator(self, accel_signal, accel_group, accel_key, accel_mods, accel_flags): # real signature unknown; restored from __doc__
        """ add_accelerator(self, accel_signal:str, accel_group:Gtk.AccelGroup, accel_key:int, accel_mods:Gdk.ModifierType, accel_flags:Gtk.AccelFlags) """
        pass

    def add_child(self, builder, child, type=None): # real signature unknown; restored from __doc__
        """ add_child(self, builder:Gtk.Builder, child:GObject.Object, type:str=None) """
        pass

    def add_device_events(self, device, events): # real signature unknown; restored from __doc__
        """ add_device_events(self, device:Gdk.Device, events:Gdk.EventMask) """
        pass

    def add_events(self, events): # real signature unknown; restored from __doc__
        """ add_events(self, events:int) """
        pass

    def add_mnemonic_label(self, label): # real signature unknown; restored from __doc__
        """ add_mnemonic_label(self, label:Gtk.Widget) """
        pass

    def add_tick_callback(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_tick_callback(self, callback:Gtk.TickCallback, user_data=None) -> int """
        return 0

    def append_page(self, child, tab_label=None): # real signature unknown; restored from __doc__
        """ append_page(self, child:Gtk.Widget, tab_label:Gtk.Widget=None) -> int """
        return 0

    def append_page_menu(self, child, tab_label=None, menu_label=None): # real signature unknown; restored from __doc__
        """ append_page_menu(self, child:Gtk.Widget, tab_label:Gtk.Widget=None, menu_label:Gtk.Widget=None) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def bind_template_callback_full(self, callback_name, callback_symbol): # real signature unknown; restored from __doc__
        """ bind_template_callback_full(self, callback_name:str, callback_symbol:GObject.Callback) """
        pass

    def bind_template_child_full(self, name, internal_child, struct_offset): # real signature unknown; restored from __doc__
        """ bind_template_child_full(self, name:str, internal_child:bool, struct_offset:int) """
        pass

    def can_activate_accel(self, signal_id): # real signature unknown; restored from __doc__
        """ can_activate_accel(self, signal_id:int) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_resize(self): # real signature unknown; restored from __doc__
        """ check_resize(self) """
        pass

    def child_focus(self, direction): # real signature unknown; restored from __doc__
        """ child_focus(self, direction:Gtk.DirectionType) -> bool """
        return False

    def child_get(self, child, *prop_names): # reliably restored by inspect
        """ Returns a list of child property values for the given names. """
        pass

    def child_get_property(self, child, property_name, value=None): # reliably restored by inspect
        # no doc
        pass

    def child_notify(self, child, child_property): # real signature unknown; restored from __doc__
        """ child_notify(self, child:Gtk.Widget, child_property:str) """
        pass

    def child_notify_by_pspec(self, child, pspec): # real signature unknown; restored from __doc__
        """ child_notify_by_pspec(self, child:Gtk.Widget, pspec:GObject.ParamSpec) """
        pass

    def child_set(self, child, **kwargs): # reliably restored by inspect
        """ Set a child properties on the given child to key/value pairs. """
        pass

    def child_set_property(self, child, property_name, value): # real signature unknown; restored from __doc__
        """ child_set_property(self, child:Gtk.Widget, property_name:str, value:GObject.Value) """
        pass

    def child_type(self): # real signature unknown; restored from __doc__
        """ child_type(self) -> GType """
        pass

    def class_path(self): # real signature unknown; restored from __doc__
        """ class_path(self) -> path_length:int, path:str, path_reversed:str """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def compute_expand(self, orientation): # real signature unknown; restored from __doc__
        """ compute_expand(self, orientation:Gtk.Orientation) -> bool """
        return False

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

    def construct_child(self, builder, name): # real signature unknown; restored from __doc__
        """ construct_child(self, builder:Gtk.Builder, name:str) -> GObject.Object """
        pass

    def create_pango_context(self): # real signature unknown; restored from __doc__
        """ create_pango_context(self) -> Pango.Context """
        pass

    def create_pango_layout(self, text=None): # real signature unknown; restored from __doc__
        """ create_pango_layout(self, text:str=None) -> Pango.Layout """
        pass

    def custom_finished(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_finished(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_end(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_tag_end(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_start(self, builder, child=None, tagname): # real signature unknown; restored from __doc__
        """ custom_tag_start(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str) -> bool, parser:GLib.MarkupParser, data """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def destroyed(self, widget_pointer): # real signature unknown; restored from __doc__
        """ destroyed(self, widget_pointer:Gtk.Widget) -> widget_pointer:Gtk.Widget """
        pass

    def detach_tab(self, child): # real signature unknown; restored from __doc__
        """ detach_tab(self, child:Gtk.Widget) """
        pass

    def device_is_shadowed(self, device): # real signature unknown; restored from __doc__
        """ device_is_shadowed(self, device:Gdk.Device) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_add(self, *args, **kwargs): # real signature unknown
        """ add(self, widget:Gtk.Widget) """
        pass

    def do_adjust_baseline_allocation(self, *args, **kwargs): # real signature unknown
        """ adjust_baseline_allocation(self, baseline:int) """
        pass

    def do_adjust_baseline_request(self, *args, **kwargs): # real signature unknown
        """ adjust_baseline_request(self, minimum_baseline:int, natural_baseline:int) """
        pass

    def do_adjust_size_allocation(self, *args, **kwargs): # real signature unknown
        """ adjust_size_allocation(self, orientation:Gtk.Orientation, minimum_size:int, natural_size:int, allocated_pos:int, allocated_size:int) """
        pass

    def do_adjust_size_request(self, *args, **kwargs): # real signature unknown
        """ adjust_size_request(self, orientation:Gtk.Orientation, minimum_size:int, natural_size:int) """
        pass

    def do_button_press_event(self, *args, **kwargs): # real signature unknown
        """ button_press_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_button_release_event(self, *args, **kwargs): # real signature unknown
        """ button_release_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_can_activate_accel(self, *args, **kwargs): # real signature unknown
        """ can_activate_accel(self, signal_id:int) -> bool """
        pass

    def do_change_current_page(self, *args, **kwargs): # real signature unknown
        """ change_current_page(self, offset:int) -> bool """
        pass

    def do_check_resize(self, *args, **kwargs): # real signature unknown
        """ check_resize(self) """
        pass

    def do_child_notify(self, *args, **kwargs): # real signature unknown
        """ child_notify(self, child_property:GObject.ParamSpec) """
        pass

    def do_child_type(self, *args, **kwargs): # real signature unknown
        """ child_type(self) -> GType """
        pass

    def do_composited_changed(self, *args, **kwargs): # real signature unknown
        """ composited_changed(self) """
        pass

    def do_composite_name(self, *args, **kwargs): # real signature unknown
        """ composite_name(self, child:Gtk.Widget) -> str """
        pass

    def do_compute_expand(self, *args, **kwargs): # real signature unknown
        """ compute_expand(self, hexpand_p:bool, vexpand_p:bool) """
        pass

    def do_configure_event(self, *args, **kwargs): # real signature unknown
        """ configure_event(self, event:Gdk.EventConfigure) -> bool """
        pass

    def do_damage_event(self, *args, **kwargs): # real signature unknown
        """ damage_event(self, event:Gdk.EventExpose) -> bool """
        pass

    def do_delete_event(self, *args, **kwargs): # real signature unknown
        """ delete_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_destroy(self, *args, **kwargs): # real signature unknown
        """ destroy(self) """
        pass

    def do_destroy_event(self, *args, **kwargs): # real signature unknown
        """ destroy_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_direction_changed(self, *args, **kwargs): # real signature unknown
        """ direction_changed(self, previous_direction:Gtk.TextDirection) """
        pass

    def do_dispatch_child_properties_changed(self, *args, **kwargs): # real signature unknown
        """ dispatch_child_properties_changed(self, n_pspecs:int, pspecs:GObject.ParamSpec) """
        pass

    def do_drag_begin(self, *args, **kwargs): # real signature unknown
        """ drag_begin(self, context:Gdk.DragContext) """
        pass

    def do_drag_data_delete(self, *args, **kwargs): # real signature unknown
        """ drag_data_delete(self, context:Gdk.DragContext) """
        pass

    def do_drag_data_get(self, *args, **kwargs): # real signature unknown
        """ drag_data_get(self, context:Gdk.DragContext, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_drag_data_received(self, *args, **kwargs): # real signature unknown
        """ drag_data_received(self, context:Gdk.DragContext, x:int, y:int, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_drag_drop(self, *args, **kwargs): # real signature unknown
        """ drag_drop(self, context:Gdk.DragContext, x:int, y:int, time_:int) -> bool """
        pass

    def do_drag_end(self, *args, **kwargs): # real signature unknown
        """ drag_end(self, context:Gdk.DragContext) """
        pass

    def do_drag_failed(self, *args, **kwargs): # real signature unknown
        """ drag_failed(self, context:Gdk.DragContext, result:Gtk.DragResult) -> bool """
        pass

    def do_drag_leave(self, *args, **kwargs): # real signature unknown
        """ drag_leave(self, context:Gdk.DragContext, time_:int) """
        pass

    def do_drag_motion(self, *args, **kwargs): # real signature unknown
        """ drag_motion(self, context:Gdk.DragContext, x:int, y:int, time_:int) -> bool """
        pass

    def do_draw(self, *args, **kwargs): # real signature unknown
        """ draw(self, cr:cairo.Context) -> bool """
        pass

    def do_enter_notify_event(self, *args, **kwargs): # real signature unknown
        """ enter_notify_event(self, event:Gdk.EventCrossing) -> bool """
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event:Gdk.Event) -> bool """
        pass

    def do_focus(self, *args, **kwargs): # real signature unknown
        """ focus(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_focus_in_event(self, *args, **kwargs): # real signature unknown
        """ focus_in_event(self, event:Gdk.EventFocus) -> bool """
        pass

    def do_focus_out_event(self, *args, **kwargs): # real signature unknown
        """ focus_out_event(self, event:Gdk.EventFocus) -> bool """
        pass

    def do_focus_tab(self, *args, **kwargs): # real signature unknown
        """ focus_tab(self, type:Gtk.NotebookTab) -> bool """
        pass

    def do_forall(self, *args, **kwargs): # real signature unknown
        """ forall(self, include_internals:bool, callback:Gtk.Callback, callback_data=None) """
        pass

    def do_get_accessible(self, *args, **kwargs): # real signature unknown
        """ get_accessible(self) -> Atk.Object """
        pass

    def do_get_child_property(self, *args, **kwargs): # real signature unknown
        """ get_child_property(self, child:Gtk.Widget, property_id:int, value:GObject.Value, pspec:GObject.ParamSpec) """
        pass

    def do_get_path_for_child(self, *args, **kwargs): # real signature unknown
        """ get_path_for_child(self, child:Gtk.Widget) -> Gtk.WidgetPath """
        pass

    def do_get_preferred_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height(self) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_height_and_baseline_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_and_baseline_for_width(self, width:int) -> minimum_height:int, natural_height:int, minimum_baseline:int, natural_baseline:int """
        pass

    def do_get_preferred_height_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_for_width(self, width:int) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width(self) -> minimum_width:int, natural_width:int """
        pass

    def do_get_preferred_width_for_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width_for_height(self, height:int) -> minimum_width:int, natural_width:int """
        pass

    def do_get_request_mode(self, *args, **kwargs): # real signature unknown
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def do_grab_broken_event(self, *args, **kwargs): # real signature unknown
        """ grab_broken_event(self, event:Gdk.EventGrabBroken) -> bool """
        pass

    def do_grab_focus(self, *args, **kwargs): # real signature unknown
        """ grab_focus(self) """
        pass

    def do_grab_notify(self, *args, **kwargs): # real signature unknown
        """ grab_notify(self, was_grabbed:bool) """
        pass

    def do_hide(self, *args, **kwargs): # real signature unknown
        """ hide(self) """
        pass

    def do_hierarchy_changed(self, *args, **kwargs): # real signature unknown
        """ hierarchy_changed(self, previous_toplevel:Gtk.Widget) """
        pass

    def do_insert_page(self, *args, **kwargs): # real signature unknown
        """ insert_page(self, child:Gtk.Widget, tab_label:Gtk.Widget, menu_label:Gtk.Widget, position:int) -> int """
        pass

    def do_keynav_failed(self, *args, **kwargs): # real signature unknown
        """ keynav_failed(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_key_press_event(self, *args, **kwargs): # real signature unknown
        """ key_press_event(self, event:Gdk.EventKey) -> bool """
        pass

    def do_key_release_event(self, *args, **kwargs): # real signature unknown
        """ key_release_event(self, event:Gdk.EventKey) -> bool """
        pass

    def do_leave_notify_event(self, *args, **kwargs): # real signature unknown
        """ leave_notify_event(self, event:Gdk.EventCrossing) -> bool """
        pass

    def do_map(self, *args, **kwargs): # real signature unknown
        """ map(self) """
        pass

    def do_map_event(self, *args, **kwargs): # real signature unknown
        """ map_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_mnemonic_activate(self, *args, **kwargs): # real signature unknown
        """ mnemonic_activate(self, group_cycling:bool) -> bool """
        pass

    def do_motion_notify_event(self, *args, **kwargs): # real signature unknown
        """ motion_notify_event(self, event:Gdk.EventMotion) -> bool """
        pass

    def do_move_focus(self, *args, **kwargs): # real signature unknown
        """ move_focus(self, direction:Gtk.DirectionType) """
        pass

    def do_move_focus_out(self, *args, **kwargs): # real signature unknown
        """ move_focus_out(self, direction:Gtk.DirectionType) """
        pass

    def do_page_added(self, *args, **kwargs): # real signature unknown
        """ page_added(self, child:Gtk.Widget, page_num:int) """
        pass

    def do_page_removed(self, *args, **kwargs): # real signature unknown
        """ page_removed(self, child:Gtk.Widget, page_num:int) """
        pass

    def do_page_reordered(self, *args, **kwargs): # real signature unknown
        """ page_reordered(self, child:Gtk.Widget, page_num:int) """
        pass

    def do_parent_set(self, *args, **kwargs): # real signature unknown
        """ parent_set(self, previous_parent:Gtk.Widget) """
        pass

    def do_popup_menu(self, *args, **kwargs): # real signature unknown
        """ popup_menu(self) -> bool """
        pass

    def do_property_notify_event(self, *args, **kwargs): # real signature unknown
        """ property_notify_event(self, event:Gdk.EventProperty) -> bool """
        pass

    def do_proximity_in_event(self, *args, **kwargs): # real signature unknown
        """ proximity_in_event(self, event:Gdk.EventProximity) -> bool """
        pass

    def do_proximity_out_event(self, *args, **kwargs): # real signature unknown
        """ proximity_out_event(self, event:Gdk.EventProximity) -> bool """
        pass

    def do_query_tooltip(self, *args, **kwargs): # real signature unknown
        """ query_tooltip(self, x:int, y:int, keyboard_tooltip:bool, tooltip:Gtk.Tooltip) -> bool """
        pass

    def do_queue_draw_region(self, *args, **kwargs): # real signature unknown
        """ queue_draw_region(self, region:cairo.Region) """
        pass

    def do_realize(self, *args, **kwargs): # real signature unknown
        """ realize(self) """
        pass

    def do_reinit_ui(self, *args, **kwargs): # real signature unknown
        """ reinit_ui(self) """
        pass

    def do_remove(self, *args, **kwargs): # real signature unknown
        """ remove(self, widget:Gtk.Widget) """
        pass

    def do_reorder_tab(self, *args, **kwargs): # real signature unknown
        """ reorder_tab(self, direction:Gtk.DirectionType, move_to_last:bool) -> bool """
        pass

    def do_screen_changed(self, *args, **kwargs): # real signature unknown
        """ screen_changed(self, previous_screen:Gdk.Screen) """
        pass

    def do_scroll_event(self, *args, **kwargs): # real signature unknown
        """ scroll_event(self, event:Gdk.EventScroll) -> bool """
        pass

    def do_selection_clear_event(self, *args, **kwargs): # real signature unknown
        """ selection_clear_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_selection_get(self, *args, **kwargs): # real signature unknown
        """ selection_get(self, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_selection_notify_event(self, *args, **kwargs): # real signature unknown
        """ selection_notify_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_selection_received(self, *args, **kwargs): # real signature unknown
        """ selection_received(self, selection_data:Gtk.SelectionData, time_:int) """
        pass

    def do_selection_request_event(self, *args, **kwargs): # real signature unknown
        """ selection_request_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_select_page(self, *args, **kwargs): # real signature unknown
        """ select_page(self, move_focus:bool) -> bool """
        pass

    def do_set_child_property(self, *args, **kwargs): # real signature unknown
        """ set_child_property(self, child:Gtk.Widget, property_id:int, value:GObject.Value, pspec:GObject.ParamSpec) """
        pass

    def do_set_focus_child(self, *args, **kwargs): # real signature unknown
        """ set_focus_child(self, child:Gtk.Widget=None) """
        pass

    def do_show(self, *args, **kwargs): # real signature unknown
        """ show(self) """
        pass

    def do_show_all(self, *args, **kwargs): # real signature unknown
        """ show_all(self) """
        pass

    def do_show_help(self, *args, **kwargs): # real signature unknown
        """ show_help(self, help_type:Gtk.WidgetHelpType) -> bool """
        pass

    def do_size_allocate(self, *args, **kwargs): # real signature unknown
        """ size_allocate(self, allocation:Gdk.Rectangle) """
        pass

    def do_state_changed(self, *args, **kwargs): # real signature unknown
        """ state_changed(self, previous_state:Gtk.StateType) """
        pass

    def do_state_flags_changed(self, *args, **kwargs): # real signature unknown
        """ state_flags_changed(self, previous_state_flags:Gtk.StateFlags) """
        pass

    def do_style_set(self, *args, **kwargs): # real signature unknown
        """ style_set(self, previous_style:Gtk.Style) """
        pass

    def do_style_updated(self, *args, **kwargs): # real signature unknown
        """ style_updated(self) """
        pass

    def do_switch_page(self, *args, **kwargs): # real signature unknown
        """ switch_page(self, page:Gtk.Widget, page_num:int) """
        pass

    def do_touch_event(self, *args, **kwargs): # real signature unknown
        """ touch_event(self, event:Gdk.EventTouch) -> bool """
        pass

    def do_unmap(self, *args, **kwargs): # real signature unknown
        """ unmap(self) """
        pass

    def do_unmap_event(self, *args, **kwargs): # real signature unknown
        """ unmap_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_unrealize(self, *args, **kwargs): # real signature unknown
        """ unrealize(self) """
        pass

    def do_visibility_notify_event(self, *args, **kwargs): # real signature unknown
        """ visibility_notify_event(self, event:Gdk.EventVisibility) -> bool """
        pass

    def do_window_state_event(self, *args, **kwargs): # real signature unknown
        """ window_state_event(self, event:Gdk.EventWindowState) -> bool """
        pass

    def drag_begin(self, targets, actions, button, event=None): # real signature unknown; restored from __doc__
        """ drag_begin(self, targets:Gtk.TargetList, actions:Gdk.DragAction, button:int, event:Gdk.Event=None) -> Gdk.DragContext """
        pass

    def drag_begin_with_coordinates(self, targets, actions, button, event=None, x, y): # real signature unknown; restored from __doc__
        """ drag_begin_with_coordinates(self, targets:Gtk.TargetList, actions:Gdk.DragAction, button:int, event:Gdk.Event=None, x:int, y:int) -> Gdk.DragContext """
        pass

    def drag_check_threshold(self, start_x, start_y, current_x, current_y): # real signature unknown; restored from __doc__
        """ drag_check_threshold(self, start_x:int, start_y:int, current_x:int, current_y:int) -> bool """
        return False

    def drag_dest_add_image_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_image_targets(self) """
        pass

    def drag_dest_add_text_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_text_targets(self) """
        pass

    def drag_dest_add_uri_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_uri_targets(self) """
        pass

    def drag_dest_find_target(self, context, target_list=None): # real signature unknown; restored from __doc__
        """ drag_dest_find_target(self, context:Gdk.DragContext, target_list:Gtk.TargetList=None) -> Gdk.Atom """
        pass

    def drag_dest_get_target_list(self): # real signature unknown; restored from __doc__
        """ drag_dest_get_target_list(self) -> Gtk.TargetList or None """
        pass

    def drag_dest_get_track_motion(self): # real signature unknown; restored from __doc__
        """ drag_dest_get_track_motion(self) -> bool """
        return False

    def drag_dest_set(self, flags, targets=None, actions): # real signature unknown; restored from __doc__
        """ drag_dest_set(self, flags:Gtk.DestDefaults, targets:list=None, actions:Gdk.DragAction) """
        pass

    def drag_dest_set_proxy(self, proxy_window, protocol, use_coordinates): # real signature unknown; restored from __doc__
        """ drag_dest_set_proxy(self, proxy_window:Gdk.Window, protocol:Gdk.DragProtocol, use_coordinates:bool) """
        pass

    def drag_dest_set_target_list(self, target_list): # reliably restored by inspect
        # no doc
        pass

    def drag_dest_set_track_motion(self, track_motion): # real signature unknown; restored from __doc__
        """ drag_dest_set_track_motion(self, track_motion:bool) """
        pass

    def drag_dest_unset(self): # real signature unknown; restored from __doc__
        """ drag_dest_unset(self) """
        pass

    def drag_get_data(self, context, target, time_): # real signature unknown; restored from __doc__
        """ drag_get_data(self, context:Gdk.DragContext, target:Gdk.Atom, time_:int) """
        pass

    def drag_highlight(self): # real signature unknown; restored from __doc__
        """ drag_highlight(self) """
        pass

    def drag_source_add_image_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_image_targets(self) """
        pass

    def drag_source_add_text_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_text_targets(self) """
        pass

    def drag_source_add_uri_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_uri_targets(self) """
        pass

    def drag_source_get_target_list(self): # real signature unknown; restored from __doc__
        """ drag_source_get_target_list(self) -> Gtk.TargetList or None """
        pass

    def drag_source_set(self, start_button_mask, targets=None, actions): # real signature unknown; restored from __doc__
        """ drag_source_set(self, start_button_mask:Gdk.ModifierType, targets:list=None, actions:Gdk.DragAction) """
        pass

    def drag_source_set_icon_gicon(self, icon): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_gicon(self, icon:Gio.Icon) """
        pass

    def drag_source_set_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_name(self, icon_name:str) """
        pass

    def drag_source_set_icon_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf) """
        pass

    def drag_source_set_icon_stock(self, stock_id): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_stock(self, stock_id:str) """
        pass

    def drag_source_set_target_list(self, target_list): # reliably restored by inspect
        # no doc
        pass

    def drag_source_unset(self): # real signature unknown; restored from __doc__
        """ drag_source_unset(self) """
        pass

    def drag_unhighlight(self): # real signature unknown; restored from __doc__
        """ drag_unhighlight(self) """
        pass

    def draw(self, cr): # real signature unknown; restored from __doc__
        """ draw(self, cr:cairo.Context) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_style(self): # real signature unknown; restored from __doc__
        """ ensure_style(self) """
        pass

    def error_bell(self): # real signature unknown; restored from __doc__
        """ error_bell(self) """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event:Gdk.Event) -> bool """
        return False

    def find_child_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_child_property(self, property_name:str) -> GObject.ParamSpec or None """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_style_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_style_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def forall(self, callback, callback_data=None): # real signature unknown; restored from __doc__
        """ forall(self, callback:Gtk.Callback, callback_data=None) """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, callback, callback_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, callback:Gtk.Callback, callback_data=None) """
        pass

    def freeze_child_notify(self): # reliably restored by inspect
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

    def get_accessible(self): # real signature unknown; restored from __doc__
        """ get_accessible(self) -> Atk.Object """
        pass

    def get_action_group(self, prefix): # real signature unknown; restored from __doc__
        """ get_action_group(self, prefix:str) -> Gio.ActionGroup or None """
        pass

    def get_action_widget(self, pack_type): # real signature unknown; restored from __doc__
        """ get_action_widget(self, pack_type:Gtk.PackType) -> Gtk.Widget or None """
        pass

    def get_allocated_baseline(self): # real signature unknown; restored from __doc__
        """ get_allocated_baseline(self) -> int """
        return 0

    def get_allocated_height(self): # real signature unknown; restored from __doc__
        """ get_allocated_height(self) -> int """
        return 0

    def get_allocated_size(self): # real signature unknown; restored from __doc__
        """ get_allocated_size(self) -> allocation:Gdk.Rectangle, baseline:int """
        pass

    def get_allocated_width(self): # real signature unknown; restored from __doc__
        """ get_allocated_width(self) -> int """
        return 0

    def get_allocation(self): # real signature unknown; restored from __doc__
        """ get_allocation(self) -> allocation:Gdk.Rectangle """
        pass

    def get_ancestor(self, widget_type): # real signature unknown; restored from __doc__
        """ get_ancestor(self, widget_type:GType) -> Gtk.Widget or None """
        pass

    def get_app_paintable(self): # real signature unknown; restored from __doc__
        """ get_app_paintable(self) -> bool """
        return False

    def get_border_width(self): # real signature unknown; restored from __doc__
        """ get_border_width(self) -> int """
        return 0

    def get_can_default(self): # real signature unknown; restored from __doc__
        """ get_can_default(self) -> bool """
        return False

    def get_can_focus(self): # real signature unknown; restored from __doc__
        """ get_can_focus(self) -> bool """
        return False

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_child_requisition(self): # real signature unknown; restored from __doc__
        """ get_child_requisition(self) -> requisition:Gtk.Requisition """
        pass

    def get_child_visible(self): # real signature unknown; restored from __doc__
        """ get_child_visible(self) -> bool """
        return False

    def get_clip(self): # real signature unknown; restored from __doc__
        """ get_clip(self) -> clip:Gdk.Rectangle """
        pass

    def get_clipboard(self, selection): # real signature unknown; restored from __doc__
        """ get_clipboard(self, selection:Gdk.Atom) -> Gtk.Clipboard """
        pass

    def get_composite_name(self): # real signature unknown; restored from __doc__
        """ get_composite_name(self) -> str """
        return ""

    def get_css_name(self): # real signature unknown; restored from __doc__
        """ get_css_name(self) -> str """
        return ""

    def get_current_page(self): # real signature unknown; restored from __doc__
        """ get_current_page(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_direction(self): # real signature unknown; restored from __doc__
        """ get_default_direction() -> Gtk.TextDirection """
        pass

    def get_default_style(self): # real signature unknown; restored from __doc__
        """ get_default_style() -> Gtk.Style """
        pass

    def get_device_enabled(self, device): # real signature unknown; restored from __doc__
        """ get_device_enabled(self, device:Gdk.Device) -> bool """
        return False

    def get_device_events(self, device): # real signature unknown; restored from __doc__
        """ get_device_events(self, device:Gdk.Device) -> Gdk.EventMask """
        pass

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> Gtk.TextDirection """
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> Gdk.Display """
        pass

    def get_double_buffered(self): # real signature unknown; restored from __doc__
        """ get_double_buffered(self) -> bool """
        return False

    def get_events(self): # real signature unknown; restored from __doc__
        """ get_events(self) -> int """
        return 0

    def get_focus_chain(*args, **kwargs): # reliably restored by inspect
        """ get_focus_chain(self) -> bool, focusable_widgets:list """
        pass

    def get_focus_child(self): # real signature unknown; restored from __doc__
        """ get_focus_child(self) -> Gtk.Widget or None """
        pass

    def get_focus_hadjustment(self): # real signature unknown; restored from __doc__
        """ get_focus_hadjustment(self) -> Gtk.Adjustment or None """
        pass

    def get_focus_on_click(self): # real signature unknown; restored from __doc__
        """ get_focus_on_click(self) -> bool """
        return False

    def get_focus_vadjustment(self): # real signature unknown; restored from __doc__
        """ get_focus_vadjustment(self) -> Gtk.Adjustment or None """
        pass

    def get_font_map(self): # real signature unknown; restored from __doc__
        """ get_font_map(self) -> Pango.FontMap or None """
        pass

    def get_font_options(self): # real signature unknown; restored from __doc__
        """ get_font_options(self) -> cairo.FontOptions or None """
        pass

    def get_frame_clock(self): # real signature unknown; restored from __doc__
        """ get_frame_clock(self) -> Gdk.FrameClock or None """
        pass

    def get_group_name(self): # real signature unknown; restored from __doc__
        """ get_group_name(self) -> str or None """
        return ""

    def get_group_names(self): # real signature unknown; restored from __doc__
        """ get_group_names() -> list """
        return []

    def get_halign(self): # real signature unknown; restored from __doc__
        """ get_halign(self) -> Gtk.Align """
        pass

    def get_has_tooltip(self): # real signature unknown; restored from __doc__
        """ get_has_tooltip(self) -> bool """
        return False

    def get_has_window(self): # real signature unknown; restored from __doc__
        """ get_has_window(self) -> bool """
        return False

    def get_hexpand(self): # real signature unknown; restored from __doc__
        """ get_hexpand(self) -> bool """
        return False

    def get_hexpand_set(self): # real signature unknown; restored from __doc__
        """ get_hexpand_set(self) -> bool """
        return False

    def get_image_filename(self, group): # real signature unknown; restored from __doc__
        """ get_image_filename(group:int) -> str """
        return ""

    def get_internal_child(self, builder, childname): # real signature unknown; restored from __doc__
        """ get_internal_child(self, builder:Gtk.Builder, childname:str) -> GObject.Object """
        pass

    def get_mapped(self): # real signature unknown; restored from __doc__
        """ get_mapped(self) -> bool """
        return False

    def get_margin_bottom(self): # real signature unknown; restored from __doc__
        """ get_margin_bottom(self) -> int """
        return 0

    def get_margin_end(self): # real signature unknown; restored from __doc__
        """ get_margin_end(self) -> int """
        return 0

    def get_margin_left(self): # real signature unknown; restored from __doc__
        """ get_margin_left(self) -> int """
        return 0

    def get_margin_right(self): # real signature unknown; restored from __doc__
        """ get_margin_right(self) -> int """
        return 0

    def get_margin_start(self): # real signature unknown; restored from __doc__
        """ get_margin_start(self) -> int """
        return 0

    def get_margin_top(self): # real signature unknown; restored from __doc__
        """ get_margin_top(self) -> int """
        return 0

    def get_max_width_height_ratio(self): # real signature unknown; restored from __doc__
        """ get_max_width_height_ratio() -> float """
        return 0.0

    def get_menu_label(self, child): # real signature unknown; restored from __doc__
        """ get_menu_label(self, child:Gtk.Widget) -> Gtk.Widget or None """
        pass

    def get_menu_label_text(self, child): # real signature unknown; restored from __doc__
        """ get_menu_label_text(self, child:Gtk.Widget) -> str or None """
        return ""

    def get_modifier_mask(self, intent): # real signature unknown; restored from __doc__
        """ get_modifier_mask(self, intent:Gdk.ModifierIntent) -> Gdk.ModifierType """
        pass

    def get_modifier_style(self): # real signature unknown; restored from __doc__
        """ get_modifier_style(self) -> Gtk.RcStyle """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_no_show_all(self): # real signature unknown; restored from __doc__
        """ get_no_show_all(self) -> bool """
        return False

    def get_nth_page(self, page_num): # real signature unknown; restored from __doc__
        """ get_nth_page(self, page_num:int) -> Gtk.Widget or None """
        pass

    def get_n_pages(self): # real signature unknown; restored from __doc__
        """ get_n_pages(self) -> int """
        return 0

    def get_opacity(self): # real signature unknown; restored from __doc__
        """ get_opacity(self) -> float """
        return 0.0

    def get_pango_context(self): # real signature unknown; restored from __doc__
        """ get_pango_context(self) -> Pango.Context """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gtk.Widget or None """
        pass

    def get_parent_window(self): # real signature unknown; restored from __doc__
        """ get_parent_window(self) -> Gdk.Window or None """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gtk.WidgetPath """
        pass

    def get_path_for_child(self, child): # real signature unknown; restored from __doc__
        """ get_path_for_child(self, child:Gtk.Widget) -> Gtk.WidgetPath """
        pass

    def get_pointer(self): # real signature unknown; restored from __doc__
        """ get_pointer(self) -> x:int, y:int """
        pass

    def get_preferred_height(self): # real signature unknown; restored from __doc__
        """ get_preferred_height(self) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_height_and_baseline_for_width(self, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_and_baseline_for_width(self, width:int) -> minimum_height:int, natural_height:int, minimum_baseline:int, natural_baseline:int """
        pass

    def get_preferred_height_for_width(self, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_for_width(self, width:int) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_size(self): # real signature unknown; restored from __doc__
        """ get_preferred_size(self) -> minimum_size:Gtk.Requisition, natural_size:Gtk.Requisition """
        pass

    def get_preferred_width(self): # real signature unknown; restored from __doc__
        """ get_preferred_width(self) -> minimum_width:int, natural_width:int """
        pass

    def get_preferred_width_for_height(self, height): # real signature unknown; restored from __doc__
        """ get_preferred_width_for_height(self, height:int) -> minimum_width:int, natural_width:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_realized(self): # real signature unknown; restored from __doc__
        """ get_realized(self) -> bool """
        return False

    def get_receives_default(self): # real signature unknown; restored from __doc__
        """ get_receives_default(self) -> bool """
        return False

    def get_request_mode(self): # real signature unknown; restored from __doc__
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def get_requisition(self): # real signature unknown; restored from __doc__
        """ get_requisition(self) -> requisition:Gtk.Requisition """
        pass

    def get_resize_mode(self): # real signature unknown; restored from __doc__
        """ get_resize_mode(self) -> Gtk.ResizeMode """
        pass

    def get_root_window(self): # real signature unknown; restored from __doc__
        """ get_root_window(self) -> Gdk.Window """
        pass

    def get_scale_factor(self): # real signature unknown; restored from __doc__
        """ get_scale_factor(self) -> int """
        return 0

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_scrollable(self): # real signature unknown; restored from __doc__
        """ get_scrollable(self) -> bool """
        return False

    def get_sensitive(self): # real signature unknown; restored from __doc__
        """ get_sensitive(self) -> bool """
        return False

    def get_settings(self): # real signature unknown; restored from __doc__
        """ get_settings(self) -> Gtk.Settings """
        pass

    def get_show_border(self): # real signature unknown; restored from __doc__
        """ get_show_border(self) -> bool """
        return False

    def get_show_tabs(self): # real signature unknown; restored from __doc__
        """ get_show_tabs(self) -> bool """
        return False

    def get_size_request(self): # real signature unknown; restored from __doc__
        """ get_size_request(self) -> width:int, height:int """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Gtk.StateType """
        pass

    def get_state_flags(self): # real signature unknown; restored from __doc__
        """ get_state_flags(self) -> Gtk.StateFlags """
        pass

    def get_style(self): # real signature unknown; restored from __doc__
        """ get_style(self) -> Gtk.Style """
        pass

    def get_style_context(self): # real signature unknown; restored from __doc__
        """ get_style_context(self) -> Gtk.StyleContext """
        pass

    def get_support_multidevice(self): # real signature unknown; restored from __doc__
        """ get_support_multidevice(self) -> bool """
        return False

    def get_tab_detachable(self, child): # real signature unknown; restored from __doc__
        """ get_tab_detachable(self, child:Gtk.Widget) -> bool """
        return False

    def get_tab_hborder(self): # real signature unknown; restored from __doc__
        """ get_tab_hborder(self) -> int """
        return 0

    def get_tab_label(self, child): # real signature unknown; restored from __doc__
        """ get_tab_label(self, child:Gtk.Widget) -> Gtk.Widget or None """
        pass

    def get_tab_label_text(self, child): # real signature unknown; restored from __doc__
        """ get_tab_label_text(self, child:Gtk.Widget) -> str or None """
        return ""

    def get_tab_pos(self): # real signature unknown; restored from __doc__
        """ get_tab_pos(self) -> Gtk.PositionType """
        pass

    def get_tab_reorderable(self, child): # real signature unknown; restored from __doc__
        """ get_tab_reorderable(self, child:Gtk.Widget) -> bool """
        return False

    def get_tab_vborder(self): # real signature unknown; restored from __doc__
        """ get_tab_vborder(self) -> int """
        return 0

    def get_template_child(self, widget_type, name): # real signature unknown; restored from __doc__
        """ get_template_child(self, widget_type:GType, name:str) -> GObject.Object """
        pass

    def get_tooltip_markup(self): # real signature unknown; restored from __doc__
        """ get_tooltip_markup(self) -> str or None """
        return ""

    def get_tooltip_text(self): # real signature unknown; restored from __doc__
        """ get_tooltip_text(self) -> str or None """
        return ""

    def get_tooltip_window(self): # real signature unknown; restored from __doc__
        """ get_tooltip_window(self) -> Gtk.Window """
        pass

    def get_toplevel(self): # real signature unknown; restored from __doc__
        """ get_toplevel(self) -> Gtk.Widget """
        pass

    def get_valign(self): # real signature unknown; restored from __doc__
        """ get_valign(self) -> Gtk.Align """
        pass

    def get_valign_with_baseline(self): # real signature unknown; restored from __doc__
        """ get_valign_with_baseline(self) -> Gtk.Align """
        pass

    def get_vexpand(self): # real signature unknown; restored from __doc__
        """ get_vexpand(self) -> bool """
        return False

    def get_vexpand_set(self): # real signature unknown; restored from __doc__
        """ get_vexpand_set(self) -> bool """
        return False

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

    def get_visual(self): # real signature unknown; restored from __doc__
        """ get_visual(self) -> Gdk.Visual """
        pass

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> Gdk.Window or None """
        pass

    def get_xkl_engine(self): # real signature unknown; restored from __doc__
        """ get_xkl_engine() -> Xkl.Engine """
        pass

    def grab_add(self): # real signature unknown; restored from __doc__
        """ grab_add(self) """
        pass

    def grab_default(self): # real signature unknown; restored from __doc__
        """ grab_default(self) """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) """
        pass

    def grab_remove(self): # real signature unknown; restored from __doc__
        """ grab_remove(self) """
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

    def handle_border_width(self): # real signature unknown; restored from __doc__
        """ handle_border_width(self) """
        pass

    def has_default(self): # real signature unknown; restored from __doc__
        """ has_default(self) -> bool """
        return False

    def has_focus(self): # real signature unknown; restored from __doc__
        """ has_focus(self) -> bool """
        return False

    def has_grab(self): # real signature unknown; restored from __doc__
        """ has_grab(self) -> bool """
        return False

    def has_rc_style(self): # real signature unknown; restored from __doc__
        """ has_rc_style(self) -> bool """
        return False

    def has_screen(self): # real signature unknown; restored from __doc__
        """ has_screen(self) -> bool """
        return False

    def has_visible_focus(self): # real signature unknown; restored from __doc__
        """ has_visible_focus(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hide_on_delete(self): # real signature unknown; restored from __doc__
        """ hide_on_delete(self) -> bool """
        return False

    def init_template(self): # real signature unknown; restored from __doc__
        """ init_template(self) """
        pass

    def input_shape_combine_region(self, region=None): # real signature unknown; restored from __doc__
        """ input_shape_combine_region(self, region:cairo.Region=None) """
        pass

    def insert_action_group(self, name, group=None): # real signature unknown; restored from __doc__
        """ insert_action_group(self, name:str, group:Gio.ActionGroup=None) """
        pass

    def insert_page(self, child, tab_label=None, position): # real signature unknown; restored from __doc__
        """ insert_page(self, child:Gtk.Widget, tab_label:Gtk.Widget=None, position:int) -> int """
        return 0

    def insert_page_menu(self, child, tab_label=None, menu_label=None, position): # real signature unknown; restored from __doc__
        """ insert_page_menu(self, child:Gtk.Widget, tab_label:Gtk.Widget=None, menu_label:Gtk.Widget=None, position:int) -> int """
        return 0

    def install_child_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_child_properties(self, pspecs:list) """
        pass

    def install_child_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_child_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_style_property(self, pspec): # real signature unknown; restored from __doc__
        """ install_style_property(self, pspec:GObject.ParamSpec) """
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

    def intersect(self, area): # real signature unknown; restored from __doc__
        """ intersect(self, area:Gdk.Rectangle) -> bool, intersection:Gdk.Rectangle """
        return False

    def in_destruction(self): # real signature unknown; restored from __doc__
        """ in_destruction(self) -> bool """
        return False

    def is_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ is_ancestor(self, ancestor:Gtk.Widget) -> bool """
        return False

    def is_composited(self): # real signature unknown; restored from __doc__
        """ is_composited(self) -> bool """
        return False

    def is_drawable(self): # real signature unknown; restored from __doc__
        """ is_drawable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_focus(self): # real signature unknown; restored from __doc__
        """ is_focus(self) -> bool """
        return False

    def is_sensitive(self): # real signature unknown; restored from __doc__
        """ is_sensitive(self) -> bool """
        return False

    def is_toplevel(self): # real signature unknown; restored from __doc__
        """ is_toplevel(self) -> bool """
        return False

    def is_visible(self): # real signature unknown; restored from __doc__
        """ is_visible(self) -> bool """
        return False

    def keynav_failed(self, direction): # real signature unknown; restored from __doc__
        """ keynav_failed(self, direction:Gtk.DirectionType) -> bool """
        return False

    def list_accel_closures(self): # real signature unknown; restored from __doc__
        """ list_accel_closures(self) -> list """
        return []

    def list_action_prefixes(self): # real signature unknown; restored from __doc__
        """ list_action_prefixes(self) -> list """
        return []

    def list_child_properties(self): # real signature unknown; restored from __doc__
        """ list_child_properties(self) -> list, n_properties:int """
        return []

    def list_mnemonic_labels(self): # real signature unknown; restored from __doc__
        """ list_mnemonic_labels(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_style_properties(self): # real signature unknown; restored from __doc__
        """ list_style_properties(self) -> list, n_properties:int """
        return []

    def map(self): # real signature unknown; restored from __doc__
        """ map(self) """
        pass

    def mnemonic_activate(self, group_cycling): # real signature unknown; restored from __doc__
        """ mnemonic_activate(self, group_cycling:bool) -> bool """
        return False

    def modify_base(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_base(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_bg(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_bg(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_cursor(self, primary=None, secondary=None): # real signature unknown; restored from __doc__
        """ modify_cursor(self, primary:Gdk.Color=None, secondary:Gdk.Color=None) """
        pass

    def modify_fg(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_fg(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_font(self, font_desc=None): # real signature unknown; restored from __doc__
        """ modify_font(self, font_desc:Pango.FontDescription=None) """
        pass

    def modify_style(self, style): # real signature unknown; restored from __doc__
        """ modify_style(self, style:Gtk.RcStyle) """
        pass

    def modify_text(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_text(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gtk.Widget """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def next_page(self): # real signature unknown; restored from __doc__
        """ next_page(self) """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_background_color(self, state, color=None): # real signature unknown; restored from __doc__
        """ override_background_color(self, state:Gtk.StateFlags, color:Gdk.RGBA=None) """
        pass

    def override_color(self, state, color=None): # real signature unknown; restored from __doc__
        """ override_color(self, state:Gtk.StateFlags, color:Gdk.RGBA=None) """
        pass

    def override_cursor(self, cursor=None, secondary_cursor=None): # real signature unknown; restored from __doc__
        """ override_cursor(self, cursor:Gdk.RGBA=None, secondary_cursor:Gdk.RGBA=None) """
        pass

    def override_font(self, font_desc=None): # real signature unknown; restored from __doc__
        """ override_font(self, font_desc:Pango.FontDescription=None) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def override_symbolic_color(self, name, color=None): # real signature unknown; restored from __doc__
        """ override_symbolic_color(self, name:str, color:Gdk.RGBA=None) """
        pass

    def page_num(self, child): # real signature unknown; restored from __doc__
        """ page_num(self, child:Gtk.Widget) -> int """
        return 0

    def parser_finished(self, builder): # real signature unknown; restored from __doc__
        """ parser_finished(self, builder:Gtk.Builder) """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> path_length:int, path:str, path_reversed:str """
        pass

    def popup_disable(self): # real signature unknown; restored from __doc__
        """ popup_disable(self) """
        pass

    def popup_enable(self): # real signature unknown; restored from __doc__
        """ popup_enable(self) """
        pass

    def pop_composite_child(self): # real signature unknown; restored from __doc__
        """ pop_composite_child() """
        pass

    def prepend_page(self, child, tab_label=None): # real signature unknown; restored from __doc__
        """ prepend_page(self, child:Gtk.Widget, tab_label:Gtk.Widget=None) -> int """
        return 0

    def prepend_page_menu(self, child, tab_label=None, menu_label=None): # real signature unknown; restored from __doc__
        """ prepend_page_menu(self, child:Gtk.Widget, tab_label:Gtk.Widget=None, menu_label:Gtk.Widget=None) -> int """
        return 0

    def prev_page(self): # real signature unknown; restored from __doc__
        """ prev_page(self) """
        pass

    def propagate_draw(self, child, cr): # real signature unknown; restored from __doc__
        """ propagate_draw(self, child:Gtk.Widget, cr:cairo.Context) """
        pass

    def push_composite_child(self): # real signature unknown; restored from __doc__
        """ push_composite_child() """
        pass

    def queue_allocate(self): # real signature unknown; restored from __doc__
        """ queue_allocate(self) """
        pass

    def queue_compute_expand(self): # real signature unknown; restored from __doc__
        """ queue_compute_expand(self) """
        pass

    def queue_draw(self): # real signature unknown; restored from __doc__
        """ queue_draw(self) """
        pass

    def queue_draw_area(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ queue_draw_area(self, x:int, y:int, width:int, height:int) """
        pass

    def queue_draw_region(self, region): # real signature unknown; restored from __doc__
        """ queue_draw_region(self, region:cairo.Region) """
        pass

    def queue_resize(self): # real signature unknown; restored from __doc__
        """ queue_resize(self) """
        pass

    def queue_resize_no_redraw(self): # real signature unknown; restored from __doc__
        """ queue_resize_no_redraw(self) """
        pass

    def realize(self): # real signature unknown; restored from __doc__
        """ realize(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def region_intersect(self, region): # real signature unknown; restored from __doc__
        """ region_intersect(self, region:cairo.Region) -> cairo.Region """
        pass

    def register_window(self, window): # real signature unknown; restored from __doc__
        """ register_window(self, window:Gdk.Window) """
        pass

    def reinit_ui(self): # real signature unknown; restored from __doc__
        """ reinit_ui(self) """
        pass

    def remove(self, widget): # real signature unknown; restored from __doc__
        """ remove(self, widget:Gtk.Widget) """
        pass

    def remove_accelerator(self, accel_group, accel_key, accel_mods): # real signature unknown; restored from __doc__
        """ remove_accelerator(self, accel_group:Gtk.AccelGroup, accel_key:int, accel_mods:Gdk.ModifierType) -> bool """
        return False

    def remove_mnemonic_label(self, label): # real signature unknown; restored from __doc__
        """ remove_mnemonic_label(self, label:Gtk.Widget) """
        pass

    def remove_page(self, page_num): # real signature unknown; restored from __doc__
        """ remove_page(self, page_num:int) """
        pass

    def remove_tick_callback(self, id): # real signature unknown; restored from __doc__
        """ remove_tick_callback(self, id:int) """
        pass

    def render_icon(self, stock_id, size, detail=None): # real signature unknown; restored from __doc__
        """ render_icon(self, stock_id:str, size:int, detail:str=None) -> GdkPixbuf.Pixbuf or None """
        pass

    def render_icon_pixbuf(self, stock_id, size): # real signature unknown; restored from __doc__
        """ render_icon_pixbuf(self, stock_id:str, size:int) -> GdkPixbuf.Pixbuf or None """
        pass

    def reorder_child(self, child, position): # real signature unknown; restored from __doc__
        """ reorder_child(self, child:Gtk.Widget, position:int) """
        pass

    def reparent(self, new_parent): # real signature unknown; restored from __doc__
        """ reparent(self, new_parent:Gtk.Widget) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset_rc_styles(self): # real signature unknown; restored from __doc__
        """ reset_rc_styles(self) """
        pass

    def reset_style(self): # real signature unknown; restored from __doc__
        """ reset_style(self) """
        pass

    def resize_children(self): # real signature unknown; restored from __doc__
        """ resize_children(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def send_expose(self, event): # real signature unknown; restored from __doc__
        """ send_expose(self, event:Gdk.Event) -> int """
        return 0

    def send_focus_change(self, event): # real signature unknown; restored from __doc__
        """ send_focus_change(self, event:Gdk.Event) -> bool """
        return False

    def set_accel_path(self, accel_path=None, accel_group=None): # real signature unknown; restored from __doc__
        """ set_accel_path(self, accel_path:str=None, accel_group:Gtk.AccelGroup=None) """
        pass

    def set_accessible_role(self, role): # real signature unknown; restored from __doc__
        """ set_accessible_role(self, role:Atk.Role) """
        pass

    def set_accessible_type(self, type): # real signature unknown; restored from __doc__
        """ set_accessible_type(self, type:GType) """
        pass

    def set_action_widget(self, widget, pack_type): # real signature unknown; restored from __doc__
        """ set_action_widget(self, widget:Gtk.Widget, pack_type:Gtk.PackType) """
        pass

    def set_allocation(self, allocation): # real signature unknown; restored from __doc__
        """ set_allocation(self, allocation:Gdk.Rectangle) """
        pass

    def set_angle(self, angle): # real signature unknown; restored from __doc__
        """ set_angle(self, angle:float) """
        pass

    def set_app_paintable(self, app_paintable): # real signature unknown; restored from __doc__
        """ set_app_paintable(self, app_paintable:bool) """
        pass

    def set_border_width(self, border_width): # real signature unknown; restored from __doc__
        """ set_border_width(self, border_width:int) """
        pass

    def set_buildable_property(self, builder, name, value): # real signature unknown; restored from __doc__
        """ set_buildable_property(self, builder:Gtk.Builder, name:str, value:GObject.Value) """
        pass

    def set_can_default(self, can_default): # real signature unknown; restored from __doc__
        """ set_can_default(self, can_default:bool) """
        pass

    def set_can_focus(self, can_focus): # real signature unknown; restored from __doc__
        """ set_can_focus(self, can_focus:bool) """
        pass

    def set_child_visible(self, is_visible): # real signature unknown; restored from __doc__
        """ set_child_visible(self, is_visible:bool) """
        pass

    def set_clip(self, clip): # real signature unknown; restored from __doc__
        """ set_clip(self, clip:Gdk.Rectangle) """
        pass

    def set_composite_name(self, name): # real signature unknown; restored from __doc__
        """ set_composite_name(self, name:str) """
        pass

    def set_connect_func(self, connect_func, connect_data=None): # real signature unknown; restored from __doc__
        """ set_connect_func(self, connect_func:Gtk.BuilderConnectFunc, connect_data=None) """
        pass

    def set_css_name(self, name): # real signature unknown; restored from __doc__
        """ set_css_name(self, name:str) """
        pass

    def set_current_page(self, page_num): # real signature unknown; restored from __doc__
        """ set_current_page(self, page_num:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_direction(self, dir): # real signature unknown; restored from __doc__
        """ set_default_direction(dir:Gtk.TextDirection) """
        pass

    def set_device_enabled(self, device, enabled): # real signature unknown; restored from __doc__
        """ set_device_enabled(self, device:Gdk.Device, enabled:bool) """
        pass

    def set_device_events(self, device, events): # real signature unknown; restored from __doc__
        """ set_device_events(self, device:Gdk.Device, events:Gdk.EventMask) """
        pass

    def set_direction(self, dir): # real signature unknown; restored from __doc__
        """ set_direction(self, dir:Gtk.TextDirection) """
        pass

    def set_double_buffered(self, double_buffered): # real signature unknown; restored from __doc__
        """ set_double_buffered(self, double_buffered:bool) """
        pass

    def set_events(self, events): # real signature unknown; restored from __doc__
        """ set_events(self, events:int) """
        pass

    def set_focus_chain(self, focusable_widgets): # real signature unknown; restored from __doc__
        """ set_focus_chain(self, focusable_widgets:list) """
        pass

    def set_focus_child(self, child=None): # real signature unknown; restored from __doc__
        """ set_focus_child(self, child:Gtk.Widget=None) """
        pass

    def set_focus_hadjustment(self, adjustment): # real signature unknown; restored from __doc__
        """ set_focus_hadjustment(self, adjustment:Gtk.Adjustment) """
        pass

    def set_focus_on_click(self, focus_on_click): # real signature unknown; restored from __doc__
        """ set_focus_on_click(self, focus_on_click:bool) """
        pass

    def set_focus_vadjustment(self, adjustment): # real signature unknown; restored from __doc__
        """ set_focus_vadjustment(self, adjustment:Gtk.Adjustment) """
        pass

    def set_font_map(self, font_map=None): # real signature unknown; restored from __doc__
        """ set_font_map(self, font_map:Pango.FontMap=None) """
        pass

    def set_font_options(self, options=None): # real signature unknown; restored from __doc__
        """ set_font_options(self, options:cairo.FontOptions=None) """
        pass

    def set_group_name(self, group_name=None): # real signature unknown; restored from __doc__
        """ set_group_name(self, group_name:str=None) """
        pass

    def set_halign(self, align): # real signature unknown; restored from __doc__
        """ set_halign(self, align:Gtk.Align) """
        pass

    def set_has_tooltip(self, has_tooltip): # real signature unknown; restored from __doc__
        """ set_has_tooltip(self, has_tooltip:bool) """
        pass

    def set_has_window(self, has_window): # real signature unknown; restored from __doc__
        """ set_has_window(self, has_window:bool) """
        pass

    def set_hexpand(self, expand): # real signature unknown; restored from __doc__
        """ set_hexpand(self, expand:bool) """
        pass

    def set_hexpand_set(self, set): # real signature unknown; restored from __doc__
        """ set_hexpand_set(self, set:bool) """
        pass

    def set_mapped(self, mapped): # real signature unknown; restored from __doc__
        """ set_mapped(self, mapped:bool) """
        pass

    def set_margin_bottom(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_bottom(self, margin:int) """
        pass

    def set_margin_end(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_end(self, margin:int) """
        pass

    def set_margin_left(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_left(self, margin:int) """
        pass

    def set_margin_right(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_right(self, margin:int) """
        pass

    def set_margin_start(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_start(self, margin:int) """
        pass

    def set_margin_top(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_top(self, margin:int) """
        pass

    def set_menu_label(self, child, menu_label=None): # real signature unknown; restored from __doc__
        """ set_menu_label(self, child:Gtk.Widget, menu_label:Gtk.Widget=None) """
        pass

    def set_menu_label_text(self, child, menu_text): # real signature unknown; restored from __doc__
        """ set_menu_label_text(self, child:Gtk.Widget, menu_text:str) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_no_show_all(self, no_show_all): # real signature unknown; restored from __doc__
        """ set_no_show_all(self, no_show_all:bool) """
        pass

    def set_opacity(self, opacity): # real signature unknown; restored from __doc__
        """ set_opacity(self, opacity:float) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gtk.Widget) """
        pass

    def set_parent_tooltips(self, ifset): # real signature unknown; restored from __doc__
        """ set_parent_tooltips(self, ifset:bool) """
        pass

    def set_parent_window(self, parent_window): # real signature unknown; restored from __doc__
        """ set_parent_window(self, parent_window:Gdk.Window) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_realized(self, realized): # real signature unknown; restored from __doc__
        """ set_realized(self, realized:bool) """
        pass

    def set_reallocate_redraws(self, needs_redraws): # real signature unknown; restored from __doc__
        """ set_reallocate_redraws(self, needs_redraws:bool) """
        pass

    def set_receives_default(self, receives_default): # real signature unknown; restored from __doc__
        """ set_receives_default(self, receives_default:bool) """
        pass

    def set_redraw_on_allocate(self, redraw_on_allocate): # real signature unknown; restored from __doc__
        """ set_redraw_on_allocate(self, redraw_on_allocate:bool) """
        pass

    def set_resize_mode(self, resize_mode): # real signature unknown; restored from __doc__
        """ set_resize_mode(self, resize_mode:Gtk.ResizeMode) """
        pass

    def set_scrollable(self, scrollable): # real signature unknown; restored from __doc__
        """ set_scrollable(self, scrollable:bool) """
        pass

    def set_sensitive(self, sensitive): # real signature unknown; restored from __doc__
        """ set_sensitive(self, sensitive:bool) """
        pass

    def set_show_border(self, show_border): # real signature unknown; restored from __doc__
        """ set_show_border(self, show_border:bool) """
        pass

    def set_show_tabs(self, show_tabs): # real signature unknown; restored from __doc__
        """ set_show_tabs(self, show_tabs:bool) """
        pass

    def set_size_request(self, width, height): # real signature unknown; restored from __doc__
        """ set_size_request(self, width:int, height:int) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Gtk.StateType) """
        pass

    def set_state_flags(self, flags, clear): # real signature unknown; restored from __doc__
        """ set_state_flags(self, flags:Gtk.StateFlags, clear:bool) """
        pass

    def set_style(self, style=None): # real signature unknown; restored from __doc__
        """ set_style(self, style:Gtk.Style=None) """
        pass

    def set_support_multidevice(self, support_multidevice): # real signature unknown; restored from __doc__
        """ set_support_multidevice(self, support_multidevice:bool) """
        pass

    def set_tab_detachable(self, child, detachable): # real signature unknown; restored from __doc__
        """ set_tab_detachable(self, child:Gtk.Widget, detachable:bool) """
        pass

    def set_tab_label(self, child, tab_label=None): # real signature unknown; restored from __doc__
        """ set_tab_label(self, child:Gtk.Widget, tab_label:Gtk.Widget=None) """
        pass

    def set_tab_label_text(self, child, tab_text): # real signature unknown; restored from __doc__
        """ set_tab_label_text(self, child:Gtk.Widget, tab_text:str) """
        pass

    def set_tab_pos(self, pos): # real signature unknown; restored from __doc__
        """ set_tab_pos(self, pos:Gtk.PositionType) """
        pass

    def set_tab_reorderable(self, child, reorderable): # real signature unknown; restored from __doc__
        """ set_tab_reorderable(self, child:Gtk.Widget, reorderable:bool) """
        pass

    def set_template(self, template_bytes): # real signature unknown; restored from __doc__
        """ set_template(self, template_bytes:GLib.Bytes) """
        pass

    def set_template_from_resource(self, resource_name): # real signature unknown; restored from __doc__
        """ set_template_from_resource(self, resource_name:str) """
        pass

    def set_tooltip_markup(self, markup=None): # real signature unknown; restored from __doc__
        """ set_tooltip_markup(self, markup:str=None) """
        pass

    def set_tooltip_text(self, text=None): # real signature unknown; restored from __doc__
        """ set_tooltip_text(self, text:str=None) """
        pass

    def set_tooltip_window(self, custom_window=None): # real signature unknown; restored from __doc__
        """ set_tooltip_window(self, custom_window:Gtk.Window=None) """
        pass

    def set_valign(self, align): # real signature unknown; restored from __doc__
        """ set_valign(self, align:Gtk.Align) """
        pass

    def set_vexpand(self, expand): # real signature unknown; restored from __doc__
        """ set_vexpand(self, expand:bool) """
        pass

    def set_vexpand_set(self, set): # real signature unknown; restored from __doc__
        """ set_vexpand_set(self, set:bool) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
        pass

    def set_visual(self, visual=None): # real signature unknown; restored from __doc__
        """ set_visual(self, visual:Gdk.Visual=None) """
        pass

    def set_window(self, window): # real signature unknown; restored from __doc__
        """ set_window(self, window:Gdk.Window) """
        pass

    def shape_combine_region(self, region=None): # real signature unknown; restored from __doc__
        """ shape_combine_region(self, region:cairo.Region=None) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def show_all(self): # real signature unknown; restored from __doc__
        """ show_all(self) """
        pass

    def show_now(self): # real signature unknown; restored from __doc__
        """ show_now(self) """
        pass

    def size_allocate(self, allocation): # real signature unknown; restored from __doc__
        """ size_allocate(self, allocation:Gdk.Rectangle) """
        pass

    def size_allocate_with_baseline(self, allocation, baseline): # real signature unknown; restored from __doc__
        """ size_allocate_with_baseline(self, allocation:Gdk.Rectangle, baseline:int) """
        pass

    def size_request(self): # real signature unknown; restored from __doc__
        """ size_request(self) -> requisition:Gtk.Requisition """
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

    def style_attach(self): # real signature unknown; restored from __doc__
        """ style_attach(self) """
        pass

    def style_get_property(self, property_name, value=None): # reliably restored by inspect
        # no doc
        pass

    def thaw_child_notify(self): # real signature unknown; restored from __doc__
        """ thaw_child_notify(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def translate_coordinates(*args, **kwargs): # reliably restored by inspect
        """ translate_coordinates(self, dest_widget:Gtk.Widget, src_x:int, src_y:int) -> bool, dest_x:int, dest_y:int """
        pass

    def trigger_tooltip_query(self): # real signature unknown; restored from __doc__
        """ trigger_tooltip_query(self) """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unrealize(self): # real signature unknown; restored from __doc__
        """ unrealize(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unregister_window(self, window): # real signature unknown; restored from __doc__
        """ unregister_window(self, window:Gdk.Window) """
        pass

    def unset_focus_chain(self): # real signature unknown; restored from __doc__
        """ unset_focus_chain(self) """
        pass

    def unset_state_flags(self, flags): # real signature unknown; restored from __doc__
        """ unset_state_flags(self, flags:Gtk.StateFlags) """
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

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __contains__(self, child): # reliably restored by inspect
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

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __len__(self): # reliably restored by inspect
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
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __nonzero__(self): # reliably restored by inspect
        # no doc
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

    container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    widget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb1731cb0a0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Indicator), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType GkbdIndicator (94195347656320)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_group_names': gi.FunctionInfo(get_group_names), 'get_image_filename': gi.FunctionInfo(get_image_filename), 'get_max_width_height_ratio': gi.FunctionInfo(get_max_width_height_ratio), 'get_xkl_engine': gi.FunctionInfo(get_xkl_engine), 'reinit_ui': gi.FunctionInfo(reinit_ui), 'set_angle': gi.FunctionInfo(set_angle), 'set_parent_tooltips': gi.FunctionInfo(set_parent_tooltips), 'do_reinit_ui': gi.VFuncInfo(reinit_ui), 'parent': <property object at 0x7fb1731b5e00>, 'priv': <property object at 0x7fb1731b5ef0>})"
    __gdoc__ = "Object GkbdIndicator\n\nSignals from GkbdIndicator:\n  reinit-ui ()\n\nSignals from GtkNotebook:\n  switch-page (GtkWidget, guint)\n  focus-tab (GtkNotebookTab) -> gboolean\n  select-page (gboolean) -> gboolean\n  change-current-page (gint) -> gboolean\n  move-focus-out (GtkDirectionType)\n  reorder-tab (GtkDirectionType, gboolean) -> gboolean\n  page-reordered (GtkWidget, guint)\n  page-removed (GtkWidget, guint)\n  page-added (GtkWidget, guint)\n  create-window (GtkWidget, gint, gint) -> GtkNotebook\n\nProperties from GtkNotebook:\n  tab-pos -> GtkPositionType: Tab Position\n    Which side of the notebook holds the tabs\n  show-tabs -> gboolean: Show Tabs\n    Whether tabs should be shown\n  show-border -> gboolean: Show Border\n    Whether the border should be shown\n  scrollable -> gboolean: Scrollable\n    If TRUE, scroll arrows are added if there are too many tabs to fit\n  page -> gint: Page\n    The index of the current page\n  enable-popup -> gboolean: Enable Popup\n    If TRUE, pressing the right mouse button on the notebook pops up a menu that you can use to go to a page\n  group-name -> gchararray: Group Name\n    Group name for tab drag and drop\n\nSignals from GtkContainer:\n  add (GtkWidget)\n  remove (GtkWidget)\n  check-resize ()\n  set-focus-child (GtkWidget)\n\nProperties from GtkContainer:\n  border-width -> guint: Border width\n    The width of the empty border outside the containers children\n  resize-mode -> GtkResizeMode: Resize mode\n    Specify how resize events are handled\n  child -> GtkWidget: Child\n    Can be used to add a new child to the container\n\nSignals from GtkWidget:\n  composited-changed ()\n  destroy ()\n  show ()\n  hide ()\n  map ()\n  unmap ()\n  realize ()\n  unrealize ()\n  size-allocate (GdkRectangle)\n  state-changed (GtkStateType)\n  state-flags-changed (GtkStateFlags)\n  parent-set (GtkWidget)\n  hierarchy-changed (GtkWidget)\n  style-set (GtkStyle)\n  style-updated ()\n  direction-changed (GtkTextDirection)\n  grab-notify (gboolean)\n  child-notify (GParam)\n  draw (CairoContext) -> gboolean\n  mnemonic-activate (gboolean) -> gboolean\n  grab-focus ()\n  focus (GtkDirectionType) -> gboolean\n  move-focus (GtkDirectionType)\n  keynav-failed (GtkDirectionType) -> gboolean\n  event (GdkEvent) -> gboolean\n  event-after (GdkEvent)\n  button-press-event (GdkEvent) -> gboolean\n  button-release-event (GdkEvent) -> gboolean\n  touch-event (GdkEvent) -> gboolean\n  scroll-event (GdkEvent) -> gboolean\n  motion-notify-event (GdkEvent) -> gboolean\n  delete-event (GdkEvent) -> gboolean\n  destroy-event (GdkEvent) -> gboolean\n  key-press-event (GdkEvent) -> gboolean\n  key-release-event (GdkEvent) -> gboolean\n  enter-notify-event (GdkEvent) -> gboolean\n  leave-notify-event (GdkEvent) -> gboolean\n  configure-event (GdkEvent) -> gboolean\n  focus-in-event (GdkEvent) -> gboolean\n  focus-out-event (GdkEvent) -> gboolean\n  map-event (GdkEvent) -> gboolean\n  unmap-event (GdkEvent) -> gboolean\n  property-notify-event (GdkEvent) -> gboolean\n  selection-clear-event (GdkEvent) -> gboolean\n  selection-request-event (GdkEvent) -> gboolean\n  selection-notify-event (GdkEvent) -> gboolean\n  selection-received (GtkSelectionData, guint)\n  selection-get (GtkSelectionData, guint, guint)\n  proximity-in-event (GdkEvent) -> gboolean\n  proximity-out-event (GdkEvent) -> gboolean\n  drag-leave (GdkDragContext, guint)\n  drag-begin (GdkDragContext)\n  drag-end (GdkDragContext)\n  drag-data-delete (GdkDragContext)\n  drag-failed (GdkDragContext, GtkDragResult) -> gboolean\n  drag-motion (GdkDragContext, gint, gint, guint) -> gboolean\n  drag-drop (GdkDragContext, gint, gint, guint) -> gboolean\n  drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)\n  drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)\n  visibility-notify-event (GdkEvent) -> gboolean\n  window-state-event (GdkEvent) -> gboolean\n  damage-event (GdkEvent) -> gboolean\n  grab-broken-event (GdkEvent) -> gboolean\n  query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean\n  popup-menu () -> gboolean\n  show-help (GtkWidgetHelpType) -> gboolean\n  accel-closures-changed ()\n  screen-changed (GdkScreen)\n  can-activate-accel (guint) -> gboolean\n\nProperties from GtkWidget:\n  name -> gchararray: Widget name\n    The name of the widget\n  parent -> GtkContainer: Parent widget\n    The parent widget of this widget. Must be a Container widget\n  width-request -> gint: Width request\n    Override for width request of the widget, or -1 if natural request should be used\n  height-request -> gint: Height request\n    Override for height request of the widget, or -1 if natural request should be used\n  visible -> gboolean: Visible\n    Whether the widget is visible\n  sensitive -> gboolean: Sensitive\n    Whether the widget responds to input\n  app-paintable -> gboolean: Application paintable\n    Whether the application will paint directly on the widget\n  can-focus -> gboolean: Can focus\n    Whether the widget can accept the input focus\n  has-focus -> gboolean: Has focus\n    Whether the widget has the input focus\n  is-focus -> gboolean: Is focus\n    Whether the widget is the focus widget within the toplevel\n  focus-on-click -> gboolean: Focus on click\n    Whether the widget should grab focus when it is clicked with the mouse\n  can-default -> gboolean: Can default\n    Whether the widget can be the default widget\n  has-default -> gboolean: Has default\n    Whether the widget is the default widget\n  receives-default -> gboolean: Receives default\n    If TRUE, the widget will receive the default action when it is focused\n  composite-child -> gboolean: Composite child\n    Whether the widget is part of a composite widget\n  style -> GtkStyle: Style\n    The style of the widget, which contains information about how it will look (colors etc)\n  events -> GdkEventMask: Events\n    The event mask that decides what kind of GdkEvents this widget gets\n  no-show-all -> gboolean: No show all\n    Whether gtk_widget_show_all() should not affect this widget\n  has-tooltip -> gboolean: Has tooltip\n    Whether this widget has a tooltip\n  tooltip-markup -> gchararray: Tooltip markup\n    The contents of the tooltip for this widget\n  tooltip-text -> gchararray: Tooltip Text\n    The contents of the tooltip for this widget\n  window -> GdkWindow: Window\n    The widget's window if it is realized\n  opacity -> gdouble: Opacity for Widget\n    The opacity of the widget, from 0 to 1\n  double-buffered -> gboolean: Double Buffered\n    Whether the widget is double buffered\n  halign -> GtkAlign: Horizontal Alignment\n    How to position in extra horizontal space\n  valign -> GtkAlign: Vertical Alignment\n    How to position in extra vertical space\n  margin-left -> gint: Margin on Left\n    Pixels of extra space on the left side\n  margin-right -> gint: Margin on Right\n    Pixels of extra space on the right side\n  margin-start -> gint: Margin on Start\n    Pixels of extra space on the start\n  margin-end -> gint: Margin on End\n    Pixels of extra space on the end\n  margin-top -> gint: Margin on Top\n    Pixels of extra space on the top side\n  margin-bottom -> gint: Margin on Bottom\n    Pixels of extra space on the bottom side\n  margin -> gint: All Margins\n    Pixels of extra space on all four sides\n  hexpand -> gboolean: Horizontal Expand\n    Whether widget wants more horizontal space\n  vexpand -> gboolean: Vertical Expand\n    Whether widget wants more vertical space\n  hexpand-set -> gboolean: Horizontal Expand Set\n    Whether to use the hexpand property\n  vexpand-set -> gboolean: Vertical Expand Set\n    Whether to use the vexpand property\n  expand -> gboolean: Expand Both\n    Whether widget wants to expand in both directions\n  scale-factor -> gint: Scale factor\n    The scaling factor of the window\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GkbdIndicator (94195347656320)>'
    __info__ = ObjectInfo(Indicator)


class IndicatorClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        IndicatorClass()
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

    reinit_ui = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(IndicatorClass), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'IndicatorClass' objects>, '__weakref__': <attribute '__weakref__' of 'IndicatorClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fb1731b90e0>, 'reinit_ui': <property object at 0x7fb1731b91d0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(IndicatorClass)


class IndicatorConfig(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        IndicatorConfig()
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) """
        pass

    def free_image_filenames(self): # real signature unknown; restored from __doc__
        """ free_image_filenames(self) """
        pass

    def get_fg_color_for_widget(self, widget): # real signature unknown; restored from __doc__
        """ get_fg_color_for_widget(self, widget:Gtk.Widget) -> str """
        return ""

    def get_font_for_widget(self, widget, font_family, font_size): # real signature unknown; restored from __doc__
        """ get_font_for_widget(self, widget:Gtk.Widget, font_family:str, font_size:int) """
        pass

    def get_images_file(self, kbd_config, group): # real signature unknown; restored from __doc__
        """ get_images_file(self, kbd_config:Gkbd.KeyboardConfig, group:int) -> str """
        return ""

    def init(self, engine): # real signature unknown; restored from __doc__
        """ init(self, engine:Xkl.Engine) """
        pass

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) """
        pass

    def load_image_filenames(self, kbd_config): # real signature unknown; restored from __doc__
        """ load_image_filenames(self, kbd_config:Gkbd.KeyboardConfig) """
        pass

    def refresh_style(self): # real signature unknown; restored from __doc__
        """ refresh_style(self) """
        pass

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) """
        pass

    def start_listen(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ start_listen(self, func:GObject.Callback, user_data=None) """
        pass

    def stop_listen(self): # real signature unknown; restored from __doc__
        """ stop_listen(self) """
        pass

    def term(self): # real signature unknown; restored from __doc__
        """ term(self) """
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

    background_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    config_listener_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    engine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font_family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    foreground_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    icon_theme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    image_filenames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_groups_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(IndicatorConfig), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'IndicatorConfig' objects>, '__weakref__': <attribute '__weakref__' of 'IndicatorConfig' objects>, '__doc__': None, 'secondary_groups_mask': <property object at 0x7fb1731b93b0>, 'show_flags': <property object at 0x7fb1731b94a0>, 'font_family': <property object at 0x7fb1731b9590>, 'font_size': <property object at 0x7fb1731b9680>, 'foreground_color': <property object at 0x7fb1731b97c0>, 'background_color': <property object at 0x7fb1731b9900>, 'settings': <property object at 0x7fb1731b99f0>, 'image_filenames': <property object at 0x7fb1731b9ae0>, 'icon_theme': <property object at 0x7fb1731b9bd0>, 'config_listener_id': <property object at 0x7fb1731b9d10>, 'engine': <property object at 0x7fb1731b9db0>, 'activate': gi.FunctionInfo(activate), 'free_image_filenames': gi.FunctionInfo(free_image_filenames), 'get_fg_color_for_widget': gi.FunctionInfo(get_fg_color_for_widget), 'get_font_for_widget': gi.FunctionInfo(get_font_for_widget), 'get_images_file': gi.FunctionInfo(get_images_file), 'init': gi.FunctionInfo(init), 'load': gi.FunctionInfo(load), 'load_image_filenames': gi.FunctionInfo(load_image_filenames), 'refresh_style': gi.FunctionInfo(refresh_style), 'save': gi.FunctionInfo(save), 'start_listen': gi.FunctionInfo(start_listen), 'stop_listen': gi.FunctionInfo(stop_listen), 'term': gi.FunctionInfo(term)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(IndicatorConfig)


class IndicatorPrivate(__gi.Struct):
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(IndicatorPrivate), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'IndicatorPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'IndicatorPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(IndicatorPrivate)


class KeyboardConfig(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        KeyboardConfig()
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def add_default_switch_option_if_necessary(self, layouts_list, options_list, was_appended): # real signature unknown; restored from __doc__
        """ add_default_switch_option_if_necessary(layouts_list:str, options_list:str, was_appended:bool) -> list """
        return []

    def equals(self, kbd_config2): # real signature unknown; restored from __doc__
        """ equals(self, kbd_config2:Gkbd.KeyboardConfig) -> bool """
        return False

    def format_full_description(self, layout_descr, variant_descr): # real signature unknown; restored from __doc__
        """ format_full_description(layout_descr:str, variant_descr:str) -> str """
        return ""

    def get_descriptions(self, config_registry, name, layout_short_descr, layout_descr, variant_short_descr, variant_descr): # real signature unknown; restored from __doc__
        """ get_descriptions(config_registry:Xkl.ConfigRegistry, name:str, layout_short_descr:str, layout_descr:str, variant_short_descr:str, variant_descr:str) -> bool """
        return False

    def init(self, engine): # real signature unknown; restored from __doc__
        """ init(self, engine:Xkl.Engine) """
        pass

    def load(self, kbd_config_default): # real signature unknown; restored from __doc__
        """ load(self, kbd_config_default:Gkbd.KeyboardConfig) """
        pass

    def load_from_x_current(self, buf): # real signature unknown; restored from __doc__
        """ load_from_x_current(self, buf:Xkl.ConfigRec) """
        pass

    def load_from_x_initial(self, buf): # real signature unknown; restored from __doc__
        """ load_from_x_initial(self, buf:Xkl.ConfigRec) """
        pass

    def merge_items(self, parent, child): # real signature unknown; restored from __doc__
        """ merge_items(parent:str, child:str) -> str """
        return ""

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) """
        pass

    def split_items(self, merged, parent, child): # real signature unknown; restored from __doc__
        """ split_items(merged:str, parent:str, child:str) -> bool """
        return False

    def start_listen(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ start_listen(self, func:GObject.Callback, user_data=None) """
        pass

    def stop_listen(self): # real signature unknown; restored from __doc__
        """ stop_listen(self) """
        pass

    def term(self): # real signature unknown; restored from __doc__
        """ term(self) """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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

    config_listener_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    engine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layouts_variants = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(KeyboardConfig), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'KeyboardConfig' objects>, '__weakref__': <attribute '__weakref__' of 'KeyboardConfig' objects>, '__doc__': None, 'model': <property object at 0x7fb1731bb1d0>, 'layouts_variants': <property object at 0x7fb1731bb310>, 'options': <property object at 0x7fb1731bb400>, 'settings': <property object at 0x7fb1731bb4f0>, 'config_listener_id': <property object at 0x7fb1731bb630>, 'engine': <property object at 0x7fb1731bb6d0>, 'activate': gi.FunctionInfo(activate), 'equals': gi.FunctionInfo(equals), 'init': gi.FunctionInfo(init), 'load': gi.FunctionInfo(load), 'load_from_x_current': gi.FunctionInfo(load_from_x_current), 'load_from_x_initial': gi.FunctionInfo(load_from_x_initial), 'save': gi.FunctionInfo(save), 'start_listen': gi.FunctionInfo(start_listen), 'stop_listen': gi.FunctionInfo(stop_listen), 'term': gi.FunctionInfo(term), 'to_string': gi.FunctionInfo(to_string), 'add_default_switch_option_if_necessary': gi.FunctionInfo(add_default_switch_option_if_necessary), 'format_full_description': gi.FunctionInfo(format_full_description), 'get_descriptions': gi.FunctionInfo(get_descriptions), 'merge_items': gi.FunctionInfo(merge_items), 'split_items': gi.FunctionInfo(split_items)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(KeyboardConfig)


class KeyboardDrawing(__gi_repository_Gtk.DrawingArea):
    """
    :Constructors:
    
    ::
    
        KeyboardDrawing(**properties)
        dialog_new() -> Gtk.Widget
        new() -> Gtk.Widget
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def add_accelerator(self, accel_signal, accel_group, accel_key, accel_mods, accel_flags): # real signature unknown; restored from __doc__
        """ add_accelerator(self, accel_signal:str, accel_group:Gtk.AccelGroup, accel_key:int, accel_mods:Gdk.ModifierType, accel_flags:Gtk.AccelFlags) """
        pass

    def add_child(self, builder, child, type=None): # real signature unknown; restored from __doc__
        """ add_child(self, builder:Gtk.Builder, child:GObject.Object, type:str=None) """
        pass

    def add_device_events(self, device, events): # real signature unknown; restored from __doc__
        """ add_device_events(self, device:Gdk.Device, events:Gdk.EventMask) """
        pass

    def add_events(self, events): # real signature unknown; restored from __doc__
        """ add_events(self, events:int) """
        pass

    def add_mnemonic_label(self, label): # real signature unknown; restored from __doc__
        """ add_mnemonic_label(self, label:Gtk.Widget) """
        pass

    def add_tick_callback(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_tick_callback(self, callback:Gtk.TickCallback, user_data=None) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def bind_template_callback_full(self, callback_name, callback_symbol): # real signature unknown; restored from __doc__
        """ bind_template_callback_full(self, callback_name:str, callback_symbol:GObject.Callback) """
        pass

    def bind_template_child_full(self, name, internal_child, struct_offset): # real signature unknown; restored from __doc__
        """ bind_template_child_full(self, name:str, internal_child:bool, struct_offset:int) """
        pass

    def can_activate_accel(self, signal_id): # real signature unknown; restored from __doc__
        """ can_activate_accel(self, signal_id:int) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def child_focus(self, direction): # real signature unknown; restored from __doc__
        """ child_focus(self, direction:Gtk.DirectionType) -> bool """
        return False

    def child_notify(self, child_property): # real signature unknown; restored from __doc__
        """ child_notify(self, child_property:str) """
        pass

    def class_path(self): # real signature unknown; restored from __doc__
        """ class_path(self) -> path_length:int, path:str, path_reversed:str """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def compute_expand(self, orientation): # real signature unknown; restored from __doc__
        """ compute_expand(self, orientation:Gtk.Orientation) -> bool """
        return False

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

    def construct_child(self, builder, name): # real signature unknown; restored from __doc__
        """ construct_child(self, builder:Gtk.Builder, name:str) -> GObject.Object """
        pass

    def create_pango_context(self): # real signature unknown; restored from __doc__
        """ create_pango_context(self) -> Pango.Context """
        pass

    def create_pango_layout(self, text=None): # real signature unknown; restored from __doc__
        """ create_pango_layout(self, text:str=None) -> Pango.Layout """
        pass

    def custom_finished(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_finished(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_end(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_tag_end(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_start(self, builder, child=None, tagname): # real signature unknown; restored from __doc__
        """ custom_tag_start(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str) -> bool, parser:GLib.MarkupParser, data """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def destroyed(self, widget_pointer): # real signature unknown; restored from __doc__
        """ destroyed(self, widget_pointer:Gtk.Widget) -> widget_pointer:Gtk.Widget """
        pass

    def device_is_shadowed(self, device): # real signature unknown; restored from __doc__
        """ device_is_shadowed(self, device:Gdk.Device) -> bool """
        return False

    def dialog_new(self): # real signature unknown; restored from __doc__
        """ dialog_new() -> Gtk.Widget """
        pass

    def dialog_set_group(self, dialog, registry, group): # real signature unknown; restored from __doc__
        """ dialog_set_group(dialog:Gtk.Widget, registry:Xkl.ConfigRegistry, group:int) """
        pass

    def dialog_set_layout(self, dialog, registry, layout): # real signature unknown; restored from __doc__
        """ dialog_set_layout(dialog:Gtk.Widget, registry:Xkl.ConfigRegistry, layout:str) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_adjust_baseline_allocation(self, *args, **kwargs): # real signature unknown
        """ adjust_baseline_allocation(self, baseline:int) """
        pass

    def do_adjust_baseline_request(self, *args, **kwargs): # real signature unknown
        """ adjust_baseline_request(self, minimum_baseline:int, natural_baseline:int) """
        pass

    def do_adjust_size_allocation(self, *args, **kwargs): # real signature unknown
        """ adjust_size_allocation(self, orientation:Gtk.Orientation, minimum_size:int, natural_size:int, allocated_pos:int, allocated_size:int) """
        pass

    def do_adjust_size_request(self, *args, **kwargs): # real signature unknown
        """ adjust_size_request(self, orientation:Gtk.Orientation, minimum_size:int, natural_size:int) """
        pass

    def do_bad_keycode(self, *args, **kwargs): # real signature unknown
        """ bad_keycode(self, keycode:int) """
        pass

    def do_button_press_event(self, *args, **kwargs): # real signature unknown
        """ button_press_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_button_release_event(self, *args, **kwargs): # real signature unknown
        """ button_release_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_can_activate_accel(self, *args, **kwargs): # real signature unknown
        """ can_activate_accel(self, signal_id:int) -> bool """
        pass

    def do_child_notify(self, *args, **kwargs): # real signature unknown
        """ child_notify(self, child_property:GObject.ParamSpec) """
        pass

    def do_composited_changed(self, *args, **kwargs): # real signature unknown
        """ composited_changed(self) """
        pass

    def do_compute_expand(self, *args, **kwargs): # real signature unknown
        """ compute_expand(self, hexpand_p:bool, vexpand_p:bool) """
        pass

    def do_configure_event(self, *args, **kwargs): # real signature unknown
        """ configure_event(self, event:Gdk.EventConfigure) -> bool """
        pass

    def do_damage_event(self, *args, **kwargs): # real signature unknown
        """ damage_event(self, event:Gdk.EventExpose) -> bool """
        pass

    def do_delete_event(self, *args, **kwargs): # real signature unknown
        """ delete_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_destroy(self, *args, **kwargs): # real signature unknown
        """ destroy(self) """
        pass

    def do_destroy_event(self, *args, **kwargs): # real signature unknown
        """ destroy_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_direction_changed(self, *args, **kwargs): # real signature unknown
        """ direction_changed(self, previous_direction:Gtk.TextDirection) """
        pass

    def do_dispatch_child_properties_changed(self, *args, **kwargs): # real signature unknown
        """ dispatch_child_properties_changed(self, n_pspecs:int, pspecs:GObject.ParamSpec) """
        pass

    def do_drag_begin(self, *args, **kwargs): # real signature unknown
        """ drag_begin(self, context:Gdk.DragContext) """
        pass

    def do_drag_data_delete(self, *args, **kwargs): # real signature unknown
        """ drag_data_delete(self, context:Gdk.DragContext) """
        pass

    def do_drag_data_get(self, *args, **kwargs): # real signature unknown
        """ drag_data_get(self, context:Gdk.DragContext, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_drag_data_received(self, *args, **kwargs): # real signature unknown
        """ drag_data_received(self, context:Gdk.DragContext, x:int, y:int, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_drag_drop(self, *args, **kwargs): # real signature unknown
        """ drag_drop(self, context:Gdk.DragContext, x:int, y:int, time_:int) -> bool """
        pass

    def do_drag_end(self, *args, **kwargs): # real signature unknown
        """ drag_end(self, context:Gdk.DragContext) """
        pass

    def do_drag_failed(self, *args, **kwargs): # real signature unknown
        """ drag_failed(self, context:Gdk.DragContext, result:Gtk.DragResult) -> bool """
        pass

    def do_drag_leave(self, *args, **kwargs): # real signature unknown
        """ drag_leave(self, context:Gdk.DragContext, time_:int) """
        pass

    def do_drag_motion(self, *args, **kwargs): # real signature unknown
        """ drag_motion(self, context:Gdk.DragContext, x:int, y:int, time_:int) -> bool """
        pass

    def do_draw(self, *args, **kwargs): # real signature unknown
        """ draw(self, cr:cairo.Context) -> bool """
        pass

    def do_enter_notify_event(self, *args, **kwargs): # real signature unknown
        """ enter_notify_event(self, event:Gdk.EventCrossing) -> bool """
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event:Gdk.Event) -> bool """
        pass

    def do_focus(self, *args, **kwargs): # real signature unknown
        """ focus(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_focus_in_event(self, *args, **kwargs): # real signature unknown
        """ focus_in_event(self, event:Gdk.EventFocus) -> bool """
        pass

    def do_focus_out_event(self, *args, **kwargs): # real signature unknown
        """ focus_out_event(self, event:Gdk.EventFocus) -> bool """
        pass

    def do_get_accessible(self, *args, **kwargs): # real signature unknown
        """ get_accessible(self) -> Atk.Object """
        pass

    def do_get_preferred_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height(self) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_height_and_baseline_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_and_baseline_for_width(self, width:int) -> minimum_height:int, natural_height:int, minimum_baseline:int, natural_baseline:int """
        pass

    def do_get_preferred_height_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_for_width(self, width:int) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width(self) -> minimum_width:int, natural_width:int """
        pass

    def do_get_preferred_width_for_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width_for_height(self, height:int) -> minimum_width:int, natural_width:int """
        pass

    def do_get_request_mode(self, *args, **kwargs): # real signature unknown
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def do_grab_broken_event(self, *args, **kwargs): # real signature unknown
        """ grab_broken_event(self, event:Gdk.EventGrabBroken) -> bool """
        pass

    def do_grab_focus(self, *args, **kwargs): # real signature unknown
        """ grab_focus(self) """
        pass

    def do_grab_notify(self, *args, **kwargs): # real signature unknown
        """ grab_notify(self, was_grabbed:bool) """
        pass

    def do_hide(self, *args, **kwargs): # real signature unknown
        """ hide(self) """
        pass

    def do_hierarchy_changed(self, *args, **kwargs): # real signature unknown
        """ hierarchy_changed(self, previous_toplevel:Gtk.Widget) """
        pass

    def do_keynav_failed(self, *args, **kwargs): # real signature unknown
        """ keynav_failed(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_key_press_event(self, *args, **kwargs): # real signature unknown
        """ key_press_event(self, event:Gdk.EventKey) -> bool """
        pass

    def do_key_release_event(self, *args, **kwargs): # real signature unknown
        """ key_release_event(self, event:Gdk.EventKey) -> bool """
        pass

    def do_leave_notify_event(self, *args, **kwargs): # real signature unknown
        """ leave_notify_event(self, event:Gdk.EventCrossing) -> bool """
        pass

    def do_map(self, *args, **kwargs): # real signature unknown
        """ map(self) """
        pass

    def do_map_event(self, *args, **kwargs): # real signature unknown
        """ map_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_mnemonic_activate(self, *args, **kwargs): # real signature unknown
        """ mnemonic_activate(self, group_cycling:bool) -> bool """
        pass

    def do_motion_notify_event(self, *args, **kwargs): # real signature unknown
        """ motion_notify_event(self, event:Gdk.EventMotion) -> bool """
        pass

    def do_move_focus(self, *args, **kwargs): # real signature unknown
        """ move_focus(self, direction:Gtk.DirectionType) """
        pass

    def do_parent_set(self, *args, **kwargs): # real signature unknown
        """ parent_set(self, previous_parent:Gtk.Widget) """
        pass

    def do_popup_menu(self, *args, **kwargs): # real signature unknown
        """ popup_menu(self) -> bool """
        pass

    def do_property_notify_event(self, *args, **kwargs): # real signature unknown
        """ property_notify_event(self, event:Gdk.EventProperty) -> bool """
        pass

    def do_proximity_in_event(self, *args, **kwargs): # real signature unknown
        """ proximity_in_event(self, event:Gdk.EventProximity) -> bool """
        pass

    def do_proximity_out_event(self, *args, **kwargs): # real signature unknown
        """ proximity_out_event(self, event:Gdk.EventProximity) -> bool """
        pass

    def do_query_tooltip(self, *args, **kwargs): # real signature unknown
        """ query_tooltip(self, x:int, y:int, keyboard_tooltip:bool, tooltip:Gtk.Tooltip) -> bool """
        pass

    def do_queue_draw_region(self, *args, **kwargs): # real signature unknown
        """ queue_draw_region(self, region:cairo.Region) """
        pass

    def do_realize(self, *args, **kwargs): # real signature unknown
        """ realize(self) """
        pass

    def do_screen_changed(self, *args, **kwargs): # real signature unknown
        """ screen_changed(self, previous_screen:Gdk.Screen) """
        pass

    def do_scroll_event(self, *args, **kwargs): # real signature unknown
        """ scroll_event(self, event:Gdk.EventScroll) -> bool """
        pass

    def do_selection_clear_event(self, *args, **kwargs): # real signature unknown
        """ selection_clear_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_selection_get(self, *args, **kwargs): # real signature unknown
        """ selection_get(self, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_selection_notify_event(self, *args, **kwargs): # real signature unknown
        """ selection_notify_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_selection_received(self, *args, **kwargs): # real signature unknown
        """ selection_received(self, selection_data:Gtk.SelectionData, time_:int) """
        pass

    def do_selection_request_event(self, *args, **kwargs): # real signature unknown
        """ selection_request_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_show(self, *args, **kwargs): # real signature unknown
        """ show(self) """
        pass

    def do_show_all(self, *args, **kwargs): # real signature unknown
        """ show_all(self) """
        pass

    def do_show_help(self, *args, **kwargs): # real signature unknown
        """ show_help(self, help_type:Gtk.WidgetHelpType) -> bool """
        pass

    def do_size_allocate(self, *args, **kwargs): # real signature unknown
        """ size_allocate(self, allocation:Gdk.Rectangle) """
        pass

    def do_state_changed(self, *args, **kwargs): # real signature unknown
        """ state_changed(self, previous_state:Gtk.StateType) """
        pass

    def do_state_flags_changed(self, *args, **kwargs): # real signature unknown
        """ state_flags_changed(self, previous_state_flags:Gtk.StateFlags) """
        pass

    def do_style_set(self, *args, **kwargs): # real signature unknown
        """ style_set(self, previous_style:Gtk.Style) """
        pass

    def do_style_updated(self, *args, **kwargs): # real signature unknown
        """ style_updated(self) """
        pass

    def do_touch_event(self, *args, **kwargs): # real signature unknown
        """ touch_event(self, event:Gdk.EventTouch) -> bool """
        pass

    def do_unmap(self, *args, **kwargs): # real signature unknown
        """ unmap(self) """
        pass

    def do_unmap_event(self, *args, **kwargs): # real signature unknown
        """ unmap_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_unrealize(self, *args, **kwargs): # real signature unknown
        """ unrealize(self) """
        pass

    def do_visibility_notify_event(self, *args, **kwargs): # real signature unknown
        """ visibility_notify_event(self, event:Gdk.EventVisibility) -> bool """
        pass

    def do_window_state_event(self, *args, **kwargs): # real signature unknown
        """ window_state_event(self, event:Gdk.EventWindowState) -> bool """
        pass

    def drag_begin(self, targets, actions, button, event=None): # real signature unknown; restored from __doc__
        """ drag_begin(self, targets:Gtk.TargetList, actions:Gdk.DragAction, button:int, event:Gdk.Event=None) -> Gdk.DragContext """
        pass

    def drag_begin_with_coordinates(self, targets, actions, button, event=None, x, y): # real signature unknown; restored from __doc__
        """ drag_begin_with_coordinates(self, targets:Gtk.TargetList, actions:Gdk.DragAction, button:int, event:Gdk.Event=None, x:int, y:int) -> Gdk.DragContext """
        pass

    def drag_check_threshold(self, start_x, start_y, current_x, current_y): # real signature unknown; restored from __doc__
        """ drag_check_threshold(self, start_x:int, start_y:int, current_x:int, current_y:int) -> bool """
        return False

    def drag_dest_add_image_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_image_targets(self) """
        pass

    def drag_dest_add_text_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_text_targets(self) """
        pass

    def drag_dest_add_uri_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_uri_targets(self) """
        pass

    def drag_dest_find_target(self, context, target_list=None): # real signature unknown; restored from __doc__
        """ drag_dest_find_target(self, context:Gdk.DragContext, target_list:Gtk.TargetList=None) -> Gdk.Atom """
        pass

    def drag_dest_get_target_list(self): # real signature unknown; restored from __doc__
        """ drag_dest_get_target_list(self) -> Gtk.TargetList or None """
        pass

    def drag_dest_get_track_motion(self): # real signature unknown; restored from __doc__
        """ drag_dest_get_track_motion(self) -> bool """
        return False

    def drag_dest_set(self, flags, targets=None, actions): # real signature unknown; restored from __doc__
        """ drag_dest_set(self, flags:Gtk.DestDefaults, targets:list=None, actions:Gdk.DragAction) """
        pass

    def drag_dest_set_proxy(self, proxy_window, protocol, use_coordinates): # real signature unknown; restored from __doc__
        """ drag_dest_set_proxy(self, proxy_window:Gdk.Window, protocol:Gdk.DragProtocol, use_coordinates:bool) """
        pass

    def drag_dest_set_target_list(self, target_list): # reliably restored by inspect
        # no doc
        pass

    def drag_dest_set_track_motion(self, track_motion): # real signature unknown; restored from __doc__
        """ drag_dest_set_track_motion(self, track_motion:bool) """
        pass

    def drag_dest_unset(self): # real signature unknown; restored from __doc__
        """ drag_dest_unset(self) """
        pass

    def drag_get_data(self, context, target, time_): # real signature unknown; restored from __doc__
        """ drag_get_data(self, context:Gdk.DragContext, target:Gdk.Atom, time_:int) """
        pass

    def drag_highlight(self): # real signature unknown; restored from __doc__
        """ drag_highlight(self) """
        pass

    def drag_source_add_image_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_image_targets(self) """
        pass

    def drag_source_add_text_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_text_targets(self) """
        pass

    def drag_source_add_uri_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_uri_targets(self) """
        pass

    def drag_source_get_target_list(self): # real signature unknown; restored from __doc__
        """ drag_source_get_target_list(self) -> Gtk.TargetList or None """
        pass

    def drag_source_set(self, start_button_mask, targets=None, actions): # real signature unknown; restored from __doc__
        """ drag_source_set(self, start_button_mask:Gdk.ModifierType, targets:list=None, actions:Gdk.DragAction) """
        pass

    def drag_source_set_icon_gicon(self, icon): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_gicon(self, icon:Gio.Icon) """
        pass

    def drag_source_set_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_name(self, icon_name:str) """
        pass

    def drag_source_set_icon_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf) """
        pass

    def drag_source_set_icon_stock(self, stock_id): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_stock(self, stock_id:str) """
        pass

    def drag_source_set_target_list(self, target_list): # reliably restored by inspect
        # no doc
        pass

    def drag_source_unset(self): # real signature unknown; restored from __doc__
        """ drag_source_unset(self) """
        pass

    def drag_unhighlight(self): # real signature unknown; restored from __doc__
        """ drag_unhighlight(self) """
        pass

    def draw(self, cr): # real signature unknown; restored from __doc__
        """ draw(self, cr:cairo.Context) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_style(self): # real signature unknown; restored from __doc__
        """ ensure_style(self) """
        pass

    def error_bell(self): # real signature unknown; restored from __doc__
        """ error_bell(self) """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event:Gdk.Event) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_style_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_style_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_child_notify(self): # reliably restored by inspect
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

    def get_accessible(self): # real signature unknown; restored from __doc__
        """ get_accessible(self) -> Atk.Object """
        pass

    def get_action_group(self, prefix): # real signature unknown; restored from __doc__
        """ get_action_group(self, prefix:str) -> Gio.ActionGroup or None """
        pass

    def get_allocated_baseline(self): # real signature unknown; restored from __doc__
        """ get_allocated_baseline(self) -> int """
        return 0

    def get_allocated_height(self): # real signature unknown; restored from __doc__
        """ get_allocated_height(self) -> int """
        return 0

    def get_allocated_size(self): # real signature unknown; restored from __doc__
        """ get_allocated_size(self) -> allocation:Gdk.Rectangle, baseline:int """
        pass

    def get_allocated_width(self): # real signature unknown; restored from __doc__
        """ get_allocated_width(self) -> int """
        return 0

    def get_allocation(self): # real signature unknown; restored from __doc__
        """ get_allocation(self) -> allocation:Gdk.Rectangle """
        pass

    def get_ancestor(self, widget_type): # real signature unknown; restored from __doc__
        """ get_ancestor(self, widget_type:GType) -> Gtk.Widget or None """
        pass

    def get_app_paintable(self): # real signature unknown; restored from __doc__
        """ get_app_paintable(self) -> bool """
        return False

    def get_can_default(self): # real signature unknown; restored from __doc__
        """ get_can_default(self) -> bool """
        return False

    def get_can_focus(self): # real signature unknown; restored from __doc__
        """ get_can_focus(self) -> bool """
        return False

    def get_child_requisition(self): # real signature unknown; restored from __doc__
        """ get_child_requisition(self) -> requisition:Gtk.Requisition """
        pass

    def get_child_visible(self): # real signature unknown; restored from __doc__
        """ get_child_visible(self) -> bool """
        return False

    def get_clip(self): # real signature unknown; restored from __doc__
        """ get_clip(self) -> clip:Gdk.Rectangle """
        pass

    def get_clipboard(self, selection): # real signature unknown; restored from __doc__
        """ get_clipboard(self, selection:Gdk.Atom) -> Gtk.Clipboard """
        pass

    def get_compat(self): # real signature unknown; restored from __doc__
        """ get_compat(self) -> str """
        return ""

    def get_composite_name(self): # real signature unknown; restored from __doc__
        """ get_composite_name(self) -> str """
        return ""

    def get_css_name(self): # real signature unknown; restored from __doc__
        """ get_css_name(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_direction(self): # real signature unknown; restored from __doc__
        """ get_default_direction() -> Gtk.TextDirection """
        pass

    def get_default_style(self): # real signature unknown; restored from __doc__
        """ get_default_style() -> Gtk.Style """
        pass

    def get_device_enabled(self, device): # real signature unknown; restored from __doc__
        """ get_device_enabled(self, device:Gdk.Device) -> bool """
        return False

    def get_device_events(self, device): # real signature unknown; restored from __doc__
        """ get_device_events(self, device:Gdk.Device) -> Gdk.EventMask """
        pass

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> Gtk.TextDirection """
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> Gdk.Display """
        pass

    def get_double_buffered(self): # real signature unknown; restored from __doc__
        """ get_double_buffered(self) -> bool """
        return False

    def get_events(self): # real signature unknown; restored from __doc__
        """ get_events(self) -> int """
        return 0

    def get_focus_on_click(self): # real signature unknown; restored from __doc__
        """ get_focus_on_click(self) -> bool """
        return False

    def get_font_map(self): # real signature unknown; restored from __doc__
        """ get_font_map(self) -> Pango.FontMap or None """
        pass

    def get_font_options(self): # real signature unknown; restored from __doc__
        """ get_font_options(self) -> cairo.FontOptions or None """
        pass

    def get_frame_clock(self): # real signature unknown; restored from __doc__
        """ get_frame_clock(self) -> Gdk.FrameClock or None """
        pass

    def get_geometry(self): # real signature unknown; restored from __doc__
        """ get_geometry(self) -> str """
        return ""

    def get_halign(self): # real signature unknown; restored from __doc__
        """ get_halign(self) -> Gtk.Align """
        pass

    def get_has_tooltip(self): # real signature unknown; restored from __doc__
        """ get_has_tooltip(self) -> bool """
        return False

    def get_has_window(self): # real signature unknown; restored from __doc__
        """ get_has_window(self) -> bool """
        return False

    def get_hexpand(self): # real signature unknown; restored from __doc__
        """ get_hexpand(self) -> bool """
        return False

    def get_hexpand_set(self): # real signature unknown; restored from __doc__
        """ get_hexpand_set(self) -> bool """
        return False

    def get_internal_child(self, builder, childname): # real signature unknown; restored from __doc__
        """ get_internal_child(self, builder:Gtk.Builder, childname:str) -> GObject.Object """
        pass

    def get_keycodes(self): # real signature unknown; restored from __doc__
        """ get_keycodes(self) -> str """
        return ""

    def get_mapped(self): # real signature unknown; restored from __doc__
        """ get_mapped(self) -> bool """
        return False

    def get_margin_bottom(self): # real signature unknown; restored from __doc__
        """ get_margin_bottom(self) -> int """
        return 0

    def get_margin_end(self): # real signature unknown; restored from __doc__
        """ get_margin_end(self) -> int """
        return 0

    def get_margin_left(self): # real signature unknown; restored from __doc__
        """ get_margin_left(self) -> int """
        return 0

    def get_margin_right(self): # real signature unknown; restored from __doc__
        """ get_margin_right(self) -> int """
        return 0

    def get_margin_start(self): # real signature unknown; restored from __doc__
        """ get_margin_start(self) -> int """
        return 0

    def get_margin_top(self): # real signature unknown; restored from __doc__
        """ get_margin_top(self) -> int """
        return 0

    def get_modifier_mask(self, intent): # real signature unknown; restored from __doc__
        """ get_modifier_mask(self, intent:Gdk.ModifierIntent) -> Gdk.ModifierType """
        pass

    def get_modifier_style(self): # real signature unknown; restored from __doc__
        """ get_modifier_style(self) -> Gtk.RcStyle """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_no_show_all(self): # real signature unknown; restored from __doc__
        """ get_no_show_all(self) -> bool """
        return False

    def get_opacity(self): # real signature unknown; restored from __doc__
        """ get_opacity(self) -> float """
        return 0.0

    def get_pango_context(self): # real signature unknown; restored from __doc__
        """ get_pango_context(self) -> Pango.Context """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gtk.Widget or None """
        pass

    def get_parent_window(self): # real signature unknown; restored from __doc__
        """ get_parent_window(self) -> Gdk.Window or None """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gtk.WidgetPath """
        pass

    def get_pointer(self): # real signature unknown; restored from __doc__
        """ get_pointer(self) -> x:int, y:int """
        pass

    def get_preferred_height(self): # real signature unknown; restored from __doc__
        """ get_preferred_height(self) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_height_and_baseline_for_width(self, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_and_baseline_for_width(self, width:int) -> minimum_height:int, natural_height:int, minimum_baseline:int, natural_baseline:int """
        pass

    def get_preferred_height_for_width(self, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_for_width(self, width:int) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_size(self): # real signature unknown; restored from __doc__
        """ get_preferred_size(self) -> minimum_size:Gtk.Requisition, natural_size:Gtk.Requisition """
        pass

    def get_preferred_width(self): # real signature unknown; restored from __doc__
        """ get_preferred_width(self) -> minimum_width:int, natural_width:int """
        pass

    def get_preferred_width_for_height(self, height): # real signature unknown; restored from __doc__
        """ get_preferred_width_for_height(self, height:int) -> minimum_width:int, natural_width:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_realized(self): # real signature unknown; restored from __doc__
        """ get_realized(self) -> bool """
        return False

    def get_receives_default(self): # real signature unknown; restored from __doc__
        """ get_receives_default(self) -> bool """
        return False

    def get_request_mode(self): # real signature unknown; restored from __doc__
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def get_requisition(self): # real signature unknown; restored from __doc__
        """ get_requisition(self) -> requisition:Gtk.Requisition """
        pass

    def get_root_window(self): # real signature unknown; restored from __doc__
        """ get_root_window(self) -> Gdk.Window """
        pass

    def get_scale_factor(self): # real signature unknown; restored from __doc__
        """ get_scale_factor(self) -> int """
        return 0

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_sensitive(self): # real signature unknown; restored from __doc__
        """ get_sensitive(self) -> bool """
        return False

    def get_settings(self): # real signature unknown; restored from __doc__
        """ get_settings(self) -> Gtk.Settings """
        pass

    def get_size_request(self): # real signature unknown; restored from __doc__
        """ get_size_request(self) -> width:int, height:int """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Gtk.StateType """
        pass

    def get_state_flags(self): # real signature unknown; restored from __doc__
        """ get_state_flags(self) -> Gtk.StateFlags """
        pass

    def get_style(self): # real signature unknown; restored from __doc__
        """ get_style(self) -> Gtk.Style """
        pass

    def get_style_context(self): # real signature unknown; restored from __doc__
        """ get_style_context(self) -> Gtk.StyleContext """
        pass

    def get_support_multidevice(self): # real signature unknown; restored from __doc__
        """ get_support_multidevice(self) -> bool """
        return False

    def get_symbols(self): # real signature unknown; restored from __doc__
        """ get_symbols(self) -> str """
        return ""

    def get_template_child(self, widget_type, name): # real signature unknown; restored from __doc__
        """ get_template_child(self, widget_type:GType, name:str) -> GObject.Object """
        pass

    def get_tooltip_markup(self): # real signature unknown; restored from __doc__
        """ get_tooltip_markup(self) -> str or None """
        return ""

    def get_tooltip_text(self): # real signature unknown; restored from __doc__
        """ get_tooltip_text(self) -> str or None """
        return ""

    def get_tooltip_window(self): # real signature unknown; restored from __doc__
        """ get_tooltip_window(self) -> Gtk.Window """
        pass

    def get_toplevel(self): # real signature unknown; restored from __doc__
        """ get_toplevel(self) -> Gtk.Widget """
        pass

    def get_types(self): # real signature unknown; restored from __doc__
        """ get_types(self) -> str """
        return ""

    def get_valign(self): # real signature unknown; restored from __doc__
        """ get_valign(self) -> Gtk.Align """
        pass

    def get_valign_with_baseline(self): # real signature unknown; restored from __doc__
        """ get_valign_with_baseline(self) -> Gtk.Align """
        pass

    def get_vexpand(self): # real signature unknown; restored from __doc__
        """ get_vexpand(self) -> bool """
        return False

    def get_vexpand_set(self): # real signature unknown; restored from __doc__
        """ get_vexpand_set(self) -> bool """
        return False

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

    def get_visual(self): # real signature unknown; restored from __doc__
        """ get_visual(self) -> Gdk.Visual """
        pass

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> Gdk.Window or None """
        pass

    def grab_add(self): # real signature unknown; restored from __doc__
        """ grab_add(self) """
        pass

    def grab_default(self): # real signature unknown; restored from __doc__
        """ grab_default(self) """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) """
        pass

    def grab_remove(self): # real signature unknown; restored from __doc__
        """ grab_remove(self) """
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

    def has_default(self): # real signature unknown; restored from __doc__
        """ has_default(self) -> bool """
        return False

    def has_focus(self): # real signature unknown; restored from __doc__
        """ has_focus(self) -> bool """
        return False

    def has_grab(self): # real signature unknown; restored from __doc__
        """ has_grab(self) -> bool """
        return False

    def has_rc_style(self): # real signature unknown; restored from __doc__
        """ has_rc_style(self) -> bool """
        return False

    def has_screen(self): # real signature unknown; restored from __doc__
        """ has_screen(self) -> bool """
        return False

    def has_visible_focus(self): # real signature unknown; restored from __doc__
        """ has_visible_focus(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hide_on_delete(self): # real signature unknown; restored from __doc__
        """ hide_on_delete(self) -> bool """
        return False

    def init_template(self): # real signature unknown; restored from __doc__
        """ init_template(self) """
        pass

    def input_shape_combine_region(self, region=None): # real signature unknown; restored from __doc__
        """ input_shape_combine_region(self, region:cairo.Region=None) """
        pass

    def insert_action_group(self, name, group=None): # real signature unknown; restored from __doc__
        """ insert_action_group(self, name:str, group:Gio.ActionGroup=None) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_style_property(self, pspec): # real signature unknown; restored from __doc__
        """ install_style_property(self, pspec:GObject.ParamSpec) """
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

    def intersect(self, area): # real signature unknown; restored from __doc__
        """ intersect(self, area:Gdk.Rectangle) -> bool, intersection:Gdk.Rectangle """
        return False

    def in_destruction(self): # real signature unknown; restored from __doc__
        """ in_destruction(self) -> bool """
        return False

    def is_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ is_ancestor(self, ancestor:Gtk.Widget) -> bool """
        return False

    def is_composited(self): # real signature unknown; restored from __doc__
        """ is_composited(self) -> bool """
        return False

    def is_drawable(self): # real signature unknown; restored from __doc__
        """ is_drawable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_focus(self): # real signature unknown; restored from __doc__
        """ is_focus(self) -> bool """
        return False

    def is_sensitive(self): # real signature unknown; restored from __doc__
        """ is_sensitive(self) -> bool """
        return False

    def is_toplevel(self): # real signature unknown; restored from __doc__
        """ is_toplevel(self) -> bool """
        return False

    def is_visible(self): # real signature unknown; restored from __doc__
        """ is_visible(self) -> bool """
        return False

    def keynav_failed(self, direction): # real signature unknown; restored from __doc__
        """ keynav_failed(self, direction:Gtk.DirectionType) -> bool """
        return False

    def list_accel_closures(self): # real signature unknown; restored from __doc__
        """ list_accel_closures(self) -> list """
        return []

    def list_action_prefixes(self): # real signature unknown; restored from __doc__
        """ list_action_prefixes(self) -> list """
        return []

    def list_mnemonic_labels(self): # real signature unknown; restored from __doc__
        """ list_mnemonic_labels(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_style_properties(self): # real signature unknown; restored from __doc__
        """ list_style_properties(self) -> list, n_properties:int """
        return []

    def map(self): # real signature unknown; restored from __doc__
        """ map(self) """
        pass

    def mnemonic_activate(self, group_cycling): # real signature unknown; restored from __doc__
        """ mnemonic_activate(self, group_cycling:bool) -> bool """
        return False

    def modify_base(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_base(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_bg(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_bg(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_cursor(self, primary=None, secondary=None): # real signature unknown; restored from __doc__
        """ modify_cursor(self, primary:Gdk.Color=None, secondary:Gdk.Color=None) """
        pass

    def modify_fg(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_fg(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_font(self, font_desc=None): # real signature unknown; restored from __doc__
        """ modify_font(self, font_desc:Pango.FontDescription=None) """
        pass

    def modify_style(self, style): # real signature unknown; restored from __doc__
        """ modify_style(self, style:Gtk.RcStyle) """
        pass

    def modify_text(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_text(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gtk.Widget """
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

    def override_background_color(self, state, color=None): # real signature unknown; restored from __doc__
        """ override_background_color(self, state:Gtk.StateFlags, color:Gdk.RGBA=None) """
        pass

    def override_color(self, state, color=None): # real signature unknown; restored from __doc__
        """ override_color(self, state:Gtk.StateFlags, color:Gdk.RGBA=None) """
        pass

    def override_cursor(self, cursor=None, secondary_cursor=None): # real signature unknown; restored from __doc__
        """ override_cursor(self, cursor:Gdk.RGBA=None, secondary_cursor:Gdk.RGBA=None) """
        pass

    def override_font(self, font_desc=None): # real signature unknown; restored from __doc__
        """ override_font(self, font_desc:Pango.FontDescription=None) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def override_symbolic_color(self, name, color=None): # real signature unknown; restored from __doc__
        """ override_symbolic_color(self, name:str, color:Gdk.RGBA=None) """
        pass

    def parser_finished(self, builder): # real signature unknown; restored from __doc__
        """ parser_finished(self, builder:Gtk.Builder) """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> path_length:int, path:str, path_reversed:str """
        pass

    def pop_composite_child(self): # real signature unknown; restored from __doc__
        """ pop_composite_child() """
        pass

    def print_(self, parent_window, description): # real signature unknown; restored from __doc__
        """ print_(self, parent_window:Gtk.Window, description:str) """
        pass

    def push_composite_child(self): # real signature unknown; restored from __doc__
        """ push_composite_child() """
        pass

    def queue_allocate(self): # real signature unknown; restored from __doc__
        """ queue_allocate(self) """
        pass

    def queue_compute_expand(self): # real signature unknown; restored from __doc__
        """ queue_compute_expand(self) """
        pass

    def queue_draw(self): # real signature unknown; restored from __doc__
        """ queue_draw(self) """
        pass

    def queue_draw_area(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ queue_draw_area(self, x:int, y:int, width:int, height:int) """
        pass

    def queue_draw_region(self, region): # real signature unknown; restored from __doc__
        """ queue_draw_region(self, region:cairo.Region) """
        pass

    def queue_resize(self): # real signature unknown; restored from __doc__
        """ queue_resize(self) """
        pass

    def queue_resize_no_redraw(self): # real signature unknown; restored from __doc__
        """ queue_resize_no_redraw(self) """
        pass

    def realize(self): # real signature unknown; restored from __doc__
        """ realize(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def region_intersect(self, region): # real signature unknown; restored from __doc__
        """ region_intersect(self, region:cairo.Region) -> cairo.Region """
        pass

    def register_window(self, window): # real signature unknown; restored from __doc__
        """ register_window(self, window:Gdk.Window) """
        pass

    def remove_accelerator(self, accel_group, accel_key, accel_mods): # real signature unknown; restored from __doc__
        """ remove_accelerator(self, accel_group:Gtk.AccelGroup, accel_key:int, accel_mods:Gdk.ModifierType) -> bool """
        return False

    def remove_mnemonic_label(self, label): # real signature unknown; restored from __doc__
        """ remove_mnemonic_label(self, label:Gtk.Widget) """
        pass

    def remove_tick_callback(self, id): # real signature unknown; restored from __doc__
        """ remove_tick_callback(self, id:int) """
        pass

    def render(self, cr, layout, x, y, width, height, dpi_x, dpi_y): # real signature unknown; restored from __doc__
        """ render(self, cr:cairo.Context, layout:Pango.Layout, x:float, y:float, width:float, height:float, dpi_x:float, dpi_y:float) -> bool """
        return False

    def render_icon(self, stock_id, size, detail=None): # real signature unknown; restored from __doc__
        """ render_icon(self, stock_id:str, size:int, detail:str=None) -> GdkPixbuf.Pixbuf or None """
        pass

    def render_icon_pixbuf(self, stock_id, size): # real signature unknown; restored from __doc__
        """ render_icon_pixbuf(self, stock_id:str, size:int) -> GdkPixbuf.Pixbuf or None """
        pass

    def reparent(self, new_parent): # real signature unknown; restored from __doc__
        """ reparent(self, new_parent:Gtk.Widget) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset_rc_styles(self): # real signature unknown; restored from __doc__
        """ reset_rc_styles(self) """
        pass

    def reset_style(self): # real signature unknown; restored from __doc__
        """ reset_style(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def send_expose(self, event): # real signature unknown; restored from __doc__
        """ send_expose(self, event:Gdk.Event) -> int """
        return 0

    def send_focus_change(self, event): # real signature unknown; restored from __doc__
        """ send_focus_change(self, event:Gdk.Event) -> bool """
        return False

    def set_accel_path(self, accel_path=None, accel_group=None): # real signature unknown; restored from __doc__
        """ set_accel_path(self, accel_path:str=None, accel_group:Gtk.AccelGroup=None) """
        pass

    def set_accessible_role(self, role): # real signature unknown; restored from __doc__
        """ set_accessible_role(self, role:Atk.Role) """
        pass

    def set_accessible_type(self, type): # real signature unknown; restored from __doc__
        """ set_accessible_type(self, type:GType) """
        pass

    def set_allocation(self, allocation): # real signature unknown; restored from __doc__
        """ set_allocation(self, allocation:Gdk.Rectangle) """
        pass

    def set_app_paintable(self, app_paintable): # real signature unknown; restored from __doc__
        """ set_app_paintable(self, app_paintable:bool) """
        pass

    def set_buildable_property(self, builder, name, value): # real signature unknown; restored from __doc__
        """ set_buildable_property(self, builder:Gtk.Builder, name:str, value:GObject.Value) """
        pass

    def set_can_default(self, can_default): # real signature unknown; restored from __doc__
        """ set_can_default(self, can_default:bool) """
        pass

    def set_can_focus(self, can_focus): # real signature unknown; restored from __doc__
        """ set_can_focus(self, can_focus:bool) """
        pass

    def set_child_visible(self, is_visible): # real signature unknown; restored from __doc__
        """ set_child_visible(self, is_visible:bool) """
        pass

    def set_clip(self, clip): # real signature unknown; restored from __doc__
        """ set_clip(self, clip:Gdk.Rectangle) """
        pass

    def set_composite_name(self, name): # real signature unknown; restored from __doc__
        """ set_composite_name(self, name:str) """
        pass

    def set_connect_func(self, connect_func, connect_data=None): # real signature unknown; restored from __doc__
        """ set_connect_func(self, connect_func:Gtk.BuilderConnectFunc, connect_data=None) """
        pass

    def set_css_name(self, name): # real signature unknown; restored from __doc__
        """ set_css_name(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_direction(self, dir): # real signature unknown; restored from __doc__
        """ set_default_direction(dir:Gtk.TextDirection) """
        pass

    def set_device_enabled(self, device, enabled): # real signature unknown; restored from __doc__
        """ set_device_enabled(self, device:Gdk.Device, enabled:bool) """
        pass

    def set_device_events(self, device, events): # real signature unknown; restored from __doc__
        """ set_device_events(self, device:Gdk.Device, events:Gdk.EventMask) """
        pass

    def set_direction(self, dir): # real signature unknown; restored from __doc__
        """ set_direction(self, dir:Gtk.TextDirection) """
        pass

    def set_double_buffered(self, double_buffered): # real signature unknown; restored from __doc__
        """ set_double_buffered(self, double_buffered:bool) """
        pass

    def set_events(self, events): # real signature unknown; restored from __doc__
        """ set_events(self, events:int) """
        pass

    def set_focus_on_click(self, focus_on_click): # real signature unknown; restored from __doc__
        """ set_focus_on_click(self, focus_on_click:bool) """
        pass

    def set_font_map(self, font_map=None): # real signature unknown; restored from __doc__
        """ set_font_map(self, font_map:Pango.FontMap=None) """
        pass

    def set_font_options(self, options=None): # real signature unknown; restored from __doc__
        """ set_font_options(self, options:cairo.FontOptions=None) """
        pass

    def set_groups_levels(self, groupLevels): # real signature unknown; restored from __doc__
        """ set_groups_levels(self, groupLevels:Gkbd.KeyboardDrawingGroupLevel) """
        pass

    def set_halign(self, align): # real signature unknown; restored from __doc__
        """ set_halign(self, align:Gtk.Align) """
        pass

    def set_has_tooltip(self, has_tooltip): # real signature unknown; restored from __doc__
        """ set_has_tooltip(self, has_tooltip:bool) """
        pass

    def set_has_window(self, has_window): # real signature unknown; restored from __doc__
        """ set_has_window(self, has_window:bool) """
        pass

    def set_hexpand(self, expand): # real signature unknown; restored from __doc__
        """ set_hexpand(self, expand:bool) """
        pass

    def set_hexpand_set(self, set): # real signature unknown; restored from __doc__
        """ set_hexpand_set(self, set:bool) """
        pass

    def set_layout(self, id): # real signature unknown; restored from __doc__
        """ set_layout(self, id:str) """
        pass

    def set_mapped(self, mapped): # real signature unknown; restored from __doc__
        """ set_mapped(self, mapped:bool) """
        pass

    def set_margin_bottom(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_bottom(self, margin:int) """
        pass

    def set_margin_end(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_end(self, margin:int) """
        pass

    def set_margin_left(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_left(self, margin:int) """
        pass

    def set_margin_right(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_right(self, margin:int) """
        pass

    def set_margin_start(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_start(self, margin:int) """
        pass

    def set_margin_top(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_top(self, margin:int) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_no_show_all(self, no_show_all): # real signature unknown; restored from __doc__
        """ set_no_show_all(self, no_show_all:bool) """
        pass

    def set_opacity(self, opacity): # real signature unknown; restored from __doc__
        """ set_opacity(self, opacity:float) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gtk.Widget) """
        pass

    def set_parent_window(self, parent_window): # real signature unknown; restored from __doc__
        """ set_parent_window(self, parent_window:Gdk.Window) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_realized(self, realized): # real signature unknown; restored from __doc__
        """ set_realized(self, realized:bool) """
        pass

    def set_receives_default(self, receives_default): # real signature unknown; restored from __doc__
        """ set_receives_default(self, receives_default:bool) """
        pass

    def set_redraw_on_allocate(self, redraw_on_allocate): # real signature unknown; restored from __doc__
        """ set_redraw_on_allocate(self, redraw_on_allocate:bool) """
        pass

    def set_sensitive(self, sensitive): # real signature unknown; restored from __doc__
        """ set_sensitive(self, sensitive:bool) """
        pass

    def set_size_request(self, width, height): # real signature unknown; restored from __doc__
        """ set_size_request(self, width:int, height:int) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Gtk.StateType) """
        pass

    def set_state_flags(self, flags, clear): # real signature unknown; restored from __doc__
        """ set_state_flags(self, flags:Gtk.StateFlags, clear:bool) """
        pass

    def set_style(self, style=None): # real signature unknown; restored from __doc__
        """ set_style(self, style:Gtk.Style=None) """
        pass

    def set_support_multidevice(self, support_multidevice): # real signature unknown; restored from __doc__
        """ set_support_multidevice(self, support_multidevice:bool) """
        pass

    def set_template(self, template_bytes): # real signature unknown; restored from __doc__
        """ set_template(self, template_bytes:GLib.Bytes) """
        pass

    def set_template_from_resource(self, resource_name): # real signature unknown; restored from __doc__
        """ set_template_from_resource(self, resource_name:str) """
        pass

    def set_tooltip_markup(self, markup=None): # real signature unknown; restored from __doc__
        """ set_tooltip_markup(self, markup:str=None) """
        pass

    def set_tooltip_text(self, text=None): # real signature unknown; restored from __doc__
        """ set_tooltip_text(self, text:str=None) """
        pass

    def set_tooltip_window(self, custom_window=None): # real signature unknown; restored from __doc__
        """ set_tooltip_window(self, custom_window:Gtk.Window=None) """
        pass

    def set_track_config(self, enable): # real signature unknown; restored from __doc__
        """ set_track_config(self, enable:bool) """
        pass

    def set_track_modifiers(self, enable): # real signature unknown; restored from __doc__
        """ set_track_modifiers(self, enable:bool) """
        pass

    def set_valign(self, align): # real signature unknown; restored from __doc__
        """ set_valign(self, align:Gtk.Align) """
        pass

    def set_vexpand(self, expand): # real signature unknown; restored from __doc__
        """ set_vexpand(self, expand:bool) """
        pass

    def set_vexpand_set(self, set): # real signature unknown; restored from __doc__
        """ set_vexpand_set(self, set:bool) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
        pass

    def set_visual(self, visual=None): # real signature unknown; restored from __doc__
        """ set_visual(self, visual:Gdk.Visual=None) """
        pass

    def set_window(self, window): # real signature unknown; restored from __doc__
        """ set_window(self, window:Gdk.Window) """
        pass

    def shape_combine_region(self, region=None): # real signature unknown; restored from __doc__
        """ shape_combine_region(self, region:cairo.Region=None) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def show_all(self): # real signature unknown; restored from __doc__
        """ show_all(self) """
        pass

    def show_now(self): # real signature unknown; restored from __doc__
        """ show_now(self) """
        pass

    def size_allocate(self, allocation): # real signature unknown; restored from __doc__
        """ size_allocate(self, allocation:Gdk.Rectangle) """
        pass

    def size_allocate_with_baseline(self, allocation, baseline): # real signature unknown; restored from __doc__
        """ size_allocate_with_baseline(self, allocation:Gdk.Rectangle, baseline:int) """
        pass

    def size_request(self): # real signature unknown; restored from __doc__
        """ size_request(self) -> requisition:Gtk.Requisition """
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

    def style_attach(self): # real signature unknown; restored from __doc__
        """ style_attach(self) """
        pass

    def style_get_property(self, property_name, value=None): # reliably restored by inspect
        # no doc
        pass

    def thaw_child_notify(self): # real signature unknown; restored from __doc__
        """ thaw_child_notify(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def translate_coordinates(*args, **kwargs): # reliably restored by inspect
        """ translate_coordinates(self, dest_widget:Gtk.Widget, src_x:int, src_y:int) -> bool, dest_x:int, dest_y:int """
        pass

    def trigger_tooltip_query(self): # real signature unknown; restored from __doc__
        """ trigger_tooltip_query(self) """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unrealize(self): # real signature unknown; restored from __doc__
        """ unrealize(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unregister_window(self, window): # real signature unknown; restored from __doc__
        """ unregister_window(self, window:Gdk.Window) """
        pass

    def unset_state_flags(self, flags): # real signature unknown; restored from __doc__
        """ unset_state_flags(self, flags:Gtk.StateFlags) """
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

    colors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    groupLevels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keyboard_items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    l3mod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    physical_indicators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    physical_indicators_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    renderContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    screen_num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    track_config = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    track_modifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    widget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xkb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xkbOnDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xkb_event_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb1731cb760>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(KeyboardDrawing), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType GkbdKeyboardDrawing (94195347824576)>, '__doc__': None, '__gsignals__': {}, 'dialog_new': gi.FunctionInfo(dialog_new), 'new': gi.FunctionInfo(new), 'dialog_set_group': gi.FunctionInfo(dialog_set_group), 'dialog_set_layout': gi.FunctionInfo(dialog_set_layout), 'get_compat': gi.FunctionInfo(get_compat), 'get_geometry': gi.FunctionInfo(get_geometry), 'get_keycodes': gi.FunctionInfo(get_keycodes), 'get_symbols': gi.FunctionInfo(get_symbols), 'get_types': gi.FunctionInfo(get_types), 'print_': gi.FunctionInfo(print), 'render': gi.FunctionInfo(render), 'set_groups_levels': gi.FunctionInfo(set_groups_levels), 'set_layout': gi.FunctionInfo(set_layout), 'set_track_config': gi.FunctionInfo(set_track_config), 'set_track_modifiers': gi.FunctionInfo(set_track_modifiers), 'do_bad_keycode': gi.VFuncInfo(bad_keycode), 'parent': <property object at 0x7fb1731bbdb0>, 'xkb': <property object at 0x7fb1731bbea0>, 'xkbOnDisplay': <property object at 0x7fb1731bbf90>, 'l3mod': <property object at 0x7fb1731bd0e0>, 'renderContext': <property object at 0x7fb1731bd1d0>, 'keys': <property object at 0x7fb1731bd2c0>, 'keyboard_items': <property object at 0x7fb1731bd3b0>, 'colors': <property object at 0x7fb1731bd4a0>, 'timeout': <property object at 0x7fb1731bd590>, 'groupLevels': <property object at 0x7fb1731bd680>, 'mods': <property object at 0x7fb1731bd770>, 'display': <property object at 0x7fb1731bd860>, 'screen_num': <property object at 0x7fb1731bd950>, 'xkb_event_type': <property object at 0x7fb1731bda40>, 'physical_indicators': <property object at 0x7fb1731bdb80>, 'physical_indicators_size': <property object at 0x7fb1731bdcc0>, 'track_config': <property object at 0x7fb1731bddb0>, 'track_modifiers': <property object at 0x7fb1731bdea0>})"
    __gdoc__ = "Object GkbdKeyboardDrawing\n\nSignals from GkbdKeyboardDrawing:\n  bad-keycode (guint)\n\nSignals from GtkWidget:\n  composited-changed ()\n  destroy ()\n  show ()\n  hide ()\n  map ()\n  unmap ()\n  realize ()\n  unrealize ()\n  size-allocate (GdkRectangle)\n  state-changed (GtkStateType)\n  state-flags-changed (GtkStateFlags)\n  parent-set (GtkWidget)\n  hierarchy-changed (GtkWidget)\n  style-set (GtkStyle)\n  style-updated ()\n  direction-changed (GtkTextDirection)\n  grab-notify (gboolean)\n  child-notify (GParam)\n  draw (CairoContext) -> gboolean\n  mnemonic-activate (gboolean) -> gboolean\n  grab-focus ()\n  focus (GtkDirectionType) -> gboolean\n  move-focus (GtkDirectionType)\n  keynav-failed (GtkDirectionType) -> gboolean\n  event (GdkEvent) -> gboolean\n  event-after (GdkEvent)\n  button-press-event (GdkEvent) -> gboolean\n  button-release-event (GdkEvent) -> gboolean\n  touch-event (GdkEvent) -> gboolean\n  scroll-event (GdkEvent) -> gboolean\n  motion-notify-event (GdkEvent) -> gboolean\n  delete-event (GdkEvent) -> gboolean\n  destroy-event (GdkEvent) -> gboolean\n  key-press-event (GdkEvent) -> gboolean\n  key-release-event (GdkEvent) -> gboolean\n  enter-notify-event (GdkEvent) -> gboolean\n  leave-notify-event (GdkEvent) -> gboolean\n  configure-event (GdkEvent) -> gboolean\n  focus-in-event (GdkEvent) -> gboolean\n  focus-out-event (GdkEvent) -> gboolean\n  map-event (GdkEvent) -> gboolean\n  unmap-event (GdkEvent) -> gboolean\n  property-notify-event (GdkEvent) -> gboolean\n  selection-clear-event (GdkEvent) -> gboolean\n  selection-request-event (GdkEvent) -> gboolean\n  selection-notify-event (GdkEvent) -> gboolean\n  selection-received (GtkSelectionData, guint)\n  selection-get (GtkSelectionData, guint, guint)\n  proximity-in-event (GdkEvent) -> gboolean\n  proximity-out-event (GdkEvent) -> gboolean\n  drag-leave (GdkDragContext, guint)\n  drag-begin (GdkDragContext)\n  drag-end (GdkDragContext)\n  drag-data-delete (GdkDragContext)\n  drag-failed (GdkDragContext, GtkDragResult) -> gboolean\n  drag-motion (GdkDragContext, gint, gint, guint) -> gboolean\n  drag-drop (GdkDragContext, gint, gint, guint) -> gboolean\n  drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)\n  drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)\n  visibility-notify-event (GdkEvent) -> gboolean\n  window-state-event (GdkEvent) -> gboolean\n  damage-event (GdkEvent) -> gboolean\n  grab-broken-event (GdkEvent) -> gboolean\n  query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean\n  popup-menu () -> gboolean\n  show-help (GtkWidgetHelpType) -> gboolean\n  accel-closures-changed ()\n  screen-changed (GdkScreen)\n  can-activate-accel (guint) -> gboolean\n\nProperties from GtkWidget:\n  name -> gchararray: Widget name\n    The name of the widget\n  parent -> GtkContainer: Parent widget\n    The parent widget of this widget. Must be a Container widget\n  width-request -> gint: Width request\n    Override for width request of the widget, or -1 if natural request should be used\n  height-request -> gint: Height request\n    Override for height request of the widget, or -1 if natural request should be used\n  visible -> gboolean: Visible\n    Whether the widget is visible\n  sensitive -> gboolean: Sensitive\n    Whether the widget responds to input\n  app-paintable -> gboolean: Application paintable\n    Whether the application will paint directly on the widget\n  can-focus -> gboolean: Can focus\n    Whether the widget can accept the input focus\n  has-focus -> gboolean: Has focus\n    Whether the widget has the input focus\n  is-focus -> gboolean: Is focus\n    Whether the widget is the focus widget within the toplevel\n  focus-on-click -> gboolean: Focus on click\n    Whether the widget should grab focus when it is clicked with the mouse\n  can-default -> gboolean: Can default\n    Whether the widget can be the default widget\n  has-default -> gboolean: Has default\n    Whether the widget is the default widget\n  receives-default -> gboolean: Receives default\n    If TRUE, the widget will receive the default action when it is focused\n  composite-child -> gboolean: Composite child\n    Whether the widget is part of a composite widget\n  style -> GtkStyle: Style\n    The style of the widget, which contains information about how it will look (colors etc)\n  events -> GdkEventMask: Events\n    The event mask that decides what kind of GdkEvents this widget gets\n  no-show-all -> gboolean: No show all\n    Whether gtk_widget_show_all() should not affect this widget\n  has-tooltip -> gboolean: Has tooltip\n    Whether this widget has a tooltip\n  tooltip-markup -> gchararray: Tooltip markup\n    The contents of the tooltip for this widget\n  tooltip-text -> gchararray: Tooltip Text\n    The contents of the tooltip for this widget\n  window -> GdkWindow: Window\n    The widget's window if it is realized\n  opacity -> gdouble: Opacity for Widget\n    The opacity of the widget, from 0 to 1\n  double-buffered -> gboolean: Double Buffered\n    Whether the widget is double buffered\n  halign -> GtkAlign: Horizontal Alignment\n    How to position in extra horizontal space\n  valign -> GtkAlign: Vertical Alignment\n    How to position in extra vertical space\n  margin-left -> gint: Margin on Left\n    Pixels of extra space on the left side\n  margin-right -> gint: Margin on Right\n    Pixels of extra space on the right side\n  margin-start -> gint: Margin on Start\n    Pixels of extra space on the start\n  margin-end -> gint: Margin on End\n    Pixels of extra space on the end\n  margin-top -> gint: Margin on Top\n    Pixels of extra space on the top side\n  margin-bottom -> gint: Margin on Bottom\n    Pixels of extra space on the bottom side\n  margin -> gint: All Margins\n    Pixels of extra space on all four sides\n  hexpand -> gboolean: Horizontal Expand\n    Whether widget wants more horizontal space\n  vexpand -> gboolean: Vertical Expand\n    Whether widget wants more vertical space\n  hexpand-set -> gboolean: Horizontal Expand Set\n    Whether to use the hexpand property\n  vexpand-set -> gboolean: Vertical Expand Set\n    Whether to use the vexpand property\n  expand -> gboolean: Expand Both\n    Whether widget wants to expand in both directions\n  scale-factor -> gint: Scale factor\n    The scaling factor of the window\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GkbdKeyboardDrawing (94195347824576)>'
    __info__ = ObjectInfo(KeyboardDrawing)


class KeyboardDrawingClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        KeyboardDrawingClass()
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

    bad_keycode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(KeyboardDrawingClass), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'KeyboardDrawingClass' objects>, '__weakref__': <attribute '__weakref__' of 'KeyboardDrawingClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fb1731bf040>, 'bad_keycode': <property object at 0x7fb1731bf130>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(KeyboardDrawingClass)


class KeyboardDrawingDoodad(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        KeyboardDrawingDoodad()
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

    angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    doodad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    on = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin_x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin_y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(KeyboardDrawingDoodad), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'KeyboardDrawingDoodad' objects>, '__weakref__': <attribute '__weakref__' of 'KeyboardDrawingDoodad' objects>, '__doc__': None, 'type': <property object at 0x7fb1731bf270>, 'origin_x': <property object at 0x7fb1731bf360>, 'origin_y': <property object at 0x7fb1731bf450>, 'angle': <property object at 0x7fb1731bf540>, 'priority': <property object at 0x7fb1731bf630>, 'doodad': <property object at 0x7fb1731bf720>, 'on': <property object at 0x7fb1731bf810>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(KeyboardDrawingDoodad)


class KeyboardDrawingGroupLevel(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        KeyboardDrawingGroupLevel()
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

    group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(KeyboardDrawingGroupLevel), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'KeyboardDrawingGroupLevel' objects>, '__weakref__': <attribute '__weakref__' of 'KeyboardDrawingGroupLevel' objects>, '__doc__': None, 'group': <property object at 0x7fb1731bf9a0>, 'level': <property object at 0x7fb1731bfa90>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(KeyboardDrawingGroupLevel)


class KeyboardDrawingGroupLevelPosition(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BOTTOMLEFT = 2
    BOTTOMRIGHT = 3
    FIRST = 0
    LAST = 3
    TOPLEFT = 0
    TOPRIGHT = 1
    TOTAL = 4
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gkbd', '__dict__': <attribute '__dict__' of 'KeyboardDrawingGroupLevelPosition' objects>, '__doc__': None, '__gtype__': <GType PyGkbdKeyboardDrawingGroupLevelPosition (94195347641728)>, '__enum_values__': {0: <enum GKBD_KEYBOARD_DRAWING_POS_TOPLEFT of type Gkbd.KeyboardDrawingGroupLevelPosition>, 1: <enum GKBD_KEYBOARD_DRAWING_POS_TOPRIGHT of type Gkbd.KeyboardDrawingGroupLevelPosition>, 2: <enum GKBD_KEYBOARD_DRAWING_POS_BOTTOMLEFT of type Gkbd.KeyboardDrawingGroupLevelPosition>, 3: <enum GKBD_KEYBOARD_DRAWING_POS_BOTTOMRIGHT of type Gkbd.KeyboardDrawingGroupLevelPosition>, 4: <enum GKBD_KEYBOARD_DRAWING_POS_TOTAL of type Gkbd.KeyboardDrawingGroupLevelPosition>}, '__info__': gi.EnumInfo(KeyboardDrawingGroupLevelPosition), 'TOPLEFT': <enum GKBD_KEYBOARD_DRAWING_POS_TOPLEFT of type Gkbd.KeyboardDrawingGroupLevelPosition>, 'TOPRIGHT': <enum GKBD_KEYBOARD_DRAWING_POS_TOPRIGHT of type Gkbd.KeyboardDrawingGroupLevelPosition>, 'BOTTOMLEFT': <enum GKBD_KEYBOARD_DRAWING_POS_BOTTOMLEFT of type Gkbd.KeyboardDrawingGroupLevelPosition>, 'BOTTOMRIGHT': <enum GKBD_KEYBOARD_DRAWING_POS_BOTTOMRIGHT of type Gkbd.KeyboardDrawingGroupLevelPosition>, 'TOTAL': <enum GKBD_KEYBOARD_DRAWING_POS_TOTAL of type Gkbd.KeyboardDrawingGroupLevelPosition>, 'FIRST': <enum GKBD_KEYBOARD_DRAWING_POS_TOPLEFT of type Gkbd.KeyboardDrawingGroupLevelPosition>, 'LAST': <enum GKBD_KEYBOARD_DRAWING_POS_BOTTOMRIGHT of type Gkbd.KeyboardDrawingGroupLevelPosition>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    __gtype__ = None # (!) real value is '<GType PyGkbdKeyboardDrawingGroupLevelPosition (94195347641728)>'
    __info__ = gi.EnumInfo(KeyboardDrawingGroupLevelPosition)


class KeyboardDrawingItem(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        KeyboardDrawingItem()
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

    angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin_x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin_y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(KeyboardDrawingItem), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'KeyboardDrawingItem' objects>, '__weakref__': <attribute '__weakref__' of 'KeyboardDrawingItem' objects>, '__doc__': None, 'type': <property object at 0x7fb1731bfef0>, 'origin_x': <property object at 0x7fb1731c1040>, 'origin_y': <property object at 0x7fb1731c1130>, 'angle': <property object at 0x7fb1731c1220>, 'priority': <property object at 0x7fb1731c1310>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(KeyboardDrawingItem)


class KeyboardDrawingItemType(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DOODAD = 3
    INVALID = 0
    KEY = 1
    KEY_EXTRA = 2
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gkbd', '__dict__': <attribute '__dict__' of 'KeyboardDrawingItemType' objects>, '__doc__': None, '__gtype__': <GType PyGkbdKeyboardDrawingItemType (94195347836944)>, '__enum_values__': {0: <enum GKBD_KEYBOARD_DRAWING_ITEM_TYPE_INVALID of type Gkbd.KeyboardDrawingItemType>, 1: <enum GKBD_KEYBOARD_DRAWING_ITEM_TYPE_KEY of type Gkbd.KeyboardDrawingItemType>, 2: <enum GKBD_KEYBOARD_DRAWING_ITEM_TYPE_KEY_EXTRA of type Gkbd.KeyboardDrawingItemType>, 3: <enum GKBD_KEYBOARD_DRAWING_ITEM_TYPE_DOODAD of type Gkbd.KeyboardDrawingItemType>}, '__info__': gi.EnumInfo(KeyboardDrawingItemType), 'INVALID': <enum GKBD_KEYBOARD_DRAWING_ITEM_TYPE_INVALID of type Gkbd.KeyboardDrawingItemType>, 'KEY': <enum GKBD_KEYBOARD_DRAWING_ITEM_TYPE_KEY of type Gkbd.KeyboardDrawingItemType>, 'KEY_EXTRA': <enum GKBD_KEYBOARD_DRAWING_ITEM_TYPE_KEY_EXTRA of type Gkbd.KeyboardDrawingItemType>, 'DOODAD': <enum GKBD_KEYBOARD_DRAWING_ITEM_TYPE_DOODAD of type Gkbd.KeyboardDrawingItemType>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }
    __gtype__ = None # (!) real value is '<GType PyGkbdKeyboardDrawingItemType (94195347836944)>'
    __info__ = gi.EnumInfo(KeyboardDrawingItemType)


class KeyboardDrawingKey(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        KeyboardDrawingKey()
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

    angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keycode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin_x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin_y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pressed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xkbkey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(KeyboardDrawingKey), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'KeyboardDrawingKey' objects>, '__weakref__': <attribute '__weakref__' of 'KeyboardDrawingKey' objects>, '__doc__': None, 'type': <property object at 0x7fb1731c16d0>, 'origin_x': <property object at 0x7fb1731c17c0>, 'origin_y': <property object at 0x7fb1731c18b0>, 'angle': <property object at 0x7fb1731c19a0>, 'priority': <property object at 0x7fb1731c1a90>, 'xkbkey': <property object at 0x7fb1731c1b80>, 'pressed': <property object at 0x7fb1731c1c70>, 'keycode': <property object at 0x7fb1731c1d60>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(KeyboardDrawingKey)


class KeyboardDrawingRenderContext(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        KeyboardDrawingRenderContext()
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

    angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dark_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font_desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scale_denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scale_numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(KeyboardDrawingRenderContext), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'KeyboardDrawingRenderContext' objects>, '__weakref__': <attribute '__weakref__' of 'KeyboardDrawingRenderContext' objects>, '__doc__': None, 'cr': <property object at 0x7fb1731c1ef0>, 'angle': <property object at 0x7fb1731c4040>, 'layout': <property object at 0x7fb1731c4130>, 'font_desc': <property object at 0x7fb1731c4220>, 'scale_numerator': <property object at 0x7fb1731c4310>, 'scale_denominator': <property object at 0x7fb1731c4450>, 'dark_color': <property object at 0x7fb1731c4540>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(KeyboardDrawingRenderContext)


class Status(__gi_repository_Gtk.StatusIcon):
    """
    :Constructors:
    
    ::
    
        Status(**properties)
        new() -> Gtk.StatusIcon
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

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self) """
        pass

    def do_button_press_event(self, *args, **kwargs): # real signature unknown
        """ button_press_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_button_release_event(self, *args, **kwargs): # real signature unknown
        """ button_release_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_popup_menu(self, *args, **kwargs): # real signature unknown
        """ popup_menu(self, button:int, activate_time:int) """
        pass

    def do_query_tooltip(self, *args, **kwargs): # real signature unknown
        """ query_tooltip(self, x:int, y:int, keyboard_mode:bool, tooltip:Gtk.Tooltip) -> bool """
        pass

    def do_scroll_event(self, *args, **kwargs): # real signature unknown
        """ scroll_event(self, event:Gdk.EventScroll) -> bool """
        pass

    def do_size_changed(self, *args, **kwargs): # real signature unknown
        """ size_changed(self, size:int) -> bool """
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

    def get_geometry(self): # real signature unknown; restored from __doc__
        """ get_geometry(self) -> bool, screen:Gdk.Screen, area:Gdk.Rectangle, orientation:Gtk.Orientation """
        return False

    def get_gicon(self): # real signature unknown; restored from __doc__
        """ get_gicon(self) -> Gio.Icon or None """
        pass

    def get_group_names(self): # real signature unknown; restored from __doc__
        """ get_group_names() -> list """
        return []

    def get_has_tooltip(self): # real signature unknown; restored from __doc__
        """ get_has_tooltip(self) -> bool """
        return False

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str or None """
        return ""

    def get_image_filename(self, group): # real signature unknown; restored from __doc__
        """ get_image_filename(group:int) -> str """
        return ""

    def get_pixbuf(self): # real signature unknown; restored from __doc__
        """ get_pixbuf(self) -> GdkPixbuf.Pixbuf or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_stock(self): # real signature unknown; restored from __doc__
        """ get_stock(self) -> str or None """
        return ""

    def get_storage_type(self): # real signature unknown; restored from __doc__
        """ get_storage_type(self) -> Gtk.ImageType """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_tooltip_markup(self): # real signature unknown; restored from __doc__
        """ get_tooltip_markup(self) -> str or None """
        return ""

    def get_tooltip_text(self): # real signature unknown; restored from __doc__
        """ get_tooltip_text(self) -> str or None """
        return ""

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

    def get_x11_window_id(self): # real signature unknown; restored from __doc__
        """ get_x11_window_id(self) -> int """
        return 0

    def get_xkl_engine(self): # real signature unknown; restored from __doc__
        """ get_xkl_engine() -> Xkl.Engine """
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

    def is_embedded(self): # real signature unknown; restored from __doc__
        """ is_embedded(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gtk.StatusIcon """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_file(self, filename): # real signature unknown; restored from __doc__
        """ new_from_file(filename:str) -> Gtk.StatusIcon """
        pass

    def new_from_gicon(self, icon): # real signature unknown; restored from __doc__
        """ new_from_gicon(icon:Gio.Icon) -> Gtk.StatusIcon """
        pass

    def new_from_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ new_from_icon_name(icon_name:str) -> Gtk.StatusIcon """
        pass

    def new_from_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ new_from_pixbuf(pixbuf:GdkPixbuf.Pixbuf) -> Gtk.StatusIcon """
        pass

    def new_from_stock(self, stock_id): # real signature unknown; restored from __doc__
        """ new_from_stock(stock_id:str) -> Gtk.StatusIcon """
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

    def position_menu(self, menu, x, y, user_data): # real signature unknown; restored from __doc__
        """ position_menu(menu:Gtk.Menu, x:int, y:int, user_data:Gtk.StatusIcon) -> x:int, y:int, push_in:bool """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reinit_ui(self): # real signature unknown; restored from __doc__
        """ reinit_ui(self) """
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

    def set_from_file(self, filename): # real signature unknown; restored from __doc__
        """ set_from_file(self, filename:str) """
        pass

    def set_from_gicon(self, icon): # real signature unknown; restored from __doc__
        """ set_from_gicon(self, icon:Gio.Icon) """
        pass

    def set_from_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ set_from_icon_name(self, icon_name:str) """
        pass

    def set_from_pixbuf(self, pixbuf=None): # real signature unknown; restored from __doc__
        """ set_from_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf=None) """
        pass

    def set_from_stock(self, stock_id): # real signature unknown; restored from __doc__
        """ set_from_stock(self, stock_id:str) """
        pass

    def set_has_tooltip(self, has_tooltip): # real signature unknown; restored from __doc__
        """ set_has_tooltip(self, has_tooltip:bool) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_screen(self, screen): # real signature unknown; restored from __doc__
        """ set_screen(self, screen:Gdk.Screen) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_tooltip_markup(self, markup=None): # real signature unknown; restored from __doc__
        """ set_tooltip_markup(self, markup:str=None) """
        pass

    def set_tooltip_text(self, text): # real signature unknown; restored from __doc__
        """ set_tooltip_text(self, text:str) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb1731c0ac0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Status), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType GkbdStatus (94195347881760)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_group_names': gi.FunctionInfo(get_group_names), 'get_image_filename': gi.FunctionInfo(get_image_filename), 'get_xkl_engine': gi.FunctionInfo(get_xkl_engine), 'reinit_ui': gi.FunctionInfo(reinit_ui), 'parent': <property object at 0x7fb1731c49a0>, 'priv': <property object at 0x7fb1731c4a90>})"
    __gdoc__ = 'Object GkbdStatus\n\nSignals from GtkStatusIcon:\n  size-changed (gint) -> gboolean\n  button-press-event (GdkEvent) -> gboolean\n  button-release-event (GdkEvent) -> gboolean\n  scroll-event (GdkEvent) -> gboolean\n  query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean\n  popup-menu (guint, guint)\n  activate ()\n\nProperties from GtkStatusIcon:\n  pixbuf -> GdkPixbuf: Pixbuf\n    A GdkPixbuf to display\n  file -> gchararray: Filename\n    Filename to load and display\n  stock -> gchararray: Stock ID\n    Stock ID for a stock image to display\n  icon-name -> gchararray: Icon Name\n    The name of the icon from the icon theme\n  gicon -> GIcon: GIcon\n    The GIcon being displayed\n  storage-type -> GtkImageType: Storage type\n    The representation being used for image data\n  size -> gint: Size\n    The size of the icon\n  screen -> GdkScreen: Screen\n    The screen where this status icon will be displayed\n  visible -> gboolean: Visible\n    Whether the status icon is visible\n  orientation -> GtkOrientation: Orientation\n    The orientation of the tray\n  embedded -> gboolean: Embedded\n    Whether the status icon is embedded\n  has-tooltip -> gboolean: Has tooltip\n    Whether this tray icon has a tooltip\n  tooltip-text -> gchararray: Tooltip Text\n    The contents of the tooltip for this widget\n  tooltip-markup -> gchararray: Tooltip markup\n    The contents of the tooltip for this tray icon\n  title -> gchararray: Title\n    The title of this tray icon\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GkbdStatus (94195347881760)>'
    __info__ = ObjectInfo(Status)


class StatusClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        StatusClass()
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


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(StatusClass), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'StatusClass' objects>, '__weakref__': <attribute '__weakref__' of 'StatusClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fb1731c4c20>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(StatusClass)


class StatusPrivate(__gi.Struct):
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(StatusPrivate), '__module__': 'gi.repository.Gkbd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'StatusPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'StatusPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(StatusPrivate)


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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7fb1745f01f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7fb1745f0280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7fb1745f0310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7fb1745f03a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fb17522cd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Gkbd-3.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gkbd', loader=<gi.importer.DynamicImporter object at 0x7fb17522cd00>)"

