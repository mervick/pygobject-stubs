# encoding: utf-8
# module gi.repository.GUPnPAV
# from /usr/lib64/girepository-1.0/GUPnPAV-1.0.typelib
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
import gobject as __gobject


from .DIDLLiteObject import DIDLLiteObject

class DIDLLiteItem(DIDLLiteObject):
    """
    :Constructors:
    
    ::
    
        DIDLLiteItem(**properties)
    """
    def add_artist(self): # real signature unknown; restored from __doc__
        """ add_artist(self) -> GUPnPAV.DIDLLiteContributor """
        pass

    def add_author(self): # real signature unknown; restored from __doc__
        """ add_author(self) -> GUPnPAV.DIDLLiteContributor """
        pass

    def add_creator(self): # real signature unknown; restored from __doc__
        """ add_creator(self) -> GUPnPAV.DIDLLiteContributor """
        pass

    def add_descriptor(self): # real signature unknown; restored from __doc__
        """ add_descriptor(self) -> GUPnPAV.DIDLLiteDescriptor """
        pass

    def add_resource(self): # real signature unknown; restored from __doc__
        """ add_resource(self) -> GUPnPAV.DIDLLiteResource """
        pass

    def apply_fragments(self, current_fragments, new_fragments): # real signature unknown; restored from __doc__
        """ apply_fragments(self, current_fragments:list, new_fragments:list) -> GUPnPAV.DIDLLiteFragmentResult """
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

    def get_album(self): # real signature unknown; restored from __doc__
        """ get_album(self) -> str """
        return ""

    def get_album_art(self): # real signature unknown; restored from __doc__
        """ get_album_art(self) -> str """
        return ""

    def get_album_xml_string(self): # real signature unknown; restored from __doc__
        """ get_album_xml_string(self) -> str """
        return ""

    def get_artist(self): # real signature unknown; restored from __doc__
        """ get_artist(self) -> str """
        return ""

    def get_artists(self): # real signature unknown; restored from __doc__
        """ get_artists(self) -> list """
        return []

    def get_artists_xml_string(self): # real signature unknown; restored from __doc__
        """ get_artists_xml_string(self) -> str """
        return ""

    def get_author(self): # real signature unknown; restored from __doc__
        """ get_author(self) -> str """
        return ""

    def get_authors(self): # real signature unknown; restored from __doc__
        """ get_authors(self) -> list """
        return []

    def get_compat_resource(self, sink_protocol_info, lenient): # real signature unknown; restored from __doc__
        """ get_compat_resource(self, sink_protocol_info:str, lenient:bool) -> GUPnPAV.DIDLLiteResource """
        pass

    def get_creator(self): # real signature unknown; restored from __doc__
        """ get_creator(self) -> str """
        return ""

    def get_creators(self): # real signature unknown; restored from __doc__
        """ get_creators(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_date(self): # real signature unknown; restored from __doc__
        """ get_date(self) -> str """
        return ""

    def get_date_xml_string(self): # real signature unknown; restored from __doc__
        """ get_date_xml_string(self) -> str """
        return ""

    def get_dc_namespace(self): # real signature unknown; restored from __doc__
        """ get_dc_namespace(self) -> libxml2.NsPtr """
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_descriptors(self): # real signature unknown; restored from __doc__
        """ get_descriptors(self) -> list """
        return []

    def get_dlna_managed(self): # real signature unknown; restored from __doc__
        """ get_dlna_managed(self) -> GUPnPAV.OCMFlags """
        pass

    def get_dlna_namespace(self): # real signature unknown; restored from __doc__
        """ get_dlna_namespace(self) -> libxml2.NsPtr """
        pass

    def get_genre(self): # real signature unknown; restored from __doc__
        """ get_genre(self) -> str """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_lifetime(self): # real signature unknown; restored from __doc__
        """ get_lifetime(self) -> int """
        return 0

    def get_parent_id(self): # real signature unknown; restored from __doc__
        """ get_parent_id(self) -> str """
        return ""

    def get_properties(self, name): # real signature unknown; restored from __doc__
        """ get_properties(self, name:str) -> list """
        return []

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_pv_namespace(self): # real signature unknown; restored from __doc__
        """ get_pv_namespace(self) -> libxml2.NsPtr """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_ref_id(self): # real signature unknown; restored from __doc__
        """ get_ref_id(self) -> str """
        return ""

    def get_resources(self): # real signature unknown; restored from __doc__
        """ get_resources(self) -> list """
        return []

    def get_restricted(self): # real signature unknown; restored from __doc__
        """ get_restricted(self) -> bool """
        return False

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_title_xml_string(self): # real signature unknown; restored from __doc__
        """ get_title_xml_string(self) -> str """
        return ""

    def get_track_number(self): # real signature unknown; restored from __doc__
        """ get_track_number(self) -> int """
        return 0

    def get_track_number_xml_string(self): # real signature unknown; restored from __doc__
        """ get_track_number_xml_string(self) -> str """
        return ""

    def get_update_id(self): # real signature unknown; restored from __doc__
        """ get_update_id(self) -> int """
        return 0

    def get_upnp_class(self): # real signature unknown; restored from __doc__
        """ get_upnp_class(self) -> str """
        return ""

    def get_upnp_class_xml_string(self): # real signature unknown; restored from __doc__
        """ get_upnp_class_xml_string(self) -> str """
        return ""

    def get_upnp_namespace(self): # real signature unknown; restored from __doc__
        """ get_upnp_namespace(self) -> libxml2.NsPtr """
        pass

    def get_write_status(self): # real signature unknown; restored from __doc__
        """ get_write_status(self) -> str """
        return ""

    def get_xml_node(self): # real signature unknown; restored from __doc__
        """ get_xml_node(self) -> libxml2.Node """
        pass

    def get_xml_string(self): # real signature unknown; restored from __doc__
        """ get_xml_string(self) -> str """
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

    def is_restricted_set(self): # real signature unknown; restored from __doc__
        """ is_restricted_set(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
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

    def set_album(self, album): # real signature unknown; restored from __doc__
        """ set_album(self, album:str) """
        pass

    def set_album_art(self, album_art): # real signature unknown; restored from __doc__
        """ set_album_art(self, album_art:str) """
        pass

    def set_artist(self, artist): # real signature unknown; restored from __doc__
        """ set_artist(self, artist:str) """
        pass

    def set_author(self, author): # real signature unknown; restored from __doc__
        """ set_author(self, author:str) """
        pass

    def set_creator(self, creator): # real signature unknown; restored from __doc__
        """ set_creator(self, creator:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_date(self, date): # real signature unknown; restored from __doc__
        """ set_date(self, date:str) """
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_dlna_managed(self, dlna_managed): # real signature unknown; restored from __doc__
        """ set_dlna_managed(self, dlna_managed:GUPnPAV.OCMFlags) """
        pass

    def set_genre(self, genre): # real signature unknown; restored from __doc__
        """ set_genre(self, genre:str) """
        pass

    def set_id(self, id): # real signature unknown; restored from __doc__
        """ set_id(self, id:str) """
        pass

    def set_lifetime(self, lifetime): # real signature unknown; restored from __doc__
        """ set_lifetime(self, lifetime:int) """
        pass

    def set_parent_id(self, parent_id): # real signature unknown; restored from __doc__
        """ set_parent_id(self, parent_id:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_ref_id(self, ref_id): # real signature unknown; restored from __doc__
        """ set_ref_id(self, ref_id:str) """
        pass

    def set_restricted(self, restricted): # real signature unknown; restored from __doc__
        """ set_restricted(self, restricted:bool) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_track_number(self, track_number): # real signature unknown; restored from __doc__
        """ set_track_number(self, track_number:int) """
        pass

    def set_update_id(self, update_id): # real signature unknown; restored from __doc__
        """ set_update_id(self, update_id:int) """
        pass

    def set_upnp_class(self, upnp_class): # real signature unknown; restored from __doc__
        """ set_upnp_class(self, upnp_class:str) """
        pass

    def set_write_status(self, write_status): # real signature unknown; restored from __doc__
        """ set_write_status(self, write_status:str) """
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

    def unset_artists(self): # real signature unknown; restored from __doc__
        """ unset_artists(self) """
        pass

    def unset_update_id(self): # real signature unknown; restored from __doc__
        """ unset_update_id(self) """
        pass

    def update_id_is_set(self): # real signature unknown; restored from __doc__
        """ update_id_is_set(self) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fda4df67760>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DIDLLiteItem), '__module__': 'gi.repository.GUPnPAV', '__gtype__': <GType GUPnPDIDLLiteItem (94653147450944)>, '__doc__': None, '__gsignals__': {}, 'get_lifetime': gi.FunctionInfo(get_lifetime), 'get_ref_id': gi.FunctionInfo(get_ref_id), 'set_lifetime': gi.FunctionInfo(set_lifetime), 'set_ref_id': gi.FunctionInfo(set_ref_id), 'parent': <property object at 0x7fda4e17f450>})"
    __gdoc__ = "Object GUPnPDIDLLiteItem\n\nProperties from GUPnPDIDLLiteItem:\n  ref-id -> gchararray: RefID\n    The ref ID of this item.\n  lifetime -> glong: Lifetime\n    The lifetime (in seconds) of this item.\n\nProperties from GUPnPDIDLLiteObject:\n  xml-node -> gpointer: XMLNode\n    The pointer to object node in XML document.\n  xml-doc -> GUPnPAVXMLDoc: XMLDoc\n    The reference to XML document containing this object.\n  upnp-namespace -> gpointer: XML namespace\n    Pointer to the UPnP XML namespace registered with the XML document containing this object.\n  dc-namespace -> gpointer: XML namespace\n    Pointer to the Dublin Core XML namespace registered with the XML document containing this object.\n  dlna-namespace -> gpointer: XML namespace\n    Pointer to the DLNA metadata namespace registered with the XML document containing this object.\n  pv-namespace -> gpointer: XML namespace\n    Pointer to the PV metadata namespace registered with the XML document containing this object.\n  id -> gchararray: ID\n    The ID of this object.\n  parent-id -> gchararray: ParentID\n    The ID of the parent container of this object.\n  restricted -> gboolean: Restricted\n    Whether this object is restricted.\n  title -> gchararray: Title\n    The title of this object.\n  upnp-class -> gchararray: UPnPClassName\n    The UPnP class of this object.\n  creator -> gchararray: Creator\n    The creator of this object.\n  artist -> gchararray: Artist\n    The artist of this object.\n  author -> gchararray: Author\n    The author of this object.\n  genre -> gchararray: Genre\n    The genre of this object.\n  write-status -> gchararray: WriteStatus\n    The write status of this object.\n  album -> gchararray: Album\n    The album of this object.\n  album-art -> gchararray: AlbumArt\n    The URI to album art of this object.\n  description -> gchararray: Description\n    The description of this object.\n  date -> gchararray: Date\n    The date of this object.\n  track-number -> gint: TrackNumber\n    The original track number of this  object.\n  dlna-managed -> GUPnPOCMFlags: DLNAManaged\n    The 'dlna:dlnaManaged' attribute\n  update-id -> guint: UpdateID\n    Update ID of this object.\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GUPnPDIDLLiteItem (94653147450944)>'
    __info__ = ObjectInfo(DIDLLiteItem)


