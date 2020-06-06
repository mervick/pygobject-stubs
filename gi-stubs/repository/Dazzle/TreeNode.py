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


class TreeNode(__gi_repository_GObject.InitiallyUnowned):
    """
    :Constructors:
    
    ::
    
        TreeNode(**properties)
        new() -> Dazzle.TreeNode
    """
    def add_emblem(self, emblem_name): # real signature unknown; restored from __doc__
        """ add_emblem(self, emblem_name:str) """
        pass

    def append(self, child): # real signature unknown; restored from __doc__
        """ append(self, child:Dazzle.TreeNode) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_emblems(self): # real signature unknown; restored from __doc__
        """ clear_emblems(self) """
        pass

    def collapse(self): # real signature unknown; restored from __doc__
        """ collapse(self) """
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

    def expand(self, expand_ancestors): # real signature unknown; restored from __doc__
        """ expand(self, expand_ancestors:bool) -> bool """
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

    def get_area(self, area): # real signature unknown; restored from __doc__
        """ get_area(self, area:Gdk.Rectangle) """
        pass

    def get_children_possible(self): # real signature unknown; restored from __doc__
        """ get_children_possible(self) -> bool """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_expanded(self): # real signature unknown; restored from __doc__
        """ get_expanded(self) -> bool """
        return False

    def get_foreground_rgba(self): # real signature unknown; restored from __doc__
        """ get_foreground_rgba(self) -> Gdk.RGBA or None """
        pass

    def get_gicon(self): # real signature unknown; restored from __doc__
        """ get_gicon(self) -> Gio.Icon """
        pass

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str """
        return ""

    def get_item(self): # real signature unknown; restored from __doc__
        """ get_item(self) -> GObject.Object """
        pass

    def get_iter(self, iter): # real signature unknown; restored from __doc__
        """ get_iter(self, iter:Gtk.TreeIter) -> bool """
        return False

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Dazzle.TreeNode """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gtk.TreePath or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_reset_on_collapse(self): # real signature unknown; restored from __doc__
        """ get_reset_on_collapse(self) -> bool """
        return False

    def get_text(self): # real signature unknown; restored from __doc__
        """ get_text(self) -> str """
        return ""

    def get_tree(self): # real signature unknown; restored from __doc__
        """ get_tree(self) -> Dazzle.Tree """
        pass

    def get_use_dim_label(self): # real signature unknown; restored from __doc__
        """ get_use_dim_label(self) -> bool """
        return False

    def get_use_markup(self): # real signature unknown; restored from __doc__
        """ get_use_markup(self) -> bool """
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

    def has_emblem(self, emblem_name): # real signature unknown; restored from __doc__
        """ has_emblem(self, emblem_name:str) -> bool """
        return False

    def insert(self, child, position): # real signature unknown; restored from __doc__
        """ insert(self, child:Dazzle.TreeNode, position:int) """
        pass

    def insert_sorted(self, child, compare_func, user_data=None): # real signature unknown; restored from __doc__
        """ insert_sorted(self, child:Dazzle.TreeNode, compare_func:Dazzle.TreeNodeCompareFunc, user_data=None) """
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

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_root(self): # real signature unknown; restored from __doc__
        """ is_root(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Dazzle.TreeNode """
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

    def nth_child(self, nth): # real signature unknown; restored from __doc__
        """ nth_child(self, nth:int) -> Dazzle.TreeNode or None """
        pass

    def n_children(self): # real signature unknown; restored from __doc__
        """ n_children(self) -> int """
        return 0

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def prepend(self, child): # real signature unknown; restored from __doc__
        """ prepend(self, child:Dazzle.TreeNode) """
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

    def remove(self, child): # real signature unknown; restored from __doc__
        """ remove(self, child:Dazzle.TreeNode) """
        pass

    def remove_emblem(self, emblem_name): # real signature unknown; restored from __doc__
        """ remove_emblem(self, emblem_name:str) """
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

    def select(self): # real signature unknown; restored from __doc__
        """ select(self) """
        pass

    def set_children_possible(self, children_possible): # real signature unknown; restored from __doc__
        """ set_children_possible(self, children_possible:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_emblems(self, emblems): # real signature unknown; restored from __doc__
        """ set_emblems(self, emblems:str) """
        pass

    def set_foreground_rgba(self, foreground_rgba=None): # real signature unknown; restored from __doc__
        """ set_foreground_rgba(self, foreground_rgba:Gdk.RGBA=None) """
        pass

    def set_gicon(self, icon): # real signature unknown; restored from __doc__
        """ set_gicon(self, icon:Gio.Icon) """
        pass

    def set_icon_name(self, icon_name=None): # real signature unknown; restored from __doc__
        """ set_icon_name(self, icon_name:str=None) """
        pass

    def set_item(self, item): # real signature unknown; restored from __doc__
        """ set_item(self, item:GObject.Object) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_reset_on_collapse(self, reset_on_collapse): # real signature unknown; restored from __doc__
        """ set_reset_on_collapse(self, reset_on_collapse:bool) """
        pass

    def set_text(self, text=None): # real signature unknown; restored from __doc__
        """ set_text(self, text:str=None) """
        pass

    def set_use_dim_label(self, use_dim_label): # real signature unknown; restored from __doc__
        """ set_use_dim_label(self, use_dim_label:bool) """
        pass

    def set_use_markup(self, use_markup): # real signature unknown; restored from __doc__
        """ set_use_markup(self, use_markup:bool) """
        pass

    def show_popover(self, popover): # real signature unknown; restored from __doc__
        """ show_popover(self, popover:Gtk.Popover) """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f3b25efee50>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TreeNode), '__module__': 'gi.repository.Dazzle', '__gtype__': <GType DzlTreeNode (93962411863888)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_emblem': gi.FunctionInfo(add_emblem), 'append': gi.FunctionInfo(append), 'clear_emblems': gi.FunctionInfo(clear_emblems), 'collapse': gi.FunctionInfo(collapse), 'expand': gi.FunctionInfo(expand), 'get_area': gi.FunctionInfo(get_area), 'get_children_possible': gi.FunctionInfo(get_children_possible), 'get_expanded': gi.FunctionInfo(get_expanded), 'get_foreground_rgba': gi.FunctionInfo(get_foreground_rgba), 'get_gicon': gi.FunctionInfo(get_gicon), 'get_icon_name': gi.FunctionInfo(get_icon_name), 'get_item': gi.FunctionInfo(get_item), 'get_iter': gi.FunctionInfo(get_iter), 'get_parent': gi.FunctionInfo(get_parent), 'get_path': gi.FunctionInfo(get_path), 'get_reset_on_collapse': gi.FunctionInfo(get_reset_on_collapse), 'get_text': gi.FunctionInfo(get_text), 'get_tree': gi.FunctionInfo(get_tree), 'get_use_dim_label': gi.FunctionInfo(get_use_dim_label), 'get_use_markup': gi.FunctionInfo(get_use_markup), 'has_emblem': gi.FunctionInfo(has_emblem), 'insert': gi.FunctionInfo(insert), 'insert_sorted': gi.FunctionInfo(insert_sorted), 'invalidate': gi.FunctionInfo(invalidate), 'is_root': gi.FunctionInfo(is_root), 'n_children': gi.FunctionInfo(n_children), 'nth_child': gi.FunctionInfo(nth_child), 'prepend': gi.FunctionInfo(prepend), 'rebuild': gi.FunctionInfo(rebuild), 'remove': gi.FunctionInfo(remove), 'remove_emblem': gi.FunctionInfo(remove_emblem), 'select': gi.FunctionInfo(select), 'set_children_possible': gi.FunctionInfo(set_children_possible), 'set_emblems': gi.FunctionInfo(set_emblems), 'set_foreground_rgba': gi.FunctionInfo(set_foreground_rgba), 'set_gicon': gi.FunctionInfo(set_gicon), 'set_icon_name': gi.FunctionInfo(set_icon_name), 'set_item': gi.FunctionInfo(set_item), 'set_reset_on_collapse': gi.FunctionInfo(set_reset_on_collapse), 'set_text': gi.FunctionInfo(set_text), 'set_use_dim_label': gi.FunctionInfo(set_use_dim_label), 'set_use_markup': gi.FunctionInfo(set_use_markup), 'show_popover': gi.FunctionInfo(show_popover)})"
    __gdoc__ = 'Object DzlTreeNode\n\nProperties from DzlTreeNode:\n  children-possible -> gboolean: Children Possible\n    Allows for lazy creation of children nodes.\n  expanded-icon-name -> gchararray: Expanded Icon Name\n    The icon-name to use when the row is expanded\n  icon-name -> gchararray: Icon Name\n    The icon name to display.\n  gicon -> GIcon: GIcon\n    The GIcon object\n  item -> GObject: Item\n    Optional object to associate with node.\n  parent -> DzlTreeNode: Parent\n    The parent node.\n  reset-on-collapse -> gboolean: Reset on Collapse\n    Reset by clearing children on collapse, requiring a rebuild on next expand\n  text -> gchararray: Text\n    The text of the node.\n  tree -> DzlTree: Tree\n    The DzlTree the node belongs to.\n  use-dim-label -> gboolean: Use Dim Label\n    If text should be rendered with a dim label.\n  use-markup -> gboolean: Use Markup\n    If text should be translated as markup.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType DzlTreeNode (93962411863888)>'
    __info__ = ObjectInfo(TreeNode)


