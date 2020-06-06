# encoding: utf-8
# module gi.repository.EBookContacts
# from /usr/lib64/girepository-1.0/EBookContacts-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gobject as __gobject


from .VCard import VCard

class Contact(VCard):
    """
    :Constructors:
    
    ::
    
        Contact(**properties)
        new() -> EBookContacts.Contact
        new_from_vcard(vcard:str) -> EBookContacts.Contact
        new_from_vcard_with_uid(vcard:str, uid:str) -> EBookContacts.Contact
    """
    def add_attribute(self, attr): # real signature unknown; restored from __doc__
        """ add_attribute(self, attr:EBookContacts.VCardAttribute) """
        pass

    def add_attribute_with_value(self, attr, value): # real signature unknown; restored from __doc__
        """ add_attribute_with_value(self, attr:EBookContacts.VCardAttribute, value:str) """
        pass

    def append_attribute(self, attr): # real signature unknown; restored from __doc__
        """ append_attribute(self, attr:EBookContacts.VCardAttribute) """
        pass

    def append_attribute_with_value(self, attr, value): # real signature unknown; restored from __doc__
        """ append_attribute_with_value(self, attr:EBookContacts.VCardAttribute, value:str) """
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

    def construct(self, p_str): # real signature unknown; restored from __doc__
        """ construct(self, str:str) """
        pass

    def construct_full(self, p_str, len, uid=None): # real signature unknown; restored from __doc__
        """ construct_full(self, str:str, len:int, uid:str=None) """
        pass

    def construct_with_uid(self, p_str, uid=None): # real signature unknown; restored from __doc__
        """ construct_with_uid(self, str:str, uid:str=None) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def dump_structure(self): # real signature unknown; restored from __doc__
        """ dump_structure(self) """
        pass

    def duplicate(self): # real signature unknown; restored from __doc__
        """ duplicate(self) -> EBookContacts.Contact """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def escape_string(self, s): # real signature unknown; restored from __doc__
        """ escape_string(s:str) -> str """
        return ""

    def field_id(self, field_name): # real signature unknown; restored from __doc__
        """ field_id(field_name:str) -> EBookContacts.ContactField """
        pass

    def field_id_from_vcard(self, vcard_field): # real signature unknown; restored from __doc__
        """ field_id_from_vcard(vcard_field:str) -> EBookContacts.ContactField """
        pass

    def field_is_string(self, field_id): # real signature unknown; restored from __doc__
        """ field_is_string(field_id:EBookContacts.ContactField) -> bool """
        return False

    def field_name(self, field_id): # real signature unknown; restored from __doc__
        """ field_name(field_id:EBookContacts.ContactField) -> str """
        return ""

    def field_type(self, field_id): # real signature unknown; restored from __doc__
        """ field_type(field_id:EBookContacts.ContactField) -> GType """
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

    def get(self, field_id): # real signature unknown; restored from __doc__
        """ get(self, field_id:EBookContacts.ContactField) """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_attribute(self, name): # real signature unknown; restored from __doc__
        """ get_attribute(self, name:str) -> EBookContacts.VCardAttribute or None """
        pass

    def get_attributes(self, field_id): # real signature unknown; restored from __doc__
        """ get_attributes(self, field_id:EBookContacts.ContactField) -> list """
        return []

    def get_attributes_set(self, field_ids, size): # real signature unknown; restored from __doc__
        """ get_attributes_set(self, field_ids:EBookContacts.ContactField, size:int) -> list """
        return []

    def get_attribute_if_parsed(self, name): # real signature unknown; restored from __doc__
        """ get_attribute_if_parsed(self, name:str) -> EBookContacts.VCardAttribute or None """
        pass

    def get_const(self, field_id): # real signature unknown; restored from __doc__
        """ get_const(self, field_id:EBookContacts.ContactField) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def inline_local_photos(self): # real signature unknown; restored from __doc__
        """ inline_local_photos(self) -> bool """
        return False

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

    def is_parsed(self): # real signature unknown; restored from __doc__
        """ is_parsed(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> EBookContacts.Contact """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ new_from_string(str:str) -> EBookContacts.VCard """
        pass

    def new_from_vcard(self, vcard): # real signature unknown; restored from __doc__
        """ new_from_vcard(vcard:str) -> EBookContacts.Contact """
        pass

    def new_from_vcard_with_uid(self, vcard, uid): # real signature unknown; restored from __doc__
        """ new_from_vcard_with_uid(vcard:str, uid:str) -> EBookContacts.Contact """
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

    def pretty_name(self, field_id): # real signature unknown; restored from __doc__
        """ pretty_name(field_id:EBookContacts.ContactField) -> str """
        return ""

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_attribute(self, attr): # real signature unknown; restored from __doc__
        """ remove_attribute(self, attr:EBookContacts.VCardAttribute) """
        pass

    def remove_attributes(self, attr_group=None, attr_name): # real signature unknown; restored from __doc__
        """ remove_attributes(self, attr_group:str=None, attr_name:str) """
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

    def set(self, field_id, value=None): # real signature unknown; restored from __doc__
        """ set(self, field_id:EBookContacts.ContactField, value=None) """
        pass

    def set_attributes(self, field_id, attributes): # real signature unknown; restored from __doc__
        """ set_attributes(self, field_id:EBookContacts.ContactField, attributes:list) """
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

    def to_string(self, format): # real signature unknown; restored from __doc__
        """ to_string(self, format:EBookContacts.VCardFormat) -> str """
        return ""

    def unescape_string(self, s): # real signature unknown; restored from __doc__
        """ unescape_string(s:str) -> str """
        return ""

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def util_dup_x_attribute(self, x_name): # real signature unknown; restored from __doc__
        """ util_dup_x_attribute(self, x_name:str) -> str or None """
        return ""

    def util_set_x_attribute(self, x_name, value=None): # real signature unknown; restored from __doc__
        """ util_set_x_attribute(self, x_name:str, value:str=None) """
        pass

    def vcard_attribute(self, field_id): # real signature unknown; restored from __doc__
        """ vcard_attribute(field_id:EBookContacts.ContactField) -> str """
        return ""

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f71488365e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Contact), '__module__': 'gi.repository.EBookContacts', '__gtype__': <GType EContact (94769385548528)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_vcard': gi.FunctionInfo(new_from_vcard), 'new_from_vcard_with_uid': gi.FunctionInfo(new_from_vcard_with_uid), 'field_id': gi.FunctionInfo(field_id), 'field_id_from_vcard': gi.FunctionInfo(field_id_from_vcard), 'field_is_string': gi.FunctionInfo(field_is_string), 'field_name': gi.FunctionInfo(field_name), 'field_type': gi.FunctionInfo(field_type), 'pretty_name': gi.FunctionInfo(pretty_name), 'vcard_attribute': gi.FunctionInfo(vcard_attribute), 'duplicate': gi.FunctionInfo(duplicate), 'get': gi.FunctionInfo(get), 'get_attributes': gi.FunctionInfo(get_attributes), 'get_attributes_set': gi.FunctionInfo(get_attributes_set), 'get_const': gi.FunctionInfo(get_const), 'inline_local_photos': gi.FunctionInfo(inline_local_photos), 'set': gi.FunctionInfo(set), 'set_attributes': gi.FunctionInfo(set_attributes), 'parent': <property object at 0x7f714bb37810>, 'priv': <property object at 0x7f714bb37900>})"
    __gdoc__ = 'Object EContact\n\nProperties from EContact:\n  id -> gchararray: Unique ID\n    Unique ID\n  file-as -> gchararray: File Under\n    File Under\n  book-uid -> gchararray: Book UID\n    Book UID\n  full-name -> gchararray: Full Name\n    Full Name\n  given-name -> gchararray: Given Name\n    Given Name\n  family-name -> gchararray: Family Name\n    Family Name\n  nickname -> gchararray: Nickname\n    Nickname\n  email-1 -> gchararray: Email 1\n    Email 1\n  email-2 -> gchararray: Email 2\n    Email 2\n  email-3 -> gchararray: Email 3\n    Email 3\n  email-4 -> gchararray: Email 4\n    Email 4\n  mailer -> gchararray: Mailer\n    Mailer\n  address-label-home -> gchararray: Home Address Label\n    Home Address Label\n  address-label-work -> gchararray: Work Address Label\n    Work Address Label\n  address-label-other -> gchararray: Other Address Label\n    Other Address Label\n  assistant-phone -> gchararray: Assistant Phone\n    Assistant Phone\n  business-phone -> gchararray: Business Phone\n    Business Phone\n  business-phone-2 -> gchararray: Business Phone 2\n    Business Phone 2\n  business-fax -> gchararray: Business Fax\n    Business Fax\n  callback-phone -> gchararray: Callback Phone\n    Callback Phone\n  car-phone -> gchararray: Car Phone\n    Car Phone\n  company-phone -> gchararray: Company Phone\n    Company Phone\n  home-phone -> gchararray: Home Phone\n    Home Phone\n  home-phone-2 -> gchararray: Home Phone 2\n    Home Phone 2\n  home-fax -> gchararray: Home Fax\n    Home Fax\n  isdn-phone -> gchararray: ISDN\n    ISDN\n  mobile-phone -> gchararray: Mobile Phone\n    Mobile Phone\n  other-phone -> gchararray: Other Phone\n    Other Phone\n  other-fax -> gchararray: Other Fax\n    Other Fax\n  pager -> gchararray: Pager\n    Pager\n  primary-phone -> gchararray: Primary Phone\n    Primary Phone\n  radio -> gchararray: Radio\n    Radio\n  telex -> gchararray: Telex\n    Telex\n  tty -> gchararray: TTY\n    TTY\n  org -> gchararray: Organization\n    Organization\n  org-unit -> gchararray: Organizational Unit\n    Organizational Unit\n  office -> gchararray: Office\n    Office\n  title -> gchararray: Title\n    Title\n  role -> gchararray: Role\n    Role\n  manager -> gchararray: Manager\n    Manager\n  assistant -> gchararray: Assistant\n    Assistant\n  homepage-url -> gchararray: Homepage URL\n    Homepage URL\n  blog-url -> gchararray: Weblog URL\n    Weblog URL\n  categories -> gchararray: Categories\n    Categories\n  caluri -> gchararray: Calendar URI\n    Calendar URI\n  fburl -> gchararray: Free/Busy URL\n    Free/Busy URL\n  icscalendar -> gchararray: ICS Calendar\n    ICS Calendar\n  video-url -> gchararray: Video Conferencing URL\n    Video Conferencing URL\n  spouse -> gchararray: Spouse’s Name\n    Spouse’s Name\n  note -> gchararray: Note\n    Note\n  im-aim-home-1 -> gchararray: AIM Home Screen Name 1\n    AIM Home Screen Name 1\n  im-aim-home-2 -> gchararray: AIM Home Screen Name 2\n    AIM Home Screen Name 2\n  im-aim-home-3 -> gchararray: AIM Home Screen Name 3\n    AIM Home Screen Name 3\n  im-aim-work-1 -> gchararray: AIM Work Screen Name 1\n    AIM Work Screen Name 1\n  im-aim-work-2 -> gchararray: AIM Work Screen Name 2\n    AIM Work Screen Name 2\n  im-aim-work-3 -> gchararray: AIM Work Screen Name 3\n    AIM Work Screen Name 3\n  im-groupwise-home-1 -> gchararray: GroupWise Home Screen Name 1\n    GroupWise Home Screen Name 1\n  im-groupwise-home-2 -> gchararray: GroupWise Home Screen Name 2\n    GroupWise Home Screen Name 2\n  im-groupwise-home-3 -> gchararray: GroupWise Home Screen Name 3\n    GroupWise Home Screen Name 3\n  im-groupwise-work-1 -> gchararray: GroupWise Work Screen Name 1\n    GroupWise Work Screen Name 1\n  im-groupwise-work-2 -> gchararray: GroupWise Work Screen Name 2\n    GroupWise Work Screen Name 2\n  im-groupwise-work-3 -> gchararray: GroupWise Work Screen Name 3\n    GroupWise Work Screen Name 3\n  im-jabber-home-1 -> gchararray: Jabber Home ID 1\n    Jabber Home ID 1\n  im-jabber-home-2 -> gchararray: Jabber Home ID 2\n    Jabber Home ID 2\n  im-jabber-home-3 -> gchararray: Jabber Home ID 3\n    Jabber Home ID 3\n  im-jabber-work-1 -> gchararray: Jabber Work ID 1\n    Jabber Work ID 1\n  im-jabber-work-2 -> gchararray: Jabber Work ID 2\n    Jabber Work ID 2\n  im-jabber-work-3 -> gchararray: Jabber Work ID 3\n    Jabber Work ID 3\n  im-yahoo-home-1 -> gchararray: Yahoo! Home Screen Name 1\n    Yahoo! Home Screen Name 1\n  im-yahoo-home-2 -> gchararray: Yahoo! Home Screen Name 2\n    Yahoo! Home Screen Name 2\n  im-yahoo-home-3 -> gchararray: Yahoo! Home Screen Name 3\n    Yahoo! Home Screen Name 3\n  im-yahoo-work-1 -> gchararray: Yahoo! Work Screen Name 1\n    Yahoo! Work Screen Name 1\n  im-yahoo-work-2 -> gchararray: Yahoo! Work Screen Name 2\n    Yahoo! Work Screen Name 2\n  im-yahoo-work-3 -> gchararray: Yahoo! Work Screen Name 3\n    Yahoo! Work Screen Name 3\n  im-msn-home-1 -> gchararray: MSN Home Screen Name 1\n    MSN Home Screen Name 1\n  im-msn-home-2 -> gchararray: MSN Home Screen Name 2\n    MSN Home Screen Name 2\n  im-msn-home-3 -> gchararray: MSN Home Screen Name 3\n    MSN Home Screen Name 3\n  im-msn-work-1 -> gchararray: MSN Work Screen Name 1\n    MSN Work Screen Name 1\n  im-msn-work-2 -> gchararray: MSN Work Screen Name 2\n    MSN Work Screen Name 2\n  im-msn-work-3 -> gchararray: MSN Work Screen Name 3\n    MSN Work Screen Name 3\n  im-icq-home-1 -> gchararray: ICQ Home ID 1\n    ICQ Home ID 1\n  im-icq-home-2 -> gchararray: ICQ Home ID 2\n    ICQ Home ID 2\n  im-icq-home-3 -> gchararray: ICQ Home ID 3\n    ICQ Home ID 3\n  im-icq-work-1 -> gchararray: ICQ Work ID 1\n    ICQ Work ID 1\n  im-icq-work-2 -> gchararray: ICQ Work ID 2\n    ICQ Work ID 2\n  im-icq-work-3 -> gchararray: ICQ Work ID 3\n    ICQ Work ID 3\n  Rev -> gchararray: Last Revision\n    Last Revision\n  name-or-org -> gchararray: Name or Org\n    Name or Org\n  address -> EContactAttrList: Address List\n    Address List\n  address-home -> EContactAddress: Home Address\n    Home Address\n  address-work -> EContactAddress: Work Address\n    Work Address\n  address-other -> EContactAddress: Other Address\n    Other Address\n  category-list -> gpointer: Category List\n    Category List\n  photo -> EContactPhoto: Photo\n    Photo\n  logo -> EContactPhoto: Logo\n    Logo\n  name -> EContactName: Name\n    Name\n  email -> EContactAttrList: Email List\n    Email List\n  im-aim -> EContactAttrList: AIM Screen Name List\n    AIM Screen Name List\n  im-groupwise -> EContactAttrList: GroupWise ID List\n    GroupWise ID List\n  im-jabber -> EContactAttrList: Jabber ID List\n    Jabber ID List\n  im-yahoo -> EContactAttrList: Yahoo! Screen Name List\n    Yahoo! Screen Name List\n  im-msn -> EContactAttrList: MSN Screen Name List\n    MSN Screen Name List\n  im-icq -> EContactAttrList: ICQ ID List\n    ICQ ID List\n  wants-html -> gboolean: Wants HTML Mail\n    Wants HTML Mail\n  list -> gboolean: List\n    List\n  list-show-addresses -> gboolean: List Shows Addresses\n    List Shows Addresses\n  birth-date -> EContactDate: Birth Date\n    Birth Date\n  anniversary -> EContactDate: Anniversary\n    Anniversary\n  x509Cert -> EContactCert: X.509 Certificate\n    X.509 Certificate\n  pgpCert -> EContactCert: PGP Certificate\n    PGP Certificate\n  im-gadugadu-home-1 -> gchararray: Gadu-Gadu Home ID 1\n    Gadu-Gadu Home ID 1\n  im-gadugadu-home-2 -> gchararray: Gadu-Gadu Home ID 2\n    Gadu-Gadu Home ID 2\n  im-gadugadu-home-3 -> gchararray: Gadu-Gadu Home ID 3\n    Gadu-Gadu Home ID 3\n  im-gadugadu-work-1 -> gchararray: Gadu-Gadu Work ID 1\n    Gadu-Gadu Work ID 1\n  im-gadugadu-work-2 -> gchararray: Gadu-Gadu Work ID 2\n    Gadu-Gadu Work ID 2\n  im-gadugadu-work-3 -> gchararray: Gadu-Gadu Work ID 3\n    Gadu-Gadu Work ID 3\n  im-gadugadu -> EContactAttrList: Gadu-Gadu ID List\n    Gadu-Gadu ID List\n  geo -> EContactGeo: Geographic Information\n    Geographic Information\n  phone -> EContactAttrList: Telephone\n    Telephone\n  im-skype-home-1 -> gchararray: Skype Home Name 1\n    Skype Home Name 1\n  im-skype-home-2 -> gchararray: Skype Home Name 2\n    Skype Home Name 2\n  im-skype-home-3 -> gchararray: Skype Home Name 3\n    Skype Home Name 3\n  im-skype-work-1 -> gchararray: Skype Work Name 1\n    Skype Work Name 1\n  im-skype-work-2 -> gchararray: Skype Work Name 2\n    Skype Work Name 2\n  im-skype-work-3 -> gchararray: Skype Work Name 3\n    Skype Work Name 3\n  im-skype -> EContactAttrList: Skype Name List\n    Skype Name List\n  sip -> EContactAttrList: SIP address\n    SIP address\n  im-google-talk-home-1 -> gchararray: Google Talk Home Name 1\n    Google Talk Home Name 1\n  im-google-talk-home-2 -> gchararray: Google Talk Home Name 2\n    Google Talk Home Name 2\n  im-google-talk-home-3 -> gchararray: Google Talk Home Name 3\n    Google Talk Home Name 3\n  im-google-talk-work-1 -> gchararray: Google Talk Work Name 1\n    Google Talk Work Name 1\n  im-google-talk-work-2 -> gchararray: Google Talk Work Name 2\n    Google Talk Work Name 2\n  im-google-talk-work-3 -> gchararray: Google Talk Work Name 3\n    Google Talk Work Name 3\n  im-google-talk -> EContactAttrList: Google Talk Name List\n    Google Talk Name List\n  im-twitter -> EContactAttrList: Twitter Name List\n    Twitter Name List\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EContact (94769385548528)>'
    __info__ = ObjectInfo(Contact)


