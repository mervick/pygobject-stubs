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


from .Query import Query

class YouTubeQuery(Query):
    """
    :Constructors:
    
    ::
    
        YouTubeQuery(**properties)
        new(q:str=None) -> GData.YouTubeQuery
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

    def do_get_query_uri(self, *args, **kwargs): # real signature unknown
        """ get_query_uri(self, feed_uri:str, query_uri:GLib.String, params_started:bool) """
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

    def get_age(self): # real signature unknown; restored from __doc__
        """ get_age(self) -> GData.YouTubeAge """
        pass

    def get_author(self): # real signature unknown; restored from __doc__
        """ get_author(self) -> str """
        return ""

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_etag(self): # real signature unknown; restored from __doc__
        """ get_etag(self) -> str """
        return ""

    def get_format(self): # real signature unknown; restored from __doc__
        """ get_format(self) -> GData.YouTubeFormat """
        pass

    def get_language(self): # real signature unknown; restored from __doc__
        """ get_language(self) -> str """
        return ""

    def get_license(self): # real signature unknown; restored from __doc__
        """ get_license(self) -> str """
        return ""

    def get_location(self): # real signature unknown; restored from __doc__
        """ get_location(self) -> latitude:float, longitude:float, radius:float, has_location:bool """
        pass

    def get_max_results(self): # real signature unknown; restored from __doc__
        """ get_max_results(self) -> int """
        return 0

    def get_order_by(self): # real signature unknown; restored from __doc__
        """ get_order_by(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_published_max(self): # real signature unknown; restored from __doc__
        """ get_published_max(self) -> int """
        return 0

    def get_published_min(self): # real signature unknown; restored from __doc__
        """ get_published_min(self) -> int """
        return 0

    def get_q(self): # real signature unknown; restored from __doc__
        """ get_q(self) -> str """
        return ""

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_query_uri(self, feed_uri): # real signature unknown; restored from __doc__
        """ get_query_uri(self, feed_uri:str) -> str """
        return ""

    def get_restriction(self): # real signature unknown; restored from __doc__
        """ get_restriction(self) -> str """
        return ""

    def get_safe_search(self): # real signature unknown; restored from __doc__
        """ get_safe_search(self) -> GData.YouTubeSafeSearch """
        pass

    def get_sort_order(self): # real signature unknown; restored from __doc__
        """ get_sort_order(self) -> GData.YouTubeSortOrder """
        pass

    def get_start_index(self): # real signature unknown; restored from __doc__
        """ get_start_index(self) -> int """
        return 0

    def get_updated_max(self): # real signature unknown; restored from __doc__
        """ get_updated_max(self) -> int """
        return 0

    def get_updated_min(self): # real signature unknown; restored from __doc__
        """ get_updated_min(self) -> int """
        return 0

    def get_uploader(self): # real signature unknown; restored from __doc__
        """ get_uploader(self) -> GData.YouTubeUploader """
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

    def is_strict(self): # real signature unknown; restored from __doc__
        """ is_strict(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, q=None): # real signature unknown; restored from __doc__
        """ new(q:str=None) -> GData.YouTubeQuery """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_limits(self, q=None, start_index, max_results): # real signature unknown; restored from __doc__
        """ new_with_limits(q:str=None, start_index:int, max_results:int) -> GData.Query """
        pass

    def next_page(self): # real signature unknown; restored from __doc__
        """ next_page(self) """
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

    def previous_page(self): # real signature unknown; restored from __doc__
        """ previous_page(self) -> bool """
        return False

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

    def set_age(self, age): # real signature unknown; restored from __doc__
        """ set_age(self, age:GData.YouTubeAge) """
        pass

    def set_author(self, author=None): # real signature unknown; restored from __doc__
        """ set_author(self, author:str=None) """
        pass

    def set_categories(self, categories=None): # real signature unknown; restored from __doc__
        """ set_categories(self, categories:str=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_etag(self, etag=None): # real signature unknown; restored from __doc__
        """ set_etag(self, etag:str=None) """
        pass

    def set_format(self, format): # real signature unknown; restored from __doc__
        """ set_format(self, format:GData.YouTubeFormat) """
        pass

    def set_is_strict(self, is_strict): # real signature unknown; restored from __doc__
        """ set_is_strict(self, is_strict:bool) """
        pass

    def set_language(self, language=None): # real signature unknown; restored from __doc__
        """ set_language(self, language:str=None) """
        pass

    def set_license(self, license=None): # real signature unknown; restored from __doc__
        """ set_license(self, license:str=None) """
        pass

    def set_location(self, latitude, longitude, radius, has_location): # real signature unknown; restored from __doc__
        """ set_location(self, latitude:float, longitude:float, radius:float, has_location:bool) """
        pass

    def set_max_results(self, max_results): # real signature unknown; restored from __doc__
        """ set_max_results(self, max_results:int) """
        pass

    def set_order_by(self, order_by=None): # real signature unknown; restored from __doc__
        """ set_order_by(self, order_by:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_published_max(self, published_max): # real signature unknown; restored from __doc__
        """ set_published_max(self, published_max:int) """
        pass

    def set_published_min(self, published_min): # real signature unknown; restored from __doc__
        """ set_published_min(self, published_min:int) """
        pass

    def set_q(self, q=None): # real signature unknown; restored from __doc__
        """ set_q(self, q:str=None) """
        pass

    def set_restriction(self, restriction=None): # real signature unknown; restored from __doc__
        """ set_restriction(self, restriction:str=None) """
        pass

    def set_safe_search(self, safe_search): # real signature unknown; restored from __doc__
        """ set_safe_search(self, safe_search:GData.YouTubeSafeSearch) """
        pass

    def set_sort_order(self, sort_order): # real signature unknown; restored from __doc__
        """ set_sort_order(self, sort_order:GData.YouTubeSortOrder) """
        pass

    def set_start_index(self, start_index): # real signature unknown; restored from __doc__
        """ set_start_index(self, start_index:int) """
        pass

    def set_updated_max(self, updated_max): # real signature unknown; restored from __doc__
        """ set_updated_max(self, updated_max:int) """
        pass

    def set_updated_min(self, updated_min): # real signature unknown; restored from __doc__
        """ set_updated_min(self, updated_min:int) """
        pass

    def set_uploader(self, uploader): # real signature unknown; restored from __doc__
        """ set_uploader(self, uploader:GData.YouTubeUploader) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fd5e24afd60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(YouTubeQuery), '__module__': 'gi.repository.GData', '__gtype__': <GType GDataYouTubeQuery (94233464927280)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_age': gi.FunctionInfo(get_age), 'get_format': gi.FunctionInfo(get_format), 'get_language': gi.FunctionInfo(get_language), 'get_license': gi.FunctionInfo(get_license), 'get_location': gi.FunctionInfo(get_location), 'get_order_by': gi.FunctionInfo(get_order_by), 'get_restriction': gi.FunctionInfo(get_restriction), 'get_safe_search': gi.FunctionInfo(get_safe_search), 'get_sort_order': gi.FunctionInfo(get_sort_order), 'get_uploader': gi.FunctionInfo(get_uploader), 'set_age': gi.FunctionInfo(set_age), 'set_format': gi.FunctionInfo(set_format), 'set_language': gi.FunctionInfo(set_language), 'set_license': gi.FunctionInfo(set_license), 'set_location': gi.FunctionInfo(set_location), 'set_order_by': gi.FunctionInfo(set_order_by), 'set_restriction': gi.FunctionInfo(set_restriction), 'set_safe_search': gi.FunctionInfo(set_safe_search), 'set_sort_order': gi.FunctionInfo(set_sort_order), 'set_uploader': gi.FunctionInfo(set_uploader), 'parent': <property object at 0x7fd5e16f6400>, 'priv': <property object at 0x7fd5e16f64f0>})"
    __gdoc__ = 'Object GDataYouTubeQuery\n\nProperties from GDataYouTubeQuery:\n  format -> GDataYouTubeFormat: Format\n    Specifies that videos must be available in a particular video format.\n  latitude -> gdouble: Latitude\n    The latitude of a particular location of which videos should be found.\n  longitude -> gdouble: Longitude\n    The longitude of a particular location of which videos should be found.\n  location-radius -> gdouble: Location radius\n    The radius, in metres, of a circle to search within.\n  has-location -> gboolean: Has location?\n    Whether to restrict results to videos with specific coordinates.\n  language -> gchararray: Language\n    Restricts the search to videos described in the given language.\n  order-by -> gchararray: Order by\n    Specifies the order of entries in a feed.\n  restriction -> gchararray: Restriction\n    The country code to filter videos playable only in specific countries.\n  safe-search -> GDataYouTubeSafeSearch: Safe search\n    Whether the search results should include restricted content.\n  sort-order -> GDataYouTubeSortOrder: Sort order\n    Specifies the direction of sorting.\n  age -> GDataYouTubeAge: Age\n    Restricts the search to videos uploaded within the specified time period.\n  uploader -> GDataYouTubeUploader: Uploader\n    Restricts the search to videos from the specified type of uploader.\n  license -> gchararray: License\n    The content license which should be used to filter search results.\n\nProperties from GDataQuery:\n  q -> gchararray: Query terms\n    Query terms for which to search.\n  categories -> gchararray: Category string\n    Category search string.\n  author -> gchararray: Author\n    Author search string.\n  updated-min -> gint64: Minimum update date\n    Minimum date for updates on returned entries.\n  updated-max -> gint64: Maximum update date\n    Maximum date for updates on returned entries.\n  published-min -> gint64: Minimum publish date\n    Minimum date for returned entries to be published.\n  published-max -> gint64: Maximum publish date\n    Maximum date for returned entries to be published.\n  start-index -> guint: Start index\n    One-based result start index.\n  is-strict -> gboolean: Strict?\n    Should the server be strict about the query?\n  max-results -> guint: Maximum number of results\n    The maximum number of entries to return.\n  etag -> gchararray: ETag\n    An ETag against which to check.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDataYouTubeQuery (94233464927280)>'
    __info__ = ObjectInfo(YouTubeQuery)


