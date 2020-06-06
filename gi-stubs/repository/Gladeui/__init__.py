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


# Variables with simple values

DEVHELP_FALLBACK_ICON_FILE = 'devhelp.png'

DEVHELP_ICON_NAME = 'devhelp'

ENV_BUNDLED = 'GLADE_BUNDLED'

ENV_CATALOG_PATH = 'GLADE_CATALOG_SEARCH_PATH'

ENV_ICON_THEME_PATH = 'GLADE_ICON_THEME_PATH'

ENV_MODULE_PATH = 'GLADE_MODULE_SEARCH_PATH'

ENV_PIXMAP_DIR = 'GLADE_PIXMAP_DIR'

ENV_TESTING = 'GLADE_TESTING'

GTKBUILDER_VERSIONING_BASE_MAJOR = 2
GTKBUILDER_VERSIONING_BASE_MINOR = 14

PROPERTY_DEF_OBJECT_DELIMITER = ', '

TAG_ACTION = 'action'
TAG_ACTIONS = 'actions'

TAG_ACTION_ACTIVATE_FUNCTION = 'action-activate-function'

TAG_ACTION_SUBMENU_FUNCTION = 'action-submenu-function'

TAG_ADAPTOR = 'adaptor'

TAG_ADD_CHILD_FUNCTION = 'add-child-function'

TAG_ADD_CHILD_VERIFY_FUNCTION = 'add-child-verify-function'

TAG_ANARCHIST = 'anarchist'

TAG_ATK_PROPERTY = 'atk-property'

TAG_BIND_FLAGS = 'bind-flags'
TAG_BIND_PROPERTY = 'bind-property'
TAG_BIND_SOURCE = 'bind-source'

TAG_BOOK = 'book'

TAG_BUILDER_SINCE = 'gtkbuilder-since'

TAG_CHILD_ACTION_ACTIVATE_FUNCTION = 'child-action-activate-function'

TAG_CHILD_GET_PROP_FUNCTION = 'child-get-property-function'

TAG_CHILD_PROPERTY = 'child-property'

TAG_CHILD_SET_PROP_FUNCTION = 'child-set-property-function'

TAG_CHILD_VERIFY_FUNCTION = 'child-verify-function'

TAG_COMMENT = 'comments'
TAG_COMMON = 'common'

TAG_CONSTRUCTOR_FUNCTION = 'constructor-function'

TAG_CONSTRUCT_OBJECT_FUNCTION = 'construct-object-function'

TAG_CONSTRUCT_ONLY = 'construct-only'

TAG_CONTEXT = 'context'

TAG_CREATE_EDITABLE_FUNCTION = 'create-editable-function'

TAG_CREATE_EPROP_FUNCTION = 'create-editor-property-function'

TAG_CREATE_TYPE = 'create-type'

TAG_CREATE_WIDGET_FUNCTION = 'create-widget-function'

TAG_CUSTOM_LAYOUT = 'custom-layout'

TAG_DEEP_POST_CREATE_FUNCTION = 'deep-post-create-function'

TAG_DEFAULT = 'default'

TAG_DEFAULT_HEIGHT = 'default-height'

TAG_DEFAULT_PALETTE_STATE = 'default-palette-state'

TAG_DEFAULT_WIDTH = 'default-width'

TAG_DEPENDS = 'depends'

TAG_DEPENDS_FUNCTION = 'depends-function'

TAG_DEPRECATED = 'deprecated'

TAG_DEPRECATED_SINCE = 'deprecated-since'

TAG_DESTROY_OBJECT_FUNCTION = 'destroy-object-function'

TAG_DISABLED = 'disabled'

TAG_DISPLAYABLE_VALUES = 'displayable-values'

TAG_DOMAIN = 'domain'
TAG_EDITABLE = 'editable'

TAG_EVENT_HANDLER_CONNECTED = 'EventHandlerConnected'

TAG_EXPANDED = 'expanded'
TAG_FALSE = 'False'

