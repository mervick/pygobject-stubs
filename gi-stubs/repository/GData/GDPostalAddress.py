# encoding: utf-8
# module gi.repository.GData
# from /usr/lib64/girepository-1.0/GData-0.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .Parsable import Parsable

from .Comparable import Comparable

class GDPostalAddress(Parsable, Comparable):
    """
    :Constructors:
    
    ::
    
        GDPostalAddress(**properties)
        new(relation_type:str=None, label:str=None, is_primary:bool) -> GData.GDPostalAddress
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compare(self, other=None): # real signature unknown; restored from __doc__
        """ compare(self, other:GData.Comparable=None) -> int """
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_get_json(self, *args, **kwargs): # real signature unknown
        """ get_json(self, builder:Json.Builder) """
        pass

    def do_get_namespaces(self, *args, **kwargs): # real signature unknown
        """ get_namespaces(self, namespaces:dict) """
        pass

    def do_get_xml(self, *args, **kwargs): # real signature unknown
        """ get_xml(self, xml_string:GLib.String) """
        pass

    def do_parse_json(self, *args, **kwargs): # real signature unknown
        """ parse_json(self, reader:Json.Reader, user_data=None) -> bool """
        pass

    def do_parse_xml(self, *args, **kwargs): # real signature unknown
        """ parse_xml(self, doc:libxml2.Doc, node:libxml2.Node, user_data=None) -> bool """
        pass

    def do_post_parse_json(self, *args, **kwargs): # real signature unknown
        """ post_parse_json(self, user_data=None) -> bool """
        pass

    def do_post_parse_xml(self, *args, **kwargs): # real signature unknown
        """ post_parse_xml(self, user_data=None) -> bool """
        pass

    def do_pre_get_xml(self, *args, **kwargs): # real signature unknown
        """ pre_get_xml(self, xml_string:GLib.String) """
        pass

    def do_pre_parse_xml(self, *args, **kwargs): # real signature unknown
        """ pre_parse_xml(self, doc:libxml2.Doc, root_node:libxml2.Node, user_data=None) -> bool """
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

    def get_address(self): # real signature unknown; restored from __doc__
        """ get_address(self) -> str """
        return ""

    def get_agent(self): # real signature unknown; restored from __doc__
        """ get_agent(self) -> str """
        return ""

    def get_city(self): # real signature unknown; restored from __doc__
        """ get_city(self) -> str """
        return ""

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> str """
        return ""

    def get_country(self): # real signature unknown; restored from __doc__
        """ get_country(self) -> str """
        return ""

    def get_country_code(self): # real signature unknown; restored from __doc__
        """ get_country_code(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_house_name(self): # real signature unknown; restored from __doc__
        """ get_house_name(self) -> str """
        return ""

    def get_json(self): # real signature unknown; restored from __doc__
        """ get_json(self) -> str """
        return ""

    def get_label(self): # real signature unknown; restored from __doc__
        """ get_label(self) -> str """
        return ""

    def get_mail_class(self): # real signature unknown; restored from __doc__
        """ get_mail_class(self) -> str """
        return ""

    def get_neighborhood(self): # real signature unknown; restored from __doc__
        """ get_neighborhood(self) -> str """
        return ""

    def get_postcode(self): # real signature unknown; restored from __doc__
        """ get_postcode(self) -> str """
        return ""

    def get_po_box(self): # real signature unknown; restored from __doc__
        """ get_po_box(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_region(self): # real signature unknown; restored from __doc__
        """ get_region(self) -> str """
        return ""

    def get_relation_type(self): # real signature unknown; restored from __doc__
        """ get_relation_type(self) -> str """
        return ""

    def get_street(self): # real signature unknown; restored from __doc__
        """ get_street(self) -> str """
        return ""

    def get_subregion(self): # real signature unknown; restored from __doc__
        """ get_subregion(self) -> str """
        return ""

    def get_usage(self): # real signature unknown; restored from __doc__
        """ get_usage(self) -> str """
        return ""

    def get_xml(self): # real signature unknown; restored from __doc__
        """ get_xml(self) -> str """
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

    def is_primary(self): # real signature unknown; restored from __doc__
        """ is_primary(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, relation_type=None, label=None, is_primary): # real signature unknown; restored from __doc__
        """ new(relation_type:str=None, label:str=None, is_primary:bool) -> GData.GDPostalAddress """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_json(self, parsable_type, json, length): # real signature unknown; restored from __doc__
        """ new_from_json(parsable_type:GType, json:str, length:int) -> GData.Parsable """
        pass

    def new_from_xml(self, parsable_type, xml, length): # real signature unknown; restored from __doc__
        """ new_from_xml(parsable_type:GType, xml:str, length:int) -> GData.Parsable """
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

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_address(self, address=None): # real signature unknown; restored from __doc__
        """ set_address(self, address:str=None) """
        pass

    def set_agent(self, agent=None): # real signature unknown; restored from __doc__
        """ set_agent(self, agent:str=None) """
        pass

    def set_city(self, city=None): # real signature unknown; restored from __doc__
        """ set_city(self, city:str=None) """
        pass

    def set_country(self, country=None, country_code=None): # real signature unknown; restored from __doc__
        """ set_country(self, country:str=None, country_code:str=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_house_name(self, house_name=None): # real signature unknown; restored from __doc__
        """ set_house_name(self, house_name:str=None) """
        pass

    def set_is_primary(self, is_primary): # real signature unknown; restored from __doc__
        """ set_is_primary(self, is_primary:bool) """
        pass

    def set_label(self, label=None): # real signature unknown; restored from __doc__
        """ set_label(self, label:str=None) """
        pass

    def set_mail_class(self, mail_class=None): # real signature unknown; restored from __doc__
        """ set_mail_class(self, mail_class:str=None) """
        pass

    def set_neighborhood(self, neighborhood=None): # real signature unknown; restored from __doc__
        """ set_neighborhood(self, neighborhood:str=None) """
        pass

    def set_postcode(self, postcode=None): # real signature unknown; restored from __doc__
        """ set_postcode(self, postcode:str=None) """
        pass

    def set_po_box(self, po_box=None): # real signature unknown; restored from __doc__
        """ set_po_box(self, po_box:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_region(self, region=None): # real signature unknown; restored from __doc__
        """ set_region(self, region:str=None) """
        pass

    def set_relation_type(self, relation_type=None): # real signature unknown; restored from __doc__
        """ set_relation_type(self, relation_type:str=None) """
        pass

    def set_street(self, street=None): # real signature unknown; restored from __doc__
        """ set_street(self, street:str=None) """
        pass

    def set_subregion(self, subregion=None): # real signature unknown; restored from __doc__
        """ set_subregion(self, subregion:str=None) """
        pass

    def set_usage(self, usage=None): # real signature unknown; restored from __doc__
        """ set_usage(self, usage:str=None) """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fd5e1377c40>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(GDPostalAddress), '__module__': 'gi.repository.GData', '__gtype__': <GType GDataGDPostalAddress (94233464465280)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_address': gi.FunctionInfo(get_address), 'get_agent': gi.FunctionInfo(get_agent), 'get_city': gi.FunctionInfo(get_city), 'get_country': gi.FunctionInfo(get_country), 'get_country_code': gi.FunctionInfo(get_country_code), 'get_house_name': gi.FunctionInfo(get_house_name), 'get_label': gi.FunctionInfo(get_label), 'get_mail_class': gi.FunctionInfo(get_mail_class), 'get_neighborhood': gi.FunctionInfo(get_neighborhood), 'get_po_box': gi.FunctionInfo(get_po_box), 'get_postcode': gi.FunctionInfo(get_postcode), 'get_region': gi.FunctionInfo(get_region), 'get_relation_type': gi.FunctionInfo(get_relation_type), 'get_street': gi.FunctionInfo(get_street), 'get_subregion': gi.FunctionInfo(get_subregion), 'get_usage': gi.FunctionInfo(get_usage), 'is_primary': gi.FunctionInfo(is_primary), 'set_address': gi.FunctionInfo(set_address), 'set_agent': gi.FunctionInfo(set_agent), 'set_city': gi.FunctionInfo(set_city), 'set_country': gi.FunctionInfo(set_country), 'set_house_name': gi.FunctionInfo(set_house_name), 'set_is_primary': gi.FunctionInfo(set_is_primary), 'set_label': gi.FunctionInfo(set_label), 'set_mail_class': gi.FunctionInfo(set_mail_class), 'set_neighborhood': gi.FunctionInfo(set_neighborhood), 'set_po_box': gi.FunctionInfo(set_po_box), 'set_postcode': gi.FunctionInfo(set_postcode), 'set_region': gi.FunctionInfo(set_region), 'set_relation_type': gi.FunctionInfo(set_relation_type), 'set_street': gi.FunctionInfo(set_street), 'set_subregion': gi.FunctionInfo(set_subregion), 'set_usage': gi.FunctionInfo(set_usage), 'parent': <property object at 0x7fd5e1742040>, 'priv': <property object at 0x7fd5e1742130>})"
    __gdoc__ = 'Object GDataGDPostalAddress\n\nProperties from GDataGDPostalAddress:\n  address -> gchararray: Address\n    The postal address itself.\n  relation-type -> gchararray: Relation type\n    A programmatic value that identifies the type of postal address.\n  label -> gchararray: Label\n    A simple string value used to name this postal address.\n  is-primary -> gboolean: Primary?\n    Indicates which postal address out of a group is primary.\n  mail-class -> gchararray: Mail class\n    Classes of mail accepted at this address.\n  usage -> gchararray: Usage\n    The context in which this addess can be used.\n  agent -> gchararray: Agent\n    The agent who actually receives the mail.\n  house-name -> gchararray: House name\n    Used in places where houses or buildings have names (and not numbers).\n  street -> gchararray: Street\n    Can be street, avenue, road, etc.\n  po-box -> gchararray: PO box\n    Covers actual P.O. boxes, drawers, locked bags, etc.\n  neighborhood -> gchararray: Neighborhood\n    This is used to disambiguate a street address.\n  city -> gchararray: City\n    Can be city, village, town, borough, etc.\n  subregion -> gchararray: Subregion\n    Handles administrative districts such as U.S. or U.K. counties.\n  region -> gchararray: Region\n    A state, province, county, Land, departement, etc.\n  postcode -> gchararray: Postcode\n    Postal code.\n  country -> gchararray: Country\n    The name of the country.\n  country-code -> gchararray: Country code\n    The ISO 3166-1 alpha-2 country code for the country.\n\nProperties from GDataParsable:\n  constructed-from-xml -> gboolean: Constructed from XML?\n    Specifies whether the object was constructed by parsing XML or manually.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDataGDPostalAddress (94233464465280)>'
    __info__ = ObjectInfo(GDPostalAddress)


