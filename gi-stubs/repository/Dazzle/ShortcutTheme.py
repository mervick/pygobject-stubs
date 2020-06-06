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


class ShortcutTheme(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        ShortcutTheme(**properties)
        new(name:str) -> Dazzle.ShortcutTheme
    """
    def add_command(self, accelerator, command): # real signature unknown; restored from __doc__
        """ add_command(self, accelerator:str, command:str) """
        pass

    def add_context(self, context): # real signature unknown; restored from __doc__
        """ add_context(self, context:Dazzle.ShortcutContext) """
        pass

    def add_css_resource(self, path): # real signature unknown; restored from __doc__
        """ add_css_resource(self, path:str) """
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

    def find_context_by_name(self, name): # real signature unknown; restored from __doc__
        """ find_context_by_name(self, name:str) -> Dazzle.ShortcutContext """
        pass

    def find_default_context(self, widget): # real signature unknown; restored from __doc__
        """ find_default_context(self, widget:Gtk.Widget) -> Dazzle.ShortcutContext or None """
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

    def get_chord_for_action(self, detailed_action_name): # real signature unknown; restored from __doc__
        """ get_chord_for_action(self, detailed_action_name:str) -> Dazzle.ShortcutChord """
        pass

    def get_chord_for_command(self, command): # real signature unknown; restored from __doc__
        """ get_chord_for_command(self, command:str) -> Dazzle.ShortcutChord """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Dazzle.ShortcutTheme or None """
        pass

    def get_parent_name(self): # real signature unknown; restored from __doc__
        """ get_parent_name(self) -> str or None """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_subtitle(self): # real signature unknown; restored from __doc__
        """ get_subtitle(self) -> str """
        return ""

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
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

    def load_from_data(self, data, len): # real signature unknown; restored from __doc__
        """ load_from_data(self, data:str, len:int) -> bool """
        return False

    def load_from_file(self, file, cancellable=None): # real signature unknown; restored from __doc__
        """ load_from_file(self, file:Gio.File, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def load_from_path(self, path, cancellable=None): # real signature unknown; restored from __doc__
        """ load_from_path(self, path:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def new(self, name): # real signature unknown; restored from __doc__
        """ new(name:str) -> Dazzle.ShortcutTheme """
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

    def remove_css_resource(self, path): # real signature unknown; restored from __doc__
        """ remove_css_resource(self, path:str) """
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

    def save_to_file(self, file, cancellable=None): # real signature unknown; restored from __doc__
        """ save_to_file(self, file:Gio.File, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def save_to_path(self, path, cancellable=None): # real signature unknown; restored from __doc__
        """ save_to_path(self, path:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def save_to_stream(self, stream, cancellable=None): # real signature unknown; restored from __doc__
        """ save_to_stream(self, stream:Gio.OutputStream, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_accel_for_action(self, detailed_action_name, accel, phase): # real signature unknown; restored from __doc__
        """ set_accel_for_action(self, detailed_action_name:str, accel:str, phase:Dazzle.ShortcutPhase) """
        pass

    def set_accel_for_command(self, command=None, accel=None, phase): # real signature unknown; restored from __doc__
        """ set_accel_for_command(self, command:str=None, accel:str=None, phase:Dazzle.ShortcutPhase) """
        pass

    def set_chord_for_action(self, detailed_action_name, chord, phase): # real signature unknown; restored from __doc__
        """ set_chord_for_action(self, detailed_action_name:str, chord:Dazzle.ShortcutChord, phase:Dazzle.ShortcutPhase) """
        pass

    def set_chord_for_command(self, command=None, chord=None, phase): # real signature unknown; restored from __doc__
        """ set_chord_for_command(self, command:str=None, chord:Dazzle.ShortcutChord=None, phase:Dazzle.ShortcutPhase) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_parent_name(self, parent_name): # real signature unknown; restored from __doc__
        """ set_parent_name(self, parent_name:str) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f3b25ca9e80>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ShortcutTheme), '__module__': 'gi.repository.Dazzle', '__gtype__': <GType DzlShortcutTheme (93962411716368)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_command': gi.FunctionInfo(add_command), 'add_context': gi.FunctionInfo(add_context), 'add_css_resource': gi.FunctionInfo(add_css_resource), 'find_context_by_name': gi.FunctionInfo(find_context_by_name), 'find_default_context': gi.FunctionInfo(find_default_context), 'get_chord_for_action': gi.FunctionInfo(get_chord_for_action), 'get_chord_for_command': gi.FunctionInfo(get_chord_for_command), 'get_name': gi.FunctionInfo(get_name), 'get_parent': gi.FunctionInfo(get_parent), 'get_parent_name': gi.FunctionInfo(get_parent_name), 'get_subtitle': gi.FunctionInfo(get_subtitle), 'get_title': gi.FunctionInfo(get_title), 'load_from_data': gi.FunctionInfo(load_from_data), 'load_from_file': gi.FunctionInfo(load_from_file), 'load_from_path': gi.FunctionInfo(load_from_path), 'remove_css_resource': gi.FunctionInfo(remove_css_resource), 'save_to_file': gi.FunctionInfo(save_to_file), 'save_to_path': gi.FunctionInfo(save_to_path), 'save_to_stream': gi.FunctionInfo(save_to_stream), 'set_accel_for_action': gi.FunctionInfo(set_accel_for_action), 'set_accel_for_command': gi.FunctionInfo(set_accel_for_command), 'set_chord_for_action': gi.FunctionInfo(set_chord_for_action), 'set_chord_for_command': gi.FunctionInfo(set_chord_for_command), 'set_parent_name': gi.FunctionInfo(set_parent_name), 'parent_instance': <property object at 0x7f3b25f55f90>})"
    __gdoc__ = 'Object DzlShortcutTheme\n\nProperties from DzlShortcutTheme:\n  name -> gchararray: Name\n    The name of the theme\n  parent-name -> gchararray: Parent Name\n    The name of the parent shortcut theme\n  subtitle -> gchararray: Subtitle\n    The subtitle of the theme as used for UI elements\n  title -> gchararray: Title\n    The title of the theme as used for UI elements\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType DzlShortcutTheme (93962411716368)>'
    __info__ = ObjectInfo(ShortcutTheme)