TAG_GENERIC_NAME = 'generic-name'

TAG_GET_CHILDREN_FUNCTION = 'get-children-function'

TAG_GET_FUNCTION = 'get-property-function'

TAG_GET_INTERNAL_CHILD_FUNCTION = 'get-internal-child-function'

TAG_GET_TYPE_FUNCTION = 'get-type-function'

TAG_GLADE_CATALOG = 'glade-catalog'

TAG_GLADE_WIDGET_CLASS = 'glade-widget-class'
TAG_GLADE_WIDGET_CLASSES = 'glade-widget-classes'

TAG_GLADE_WIDGET_CLASS_REF = 'glade-widget-class-ref'

TAG_GLADE_WIDGET_GROUP = 'glade-widget-group'

TAG_HAS_CONTEXT = 'context'

TAG_ICON_NAME = 'icon-name'
TAG_ICON_PREFIX = 'icon-prefix'

TAG_ID = 'id'
TAG_IGNORE = 'ignore'
TAG_IMPORTANT = 'important'

TAG_INIT_FUNCTION = 'init-function'

TAG_INTERNAL_CHILDREN = 'internal-children'

TAG_KEY = 'key'
TAG_LIBRARY = 'library'

TAG_MAX_VALUE = 'max'

TAG_MIN_VALUE = 'min'

TAG_MULTILINE = 'multiline'
TAG_NAME = 'name'

TAG_NEEDS_SYNC = 'needs-sync'

TAG_NICK = 'nick'
TAG_NO = 'No'
TAG_OPTIONAL = 'optional'

TAG_OPTIONAL_DEFAULT = 'optional-default'

TAG_PACKING_ACTIONS = 'packing-actions'
TAG_PACKING_DEFAULTS = 'packing-defaults'
TAG_PACKING_PROPERTIES = 'packing-properties'

TAG_PARENT = 'parent'

TAG_PARENTLESS_WIDGET = 'parentless-widget'

TAG_PARENT_CLASS = 'parent-class'

TAG_POST_CREATE_FUNCTION = 'post-create-function'

TAG_PROPERTIES = 'properties'
TAG_PROPERTY = 'property'
TAG_QUERY = 'query'

TAG_READ_CHILD_FUNCTION = 'read-child-function'

TAG_READ_WIDGET_FUNCTION = 'read-widget-function'

TAG_REMOVE_CHILD_FUNCTION = 'remove-child-function'

TAG_REPLACE_CHILD_FUNCTION = 'replace-child-function'

TAG_RESOURCE = 'resource'
TAG_SAVE = 'save'

TAG_SAVE_ALWAYS = 'save-always'

TAG_SET_FUNCTION = 'set-property-function'

TAG_SIGNAL = 'signal'
TAG_SIGNALS = 'signals'
TAG_SPEC = 'spec'

TAG_SPECIAL_CHILD_TYPE = 'special-child-type'

TAG_SPECIFICATIONS = 'parameter-spec'
TAG_STOCK = 'stock'

TAG_STOCK_ICON = 'stock-icon'

TAG_STRING_FROM_VALUE_FUNCTION = 'string-from-value-function'

TAG_TARGETABLE = 'targetable'

TAG_TEMPLATE_PREFIX = 'template-prefix'

TAG_THEMED_ICON = 'themed-icon'

TAG_TITLE = 'title'
TAG_TOOLTIP = 'tooltip'
TAG_TOPLEVEL = 'toplevel'

TAG_TRANSFER_ON_PASTE = 'transfer-on-paste'

TAG_TRANSLATABLE = 'translatable'
TAG_TRUE = 'True'
TAG_TYPE = 'type'

TAG_USE_PLACEHOLDERS = 'use-placeholders'

TAG_VALUE = 'value'

TAG_VALUE_TYPE = 'value-type'

TAG_VERIFY_FUNCTION = 'verify-function'

TAG_VERSION = 'version'

