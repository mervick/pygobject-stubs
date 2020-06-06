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


from .Entry import Entry

from .Commentable import Commentable

class YouTubeVideo(Entry, Commentable):
    """
    :Constructors:
    
    ::
    
        YouTubeVideo(**properties)
        new(id:str=None) -> GData.YouTubeVideo
    """
    def add_author(self, author): # real signature unknown; restored from __doc__
        """ add_author(self, author:GData.Author) """
        pass

    def add_category(self, category): # real signature unknown; restored from __doc__
        """ add_category(self, category:GData.Category) """
        pass

    def add_link(self, _link): # real signature unknown; restored from __doc__
        """ add_link(self, _link:GData.Link) """
        pass

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

    def delete_comment(self, service, comment_, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_comment(self, service:GData.Service, comment_:GData.Comment, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def delete_comment_async(self, service, comment_, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_comment_async(self, service:GData.Service, comment_:GData.Comment, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_comment_finish(self, result): # real signature unknown; restored from __doc__
        """ delete_comment_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    def get_access_control(self, action): # real signature unknown; restored from __doc__
        """ get_access_control(self, action:str) -> GData.YouTubePermission """
        pass

    def get_aspect_ratio(self): # real signature unknown; restored from __doc__
        """ get_aspect_ratio(self) -> str """
        return ""

    def get_authors(self): # real signature unknown; restored from __doc__
        """ get_authors(self) -> list """
        return []

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> list """
        return []

    def get_category(self): # real signature unknown; restored from __doc__
        """ get_category(self) -> GData.MediaCategory """
        pass

    def get_content(self): # real signature unknown; restored from __doc__
        """ get_content(self) -> str """
        return ""

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> str """
        return ""

    def get_content_uri(self): # real signature unknown; restored from __doc__
        """ get_content_uri(self) -> str """
        return ""

    def get_coordinates(self): # real signature unknown; restored from __doc__
        """ get_coordinates(self) -> latitude:float, longitude:float """
        pass

    def get_credit(self): # real signature unknown; restored from __doc__
        """ get_credit(self) -> GData.YouTubeCredit """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> int """
        return 0

    def get_etag(self): # real signature unknown; restored from __doc__
        """ get_etag(self) -> str or None """
        return ""

    def get_favorite_count(self): # real signature unknown; restored from __doc__
        """ get_favorite_count(self) -> int """
        return 0

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str or None """
        return ""

    def get_json(self): # real signature unknown; restored from __doc__
        """ get_json(self) -> str """
        return ""

    def get_keywords(self): # real signature unknown; restored from __doc__
        """ get_keywords(self) -> list """
        return []

    def get_location(self): # real signature unknown; restored from __doc__
        """ get_location(self) -> str """
        return ""

    def get_media_rating(self, rating_type): # real signature unknown; restored from __doc__
        """ get_media_rating(self, rating_type:str) -> str """
        return ""

    def get_player_uri(self): # real signature unknown; restored from __doc__
        """ get_player_uri(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_published(self): # real signature unknown; restored from __doc__
        """ get_published(self) -> int """
        return 0

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rating(self): # real signature unknown; restored from __doc__
        """ get_rating(self) -> min:int, max:int, count:int, average:float """
        pass

    def get_recorded(self): # real signature unknown; restored from __doc__
        """ get_recorded(self) -> int """
        return 0

    def get_rights(self): # real signature unknown; restored from __doc__
        """ get_rights(self) -> str """
        return ""

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> GData.YouTubeState """
        pass

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

    def get_thumbnails(self): # real signature unknown; restored from __doc__
        """ get_thumbnails(self) -> list """
        return []

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_updated(self): # real signature unknown; restored from __doc__
        """ get_updated(self) -> int """
        return 0

    def get_uploaded(self): # real signature unknown; restored from __doc__
        """ get_uploaded(self) -> int """
        return 0

    def get_video_id(self): # real signature unknown; restored from __doc__
        """ get_video_id(self) -> str """
        return ""

    def get_video_id_from_uri(self, video_uri): # real signature unknown; restored from __doc__
        """ get_video_id_from_uri(video_uri:str) -> str """
        return ""

    def get_view_count(self): # real signature unknown; restored from __doc__
        """ get_view_count(self) -> int """
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

    def insert_comment(self, service, comment_, cancellable=None): # real signature unknown; restored from __doc__
        """ insert_comment(self, service:GData.Service, comment_:GData.Comment, cancellable:Gio.Cancellable=None) -> GData.Comment or None """
        pass

    def insert_comment_async(self, service, comment_, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ insert_comment_async(self, service:GData.Service, comment_:GData.Comment, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def insert_comment_finish(self, result): # real signature unknown; restored from __doc__
        """ insert_comment_finish(self, result:Gio.AsyncResult) -> GData.Comment or None """
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

    def is_draft(self): # real signature unknown; restored from __doc__
        """ is_draft(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_inserted(self): # real signature unknown; restored from __doc__
        """ is_inserted(self) -> bool """
        return False

    def is_private(self): # real signature unknown; restored from __doc__
        """ is_private(self) -> bool """
        return False

    def is_restricted_in_country(self, country): # real signature unknown; restored from __doc__
        """ is_restricted_in_country(self, country:str) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def look_up_content(self, type): # real signature unknown; restored from __doc__
        """ look_up_content(self, type:str) -> GData.YouTubeContent """
        pass

    def look_up_link(self, rel): # real signature unknown; restored from __doc__
        """ look_up_link(self, rel:str) -> GData.Link """
        pass

    def look_up_links(self, rel): # real signature unknown; restored from __doc__
        """ look_up_links(self, rel:str) -> list """
        return []

    def new(self, id=None): # real signature unknown; restored from __doc__
        """ new(id:str=None) -> GData.YouTubeVideo """
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

    def query_comments(self, service, query=None, cancellable=None, progress_callback=None, progress_user_data=None): # real signature unknown; restored from __doc__
        """ query_comments(self, service:GData.Service, query:GData.Query=None, cancellable:Gio.Cancellable=None, progress_callback:GData.QueryProgressCallback=None, progress_user_data=None) -> GData.Feed or None """
        pass

    def query_comments_async(self, service, query=None, cancellable=None, progress_callback=None, progress_user_data=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_comments_async(self, service:GData.Service, query:GData.Query=None, cancellable:Gio.Cancellable=None, progress_callback:GData.QueryProgressCallback=None, progress_user_data=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_comments_finish(self, result): # real signature unknown; restored from __doc__
        """ query_comments_finish(self, result:Gio.AsyncResult) -> GData.Feed or None """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_link(self, _link): # real signature unknown; restored from __doc__
        """ remove_link(self, _link:GData.Link) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_access_control(self, action, permission): # real signature unknown; restored from __doc__
        """ set_access_control(self, action:str, permission:GData.YouTubePermission) """
        pass

    def set_aspect_ratio(self, aspect_ratio=None): # real signature unknown; restored from __doc__
        """ set_aspect_ratio(self, aspect_ratio:str=None) """
        pass

    def set_category(self, category): # real signature unknown; restored from __doc__
        """ set_category(self, category:GData.MediaCategory) """
        pass

    def set_content(self, content=None): # real signature unknown; restored from __doc__
        """ set_content(self, content:str=None) """
        pass

    def set_content_uri(self, content_uri=None): # real signature unknown; restored from __doc__
        """ set_content_uri(self, content_uri:str=None) """
        pass

    def set_coordinates(self, latitude, longitude): # real signature unknown; restored from __doc__
        """ set_coordinates(self, latitude:float, longitude:float) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description=None): # real signature unknown; restored from __doc__
        """ set_description(self, description:str=None) """
        pass

    def set_is_draft(self, is_draft): # real signature unknown; restored from __doc__
        """ set_is_draft(self, is_draft:bool) """
        pass

    def set_is_private(self, is_private): # real signature unknown; restored from __doc__
        """ set_is_private(self, is_private:bool) """
        pass

    def set_keywords(self, keywords): # real signature unknown; restored from __doc__
        """ set_keywords(self, keywords:list) """
        pass

    def set_location(self, location=None): # real signature unknown; restored from __doc__
        """ set_location(self, location:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_recorded(self, recorded): # real signature unknown; restored from __doc__
        """ set_recorded(self, recorded:int) """
        pass

    def set_rights(self, rights=None): # real signature unknown; restored from __doc__
        """ set_rights(self, rights:str=None) """
        pass

    def set_summary(self, summary=None): # real signature unknown; restored from __doc__
        """ set_summary(self, summary:str=None) """
        pass

    def set_title(self, title=None): # real signature unknown; restored from __doc__
        """ set_title(self, title:str=None) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fd5e2514940>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(YouTubeVideo), '__module__': 'gi.repository.GData', '__gtype__': <GType GDataYouTubeVideo (94233464299344)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_video_id_from_uri': gi.FunctionInfo(get_video_id_from_uri), 'get_access_control': gi.FunctionInfo(get_access_control), 'get_aspect_ratio': gi.FunctionInfo(get_aspect_ratio), 'get_category': gi.FunctionInfo(get_category), 'get_coordinates': gi.FunctionInfo(get_coordinates), 'get_credit': gi.FunctionInfo(get_credit), 'get_description': gi.FunctionInfo(get_description), 'get_duration': gi.FunctionInfo(get_duration), 'get_favorite_count': gi.FunctionInfo(get_favorite_count), 'get_keywords': gi.FunctionInfo(get_keywords), 'get_location': gi.FunctionInfo(get_location), 'get_media_rating': gi.FunctionInfo(get_media_rating), 'get_player_uri': gi.FunctionInfo(get_player_uri), 'get_rating': gi.FunctionInfo(get_rating), 'get_recorded': gi.FunctionInfo(get_recorded), 'get_state': gi.FunctionInfo(get_state), 'get_thumbnails': gi.FunctionInfo(get_thumbnails), 'get_uploaded': gi.FunctionInfo(get_uploaded), 'get_video_id': gi.FunctionInfo(get_video_id), 'get_view_count': gi.FunctionInfo(get_view_count), 'is_draft': gi.FunctionInfo(is_draft), 'is_private': gi.FunctionInfo(is_private), 'is_restricted_in_country': gi.FunctionInfo(is_restricted_in_country), 'look_up_content': gi.FunctionInfo(look_up_content), 'set_access_control': gi.FunctionInfo(set_access_control), 'set_aspect_ratio': gi.FunctionInfo(set_aspect_ratio), 'set_category': gi.FunctionInfo(set_category), 'set_coordinates': gi.FunctionInfo(set_coordinates), 'set_description': gi.FunctionInfo(set_description), 'set_is_draft': gi.FunctionInfo(set_is_draft), 'set_is_private': gi.FunctionInfo(set_is_private), 'set_keywords': gi.FunctionInfo(set_keywords), 'set_location': gi.FunctionInfo(set_location), 'set_recorded': gi.FunctionInfo(set_recorded), 'parent': <property object at 0x7fd5e1700360>, 'priv': <property object at 0x7fd5e1700450>})"
    __gdoc__ = 'Object GDataYouTubeVideo\n\nProperties from GDataYouTubeVideo:\n  view-count -> guint: View count\n    The number of times the video has been viewed.\n  favorite-count -> guint: Favorite count\n    The number of users who have added the video to their favorites.\n  location -> gchararray: Location\n    Descriptive text about the location where the video was taken.\n  min-rating -> guint: Minimum rating\n    The minimum allowed rating for the video.\n  max-rating -> guint: Maximum rating\n    The maximum allowed rating for the video.\n  rating-count -> guint: Rating count\n    The number of times the video has been rated.\n  average-rating -> gdouble: Average rating\n    The average rating of the video.\n  keywords -> GStrv: Keywords\n    A NULL-terminated array of words associated with the video.\n  player-uri -> gchararray: Player URI\n    A URI for a browser-based media player for the full-length video.\n  category -> GDataMediaCategory: Category\n    Specifies a genre or developer tag that describes the video.\n  credit -> GDataYouTubeCredit: Credit\n    Identifies the owner of the video.\n  description -> gchararray: Description\n    A summary or description of the video.\n  duration -> guint: Duration\n    The duration of the video in seconds.\n  is-private -> gboolean: Private?\n    Indicates whether the video is private.\n  uploaded -> gint64: Uploaded\n    Specifies the time the video was originally uploaded to YouTube.\n  video-id -> gchararray: Video ID\n    Specifies a unique ID which YouTube uses to identify the video.\n  is-draft -> gboolean: Draft?\n    Indicates whether the video is in draft, or unpublished, status.\n  state -> GDataYouTubeState: State\n    Information describing the state of the video.\n  recorded -> gint64: Recorded\n    Specifies the time the video was originally recorded.\n  aspect-ratio -> gchararray: Aspect Ratio\n    The aspect ratio of the video.\n  latitude -> gdouble: Latitude\n    The location as a latitude coordinate associated with this video.\n  longitude -> gdouble: Longitude\n    The location as a longitude coordinate associated with this video.\n\nProperties from GDataEntry:\n  title -> gchararray: Title\n    A human-readable title for the entry.\n  summary -> gchararray: Summary\n    A short summary, abstract, or excerpt of the entry.\n  etag -> gchararray: ETag\n    An identifier for a particular version of the entry.\n  id -> gchararray: ID\n    A permanent, universally unique identifier for the entry, in IRI form.\n  updated -> gint64: Updated\n    The date and time when the entry was most recently updated significantly.\n  published -> gint64: Published\n    The date and time the entry was first published or made available.\n  content -> gchararray: Content\n    The content of the entry.\n  is-inserted -> gboolean: Inserted?\n    Whether the entry has been inserted on the server.\n  rights -> gchararray: Rights\n    The ownership rights pertaining to the entry.\n  content-uri -> gchararray: Content URI\n    A URI pointing to the location of the content of the entry.\n\nProperties from GDataParsable:\n  constructed-from-xml -> gboolean: Constructed from XML?\n    Specifies whether the object was constructed by parsing XML or manually.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDataYouTubeVideo (94233464299344)>'
    __info__ = ObjectInfo(YouTubeVideo)


