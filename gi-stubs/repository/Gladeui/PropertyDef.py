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


class PropertyDef(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(adaptor:Gladeui.WidgetAdaptor, id:str) -> Gladeui.PropertyDef
        new_from_spec(adaptor:Gladeui.WidgetAdaptor, spec:GObject.ParamSpec) -> Gladeui.PropertyDef
        new_from_spec_full(adaptor:Gladeui.WidgetAdaptor, spec:GObject.ParamSpec, need_handle:bool) -> Gladeui.PropertyDef
    """
    def atk(self): # real signature unknown; restored from __doc__
        """ atk(self) -> bool """
        return False

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> Gladeui.PropertyDef """
        pass

    def common(self): # real signature unknown; restored from __doc__
        """ common(self) -> bool """
        return False

    def compare(self, value1, value2): # real signature unknown; restored from __doc__
        """ compare(self, value1:GObject.Value, value2:GObject.Value) -> int """
        return 0

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def create_type(self): # real signature unknown; restored from __doc__
        """ create_type(self) -> str """
        return ""

    def custom_layout(self): # real signature unknown; restored from __doc__
        """ custom_layout(self) -> bool """
        return False

    def deprecated(self): # real signature unknown; restored from __doc__
        """ deprecated(self) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_adaptor(self): # real signature unknown; restored from __doc__
        """ get_adaptor(self) -> Gladeui.WidgetAdaptor """
        pass

    def get_construct_only(self): # real signature unknown; restored from __doc__
        """ get_construct_only(self) -> bool """
        return False

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default(self) -> GObject.Value """
        pass

    def get_default_from_spec(self, spec): # real signature unknown; restored from __doc__
        """ get_default_from_spec(spec:GObject.ParamSpec) -> GObject.Value """
        pass

    def get_ignore(self): # real signature unknown; restored from __doc__
        """ get_ignore(self) -> bool """
        return False

    def get_is_packing(self): # real signature unknown; restored from __doc__
        """ get_is_packing(self) -> bool """
        return False

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_original_default(self): # real signature unknown; restored from __doc__
        """ get_original_default(self) -> GObject.Value """
        pass

    def get_pspec(self): # real signature unknown; restored from __doc__
        """ get_pspec(self) -> GObject.ParamSpec """
        pass

    def get_tooltip(self): # real signature unknown; restored from __doc__
        """ get_tooltip(self) -> str """
        return ""

    def get_virtual(self): # real signature unknown; restored from __doc__
        """ get_virtual(self) -> bool """
        return False

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> str """
        return ""

    def is_object(self): # real signature unknown; restored from __doc__
        """ is_object(self) -> bool """
        return False

    def is_visible(self): # real signature unknown; restored from __doc__
        """ is_visible(self) -> bool """
        return False

    def load_defaults_from_spec(self): # real signature unknown; restored from __doc__
        """ load_defaults_from_spec(self) """
        pass

    def make_adjustment(self): # real signature unknown; restored from __doc__
        """ make_adjustment(self) -> Gtk.Adjustment """
        pass

    def make_flags_from_string(self, type, string): # real signature unknown; restored from __doc__
        """ make_flags_from_string(type:GType, string:str) -> int """
        return 0

    def make_gvalue_from_string(self, string, project): # real signature unknown; restored from __doc__
        """ make_gvalue_from_string(self, string:str, project:Gladeui.Project) -> GObject.Value """
        pass

    def make_string_from_gvalue(self, value): # real signature unknown; restored from __doc__
        """ make_string_from_gvalue(self, value:GObject.Value) -> str """
        return ""

    def match(self, comp): # real signature unknown; restored from __doc__
        """ match(self, comp:Gladeui.PropertyDef) -> bool """
        return False

    def multiline(self): # real signature unknown; restored from __doc__
        """ multiline(self) -> bool """
        return False

    def needs_sync(self): # real signature unknown; restored from __doc__
        """ needs_sync(self) -> bool """
        return False

    def new(self, adaptor, id): # real signature unknown; restored from __doc__
        """ new(adaptor:Gladeui.WidgetAdaptor, id:str) -> Gladeui.PropertyDef """
        pass

    def new_from_spec(self, adaptor, spec): # real signature unknown; restored from __doc__
        """ new_from_spec(adaptor:Gladeui.WidgetAdaptor, spec:GObject.ParamSpec) -> Gladeui.PropertyDef """
        pass

    def new_from_spec_full(self, adaptor, spec, need_handle): # real signature unknown; restored from __doc__
        """ new_from_spec_full(adaptor:Gladeui.WidgetAdaptor, spec:GObject.ParamSpec, need_handle:bool) -> Gladeui.PropertyDef """
        pass

    def optional(self): # real signature unknown; restored from __doc__
        """ optional(self) -> bool """
        return False

    def optional_default(self): # real signature unknown; restored from __doc__
        """ optional_default(self) -> bool """
        return False

    def parentless_widget(self): # real signature unknown; restored from __doc__
        """ parentless_widget(self) -> bool """
        return False

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> bool """
        return False

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) -> bool """
        return False

    def save_always(self): # real signature unknown; restored from __doc__
        """ save_always(self) -> bool """
        return False

    def set_adaptor(self, adaptor): # real signature unknown; restored from __doc__
        """ set_adaptor(self, adaptor:Gladeui.WidgetAdaptor) """
        pass

    def set_construct_only(self, construct_only): # real signature unknown; restored from __doc__
        """ set_construct_only(self, construct_only:bool) """
        pass

    def set_ignore(self, ignore): # real signature unknown; restored from __doc__
        """ set_ignore(self, ignore:bool) """
        pass

    def set_is_packing(self, is_packing): # real signature unknown; restored from __doc__
        """ set_is_packing(self, is_packing:bool) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_pspec(self, pspec): # real signature unknown; restored from __doc__
        """ set_pspec(self, pspec:GObject.ParamSpec) """
        pass

    def set_tooltip(self, tooltip): # real signature unknown; restored from __doc__
        """ set_tooltip(self, tooltip:str) """
        pass

    def set_virtual(self, value): # real signature unknown; restored from __doc__
        """ set_virtual(self, value:bool) """
        pass

    def set_weights(self, properties, parent): # real signature unknown; restored from __doc__
        """ set_weights(properties:list, parent:GType) """
        pass

    def since_major(self): # real signature unknown; restored from __doc__
        """ since_major(self) -> int """
        return 0

    def since_minor(self): # real signature unknown; restored from __doc__
        """ since_minor(self) -> int """
        return 0

    def stock(self): # real signature unknown; restored from __doc__
        """ stock(self) -> bool """
        return False

    def stock_icon(self): # real signature unknown; restored from __doc__
        """ stock_icon(self) -> bool """
        return False

    def themed_icon(self): # real signature unknown; restored from __doc__
        """ themed_icon(self) -> bool """
        return False

    def transfer_on_paste(self): # real signature unknown; restored from __doc__
        """ transfer_on_paste(self) -> bool """
        return False

    def translatable(self): # real signature unknown; restored from __doc__
        """ translatable(self) -> bool """
        return False

    def update_from_node(self, node, object_type, property_def_ref=None, domain): # real signature unknown; restored from __doc__
        """ update_from_node(node:Gladeui.XmlNode, object_type:GType, property_def_ref:Gladeui.PropertyDef=None, domain:str) -> bool, property_def_ref:Gladeui.PropertyDef """
        return False

    def void_value(self, value): # real signature unknown; restored from __doc__
        """ void_value(self, value:GObject.Value) -> bool """
        return False

    def weight(self): # real signature unknown; restored from __doc__
        """ weight(self) -> float """
        return 0.0

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new(adaptor:Gladeui.WidgetAdaptor, id:str) -> Gladeui.PropertyDef """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PropertyDef), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType GladePropertyDef (94653531119216)>, '__dict__': <attribute '__dict__' of 'PropertyDef' objects>, '__weakref__': <attribute '__weakref__' of 'PropertyDef' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_from_spec': gi.FunctionInfo(new_from_spec), 'new_from_spec_full': gi.FunctionInfo(new_from_spec_full), 'atk': gi.FunctionInfo(atk), 'clone': gi.FunctionInfo(clone), 'common': gi.FunctionInfo(common), 'compare': gi.FunctionInfo(compare), 'create_type': gi.FunctionInfo(create_type), 'custom_layout': gi.FunctionInfo(custom_layout), 'deprecated': gi.FunctionInfo(deprecated), 'free': gi.FunctionInfo(free), 'get_adaptor': gi.FunctionInfo(get_adaptor), 'get_construct_only': gi.FunctionInfo(get_construct_only), 'get_default': gi.FunctionInfo(get_default), 'get_ignore': gi.FunctionInfo(get_ignore), 'get_is_packing': gi.FunctionInfo(get_is_packing), 'get_name': gi.FunctionInfo(get_name), 'get_original_default': gi.FunctionInfo(get_original_default), 'get_pspec': gi.FunctionInfo(get_pspec), 'get_tooltip': gi.FunctionInfo(get_tooltip), 'get_virtual': gi.FunctionInfo(get_virtual), 'id': gi.FunctionInfo(id), 'is_object': gi.FunctionInfo(is_object), 'is_visible': gi.FunctionInfo(is_visible), 'load_defaults_from_spec': gi.FunctionInfo(load_defaults_from_spec), 'make_adjustment': gi.FunctionInfo(make_adjustment), 'make_gvalue_from_string': gi.FunctionInfo(make_gvalue_from_string), 'make_string_from_gvalue': gi.FunctionInfo(make_string_from_gvalue), 'match': gi.FunctionInfo(match), 'multiline': gi.FunctionInfo(multiline), 'needs_sync': gi.FunctionInfo(needs_sync), 'optional': gi.FunctionInfo(optional), 'optional_default': gi.FunctionInfo(optional_default), 'parentless_widget': gi.FunctionInfo(parentless_widget), 'query': gi.FunctionInfo(query), 'save': gi.FunctionInfo(save), 'save_always': gi.FunctionInfo(save_always), 'set_adaptor': gi.FunctionInfo(set_adaptor), 'set_construct_only': gi.FunctionInfo(set_construct_only), 'set_ignore': gi.FunctionInfo(set_ignore), 'set_is_packing': gi.FunctionInfo(set_is_packing), 'set_name': gi.FunctionInfo(set_name), 'set_pspec': gi.FunctionInfo(set_pspec), 'set_tooltip': gi.FunctionInfo(set_tooltip), 'set_virtual': gi.FunctionInfo(set_virtual), 'since_major': gi.FunctionInfo(since_major), 'since_minor': gi.FunctionInfo(since_minor), 'stock': gi.FunctionInfo(stock), 'stock_icon': gi.FunctionInfo(stock_icon), 'themed_icon': gi.FunctionInfo(themed_icon), 'transfer_on_paste': gi.FunctionInfo(transfer_on_paste), 'translatable': gi.FunctionInfo(translatable), 'void_value': gi.FunctionInfo(void_value), 'weight': gi.FunctionInfo(weight), 'get_default_from_spec': gi.FunctionInfo(get_default_from_spec), 'make_flags_from_string': gi.FunctionInfo(make_flags_from_string), 'set_weights': gi.FunctionInfo(set_weights), 'update_from_node': gi.FunctionInfo(update_from_node), '__new__': <staticmethod object at 0x7f1341a4b370>, '__init__': <function nothing at 0x7f1342e6cee0>})"
    __gtype__ = None # (!) real value is '<GType GladePropertyDef (94653531119216)>'
    __info__ = StructInfo(PropertyDef)


