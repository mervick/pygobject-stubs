# encoding: utf-8
# module gi.repository.GtkSource
# from /usr/lib64/girepository-1.0/GtkSource-3.0.typelib
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


class SearchContext(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        SearchContext(**properties)
        new(buffer:GtkSource.Buffer, settings:GtkSource.SearchSettings=None) -> GtkSource.SearchContext
    """
    def backward(self, iter): # real signature unknown; restored from __doc__
        """ backward(self, iter:Gtk.TextIter) -> bool, match_start:Gtk.TextIter, match_end:Gtk.TextIter, has_wrapped_around:bool """
        return False

    def backward_async(self, iter, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ backward_async(self, iter:Gtk.TextIter, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def backward_finish(self, result): # real signature unknown; restored from __doc__
        """ backward_finish(self, result:Gio.AsyncResult) -> bool, match_start:Gtk.TextIter, match_end:Gtk.TextIter, has_wrapped_around:bool """
        return False

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

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def forward(self, iter): # real signature unknown; restored from __doc__
        """ forward(self, iter:Gtk.TextIter) -> bool, match_start:Gtk.TextIter, match_end:Gtk.TextIter, has_wrapped_around:bool """
        return False

    def forward_async(self, iter, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ forward_async(self, iter:Gtk.TextIter, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def forward_finish(self, result): # real signature unknown; restored from __doc__
        """ forward_finish(self, result:Gio.AsyncResult) -> bool, match_start:Gtk.TextIter, match_end:Gtk.TextIter, has_wrapped_around:bool """
        return False

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

    def get_buffer(self): # real signature unknown; restored from __doc__
        """ get_buffer(self) -> GtkSource.Buffer """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_highlight(self): # real signature unknown; restored from __doc__
        """ get_highlight(self) -> bool """
        return False

    def get_match_style(self): # real signature unknown; restored from __doc__
        """ get_match_style(self) -> GtkSource.Style """
        pass

    def get_occurrences_count(self): # real signature unknown; restored from __doc__
        """ get_occurrences_count(self) -> int """
        return 0

    def get_occurrence_position(self, match_start, match_end): # real signature unknown; restored from __doc__
        """ get_occurrence_position(self, match_start:Gtk.TextIter, match_end:Gtk.TextIter) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_regex_error(self): # real signature unknown; restored from __doc__
        """ get_regex_error(self) -> error or None """
        pass

    def get_settings(self): # real signature unknown; restored from __doc__
        """ get_settings(self) -> GtkSource.SearchSettings """
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

    def new(self, buffer, settings=None): # real signature unknown; restored from __doc__
        """ new(buffer:GtkSource.Buffer, settings:GtkSource.SearchSettings=None) -> GtkSource.SearchContext """
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

    def replace(self, match_start, match_end, replace, replace_length): # real signature unknown; restored from __doc__
        """ replace(self, match_start:Gtk.TextIter, match_end:Gtk.TextIter, replace:str, replace_length:int) -> bool """
        return False

    def replace_all(self, replace, replace_length): # real signature unknown; restored from __doc__
        """ replace_all(self, replace:str, replace_length:int) -> int """
        return 0

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

    def set_highlight(self, highlight): # real signature unknown; restored from __doc__
        """ set_highlight(self, highlight:bool) """
        pass

    def set_match_style(self, match_style=None): # real signature unknown; restored from __doc__
        """ set_match_style(self, match_style:GtkSource.Style=None) """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f77ca442340>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SearchContext), '__module__': 'gi.repository.GtkSource', '__gtype__': <GType GtkSourceSearchContext (94260244620128)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'backward': gi.FunctionInfo(backward), 'backward_async': gi.FunctionInfo(backward_async), 'backward_finish': gi.FunctionInfo(backward_finish), 'forward': gi.FunctionInfo(forward), 'forward_async': gi.FunctionInfo(forward_async), 'forward_finish': gi.FunctionInfo(forward_finish), 'get_buffer': gi.FunctionInfo(get_buffer), 'get_highlight': gi.FunctionInfo(get_highlight), 'get_match_style': gi.FunctionInfo(get_match_style), 'get_occurrence_position': gi.FunctionInfo(get_occurrence_position), 'get_occurrences_count': gi.FunctionInfo(get_occurrences_count), 'get_regex_error': gi.FunctionInfo(get_regex_error), 'get_settings': gi.FunctionInfo(get_settings), 'replace': gi.FunctionInfo(replace), 'replace_all': gi.FunctionInfo(replace_all), 'set_highlight': gi.FunctionInfo(set_highlight), 'set_match_style': gi.FunctionInfo(set_match_style), 'parent': <property object at 0x7f77ca6e6e50>, 'priv': <property object at 0x7f77ca6e6f40>})"
    __gdoc__ = 'Object GtkSourceSearchContext\n\nProperties from GtkSourceSearchContext:\n  buffer -> GtkSourceBuffer: Buffer\n    The associated GtkSourceBuffer\n  settings -> GtkSourceSearchSettings: Settings\n    The associated GtkSourceSearchSettings\n  highlight -> gboolean: Highlight\n    Highlight search occurrences\n  match-style -> GtkSourceStyle: Match style\n    The text style for matches\n  occurrences-count -> gint: Occurrences count\n    Total number of search occurrences\n  regex-error -> gpointer: Regex error\n    Regular expression error\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkSourceSearchContext (94260244620128)>'
    __info__ = ObjectInfo(SearchContext)


