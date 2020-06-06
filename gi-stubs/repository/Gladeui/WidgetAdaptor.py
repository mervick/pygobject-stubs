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


class WidgetAdaptor(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        WidgetAdaptor(**properties)
    """
    def actions_new(self): # real signature unknown; restored from __doc__
        """ actions_new(self) -> list """
        return []

    def action_activate(self, p_object, action_path): # real signature unknown; restored from __doc__
        """ action_activate(self, object:GObject.Object, action_path:str) """
        pass

    def action_add(self, action_path, label, stock, important): # real signature unknown; restored from __doc__
        """ action_add(self, action_path:str, label:str, stock:str, important:bool) -> bool """
        return False

    def action_remove(self, action_path): # real signature unknown; restored from __doc__
        """ action_remove(self, action_path:str) -> bool """
        return False

    def action_submenu(self, p_object, action_path): # real signature unknown; restored from __doc__
        """ action_submenu(self, object:GObject.Object, action_path:str) -> Gtk.Widget or None """
        pass

    def add(self, container, child): # real signature unknown; restored from __doc__
        """ add(self, container:GObject.Object, child:GObject.Object) """
        pass

    def add_verify(self, container, child, user_feedback): # real signature unknown; restored from __doc__
        """ add_verify(self, container:GObject.Object, child:GObject.Object, user_feedback:bool) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def child_action_activate(self, container, p_object, action_path): # real signature unknown; restored from __doc__
        """ child_action_activate(self, container:GObject.Object, object:GObject.Object, action_path:str) """
        pass

    def child_get_property(self, container, child, property_name, value): # real signature unknown; restored from __doc__
        """ child_get_property(self, container:GObject.Object, child:GObject.Object, property_name:str, value:GObject.Value) """
        pass

    def child_set_property(self, container, child, property_name, value): # real signature unknown; restored from __doc__
        """ child_set_property(self, container:GObject.Object, child:GObject.Object, property_name:str, value:GObject.Value) """
        pass

    def child_verify_property(self, container, child, property_name, value): # real signature unknown; restored from __doc__
        """ child_verify_property(self, container:GObject.Object, child:GObject.Object, property_name:str, value:GObject.Value) -> bool """
        return False

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

    def construct_object(self, n_parameters, parameters): # real signature unknown; restored from __doc__
        """ construct_object(self, n_parameters:int, parameters:GObject.Parameter) -> GObject.Object """
        pass

    def create_editable(self, type): # real signature unknown; restored from __doc__
        """ create_editable(self, type:Gladeui.EditorPageType) -> Gladeui.Editable """
        pass

    def create_eprop(self, def_, use_command): # real signature unknown; restored from __doc__
        """ create_eprop(self, def_:Gladeui.PropertyDef, use_command:bool) -> Gladeui.EditorProperty """
        pass

    def create_eprop_by_name(self, property_id, packing, use_command): # real signature unknown; restored from __doc__
        """ create_eprop_by_name(self, property_id:str, packing:bool, use_command:bool) -> Gladeui.EditorProperty """
        pass

    def depends(self, widget, another): # real signature unknown; restored from __doc__
        """ depends(self, widget:Gladeui.Widget, another:Gladeui.Widget) -> bool """
        return False

    def destroy_object(self, p_object): # real signature unknown; restored from __doc__
        """ destroy_object(self, object:GObject.Object) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_action_activate(self, *args, **kwargs): # real signature unknown
        """ action_activate(self, object:GObject.Object, action_path:str) """
        pass

    def do_action_submenu(self, *args, **kwargs): # real signature unknown
        """ action_submenu(self, object:GObject.Object, action_path:str) -> Gtk.Widget or None """
        pass

    def do_add(self, *args, **kwargs): # real signature unknown
        """ add(self, container:GObject.Object, child:GObject.Object) """
        pass

    def do_add_verify(self, *args, **kwargs): # real signature unknown
        """ add_verify(self, container:GObject.Object, child:GObject.Object, user_feedback:bool) -> bool """
        pass

    def do_child_action_activate(self, *args, **kwargs): # real signature unknown
        """ child_action_activate(self, container:GObject.Object, object:GObject.Object, action_path:str) """
        pass

    def do_child_get_property(self, *args, **kwargs): # real signature unknown
        """ child_get_property(self, container:GObject.Object, child:GObject.Object, property_name:str, value:GObject.Value) """
        pass

    def do_child_set_property(self, *args, **kwargs): # real signature unknown
        """ child_set_property(self, container:GObject.Object, child:GObject.Object, property_name:str, value:GObject.Value) """
        pass

    def do_child_verify_property(self, *args, **kwargs): # real signature unknown
        """ child_verify_property(self, container:GObject.Object, child:GObject.Object, property_name:str, value:GObject.Value) -> bool """
        pass

    def do_construct_object(self, *args, **kwargs): # real signature unknown
        """ construct_object(self, n_parameters:int, parameters:GObject.Parameter) -> GObject.Object """
        pass

    def do_create_editable(self, *args, **kwargs): # real signature unknown
        """ create_editable(self, type:Gladeui.EditorPageType) -> Gladeui.Editable """
        pass

    def do_create_eprop(self, *args, **kwargs): # real signature unknown
        """ create_eprop(self, def_:Gladeui.PropertyDef, use_command:bool) -> Gladeui.EditorProperty """
        pass

    def do_deep_post_create(self, *args, **kwargs): # real signature unknown
        """ deep_post_create(self, object:GObject.Object, reason:Gladeui.CreateReason) """
        pass

    def do_depends(self, *args, **kwargs): # real signature unknown
        """ depends(self, widget:Gladeui.Widget, another:Gladeui.Widget) -> bool """
        pass

    def do_destroy_object(self, *args, **kwargs): # real signature unknown
        """ destroy_object(self, object:GObject.Object) """
        pass

    def do_get_children(self, *args, **kwargs): # real signature unknown
        """ get_children(self, container:GObject.Object) -> list """
        pass

    def do_get_internal_child(self, *args, **kwargs): # real signature unknown
        """ get_internal_child(self, object:GObject.Object, internal_name:str) -> GObject.Object or None """
        pass

    def do_get_property(self, *args, **kwargs): # real signature unknown
        """ get_property(self, object:GObject.Object, property_name:str, value:GObject.Value) """
        pass

    def do_post_create(self, *args, **kwargs): # real signature unknown
        """ post_create(self, object:GObject.Object, reason:Gladeui.CreateReason) """
        pass

    def do_read_child(self, *args, **kwargs): # real signature unknown
        """ read_child(self, widget:Gladeui.Widget, node:Gladeui.XmlNode) """
        pass

    def do_read_widget(self, *args, **kwargs): # real signature unknown
        """ read_widget(self, widget:Gladeui.Widget, node:Gladeui.XmlNode) """
        pass

    def do_remove(self, *args, **kwargs): # real signature unknown
        """ remove(self, container:GObject.Object, child:GObject.Object) """
        pass

    def do_replace_child(self, *args, **kwargs): # real signature unknown
        """ replace_child(self, container:GObject.Object, old_obj:GObject.Object, new_obj:GObject.Object) """
        pass

    def do_set_property(self, *args, **kwargs): # real signature unknown
        """ set_property(self, object:GObject.Object, property_name:str, value:GObject.Value) """
        pass

    def do_string_from_value(self, *args, **kwargs): # real signature unknown
        """ string_from_value(self, def_:Gladeui.PropertyDef, value:GObject.Value) -> str """
        pass

    def do_verify_property(self, *args, **kwargs): # real signature unknown
        """ verify_property(self, object:GObject.Object, property_name:str, value:GObject.Value) -> bool """
        pass

    def do_write_child(self, *args, **kwargs): # real signature unknown
        """ write_child(self, widget:Gladeui.Widget, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
        pass

    def do_write_widget(self, *args, **kwargs): # real signature unknown
        """ write_widget(self, widget:Gladeui.Widget, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
        pass

    def do_write_widget_after(self, *args, **kwargs): # real signature unknown
        """ write_widget_after(self, widget:Gladeui.Widget, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
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

    def from_catalog(self, catalog, class_node, module): # real signature unknown; restored from __doc__
        """ from_catalog(catalog:Gladeui.Catalog, class_node:Gladeui.XmlNode, module:GModule.Module) -> Gladeui.WidgetAdaptor """
        pass

    def from_pspec(self, pspec): # real signature unknown; restored from __doc__
        """ from_pspec(self, pspec:GObject.ParamSpec) -> Gladeui.WidgetAdaptor """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_book(self): # real signature unknown; restored from __doc__
        """ get_book(self) -> str """
        return ""

    def get_by_name(self, name): # real signature unknown; restored from __doc__
        """ get_by_name(name:str) -> Gladeui.WidgetAdaptor or None """
        pass

    def get_by_type(self, type): # real signature unknown; restored from __doc__
        """ get_by_type(type:GType) -> Gladeui.WidgetAdaptor or None """
        pass

    def get_catalog(self): # real signature unknown; restored from __doc__
        """ get_catalog(self) -> str """
        return ""

    def get_children(self, container): # real signature unknown; restored from __doc__
        """ get_children(self, container:GObject.Object) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_generic_name(self): # real signature unknown; restored from __doc__
        """ get_generic_name(self) -> str """
        return ""

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str """
        return ""

    def get_internal_child(self, p_object, internal_name): # real signature unknown; restored from __doc__
        """ get_internal_child(self, object:GObject.Object, internal_name:str) -> GObject.Object or None """
        pass

    def get_missing_icon(self): # real signature unknown; restored from __doc__
        """ get_missing_icon(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_object_type(self): # real signature unknown; restored from __doc__
        """ get_object_type(self) -> GType """
        pass

    def get_packing_default(self, container_adaptor, id): # real signature unknown; restored from __doc__
        """ get_packing_default(self, container_adaptor:Gladeui.WidgetAdaptor, id:str) -> str """
        return ""

    def get_packing_props(self): # real signature unknown; restored from __doc__
        """ get_packing_props(self) -> list """
        return []

    def get_pack_property_def(self, name): # real signature unknown; restored from __doc__
        """ get_pack_property_def(self, name:str) -> Gladeui.PropertyDef or None """
        pass

    def get_parent_adaptor(self): # real signature unknown; restored from __doc__
        """ get_parent_adaptor(self) -> Gladeui.WidgetAdaptor """
        pass

    def get_properties(self): # real signature unknown; restored from __doc__
        """ get_properties(self) -> list """
        return []

    def get_property(self, p_object, property_name, value): # real signature unknown; restored from __doc__
        """ get_property(self, object:GObject.Object, property_name:str, value:GObject.Value) """
        pass

    def get_property_def(self, name): # real signature unknown; restored from __doc__
        """ get_property_def(self, name:str) -> Gladeui.PropertyDef or None """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_signals(self): # real signature unknown; restored from __doc__
        """ get_signals(self) -> list """
        return []

    def get_signal_def(self, name): # real signature unknown; restored from __doc__
        """ get_signal_def(self, name:str) -> Gladeui.SignalDef or None """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_type_func(self): # real signature unknown; restored from __doc__
        """ get_type_func(self) -> str or None """
        return ""

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

    def has_child(self, container, child): # real signature unknown; restored from __doc__
        """ has_child(self, container:GObject.Object, child:GObject.Object) -> bool """
        return False

    def has_internal_children(self): # real signature unknown; restored from __doc__
        """ has_internal_children(self) -> bool """
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

    def is_container(self): # real signature unknown; restored from __doc__
        """ is_container(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_adaptors(self): # real signature unknown; restored from __doc__
        """ list_adaptors() -> list """
        return []

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

    def pack_actions_new(self): # real signature unknown; restored from __doc__
        """ pack_actions_new(self) -> list """
        return []

    def pack_action_add(self, action_path, label, stock, important): # real signature unknown; restored from __doc__
        """ pack_action_add(self, action_path:str, label:str, stock:str, important:bool) -> bool """
        return False

    def pack_action_remove(self, action_path): # real signature unknown; restored from __doc__
        """ pack_action_remove(self, action_path:str) -> bool """
        return False

    def post_create(self, p_object, reason): # real signature unknown; restored from __doc__
        """ post_create(self, object:GObject.Object, reason:Gladeui.CreateReason) """
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> bool """
        return False

    def read_child(self, widget, node): # real signature unknown; restored from __doc__
        """ read_child(self, widget:Gladeui.Widget, node:Gladeui.XmlNode) """
        pass

    def read_widget(self, widget, node): # real signature unknown; restored from __doc__
        """ read_widget(self, widget:Gladeui.Widget, node:Gladeui.XmlNode) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register(self): # real signature unknown; restored from __doc__
        """ register(self) """
        pass

    def remove(self, container, child): # real signature unknown; restored from __doc__
        """ remove(self, container:GObject.Object, child:GObject.Object) """
        pass

    def replace_child(self, container, old_obj, new_obj): # real signature unknown; restored from __doc__
        """ replace_child(self, container:GObject.Object, old_obj:GObject.Object, new_obj:GObject.Object) """
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

    def set_property(self, p_object, property_name, value): # real signature unknown; restored from __doc__
        """ set_property(self, object:GObject.Object, property_name:str, value:GObject.Value) """
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

    def string_from_value(self, def_, value): # real signature unknown; restored from __doc__
        """ string_from_value(self, def_:Gladeui.PropertyDef, value:GObject.Value) -> str """
        return ""

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def verify_property(self, p_object, property_name, value): # real signature unknown; restored from __doc__
        """ verify_property(self, object:GObject.Object, property_name:str, value:GObject.Value) -> bool """
        return False

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write_child(self, widget, context, node): # real signature unknown; restored from __doc__
        """ write_child(self, widget:Gladeui.Widget, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
        pass

    def write_widget(self, widget, context, node): # real signature unknown; restored from __doc__
        """ write_widget(self, widget:Gladeui.Widget, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
        pass

    def write_widget_after(self, widget, context, node): # real signature unknown; restored from __doc__
        """ write_widget_after(self, widget:Gladeui.Widget, context:Gladeui.XmlContext, node:Gladeui.XmlNode) """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f13410dbca0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(WidgetAdaptor), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType GladeWidgetAdaptor (94653531316768)>, '__doc__': None, '__gsignals__': {}, 'from_catalog': gi.FunctionInfo(from_catalog), 'get_by_name': gi.FunctionInfo(get_by_name), 'get_by_type': gi.FunctionInfo(get_by_type), 'list_adaptors': gi.FunctionInfo(list_adaptors), 'action_activate': gi.FunctionInfo(action_activate), 'action_add': gi.FunctionInfo(action_add), 'action_remove': gi.FunctionInfo(action_remove), 'action_submenu': gi.FunctionInfo(action_submenu), 'actions_new': gi.FunctionInfo(actions_new), 'add': gi.FunctionInfo(add), 'add_verify': gi.FunctionInfo(add_verify), 'child_action_activate': gi.FunctionInfo(child_action_activate), 'child_get_property': gi.FunctionInfo(child_get_property), 'child_set_property': gi.FunctionInfo(child_set_property), 'child_verify_property': gi.FunctionInfo(child_verify_property), 'construct_object': gi.FunctionInfo(construct_object), 'create_editable': gi.FunctionInfo(create_editable), 'create_eprop': gi.FunctionInfo(create_eprop), 'create_eprop_by_name': gi.FunctionInfo(create_eprop_by_name), 'depends': gi.FunctionInfo(depends), 'destroy_object': gi.FunctionInfo(destroy_object), 'from_pspec': gi.FunctionInfo(from_pspec), 'get_book': gi.FunctionInfo(get_book), 'get_catalog': gi.FunctionInfo(get_catalog), 'get_children': gi.FunctionInfo(get_children), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_generic_name': gi.FunctionInfo(get_generic_name), 'get_icon_name': gi.FunctionInfo(get_icon_name), 'get_internal_child': gi.FunctionInfo(get_internal_child), 'get_missing_icon': gi.FunctionInfo(get_missing_icon), 'get_name': gi.FunctionInfo(get_name), 'get_object_type': gi.FunctionInfo(get_object_type), 'get_pack_property_def': gi.FunctionInfo(get_pack_property_def), 'get_packing_default': gi.FunctionInfo(get_packing_default), 'get_packing_props': gi.FunctionInfo(get_packing_props), 'get_parent_adaptor': gi.FunctionInfo(get_parent_adaptor), 'get_properties': gi.FunctionInfo(get_properties), 'get_property': gi.FunctionInfo(get_property), 'get_property_def': gi.FunctionInfo(get_property_def), 'get_signal_def': gi.FunctionInfo(get_signal_def), 'get_signals': gi.FunctionInfo(get_signals), 'get_title': gi.FunctionInfo(get_title), 'get_type_func': gi.FunctionInfo(get_type_func), 'has_child': gi.FunctionInfo(has_child), 'has_internal_children': gi.FunctionInfo(has_internal_children), 'is_container': gi.FunctionInfo(is_container), 'pack_action_add': gi.FunctionInfo(pack_action_add), 'pack_action_remove': gi.FunctionInfo(pack_action_remove), 'pack_actions_new': gi.FunctionInfo(pack_actions_new), 'post_create': gi.FunctionInfo(post_create), 'query': gi.FunctionInfo(query), 'read_child': gi.FunctionInfo(read_child), 'read_widget': gi.FunctionInfo(read_widget), 'register': gi.FunctionInfo(register), 'remove': gi.FunctionInfo(remove), 'replace_child': gi.FunctionInfo(replace_child), 'set_property': gi.FunctionInfo(set_property), 'string_from_value': gi.FunctionInfo(string_from_value), 'verify_property': gi.FunctionInfo(verify_property), 'write_child': gi.FunctionInfo(write_child), 'write_widget': gi.FunctionInfo(write_widget), 'write_widget_after': gi.FunctionInfo(write_widget_after), 'do_action_activate': gi.VFuncInfo(action_activate), 'do_action_submenu': gi.VFuncInfo(action_submenu), 'do_add': gi.VFuncInfo(add), 'do_add_verify': gi.VFuncInfo(add_verify), 'do_child_action_activate': gi.VFuncInfo(child_action_activate), 'do_child_get_property': gi.VFuncInfo(child_get_property), 'do_child_set_property': gi.VFuncInfo(child_set_property), 'do_child_verify_property': gi.VFuncInfo(child_verify_property), 'do_construct_object': gi.VFuncInfo(construct_object), 'do_create_editable': gi.VFuncInfo(create_editable), 'do_create_eprop': gi.VFuncInfo(create_eprop), 'do_deep_post_create': gi.VFuncInfo(deep_post_create), 'do_depends': gi.VFuncInfo(depends), 'do_destroy_object': gi.VFuncInfo(destroy_object), 'do_get_children': gi.VFuncInfo(get_children), 'do_get_internal_child': gi.VFuncInfo(get_internal_child), 'do_get_property': gi.VFuncInfo(get_property), 'do_post_create': gi.VFuncInfo(post_create), 'do_read_child': gi.VFuncInfo(read_child), 'do_read_widget': gi.VFuncInfo(read_widget), 'do_remove': gi.VFuncInfo(remove), 'do_replace_child': gi.VFuncInfo(replace_child), 'do_set_property': gi.VFuncInfo(set_property), 'do_string_from_value': gi.VFuncInfo(string_from_value), 'do_verify_property': gi.VFuncInfo(verify_property), 'do_write_child': gi.VFuncInfo(write_child), 'do_write_widget': gi.VFuncInfo(write_widget), 'do_write_widget_after': gi.VFuncInfo(write_widget_after), 'parent_instance': <property object at 0x7f1341773ef0>})"
    __gdoc__ = 'Object GladeWidgetAdaptor\n\nProperties from GladeWidgetAdaptor:\n  name -> gchararray: Name\n    Name of the class\n  type -> GType: Type\n    GType of the class\n  title -> gchararray: Title\n    Translated title for the class used in the glade UI\n  generic-name -> gchararray: Generic Name\n    Used to generate names of new widgets\n  icon-name -> gchararray: Icon Name\n    The icon name\n  catalog -> gchararray: Catalog\n    The name of the widget catalog this class was declared by\n  book -> gchararray: Book\n    DevHelp search namespace for this widget class\n  special-child-type -> gchararray: Special Child Type\n    Holds the name of the packing property to depict special children for this container class\n  cursor -> gpointer: Cursor\n    A cursor for inserting widgets in the UI\n  query -> gboolean: Query\n    Whether the adaptor should query the use or not\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GladeWidgetAdaptor (94653531316768)>'
    __info__ = ObjectInfo(WidgetAdaptor)


