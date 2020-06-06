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


from .DOMHTMLElement import DOMHTMLElement

class DOMHTMLOListElement(DOMHTMLElement):
    """
    :Constructors:
    
    ::
    
        DOMHTMLOListElement(**properties)
    """
    def add_event_listener(self, event_name, handler, use_capture): # real signature unknown; restored from __doc__
        """ add_event_listener(self, event_name:str, handler:GObject.Closure, use_capture:bool) -> bool """
        return False

    def append_child(self, newChild): # real signature unknown; restored from __doc__
        """ append_child(self, newChild:WebKit2WebExtension.DOMNode) -> WebKit2WebExtension.DOMNode """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def blur(self): # real signature unknown; restored from __doc__
        """ blur(self) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def click(self): # real signature unknown; restored from __doc__
        """ click(self) """
        pass

    def clone_node(self, deep): # real signature unknown; restored from __doc__
        """ clone_node(self, deep:bool) -> WebKit2WebExtension.DOMNode """
        pass

    def clone_node_with_error(self, deep): # real signature unknown; restored from __doc__
        """ clone_node_with_error(self, deep:bool) -> WebKit2WebExtension.DOMNode """
        pass

    def closest(self, selectors): # real signature unknown; restored from __doc__
        """ closest(self, selectors:str) -> WebKit2WebExtension.DOMElement """
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

    def focus(self): # real signature unknown; restored from __doc__
        """ focus(self) """
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

    def get_access_key(self): # real signature unknown; restored from __doc__
        """ get_access_key(self) -> str """
        return ""

    def get_attribute(self, name): # real signature unknown; restored from __doc__
        """ get_attribute(self, name:str) -> str """
        return ""

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> WebKit2WebExtension.DOMNamedNodeMap """
        pass

    def get_attribute_node(self, name): # real signature unknown; restored from __doc__
        """ get_attribute_node(self, name:str) -> WebKit2WebExtension.DOMAttr """
        pass

    def get_attribute_node_ns(self, namespaceURI, localName): # real signature unknown; restored from __doc__
        """ get_attribute_node_ns(self, namespaceURI:str, localName:str) -> WebKit2WebExtension.DOMAttr """
        pass

    def get_attribute_ns(self, namespaceURI, localName): # real signature unknown; restored from __doc__
        """ get_attribute_ns(self, namespaceURI:str, localName:str) -> str """
        return ""

    def get_base_uri(self): # real signature unknown; restored from __doc__
        """ get_base_uri(self) -> str """
        return ""

    def get_bounding_client_rect(self): # real signature unknown; restored from __doc__
        """ get_bounding_client_rect(self) -> WebKit2WebExtension.DOMClientRect """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_child_element_count(self): # real signature unknown; restored from __doc__
        """ get_child_element_count(self) -> int """
        return 0

    def get_child_nodes(self): # real signature unknown; restored from __doc__
        """ get_child_nodes(self) -> WebKit2WebExtension.DOMNodeList """
        pass

    def get_class_list(self): # real signature unknown; restored from __doc__
        """ get_class_list(self) -> WebKit2WebExtension.DOMDOMTokenList """
        pass

    def get_class_name(self): # real signature unknown; restored from __doc__
        """ get_class_name(self) -> str """
        return ""

    def get_client_height(self): # real signature unknown; restored from __doc__
        """ get_client_height(self) -> float """
        return 0.0

    def get_client_left(self): # real signature unknown; restored from __doc__
        """ get_client_left(self) -> float """
        return 0.0

    def get_client_rects(self): # real signature unknown; restored from __doc__
        """ get_client_rects(self) -> WebKit2WebExtension.DOMClientRectList """
        pass

    def get_client_top(self): # real signature unknown; restored from __doc__
        """ get_client_top(self) -> float """
        return 0.0

    def get_client_width(self): # real signature unknown; restored from __doc__
        """ get_client_width(self) -> float """
        return 0.0

    def get_compact(self): # real signature unknown; restored from __doc__
        """ get_compact(self) -> bool """
        return False

    def get_content_editable(self): # real signature unknown; restored from __doc__
        """ get_content_editable(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_dir(self): # real signature unknown; restored from __doc__
        """ get_dir(self) -> str """
        return ""

    def get_draggable(self): # real signature unknown; restored from __doc__
        """ get_draggable(self) -> bool """
        return False

    def get_elements_by_class_name(self, class_name): # real signature unknown; restored from __doc__
        """ get_elements_by_class_name(self, class_name:str) -> WebKit2WebExtension.DOMNodeList """
        pass

    def get_elements_by_class_name_as_html_collection(self, name): # real signature unknown; restored from __doc__
        """ get_elements_by_class_name_as_html_collection(self, name:str) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_elements_by_tag_name(self, tag_name): # real signature unknown; restored from __doc__
        """ get_elements_by_tag_name(self, tag_name:str) -> WebKit2WebExtension.DOMNodeList """
        pass

    def get_elements_by_tag_name_as_html_collection(self, name): # real signature unknown; restored from __doc__
        """ get_elements_by_tag_name_as_html_collection(self, name:str) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_elements_by_tag_name_ns(self, namespace_uri, tag_name): # real signature unknown; restored from __doc__
        """ get_elements_by_tag_name_ns(self, namespace_uri:str, tag_name:str) -> WebKit2WebExtension.DOMNodeList """
        pass

    def get_elements_by_tag_name_ns_as_html_collection(self, namespaceURI, localName): # real signature unknown; restored from __doc__
        """ get_elements_by_tag_name_ns_as_html_collection(self, namespaceURI:str, localName:str) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_first_child(self): # real signature unknown; restored from __doc__
        """ get_first_child(self) -> WebKit2WebExtension.DOMNode """
        pass

    def get_first_element_child(self): # real signature unknown; restored from __doc__
        """ get_first_element_child(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_hidden(self): # real signature unknown; restored from __doc__
        """ get_hidden(self) -> bool """
        return False

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_inner_html(self): # real signature unknown; restored from __doc__
        """ get_inner_html(self) -> str """
        return ""

    def get_inner_text(self): # real signature unknown; restored from __doc__
        """ get_inner_text(self) -> str """
        return ""

    def get_is_content_editable(self): # real signature unknown; restored from __doc__
        """ get_is_content_editable(self) -> bool """
        return False

    def get_lang(self): # real signature unknown; restored from __doc__
        """ get_lang(self) -> str """
        return ""

    def get_last_child(self): # real signature unknown; restored from __doc__
        """ get_last_child(self) -> WebKit2WebExtension.DOMNode """
        pass

    def get_last_element_child(self): # real signature unknown; restored from __doc__
        """ get_last_element_child(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_local_name(self): # real signature unknown; restored from __doc__
        """ get_local_name(self) -> str """
        return ""

    def get_namespace_uri(self): # real signature unknown; restored from __doc__
        """ get_namespace_uri(self) -> str """
        return ""

    def get_next_element_sibling(self): # real signature unknown; restored from __doc__
        """ get_next_element_sibling(self) -> WebKit2WebExtension.DOMElement """
        pass

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

    def get_offset_height(self): # real signature unknown; restored from __doc__
        """ get_offset_height(self) -> float """
        return 0.0

    def get_offset_left(self): # real signature unknown; restored from __doc__
        """ get_offset_left(self) -> float """
        return 0.0

    def get_offset_parent(self): # real signature unknown; restored from __doc__
        """ get_offset_parent(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_offset_top(self): # real signature unknown; restored from __doc__
        """ get_offset_top(self) -> float """
        return 0.0

    def get_offset_width(self): # real signature unknown; restored from __doc__
        """ get_offset_width(self) -> float """
        return 0.0

    def get_outer_html(self): # real signature unknown; restored from __doc__
        """ get_outer_html(self) -> str """
        return ""

    def get_outer_text(self): # real signature unknown; restored from __doc__
        """ get_outer_text(self) -> str """
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

    def get_previous_element_sibling(self): # real signature unknown; restored from __doc__
        """ get_previous_element_sibling(self) -> WebKit2WebExtension.DOMElement """
        pass

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

    def get_scroll_height(self): # real signature unknown; restored from __doc__
        """ get_scroll_height(self) -> int """
        return 0

    def get_scroll_left(self): # real signature unknown; restored from __doc__
        """ get_scroll_left(self) -> int """
        return 0

    def get_scroll_top(self): # real signature unknown; restored from __doc__
        """ get_scroll_top(self) -> int """
        return 0

    def get_scroll_width(self): # real signature unknown; restored from __doc__
        """ get_scroll_width(self) -> int """
        return 0

    def get_spellcheck(self): # real signature unknown; restored from __doc__
        """ get_spellcheck(self) -> bool """
        return False

    def get_start(self): # real signature unknown; restored from __doc__
        """ get_start(self) -> int """
        return 0

    def get_style(self): # real signature unknown; restored from __doc__
        """ get_style(self) -> WebKit2WebExtension.DOMCSSStyleDeclaration """
        pass

    def get_tab_index(self): # real signature unknown; restored from __doc__
        """ get_tab_index(self) -> int """
        return 0

    def get_tag_name(self): # real signature unknown; restored from __doc__
        """ get_tag_name(self) -> str """
        return ""

    def get_text_content(self): # real signature unknown; restored from __doc__
        """ get_text_content(self) -> str """
        return ""

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_translate(self): # real signature unknown; restored from __doc__
        """ get_translate(self) -> bool """
        return False

    def get_type_attr(self): # real signature unknown; restored from __doc__
        """ get_type_attr(self) -> str """
        return ""

    def get_webkitdropzone(self): # real signature unknown; restored from __doc__
        """ get_webkitdropzone(self) -> str """
        return ""

    def get_webkit_region_overset(self): # real signature unknown; restored from __doc__
        """ get_webkit_region_overset(self) -> str """
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

    def has_attribute(self, name): # real signature unknown; restored from __doc__
        """ has_attribute(self, name:str) -> bool """
        return False

    def has_attributes(self): # real signature unknown; restored from __doc__
        """ has_attributes(self) -> bool """
        return False

    def has_attribute_ns(self, namespaceURI, localName): # real signature unknown; restored from __doc__
        """ has_attribute_ns(self, namespaceURI:str, localName:str) -> bool """
        return False

    def has_child_nodes(self): # real signature unknown; restored from __doc__
        """ has_child_nodes(self) -> bool """
        return False

    def html_input_element_get_auto_filled(self): # real signature unknown; restored from __doc__
        """ html_input_element_get_auto_filled(self) -> bool """
        return False

    def html_input_element_is_user_edited(self): # real signature unknown; restored from __doc__
        """ html_input_element_is_user_edited(self) -> bool """
        return False

    def html_input_element_set_auto_filled(self, auto_filled): # real signature unknown; restored from __doc__
        """ html_input_element_set_auto_filled(self, auto_filled:bool) """
        pass

    def html_input_element_set_editing_value(self, value): # real signature unknown; restored from __doc__
        """ html_input_element_set_editing_value(self, value:str) """
        pass

    def insert_adjacent_element(self, where, element): # real signature unknown; restored from __doc__
        """ insert_adjacent_element(self, where:str, element:WebKit2WebExtension.DOMElement) -> WebKit2WebExtension.DOMElement """
        pass

    def insert_adjacent_html(self, where, html): # real signature unknown; restored from __doc__
        """ insert_adjacent_html(self, where:str, html:str) """
        pass

    def insert_adjacent_text(self, where, text): # real signature unknown; restored from __doc__
        """ insert_adjacent_text(self, where:str, text:str) """
        pass

    def insert_before(self, newChild, refChild=None): # real signature unknown; restored from __doc__
        """ insert_before(self, newChild:WebKit2WebExtension.DOMNode, refChild:WebKit2WebExtension.DOMNode=None) -> WebKit2WebExtension.DOMNode """
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

    def matches(self, selectors): # real signature unknown; restored from __doc__
        """ matches(self, selectors:str) -> bool """
        return False

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

    def query_selector(self, selectors): # real signature unknown; restored from __doc__
        """ query_selector(self, selectors:str) -> WebKit2WebExtension.DOMElement """
        pass

    def query_selector_all(self, selectors): # real signature unknown; restored from __doc__
        """ query_selector_all(self, selectors:str) -> WebKit2WebExtension.DOMNodeList """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove(self): # real signature unknown; restored from __doc__
        """ remove(self) """
        pass

    def remove_attribute(self, name): # real signature unknown; restored from __doc__
        """ remove_attribute(self, name:str) """
        pass

    def remove_attribute_node(self, oldAttr): # real signature unknown; restored from __doc__
        """ remove_attribute_node(self, oldAttr:WebKit2WebExtension.DOMAttr) -> WebKit2WebExtension.DOMAttr """
        pass

    def remove_attribute_ns(self, namespaceURI, localName): # real signature unknown; restored from __doc__
        """ remove_attribute_ns(self, namespaceURI:str, localName:str) """
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

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def request_pointer_lock(self): # real signature unknown; restored from __doc__
        """ request_pointer_lock(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scroll_by_lines(self, lines): # real signature unknown; restored from __doc__
        """ scroll_by_lines(self, lines:int) """
        pass

    def scroll_by_pages(self, pages): # real signature unknown; restored from __doc__
        """ scroll_by_pages(self, pages:int) """
        pass

    def scroll_into_view(self, alignWithTop): # real signature unknown; restored from __doc__
        """ scroll_into_view(self, alignWithTop:bool) """
        pass

    def scroll_into_view_if_needed(self, centerIfNeeded): # real signature unknown; restored from __doc__
        """ scroll_into_view_if_needed(self, centerIfNeeded:bool) """
        pass

    def set_access_key(self, value): # real signature unknown; restored from __doc__
        """ set_access_key(self, value:str) """
        pass

    def set_attribute(self, name, value): # real signature unknown; restored from __doc__
        """ set_attribute(self, name:str, value:str) """
        pass

    def set_attribute_node(self, newAttr): # real signature unknown; restored from __doc__
        """ set_attribute_node(self, newAttr:WebKit2WebExtension.DOMAttr) -> WebKit2WebExtension.DOMAttr """
        pass

    def set_attribute_node_ns(self, newAttr): # real signature unknown; restored from __doc__
        """ set_attribute_node_ns(self, newAttr:WebKit2WebExtension.DOMAttr) -> WebKit2WebExtension.DOMAttr """
        pass

    def set_attribute_ns(self, namespaceURI=None, qualifiedName, value): # real signature unknown; restored from __doc__
        """ set_attribute_ns(self, namespaceURI:str=None, qualifiedName:str, value:str) """
        pass

    def set_class_name(self, value): # real signature unknown; restored from __doc__
        """ set_class_name(self, value:str) """
        pass

    def set_compact(self, value): # real signature unknown; restored from __doc__
        """ set_compact(self, value:bool) """
        pass

    def set_content_editable(self, value): # real signature unknown; restored from __doc__
        """ set_content_editable(self, value:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_dir(self, value): # real signature unknown; restored from __doc__
        """ set_dir(self, value:str) """
        pass

    def set_draggable(self, value): # real signature unknown; restored from __doc__
        """ set_draggable(self, value:bool) """
        pass

    def set_hidden(self, value): # real signature unknown; restored from __doc__
        """ set_hidden(self, value:bool) """
        pass

    def set_id(self, value): # real signature unknown; restored from __doc__
        """ set_id(self, value:str) """
        pass

    def set_inner_html(self, contents): # real signature unknown; restored from __doc__
        """ set_inner_html(self, contents:str) """
        pass

    def set_inner_text(self, value): # real signature unknown; restored from __doc__
        """ set_inner_text(self, value:str) """
        pass

    def set_lang(self, value): # real signature unknown; restored from __doc__
        """ set_lang(self, value:str) """
        pass

    def set_node_value(self, value): # real signature unknown; restored from __doc__
        """ set_node_value(self, value:str) """
        pass

    def set_outer_html(self, contents): # real signature unknown; restored from __doc__
        """ set_outer_html(self, contents:str) """
        pass

    def set_outer_text(self, value): # real signature unknown; restored from __doc__
        """ set_outer_text(self, value:str) """
        pass

    def set_prefix(self, value): # real signature unknown; restored from __doc__
        """ set_prefix(self, value:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_scroll_left(self, value): # real signature unknown; restored from __doc__
        """ set_scroll_left(self, value:int) """
        pass

    def set_scroll_top(self, value): # real signature unknown; restored from __doc__
        """ set_scroll_top(self, value:int) """
        pass

    def set_spellcheck(self, value): # real signature unknown; restored from __doc__
        """ set_spellcheck(self, value:bool) """
        pass

    def set_start(self, value): # real signature unknown; restored from __doc__
        """ set_start(self, value:int) """
        pass

    def set_tab_index(self, value): # real signature unknown; restored from __doc__
        """ set_tab_index(self, value:int) """
        pass

    def set_text_content(self, value): # real signature unknown; restored from __doc__
        """ set_text_content(self, value:str) """
        pass

    def set_title(self, value): # real signature unknown; restored from __doc__
        """ set_title(self, value:str) """
        pass

    def set_translate(self, value): # real signature unknown; restored from __doc__
        """ set_translate(self, value:bool) """
        pass

    def set_type_attr(self, value): # real signature unknown; restored from __doc__
        """ set_type_attr(self, value:str) """
        pass

    def set_webkitdropzone(self, value): # real signature unknown; restored from __doc__
        """ set_webkitdropzone(self, value:str) """
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

    def webkit_matches_selector(self, selectors): # real signature unknown; restored from __doc__
        """ webkit_matches_selector(self, selectors:str) -> bool """
        return False

    def webkit_request_fullscreen(self): # real signature unknown; restored from __doc__
        """ webkit_request_fullscreen(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f17450a6d60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DOMHTMLOListElement), '__module__': 'gi.repository.WebKit2WebExtension', '__gtype__': <GType WebKitDOMHTMLOListElement (94252901510688)>, '__doc__': None, '__gsignals__': {}, 'get_compact': gi.FunctionInfo(get_compact), 'get_start': gi.FunctionInfo(get_start), 'get_type_attr': gi.FunctionInfo(get_type_attr), 'set_compact': gi.FunctionInfo(set_compact), 'set_start': gi.FunctionInfo(set_start), 'set_type_attr': gi.FunctionInfo(set_type_attr), 'parent_instance': <property object at 0x7f1745621400>})"
    __gdoc__ = 'Object WebKitDOMHTMLOListElement\n\nProperties from WebKitDOMHTMLOListElement:\n  compact -> gboolean: HTMLOListElement:compact\n    read-write gboolean HTMLOListElement:compact\n  start -> glong: HTMLOListElement:start\n    read-write glong HTMLOListElement:start\n  type -> gchararray: HTMLOListElement:type\n    read-write gchar* HTMLOListElement:type\n\nProperties from WebKitDOMHTMLElement:\n  title -> gchararray: HTMLElement:title\n    read-write gchar* HTMLElement:title\n  lang -> gchararray: HTMLElement:lang\n    read-write gchar* HTMLElement:lang\n  translate -> gboolean: HTMLElement:translate\n    read-write gboolean HTMLElement:translate\n  dir -> gchararray: HTMLElement:dir\n    read-write gchar* HTMLElement:dir\n  tab-index -> glong: HTMLElement:tab-index\n    read-write glong HTMLElement:tab-index\n  draggable -> gboolean: HTMLElement:draggable\n    read-write gboolean HTMLElement:draggable\n  webkitdropzone -> gchararray: HTMLElement:webkitdropzone\n    read-write gchar* HTMLElement:webkitdropzone\n  hidden -> gboolean: HTMLElement:hidden\n    read-write gboolean HTMLElement:hidden\n  access-key -> gchararray: HTMLElement:access-key\n    read-write gchar* HTMLElement:access-key\n  inner-text -> gchararray: HTMLElement:inner-text\n    read-write gchar* HTMLElement:inner-text\n  outer-text -> gchararray: HTMLElement:outer-text\n    read-write gchar* HTMLElement:outer-text\n  content-editable -> gchararray: HTMLElement:content-editable\n    read-write gchar* HTMLElement:content-editable\n  is-content-editable -> gboolean: HTMLElement:is-content-editable\n    read-only gboolean HTMLElement:is-content-editable\n  spellcheck -> gboolean: HTMLElement:spellcheck\n    read-write gboolean HTMLElement:spellcheck\n\nProperties from WebKitDOMElement:\n  tag-name -> gchararray: Element:tag-name\n    read-only gchar* Element:tag-name\n  attributes -> WebKitDOMNamedNodeMap: Element:attributes\n    read-only WebKitDOMNamedNodeMap* Element:attributes\n  style -> WebKitDOMCSSStyleDeclaration: Element:style\n    read-only WebKitDOMCSSStyleDeclaration* Element:style\n  id -> gchararray: Element:id\n    read-write gchar* Element:id\n  namespace-uri -> gchararray: Element:namespace-uri\n    read-only gchar* Element:namespace-uri\n  prefix -> gchararray: Element:prefix\n    read-only gchar* Element:prefix\n  local-name -> gchararray: Element:local-name\n    read-only gchar* Element:local-name\n  offset-left -> gdouble: Element:offset-left\n    read-only gdouble Element:offset-left\n  offset-top -> gdouble: Element:offset-top\n    read-only gdouble Element:offset-top\n  offset-width -> gdouble: Element:offset-width\n    read-only gdouble Element:offset-width\n  offset-height -> gdouble: Element:offset-height\n    read-only gdouble Element:offset-height\n  client-left -> gdouble: Element:client-left\n    read-only gdouble Element:client-left\n  client-top -> gdouble: Element:client-top\n    read-only gdouble Element:client-top\n  client-width -> gdouble: Element:client-width\n    read-only gdouble Element:client-width\n  client-height -> gdouble: Element:client-height\n    read-only gdouble Element:client-height\n  scroll-left -> glong: Element:scroll-left\n    read-write glong Element:scroll-left\n  scroll-top -> glong: Element:scroll-top\n    read-write glong Element:scroll-top\n  scroll-width -> glong: Element:scroll-width\n    read-only glong Element:scroll-width\n  scroll-height -> glong: Element:scroll-height\n    read-only glong Element:scroll-height\n  offset-parent -> WebKitDOMElement: Element:offset-parent\n    read-only WebKitDOMElement* Element:offset-parent\n  inner-html -> gchararray: Element:inner-html\n    read-write gchar* Element:inner-html\n  outer-html -> gchararray: Element:outer-html\n    read-write gchar* Element:outer-html\n  class-name -> gchararray: Element:class-name\n    read-write gchar* Element:class-name\n  class-list -> WebKitDOMDOMTokenList: Element:class-list\n    read-only WebKitDOMDOMTokenList* Element:class-list\n  webkit-region-overset -> gchararray: Element:webkit-region-overset\n    read-only gchar* Element:webkit-region-overset\n  previous-element-sibling -> WebKitDOMElement: Element:previous-element-sibling\n    read-only WebKitDOMElement* Element:previous-element-sibling\n  next-element-sibling -> WebKitDOMElement: Element:next-element-sibling\n    read-only WebKitDOMElement* Element:next-element-sibling\n  children -> WebKitDOMHTMLCollection: Element:children\n    read-only WebKitDOMHTMLCollection* Element:children\n  first-element-child -> WebKitDOMElement: Element:first-element-child\n    read-only WebKitDOMElement* Element:first-element-child\n  last-element-child -> WebKitDOMElement: Element:last-element-child\n    read-only WebKitDOMElement* Element:last-element-child\n  child-element-count -> gulong: Element:child-element-count\n    read-only gulong Element:child-element-count\n\nProperties from WebKitDOMNode:\n  node-name -> gchararray: Node:node-name\n    read-only gchar* Node:node-name\n  node-value -> gchararray: Node:node-value\n    read-write gchar* Node:node-value\n  node-type -> guint: Node:node-type\n    read-only gushort Node:node-type\n  parent-node -> WebKitDOMNode: Node:parent-node\n    read-only WebKitDOMNode* Node:parent-node\n  child-nodes -> WebKitDOMNodeList: Node:child-nodes\n    read-only WebKitDOMNodeList* Node:child-nodes\n  first-child -> WebKitDOMNode: Node:first-child\n    read-only WebKitDOMNode* Node:first-child\n  last-child -> WebKitDOMNode: Node:last-child\n    read-only WebKitDOMNode* Node:last-child\n  previous-sibling -> WebKitDOMNode: Node:previous-sibling\n    read-only WebKitDOMNode* Node:previous-sibling\n  next-sibling -> WebKitDOMNode: Node:next-sibling\n    read-only WebKitDOMNode* Node:next-sibling\n  owner-document -> WebKitDOMDocument: Node:owner-document\n    read-only WebKitDOMDocument* Node:owner-document\n  base-uri -> gchararray: Node:base-uri\n    read-only gchar* Node:base-uri\n  text-content -> gchararray: Node:text-content\n    read-write gchar* Node:text-content\n  parent-element -> WebKitDOMElement: Node:parent-element\n    read-only WebKitDOMElement* Node:parent-element\n\nProperties from WebKitDOMObject:\n  core-object -> gpointer: Core Object\n    The WebCore object the WebKitDOMObject wraps\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType WebKitDOMHTMLOListElement (94252901510688)>'
    __info__ = ObjectInfo(DOMHTMLOListElement)


