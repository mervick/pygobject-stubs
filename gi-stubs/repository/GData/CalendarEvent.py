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

class CalendarEvent(Entry):
    """
    :Constructors:
    
    ::
    
        CalendarEvent(**properties)
        new(id:str=None) -> GData.CalendarEvent
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

    def add_person(self, who): # real signature unknown; restored from __doc__
        """ add_person(self, who:GData.GDWho) """
        pass

    def add_place(self, where): # real signature unknown; restored from __doc__
        """ add_place(self, where:GData.GDWhere) """
        pass

    def add_time(self, when): # real signature unknown; restored from __doc__
        """ add_time(self, when:GData.GDWhen) """
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

    def get_anyone_can_add_self(self): # real signature unknown; restored from __doc__
        """ get_anyone_can_add_self(self) -> bool """
        return False

    def get_authors(self): # real signature unknown; restored from __doc__
        """ get_authors(self) -> list """
        return []

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> list """
        return []

    def get_content(self): # real signature unknown; restored from __doc__
        """ get_content(self) -> str """
        return ""

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> str """
        return ""

    def get_content_uri(self): # real signature unknown; restored from __doc__
        """ get_content_uri(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_edited(self): # real signature unknown; restored from __doc__
        """ get_edited(self) -> int """
        return 0

    def get_etag(self): # real signature unknown; restored from __doc__
        """ get_etag(self) -> str or None """
        return ""

    def get_guests_can_invite_others(self): # real signature unknown; restored from __doc__
        """ get_guests_can_invite_others(self) -> bool """
        return False

    def get_guests_can_modify(self): # real signature unknown; restored from __doc__
        """ get_guests_can_modify(self) -> bool """
        return False

    def get_guests_can_see_guests(self): # real signature unknown; restored from __doc__
        """ get_guests_can_see_guests(self) -> bool """
        return False

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str or None """
        return ""

    def get_json(self): # real signature unknown; restored from __doc__
        """ get_json(self) -> str """
        return ""

    def get_original_event_details(self): # real signature unknown; restored from __doc__
        """ get_original_event_details(self) -> event_id:str, event_uri:str """
        pass

    def get_people(self): # real signature unknown; restored from __doc__
        """ get_people(self) -> list """
        return []

    def get_places(self): # real signature unknown; restored from __doc__
        """ get_places(self) -> list """
        return []

    def get_primary_time(self): # real signature unknown; restored from __doc__
        """ get_primary_time(self) -> bool, start_time:int, end_time:int, when:GData.GDWhen """
        return False

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

    def get_recurrence(self): # real signature unknown; restored from __doc__
        """ get_recurrence(self) -> str """
        return ""

    def get_rights(self): # real signature unknown; restored from __doc__
        """ get_rights(self) -> str """
        return ""

    def get_sequence(self): # real signature unknown; restored from __doc__
        """ get_sequence(self) -> int """
        return 0

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> str """
        return ""

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

    def get_times(self): # real signature unknown; restored from __doc__
        """ get_times(self) -> list """
        return []

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_transparency(self): # real signature unknown; restored from __doc__
        """ get_transparency(self) -> str """
        return ""

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str """
        return ""

    def get_updated(self): # real signature unknown; restored from __doc__
        """ get_updated(self) -> int """
        return 0

    def get_visibility(self): # real signature unknown; restored from __doc__
        """ get_visibility(self) -> str """
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

    def is_exception(self): # real signature unknown; restored from __doc__
        """ is_exception(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_inserted(self): # real signature unknown; restored from __doc__
        """ is_inserted(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def look_up_link(self, rel): # real signature unknown; restored from __doc__
        """ look_up_link(self, rel:str) -> GData.Link """
        pass

    def look_up_links(self, rel): # real signature unknown; restored from __doc__
        """ look_up_links(self, rel:str) -> list """
        return []

    def new(self, id=None): # real signature unknown; restored from __doc__
        """ new(id:str=None) -> GData.CalendarEvent """
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

    def set_anyone_can_add_self(self, anyone_can_add_self): # real signature unknown; restored from __doc__
        """ set_anyone_can_add_self(self, anyone_can_add_self:bool) """
        pass

    def set_content(self, content=None): # real signature unknown; restored from __doc__
        """ set_content(self, content:str=None) """
        pass

    def set_content_uri(self, content_uri=None): # real signature unknown; restored from __doc__
        """ set_content_uri(self, content_uri:str=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_guests_can_invite_others(self, guests_can_invite_others): # real signature unknown; restored from __doc__
        """ set_guests_can_invite_others(self, guests_can_invite_others:bool) """
        pass

    def set_guests_can_modify(self, guests_can_modify): # real signature unknown; restored from __doc__
        """ set_guests_can_modify(self, guests_can_modify:bool) """
        pass

    def set_guests_can_see_guests(self, guests_can_see_guests): # real signature unknown; restored from __doc__
        """ set_guests_can_see_guests(self, guests_can_see_guests:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_recurrence(self, recurrence=None): # real signature unknown; restored from __doc__
        """ set_recurrence(self, recurrence:str=None) """
        pass

    def set_rights(self, rights=None): # real signature unknown; restored from __doc__
        """ set_rights(self, rights:str=None) """
        pass

    def set_sequence(self, sequence): # real signature unknown; restored from __doc__
        """ set_sequence(self, sequence:int) """
        pass

    def set_status(self, status=None): # real signature unknown; restored from __doc__
        """ set_status(self, status:str=None) """
        pass

    def set_summary(self, summary=None): # real signature unknown; restored from __doc__
        """ set_summary(self, summary:str=None) """
        pass

    def set_title(self, title=None): # real signature unknown; restored from __doc__
        """ set_title(self, title:str=None) """
        pass

    def set_transparency(self, transparency=None): # real signature unknown; restored from __doc__
        """ set_transparency(self, transparency:str=None) """
        pass

    def set_uid(self, uid=None): # real signature unknown; restored from __doc__
        """ set_uid(self, uid:str=None) """
        pass

    def set_visibility(self, visibility=None): # real signature unknown; restored from __doc__
        """ set_visibility(self, visibility:str=None) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fd5e2360be0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(CalendarEvent), '__module__': 'gi.repository.GData', '__gtype__': <GType GDataCalendarEvent (94233464343456)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_person': gi.FunctionInfo(add_person), 'add_place': gi.FunctionInfo(add_place), 'add_time': gi.FunctionInfo(add_time), 'get_anyone_can_add_self': gi.FunctionInfo(get_anyone_can_add_self), 'get_edited': gi.FunctionInfo(get_edited), 'get_guests_can_invite_others': gi.FunctionInfo(get_guests_can_invite_others), 'get_guests_can_modify': gi.FunctionInfo(get_guests_can_modify), 'get_guests_can_see_guests': gi.FunctionInfo(get_guests_can_see_guests), 'get_original_event_details': gi.FunctionInfo(get_original_event_details), 'get_people': gi.FunctionInfo(get_people), 'get_places': gi.FunctionInfo(get_places), 'get_primary_time': gi.FunctionInfo(get_primary_time), 'get_recurrence': gi.FunctionInfo(get_recurrence), 'get_sequence': gi.FunctionInfo(get_sequence), 'get_status': gi.FunctionInfo(get_status), 'get_times': gi.FunctionInfo(get_times), 'get_transparency': gi.FunctionInfo(get_transparency), 'get_uid': gi.FunctionInfo(get_uid), 'get_visibility': gi.FunctionInfo(get_visibility), 'is_exception': gi.FunctionInfo(is_exception), 'set_anyone_can_add_self': gi.FunctionInfo(set_anyone_can_add_self), 'set_guests_can_invite_others': gi.FunctionInfo(set_guests_can_invite_others), 'set_guests_can_modify': gi.FunctionInfo(set_guests_can_modify), 'set_guests_can_see_guests': gi.FunctionInfo(set_guests_can_see_guests), 'set_recurrence': gi.FunctionInfo(set_recurrence), 'set_sequence': gi.FunctionInfo(set_sequence), 'set_status': gi.FunctionInfo(set_status), 'set_transparency': gi.FunctionInfo(set_transparency), 'set_uid': gi.FunctionInfo(set_uid), 'set_visibility': gi.FunctionInfo(set_visibility), 'parent': <property object at 0x7fd5e17734f0>, 'priv': <property object at 0x7fd5e17735e0>})"
    __gdoc__ = "Object GDataCalendarEvent\n\nProperties from GDataCalendarEvent:\n  edited -> gint64: Edited\n    The last time the event was edited.\n  status -> gchararray: Status\n    The scheduling status of the event.\n  visibility -> gchararray: Visibility\n    The event's visibility to calendar users.\n  transparency -> gchararray: Transparency\n    How the event is marked as consuming time on a calendar.\n  uid -> gchararray: UID\n    The globally unique identifier (UID) of the event.\n  sequence -> guint: Sequence\n    The revision sequence number of the event.\n  guests-can-modify -> gboolean: Guests can modify\n    Indicates whether attendees may modify the original event.\n  guests-can-invite-others -> gboolean: Guests can invite others\n    Indicates whether attendees may invite others.\n  guests-can-see-guests -> gboolean: Guests can see guests\n    Indicates whether attendees can see other people invited.\n  anyone-can-add-self -> gboolean: Anyone can add self\n    Indicates whether anyone can invite themselves to the event.\n  recurrence -> gchararray: Recurrence\n    Represents the dates and times when a recurring event takes place.\n  original-event-id -> gchararray: Original event ID\n    The event ID for the original event.\n  original-event-uri -> gchararray: Original event URI\n    The event URI for the original event.\n\nProperties from GDataEntry:\n  title -> gchararray: Title\n    A human-readable title for the entry.\n  summary -> gchararray: Summary\n    A short summary, abstract, or excerpt of the entry.\n  etag -> gchararray: ETag\n    An identifier for a particular version of the entry.\n  id -> gchararray: ID\n    A permanent, universally unique identifier for the entry, in IRI form.\n  updated -> gint64: Updated\n    The date and time when the entry was most recently updated significantly.\n  published -> gint64: Published\n    The date and time the entry was first published or made available.\n  content -> gchararray: Content\n    The content of the entry.\n  is-inserted -> gboolean: Inserted?\n    Whether the entry has been inserted on the server.\n  rights -> gchararray: Rights\n    The ownership rights pertaining to the entry.\n  content-uri -> gchararray: Content URI\n    A URI pointing to the location of the content of the entry.\n\nProperties from GDataParsable:\n  constructed-from-xml -> gboolean: Constructed from XML?\n    Specifies whether the object was constructed by parsing XML or manually.\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDataCalendarEvent (94233464343456)>'
    __info__ = ObjectInfo(CalendarEvent)


