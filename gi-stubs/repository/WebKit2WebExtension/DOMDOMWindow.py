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


from .DOMObject import DOMObject

from .DOMEventTarget import DOMEventTarget

class DOMDOMWindow(DOMObject, DOMEventTarget):
    """
    :Constructors:
    
    ::
    
        DOMDOMWindow(**properties)
    """
    def add_event_listener(self, event_name, handler, use_capture): # real signature unknown; restored from __doc__
        """ add_event_listener(self, event_name:str, handler:GObject.Closure, use_capture:bool) -> bool """
        return False

    def alert(self, message): # real signature unknown; restored from __doc__
        """ alert(self, message:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def blur(self): # real signature unknown; restored from __doc__
        """ blur(self) """
        pass

    def capture_events(self): # real signature unknown; restored from __doc__
        """ capture_events(self) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def confirm(self, message): # real signature unknown; restored from __doc__
        """ confirm(self, message:str) -> bool """
        return False

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

    def dispatch_event(self, event): # real signature unknown; restored from __doc__
        """ dispatch_event(self, event:WebKit2WebExtension.DOMEvent) -> bool """
        return False

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find(self, string, caseSensitive, backwards, wrap, wholeWord, searchInFrames, showDialog): # real signature unknown; restored from __doc__
        """ find(self, string:str, caseSensitive:bool, backwards:bool, wrap:bool, wholeWord:bool, searchInFrames:bool, showDialog:bool) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def focus(self): # real signature unknown; restored from __doc__
        """ focus(self) """
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

    def get_closed(self): # real signature unknown; restored from __doc__
        """ get_closed(self) -> bool """
        return False

    def get_computed_style(self, element, pseudoElement=None): # real signature unknown; restored from __doc__
        """ get_computed_style(self, element:WebKit2WebExtension.DOMElement, pseudoElement:str=None) -> WebKit2WebExtension.DOMCSSStyleDeclaration """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_status(self): # real signature unknown; restored from __doc__
        """ get_default_status(self) -> str """
        return ""

    def get_device_pixel_ratio(self): # real signature unknown; restored from __doc__
        """ get_device_pixel_ratio(self) -> float """
        return 0.0

    def get_document(self): # real signature unknown; restored from __doc__
        """ get_document(self) -> WebKit2WebExtension.DOMDocument """
        pass

    def get_frames(self): # real signature unknown; restored from __doc__
        """ get_frames(self) -> WebKit2WebExtension.DOMDOMWindow """
        pass

    def get_frame_element(self): # real signature unknown; restored from __doc__
        """ get_frame_element(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_inner_height(self): # real signature unknown; restored from __doc__
        """ get_inner_height(self) -> int """
        return 0

    def get_inner_width(self): # real signature unknown; restored from __doc__
        """ get_inner_width(self) -> int """
        return 0

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_offscreen_buffering(self): # real signature unknown; restored from __doc__
        """ get_offscreen_buffering(self) -> bool """
        return False

    def get_opener(self): # real signature unknown; restored from __doc__
        """ get_opener(self) -> WebKit2WebExtension.DOMDOMWindow """
        pass

    def get_orientation(self): # real signature unknown; restored from __doc__
        """ get_orientation(self) -> int """
        return 0

    def get_outer_height(self): # real signature unknown; restored from __doc__
        """ get_outer_height(self) -> int """
        return 0

    def get_outer_width(self): # real signature unknown; restored from __doc__
        """ get_outer_width(self) -> int """
        return 0

    def get_page_x_offset(self): # real signature unknown; restored from __doc__
        """ get_page_x_offset(self) -> int """
        return 0

    def get_page_y_offset(self): # real signature unknown; restored from __doc__
        """ get_page_y_offset(self) -> int """
        return 0

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> WebKit2WebExtension.DOMDOMWindow """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_screen_left(self): # real signature unknown; restored from __doc__
        """ get_screen_left(self) -> int """
        return 0

    def get_screen_top(self): # real signature unknown; restored from __doc__
        """ get_screen_top(self) -> int """
        return 0

    def get_screen_x(self): # real signature unknown; restored from __doc__
        """ get_screen_x(self) -> int """
        return 0

    def get_screen_y(self): # real signature unknown; restored from __doc__
        """ get_screen_y(self) -> int """
        return 0

    def get_scroll_x(self): # real signature unknown; restored from __doc__
        """ get_scroll_x(self) -> int """
        return 0

    def get_scroll_y(self): # real signature unknown; restored from __doc__
        """ get_scroll_y(self) -> int """
        return 0

    def get_selection(self): # real signature unknown; restored from __doc__
        """ get_selection(self) -> WebKit2WebExtension.DOMDOMSelection """
        pass

    def get_self(self): # real signature unknown; restored from __doc__
        """ get_self(self) -> WebKit2WebExtension.DOMDOMWindow """
        pass

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> str """
        return ""

    def get_top(self): # real signature unknown; restored from __doc__
        """ get_top(self) -> WebKit2WebExtension.DOMDOMWindow """
        pass

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> WebKit2WebExtension.DOMDOMWindow """
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

    def move_by(self, x, y): # real signature unknown; restored from __doc__
        """ move_by(self, x:float, y:float) """
        pass

    def move_to(self, x, y): # real signature unknown; restored from __doc__
        """ move_to(self, x:float, y:float) """
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

    def print_(self): # real signature unknown; restored from __doc__
        """ print_(self) """
        pass

    def prompt(self, message, defaultValue): # real signature unknown; restored from __doc__
        """ prompt(self, message:str, defaultValue:str) -> str """
        return ""

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def release_events(self): # real signature unknown; restored from __doc__
        """ release_events(self) """
        pass

    def remove_event_listener(self, event_name, handler, use_capture): # real signature unknown; restored from __doc__
        """ remove_event_listener(self, event_name:str, handler:GObject.Closure, use_capture:bool) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def resize_by(self, x, y): # real signature unknown; restored from __doc__
        """ resize_by(self, x:float, y:float) """
        pass

    def resize_to(self, width, height): # real signature unknown; restored from __doc__
        """ resize_to(self, width:float, height:float) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scroll_by(self, x, y): # real signature unknown; restored from __doc__
        """ scroll_by(self, x:float, y:float) """
        pass

    def scroll_to(self, x, y): # real signature unknown; restored from __doc__
        """ scroll_to(self, x:float, y:float) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_status(self, value): # real signature unknown; restored from __doc__
        """ set_default_status(self, value:str) """
        pass

    def set_name(self, value): # real signature unknown; restored from __doc__
        """ set_name(self, value:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_status(self, value): # real signature unknown; restored from __doc__
        """ set_status(self, value:str) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
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

    def webkit_message_handlers_post_message(self, handler, message): # real signature unknown; restored from __doc__
        """ webkit_message_handlers_post_message(self, handler:str, message:str) -> bool """
        return False

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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    coreObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parentInstance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f17455d1e20>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DOMDOMWindow), '__module__': 'gi.repository.WebKit2WebExtension', '__gtype__': <GType WebKitDOMDOMWindow (94252901482560)>, '__doc__': None, '__gsignals__': {}, 'alert': gi.FunctionInfo(alert), 'blur': gi.FunctionInfo(blur), 'capture_events': gi.FunctionInfo(capture_events), 'close': gi.FunctionInfo(close), 'confirm': gi.FunctionInfo(confirm), 'find': gi.FunctionInfo(find), 'focus': gi.FunctionInfo(focus), 'get_closed': gi.FunctionInfo(get_closed), 'get_computed_style': gi.FunctionInfo(get_computed_style), 'get_default_status': gi.FunctionInfo(get_default_status), 'get_device_pixel_ratio': gi.FunctionInfo(get_device_pixel_ratio), 'get_document': gi.FunctionInfo(get_document), 'get_frame_element': gi.FunctionInfo(get_frame_element), 'get_frames': gi.FunctionInfo(get_frames), 'get_inner_height': gi.FunctionInfo(get_inner_height), 'get_inner_width': gi.FunctionInfo(get_inner_width), 'get_length': gi.FunctionInfo(get_length), 'get_name': gi.FunctionInfo(get_name), 'get_offscreen_buffering': gi.FunctionInfo(get_offscreen_buffering), 'get_opener': gi.FunctionInfo(get_opener), 'get_orientation': gi.FunctionInfo(get_orientation), 'get_outer_height': gi.FunctionInfo(get_outer_height), 'get_outer_width': gi.FunctionInfo(get_outer_width), 'get_page_x_offset': gi.FunctionInfo(get_page_x_offset), 'get_page_y_offset': gi.FunctionInfo(get_page_y_offset), 'get_parent': gi.FunctionInfo(get_parent), 'get_screen_left': gi.FunctionInfo(get_screen_left), 'get_screen_top': gi.FunctionInfo(get_screen_top), 'get_screen_x': gi.FunctionInfo(get_screen_x), 'get_screen_y': gi.FunctionInfo(get_screen_y), 'get_scroll_x': gi.FunctionInfo(get_scroll_x), 'get_scroll_y': gi.FunctionInfo(get_scroll_y), 'get_selection': gi.FunctionInfo(get_selection), 'get_self': gi.FunctionInfo(get_self), 'get_status': gi.FunctionInfo(get_status), 'get_top': gi.FunctionInfo(get_top), 'get_window': gi.FunctionInfo(get_window), 'move_by': gi.FunctionInfo(move_by), 'move_to': gi.FunctionInfo(move_to), 'print_': gi.FunctionInfo(print), 'prompt': gi.FunctionInfo(prompt), 'release_events': gi.FunctionInfo(release_events), 'resize_by': gi.FunctionInfo(resize_by), 'resize_to': gi.FunctionInfo(resize_to), 'scroll_by': gi.FunctionInfo(scroll_by), 'scroll_to': gi.FunctionInfo(scroll_to), 'set_default_status': gi.FunctionInfo(set_default_status), 'set_name': gi.FunctionInfo(set_name), 'set_status': gi.FunctionInfo(set_status), 'stop': gi.FunctionInfo(stop), 'webkit_message_handlers_post_message': gi.FunctionInfo(webkit_message_handlers_post_message), 'parent_instance': <property object at 0x7f174d0b11d0>})"
    __gdoc__ = 'Object WebKitDOMDOMWindow\n\nProperties from WebKitDOMDOMWindow:\n  frame-element -> WebKitDOMElement: DOMWindow:frame-element\n    read-only WebKitDOMElement* DOMWindow:frame-element\n  offscreen-buffering -> gboolean: DOMWindow:offscreen-buffering\n    read-only gboolean DOMWindow:offscreen-buffering\n  outer-height -> glong: DOMWindow:outer-height\n    read-only glong DOMWindow:outer-height\n  outer-width -> glong: DOMWindow:outer-width\n    read-only glong DOMWindow:outer-width\n  inner-height -> glong: DOMWindow:inner-height\n    read-only glong DOMWindow:inner-height\n  inner-width -> glong: DOMWindow:inner-width\n    read-only glong DOMWindow:inner-width\n  screen-x -> glong: DOMWindow:screen-x\n    read-only glong DOMWindow:screen-x\n  screen-y -> glong: DOMWindow:screen-y\n    read-only glong DOMWindow:screen-y\n  screen-left -> glong: DOMWindow:screen-left\n    read-only glong DOMWindow:screen-left\n  screen-top -> glong: DOMWindow:screen-top\n    read-only glong DOMWindow:screen-top\n  scroll-x -> glong: DOMWindow:scroll-x\n    read-only glong DOMWindow:scroll-x\n  scroll-y -> glong: DOMWindow:scroll-y\n    read-only glong DOMWindow:scroll-y\n  page-x-offset -> glong: DOMWindow:page-x-offset\n    read-only glong DOMWindow:page-x-offset\n  page-y-offset -> glong: DOMWindow:page-y-offset\n    read-only glong DOMWindow:page-y-offset\n  closed -> gboolean: DOMWindow:closed\n    read-only gboolean DOMWindow:closed\n  length -> gulong: DOMWindow:length\n    read-only gulong DOMWindow:length\n  name -> gchararray: DOMWindow:name\n    read-write gchar* DOMWindow:name\n  status -> gchararray: DOMWindow:status\n    read-write gchar* DOMWindow:status\n  default-status -> gchararray: DOMWindow:default-status\n    read-write gchar* DOMWindow:default-status\n  self -> WebKitDOMDOMWindow: DOMWindow:self\n    read-only WebKitDOMDOMWindow* DOMWindow:self\n  window -> WebKitDOMDOMWindow: DOMWindow:window\n    read-only WebKitDOMDOMWindow* DOMWindow:window\n  frames -> WebKitDOMDOMWindow: DOMWindow:frames\n    read-only WebKitDOMDOMWindow* DOMWindow:frames\n  opener -> WebKitDOMDOMWindow: DOMWindow:opener\n    read-only WebKitDOMDOMWindow* DOMWindow:opener\n  parent -> WebKitDOMDOMWindow: DOMWindow:parent\n    read-only WebKitDOMDOMWindow* DOMWindow:parent\n  top -> WebKitDOMDOMWindow: DOMWindow:top\n    read-only WebKitDOMDOMWindow* DOMWindow:top\n  document -> WebKitDOMDocument: DOMWindow:document\n    read-only WebKitDOMDocument* DOMWindow:document\n  device-pixel-ratio -> gdouble: DOMWindow:device-pixel-ratio\n    read-only gdouble DOMWindow:device-pixel-ratio\n  orientation -> glong: DOMWindow:orientation\n    read-only glong DOMWindow:orientation\n\nProperties from WebKitDOMObject:\n  core-object -> gpointer: Core Object\n    The WebCore object the WebKitDOMObject wraps\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType WebKitDOMDOMWindow (94252901482560)>'
    __info__ = ObjectInfo(DOMDOMWindow)


