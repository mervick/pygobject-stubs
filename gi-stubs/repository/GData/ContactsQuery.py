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

class ContactsQuery(Query):
    """
    :Constructors:
    
    ::
    
        ContactsQuery(**properties)
        new(q:str=None) -> GData.ContactsQuery
        new_with_limits(q:str=None, start_index:int, max_results:int) -> GData.ContactsQuery
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

    def get_group(self): # real signature unknown; restored from __doc__
        """ get_group(self) -> str """
        return ""

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

    def get_sort_order(self): # real signature unknown; restored from __doc__
        """ get_sort_order(self) -> str """
        return ""

    def get_start_index(self): # real signature unknown; restored from __doc__
        """ get_start_index(self) -> int """
        return 0

    def get_updated_max(self): # real signature unknown; restored from __doc__
        """ get_updated_max(self) -> int """
        return 0

    def get_updated_min(self): # real signature unknown; restored from __doc__
        """ get_updated_min(self) -> int """
        return 0

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
        """ new(q:str=None) -> GData.ContactsQuery """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_limits(self, q=None, start_index, max_results): # real signature unknown; restored from __doc__
        """ new_with_limits(q:str=None, start_index:int, max_results:int) -> GData.ContactsQuery """
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

    def set_group(self, group=None): # real signature unknown; restored from __doc__
        """ set_group(self, group:str=None) """
        pass

    def set_is_strict(self, is_strict): # real signature unknown; restored from __doc__
        """ set_is_strict(self, is_strict:bool) """
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

    def set_show_deleted(self, show_deleted): # real signature unknown; restored from __doc__
        """ set_show_deleted(self, show_deleted:bool) """
        pass

    def set_sort_order(self, sort_order=None): # real signature unknown; restored from __doc__
        """ set_sort_order(self, sort_order:str=None) """
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

    def show_deleted(self): # real signature unknown; restored from __doc__
        """ show_deleted(self) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fd5e170db20>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ContactsQuery), '__module__': 'gi.repository.GData', '__gtype__': <GType GDataContactsQuery (94233464411408)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_with_limits': gi.FunctionInfo(new_with_limits), 'get_group': gi.FunctionInfo(get_group), 'get_order_by': gi.FunctionInfo(get_order_by), 'get_sort_order': gi.FunctionInfo(get_sort_order), 'set_group': gi.FunctionInfo(set_group), 'set_order_by': gi.FunctionInfo(set_order_by), 'set_show_deleted': gi.FunctionInfo(set_show_deleted), 'set_sort_order': gi.FunctionInfo(set_sort_order), 'show_deleted': gi.FunctionInfo(show_deleted), 'parent': <property object at 0x7fd5e1789400>, 'priv': <property object at 0x7fd5e17894f0>})"
    __gdoc__ = 'Object GDataContactsQuery\n\nProperties from GDataContactsQuery:\n  order-by -> gchararray: Order by\n    Sorting criterion.\n  show-deleted -> gboolean: Show deleted?\n    Whether to include deleted contacts in the query feed.\n  sort-order -> gchararray: Sort order\n    Sorting order direction.\n  group -> gchararray: Group\n    Constrains the results to only those belonging to the group specified.\n\nProperties from GDataQuery:\n  q -> gchararray: Query terms\n    Query terms for which to search.\n  categories -> gchararray: Category string\n    Category search string.\n  author -> gchararray: Author\n    Author search string.\n  updated-min -> gint64: Minimum update date\n    Minimum date for updates on returned entries.\n  updated-max -> gint64: Maximum update date\n    Maximum date for updates on returned entries.\n  published-min -> gint64: Minimum publish date\n    Minimum date for returned entries to be published.\n  published-max -> gint64: Maximum publish date\n    Maximum date for returned entries to be published.\n  start-index -> guint: Start index\n    One-based result start index.\n  is-strict -> gboolean: Strict?\n    Should the server be strict about the query?\n  max-results -> guint: Maximum number of results\n    The maximum number of entries to return.\n  etag -> gchararray: ETag\n    An ETag against which to check.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDataContactsQuery (94233464411408)>'
    __info__ = ObjectInfo(ContactsQuery)


