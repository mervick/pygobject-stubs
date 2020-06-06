# encoding: utf-8
# module gi.repository.WebKit2WebExtension
# from /usr/lib64/girepository-1.0/WebKit2WebExtension-4.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .DOMEvent import DOMEvent

class DOMUIEvent(DOMEvent):
    """
    :Constructors:
    
    ::
    
        DOMUIEvent(**properties)
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

    def get_bubbles(self): # real signature unknown; restored from __doc__
        """ get_bubbles(self) -> bool """
        return False

    def get_cancelable(self): # real signature unknown; restored from __doc__
        """ get_cancelable(self) -> bool """
        return False

    def get_cancel_bubble(self): # real signature unknown; restored from __doc__
        """ get_cancel_bubble(self) -> bool """
        return False

    def get_char_code(self): # real signature unknown; restored from __doc__
        """ get_char_code(self) -> int """
        return 0

    def get_current_target(self): # real signature unknown; restored from __doc__
        """ get_current_target(self) -> WebKit2WebExtension.DOMEventTarget """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_detail(self): # real signature unknown; restored from __doc__
        """ get_detail(self) -> int """
        return 0

    def get_event_phase(self): # real signature unknown; restored from __doc__
        """ get_event_phase(self) -> int """
        return 0

    def get_event_type(self): # real signature unknown; restored from __doc__
        """ get_event_type(self) -> str """
        return ""

    def get_key_code(self): # real signature unknown; restored from __doc__
        """ get_key_code(self) -> int """
        return 0

    def get_layer_x(self): # real signature unknown; restored from __doc__
        """ get_layer_x(self) -> int """
        return 0

    def get_layer_y(self): # real signature unknown; restored from __doc__
        """ get_layer_y(self) -> int """
        return 0

    def get_page_x(self): # real signature unknown; restored from __doc__
        """ get_page_x(self) -> int """
        return 0

    def get_page_y(self): # real signature unknown; restored from __doc__
        """ get_page_y(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_return_value(self): # real signature unknown; restored from __doc__
        """ get_return_value(self) -> bool """
        return False

    def get_src_element(self): # real signature unknown; restored from __doc__
        """ get_src_element(self) -> WebKit2WebExtension.DOMEventTarget """
        pass

    def get_target(self): # real signature unknown; restored from __doc__
        """ get_target(self) -> WebKit2WebExtension.DOMEventTarget """
        pass

    def get_time_stamp(self): # real signature unknown; restored from __doc__
        """ get_time_stamp(self) -> int """
        return 0

    def get_view(self): # real signature unknown; restored from __doc__
        """ get_view(self) -> WebKit2WebExtension.DOMDOMWindow """
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

    def init_event(self, eventTypeArg, canBubbleArg, cancelableArg): # real signature unknown; restored from __doc__
        """ init_event(self, eventTypeArg:str, canBubbleArg:bool, cancelableArg:bool) """
        pass

    def init_ui_event(self, type, canBubble, cancelable, view, detail): # real signature unknown; restored from __doc__
        """ init_ui_event(self, type:str, canBubble:bool, cancelable:bool, view:WebKit2WebExtension.DOMDOMWindow, detail:int) """
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

    def prevent_default(self): # real signature unknown; restored from __doc__
        """ prevent_default(self) """
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

    def set_cancel_bubble(self, value): # real signature unknown; restored from __doc__
        """ set_cancel_bubble(self, value:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_return_value(self, value): # real signature unknown; restored from __doc__
        """ set_return_value(self, value:bool) """
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

    def stop_propagation(self): # real signature unknown; restored from __doc__
        """ stop_propagation(self) """
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

    coreObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parentInstance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1744da91c0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DOMUIEvent), '__module__': 'gi.repository.WebKit2WebExtension', '__gtype__': <GType WebKitDOMUIEvent (94252901776704)>, '__doc__': None, '__gsignals__': {}, 'get_char_code': gi.FunctionInfo(get_char_code), 'get_detail': gi.FunctionInfo(get_detail), 'get_key_code': gi.FunctionInfo(get_key_code), 'get_layer_x': gi.FunctionInfo(get_layer_x), 'get_layer_y': gi.FunctionInfo(get_layer_y), 'get_page_x': gi.FunctionInfo(get_page_x), 'get_page_y': gi.FunctionInfo(get_page_y), 'get_view': gi.FunctionInfo(get_view), 'init_ui_event': gi.FunctionInfo(init_ui_event), 'parent_instance': <property object at 0x7f1745635590>})"
    __gdoc__ = 'Object WebKitDOMUIEvent\n\nProperties from WebKitDOMUIEvent:\n  view -> WebKitDOMDOMWindow: UIEvent:view\n    read-only WebKitDOMDOMWindow* UIEvent:view\n  detail -> glong: UIEvent:detail\n    read-only glong UIEvent:detail\n  key-code -> glong: UIEvent:key-code\n    read-only glong UIEvent:key-code\n  char-code -> glong: UIEvent:char-code\n    read-only glong UIEvent:char-code\n  layer-x -> glong: UIEvent:layer-x\n    read-only glong UIEvent:layer-x\n  layer-y -> glong: UIEvent:layer-y\n    read-only glong UIEvent:layer-y\n  page-x -> glong: UIEvent:page-x\n    read-only glong UIEvent:page-x\n  page-y -> glong: UIEvent:page-y\n    read-only glong UIEvent:page-y\n\nProperties from WebKitDOMEvent:\n  type -> gchararray: Event:type\n    read-only gchar* Event:type\n  target -> WebKitDOMEventTarget: Event:target\n    read-only WebKitDOMEventTarget* Event:target\n  current-target -> WebKitDOMEventTarget: Event:current-target\n    read-only WebKitDOMEventTarget* Event:current-target\n  event-phase -> guint: Event:event-phase\n    read-only gushort Event:event-phase\n  bubbles -> gboolean: Event:bubbles\n    read-only gboolean Event:bubbles\n  cancelable -> gboolean: Event:cancelable\n    read-only gboolean Event:cancelable\n  time-stamp -> guint: Event:time-stamp\n    read-only guint32 Event:time-stamp\n  src-element -> WebKitDOMEventTarget: Event:src-element\n    read-only WebKitDOMEventTarget* Event:src-element\n  return-value -> gboolean: Event:return-value\n    read-write gboolean Event:return-value\n  cancel-bubble -> gboolean: Event:cancel-bubble\n    read-write gboolean Event:cancel-bubble\n\nProperties from WebKitDOMObject:\n  core-object -> gpointer: Core Object\n    The WebCore object the WebKitDOMObject wraps\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType WebKitDOMUIEvent (94252901776704)>'
    __info__ = ObjectInfo(DOMUIEvent)