TAG_VERSION_SINCE = 'since'

TAG_VISIBLE = 'visible'
TAG_WEIGHT = 'weight'

TAG_WRITE_CHILD_FUNCTION = 'write-child-function'

TAG_WRITE_WIDGET_AFTER_FUNCTION = 'write-widget-after-function'

TAG_WRITE_WIDGET_FUNCTION = 'write-widget-function'

TAG_YES = 'Yes'

UNNAMED_PREFIX = '__glade_unnamed_'

WIDGET_ADAPTOR_INSTANTIABLE_PREFIX = 'GladeInstantiable'

XML_TAG_AFTER = 'after'
XML_TAG_CHILD = 'child'
XML_TAG_CLASS = 'class'
XML_TAG_FILENAME = 'filename'
XML_TAG_HANDLER = 'handler'

XML_TAG_I18N_TRUE = 'yes'

XML_TAG_ID = 'id'

XML_TAG_INTERNAL_CHILD = 'internal-child'

XML_TAG_LIB = 'lib'
XML_TAG_NAME = 'name'
XML_TAG_OBJECT = 'object'
XML_TAG_PACKING = 'packing'
XML_TAG_PLACEHOLDER = 'placeholder'
XML_TAG_PROJECT = 'interface'
XML_TAG_PROPERTY = 'property'
XML_TAG_REQUIRES = 'requires'
XML_TAG_SIGNAL = 'signal'

XML_TAG_SIGNAL_FALSE = 'no'
XML_TAG_SIGNAL_TRUE = 'yes'

XML_TAG_SOURCE = 'source'
XML_TAG_SOURCES = 'sources'

XML_TAG_STOCK_ID = 'stock-id'

XML_TAG_SWAPPED = 'swapped'
XML_TAG_TEMPLATE = 'template'
XML_TAG_TYPE = 'type'

XML_TAG_TYPE_FUNC = 'type-func'

XML_TAG_VERSION = 'version'
XML_TAG_WIDGET = 'object'

_namespace = 'Gladeui'

_version = '2.0'

__weakref__ = None

# functions

def catalog_add_path(path): # real signature unknown; restored from __doc__
    """ catalog_add_path(path:str) """
    pass

def catalog_destroy_all(): # real signature unknown; restored from __doc__
    """ catalog_destroy_all() """
    pass

def catalog_get_extra_paths(): # real signature unknown; restored from __doc__
    """ catalog_get_extra_paths() -> list """
    return []

def catalog_is_loaded(name): # real signature unknown; restored from __doc__
    """ catalog_is_loaded(name:str) -> bool """
    return False

def catalog_load_all(): # real signature unknown; restored from __doc__
    """ catalog_load_all() -> list """
    return []

def catalog_remove_path(path=None): # real signature unknown; restored from __doc__
    """ catalog_remove_path(path:str=None) """
    pass

def cursor_get_add_widget_pixbuf(): # real signature unknown; restored from __doc__
    """ cursor_get_add_widget_pixbuf() -> GdkPixbuf.Pixbuf """
    pass

def cursor_init(): # real signature unknown; restored from __doc__
    """ cursor_init() """
    pass

def cursor_set(project, window, type): # real signature unknown; restored from __doc__
    """ cursor_set(project:Gladeui.Project, window:Gdk.Window, type:Gladeui.CursorType) """
    pass

def displayable_value_is_disabled(type, value): # real signature unknown; restored from __doc__
    """ displayable_value_is_disabled(type:GType, value:str) -> bool """
    return False

def displayable_value_set_disabled(type, value, disabled): # real signature unknown; restored from __doc__
    """ displayable_value_set_disabled(type:GType, value:str, disabled:bool) """
    pass

def get_debug_flags(): # real signature unknown; restored from __doc__
    """ get_debug_flags() -> int """
    return 0

def get_displayable_value(type, value): # real signature unknown; restored from __doc__
    """ get_displayable_value(type:GType, value:str) -> str """
    return ""

