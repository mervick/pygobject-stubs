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


class Widget(__gi_repository_GObject.InitiallyUnowned):
    """
    :Constructors:
    
    ::
    
        Widget(**properties)
    """
    def adaptor_create_internal(self, internal_object, internal_name, parent_name, anarchist, reason): # real signature unknown; restored from __doc__
        """ adaptor_create_internal(self, internal_object:GObject.Object, internal_name:str, parent_name:str, anarchist:bool, reason:Gladeui.CreateReason) -> Gladeui.Widget """
        pass

    def add_child(self, child, at_mouse): # real signature unknown; restored from __doc__
        """ add_child(self, child:Gladeui.Widget, at_mouse:bool) """
        pass

    def add_prop_ref(self, property): # real signature unknown; restored from __doc__
        """ add_prop_ref(self, property:Gladeui.Property) """
        pass

    def add_signal_handler(self, signal_handler): # real signature unknown; restored from __doc__
        """ add_signal_handler(self, signal_handler:Gladeui.Signal) """
        pass

    def add_verify(self, child, user_feedback): # real signature unknown; restored from __doc__
        """ add_verify(self, child:Gladeui.Widget, user_feedback:bool) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_signal_handler(self, old_signal_handler, new_signal_handler): # real signature unknown; restored from __doc__
        """ change_signal_handler(self, old_signal_handler:Gladeui.Signal, new_signal_handler:Gladeui.Signal) """
        pass

    def child_get_property(self, child, property_name, value): # real signature unknown; restored from __doc__
        """ child_get_property(self, child:Gladeui.Widget, property_name:str, value:GObject.Value) """
        pass

    def child_set_property(self, child, property_name, value): # real signature unknown; restored from __doc__
        """ child_set_property(self, child:Gladeui.Widget, property_name:str, value:GObject.Value) """
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

    def copy_properties(self, template_widget, copy_parentless, exact): # real signature unknown; restored from __doc__
        """ copy_properties(self, template_widget:Gladeui.Widget, copy_parentless:bool, exact:bool) """
        pass

    def copy_signals(self, template_widget): # real signature unknown; restored from __doc__
        """ copy_signals(self, template_widget:Gladeui.Widget) """
        pass

    def create_editor_property(self, property, packing, use_command): # real signature unknown; restored from __doc__
        """ create_editor_property(self, property:str, packing:bool, use_command:bool) -> Gladeui.EditorProperty """
        pass

    def depends(self, other): # real signature unknown; restored from __doc__
        """ depends(self, other:Gladeui.Widget) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_add_child(self, *args, **kwargs): # real signature unknown
        """ add_child(self, child:Gladeui.Widget, at_mouse:bool) """
        pass

    def do_add_signal_handler(self, *args, **kwargs): # real signature unknown
        """ add_signal_handler(self, signal_handler:Gladeui.Signal) """
        pass

    def do_button_press_event(self, *args, **kwargs): # real signature unknown
        """ button_press_event(self, event:Gdk.Event) -> int """
        pass

    def do_button_release_event(self, *args, **kwargs): # real signature unknown
        """ button_release_event(self, event:Gdk.Event) -> int """
        pass

    def do_change_signal_handler(self, *args, **kwargs): # real signature unknown
        """ change_signal_handler(self, new_signal_handler:Gladeui.Signal) """
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event:Gdk.Event) -> bool """
        pass

    def do_motion_notify_event(self, *args, **kwargs): # real signature unknown
        """ motion_notify_event(self, event:Gdk.Event) -> int """
        pass

    def do_remove_child(self, *args, **kwargs): # real signature unknown
        """ remove_child(self, child:Gladeui.Widget) """
        pass

    def do_remove_signal_handler(self, *args, **kwargs): # real signature unknown
        """ remove_signal_handler(self, signal_handler:Gladeui.Signal) """
        pass

    def do_replace_child(self, *args, **kwargs): # real signature unknown
        """ replace_child(self, old_object:GObject.Object, new_object:GObject.Object) """
        pass

    def dup(self, exact): # real signature unknown; restored from __doc__
        """ dup(self, exact:bool) -> Gladeui.Widget """
        pass

    def dup_properties(self, template_props, as_load, copy_parentless, exact): # real signature unknown; restored from __doc__
        """ dup_properties(self, template_props:list, as_load:bool, copy_parentless:bool, exact:bool) -> list """
        return []

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_name(self, project, use_command): # real signature unknown; restored from __doc__
        """ ensure_name(self, project:Gladeui.Project, use_command:bool) """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event:Gdk.Event) -> bool """
        return False

    def find_child(self, name): # real signature unknown; restored from __doc__
        """ find_child(self, name:str) -> Gladeui.Widget or None """
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

    def generate_path_name(self): # real signature unknown; restored from __doc__
        """ generate_path_name(self) -> str """
        return ""

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_action(self, action_path): # real signature unknown; restored from __doc__
        """ get_action(self, action_path:str) -> Gladeui.WidgetAction or None """
        pass

    def get_actions(self): # real signature unknown; restored from __doc__
        """ get_actions(self) -> list """
        return []

    def get_adaptor(self): # real signature unknown; restored from __doc__
        """ get_adaptor(self) -> Gladeui.WidgetAdaptor """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_device_from_event(self, event): # real signature unknown; restored from __doc__
        """ get_device_from_event(event:Gdk.Event) -> Gdk.Device """
        pass

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_from_gobject(self, p_object=None): # real signature unknown; restored from __doc__
        """ get_from_gobject(object=None) -> Gladeui.Widget """
        pass

    def get_internal(self): # real signature unknown; restored from __doc__
        """ get_internal(self) -> str """
        return ""

    def get_is_composite(self): # real signature unknown; restored from __doc__
        """ get_is_composite(self) -> bool """
        return False

    def get_locker(self): # real signature unknown; restored from __doc__
        """ get_locker(self) -> Gladeui.Widget or None """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GObject.Object """
        pass

    def get_packing_properties(self): # real signature unknown; restored from __doc__
        """ get_packing_properties(self) -> list """
        return []

    def get_pack_action(self, action_path): # real signature unknown; restored from __doc__
        """ get_pack_action(self, action_path:str) -> Gladeui.WidgetAction or None """
        pass

    def get_pack_actions(self): # real signature unknown; restored from __doc__
        """ get_pack_actions(self) -> list """
        return []

    def get_pack_property(self, id_property): # real signature unknown; restored from __doc__
        """ get_pack_property(self, id_property:str) -> Gladeui.Property or None """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gladeui.Widget """
        pass

    def get_parentless_reffed_widgets(self): # real signature unknown; restored from __doc__
        """ get_parentless_reffed_widgets(self) -> list """
        return []

    def get_parentless_widget_ref(self): # real signature unknown; restored from __doc__
        """ get_parentless_widget_ref(self) -> Gladeui.Property """
        pass

    def get_project(self): # real signature unknown; restored from __doc__
        """ get_project(self) -> Gladeui.Project """
        pass

    def get_properties(self): # real signature unknown; restored from __doc__
        """ get_properties(self) -> list """
        return []

    def get_property(self, id_property): # real signature unknown; restored from __doc__
        """ get_property(self, id_property:str) -> Gladeui.Property or None """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_signal_list(self): # real signature unknown; restored from __doc__
        """ get_signal_list(self) -> list """
        return []

    def get_signal_model(self): # real signature unknown; restored from __doc__
        """ get_signal_model(self) -> Gtk.TreeModel """
        pass

    def get_toplevel(self): # real signature unknown; restored from __doc__
        """ get_toplevel(self) -> Gladeui.Widget """
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

    def has_decendant(self, type): # real signature unknown; restored from __doc__
        """ has_decendant(self, type:GType) -> bool """
        return False

    def has_name(self): # real signature unknown; restored from __doc__
        """ has_name(self) -> bool """
        return False

    def has_prop_refs(self): # real signature unknown; restored from __doc__
        """ has_prop_refs(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
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

    def in_project(self): # real signature unknown; restored from __doc__
        """ in_project(self) -> bool """
        return False

    def is_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ is_ancestor(self, ancestor:Gladeui.Widget) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_locked_widgets(self): # real signature unknown; restored from __doc__
        """ list_locked_widgets(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_prop_refs(self): # real signature unknown; restored from __doc__
        """ list_prop_refs(self) -> list """
        return []

    def list_signal_handlers(self, signal_name): # real signature unknown; restored from __doc__
        """ list_signal_handlers(self, signal_name:str) -> list """
        return []

    def lock(self, locked): # real signature unknown; restored from __doc__
        """ lock(self, locked:Gladeui.Widget) """
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

    def object_get_property(self, property_name, value): # real signature unknown; restored from __doc__
        """ object_get_property(self, property_name:str, value:GObject.Value) """
        pass

    def object_set_property(self, property_name, value): # real signature unknown; restored from __doc__
        """ object_set_property(self, property_name:str, value:GObject.Value) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def pack_property_default(self, id_property): # real signature unknown; restored from __doc__
        """ pack_property_default(self, id_property:str) -> bool """
        return False

    def pack_property_reset(self, id_property): # real signature unknown; restored from __doc__
        """ pack_property_reset(self, id_property:str) -> bool """
        return False

    def pack_property_set_enabled(self, id_property, enabled): # real signature unknown; restored from __doc__
        """ pack_property_set_enabled(self, id_property:str, enabled:bool) -> bool """
        return False

    def pack_property_set_save_always(self, id_property, setting): # real signature unknown; restored from __doc__
        """ pack_property_set_save_always(self, id_property:str, setting:bool) -> bool """
        return False

    def pack_property_set_sensitive(self, id_property, sensitive, reason): # real signature unknown; restored from __doc__
        """ pack_property_set_sensitive(self, id_property:str, sensitive:bool, reason:str) -> bool """
        return False

    def pack_property_string(self, id_property, value): # real signature unknown; restored from __doc__
        """ pack_property_string(self, id_property:str, value:GObject.Value) -> str """
        return ""

    def placeholder_relation(self, widget): # real signature unknown; restored from __doc__
        """ placeholder_relation(self, widget:Gladeui.Widget) -> bool """
        return False

    def pop_superuser(self): # real signature unknown; restored from __doc__
        """ pop_superuser() """
        pass

    def property_default(self, id_property): # real signature unknown; restored from __doc__
        """ property_default(self, id_property:str) -> bool """
        return False

    def property_original_default(self, id_property): # real signature unknown; restored from __doc__
        """ property_original_default(self, id_property:str) -> bool """
        return False

    def property_reset(self, id_property): # real signature unknown; restored from __doc__
        """ property_reset(self, id_property:str) -> bool """
        return False

    def property_set_enabled(self, id_property, enabled): # real signature unknown; restored from __doc__
        """ property_set_enabled(self, id_property:str, enabled:bool) -> bool """
        return False

    def property_set_save_always(self, id_property, setting): # real signature unknown; restored from __doc__
        """ property_set_save_always(self, id_property:str, setting:bool) -> bool """
        return False

    def property_set_sensitive(self, id_property, sensitive, reason): # real signature unknown; restored from __doc__
        """ property_set_sensitive(self, id_property:str, sensitive:bool, reason:str) -> bool """
        return False

    def property_string(self, id_property, value): # real signature unknown; restored from __doc__
        """ property_string(self, id_property:str, value:GObject.Value) -> str """
        return ""

    def push_superuser(self): # real signature unknown; restored from __doc__
        """ push_superuser() """
        pass

    def read(self, project, parent=None, node, internal=None): # real signature unknown; restored from __doc__
        """ read(project:Gladeui.Project, parent:Gladeui.Widget=None, node:Gladeui.XmlNode, internal:str=None) -> Gladeui.Widget """
        pass

    def read_child(self, node): # real signature unknown; restored from __doc__
        """ read_child(self, node:Gladeui.XmlNode) """
        pass

    def rebuild(self): # real signature unknown; restored from __doc__
        """ rebuild(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_child(self, child): # real signature unknown; restored from __doc__
        """ remove_child(self, child:Gladeui.Widget) """
        pass

    def remove_property(self, id_property): # real signature unknown; restored from __doc__
        """ remove_property(self, id_property:str) """
        pass

    def remove_prop_ref(self, property): # real signature unknown; restored from __doc__
        """ remove_prop_ref(self, property:Gladeui.Property) """
        pass

    def remove_signal_handler(self, signal_handler): # real signature unknown; restored from __doc__
        """ remove_signal_handler(self, signal_handler:Gladeui.Signal) """
        pass

    def replace(self, old_object, new_object): # real signature unknown; restored from __doc__
        """ replace(self, old_object:GObject.Object, new_object:GObject.Object) """
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

    def set_action_sensitive(self, action_path, sensitive): # real signature unknown; restored from __doc__
        """ set_action_sensitive(self, action_path:str, sensitive:bool) -> bool """
        return False

    def set_action_visible(self, action_path, visible): # real signature unknown; restored from __doc__
        """ set_action_visible(self, action_path:str, visible:bool) -> bool """
        return False

    def set_child_type_from_node(self, child, node): # real signature unknown; restored from __doc__
        """ set_child_type_from_node(self, child:GObject.Object, node:Gladeui.XmlNode) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_internal(self, internal): # real signature unknown; restored from __doc__
        """ set_internal(self, internal:str) """
        pass

    def set_in_project(self, in_project): # real signature unknown; restored from __doc__
        """ set_in_project(self, in_project:bool) """
        pass

    def set_is_composite(self, composite): # real signature unknown; restored from __doc__
        """ set_is_composite(self, composite:bool) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_packing_properties(self, container): # real signature unknown; restored from __doc__
        """ set_packing_properties(self, container:Gladeui.Widget) """
        pass

    def set_pack_action_sensitive(self, action_path, sensitive): # real signature unknown; restored from __doc__
        """ set_pack_action_sensitive(self, action_path:str, sensitive:bool) -> bool """
        return False

    def set_pack_action_visible(self, action_path, visible): # real signature unknown; restored from __doc__
        """ set_pack_action_visible(self, action_path:str, visible:bool) -> bool """
        return False

    def set_parent(self, parent=None): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gladeui.Widget=None) """
        pass

    def set_project(self, project): # real signature unknown; restored from __doc__
        """ set_project(self, project:Gladeui.Project) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_support_warning(self, warning): # real signature unknown; restored from __doc__
        """ set_support_warning(self, warning:str) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
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

    def support_changed(self): # real signature unknown; restored from __doc__
        """ support_changed(self) """
        pass

    def support_warning(self): # real signature unknown; restored from __doc__
        """ support_warning(self) -> str """
        return ""

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def verify(self): # real signature unknown; restored from __doc__
        """ verify(self) """
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, context, node): # real signature unknown; restored from __doc__
        """ write(self, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
        pass

    def write_child(self, child, context, node): # real signature unknown; restored from __doc__
        """ write_child(self, child:Gladeui.Widget, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
        pass

    def write_placeholder(self, p_object, context, node): # real signature unknown; restored from __doc__
        """ write_placeholder(self, object:GObject.Object, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
        pass

    def write_signals(self, context, node): # real signature unknown; restored from __doc__
        """ write_signals(self, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
        pass

    def write_special_child_prop(self, p_object, context, node): # real signature unknown; restored from __doc__
        """ write_special_child_prop(self, object:GObject.Object, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1341061370>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Widget), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType GladeWidget (94653531301456)>, '__doc__': None, '__gsignals__': {}, 'get_device_from_event': gi.FunctionInfo(get_device_from_event), 'get_from_gobject': gi.FunctionInfo(get_from_gobject), 'pop_superuser': gi.FunctionInfo(pop_superuser), 'push_superuser': gi.FunctionInfo(push_superuser), 'read': gi.FunctionInfo(read), 'superuser': gi.FunctionInfo(superuser), 'adaptor_create_internal': gi.FunctionInfo(adaptor_create_internal), 'add_child': gi.FunctionInfo(add_child), 'add_prop_ref': gi.FunctionInfo(add_prop_ref), 'add_signal_handler': gi.FunctionInfo(add_signal_handler), 'add_verify': gi.FunctionInfo(add_verify), 'change_signal_handler': gi.FunctionInfo(change_signal_handler), 'child_get_property': gi.FunctionInfo(child_get_property), 'child_set_property': gi.FunctionInfo(child_set_property), 'copy_properties': gi.FunctionInfo(copy_properties), 'copy_signals': gi.FunctionInfo(copy_signals), 'create_editor_property': gi.FunctionInfo(create_editor_property), 'depends': gi.FunctionInfo(depends), 'dup': gi.FunctionInfo(dup), 'dup_properties': gi.FunctionInfo(dup_properties), 'ensure_name': gi.FunctionInfo(ensure_name), 'event': gi.FunctionInfo(event), 'find_child': gi.FunctionInfo(find_child), 'generate_path_name': gi.FunctionInfo(generate_path_name), 'get_action': gi.FunctionInfo(get_action), 'get_actions': gi.FunctionInfo(get_actions), 'get_adaptor': gi.FunctionInfo(get_adaptor), 'get_children': gi.FunctionInfo(get_children), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_internal': gi.FunctionInfo(get_internal), 'get_is_composite': gi.FunctionInfo(get_is_composite), 'get_locker': gi.FunctionInfo(get_locker), 'get_name': gi.FunctionInfo(get_name), 'get_object': gi.FunctionInfo(get_object), 'get_pack_action': gi.FunctionInfo(get_pack_action), 'get_pack_actions': gi.FunctionInfo(get_pack_actions), 'get_pack_property': gi.FunctionInfo(get_pack_property), 'get_packing_properties': gi.FunctionInfo(get_packing_properties), 'get_parent': gi.FunctionInfo(get_parent), 'get_parentless_reffed_widgets': gi.FunctionInfo(get_parentless_reffed_widgets), 'get_parentless_widget_ref': gi.FunctionInfo(get_parentless_widget_ref), 'get_project': gi.FunctionInfo(get_project), 'get_properties': gi.FunctionInfo(get_properties), 'get_property': gi.FunctionInfo(get_property), 'get_signal_list': gi.FunctionInfo(get_signal_list), 'get_signal_model': gi.FunctionInfo(get_signal_model), 'get_toplevel': gi.FunctionInfo(get_toplevel), 'has_decendant': gi.FunctionInfo(has_decendant), 'has_name': gi.FunctionInfo(has_name), 'has_prop_refs': gi.FunctionInfo(has_prop_refs), 'hide': gi.FunctionInfo(hide), 'in_project': gi.FunctionInfo(in_project), 'is_ancestor': gi.FunctionInfo(is_ancestor), 'list_locked_widgets': gi.FunctionInfo(list_locked_widgets), 'list_prop_refs': gi.FunctionInfo(list_prop_refs), 'list_signal_handlers': gi.FunctionInfo(list_signal_handlers), 'lock': gi.FunctionInfo(lock), 'object_get_property': gi.FunctionInfo(object_get_property), 'object_set_property': gi.FunctionInfo(object_set_property), 'pack_property_default': gi.FunctionInfo(pack_property_default), 'pack_property_reset': gi.FunctionInfo(pack_property_reset), 'pack_property_set_enabled': gi.FunctionInfo(pack_property_set_enabled), 'pack_property_set_save_always': gi.FunctionInfo(pack_property_set_save_always), 'pack_property_set_sensitive': gi.FunctionInfo(pack_property_set_sensitive), 'pack_property_string': gi.FunctionInfo(pack_property_string), 'placeholder_relation': gi.FunctionInfo(placeholder_relation), 'property_default': gi.FunctionInfo(property_default), 'property_original_default': gi.FunctionInfo(property_original_default), 'property_reset': gi.FunctionInfo(property_reset), 'property_set_enabled': gi.FunctionInfo(property_set_enabled), 'property_set_save_always': gi.FunctionInfo(property_set_save_always), 'property_set_sensitive': gi.FunctionInfo(property_set_sensitive), 'property_string': gi.FunctionInfo(property_string), 'read_child': gi.FunctionInfo(read_child), 'rebuild': gi.FunctionInfo(rebuild), 'remove_child': gi.FunctionInfo(remove_child), 'remove_prop_ref': gi.FunctionInfo(remove_prop_ref), 'remove_property': gi.FunctionInfo(remove_property), 'remove_signal_handler': gi.FunctionInfo(remove_signal_handler), 'replace': gi.FunctionInfo(replace), 'set_action_sensitive': gi.FunctionInfo(set_action_sensitive), 'set_action_visible': gi.FunctionInfo(set_action_visible), 'set_child_type_from_node': gi.FunctionInfo(set_child_type_from_node), 'set_in_project': gi.FunctionInfo(set_in_project), 'set_internal': gi.FunctionInfo(set_internal), 'set_is_composite': gi.FunctionInfo(set_is_composite), 'set_name': gi.FunctionInfo(set_name), 'set_pack_action_sensitive': gi.FunctionInfo(set_pack_action_sensitive), 'set_pack_action_visible': gi.FunctionInfo(set_pack_action_visible), 'set_packing_properties': gi.FunctionInfo(set_packing_properties), 'set_parent': gi.FunctionInfo(set_parent), 'set_project': gi.FunctionInfo(set_project), 'set_support_warning': gi.FunctionInfo(set_support_warning), 'show': gi.FunctionInfo(show), 'support_changed': gi.FunctionInfo(support_changed), 'support_warning': gi.FunctionInfo(support_warning), 'unlock': gi.FunctionInfo(unlock), 'verify': gi.FunctionInfo(verify), 'write': gi.FunctionInfo(write), 'write_child': gi.FunctionInfo(write_child), 'write_placeholder': gi.FunctionInfo(write_placeholder), 'write_signals': gi.FunctionInfo(write_signals), 'write_special_child_prop': gi.FunctionInfo(write_special_child_prop), 'do_add_child': gi.VFuncInfo(add_child), 'do_add_signal_handler': gi.VFuncInfo(add_signal_handler), 'do_button_press_event': gi.VFuncInfo(button_press_event), 'do_button_release_event': gi.VFuncInfo(button_release_event), 'do_change_signal_handler': gi.VFuncInfo(change_signal_handler), 'do_event': gi.VFuncInfo(event), 'do_motion_notify_event': gi.VFuncInfo(motion_notify_event), 'do_remove_child': gi.VFuncInfo(remove_child), 'do_remove_signal_handler': gi.VFuncInfo(remove_signal_handler), 'do_replace_child': gi.VFuncInfo(replace_child), 'parent_instance': <property object at 0x7f1341772400>, 'priv': <property object at 0x7f13417724f0>})"
    __gdoc__ = 'Object GladeWidget\n\nSignals from GladeWidget:\n  button-press-event (GdkEvent) -> gboolean\n  button-release-event (GdkEvent) -> gboolean\n  motion-notify-event (GdkEvent) -> gboolean\n  add-signal-handler (GladeSignal)\n  remove-signal-handler (GladeSignal)\n  change-signal-handler (GladeSignal)\n  support-changed ()\n\nProperties from GladeWidget:\n  name -> gchararray: Name\n    The name of the widget\n  internal -> gchararray: Internal name\n    The internal name of the widget\n  anarchist -> gboolean: Anarchist\n    Whether this composite child is an ancestral child or an anarchist child\n  adaptor -> GladeWidgetAdaptor: Adaptor\n    The class adaptor for the associated widget\n  object -> GObject: Object\n    The object associated\n  project -> GladeProject: Project\n    The glade project that this widget belongs to\n  properties -> gpointer: Properties\n    A list of GladeProperties\n  parent -> GladeWidget: Parent\n    A pointer to the parenting GladeWidget\n  internal-name -> gchararray: Internal Name\n    A generic name prefix for internal widgets\n  template -> GladeWidget: Template\n    A GladeWidget template to base a new widget on\n  template-exact -> gboolean: Exact Template\n    Whether we are creating an exact duplicate when using a template\n  reason -> gint: Reason\n    A GladeCreateReason for this creation\n  toplevel-width -> gint: Toplevel Width\n    The width of the widget when toplevel in the GladeDesignLayout\n  toplevel-height -> gint: Toplevel Height\n    The height of the widget when toplevel in the GladeDesignLayout\n  support-warning -> gchararray: Support Warning\n    A warning string about version mismatches\n  visible -> gboolean: Visible\n    Whether the widget is visible or not\n  composite -> gboolean: Composite\n    Whether this widget is the template for a composite widget\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GladeWidget (94653531301456)>'
    __info__ = ObjectInfo(Widget)


