# encoding: utf-8
# module gi.repository.Unity
# from /usr/lib/girepository-1.0/Unity-7.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Unity as __gi_overrides_Unity
import gi.repository.Dee as __gi_repository_Dee
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class MusicPlayer(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        MusicPlayer(**properties)
        new(desktop:str) -> Unity.MusicPlayer
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
        # no doc
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
        # no doc
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        # no doc
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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

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
        # no doc
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
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

    def __dir__(self): # real signature unknown; restored from __doc__
        """
        __dir__() -> list
        default dir() implementation
        """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ default object formatter """
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
        """ helper for pickle """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """
        __sizeof__() -> int
        size of object in memory, in bytes
        """
        return 0

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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    add_playlist = gi.FunctionInfo(add_playlist)
    edit_playlist_name = gi.FunctionInfo(edit_playlist_name)
    export = gi.FunctionInfo(export)
    getv = gi.FunctionInfo(getv)
    get_app_info = gi.FunctionInfo(get_app_info)
    get_can_go_next = gi.FunctionInfo(get_can_go_next)
    get_can_go_previous = gi.FunctionInfo(get_can_go_previous)
    get_can_pause = gi.FunctionInfo(get_can_pause)
    get_can_play = gi.FunctionInfo(get_can_play)
    get_current_playlist = gi.FunctionInfo(get_current_playlist)
    get_current_track = gi.FunctionInfo(get_current_track)
    get_desktop_file_name = gi.FunctionInfo(get_desktop_file_name)
    get_is_blacklisted = gi.FunctionInfo(get_is_blacklisted)
    get_playback_state = gi.FunctionInfo(get_playback_state)
    get_player_menu = gi.FunctionInfo(get_player_menu)
    get_playlists = gi.FunctionInfo(get_playlists)
    get_title = gi.FunctionInfo(get_title)
    get_track_menu = gi.FunctionInfo(get_track_menu)
    is_floating = gi.FunctionInfo(is_floating)
    new = gi.FunctionInfo(new)
    newv = gi.FunctionInfo(newv)
    notify = gi.FunctionInfo(notify)
    props = None # (!) real value is '<gi._gi.GProps object at 0x7f0cf0f6b160>'
    remove_playlist = gi.FunctionInfo(remove_playlist)
    set_can_go_next = gi.FunctionInfo(set_can_go_next)
    set_can_go_previous = gi.FunctionInfo(set_can_go_previous)
    set_can_pause = gi.FunctionInfo(set_can_pause)
    set_can_play = gi.FunctionInfo(set_can_play)
    set_current_playlist = gi.FunctionInfo(set_current_playlist)
    set_current_track = gi.FunctionInfo(set_current_track)
    set_is_blacklisted = gi.FunctionInfo(set_is_blacklisted)
    set_playback_state = gi.FunctionInfo(set_playback_state)
    set_player_menu = gi.FunctionInfo(set_player_menu)
    set_title = gi.FunctionInfo(set_title)
    set_track_menu = gi.FunctionInfo(set_track_menu)
    thaw_notify = gi.FunctionInfo(thaw_notify)
    unexport = gi.FunctionInfo(unexport)
    _force_floating = gi.FunctionInfo(force_floating)
    _ref = gi.FunctionInfo(ref)
    _ref_sink = gi.FunctionInfo(ref_sink)
    _unref = gi.FunctionInfo(unref)
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MusicPlayer), '__module__': 'gi.repository.Unity', '__gtype__': <GType UnityMusicPlayer (26923920)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'export': gi.FunctionInfo(export), 'unexport': gi.FunctionInfo(unexport), 'add_playlist': gi.FunctionInfo(add_playlist), 'remove_playlist': gi.FunctionInfo(remove_playlist), 'get_playlists': gi.FunctionInfo(get_playlists), 'edit_playlist_name': gi.FunctionInfo(edit_playlist_name), 'get_app_info': gi.FunctionInfo(get_app_info), 'get_desktop_file_name': gi.FunctionInfo(get_desktop_file_name), 'get_is_blacklisted': gi.FunctionInfo(get_is_blacklisted), 'set_is_blacklisted': gi.FunctionInfo(set_is_blacklisted), 'get_title': gi.FunctionInfo(get_title), 'set_title': gi.FunctionInfo(set_title), 'get_can_go_next': gi.FunctionInfo(get_can_go_next), 'set_can_go_next': gi.FunctionInfo(set_can_go_next), 'get_can_go_previous': gi.FunctionInfo(get_can_go_previous), 'set_can_go_previous': gi.FunctionInfo(set_can_go_previous), 'get_can_play': gi.FunctionInfo(get_can_play), 'set_can_play': gi.FunctionInfo(set_can_play), 'get_can_pause': gi.FunctionInfo(get_can_pause), 'set_can_pause': gi.FunctionInfo(set_can_pause), 'get_current_track': gi.FunctionInfo(get_current_track), 'set_current_track': gi.FunctionInfo(set_current_track), 'get_playback_state': gi.FunctionInfo(get_playback_state), 'set_playback_state': gi.FunctionInfo(set_playback_state), 'get_current_playlist': gi.FunctionInfo(get_current_playlist), 'set_current_playlist': gi.FunctionInfo(set_current_playlist), 'get_track_menu': gi.FunctionInfo(get_track_menu), 'set_track_menu': gi.FunctionInfo(set_track_menu), 'get_player_menu': gi.FunctionInfo(get_player_menu), 'set_player_menu': gi.FunctionInfo(set_player_menu), 'parent_instance': <property object at 0x7f0cf0e45958>, 'priv': <property object at 0x7f0cf0e459a8>})"
    __gdoc__ = 'Object UnityMusicPlayer\n\nSignals from UnityMusicPlayer:\n  raise ()\n  play-pause ()\n  previous ()\n  next ()\n  activate-playlist (gchararray)\n\nProperties from UnityMusicPlayer:\n  app-info -> GAppInfo: app-info\n    app-info\n  desktop-file-name -> gchararray: desktop-file-name\n    desktop-file-name\n  is-blacklisted -> gboolean: is-blacklisted\n    is-blacklisted\n  title -> gchararray: title\n    title\n  can-go-next -> gboolean: can-go-next\n    can-go-next\n  can-go-previous -> gboolean: can-go-previous\n    can-go-previous\n  can-play -> gboolean: can-play\n    can-play\n  can-pause -> gboolean: can-pause\n    can-pause\n  current-track -> UnityTrackMetadata: current-track\n    current-track\n  playback-state -> UnityPlaybackState: playback-state\n    playback-state\n  current-playlist -> UnityPlaylist: current-playlist\n    current-playlist\n  track-menu -> DbusmenuMenuitem: track-menu\n    track-menu\n  player-menu -> DbusmenuMenuitem: player-menu\n    player-menu\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UnityMusicPlayer (26923920)>'
    __info__ = ObjectInfo(MusicPlayer)


