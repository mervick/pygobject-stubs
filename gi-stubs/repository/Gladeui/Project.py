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


class Project(__gi_overrides_GObject.Object, __gi_repository_Gtk.TreeDragSource, __gi_overrides_Gtk.TreeModel):
    """
    :Constructors:
    
    ::
    
        Project(**properties)
        new() -> Gladeui.Project
    """
    def add_object(self, p_object): # real signature unknown; restored from __doc__
        """ add_object(self, object:GObject.Object) """
        pass

    def autosave(self): # real signature unknown; restored from __doc__
        """ autosave(self) -> bool """
        return False

    def available_widget_name(self, widget, name): # real signature unknown; restored from __doc__
        """ available_widget_name(self, widget:Gladeui.Widget, name:str) -> bool """
        return False

    def backup(self, path): # real signature unknown; restored from __doc__
        """ backup(self, path:str) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cancel_load(self): # real signature unknown; restored from __doc__
        """ cancel_load(self) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_reordered(self, parent, old_order): # real signature unknown; restored from __doc__
        """ check_reordered(self, parent:Gladeui.Widget, old_order:list) """
        pass

    def command_cut(self): # real signature unknown; restored from __doc__
        """ command_cut(self) """
        pass

    def command_delete(self): # real signature unknown; restored from __doc__
        """ command_delete(self) """
        pass

    def command_paste(self, placeholder): # real signature unknown; restored from __doc__
        """ command_paste(self, placeholder:Gladeui.Placeholder) """
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

    def copy_selection(self): # real signature unknown; restored from __doc__
        """ copy_selection(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def display_dependencies(self): # real signature unknown; restored from __doc__
        """ display_dependencies(self) -> str """
        return ""

    def do_add_object(self, *args, **kwargs): # real signature unknown
        """ add_object(self, object:Gladeui.Widget) """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self, command:Gladeui.Command, forward:bool) """
        pass

    def do_close(self, *args, **kwargs): # real signature unknown
        """ close(self) """
        pass

    def do_next_redo_item(self, *args, **kwargs): # real signature unknown
        """ next_redo_item(self) -> Gladeui.Command """
        pass

    def do_next_undo_item(self, *args, **kwargs): # real signature unknown
        """ next_undo_item(self) -> Gladeui.Command """
        pass

    def do_parse_finished(self, *args, **kwargs): # real signature unknown
        """ parse_finished(self) """
        pass

    def do_push_undo(self, *args, **kwargs): # real signature unknown
        """ push_undo(self, cmd:Gladeui.Command) """
        pass

    def do_redo(self, *args, **kwargs): # real signature unknown
        """ redo(self) """
        pass

    def do_remove_object(self, *args, **kwargs): # real signature unknown
        """ remove_object(self, object:Gladeui.Widget) """
        pass

    def do_selection_changed(self, *args, **kwargs): # real signature unknown
        """ selection_changed(self) """
        pass

    def do_undo(self, *args, **kwargs): # real signature unknown
        """ undo(self) """
        pass

    def do_widget_name_changed(self, *args, **kwargs): # real signature unknown
        """ widget_name_changed(self, widget:Gladeui.Widget) """
        pass

    def drag_data_delete(self, path): # real signature unknown; restored from __doc__
        """ drag_data_delete(self, path:Gtk.TreePath) -> bool """
        return False

    def drag_data_get(self, path, selection_data): # real signature unknown; restored from __doc__
        """ drag_data_get(self, path:Gtk.TreePath, selection_data:Gtk.SelectionData) -> bool """
        return False

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def filter_new(self, root=None): # real signature unknown; restored from __doc__
        """ filter_new(self, root:Gtk.TreePath=None) -> Gtk.TreeModel """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:Gtk.TreeModelForeachFunc, user_data=None) """
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

    def get(self, treeiter, *columns): # reliably restored by inspect
        # no doc
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_add_item(self): # real signature unknown; restored from __doc__
        """ get_add_item(self) -> Gladeui.WidgetAdaptor """
        pass

    def get_column_type(self, index_): # real signature unknown; restored from __doc__
        """ get_column_type(self, index_:int) -> GType """
        pass

    def get_css_provider_path(self): # real signature unknown; restored from __doc__
        """ get_css_provider_path(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_file_mtime(self): # real signature unknown; restored from __doc__
        """ get_file_mtime(self) -> int """
        return 0

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gtk.TreeModelFlags """
        pass

    def get_has_selection(self): # real signature unknown; restored from __doc__
        """ get_has_selection(self) -> bool """
        return False

    def get_iter(self, path): # reliably restored by inspect
        # no doc
        pass

    def get_iter_first(*args, **kwargs): # reliably restored by inspect
        """ get_iter_first(self) -> bool, iter:Gtk.TreeIter """
        pass

    def get_iter_from_string(*args, **kwargs): # reliably restored by inspect
        """ get_iter_from_string(self, path_string:str) -> bool, iter:Gtk.TreeIter """
        pass

    def get_license(self): # real signature unknown; restored from __doc__
        """ get_license(self) -> str """
        return ""

    def get_modified(self): # real signature unknown; restored from __doc__
        """ get_modified(self) -> bool """
        return False

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_columns(self): # real signature unknown; restored from __doc__
        """ get_n_columns(self) -> int """
        return 0

    def get_objects(self): # real signature unknown; restored from __doc__
        """ get_objects(self) -> list """
        return []

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str """
        return ""

    def get_pointer_mode(self): # real signature unknown; restored from __doc__
        """ get_pointer_mode(self) -> Gladeui.PointerMode """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_readonly(self): # real signature unknown; restored from __doc__
        """ get_readonly(self) -> bool """
        return False

    def get_resource_path(self): # real signature unknown; restored from __doc__
        """ get_resource_path(self) -> str """
        return ""

    def get_string_from_iter(self, iter): # real signature unknown; restored from __doc__
        """ get_string_from_iter(self, iter:Gtk.TreeIter) -> str """
        return ""

    def get_target_version(self, catalog, major, minor): # real signature unknown; restored from __doc__
        """ get_target_version(self, catalog:str, major:int, minor:int) """
        pass

    def get_template(self): # real signature unknown; restored from __doc__
        """ get_template(self) -> Gladeui.Widget """
        pass

    def get_translation_domain(self): # real signature unknown; restored from __doc__
        """ get_translation_domain(self) -> str """
        return ""

    def get_value(self, iter, column): # real signature unknown; restored from __doc__
        """ get_value(self, iter:Gtk.TreeIter, column:int) -> value:GObject.Value """
        pass

    def get_widget_by_name(self, name): # real signature unknown; restored from __doc__
        """ get_widget_by_name(self, name:str) -> Gladeui.Widget or None """
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

    def has_object(self, p_object): # real signature unknown; restored from __doc__
        """ has_object(self, object:GObject.Object) -> bool """
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

    def is_loading(self): # real signature unknown; restored from __doc__
        """ is_loading(self) -> bool """
        return False

    def is_selected(self, p_object): # real signature unknown; restored from __doc__
        """ is_selected(self, object:GObject.Object) -> bool """
        return False

    def iter_children(*args, **kwargs): # reliably restored by inspect
        """ iter_children(self, parent:Gtk.TreeIter=None) -> bool, iter:Gtk.TreeIter """
        pass

    def iter_has_child(self, iter): # real signature unknown; restored from __doc__
        """ iter_has_child(self, iter:Gtk.TreeIter) -> bool """
        return False

    def iter_next(self, aiter): # reliably restored by inspect
        # no doc
        pass

    def iter_nth_child(*args, **kwargs): # reliably restored by inspect
        """ iter_nth_child(self, parent:Gtk.TreeIter=None, n:int) -> bool, iter:Gtk.TreeIter """
        pass

    def iter_n_children(self, iter=None): # real signature unknown; restored from __doc__
        """ iter_n_children(self, iter:Gtk.TreeIter=None) -> int """
        return 0

    def iter_parent(*args, **kwargs): # reliably restored by inspect
        """ iter_parent(self, child:Gtk.TreeIter) -> bool, iter:Gtk.TreeIter """
        pass

    def iter_previous(self, aiter): # reliably restored by inspect
        # no doc
        pass

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def load(self, path): # real signature unknown; restored from __doc__
        """ load(path:str) -> Gladeui.Project or None """
        pass

    def load_cancelled(self): # real signature unknown; restored from __doc__
        """ load_cancelled(self) -> bool """
        return False

    def load_from_file(self, path): # real signature unknown; restored from __doc__
        """ load_from_file(self, path:str) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gladeui.Project """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_widget_name(self, widget, base_name): # real signature unknown; restored from __doc__
        """ new_widget_name(self, widget:Gladeui.Widget, base_name:str) -> str """
        return ""

    def next_redo_item(self): # real signature unknown; restored from __doc__
        """ next_redo_item(self) -> Gladeui.Command """
        pass

    def next_undo_item(self): # real signature unknown; restored from __doc__
        """ next_undo_item(self) -> Gladeui.Command """
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

    def preview(self, gwidget): # real signature unknown; restored from __doc__
        """ preview(self, gwidget:Gladeui.Widget) """
        pass

    def properties(self): # real signature unknown; restored from __doc__
        """ properties(self) """
        pass

    def push_progress(self): # real signature unknown; restored from __doc__
        """ push_progress(self) """
        pass

    def push_undo(self, cmd): # real signature unknown; restored from __doc__
        """ push_undo(self, cmd:Gladeui.Command) """
        pass

    def queue_selection_changed(self): # real signature unknown; restored from __doc__
        """ queue_selection_changed(self) """
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
        pass

    def redo_items(self): # real signature unknown; restored from __doc__
        """ redo_items(self) -> Gtk.Widget """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_node(self, iter): # real signature unknown; restored from __doc__
        """ ref_node(self, iter:Gtk.TreeIter) """
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

    def required_libs(self): # real signature unknown; restored from __doc__
        """ required_libs(self) -> list """
        return []

    def reset_path(self): # real signature unknown; restored from __doc__
        """ reset_path(self) """
        pass

    def resource_fullpath(self, resource): # real signature unknown; restored from __doc__
        """ resource_fullpath(self, resource:str) -> str """
        return ""

    def rows_reordered(self, path, iter, new_order): # reliably restored by inspect
        # no doc
        pass

    def row_changed(self, path, iter): # reliably restored by inspect
        # no doc
        pass

    def row_deleted(self, path): # reliably restored by inspect
        # no doc
        pass

    def row_draggable(self, path): # real signature unknown; restored from __doc__
        """ row_draggable(self, path:Gtk.TreePath) -> bool """
        return False

    def row_has_child_toggled(self, path, iter): # reliably restored by inspect
        # no doc
        pass

    def row_inserted(self, path, iter): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def save(self, path): # real signature unknown; restored from __doc__
        """ save(self, path:str) -> bool """
        return False

    def save_verify(self, path, flags): # real signature unknown; restored from __doc__
        """ save_verify(self, path:str, flags:Gladeui.VerifyFlags) -> bool """
        return False

    def selection_add(self, p_object, emit_signal): # real signature unknown; restored from __doc__
        """ selection_add(self, object:GObject.Object, emit_signal:bool) """
        pass

    def selection_changed(self): # real signature unknown; restored from __doc__
        """ selection_changed(self) """
        pass

    def selection_clear(self, emit_signal): # real signature unknown; restored from __doc__
        """ selection_clear(self, emit_signal:bool) """
        pass

    def selection_get(self): # real signature unknown; restored from __doc__
        """ selection_get(self) -> list """
        return []

    def selection_remove(self, p_object, emit_signal): # real signature unknown; restored from __doc__
        """ selection_remove(self, object:GObject.Object, emit_signal:bool) """
        pass

    def selection_set(self, p_object, emit_signal): # real signature unknown; restored from __doc__
        """ selection_set(self, object:GObject.Object, emit_signal:bool) """
        pass

    def set_add_item(self, adaptor): # real signature unknown; restored from __doc__
        """ set_add_item(self, adaptor:Gladeui.WidgetAdaptor) """
        pass

    def set_css_provider_path(self, path): # real signature unknown; restored from __doc__
        """ set_css_provider_path(self, path:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_license(self, license): # real signature unknown; restored from __doc__
        """ set_license(self, license:str) """
        pass

    def set_pointer_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_pointer_mode(self, mode:Gladeui.PointerMode) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resource_path(self, path): # real signature unknown; restored from __doc__
        """ set_resource_path(self, path:str) """
        pass

    def set_row(self, treeiter, row): # reliably restored by inspect
        # no doc
        pass

    def set_target_version(self, catalog, major, minor): # real signature unknown; restored from __doc__
        """ set_target_version(self, catalog:str, major:int, minor:int) """
        pass

    def set_template(self, widget): # real signature unknown; restored from __doc__
        """ set_template(self, widget:Gladeui.Widget) """
        pass

    def set_translation_domain(self, domain): # real signature unknown; restored from __doc__
        """ set_translation_domain(self, domain:str) """
        pass

    def set_widget_name(self, widget, name): # real signature unknown; restored from __doc__
        """ set_widget_name(self, widget:Gladeui.Widget, name:str) """
        pass

    def sort_new_with_model(self): # reliably restored by inspect
        # no doc
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

    def toplevels(self): # real signature unknown; restored from __doc__
        """ toplevels(self) -> list """
        return []

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
        pass

    def undo_items(self): # real signature unknown; restored from __doc__
        """ undo_items(self) -> Gtk.Widget """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unref_node(self, iter): # real signature unknown; restored from __doc__
        """ unref_node(self, iter:Gtk.TreeIter) """
        pass

    def verify(self, saving, flags): # real signature unknown; restored from __doc__
        """ verify(self, saving:bool, flags:Gladeui.VerifyFlags) -> bool """
        return False

    def verify_property(self, property): # real signature unknown; restored from __doc__
        """ verify_property(property:Gladeui.Property) """
        pass

    def verify_signal(self, widget, signal): # real signature unknown; restored from __doc__
        """ verify_signal(widget:Gladeui.Widget, signal:Gladeui.Signal) """
        pass

    def verify_widget_adaptor(self, adaptor, mask): # real signature unknown; restored from __doc__
        """ verify_widget_adaptor(self, adaptor:Gladeui.WidgetAdaptor, mask:Gladeui.SupportMask) -> str """
        return ""

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def widget_changed(self, gwidget): # real signature unknown; restored from __doc__
        """ widget_changed(self, gwidget:Gladeui.Widget) """
        pass

    def widget_visibility_changed(self, widget, visible): # real signature unknown; restored from __doc__
        """ widget_visibility_changed(self, widget:Gladeui.Widget, visible:bool) """
        pass

    def writing_preview(self): # real signature unknown; restored from __doc__
        """ writing_preview(self) -> bool """
        return False

    def _coerce_path(self, path): # reliably restored by inspect
        # no doc
        pass

    def _convert_row(self, row): # reliably restored by inspect
        # no doc
        pass

    def _convert_value(self, column, value): # reliably restored by inspect
        """ Convert value to a GObject.Value of the expected type """
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _getiter(self, key): # reliably restored by inspect
        # no doc
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

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, key): # reliably restored by inspect
        # no doc
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

    def __getitem__(self, key): # reliably restored by inspect
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

    def __setitem__(self, key, value): # reliably restored by inspect
        # no doc
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f13412336d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Project), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType GladeProject (94653531141792)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'load': gi.FunctionInfo(load), 'verify_property': gi.FunctionInfo(verify_property), 'verify_signal': gi.FunctionInfo(verify_signal), 'add_object': gi.FunctionInfo(add_object), 'autosave': gi.FunctionInfo(autosave), 'available_widget_name': gi.FunctionInfo(available_widget_name), 'backup': gi.FunctionInfo(backup), 'cancel_load': gi.FunctionInfo(cancel_load), 'check_reordered': gi.FunctionInfo(check_reordered), 'command_cut': gi.FunctionInfo(command_cut), 'command_delete': gi.FunctionInfo(command_delete), 'command_paste': gi.FunctionInfo(command_paste), 'copy_selection': gi.FunctionInfo(copy_selection), 'display_dependencies': gi.FunctionInfo(display_dependencies), 'get_add_item': gi.FunctionInfo(get_add_item), 'get_css_provider_path': gi.FunctionInfo(get_css_provider_path), 'get_file_mtime': gi.FunctionInfo(get_file_mtime), 'get_has_selection': gi.FunctionInfo(get_has_selection), 'get_license': gi.FunctionInfo(get_license), 'get_modified': gi.FunctionInfo(get_modified), 'get_name': gi.FunctionInfo(get_name), 'get_objects': gi.FunctionInfo(get_objects), 'get_path': gi.FunctionInfo(get_path), 'get_pointer_mode': gi.FunctionInfo(get_pointer_mode), 'get_readonly': gi.FunctionInfo(get_readonly), 'get_resource_path': gi.FunctionInfo(get_resource_path), 'get_target_version': gi.FunctionInfo(get_target_version), 'get_template': gi.FunctionInfo(get_template), 'get_translation_domain': gi.FunctionInfo(get_translation_domain), 'get_widget_by_name': gi.FunctionInfo(get_widget_by_name), 'has_object': gi.FunctionInfo(has_object), 'is_loading': gi.FunctionInfo(is_loading), 'is_selected': gi.FunctionInfo(is_selected), 'load_cancelled': gi.FunctionInfo(load_cancelled), 'load_from_file': gi.FunctionInfo(load_from_file), 'new_widget_name': gi.FunctionInfo(new_widget_name), 'next_redo_item': gi.FunctionInfo(next_redo_item), 'next_undo_item': gi.FunctionInfo(next_undo_item), 'preview': gi.FunctionInfo(preview), 'properties': gi.FunctionInfo(properties), 'push_progress': gi.FunctionInfo(push_progress), 'push_undo': gi.FunctionInfo(push_undo), 'queue_selection_changed': gi.FunctionInfo(queue_selection_changed), 'redo': gi.FunctionInfo(redo), 'redo_items': gi.FunctionInfo(redo_items), 'remove_object': gi.FunctionInfo(remove_object), 'required_libs': gi.FunctionInfo(required_libs), 'reset_path': gi.FunctionInfo(reset_path), 'resource_fullpath': gi.FunctionInfo(resource_fullpath), 'save': gi.FunctionInfo(save), 'save_verify': gi.FunctionInfo(save_verify), 'selection_add': gi.FunctionInfo(selection_add), 'selection_changed': gi.FunctionInfo(selection_changed), 'selection_clear': gi.FunctionInfo(selection_clear), 'selection_get': gi.FunctionInfo(selection_get), 'selection_remove': gi.FunctionInfo(selection_remove), 'selection_set': gi.FunctionInfo(selection_set), 'set_add_item': gi.FunctionInfo(set_add_item), 'set_css_provider_path': gi.FunctionInfo(set_css_provider_path), 'set_license': gi.FunctionInfo(set_license), 'set_pointer_mode': gi.FunctionInfo(set_pointer_mode), 'set_resource_path': gi.FunctionInfo(set_resource_path), 'set_target_version': gi.FunctionInfo(set_target_version), 'set_template': gi.FunctionInfo(set_template), 'set_translation_domain': gi.FunctionInfo(set_translation_domain), 'set_widget_name': gi.FunctionInfo(set_widget_name), 'toplevels': gi.FunctionInfo(toplevels), 'undo': gi.FunctionInfo(undo), 'undo_items': gi.FunctionInfo(undo_items), 'verify': gi.FunctionInfo(verify), 'verify_widget_adaptor': gi.FunctionInfo(verify_widget_adaptor), 'widget_changed': gi.FunctionInfo(widget_changed), 'widget_visibility_changed': gi.FunctionInfo(widget_visibility_changed), 'writing_preview': gi.FunctionInfo(writing_preview), 'do_add_object': gi.VFuncInfo(add_object), 'do_changed': gi.VFuncInfo(changed), 'do_close': gi.VFuncInfo(close), 'do_next_redo_item': gi.VFuncInfo(next_redo_item), 'do_next_undo_item': gi.VFuncInfo(next_undo_item), 'do_parse_finished': gi.VFuncInfo(parse_finished), 'do_push_undo': gi.VFuncInfo(push_undo), 'do_redo': gi.VFuncInfo(redo), 'do_remove_object': gi.VFuncInfo(remove_object), 'do_selection_changed': gi.VFuncInfo(selection_changed), 'do_undo': gi.VFuncInfo(undo), 'do_widget_name_changed': gi.VFuncInfo(widget_name_changed), 'parent_instance': <property object at 0x7f1341a451d0>, 'priv': <property object at 0x7f1341a452c0>})"
    __gdoc__ = "Object GladeProject\n\nSignals from GladeProject:\n  changed (GladeCommand, gboolean)\n  selection-changed ()\n  close ()\n  add-widget (GladeWidget)\n  remove-widget (GladeWidget)\n  widget-name-changed (GladeWidget)\n  parse-began ()\n  parse-finished ()\n  targets-changed ()\n  load-progress (gint, gint)\n  widget-visibility-changed (GladeWidget, gboolean)\n  add-signal-handler (GladeWidget, GladeSignal)\n  remove-signal-handler (GladeWidget, GladeSignal)\n  change-signal-handler (GladeWidget, GladeSignal, GladeSignal)\n  activate-signal-handler (GladeWidget, GladeSignal)\n\nProperties from GladeProject:\n  modified -> gboolean: Modified\n    Whether project has been modified since it was last saved\n  has-selection -> gboolean: Has Selection\n    Whether project has a selection\n  path -> gchararray: Path\n    The filesystem path of the project\n  read-only -> gboolean: Read Only\n    Whether project is read-only\n  add-item -> GladeWidgetAdaptor: Add Item\n    The current item to add to the project\n  pointer-mode -> GladePointerMode: Pointer Mode\n    The currently effective GladePointerMode\n  translation-domain -> gchararray: Translation Domain\n    The project translation domain\n  template -> GladeWidget: Template\n    The project's template widget, if any\n  resource-path -> gchararray: Resource Path\n    Path to load images and resources in Glade's runtime\n  license -> gchararray: License\n    License for this project, it will be added as a document level comment.\n  css-provider-path -> gchararray: CSS Provider Path\n    Path to use as the custom CSS provider for this project.\n\nSignals from GtkTreeModel:\n  row-changed (GtkTreePath, GtkTreeIter)\n  row-inserted (GtkTreePath, GtkTreeIter)\n  row-has-child-toggled (GtkTreePath, GtkTreeIter)\n  row-deleted (GtkTreePath)\n  rows-reordered (GtkTreePath, GtkTreeIter, gpointer)\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GladeProject (94653531141792)>'
    __info__ = ObjectInfo(Project)


