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


from .DOMText import DOMText

class DOMCDATASection(DOMText):
    """
    :Constructors:
    
    ::
    
        DOMCDATASection(**properties)
    """
    def add_event_listener(self, event_name, handler, use_capture): # real signature unknown; restored from __doc__
        """ add_event_listener(self, event_name:str, handler:GObject.Closure, use_capture:bool) -> bool """
        return False

    def append_child(self, newChild): # real signature unknown; restored from __doc__
        """ append_child(self, newChild:WebKit2WebExtension.DOMNode) -> WebKit2WebExtension.DOMNode """
        pass

    def append_data(self, data): # real signature unknown; restored from __doc__
        """ append_data(self, data:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clone_node(self, deep): # real signature unknown; restored from __doc__
        """ clone_node(self, deep:bool) -> WebKit2WebExtension.DOMNode """
        pass

    def clone_node_with_error(self, deep): # real signature unknown; restored from __doc__
        """ clone_node_with_error(self, deep:bool) -> WebKit2WebExtension.DOMNode """
        pass

    def compare_document_position(self, other): # real signature unknown; restored from __doc__
        """ compare_document_position(self, other:WebKit2WebExtension.DOMNode) -> int """
        return 0

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

    def contains(self, other): # real signature unknown; restored from __doc__
        """ contains(self, other:WebKit2WebExtension.DOMNode) -> bool """
        return False

    def delete_data(self, offset, length): # real signature unknown; restored from __doc__
        """ delete_data(self, offset:int, length:int) """
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

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def for_js_value(self, value): # real signature unknown; restored from __doc__
        """ for_js_value(value:JavaScriptCore.Value) -> WebKit2WebExtension.DOMNode """
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

    def get_base_uri(self): # real signature unknown; restored from __doc__
        """ get_base_uri(self) -> str """
        return ""

    def get_child_nodes(self): # real signature unknown; restored from __doc__
        """ get_child_nodes(self) -> WebKit2WebExtension.DOMNodeList """
        pass

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> str """
        return ""

    def get_first_child(self): # real signature unknown; restored from __doc__
        """ get_first_child(self) -> WebKit2WebExtension.DOMNode """
        pass

    def get_last_child(self): # real signature unknown; restored from __doc__
        """ get_last_child(self) -> WebKit2WebExtension.DOMNode """
        pass

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def get_local_name(self): # real signature unknown; restored from __doc__
        """ get_local_name(self) -> str """
        return ""

    def get_namespace_uri(self): # real signature unknown; restored from __doc__
        """ get_namespace_uri(self) -> str """
        return ""

    def get_next_sibling(self): # real signature unknown; restored from __doc__
        """ get_next_sibling(self) -> WebKit2WebExtension.DOMNode """
        pass

    def get_node_name(self): # real signature unknown; restored from __doc__
        """ get_node_name(self) -> str """
        return ""

    def get_node_type(self): # real signature unknown; restored from __doc__
        """ get_node_type(self) -> int """
        return 0

    def get_node_value(self): # real signature unknown; restored from __doc__
        """ get_node_value(self) -> str """
        return ""

    def get_owner_document(self): # real signature unknown; restored from __doc__
        """ get_owner_document(self) -> WebKit2WebExtension.DOMDocument """
        pass

    def get_parent_element(self): # real signature unknown; restored from __doc__
        """ get_parent_element(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_parent_node(self): # real signature unknown; restored from __doc__
        """ get_parent_node(self) -> WebKit2WebExtension.DOMNode """
        pass

    def get_prefix(self): # real signature unknown; restored from __doc__
        """ get_prefix(self) -> str """
        return ""

    def get_previous_sibling(self): # real signature unknown; restored from __doc__
        """ get_previous_sibling(self) -> WebKit2WebExtension.DOMNode """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_text_content(self): # real signature unknown; restored from __doc__
        """ get_text_content(self) -> str """
        return ""

    def get_whole_text(self): # real signature unknown; restored from __doc__
        """ get_whole_text(self) -> str """
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

    def has_child_nodes(self): # real signature unknown; restored from __doc__
        """ has_child_nodes(self) -> bool """
        return False

    def insert_before(self, newChild, refChild=None): # real signature unknown; restored from __doc__
        """ insert_before(self, newChild:WebKit2WebExtension.DOMNode, refChild:WebKit2WebExtension.DOMNode=None) -> WebKit2WebExtension.DOMNode """
        pass

    def insert_data(self, offset, data): # real signature unknown; restored from __doc__
        """ insert_data(self, offset:int, data:str) """
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

    def is_default_namespace(self, namespaceURI): # real signature unknown; restored from __doc__
        """ is_default_namespace(self, namespaceURI:str) -> bool """
        return False

    def is_equal_node(self, other): # real signature unknown; restored from __doc__
        """ is_equal_node(self, other:WebKit2WebExtension.DOMNode) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_same_node(self, other): # real signature unknown; restored from __doc__
        """ is_same_node(self, other:WebKit2WebExtension.DOMNode) -> bool """
        return False

    def is_supported(self, feature, version): # real signature unknown; restored from __doc__
        """ is_supported(self, feature:str, version:str) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lookup_namespace_uri(self, prefix): # real signature unknown; restored from __doc__
        """ lookup_namespace_uri(self, prefix:str) -> str """
        return ""

    def lookup_prefix(self, namespaceURI): # real signature unknown; restored from __doc__
        """ lookup_prefix(self, namespaceURI:str) -> str """
        return ""

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) """
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

    def remove_child(self, oldChild): # real signature unknown; restored from __doc__
        """ remove_child(self, oldChild:WebKit2WebExtension.DOMNode) -> WebKit2WebExtension.DOMNode """
        pass

    def remove_event_listener(self, event_name, handler, use_capture): # real signature unknown; restored from __doc__
        """ remove_event_listener(self, event_name:str, handler:GObject.Closure, use_capture:bool) -> bool """
        return False

    def replace_child(self, newChild, oldChild): # real signature unknown; restored from __doc__
        """ replace_child(self, newChild:WebKit2WebExtension.DOMNode, oldChild:WebKit2WebExtension.DOMNode) -> WebKit2WebExtension.DOMNode """
        pass

    def replace_data(self, offset, length, data): # real signature unknown; restored from __doc__
        """ replace_data(self, offset:int, length:int, data:str) """
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_whole_text(self, content): # real signature unknown; restored from __doc__
        """ replace_whole_text(self, content:str) -> WebKit2WebExtension.DOMText """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, value): # real signature unknown; restored from __doc__
        """ set_data(self, value:str) """
        pass

    def set_node_value(self, value): # real signature unknown; restored from __doc__
        """ set_node_value(self, value:str) """
        pass

    def set_prefix(self, value): # real signature unknown; restored from __doc__
        """ set_prefix(self, value:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_text_content(self, value): # real signature unknown; restored from __doc__
        """ set_text_content(self, value:str) """
        pass

    def split_text(self, offset): # real signature unknown; restored from __doc__
        """ split_text(self, offset:int) -> WebKit2WebExtension.DOMText """
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

    def substring_data(self, offset, length): # real signature unknown; restored from __doc__
        """ substring_data(self, offset:int, length:int) -> str """
        return ""

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f17455d1c70>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DOMCDATASection), '__module__': 'gi.repository.WebKit2WebExtension', '__gtype__': <GType WebKitDOMCDATASection (94252901443536)>, '__doc__': None, '__gsignals__': {}, 'parent_instance': <property object at 0x7f174d0a4590>})"
    __gdoc__ = 'Object WebKitDOMCDATASection\n\nProperties from WebKitDOMText:\n  whole-text -> gchararray: Text:whole-text\n    read-only gchar* Text:whole-text\n\nProperties from WebKitDOMCharacterData:\n  data -> gchararray: CharacterData:data\n    read-write gchar* CharacterData:data\n  length -> gulong: CharacterData:length\n    read-only gulong CharacterData:length\n\nProperties from WebKitDOMNode:\n  node-name -> gchararray: Node:node-name\n    read-only gchar* Node:node-name\n  node-value -> gchararray: Node:node-value\n    read-write gchar* Node:node-value\n  node-type -> guint: Node:node-type\n    read-only gushort Node:node-type\n  parent-node -> WebKitDOMNode: Node:parent-node\n    read-only WebKitDOMNode* Node:parent-node\n  child-nodes -> WebKitDOMNodeList: Node:child-nodes\n    read-only WebKitDOMNodeList* Node:child-nodes\n  first-child -> WebKitDOMNode: Node:first-child\n    read-only WebKitDOMNode* Node:first-child\n  last-child -> WebKitDOMNode: Node:last-child\n    read-only WebKitDOMNode* Node:last-child\n  previous-sibling -> WebKitDOMNode: Node:previous-sibling\n    read-only WebKitDOMNode* Node:previous-sibling\n  next-sibling -> WebKitDOMNode: Node:next-sibling\n    read-only WebKitDOMNode* Node:next-sibling\n  owner-document -> WebKitDOMDocument: Node:owner-document\n    read-only WebKitDOMDocument* Node:owner-document\n  base-uri -> gchararray: Node:base-uri\n    read-only gchar* Node:base-uri\n  text-content -> gchararray: Node:text-content\n    read-write gchar* Node:text-content\n  parent-element -> WebKitDOMElement: Node:parent-element\n    read-only WebKitDOMElement* Node:parent-element\n\nProperties from WebKitDOMObject:\n  core-object -> gpointer: Core Object\n    The WebCore object the WebKitDOMObject wraps\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType WebKitDOMCDATASection (94252901443536)>'
    __info__ = ObjectInfo(DOMCDATASection)


