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


from .DOMNode import DOMNode

class DOMDocument(DOMNode):
    """
    :Constructors:
    
    ::
    
        DOMDocument(**properties)
    """
    def add_event_listener(self, event_name, handler, use_capture): # real signature unknown; restored from __doc__
        """ add_event_listener(self, event_name:str, handler:GObject.Closure, use_capture:bool) -> bool """
        return False

    def adopt_node(self, source): # real signature unknown; restored from __doc__
        """ adopt_node(self, source:WebKit2WebExtension.DOMNode) -> WebKit2WebExtension.DOMNode """
        pass

    def append_child(self, newChild): # real signature unknown; restored from __doc__
        """ append_child(self, newChild:WebKit2WebExtension.DOMNode) -> WebKit2WebExtension.DOMNode """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def caret_range_from_point(self, x, y): # real signature unknown; restored from __doc__
        """ caret_range_from_point(self, x:int, y:int) -> WebKit2WebExtension.DOMRange """
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

    def create_attribute(self, name): # real signature unknown; restored from __doc__
        """ create_attribute(self, name:str) -> WebKit2WebExtension.DOMAttr """
        pass

    def create_attribute_ns(self, namespaceURI=None, qualifiedName): # real signature unknown; restored from __doc__
        """ create_attribute_ns(self, namespaceURI:str=None, qualifiedName:str) -> WebKit2WebExtension.DOMAttr """
        pass

    def create_cdata_section(self, data): # real signature unknown; restored from __doc__
        """ create_cdata_section(self, data:str) -> WebKit2WebExtension.DOMCDATASection """
        pass

    def create_comment(self, data): # real signature unknown; restored from __doc__
        """ create_comment(self, data:str) -> WebKit2WebExtension.DOMComment """
        pass

    def create_css_style_declaration(self): # real signature unknown; restored from __doc__
        """ create_css_style_declaration(self) -> WebKit2WebExtension.DOMCSSStyleDeclaration """
        pass

    def create_document_fragment(self): # real signature unknown; restored from __doc__
        """ create_document_fragment(self) -> WebKit2WebExtension.DOMDocumentFragment """
        pass

    def create_element(self, tagName): # real signature unknown; restored from __doc__
        """ create_element(self, tagName:str) -> WebKit2WebExtension.DOMElement """
        pass

    def create_element_ns(self, namespaceURI=None, qualifiedName): # real signature unknown; restored from __doc__
        """ create_element_ns(self, namespaceURI:str=None, qualifiedName:str) -> WebKit2WebExtension.DOMElement """
        pass

    def create_entity_reference(self, name=None): # real signature unknown; restored from __doc__
        """ create_entity_reference(self, name:str=None) -> WebKit2WebExtension.DOMEntityReference """
        pass

    def create_event(self, eventType): # real signature unknown; restored from __doc__
        """ create_event(self, eventType:str) -> WebKit2WebExtension.DOMEvent """
        pass

    def create_expression(self, expression, resolver): # real signature unknown; restored from __doc__
        """ create_expression(self, expression:str, resolver:WebKit2WebExtension.DOMXPathNSResolver) -> WebKit2WebExtension.DOMXPathExpression """
        pass

    def create_node_iterator(self, root, whatToShow, filter=None, expandEntityReferences): # real signature unknown; restored from __doc__
        """ create_node_iterator(self, root:WebKit2WebExtension.DOMNode, whatToShow:int, filter:WebKit2WebExtension.DOMNodeFilter=None, expandEntityReferences:bool) -> WebKit2WebExtension.DOMNodeIterator """
        pass

    def create_ns_resolver(self, nodeResolver): # real signature unknown; restored from __doc__
        """ create_ns_resolver(self, nodeResolver:WebKit2WebExtension.DOMNode) -> WebKit2WebExtension.DOMXPathNSResolver """
        pass

    def create_processing_instruction(self, target, data): # real signature unknown; restored from __doc__
        """ create_processing_instruction(self, target:str, data:str) -> WebKit2WebExtension.DOMProcessingInstruction """
        pass

    def create_range(self): # real signature unknown; restored from __doc__
        """ create_range(self) -> WebKit2WebExtension.DOMRange """
        pass

    def create_text_node(self, data): # real signature unknown; restored from __doc__
        """ create_text_node(self, data:str) -> WebKit2WebExtension.DOMText """
        pass

    def create_tree_walker(self, root, whatToShow, filter=None, expandEntityReferences): # real signature unknown; restored from __doc__
        """ create_tree_walker(self, root:WebKit2WebExtension.DOMNode, whatToShow:int, filter:WebKit2WebExtension.DOMNodeFilter=None, expandEntityReferences:bool) -> WebKit2WebExtension.DOMTreeWalker """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def dispatch_event(self, event): # real signature unknown; restored from __doc__
        """ dispatch_event(self, event:WebKit2WebExtension.DOMEvent) -> bool """
        return False

    def element_from_point(self, x, y): # real signature unknown; restored from __doc__
        """ element_from_point(self, x:int, y:int) -> WebKit2WebExtension.DOMElement """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def evaluate(self, expression, contextNode, resolver=None, type, inResult=None): # real signature unknown; restored from __doc__
        """ evaluate(self, expression:str, contextNode:WebKit2WebExtension.DOMNode, resolver:WebKit2WebExtension.DOMXPathNSResolver=None, type:int, inResult:WebKit2WebExtension.DOMXPathResult=None) -> WebKit2WebExtension.DOMXPathResult """
        pass

    def exec_command(self, command, userInterface, value): # real signature unknown; restored from __doc__
        """ exec_command(self, command:str, userInterface:bool, value:str) -> bool """
        return False

    def exit_pointer_lock(self): # real signature unknown; restored from __doc__
        """ exit_pointer_lock(self) """
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

    def get_active_element(self): # real signature unknown; restored from __doc__
        """ get_active_element(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_anchors(self): # real signature unknown; restored from __doc__
        """ get_anchors(self) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_applets(self): # real signature unknown; restored from __doc__
        """ get_applets(self) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_base_uri(self): # real signature unknown; restored from __doc__
        """ get_base_uri(self) -> str """
        return ""

    def get_body(self): # real signature unknown; restored from __doc__
        """ get_body(self) -> WebKit2WebExtension.DOMHTMLElement """
        pass

    def get_character_set(self): # real signature unknown; restored from __doc__
        """ get_character_set(self) -> str """
        return ""

    def get_charset(self): # real signature unknown; restored from __doc__
        """ get_charset(self) -> str """
        return ""

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_child_element_count(self): # real signature unknown; restored from __doc__
        """ get_child_element_count(self) -> int """
        return 0

    def get_child_nodes(self): # real signature unknown; restored from __doc__
        """ get_child_nodes(self) -> WebKit2WebExtension.DOMNodeList """
        pass

    def get_compat_mode(self): # real signature unknown; restored from __doc__
        """ get_compat_mode(self) -> str """
        return ""

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> str """
        return ""

    def get_cookie(self): # real signature unknown; restored from __doc__
        """ get_cookie(self) -> str """
        return ""

    def get_current_script(self): # real signature unknown; restored from __doc__
        """ get_current_script(self) -> WebKit2WebExtension.DOMHTMLScriptElement """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_charset(self): # real signature unknown; restored from __doc__
        """ get_default_charset(self) -> str """
        return ""

    def get_default_view(self): # real signature unknown; restored from __doc__
        """ get_default_view(self) -> WebKit2WebExtension.DOMDOMWindow """
        pass

    def get_design_mode(self): # real signature unknown; restored from __doc__
        """ get_design_mode(self) -> str """
        return ""

    def get_dir(self): # real signature unknown; restored from __doc__
        """ get_dir(self) -> str """
        return ""

    def get_doctype(self): # real signature unknown; restored from __doc__
        """ get_doctype(self) -> WebKit2WebExtension.DOMDocumentType """
        pass

    def get_document_element(self): # real signature unknown; restored from __doc__
        """ get_document_element(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_document_uri(self): # real signature unknown; restored from __doc__
        """ get_document_uri(self) -> str """
        return ""

    def get_domain(self): # real signature unknown; restored from __doc__
        """ get_domain(self) -> str """
        return ""

    def get_elements_by_class_name(self, class_name): # real signature unknown; restored from __doc__
        """ get_elements_by_class_name(self, class_name:str) -> WebKit2WebExtension.DOMNodeList """
        pass

    def get_elements_by_class_name_as_html_collection(self, classNames): # real signature unknown; restored from __doc__
        """ get_elements_by_class_name_as_html_collection(self, classNames:str) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_elements_by_name(self, elementName): # real signature unknown; restored from __doc__
        """ get_elements_by_name(self, elementName:str) -> WebKit2WebExtension.DOMNodeList """
        pass

    def get_elements_by_tag_name(self, tag_name): # real signature unknown; restored from __doc__
        """ get_elements_by_tag_name(self, tag_name:str) -> WebKit2WebExtension.DOMNodeList """
        pass

    def get_elements_by_tag_name_as_html_collection(self, tagname): # real signature unknown; restored from __doc__
        """ get_elements_by_tag_name_as_html_collection(self, tagname:str) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_elements_by_tag_name_ns(self, namespace_uri, tag_name): # real signature unknown; restored from __doc__
        """ get_elements_by_tag_name_ns(self, namespace_uri:str, tag_name:str) -> WebKit2WebExtension.DOMNodeList """
        pass

    def get_elements_by_tag_name_ns_as_html_collection(self, namespaceURI, localName): # real signature unknown; restored from __doc__
        """ get_elements_by_tag_name_ns_as_html_collection(self, namespaceURI:str, localName:str) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_element_by_id(self, elementId): # real signature unknown; restored from __doc__
        """ get_element_by_id(self, elementId:str) -> WebKit2WebExtension.DOMElement """
        pass

    def get_embeds(self): # real signature unknown; restored from __doc__
        """ get_embeds(self) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_first_child(self): # real signature unknown; restored from __doc__
        """ get_first_child(self) -> WebKit2WebExtension.DOMNode """
        pass

    def get_first_element_child(self): # real signature unknown; restored from __doc__
        """ get_first_element_child(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_forms(self): # real signature unknown; restored from __doc__
        """ get_forms(self) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_head(self): # real signature unknown; restored from __doc__
        """ get_head(self) -> WebKit2WebExtension.DOMHTMLHeadElement """
        pass

    def get_hidden(self): # real signature unknown; restored from __doc__
        """ get_hidden(self) -> bool """
        return False

    def get_images(self): # real signature unknown; restored from __doc__
        """ get_images(self) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_implementation(self): # real signature unknown; restored from __doc__
        """ get_implementation(self) -> WebKit2WebExtension.DOMDOMImplementation """
        pass

    def get_input_encoding(self): # real signature unknown; restored from __doc__
        """ get_input_encoding(self) -> str """
        return ""

    def get_last_child(self): # real signature unknown; restored from __doc__
        """ get_last_child(self) -> WebKit2WebExtension.DOMNode """
        pass

    def get_last_element_child(self): # real signature unknown; restored from __doc__
        """ get_last_element_child(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_last_modified(self): # real signature unknown; restored from __doc__
        """ get_last_modified(self) -> str """
        return ""

    def get_links(self): # real signature unknown; restored from __doc__
        """ get_links(self) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

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

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> str """
        return ""

    def get_override_style(self, element, pseudoElement=None): # real signature unknown; restored from __doc__
        """ get_override_style(self, element:WebKit2WebExtension.DOMElement, pseudoElement:str=None) -> WebKit2WebExtension.DOMCSSStyleDeclaration """
        pass

    def get_owner_document(self): # real signature unknown; restored from __doc__
        """ get_owner_document(self) -> WebKit2WebExtension.DOMDocument """
        pass

    def get_parent_element(self): # real signature unknown; restored from __doc__
        """ get_parent_element(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_parent_node(self): # real signature unknown; restored from __doc__
        """ get_parent_node(self) -> WebKit2WebExtension.DOMNode """
        pass

    def get_plugins(self): # real signature unknown; restored from __doc__
        """ get_plugins(self) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_pointer_lock_element(self): # real signature unknown; restored from __doc__
        """ get_pointer_lock_element(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_preferred_stylesheet_set(self): # real signature unknown; restored from __doc__
        """ get_preferred_stylesheet_set(self) -> str """
        return ""

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

    def get_ready_state(self): # real signature unknown; restored from __doc__
        """ get_ready_state(self) -> str """
        return ""

    def get_referrer(self): # real signature unknown; restored from __doc__
        """ get_referrer(self) -> str """
        return ""

    def get_scripts(self): # real signature unknown; restored from __doc__
        """ get_scripts(self) -> WebKit2WebExtension.DOMHTMLCollection """
        pass

    def get_scrolling_element(self): # real signature unknown; restored from __doc__
        """ get_scrolling_element(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_selected_stylesheet_set(self): # real signature unknown; restored from __doc__
        """ get_selected_stylesheet_set(self) -> str """
        return ""

    def get_style_sheets(self): # real signature unknown; restored from __doc__
        """ get_style_sheets(self) -> WebKit2WebExtension.DOMStyleSheetList """
        pass

    def get_text_content(self): # real signature unknown; restored from __doc__
        """ get_text_content(self) -> str """
        return ""

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_url(self): # real signature unknown; restored from __doc__
        """ get_url(self) -> str """
        return ""

    def get_visibility_state(self): # real signature unknown; restored from __doc__
        """ get_visibility_state(self) -> str """
        return ""

    def get_webkit_current_fullscreen_element(self): # real signature unknown; restored from __doc__
        """ get_webkit_current_fullscreen_element(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_webkit_fullscreen_element(self): # real signature unknown; restored from __doc__
        """ get_webkit_fullscreen_element(self) -> WebKit2WebExtension.DOMElement """
        pass

    def get_webkit_fullscreen_enabled(self): # real signature unknown; restored from __doc__
        """ get_webkit_fullscreen_enabled(self) -> bool """
        return False

    def get_webkit_fullscreen_keyboard_input_allowed(self): # real signature unknown; restored from __doc__
        """ get_webkit_fullscreen_keyboard_input_allowed(self) -> bool """
        return False

    def get_webkit_is_fullscreen(self): # real signature unknown; restored from __doc__
        """ get_webkit_is_fullscreen(self) -> bool """
        return False

    def get_xml_encoding(self): # real signature unknown; restored from __doc__
        """ get_xml_encoding(self) -> str """
        return ""

    def get_xml_standalone(self): # real signature unknown; restored from __doc__
        """ get_xml_standalone(self) -> bool """
        return False

    def get_xml_version(self): # real signature unknown; restored from __doc__
        """ get_xml_version(self) -> str """
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

    def has_focus(self): # real signature unknown; restored from __doc__
        """ has_focus(self) -> bool """
        return False

    def import_node(self, importedNode, deep): # real signature unknown; restored from __doc__
        """ import_node(self, importedNode:WebKit2WebExtension.DOMNode, deep:bool) -> WebKit2WebExtension.DOMNode """
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

    def query_command_enabled(self, command): # real signature unknown; restored from __doc__
        """ query_command_enabled(self, command:str) -> bool """
        return False

    def query_command_indeterm(self, command): # real signature unknown; restored from __doc__
        """ query_command_indeterm(self, command:str) -> bool """
        return False

    def query_command_state(self, command): # real signature unknown; restored from __doc__
        """ query_command_state(self, command:str) -> bool """
        return False

    def query_command_supported(self, command): # real signature unknown; restored from __doc__
        """ query_command_supported(self, command:str) -> bool """
        return False

    def query_command_value(self, command): # real signature unknown; restored from __doc__
        """ query_command_value(self, command:str) -> str """
        return ""

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

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_body(self, value): # real signature unknown; restored from __doc__
        """ set_body(self, value:WebKit2WebExtension.DOMHTMLElement) """
        pass

    def set_charset(self, value): # real signature unknown; restored from __doc__
        """ set_charset(self, value:str) """
        pass

    def set_cookie(self, value): # real signature unknown; restored from __doc__
        """ set_cookie(self, value:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_design_mode(self, value): # real signature unknown; restored from __doc__
        """ set_design_mode(self, value:str) """
        pass

    def set_dir(self, value): # real signature unknown; restored from __doc__
        """ set_dir(self, value:str) """
        pass

    def set_document_uri(self, value): # real signature unknown; restored from __doc__
        """ set_document_uri(self, value:str) """
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

    def set_selected_stylesheet_set(self, value): # real signature unknown; restored from __doc__
        """ set_selected_stylesheet_set(self, value:str) """
        pass

    def set_text_content(self, value): # real signature unknown; restored from __doc__
        """ set_text_content(self, value:str) """
        pass

    def set_title(self, value): # real signature unknown; restored from __doc__
        """ set_title(self, value:str) """
        pass

    def set_xml_standalone(self, value): # real signature unknown; restored from __doc__
        """ set_xml_standalone(self, value:bool) """
        pass

    def set_xml_version(self, value): # real signature unknown; restored from __doc__
        """ set_xml_version(self, value:str) """
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

    def webkit_cancel_fullscreen(self): # real signature unknown; restored from __doc__
        """ webkit_cancel_fullscreen(self) """
        pass

    def webkit_exit_fullscreen(self): # real signature unknown; restored from __doc__
        """ webkit_exit_fullscreen(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1745601370>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DOMDocument), '__module__': 'gi.repository.WebKit2WebExtension', '__gtype__': <GType WebKitDOMDocument (94252901487728)>, '__doc__': None, '__gsignals__': {}, 'adopt_node': gi.FunctionInfo(adopt_node), 'caret_range_from_point': gi.FunctionInfo(caret_range_from_point), 'create_attribute': gi.FunctionInfo(create_attribute), 'create_attribute_ns': gi.FunctionInfo(create_attribute_ns), 'create_cdata_section': gi.FunctionInfo(create_cdata_section), 'create_comment': gi.FunctionInfo(create_comment), 'create_css_style_declaration': gi.FunctionInfo(create_css_style_declaration), 'create_document_fragment': gi.FunctionInfo(create_document_fragment), 'create_element': gi.FunctionInfo(create_element), 'create_element_ns': gi.FunctionInfo(create_element_ns), 'create_entity_reference': gi.FunctionInfo(create_entity_reference), 'create_event': gi.FunctionInfo(create_event), 'create_expression': gi.FunctionInfo(create_expression), 'create_node_iterator': gi.FunctionInfo(create_node_iterator), 'create_ns_resolver': gi.FunctionInfo(create_ns_resolver), 'create_processing_instruction': gi.FunctionInfo(create_processing_instruction), 'create_range': gi.FunctionInfo(create_range), 'create_text_node': gi.FunctionInfo(create_text_node), 'create_tree_walker': gi.FunctionInfo(create_tree_walker), 'element_from_point': gi.FunctionInfo(element_from_point), 'evaluate': gi.FunctionInfo(evaluate), 'exec_command': gi.FunctionInfo(exec_command), 'exit_pointer_lock': gi.FunctionInfo(exit_pointer_lock), 'get_active_element': gi.FunctionInfo(get_active_element), 'get_anchors': gi.FunctionInfo(get_anchors), 'get_applets': gi.FunctionInfo(get_applets), 'get_body': gi.FunctionInfo(get_body), 'get_character_set': gi.FunctionInfo(get_character_set), 'get_charset': gi.FunctionInfo(get_charset), 'get_child_element_count': gi.FunctionInfo(get_child_element_count), 'get_children': gi.FunctionInfo(get_children), 'get_compat_mode': gi.FunctionInfo(get_compat_mode), 'get_content_type': gi.FunctionInfo(get_content_type), 'get_cookie': gi.FunctionInfo(get_cookie), 'get_current_script': gi.FunctionInfo(get_current_script), 'get_default_charset': gi.FunctionInfo(get_default_charset), 'get_default_view': gi.FunctionInfo(get_default_view), 'get_design_mode': gi.FunctionInfo(get_design_mode), 'get_dir': gi.FunctionInfo(get_dir), 'get_doctype': gi.FunctionInfo(get_doctype), 'get_document_element': gi.FunctionInfo(get_document_element), 'get_document_uri': gi.FunctionInfo(get_document_uri), 'get_domain': gi.FunctionInfo(get_domain), 'get_element_by_id': gi.FunctionInfo(get_element_by_id), 'get_elements_by_class_name': gi.FunctionInfo(get_elements_by_class_name), 'get_elements_by_class_name_as_html_collection': gi.FunctionInfo(get_elements_by_class_name_as_html_collection), 'get_elements_by_name': gi.FunctionInfo(get_elements_by_name), 'get_elements_by_tag_name': gi.FunctionInfo(get_elements_by_tag_name), 'get_elements_by_tag_name_as_html_collection': gi.FunctionInfo(get_elements_by_tag_name_as_html_collection), 'get_elements_by_tag_name_ns': gi.FunctionInfo(get_elements_by_tag_name_ns), 'get_elements_by_tag_name_ns_as_html_collection': gi.FunctionInfo(get_elements_by_tag_name_ns_as_html_collection), 'get_embeds': gi.FunctionInfo(get_embeds), 'get_first_element_child': gi.FunctionInfo(get_first_element_child), 'get_forms': gi.FunctionInfo(get_forms), 'get_head': gi.FunctionInfo(get_head), 'get_hidden': gi.FunctionInfo(get_hidden), 'get_images': gi.FunctionInfo(get_images), 'get_implementation': gi.FunctionInfo(get_implementation), 'get_input_encoding': gi.FunctionInfo(get_input_encoding), 'get_last_element_child': gi.FunctionInfo(get_last_element_child), 'get_last_modified': gi.FunctionInfo(get_last_modified), 'get_links': gi.FunctionInfo(get_links), 'get_origin': gi.FunctionInfo(get_origin), 'get_override_style': gi.FunctionInfo(get_override_style), 'get_plugins': gi.FunctionInfo(get_plugins), 'get_pointer_lock_element': gi.FunctionInfo(get_pointer_lock_element), 'get_preferred_stylesheet_set': gi.FunctionInfo(get_preferred_stylesheet_set), 'get_ready_state': gi.FunctionInfo(get_ready_state), 'get_referrer': gi.FunctionInfo(get_referrer), 'get_scripts': gi.FunctionInfo(get_scripts), 'get_scrolling_element': gi.FunctionInfo(get_scrolling_element), 'get_selected_stylesheet_set': gi.FunctionInfo(get_selected_stylesheet_set), 'get_style_sheets': gi.FunctionInfo(get_style_sheets), 'get_title': gi.FunctionInfo(get_title), 'get_url': gi.FunctionInfo(get_url), 'get_visibility_state': gi.FunctionInfo(get_visibility_state), 'get_webkit_current_fullscreen_element': gi.FunctionInfo(get_webkit_current_fullscreen_element), 'get_webkit_fullscreen_element': gi.FunctionInfo(get_webkit_fullscreen_element), 'get_webkit_fullscreen_enabled': gi.FunctionInfo(get_webkit_fullscreen_enabled), 'get_webkit_fullscreen_keyboard_input_allowed': gi.FunctionInfo(get_webkit_fullscreen_keyboard_input_allowed), 'get_webkit_is_fullscreen': gi.FunctionInfo(get_webkit_is_fullscreen), 'get_xml_encoding': gi.FunctionInfo(get_xml_encoding), 'get_xml_standalone': gi.FunctionInfo(get_xml_standalone), 'get_xml_version': gi.FunctionInfo(get_xml_version), 'has_focus': gi.FunctionInfo(has_focus), 'import_node': gi.FunctionInfo(import_node), 'query_command_enabled': gi.FunctionInfo(query_command_enabled), 'query_command_indeterm': gi.FunctionInfo(query_command_indeterm), 'query_command_state': gi.FunctionInfo(query_command_state), 'query_command_supported': gi.FunctionInfo(query_command_supported), 'query_command_value': gi.FunctionInfo(query_command_value), 'query_selector': gi.FunctionInfo(query_selector), 'query_selector_all': gi.FunctionInfo(query_selector_all), 'set_body': gi.FunctionInfo(set_body), 'set_charset': gi.FunctionInfo(set_charset), 'set_cookie': gi.FunctionInfo(set_cookie), 'set_design_mode': gi.FunctionInfo(set_design_mode), 'set_dir': gi.FunctionInfo(set_dir), 'set_document_uri': gi.FunctionInfo(set_document_uri), 'set_selected_stylesheet_set': gi.FunctionInfo(set_selected_stylesheet_set), 'set_title': gi.FunctionInfo(set_title), 'set_xml_standalone': gi.FunctionInfo(set_xml_standalone), 'set_xml_version': gi.FunctionInfo(set_xml_version), 'webkit_cancel_fullscreen': gi.FunctionInfo(webkit_cancel_fullscreen), 'webkit_exit_fullscreen': gi.FunctionInfo(webkit_exit_fullscreen), 'parent_instance': <property object at 0x7f174d0b56d0>})"
    __gdoc__ = 'Object WebKitDOMDocument\n\nProperties from WebKitDOMDocument:\n  doctype -> WebKitDOMDocumentType: Document:doctype\n    read-only WebKitDOMDocumentType* Document:doctype\n  implementation -> WebKitDOMDOMImplementation: Document:implementation\n    read-only WebKitDOMDOMImplementation* Document:implementation\n  document-element -> WebKitDOMElement: Document:document-element\n    read-only WebKitDOMElement* Document:document-element\n  input-encoding -> gchararray: Document:input-encoding\n    read-only gchar* Document:input-encoding\n  xml-encoding -> gchararray: Document:xml-encoding\n    read-only gchar* Document:xml-encoding\n  xml-version -> gchararray: Document:xml-version\n    read-write gchar* Document:xml-version\n  xml-standalone -> gboolean: Document:xml-standalone\n    read-write gboolean Document:xml-standalone\n  document-uri -> gchararray: Document:document-uri\n    read-write gchar* Document:document-uri\n  default-view -> WebKitDOMDOMWindow: Document:default-view\n    read-only WebKitDOMDOMWindow* Document:default-view\n  style-sheets -> WebKitDOMStyleSheetList: Document:style-sheets\n    read-only WebKitDOMStyleSheetList* Document:style-sheets\n  content-type -> gchararray: Document:content-type\n    read-only gchar* Document:content-type\n  title -> gchararray: Document:title\n    read-write gchar* Document:title\n  dir -> gchararray: Document:dir\n    read-write gchar* Document:dir\n  design-mode -> gchararray: Document:design-mode\n    read-write gchar* Document:design-mode\n  referrer -> gchararray: Document:referrer\n    read-only gchar* Document:referrer\n  domain -> gchararray: Document:domain\n    read-only gchar* Document:domain\n  url -> gchararray: Document:url\n    read-only gchar* Document:url\n  cookie -> gchararray: Document:cookie\n    read-write gchar* Document:cookie\n  body -> WebKitDOMHTMLElement: Document:body\n    read-only WebKitDOMHTMLElement* Document:body\n  head -> WebKitDOMHTMLHeadElement: Document:head\n    read-only WebKitDOMHTMLHeadElement* Document:head\n  images -> WebKitDOMHTMLCollection: Document:images\n    read-only WebKitDOMHTMLCollection* Document:images\n  applets -> WebKitDOMHTMLCollection: Document:applets\n    read-only WebKitDOMHTMLCollection* Document:applets\n  links -> WebKitDOMHTMLCollection: Document:links\n    read-only WebKitDOMHTMLCollection* Document:links\n  forms -> WebKitDOMHTMLCollection: Document:forms\n    read-only WebKitDOMHTMLCollection* Document:forms\n  anchors -> WebKitDOMHTMLCollection: Document:anchors\n    read-only WebKitDOMHTMLCollection* Document:anchors\n  embeds -> WebKitDOMHTMLCollection: Document:embeds\n    read-only WebKitDOMHTMLCollection* Document:embeds\n  plugins -> WebKitDOMHTMLCollection: Document:plugins\n    read-only WebKitDOMHTMLCollection* Document:plugins\n  scripts -> WebKitDOMHTMLCollection: Document:scripts\n    read-only WebKitDOMHTMLCollection* Document:scripts\n  last-modified -> gchararray: Document:last-modified\n    read-only gchar* Document:last-modified\n  charset -> gchararray: Document:charset\n    read-write gchar* Document:charset\n  ready-state -> gchararray: Document:ready-state\n    read-only gchar* Document:ready-state\n  character-set -> gchararray: Document:character-set\n    read-only gchar* Document:character-set\n  preferred-stylesheet-set -> gchararray: Document:preferred-stylesheet-set\n    read-only gchar* Document:preferred-stylesheet-set\n  selected-stylesheet-set -> gchararray: Document:selected-stylesheet-set\n    read-write gchar* Document:selected-stylesheet-set\n  active-element -> WebKitDOMElement: Document:active-element\n    read-only WebKitDOMElement* Document:active-element\n  compat-mode -> gchararray: Document:compat-mode\n    read-only gchar* Document:compat-mode\n  webkit-is-full-screen -> gboolean: Document:webkit-is-full-screen\n    read-only gboolean Document:webkit-is-full-screen\n  webkit-full-screen-keyboard-input-allowed -> gboolean: Document:webkit-full-screen-keyboard-input-allowed\n    read-only gboolean Document:webkit-full-screen-keyboard-input-allowed\n  webkit-current-full-screen-element -> WebKitDOMElement: Document:webkit-current-full-screen-element\n    read-only WebKitDOMElement* Document:webkit-current-full-screen-element\n  webkit-fullscreen-enabled -> gboolean: Document:webkit-fullscreen-enabled\n    read-only gboolean Document:webkit-fullscreen-enabled\n  webkit-fullscreen-element -> WebKitDOMElement: Document:webkit-fullscreen-element\n    read-only WebKitDOMElement* Document:webkit-fullscreen-element\n  pointer-lock-element -> WebKitDOMElement: Document:pointer-lock-element\n    read-only WebKitDOMElement* Document:pointer-lock-element\n  visibility-state -> gchararray: Document:visibility-state\n    read-only gchar* Document:visibility-state\n  hidden -> gboolean: Document:hidden\n    read-only gboolean Document:hidden\n  current-script -> WebKitDOMHTMLScriptElement: Document:current-script\n    read-only WebKitDOMHTMLScriptElement* Document:current-script\n  origin -> gchararray: Document:origin\n    read-only gchar* Document:origin\n  scrolling-element -> WebKitDOMElement: Document:scrolling-element\n    read-only WebKitDOMElement* Document:scrolling-element\n  children -> WebKitDOMHTMLCollection: Document:children\n    read-only WebKitDOMHTMLCollection* Document:children\n  first-element-child -> WebKitDOMElement: Document:first-element-child\n    read-only WebKitDOMElement* Document:first-element-child\n  last-element-child -> WebKitDOMElement: Document:last-element-child\n    read-only WebKitDOMElement* Document:last-element-child\n  child-element-count -> gulong: Document:child-element-count\n    read-only gulong Document:child-element-count\n\nProperties from WebKitDOMNode:\n  node-name -> gchararray: Node:node-name\n    read-only gchar* Node:node-name\n  node-value -> gchararray: Node:node-value\n    read-write gchar* Node:node-value\n  node-type -> guint: Node:node-type\n    read-only gushort Node:node-type\n  parent-node -> WebKitDOMNode: Node:parent-node\n    read-only WebKitDOMNode* Node:parent-node\n  child-nodes -> WebKitDOMNodeList: Node:child-nodes\n    read-only WebKitDOMNodeList* Node:child-nodes\n  first-child -> WebKitDOMNode: Node:first-child\n    read-only WebKitDOMNode* Node:first-child\n  last-child -> WebKitDOMNode: Node:last-child\n    read-only WebKitDOMNode* Node:last-child\n  previous-sibling -> WebKitDOMNode: Node:previous-sibling\n    read-only WebKitDOMNode* Node:previous-sibling\n  next-sibling -> WebKitDOMNode: Node:next-sibling\n    read-only WebKitDOMNode* Node:next-sibling\n  owner-document -> WebKitDOMDocument: Node:owner-document\n    read-only WebKitDOMDocument* Node:owner-document\n  base-uri -> gchararray: Node:base-uri\n    read-only gchar* Node:base-uri\n  text-content -> gchararray: Node:text-content\n    read-write gchar* Node:text-content\n  parent-element -> WebKitDOMElement: Node:parent-element\n    read-only WebKitDOMElement* Node:parent-element\n\nProperties from WebKitDOMObject:\n  core-object -> gpointer: Core Object\n    The WebCore object the WebKitDOMObject wraps\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType WebKitDOMDocument (94252901487728)>'
    __info__ = ObjectInfo(DOMDocument)


