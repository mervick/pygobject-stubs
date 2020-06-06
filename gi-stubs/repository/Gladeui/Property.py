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


class Property(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Property(**properties)
        new(def_:Gladeui.PropertyDef, widget:Gladeui.Widget, value:GObject.Value) -> Gladeui.Property
    """
    def add_object(self, p_object): # real signature unknown; restored from __doc__
        """ add_object(self, object:GObject.Object) """
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

    def default(self): # real signature unknown; restored from __doc__
        """ default(self) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_dup(self, *args, **kwargs): # real signature unknown
        """ dup(self, widget:Gladeui.Widget) -> Gladeui.Property """
        pass

    def do_equals_value(self, *args, **kwargs): # real signature unknown
        """ equals_value(self, value:GObject.Value) -> bool """
        pass

    def do_get_value(self, *args, **kwargs): # real signature unknown
        """ get_value(self, value:GObject.Value) """
        pass

    def do_load(self, *args, **kwargs): # real signature unknown
        """ load(self) """
        pass

    def do_set_value(self, *args, **kwargs): # real signature unknown
        """ set_value(self, value:GObject.Value) -> bool """
        pass

    def do_sync(self, *args, **kwargs): # real signature unknown
        """ sync(self) """
        pass

    def do_tooltip_changed(self, *args, **kwargs): # real signature unknown
        """ tooltip_changed(self, tooltip:str, insensitive_tooltip:str, support_warning:str) """
        pass

    def do_value_changed(self, *args, **kwargs): # real signature unknown
        """ value_changed(self, old_value:GObject.Value, new_value:GObject.Value) """
        pass

    def dup(self, widget): # real signature unknown; restored from __doc__
        """ dup(self, widget:Gladeui.Widget) -> Gladeui.Property """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def equals_value(self, value): # real signature unknown; restored from __doc__
        """ equals_value(self, value:GObject.Value) -> bool """
        return False

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

    def get_def(self): # real signature unknown; restored from __doc__
        """ get_def(self) -> Gladeui.PropertyDef """
        pass

    def get_default(self, value): # real signature unknown; restored from __doc__
        """ get_default(self, value:GObject.Value) """
        pass

    def get_enabled(self): # real signature unknown; restored from __doc__
        """ get_enabled(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_save_always(self): # real signature unknown; restored from __doc__
        """ get_save_always(self) -> bool """
        return False

    def get_sensitive(self): # real signature unknown; restored from __doc__
        """ get_sensitive(self) -> bool """
        return False

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Gladeui.PropertyState """
        pass

    def get_support_warning(self): # real signature unknown; restored from __doc__
        """ get_support_warning(self) -> str """
        return ""

    def get_value(self, value): # real signature unknown; restored from __doc__
        """ get_value(self, value:GObject.Value) """
        pass

    def get_widget(self): # real signature unknown; restored from __doc__
        """ get_widget(self) -> Gladeui.Widget """
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

    def i18n_get_comment(self): # real signature unknown; restored from __doc__
        """ i18n_get_comment(self) -> str """
        return ""

    def i18n_get_context(self): # real signature unknown; restored from __doc__
        """ i18n_get_context(self) -> str """
        return ""

    def i18n_get_translatable(self): # real signature unknown; restored from __doc__
        """ i18n_get_translatable(self) -> bool """
        return False

    def i18n_set_comment(self, p_str): # real signature unknown; restored from __doc__
        """ i18n_set_comment(self, str:str) """
        pass

    def i18n_set_context(self, p_str): # real signature unknown; restored from __doc__
        """ i18n_set_context(self, str:str) """
        pass

    def i18n_set_translatable(self, translatable): # real signature unknown; restored from __doc__
        """ i18n_set_translatable(self, translatable:bool) """
        pass

    def inline_value(self): # real signature unknown; restored from __doc__
        """ inline_value(self) -> GObject.Value """
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

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) """
        pass

    def make_string(self): # real signature unknown; restored from __doc__
        """ make_string(self) -> str """
        return ""

    def new(self, def_, widget, value): # real signature unknown; restored from __doc__
        """ new(def_:Gladeui.PropertyDef, widget:Gladeui.Widget, value:GObject.Value) -> Gladeui.Property """
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

    def original_default(self): # real signature unknown; restored from __doc__
        """ original_default(self) -> bool """
        return False

    def original_reset(self): # real signature unknown; restored from __doc__
        """ original_reset(self) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def pop_superuser(self): # real signature unknown; restored from __doc__
        """ pop_superuser() """
        pass

    def push_superuser(self): # real signature unknown; restored from __doc__
        """ push_superuser() """
        pass

    def read(self, project, node): # real signature unknown; restored from __doc__
        """ read(self, project:Gladeui.Project, node:Gladeui.XmlNode) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_object(self, p_object): # real signature unknown; restored from __doc__
        """ remove_object(self, object:GObject.Object) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_enabled(self, enabled:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_save_always(self, setting): # real signature unknown; restored from __doc__
        """ set_save_always(self, setting:bool) """
        pass

    def set_sensitive(self, sensitive, reason): # real signature unknown; restored from __doc__
        """ set_sensitive(self, sensitive:bool, reason:str) """
        pass

    def set_support_warning(self, disable, reason): # real signature unknown; restored from __doc__
        """ set_support_warning(self, disable:bool, reason:str) """
        pass

    def set_value(self, value): # real signature unknown; restored from __doc__
        """ set_value(self, value:GObject.Value) -> bool """
        return False

    def set_widget(self, widget): # real signature unknown; restored from __doc__
        """ set_widget(self, widget:Gladeui.Widget) """
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

    def superuser(self): # real signature unknown; restored from __doc__
        """ superuser() -> bool """
        return False

    def sync(self): # real signature unknown; restored from __doc__
        """ sync(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def warn_usage(self): # real signature unknown; restored from __doc__
        """ warn_usage(self) -> bool """
        return False

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, context, node): # real signature unknown; restored from __doc__
        """ write(self, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f13412334f0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Property), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType GladeProperty (94653531169296)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'pop_superuser': gi.FunctionInfo(pop_superuser), 'push_superuser': gi.FunctionInfo(push_superuser), 'superuser': gi.FunctionInfo(superuser), 'add_object': gi.FunctionInfo(add_object), 'default': gi.FunctionInfo(default), 'dup': gi.FunctionInfo(dup), 'equals_value': gi.FunctionInfo(equals_value), 'get_def': gi.FunctionInfo(get_def), 'get_default': gi.FunctionInfo(get_default), 'get_enabled': gi.FunctionInfo(get_enabled), 'get_save_always': gi.FunctionInfo(get_save_always), 'get_sensitive': gi.FunctionInfo(get_sensitive), 'get_state': gi.FunctionInfo(get_state), 'get_support_warning': gi.FunctionInfo(get_support_warning), 'get_value': gi.FunctionInfo(get_value), 'get_widget': gi.FunctionInfo(get_widget), 'i18n_get_comment': gi.FunctionInfo(i18n_get_comment), 'i18n_get_context': gi.FunctionInfo(i18n_get_context), 'i18n_get_translatable': gi.FunctionInfo(i18n_get_translatable), 'i18n_set_comment': gi.FunctionInfo(i18n_set_comment), 'i18n_set_context': gi.FunctionInfo(i18n_set_context), 'i18n_set_translatable': gi.FunctionInfo(i18n_set_translatable), 'inline_value': gi.FunctionInfo(inline_value), 'load': gi.FunctionInfo(load), 'make_string': gi.FunctionInfo(make_string), 'original_default': gi.FunctionInfo(original_default), 'original_reset': gi.FunctionInfo(original_reset), 'read': gi.FunctionInfo(read), 'remove_object': gi.FunctionInfo(remove_object), 'reset': gi.FunctionInfo(reset), 'set_enabled': gi.FunctionInfo(set_enabled), 'set_save_always': gi.FunctionInfo(set_save_always), 'set_sensitive': gi.FunctionInfo(set_sensitive), 'set_support_warning': gi.FunctionInfo(set_support_warning), 'set_value': gi.FunctionInfo(set_value), 'set_widget': gi.FunctionInfo(set_widget), 'sync': gi.FunctionInfo(sync), 'warn_usage': gi.FunctionInfo(warn_usage), 'write': gi.FunctionInfo(write), 'do_dup': gi.VFuncInfo(dup), 'do_equals_value': gi.VFuncInfo(equals_value), 'do_get_value': gi.VFuncInfo(get_value), 'do_load': gi.VFuncInfo(load), 'do_set_value': gi.VFuncInfo(set_value), 'do_sync': gi.VFuncInfo(sync), 'do_tooltip_changed': gi.VFuncInfo(tooltip_changed), 'do_value_changed': gi.VFuncInfo(value_changed), 'parent_instance': <property object at 0x7f1341a49220>, 'priv': <property object at 0x7f1341a49310>})"
    __gdoc__ = 'Object GladeProperty\n\nSignals from GladeProperty:\n  value-changed (gpointer, gpointer)\n  tooltip-changed (gchararray, gchararray, gchararray)\n\nProperties from GladeProperty:\n  class -> gpointer: Class\n    The GladePropertyDef for this property\n  enabled -> gboolean: Enabled\n    If the property is optional, this is its enabled state\n  sensitive -> gboolean: Sensitive\n    This gives backends control to set property sensitivity\n  i18n-translatable -> gboolean: Translatable\n    Whether this property is translatable\n  i18n-context -> gchararray: Context\n    Context for translation\n  i18n-comment -> gchararray: Comment\n    Comment for translators\n  state -> gint: Visual State\n    Priority information for the property editor to act on\n  precision -> gint: Precision\n    Where applicable, precision to use on editors\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GladeProperty (94653531169296)>'
    __info__ = ObjectInfo(Property)


