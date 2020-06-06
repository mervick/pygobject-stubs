# encoding: utf-8
# module gi.repository.Dazzle
# from /usr/lib64/girepository-1.0/Dazzle-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class TreeBuilder(__gi_repository_GObject.InitiallyUnowned):
    """
    :Constructors:
    
    ::
    
        TreeBuilder(**properties)
        new() -> Dazzle.TreeBuilder
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

    def do_added(self, *args, **kwargs): # real signature unknown
        """ added(self, tree:Gtk.Widget) """
        pass

    def do_build_children(self, *args, **kwargs): # real signature unknown
        """ build_children(self, parent:Dazzle.TreeNode) """
        pass

    def do_build_node(self, *args, **kwargs): # real signature unknown
        """ build_node(self, node:Dazzle.TreeNode) """
        pass

    def do_cell_data_func(self, *args, **kwargs): # real signature unknown
        """ cell_data_func(self, node:Dazzle.TreeNode, cell:Gtk.CellRenderer) """
        pass

    def do_drag_data_get(self, *args, **kwargs): # real signature unknown
        """ drag_data_get(self, node:Dazzle.TreeNode, data:Gtk.SelectionData) -> bool """
        pass

    def do_drag_data_received(self, *args, **kwargs): # real signature unknown
        """ drag_data_received(self, drop_node:Dazzle.TreeNode, position:Dazzle.TreeDropPosition, action:Gdk.DragAction, data:Gtk.SelectionData) -> bool """
        pass

    def do_drag_node_delete(self, *args, **kwargs): # real signature unknown
        """ drag_node_delete(self, node:Dazzle.TreeNode) -> bool """
        pass

    def do_drag_node_received(self, *args, **kwargs): # real signature unknown
        """ drag_node_received(self, drag_node:Dazzle.TreeNode, drop_node:Dazzle.TreeNode, position:Dazzle.TreeDropPosition, action:Gdk.DragAction, data:Gtk.SelectionData) -> bool """
        pass

    def do_node_activated(self, *args, **kwargs): # real signature unknown
        """ node_activated(self, node:Dazzle.TreeNode) -> bool """
        pass

    def do_node_collapsed(self, *args, **kwargs): # real signature unknown
        """ node_collapsed(self, node:Dazzle.TreeNode) """
        pass

    def do_node_draggable(self, *args, **kwargs): # real signature unknown
        """ node_draggable(self, node:Dazzle.TreeNode) -> bool """
        pass

    def do_node_droppable(self, *args, **kwargs): # real signature unknown
        """ node_droppable(self, node:Dazzle.TreeNode, data:Gtk.SelectionData) -> bool """
        pass

    def do_node_expanded(self, *args, **kwargs): # real signature unknown
        """ node_expanded(self, node:Dazzle.TreeNode) """
        pass

    def do_node_popup(self, *args, **kwargs): # real signature unknown
        """ node_popup(self, node:Dazzle.TreeNode, menu:Gio.Menu) """
        pass

    def do_node_selected(self, *args, **kwargs): # real signature unknown
        """ node_selected(self, node:Dazzle.TreeNode) """
        pass

    def do_node_unselected(self, *args, **kwargs): # real signature unknown
        """ node_unselected(self, node:Dazzle.TreeNode) """
        pass

    def do_removed(self, *args, **kwargs): # real signature unknown
        """ removed(self, tree:Gtk.Widget) """
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

    def get_tree(self): # real signature unknown; restored from __doc__
        """ get_tree(self) -> Dazzle.Tree or None """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Dazzle.TreeBuilder """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f3b272ee550>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TreeBuilder), '__module__': 'gi.repository.Dazzle', '__gtype__': <GType DzlTreeBuilder (93962411863296)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_tree': gi.FunctionInfo(get_tree), 'do_added': gi.VFuncInfo(added), 'do_build_children': gi.VFuncInfo(build_children), 'do_build_node': gi.VFuncInfo(build_node), 'do_cell_data_func': gi.VFuncInfo(cell_data_func), 'do_drag_data_get': gi.VFuncInfo(drag_data_get), 'do_drag_data_received': gi.VFuncInfo(drag_data_received), 'do_drag_node_delete': gi.VFuncInfo(drag_node_delete), 'do_drag_node_received': gi.VFuncInfo(drag_node_received), 'do_node_activated': gi.VFuncInfo(node_activated), 'do_node_collapsed': gi.VFuncInfo(node_collapsed), 'do_node_draggable': gi.VFuncInfo(node_draggable), 'do_node_droppable': gi.VFuncInfo(node_droppable), 'do_node_expanded': gi.VFuncInfo(node_expanded), 'do_node_popup': gi.VFuncInfo(node_popup), 'do_node_selected': gi.VFuncInfo(node_selected), 'do_node_unselected': gi.VFuncInfo(node_unselected), 'do_removed': gi.VFuncInfo(removed), 'parent_instance': <property object at 0x7f3b25ef70e0>})"
    __gdoc__ = 'Object DzlTreeBuilder\n\nSignals from DzlTreeBuilder:\n  drag-data-get (DzlTreeNode, GtkSelectionData) -> gboolean\n  drag-data-received (DzlTreeNode, DzlTreeDropPosition, GdkDragAction, GtkSelectionData) -> gboolean\n  added (DzlTree)\n  build-node (DzlTreeNode)\n  build-children (DzlTreeNode)\n  drag-node-received (DzlTreeNode, DzlTreeNode, DzlTreeDropPosition, GdkDragAction, GtkSelectionData) -> gboolean\n  drag-node-delete (DzlTreeNode) -> gboolean\n  node-activated (DzlTreeNode) -> gboolean\n  node-draggable (DzlTreeNode) -> gboolean\n  node-droppable (DzlTreeNode, GtkSelectionData) -> gboolean\n  node-collapsed (DzlTreeNode)\n  node-expanded (DzlTreeNode)\n  node-popup (DzlTreeNode, GMenu)\n  node-selected (DzlTreeNode)\n  node-unselected (DzlTreeNode)\n  removed (DzlTree)\n\nProperties from DzlTreeBuilder:\n  tree -> DzlTree: Tree\n    The DzlTree the builder belongs to.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType DzlTreeBuilder (93962411863296)>'
    __info__ = ObjectInfo(TreeBuilder)


