# encoding: utf-8
# module gi.repository.Flatpak
# from /usr/lib64/girepository-1.0/Flatpak-1.0.typelib
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


class Remote(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Remote(**properties)
        new(name:str) -> Flatpak.Remote
        new_from_file(name:str, data:GLib.Bytes) -> Flatpak.Remote
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

    def get_appstream_dir(self, arch=None): # real signature unknown; restored from __doc__
        """ get_appstream_dir(self, arch:str=None) -> Gio.File """
        pass

    def get_appstream_timestamp(self, arch=None): # real signature unknown; restored from __doc__
        """ get_appstream_timestamp(self, arch:str=None) -> Gio.File """
        pass

    def get_collection_id(self): # real signature unknown; restored from __doc__
        """ get_collection_id(self) -> str or None """
        return ""

    def get_comment(self): # real signature unknown; restored from __doc__
        """ get_comment(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_branch(self): # real signature unknown; restored from __doc__
        """ get_default_branch(self) -> str """
        return ""

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_disabled(self): # real signature unknown; restored from __doc__
        """ get_disabled(self) -> bool """
        return False

    def get_filter(self): # real signature unknown; restored from __doc__
        """ get_filter(self) -> str """
        return ""

    def get_gpg_verify(self): # real signature unknown; restored from __doc__
        """ get_gpg_verify(self) -> bool """
        return False

    def get_homepage(self): # real signature unknown; restored from __doc__
        """ get_homepage(self) -> str """
        return ""

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> str """
        return ""

    def get_main_ref(self): # real signature unknown; restored from __doc__
        """ get_main_ref(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_nodeps(self): # real signature unknown; restored from __doc__
        """ get_nodeps(self) -> bool """
        return False

    def get_noenumerate(self): # real signature unknown; restored from __doc__
        """ get_noenumerate(self) -> bool """
        return False

    def get_prio(self): # real signature unknown; restored from __doc__
        """ get_prio(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_remote_type(self): # real signature unknown; restored from __doc__
        """ get_remote_type(self) -> Flatpak.RemoteType """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_url(self): # real signature unknown; restored from __doc__
        """ get_url(self) -> str """
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

    def new(self, name): # real signature unknown; restored from __doc__
        """ new(name:str) -> Flatpak.Remote """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_file(self, name, data): # real signature unknown; restored from __doc__
        """ new_from_file(name:str, data:GLib.Bytes) -> Flatpak.Remote """
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

    def set_collection_id(self, collection_id=None): # real signature unknown; restored from __doc__
        """ set_collection_id(self, collection_id:str=None) """
        pass

    def set_comment(self, comment): # real signature unknown; restored from __doc__
        """ set_comment(self, comment:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_branch(self, default_branch): # real signature unknown; restored from __doc__
        """ set_default_branch(self, default_branch:str) """
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_disabled(self, disabled): # real signature unknown; restored from __doc__
        """ set_disabled(self, disabled:bool) """
        pass

    def set_filter(self, filter_path): # real signature unknown; restored from __doc__
        """ set_filter(self, filter_path:str) """
        pass

    def set_gpg_key(self, gpg_key): # real signature unknown; restored from __doc__
        """ set_gpg_key(self, gpg_key:GLib.Bytes) """
        pass

    def set_gpg_verify(self, gpg_verify): # real signature unknown; restored from __doc__
        """ set_gpg_verify(self, gpg_verify:bool) """
        pass

    def set_homepage(self, homepage): # real signature unknown; restored from __doc__
        """ set_homepage(self, homepage:str) """
        pass

    def set_icon(self, icon): # real signature unknown; restored from __doc__
        """ set_icon(self, icon:str) """
        pass

    def set_main_ref(self, main_ref): # real signature unknown; restored from __doc__
        """ set_main_ref(self, main_ref:str) """
        pass

    def set_nodeps(self, nodeps): # real signature unknown; restored from __doc__
        """ set_nodeps(self, nodeps:bool) """
        pass

    def set_noenumerate(self, noenumerate): # real signature unknown; restored from __doc__
        """ set_noenumerate(self, noenumerate:bool) """
        pass

    def set_prio(self, prio): # real signature unknown; restored from __doc__
        """ set_prio(self, prio:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_url(self, url): # real signature unknown; restored from __doc__
        """ set_url(self, url:str) """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f29534f65e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Remote), '__module__': 'gi.repository.Flatpak', '__gtype__': <GType FlatpakRemote (94781644105600)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_file': gi.FunctionInfo(new_from_file), 'get_appstream_dir': gi.FunctionInfo(get_appstream_dir), 'get_appstream_timestamp': gi.FunctionInfo(get_appstream_timestamp), 'get_collection_id': gi.FunctionInfo(get_collection_id), 'get_comment': gi.FunctionInfo(get_comment), 'get_default_branch': gi.FunctionInfo(get_default_branch), 'get_description': gi.FunctionInfo(get_description), 'get_disabled': gi.FunctionInfo(get_disabled), 'get_filter': gi.FunctionInfo(get_filter), 'get_gpg_verify': gi.FunctionInfo(get_gpg_verify), 'get_homepage': gi.FunctionInfo(get_homepage), 'get_icon': gi.FunctionInfo(get_icon), 'get_main_ref': gi.FunctionInfo(get_main_ref), 'get_name': gi.FunctionInfo(get_name), 'get_nodeps': gi.FunctionInfo(get_nodeps), 'get_noenumerate': gi.FunctionInfo(get_noenumerate), 'get_prio': gi.FunctionInfo(get_prio), 'get_remote_type': gi.FunctionInfo(get_remote_type), 'get_title': gi.FunctionInfo(get_title), 'get_url': gi.FunctionInfo(get_url), 'set_collection_id': gi.FunctionInfo(set_collection_id), 'set_comment': gi.FunctionInfo(set_comment), 'set_default_branch': gi.FunctionInfo(set_default_branch), 'set_description': gi.FunctionInfo(set_description), 'set_disabled': gi.FunctionInfo(set_disabled), 'set_filter': gi.FunctionInfo(set_filter), 'set_gpg_key': gi.FunctionInfo(set_gpg_key), 'set_gpg_verify': gi.FunctionInfo(set_gpg_verify), 'set_homepage': gi.FunctionInfo(set_homepage), 'set_icon': gi.FunctionInfo(set_icon), 'set_main_ref': gi.FunctionInfo(set_main_ref), 'set_nodeps': gi.FunctionInfo(set_nodeps), 'set_noenumerate': gi.FunctionInfo(set_noenumerate), 'set_prio': gi.FunctionInfo(set_prio), 'set_title': gi.FunctionInfo(set_title), 'set_url': gi.FunctionInfo(set_url), 'parent': <property object at 0x7f29534eaf40>})"
    __gdoc__ = 'Object FlatpakRemote\n\nProperties from FlatpakRemote:\n  name -> gchararray: Name\n    The name of the remote\n  type -> FlatpakRemoteType: Type\n    The type of the remote\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType FlatpakRemote (94781644105600)>'
    __info__ = ObjectInfo(Remote)