def get_value_from_displayable(type, displayabe): # real signature unknown; restored from __doc__
    """ get_value_from_displayable(type:GType, displayabe:str) -> str """
    return ""

def init(): # real signature unknown; restored from __doc__
    """ init() """
    pass

def init_debug_flags(): # real signature unknown; restored from __doc__
    """ init_debug_flags() """
    pass

def param_spec_objects(name, nick, blurb, accepted_type, flags): # real signature unknown; restored from __doc__
    """ param_spec_objects(name:str, nick:str, blurb:str, accepted_type:GType, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def property_def_get_default_from_spec(spec): # real signature unknown; restored from __doc__
    """ property_def_get_default_from_spec(spec:GObject.ParamSpec) -> GObject.Value """
    pass

def property_def_make_flags_from_string(type, string): # real signature unknown; restored from __doc__
    """ property_def_make_flags_from_string(type:GType, string:str) -> int """
    return 0

def property_def_set_weights(properties, parent): # real signature unknown; restored from __doc__
    """ property_def_set_weights(properties:list, parent:GType) """
    pass

def property_def_update_from_node(node, object_type, property_def_ref=None, domain): # real signature unknown; restored from __doc__
    """ property_def_update_from_node(node:Gladeui.XmlNode, object_type:GType, property_def_ref:Gladeui.PropertyDef=None, domain:str) -> bool, property_def_ref:Gladeui.PropertyDef """
    return False

def propert_get_insensitive_tooltip(property): # real signature unknown; restored from __doc__
    """ propert_get_insensitive_tooltip(property:Gladeui.Property) -> str """
    return ""

def register_displayable_value(type, value, domain, string): # real signature unknown; restored from __doc__
    """ register_displayable_value(type:GType, value:str, domain:str, string:str) """
    pass

def register_translated_value(type, value, string): # real signature unknown; restored from __doc__
    """ register_translated_value(type:GType, value:str, string:str) """
    pass

def setup_log_handlers(): # real signature unknown; restored from __doc__
    """ setup_log_handlers() """
    pass

def standard_boolean_spec(): # real signature unknown; restored from __doc__
    """ standard_boolean_spec() -> GObject.ParamSpec """
    pass

def standard_float_spec(): # real signature unknown; restored from __doc__
    """ standard_float_spec() -> GObject.ParamSpec """
    pass

def standard_gdkcolor_spec(): # real signature unknown; restored from __doc__
    """ standard_gdkcolor_spec() -> GObject.ParamSpec """
    pass

def standard_int_spec(): # real signature unknown; restored from __doc__
    """ standard_int_spec() -> GObject.ParamSpec """
    pass

def standard_objects_spec(): # real signature unknown; restored from __doc__
    """ standard_objects_spec() -> GObject.ParamSpec """
    pass

def standard_pixbuf_spec(): # real signature unknown; restored from __doc__
    """ standard_pixbuf_spec() -> GObject.ParamSpec """
    pass

def standard_stock_append_prefix(prefix): # real signature unknown; restored from __doc__
    """ standard_stock_append_prefix(prefix:str) """
    pass

def standard_stock_image_spec(): # real signature unknown; restored from __doc__
    """ standard_stock_image_spec() -> GObject.ParamSpec """
    pass

def standard_stock_spec(): # real signature unknown; restored from __doc__
    """ standard_stock_spec() -> GObject.ParamSpec """
    pass

def standard_string_spec(): # real signature unknown; restored from __doc__
    """ standard_string_spec() -> GObject.ParamSpec """
    pass

def standard_strv_spec(): # real signature unknown; restored from __doc__
    """ standard_strv_spec() -> GObject.ParamSpec """
    pass

def standard_uint_spec(): # real signature unknown; restored from __doc__
    """ standard_uint_spec() -> GObject.ParamSpec """
    pass

def type_has_displayable_values(type): # real signature unknown; restored from __doc__
    """ type_has_displayable_values(type:GType) -> bool """
    return False

def utils_boolean_from_string(string): # real signature unknown; restored from __doc__
    """ utils_boolean_from_string(string:str) -> bool, value:bool """
    return False

def utils_cairo_draw_line(cr, color, x1, y1, x2, y2): # real signature unknown; restored from __doc__
    """ utils_cairo_draw_line(cr:cairo.Context, color:Gdk.Color, x1:int, y1:int, x2:int, y2:int) """
    pass

def utils_cairo_draw_rectangle(cr, color, filled, x, y, width, height): # real signature unknown; restored from __doc__
    """ utils_cairo_draw_rectangle(cr:cairo.Context, color:Gdk.Color, filled:bool, x:int, y:int, width:int, height:int) """
    pass

def utils_enum_string_from_value(enum_type, value): # real signature unknown; restored from __doc__
    """ utils_enum_string_from_value(enum_type:GType, value:int) -> str """
    return ""

def utils_enum_string_from_value_displayable(flags_type, value): # real signature unknown; restored from __doc__
    """ utils_enum_string_from_value_displayable(flags_type:GType, value:int) -> str """
    return ""

def utils_enum_value_from_string(enum_type, strval): # real signature unknown; restored from __doc__
    """ utils_enum_value_from_string(enum_type:GType, strval:str) -> int """
    return 0

def utils_flags_string_from_value(enum_type, value): # real signature unknown; restored from __doc__
    """ utils_flags_string_from_value(enum_type:GType, value:int) -> str """
    return ""

def utils_flags_string_from_value_displayable(flags_type, value): # real signature unknown; restored from __doc__
    """ utils_flags_string_from_value_displayable(flags_type:GType, value:int) -> str """
    return ""

def utils_flags_value_from_string(enum_type, strval): # real signature unknown; restored from __doc__
    """ utils_flags_value_from_string(enum_type:GType, strval:str) -> int """
    return 0

def utils_get_pointer(widget, window, device, x, y): # real signature unknown; restored from __doc__
    """ utils_get_pointer(widget:Gtk.Widget, window:Gdk.Window, device:Gdk.Device, x:int, y:int) """
    pass

def utils_get_pspec_from_funcname(funcname): # real signature unknown; restored from __doc__
    """ utils_get_pspec_from_funcname(funcname:str) -> GObject.ParamSpec or None """
    pass

def utils_hijack_key_press(win, event, user_data=None): # real signature unknown; restored from __doc__
    """ utils_hijack_key_press(win:Gtk.Window, event:Gdk.EventKey, user_data=None) -> int """
    return 0

def utils_liststore_from_enum_type(enum_type, include_empty): # real signature unknown; restored from __doc__
    """ utils_liststore_from_enum_type(enum_type:GType, include_empty:bool) -> Gtk.ListStore """
    pass

def utils_pointer_mode_render_icon(mode, size): # real signature unknown; restored from __doc__
    """ utils_pointer_mode_render_icon(mode:Gladeui.PointerMode, size:Gtk.IconSize) -> GdkPixbuf.Pixbuf """
    pass

def utils_replace_home_dir_with_tilde(path): # real signature unknown; restored from __doc__
    """ utils_replace_home_dir_with_tilde(path:str) -> str """
    return ""

def utils_string_from_value(value): # real signature unknown; restored from __doc__
    """ utils_string_from_value(value:GObject.Value) -> str """
    return ""

def utils_value_from_string(type, string, project): # real signature unknown; restored from __doc__
    """ utils_value_from_string(type:GType, string:str, project:Gladeui.Project) -> GObject.Value """
    pass

def util_canonical_path(path): # real signature unknown; restored from __doc__
    """ util_canonical_path(path:str) -> str """
    return ""

def util_check_and_warn_scrollable(parent, child_adaptor, parent_widget): # real signature unknown; restored from __doc__
    """ util_check_and_warn_scrollable(parent:Gladeui.Widget, child_adaptor:Gladeui.WidgetAdaptor, parent_widget:Gtk.Widget) -> bool """
    return False

def util_compare_stock_labels(a=None, b=None): # real signature unknown; restored from __doc__
    """ util_compare_stock_labels(a=None, b=None) -> int """
    return 0

def util_container_get_all_children(container): # real signature unknown; restored from __doc__
    """ util_container_get_all_children(container:Gtk.Container) -> list """
    return []

def util_count_placeholders(parent): # real signature unknown; restored from __doc__
    """ util_count_placeholders(parent:Gladeui.Widget) -> int """
    return 0

def util_duplicate_underscores(name): # real signature unknown; restored from __doc__
    """ util_duplicate_underscores(name:str) -> str """
    return ""

def util_filename_to_icon_name(value): # real signature unknown; restored from __doc__
    """ util_filename_to_icon_name(value:str) -> str """
    return ""

def util_file_dialog_new(title, project, parent, action): # real signature unknown; restored from __doc__
    """ util_file_dialog_new(title:str, project:Gladeui.Project, parent:Gtk.Window, action:Gladeui.UtilFileDialogType) -> Gtk.Widget """
    pass

def util_file_is_writeable(path): # real signature unknown; restored from __doc__
    """ util_file_is_writeable(path:str) -> bool """
    return False

def util_find_iter_by_widget(model, findme, column): # real signature unknown; restored from __doc__
    """ util_find_iter_by_widget(model:Gtk.TreeModel, findme:Gladeui.Widget, column:int) -> Gtk.TreeIter """
    pass

def util_get_devhelp_icon(size): # real signature unknown; restored from __doc__
    """ util_get_devhelp_icon(size:Gtk.IconSize) -> Gtk.Widget """
    pass

def util_get_file_mtime(filename): # real signature unknown; restored from __doc__
    """ util_get_file_mtime(filename:str) -> int """
    return 0

def util_get_placeholder_from_pointer(container): # real signature unknown; restored from __doc__
    """ util_get_placeholder_from_pointer(container:Gtk.Container) -> Gtk.Widget """
    pass

def util_get_type_from_name(name, have_func): # real signature unknown; restored from __doc__
    """ util_get_type_from_name(name:str, have_func:bool) -> GType """
    pass

def util_have_devhelp(): # real signature unknown; restored from __doc__
    """ util_have_devhelp() -> bool """
    return False

def util_icon_name_to_filename(value): # real signature unknown; restored from __doc__
    """ util_icon_name_to_filename(value:str) -> str """
    return ""

def util_object_is_loading(p_object): # real signature unknown; restored from __doc__
    """ util_object_is_loading(object:GObject.Object) -> bool """
    return False

def util_read_prop_name(p_str): # real signature unknown; restored from __doc__
    """ util_read_prop_name(str:str) -> str """
    return ""

def util_remove_scroll_events(widget): # real signature unknown; restored from __doc__
    """ util_remove_scroll_events(widget:Gtk.Widget) """
    pass

def util_replace(p_str, a, b): # real signature unknown; restored from __doc__
    """ util_replace(str:str, a:int, b:int) """
    pass

def util_search_devhelp(book, page, search): # real signature unknown; restored from __doc__
    """ util_search_devhelp(book:str, page:str, search:str) """
    pass

def util_url_show(url): # real signature unknown; restored from __doc__
    """ util_url_show(url:str) -> bool """
    return False

def xml_dump_from_context(context): # real signature unknown; restored from __doc__
    """ xml_dump_from_context(context:Gladeui.XmlContext) -> str """
    return ""

def xml_get_boolean(node, name, _default): # real signature unknown; restored from __doc__
    """ xml_get_boolean(node:Gladeui.XmlNode, name:str, _default:bool) -> bool """
    return False

def xml_get_content(node_in): # real signature unknown; restored from __doc__
    """ xml_get_content(node_in:Gladeui.XmlNode) -> str """
    return ""

def xml_get_property_boolean(node_in, name, _default): # real signature unknown; restored from __doc__
    """ xml_get_property_boolean(node_in:Gladeui.XmlNode, name:str, _default:bool) -> bool """
    return False

def xml_get_property_double(node_in, name, _default): # real signature unknown; restored from __doc__
    """ xml_get_property_double(node_in:Gladeui.XmlNode, name:str, _default:float) -> float """
    return 0.0

def xml_get_property_int(node_in, name, _default): # real signature unknown; restored from __doc__
    """ xml_get_property_int(node_in:Gladeui.XmlNode, name:str, _default:int) -> int """
    return 0

def xml_get_property_string(node_in, name): # real signature unknown; restored from __doc__
    """ xml_get_property_string(node_in:Gladeui.XmlNode, name:str) -> str """
    return ""

def xml_get_property_string_required(node_in, name, xtra): # real signature unknown; restored from __doc__
    """ xml_get_property_string_required(node_in:Gladeui.XmlNode, name:str, xtra:str) -> str """
    return ""

def xml_get_property_targetable_versions(node_in, name): # real signature unknown; restored from __doc__
    """ xml_get_property_targetable_versions(node_in:Gladeui.XmlNode, name:str) -> list """
    return []

def xml_get_property_version(node_in, name, major, minor): # real signature unknown; restored from __doc__
    """ xml_get_property_version(node_in:Gladeui.XmlNode, name:str, major:int, minor:int) -> bool """
    return False

def xml_get_value_int(node_in, name, val): # real signature unknown; restored from __doc__
    """ xml_get_value_int(node_in:Gladeui.XmlNode, name:str, val:int) -> bool """
    return False

def xml_get_value_int_required(node, name, val): # real signature unknown; restored from __doc__
    """ xml_get_value_int_required(node:Gladeui.XmlNode, name:str, val:int) -> bool """
    return False

def xml_get_value_string(node, name): # real signature unknown; restored from __doc__
    """ xml_get_value_string(node:Gladeui.XmlNode, name:str) -> str """
    return ""

def xml_get_value_string_required(node, name, xtra_info): # real signature unknown; restored from __doc__
    """ xml_get_value_string_required(node:Gladeui.XmlNode, name:str, xtra_info:str) -> str """
    return ""

def xml_load_sym_from_node(node_in, module, tagname, sym_location=None): # real signature unknown; restored from __doc__
    """ xml_load_sym_from_node(node_in:Gladeui.XmlNode, module:GModule.Module, tagname:str, sym_location=None) -> bool """
    return False

def xml_search_child(node, name): # real signature unknown; restored from __doc__
    """ xml_search_child(node:Gladeui.XmlNode, name:str) -> Gladeui.XmlNode """
    pass

def xml_search_child_required(tree, name): # real signature unknown; restored from __doc__
    """ xml_search_child_required(tree:Gladeui.XmlNode, name:str) -> Gladeui.XmlNode or None """
    pass

def xml_set_content(node_in, content): # real signature unknown; restored from __doc__
    """ xml_set_content(node_in:Gladeui.XmlNode, content:str) """
    pass

def xml_set_value(node_in, name, val): # real signature unknown; restored from __doc__
    """ xml_set_value(node_in:Gladeui.XmlNode, name:str, val:str) """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .AdaptorChooser import AdaptorChooser
from .AdaptorChooserClass import AdaptorChooserClass
from .App import App
from .AppClass import AppClass
from .BaseEditor import BaseEditor
from .BaseEditorClass import BaseEditorClass
from .Catalog import Catalog
from .CellRendererIcon import CellRendererIcon
from .CellRendererIconClass import CellRendererIconClass
from .Clipboard import Clipboard
from .ClipboardClass import ClipboardClass
from .Command import Command
from .CommandClass import CommandClass
from .CommandSetPropData import CommandSetPropData
from .CreateReason import CreateReason
from .Cursor import Cursor
from .CursorType import CursorType
from .DebugFlag import DebugFlag
from .DesignView import DesignView
from .DesignViewClass import DesignViewClass
from .Editable import Editable
from .EditableInterface import EditableInterface
from .Editor import Editor
from .EditorClass import EditorClass
from .EditorPageType import EditorPageType
from .EditorProperty import EditorProperty
from .EditorPropertyClass import EditorPropertyClass
from .EditorSkeleton import EditorSkeleton
from .EditorSkeletonClass import EditorSkeletonClass
from .EditorTable import EditorTable
from .EditorTableClass import EditorTableClass
from .EPropBool import EPropBool
from .EPropCheck import EPropCheck
from .EPropColor import EPropColor
from .EPropEnum import EPropEnum
from .EPropFlags import EPropFlags
from .EPropNamedIcon import EPropNamedIcon
from .EPropNumeric import EPropNumeric
from .EPropObject import EPropObject
from .EPropObjects import EPropObjects
from .EPropText import EPropText
from .EPropUnichar import EPropUnichar
from .GList import GList
from .IDAllocator import IDAllocator
from .Inspector import Inspector
from .InspectorClass import InspectorClass
from .ItemAppearance import ItemAppearance
from .NameContext import NameContext
from .NamedIconChooserDialog import NamedIconChooserDialog
from .NamedIconChooserDialogClass import NamedIconChooserDialogClass
from .Palette import Palette
from .PaletteClass import PaletteClass
from .PalettePrivate import PalettePrivate
from .ParamObjects import ParamObjects
from .ParamSpecObjects import ParamSpecObjects
from .Placeholder import Placeholder
from .PlaceholderClass import PlaceholderClass
from .PlaceholderPrivate import PlaceholderPrivate
from .PointerMode import PointerMode
from .Project import Project
from .ProjectClass import ProjectClass
from .ProjectModelColumns import ProjectModelColumns
from .ProjectPrivate import ProjectPrivate
from .Property import Property
from .PropertyClass import PropertyClass
from .PropertyDef import PropertyDef
from .PropertyLabel import PropertyLabel
from .PropertyLabelClass import PropertyLabelClass
from .PropertyLabelPrivate import PropertyLabelPrivate
from .PropertyPrivate import PropertyPrivate
from .PropertyShell import PropertyShell
from .PropertyShellClass import PropertyShellClass
from .PropertyShellPrivate import PropertyShellPrivate
from .PropertyState import PropertyState
from .Signal import Signal
from .SignalClass import SignalClass
from .SignalDef import SignalDef
from .SignalEditor import SignalEditor
from .SignalEditorClass import SignalEditorClass
from .SignalModel import SignalModel
from .SignalModelClass import SignalModelClass
from .SignalModelColumns import SignalModelColumns
from .SignalModelPrivate import SignalModelPrivate
from .SignalPrivate import SignalPrivate
from .Stock import Stock
from .StockImage import StockImage
from .SupportMask import SupportMask
from .TargetableVersion import TargetableVersion
from .UIMessageType import UIMessageType
from .UtilFileDialogType import UtilFileDialogType
from .VerifyFlags import VerifyFlags
from .Widget import Widget
from .WidgetAction import WidgetAction
from .WidgetActionClass import WidgetActionClass
from .WidgetActionDef import WidgetActionDef
from .WidgetActionPrivate import WidgetActionPrivate
from .WidgetAdaptor import WidgetAdaptor
from .WidgetAdaptorClass import WidgetAdaptorClass
from .WidgetClass import WidgetClass
from .WidgetGroup import WidgetGroup
from .WidgetPrivate import WidgetPrivate
from .XmlContext import XmlContext
from .XmlDoc import XmlDoc
from .XmlNode import XmlNode
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f1343aaad00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Gladeui-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gladeui', loader=<gi.importer.DynamicImporter object at 0x7f1343aaad00>)"

