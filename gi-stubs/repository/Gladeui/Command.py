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


class Command(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Command(**properties)
    """
    def add(self, widgets, parent, placeholder, project, pasting): # real signature unknown; restored from __doc__
        """ add(widgets:list, parent:Gladeui.Widget, placeholder:Gladeui.Placeholder, project:Gladeui.Project, pasting:bool) """
        pass

    def add_signal(self, glade_widget, signal): # real signature unknown; restored from __doc__
        """ add_signal(glade_widget:Gladeui.Widget, signal:Gladeui.Signal) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_signal(self, glade_widget, old_signal, new_signal): # real signature unknown; restored from __doc__
        """ change_signal(glade_widget:Gladeui.Widget, old_signal:Gladeui.Signal, new_signal:Gladeui.Signal) """
        pass

    def collapse(self, other): # real signature unknown; restored from __doc__
        """ collapse(self, other:Gladeui.Command) """
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

    def create(self, adaptor, parent=None, placeholder=None, project): # real signature unknown; restored from __doc__
        """ create(adaptor:Gladeui.WidgetAdaptor, parent:Gladeui.Widget=None, placeholder:Gladeui.Placeholder=None, project:Gladeui.Project) -> Gladeui.Widget """
        pass

    def cut(self, widgets): # real signature unknown; restored from __doc__
        """ cut(widgets:list) """
        pass

    def delete(self, widgets): # real signature unknown; restored from __doc__
        """ delete(widgets:list) """
        pass

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def dnd(self, widgets, parent=None, placeholder=None): # real signature unknown; restored from __doc__
        """ dnd(widgets:list, parent:Gladeui.Widget=None, placeholder:Gladeui.Placeholder=None) """
        pass

    def do_collapse(self, *args, **kwargs): # real signature unknown
        """ collapse(self, other:Gladeui.Command) """
        pass

    def do_execute(self, *args, **kwargs): # real signature unknown
        """ execute(self) -> bool """
        pass

    def do_undo(self, *args, **kwargs): # real signature unknown
        """ undo(self) -> bool """
        pass

    def do_unifies(self, *args, **kwargs): # real signature unknown
        """ unifies(self, other:Gladeui.Command) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def execute(self): # real signature unknown; restored from __doc__
        """ execute(self) -> bool """
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

    def get_group_depth(self): # real signature unknown; restored from __doc__
        """ get_group_depth() -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def group_id(self): # real signature unknown; restored from __doc__
        """ group_id(self) -> int """
        return 0

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

    def lock_widget(self, widget, locked): # real signature unknown; restored from __doc__
        """ lock_widget(widget:Gladeui.Widget, locked:Gladeui.Widget) """
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

    def paste(self, widgets, parent=None, placeholder=None, project): # real signature unknown; restored from __doc__
        """ paste(widgets:list, parent:Gladeui.Widget=None, placeholder:Gladeui.Placeholder=None, project:Gladeui.Project) """
        pass

    def pop_group(self): # real signature unknown; restored from __doc__
        """ pop_group() """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_signal(self, glade_widget, signal): # real signature unknown; restored from __doc__
        """ remove_signal(glade_widget:Gladeui.Widget, signal:Gladeui.Signal) """
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

    def set_i18n(self, property, translatable, context, comment): # real signature unknown; restored from __doc__
        """ set_i18n(property:Gladeui.Property, translatable:bool, context:str, comment:str) """
        pass

    def set_name(self, glade_widget, name): # real signature unknown; restored from __doc__
        """ set_name(glade_widget:Gladeui.Widget, name:str) """
        pass

    def set_project_domain(self, project, domain): # real signature unknown; restored from __doc__
        """ set_project_domain(project:Gladeui.Project, domain:str) """
        pass

    def set_project_license(self, project, license): # real signature unknown; restored from __doc__
        """ set_project_license(project:Gladeui.Project, license:str) """
        pass

    def set_project_resource_path(self, project, path): # real signature unknown; restored from __doc__
        """ set_project_resource_path(project:Gladeui.Project, path:str) """
        pass

    def set_project_target(self, project, catalog, major, minor): # real signature unknown; restored from __doc__
        """ set_project_target(project:Gladeui.Project, catalog:str, major:int, minor:int) """
        pass

    def set_project_template(self, project, widget): # real signature unknown; restored from __doc__
        """ set_project_template(project:Gladeui.Project, widget:Gladeui.Widget) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_properties_list(self, project, props): # real signature unknown; restored from __doc__
        """ set_properties_list(project:Gladeui.Project, props:list) """
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_property_enabled(self, property, enabled): # real signature unknown; restored from __doc__
        """ set_property_enabled(property:Gladeui.Property, enabled:bool) """
        pass

    def set_property_value(self, property, value): # real signature unknown; restored from __doc__
        """ set_property_value(property:Gladeui.Property, value:GObject.Value) """
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

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) -> bool """
        return False

    def unifies(self, other): # real signature unknown; restored from __doc__
        """ unifies(self, other:Gladeui.Command) -> bool """
        return False

    def unlock_widget(self, widget): # real signature unknown; restored from __doc__
        """ unlock_widget(widget:Gladeui.Widget) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1341791670>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Command), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType GladeCommand (94653530157088)>, '__doc__': None, '__gsignals__': {}, 'add': gi.FunctionInfo(add), 'add_signal': gi.FunctionInfo(add_signal), 'change_signal': gi.FunctionInfo(change_signal), 'create': gi.FunctionInfo(create), 'cut': gi.FunctionInfo(cut), 'delete': gi.FunctionInfo(delete), 'dnd': gi.FunctionInfo(dnd), 'get_group_depth': gi.FunctionInfo(get_group_depth), 'lock_widget': gi.FunctionInfo(lock_widget), 'paste': gi.FunctionInfo(paste), 'pop_group': gi.FunctionInfo(pop_group), 'remove_signal': gi.FunctionInfo(remove_signal), 'set_i18n': gi.FunctionInfo(set_i18n), 'set_name': gi.FunctionInfo(set_name), 'set_project_domain': gi.FunctionInfo(set_project_domain), 'set_project_license': gi.FunctionInfo(set_project_license), 'set_project_resource_path': gi.FunctionInfo(set_project_resource_path), 'set_project_target': gi.FunctionInfo(set_project_target), 'set_project_template': gi.FunctionInfo(set_project_template), 'set_properties_list': gi.FunctionInfo(set_properties_list), 'set_property_enabled': gi.FunctionInfo(set_property_enabled), 'set_property_value': gi.FunctionInfo(set_property_value), 'unlock_widget': gi.FunctionInfo(unlock_widget), 'collapse': gi.FunctionInfo(collapse), 'description': gi.FunctionInfo(description), 'execute': gi.FunctionInfo(execute), 'group_id': gi.FunctionInfo(group_id), 'undo': gi.FunctionInfo(undo), 'unifies': gi.FunctionInfo(unifies), 'do_collapse': gi.VFuncInfo(collapse), 'do_execute': gi.VFuncInfo(execute), 'do_undo': gi.VFuncInfo(undo), 'do_unifies': gi.VFuncInfo(unifies), 'parent_instance': <property object at 0x7f1341a29d10>})"
    __gdoc__ = 'Object GladeCommand\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GladeCommand (94653530157088)>'
    __info__ = ObjectInfo(Command)


