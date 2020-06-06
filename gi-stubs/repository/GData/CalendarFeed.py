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


from .Feed import Feed

class CalendarFeed(Feed):
    """
    :Constructors:
    
    ::
    
        CalendarFeed(**properties)
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

    def get_authors(self): # real signature unknown; restored from __doc__
        """ get_authors(self) -> list """
        return []

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> list """
        return []

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_entries(self): # real signature unknown; restored from __doc__
        """ get_entries(self) -> list """
        return []

    def get_etag(self): # real signature unknown; restored from __doc__
        """ get_etag(self) -> str """
        return ""

    def get_generator(self): # real signature unknown; restored from __doc__
        """ get_generator(self) -> GData.Generator """
        pass

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> str """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_items_per_page(self): # real signature unknown; restored from __doc__
        """ get_items_per_page(self) -> int """
        return 0

    def get_json(self): # real signature unknown; restored from __doc__
        """ get_json(self) -> str """
        return ""

    def get_links(self): # real signature unknown; restored from __doc__
        """ get_links(self) -> list """
        return []

    def get_logo(self): # real signature unknown; restored from __doc__
        """ get_logo(self) -> str """
        return ""

    def get_next_page_token(self): # real signature unknown; restored from __doc__
        """ get_next_page_token(self) -> str or None """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rights(self): # real signature unknown; restored from __doc__
        """ get_rights(self) -> str """
        return ""

    def get_start_index(self): # real signature unknown; restored from __doc__
        """ get_start_index(self) -> int """
        return 0

    def get_subtitle(self): # real signature unknown; restored from __doc__
        """ get_subtitle(self) -> str """
        return ""

    def get_times_cleaned(self): # real signature unknown; restored from __doc__
        """ get_times_cleaned(self) -> int """
        return 0

    def get_timezone(self): # real signature unknown; restored from __doc__
        """ get_timezone(self) -> str """
        return ""

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_total_results(self): # real signature unknown; restored from __doc__
        """ get_total_results(self) -> int """
        return 0

    def get_updated(self): # real signature unknown; restored from __doc__
        """ get_updated(self) -> int """
        return 0

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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def look_up_entry(self, id): # real signature unknown; restored from __doc__
        """ look_up_entry(self, id:str) -> GData.Entry """
        pass

    def look_up_link(self, rel): # real signature unknown; restored from __doc__
        """ look_up_link(self, rel:str) -> GData.Link """
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fd5e16e17f0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(CalendarFeed), '__module__': 'gi.repository.GData', '__gtype__': <GType GDataCalendarFeed (94233464347952)>, '__doc__': None, '__gsignals__': {}, 'get_times_cleaned': gi.FunctionInfo(get_times_cleaned), 'get_timezone': gi.FunctionInfo(get_timezone), 'parent': <property object at 0x7fd5e1773ef0>, 'priv': <property object at 0x7fd5e1775040>})"
    __gdoc__ = "Object GDataCalendarFeed\n\nProperties from GDataCalendarFeed:\n  timezone -> gchararray: Timezone\n    The timezone in which the feed's times are given.\n  times-cleaned -> guint: Times cleaned\n    The number of times the feed has been completely cleared of entries.\n\nProperties from GDataFeed:\n  id -> gchararray: ID\n    The unique and permanent URN ID for the feed.\n  etag -> gchararray: ETag\n    The unique ETag for this version of the feed.\n  updated -> gint64: Updated\n    The time the feed was last updated.\n  title -> gchararray: Title\n    The title of the feed.\n  subtitle -> gchararray: Subtitle\n    The subtitle of the feed.\n  logo -> gchararray: Logo\n    The URI of a logo for the feed.\n  icon -> gchararray: Icon\n    The URI of an icon for the feed.\n  generator -> GDataGenerator: Generator\n    Details of the software used to generate the feed.\n  items-per-page -> guint: Items per page\n    The number of items per results page feed.\n  start-index -> guint: Start index\n    The one-based index of the first item in the results feed.\n  total-results -> guint: Total results\n    The total number of results in the feed.\n  rights -> gchararray: Rights\n    The ownership rights pertaining to the entire feed.\n  next-page-token -> gchararray: Next page token\n    The next page token for feeds.\n\nProperties from GDataParsable:\n  constructed-from-xml -> gboolean: Constructed from XML?\n    Specifies whether the object was constructed by parsing XML or manually.\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDataCalendarFeed (94233464347952)>'
    __info__ = ObjectInfo(CalendarFeed)


