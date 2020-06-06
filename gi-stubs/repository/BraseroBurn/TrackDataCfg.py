# encoding: utf-8
# module gi.repository.BraseroBurn
# from /usr/lib64/girepository-1.0/BraseroBurn-3.1.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


from .TrackData import TrackData

class TrackDataCfg(TrackData, __gi_repository_Gtk.TreeDragDest, __gi_repository_Gtk.TreeDragSource, __gi_overrides_Gtk.TreeModel, __gi_overrides_Gtk.TreeSortable):
    """
    :Constructors:
    
    ::
    
        TrackDataCfg(**properties)
        new() -> BraseroBurn.TrackDataCfg
    """
    def add(self, uri, parent): # real signature unknown; restored from __doc__
        """ add(self, uri:str, parent:Gtk.TreePath) -> bool """
        return False

    def add_empty_directory(self, name, parent): # real signature unknown; restored from __doc__
        """ add_empty_directory(self, name:str, parent:Gtk.TreePath) -> Gtk.TreePath """
        pass

    def add_fs(self, fstype): # real signature unknown; restored from __doc__
        """ add_fs(self, fstype:BraseroBurn.ImageFS) -> BraseroBurn.BurnResult """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self): # real signature unknown; restored from __doc__
        """ changed(self) """
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

    def dont_filter_uri(self, uri): # real signature unknown; restored from __doc__
        """ dont_filter_uri(self, uri:str) """
        pass

    def do_add_fs(self, *args, **kwargs): # real signature unknown
        """ add_fs(self, fstype:BraseroBurn.ImageFS) -> BraseroBurn.BurnResult """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def do_get_file_num(self, *args, **kwargs): # real signature unknown
        """ get_file_num(self) -> int """
        pass

    def do_get_fs(self, *args, **kwargs): # real signature unknown
        """ get_fs(self) -> BraseroBurn.ImageFS """
        pass

    def do_get_grafts(self, *args, **kwargs): # real signature unknown
        """ get_grafts(self) -> list or None """
        pass

    def do_get_size(self, *args, **kwargs): # real signature unknown
        """ get_size(self, blocks:int, block_size:int) -> BraseroBurn.BurnResult """
        pass

    def do_get_status(self, *args, **kwargs): # real signature unknown
        """ get_status(self, status:BraseroBurn.Status) -> BraseroBurn.BurnResult """
        pass

    def do_get_type(self, *args, **kwargs): # real signature unknown
        """ get_type(self, type:BraseroBurn.TrackType) -> BraseroBurn.BurnResult """
        pass

    def do_rm_fs(self, *args, **kwargs): # real signature unknown
        """ rm_fs(self, fstype:BraseroBurn.ImageFS) -> BraseroBurn.BurnResult """
        pass

    def do_set_source(self, *args, **kwargs): # real signature unknown
        """ set_source(self, grafts:list, unreadable:list=None) -> BraseroBurn.BurnResult """
        pass

    def drag_data_delete(self, path): # real signature unknown; restored from __doc__
        """ drag_data_delete(self, path:Gtk.TreePath) -> bool """
        return False

    def drag_data_get(self, path, selection_data): # real signature unknown; restored from __doc__
        """ drag_data_get(self, path:Gtk.TreePath, selection_data:Gtk.SelectionData) -> bool """
        return False

    def drag_data_received(self, dest, selection_data): # real signature unknown; restored from __doc__
        """ drag_data_received(self, dest:Gtk.TreePath, selection_data:Gtk.SelectionData) -> bool """
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

    def get_checksum(self): # real signature unknown; restored from __doc__
        """ get_checksum(self) -> str """
        return ""

    def get_checksum_type(self): # real signature unknown; restored from __doc__
        """ get_checksum_type(self) -> BraseroBurn.ChecksumType """
        pass

    def get_column_type(self, index_): # real signature unknown; restored from __doc__
        """ get_column_type(self, index_:int) -> GType """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_excluded_list(self): # real signature unknown; restored from __doc__
        """ get_excluded_list(self) -> list or None """
        return []

    def get_file_num(self): # real signature unknown; restored from __doc__
        """ get_file_num(self) -> BraseroBurn.BurnResult, file_num:int """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gtk.TreeModelFlags """
        pass

    def get_fs(self): # real signature unknown; restored from __doc__
        """ get_fs(self) -> BraseroBurn.ImageFS """
        pass

    def get_grafts(self): # real signature unknown; restored from __doc__
        """ get_grafts(self) -> list or None """
        return []

    def get_icon_path(self): # real signature unknown; restored from __doc__
        """ get_icon_path(self) -> str """
        return ""

    def get_iter(self, path): # reliably restored by inspect
        # no doc
        pass

    def get_iter_first(*args, **kwargs): # reliably restored by inspect
        """ get_iter_first(self) -> bool, iter:Gtk.TreeIter """
        pass

    def get_iter_from_string(*args, **kwargs): # reliably restored by inspect
        """ get_iter_from_string(self, path_string:str) -> bool, iter:Gtk.TreeIter """
        pass

    def get_n_columns(self): # real signature unknown; restored from __doc__
        """ get_n_columns(self) -> int """
        return 0

    def get_path(self, iter): # real signature unknown; restored from __doc__
        """ get_path(self, iter:Gtk.TreeIter) -> Gtk.TreePath """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_size(self, blocks, bytes): # real signature unknown; restored from __doc__
        """ get_size(self, blocks:int, bytes:int) -> BraseroBurn.BurnResult """
        pass

    def get_sort_column_id(*args, **kwargs): # reliably restored by inspect
        """ get_sort_column_id(self) -> bool, sort_column_id:int, order:Gtk.SortType """
        pass

    def get_status(self, status): # real signature unknown; restored from __doc__
        """ get_status(self, status:BraseroBurn.Status) -> BraseroBurn.BurnResult """
        pass

    def get_string_from_iter(self, iter): # real signature unknown; restored from __doc__
        """ get_string_from_iter(self, iter:Gtk.TreeIter) -> str """
        return ""

    def get_track_type(self, type): # real signature unknown; restored from __doc__
        """ get_track_type(self, type:BraseroBurn.TrackType) -> BraseroBurn.BurnResult """
        pass

    def get_value(self, iter, column): # real signature unknown; restored from __doc__
        """ get_value(self, iter:Gtk.TreeIter, column:int) -> value:GObject.Value """
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

    def has_default_sort_func(self): # real signature unknown; restored from __doc__
        """ has_default_sort_func(self) -> bool """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> BraseroBurn.TrackDataCfg """
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

    def ref_node(self, iter): # real signature unknown; restored from __doc__
        """ ref_node(self, iter:Gtk.TreeIter) """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove(self, treepath): # real signature unknown; restored from __doc__
        """ remove(self, treepath:Gtk.TreePath) -> bool """
        return False

    def rename(self, newname, treepath): # real signature unknown; restored from __doc__
        """ rename(self, newname:str, treepath:Gtk.TreePath) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> bool """
        return False

    def restore(self, treepath): # real signature unknown; restored from __doc__
        """ restore(self, treepath:Gtk.TreePath) """
        pass

    def rm_fs(self, fstype): # real signature unknown; restored from __doc__
        """ rm_fs(self, fstype:BraseroBurn.ImageFS) -> BraseroBurn.BurnResult """
        pass

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

    def row_drop_possible(self, dest_path, selection_data): # real signature unknown; restored from __doc__
        """ row_drop_possible(self, dest_path:Gtk.TreePath, selection_data:Gtk.SelectionData) -> bool """
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

    def set_checksum(self, type, checksum): # real signature unknown; restored from __doc__
        """ set_checksum(self, type:BraseroBurn.ChecksumType, checksum:str) -> BraseroBurn.BurnResult """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data_blocks(self, blocks): # real signature unknown; restored from __doc__
        """ set_data_blocks(self, blocks:int) -> BraseroBurn.BurnResult """
        pass

    def set_default_sort_func(self, sort_func, user_data=None): # reliably restored by inspect
        # no doc
        pass

    def set_file_num(self, number): # real signature unknown; restored from __doc__
        """ set_file_num(self, number:int) -> BraseroBurn.BurnResult """
        pass

    def set_icon(self, icon_path): # real signature unknown; restored from __doc__
        """ set_icon(self, icon_path:str) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_row(self, treeiter, row): # reliably restored by inspect
        # no doc
        pass

    def set_sort_column_id(self, sort_column_id, order): # real signature unknown; restored from __doc__
        """ set_sort_column_id(self, sort_column_id:int, order:Gtk.SortType) """
        pass

    def set_sort_func(self, sort_column_id, sort_func, user_data=None): # reliably restored by inspect
        # no doc
        pass

    def set_source(self, grafts, unreadable=None): # real signature unknown; restored from __doc__
        """ set_source(self, grafts:list, unreadable:list=None) -> BraseroBurn.BurnResult """
        pass

    def sort_column_changed(self): # real signature unknown; restored from __doc__
        """ sort_column_changed(self) """
        pass

    def sort_new_with_model(self): # reliably restored by inspect
        # no doc
        pass

    def span(self, sectors, new_track): # real signature unknown; restored from __doc__
        """ span(self, sectors:int, new_track:BraseroBurn.TrackData) -> BraseroBurn.BurnResult """
        pass

    def span_again(self): # real signature unknown; restored from __doc__
        """ span_again(self) -> BraseroBurn.BurnResult """
        pass

    def span_max_space(self): # real signature unknown; restored from __doc__
        """ span_max_space(self) -> int """
        return 0

    def span_possible(self, sectors): # real signature unknown; restored from __doc__
        """ span_possible(self, sectors:int) -> BraseroBurn.BurnResult """
        pass

    def span_stop(self): # real signature unknown; restored from __doc__
        """ span_stop(self) """
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

    def tag_add(self, tag, value): # real signature unknown; restored from __doc__
        """ tag_add(self, tag:str, value:GObject.Value) -> BraseroBurn.BurnResult """
        pass

    def tag_add_int(self, tag, value): # real signature unknown; restored from __doc__
        """ tag_add_int(self, tag:str, value:int) -> BraseroBurn.BurnResult """
        pass

    def tag_add_string(self, tag, string): # real signature unknown; restored from __doc__
        """ tag_add_string(self, tag:str, string:str) -> BraseroBurn.BurnResult """
        pass

    def tag_copy_missing(self, src): # real signature unknown; restored from __doc__
        """ tag_copy_missing(self, src:BraseroBurn.Track) """
        pass

    def tag_lookup(self, tag, value): # real signature unknown; restored from __doc__
        """ tag_lookup(self, tag:str, value:GObject.Value) -> BraseroBurn.BurnResult """
        pass

    def tag_lookup_int(self, tag): # real signature unknown; restored from __doc__
        """ tag_lookup_int(self, tag:str) -> int """
        return 0

    def tag_lookup_string(self, tag): # real signature unknown; restored from __doc__
        """ tag_lookup_string(self, tag:str) -> str """
        return ""

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unload_current_medium(self): # real signature unknown; restored from __doc__
        """ unload_current_medium(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unref_node(self, iter): # real signature unknown; restored from __doc__
        """ unref_node(self, iter:Gtk.TreeIter) """
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write_to_paths(self, grafts_path, excluded_path, emptydir, videodir=None): # real signature unknown; restored from __doc__
        """ write_to_paths(self, grafts_path:str, excluded_path:str, emptydir:str, videodir:str=None) -> BraseroBurn.BurnResult """
        pass

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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fdd608dea00>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TrackDataCfg), '__module__': 'gi.repository.BraseroBurn', '__gtype__': <GType BraseroTrackDataCfg (94320849347344)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add': gi.FunctionInfo(add), 'add_empty_directory': gi.FunctionInfo(add_empty_directory), 'dont_filter_uri': gi.FunctionInfo(dont_filter_uri), 'get_icon_path': gi.FunctionInfo(get_icon_path), 'remove': gi.FunctionInfo(remove), 'rename': gi.FunctionInfo(rename), 'reset': gi.FunctionInfo(reset), 'restore': gi.FunctionInfo(restore), 'set_icon': gi.FunctionInfo(set_icon), 'span': gi.FunctionInfo(span), 'span_again': gi.FunctionInfo(span_again), 'span_max_space': gi.FunctionInfo(span_max_space), 'span_possible': gi.FunctionInfo(span_possible), 'span_stop': gi.FunctionInfo(span_stop), 'unload_current_medium': gi.FunctionInfo(unload_current_medium), 'parent_instance': <property object at 0x7fdd613614f0>})"
    __gdoc__ = 'Object BraseroTrackDataCfg\n\nSignals from BraseroTrackDataCfg:\n  session-available (GObject, gboolean)\n  session-loaded (GObject, gboolean)\n  image-uri (gchararray) -> gint\n  unreadable-uri (gpointer, gchararray)\n  recursive-sym (gchararray)\n  unknown-uri (gchararray)\n  name-collision (gchararray) -> gboolean\n  joliet-rename ()\n  deep-directory (gchararray) -> gboolean\n  source-loading (gdouble)\n  source-loaded (gpointer)\n  icon-changed ()\n\nSignals from GtkTreeModel:\n  row-changed (GtkTreePath, GtkTreeIter)\n  row-inserted (GtkTreePath, GtkTreeIter)\n  row-has-child-toggled (GtkTreePath, GtkTreeIter)\n  row-deleted (GtkTreePath)\n  rows-reordered (GtkTreePath, GtkTreeIter, gpointer)\n\nSignals from GtkTreeSortable:\n  sort-column-changed ()\n\nSignals from BraseroTrack:\n  changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType BraseroTrackDataCfg (94320849347344)>'
    __info__ = ObjectInfo(TrackDataCfg)


