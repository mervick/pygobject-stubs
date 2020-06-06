# encoding: utf-8
# module gi.repository.RygelRenderer
# from /usr/lib64/girepository-1.0/RygelRenderer-2.6.typelib
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
import gi.repository.RygelCore as __gi_repository_RygelCore
import gobject as __gobject


# Variables with simple values

_namespace = 'RygelRenderer'

_version = '2.6'

__weakref__ = None

# functions

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

class MediaPlayer(__gobject.GInterface):
    # no doc
    def get_allowed_playback_speeds(self): # real signature unknown; restored from __doc__
        """ get_allowed_playback_speeds(self) -> list, result_length1:int """
        return []

    def get_byte_position(self): # real signature unknown; restored from __doc__
        """ get_byte_position(self) -> int """
        return 0

    def get_can_seek(self): # real signature unknown; restored from __doc__
        """ get_can_seek(self) -> bool """
        return False

    def get_can_seek_bytes(self): # real signature unknown; restored from __doc__
        """ get_can_seek_bytes(self) -> bool """
        return False

    def get_content_features(self): # real signature unknown; restored from __doc__
        """ get_content_features(self) -> str """
        return ""

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> int """
        return 0

    def get_duration_as_str(self): # real signature unknown; restored from __doc__
        """ get_duration_as_str(self) -> str """
        return ""

    def get_metadata(self): # real signature unknown; restored from __doc__
        """ get_metadata(self) -> str """
        return ""

    def get_mime_type(self): # real signature unknown; restored from __doc__
        """ get_mime_type(self) -> str """
        return ""

    def get_mime_types(self): # real signature unknown; restored from __doc__
        """ get_mime_types(self) -> list, result_length1:int """
        return []

    def get_playback_speed(self): # real signature unknown; restored from __doc__
        """ get_playback_speed(self) -> str """
        return ""

    def get_playback_state(self): # real signature unknown; restored from __doc__
        """ get_playback_state(self) -> str """
        return ""

    def get_position(self): # real signature unknown; restored from __doc__
        """ get_position(self) -> int """
        return 0

    def get_position_as_str(self): # real signature unknown; restored from __doc__
        """ get_position_as_str(self) -> str """
        return ""

    def get_protocols(self): # real signature unknown; restored from __doc__
        """ get_protocols(self) -> list, result_length1:int """
        return []

    def get_protocol_info(self): # real signature unknown; restored from __doc__
        """ get_protocol_info(self) -> str """
        return ""

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def get_user_agent(self): # real signature unknown; restored from __doc__
        """ get_user_agent(self) -> str """
        return ""

    def get_volume(self): # real signature unknown; restored from __doc__
        """ get_volume(self) -> float """
        return 0.0

    def play_speed_to_double(self, speed): # real signature unknown; restored from __doc__
        """ play_speed_to_double(self, speed:str) -> float """
        return 0.0

    def seek(self, time): # real signature unknown; restored from __doc__
        """ seek(self, time:int) -> bool """
        return False

    def seek_bytes(self, bytes): # real signature unknown; restored from __doc__
        """ seek_bytes(self, bytes:int) -> bool """
        return False

    def set_content_features(self, value=None): # real signature unknown; restored from __doc__
        """ set_content_features(self, value:str=None) """
        pass

    def set_metadata(self, value=None): # real signature unknown; restored from __doc__
        """ set_metadata(self, value:str=None) """
        pass

    def set_mime_type(self, value=None): # real signature unknown; restored from __doc__
        """ set_mime_type(self, value:str=None) """
        pass

    def set_playback_speed(self, value): # real signature unknown; restored from __doc__
        """ set_playback_speed(self, value:str) """
        pass

    def set_playback_state(self, value): # real signature unknown; restored from __doc__
        """ set_playback_state(self, value:str) """
        pass

    def set_uri(self, value=None): # real signature unknown; restored from __doc__
        """ set_uri(self, value:str=None) """
        pass

    def set_user_agent(self, value=None): # real signature unknown; restored from __doc__
        """ set_user_agent(self, value:str=None) """
        pass

    def set_volume(self, value): # real signature unknown; restored from __doc__
        """ set_volume(self, value:float) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(MediaPlayer), '__module__': 'gi.repository.RygelRenderer', '__gtype__': <GType RygelMediaPlayer (94146099905216)>, '__dict__': <attribute '__dict__' of 'MediaPlayer' objects>, '__weakref__': <attribute '__weakref__' of 'MediaPlayer' objects>, '__doc__': None, '__gsignals__': {}, 'seek': gi.FunctionInfo(seek), 'seek_bytes': gi.FunctionInfo(seek_bytes), 'get_protocols': gi.FunctionInfo(get_protocols), 'get_mime_types': gi.FunctionInfo(get_mime_types), 'play_speed_to_double': gi.FunctionInfo(play_speed_to_double), 'get_playback_state': gi.FunctionInfo(get_playback_state), 'set_playback_state': gi.FunctionInfo(set_playback_state), 'get_allowed_playback_speeds': gi.FunctionInfo(get_allowed_playback_speeds), 'get_playback_speed': gi.FunctionInfo(get_playback_speed), 'set_playback_speed': gi.FunctionInfo(set_playback_speed), 'get_uri': gi.FunctionInfo(get_uri), 'set_uri': gi.FunctionInfo(set_uri), 'get_volume': gi.FunctionInfo(get_volume), 'set_volume': gi.FunctionInfo(set_volume), 'get_duration': gi.FunctionInfo(get_duration), 'get_size': gi.FunctionInfo(get_size), 'get_metadata': gi.FunctionInfo(get_metadata), 'set_metadata': gi.FunctionInfo(set_metadata), 'get_mime_type': gi.FunctionInfo(get_mime_type), 'set_mime_type': gi.FunctionInfo(set_mime_type), 'get_can_seek': gi.FunctionInfo(get_can_seek), 'get_can_seek_bytes': gi.FunctionInfo(get_can_seek_bytes), 'get_content_features': gi.FunctionInfo(get_content_features), 'set_content_features': gi.FunctionInfo(set_content_features), 'get_duration_as_str': gi.FunctionInfo(get_duration_as_str), 'get_position': gi.FunctionInfo(get_position), 'get_byte_position': gi.FunctionInfo(get_byte_position), 'get_position_as_str': gi.FunctionInfo(get_position_as_str), 'get_user_agent': gi.FunctionInfo(get_user_agent), 'set_user_agent': gi.FunctionInfo(set_user_agent), 'get_protocol_info': gi.FunctionInfo(get_protocol_info)})"
    __gdoc__ = 'Interface RygelMediaPlayer\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType RygelMediaPlayer (94146099905216)>'
    __info__ = InterfaceInfo(MediaPlayer)


class MediaPlayerIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MediaPlayerIface()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    get_allowed_playback_speeds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_byte_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_can_seek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_can_seek_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_content_features = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_duration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mime_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mime_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_playback_speed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_playback_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_protocols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_user_agent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seek_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_content_features = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_mime_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_playback_speed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_playback_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_user_agent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MediaPlayerIface), '__module__': 'gi.repository.RygelRenderer', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MediaPlayerIface' objects>, '__weakref__': <attribute '__weakref__' of 'MediaPlayerIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7ff6158bdb30>, 'seek': <property object at 0x7ff6158bdb80>, 'seek_bytes': <property object at 0x7ff6158bdbd0>, 'get_protocols': <property object at 0x7ff6158bdc20>, 'get_mime_types': <property object at 0x7ff61585e900>, 'get_playback_state': <property object at 0x7ff61585ea90>, 'set_playback_state': <property object at 0x7ff61585e6d0>, 'get_allowed_playback_speeds': <property object at 0x7ff61587b8b0>, 'get_playback_speed': <property object at 0x7ff61587b9f0>, 'set_playback_speed': <property object at 0x7ff61587bae0>, 'get_uri': <property object at 0x7ff61587bb80>, 'set_uri': <property object at 0x7ff61587bc70>, 'get_volume': <property object at 0x7ff61587bd60>, 'set_volume': <property object at 0x7ff61587be50>, 'get_duration': <property object at 0x7ff61587bf40>, 'get_size': <property object at 0x7ff61584c090>, 'get_metadata': <property object at 0x7ff61584c180>, 'set_metadata': <property object at 0x7ff61584c270>, 'get_mime_type': <property object at 0x7ff61584c360>, 'set_mime_type': <property object at 0x7ff61584c450>, 'get_can_seek': <property object at 0x7ff61584c540>, 'get_can_seek_bytes': <property object at 0x7ff61584c680>, 'get_content_features': <property object at 0x7ff61584c770>, 'set_content_features': <property object at 0x7ff61584c860>, 'get_position': <property object at 0x7ff61584c900>, 'get_byte_position': <property object at 0x7ff61584ca40>, 'get_user_agent': <property object at 0x7ff61584cae0>, 'set_user_agent': <property object at 0x7ff61584cbd0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MediaPlayerIface)


class MediaRenderer(__gi_repository_RygelCore.MediaDevice):
    """
    :Constructors:
    
    ::
    
        MediaRenderer(**properties)
        new(title:str, player:RygelRenderer.MediaPlayer, capabilities:RygelCore.PluginCapabilities) -> RygelRenderer.MediaRenderer
    """
    def add_interface(self, iface): # real signature unknown; restored from __doc__
        """ add_interface(self, iface:str) """
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

    def get_capabilities(self): # real signature unknown; restored from __doc__
        """ get_capabilities(self) -> RygelCore.PluginCapabilities """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_interfaces(self): # real signature unknown; restored from __doc__
        """ get_interfaces(self) -> list """
        return []

    def get_plugin(self): # real signature unknown; restored from __doc__
        """ get_plugin(self) -> RygelCore.Plugin """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
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

    def new(self, title, player, capabilities): # real signature unknown; restored from __doc__
        """ new(title:str, player:RygelRenderer.MediaPlayer, capabilities:RygelCore.PluginCapabilities) -> RygelRenderer.MediaRenderer """
        pass

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

    def remove_interface(self, iface): # real signature unknown; restored from __doc__
        """ remove_interface(self, iface:str) """
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

    def set_plugin(self, value): # real signature unknown; restored from __doc__
        """ set_plugin(self, value:RygelCore.Plugin) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ff61582af70>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MediaRenderer), '__module__': 'gi.repository.RygelRenderer', '__gtype__': <GType RygelMediaRenderer (94146100005616)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent_instance': <property object at 0x7ff61584d0e0>, 'priv': <property object at 0x7ff61584d1d0>})"
    __gdoc__ = 'Object RygelMediaRenderer\n\nProperties from RygelMediaRenderer:\n  player -> RygelMediaPlayer: player\n    player\n\nProperties from RygelMediaDevice:\n  plugin -> RygelPlugin: plugin\n    plugin\n  title -> gchararray: title\n    title\n  capabilities -> RygelPluginCapabilities: capabilities\n    capabilities\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType RygelMediaRenderer (94146100005616)>'
    __info__ = ObjectInfo(MediaRenderer)


class MediaRendererClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MediaRendererClass()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MediaRendererClass), '__module__': 'gi.repository.RygelRenderer', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MediaRendererClass' objects>, '__weakref__': <attribute '__weakref__' of 'MediaRendererClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ff61584d360>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MediaRendererClass)


class MediaRendererPlugin(__gi_repository_RygelCore.Plugin):
    """
    :Constructors:
    
    ::
    
        MediaRendererPlugin(**properties)
        new(name:str, title:str=None, description:str=None, capabilities:RygelCore.PluginCapabilities) -> RygelRenderer.MediaRendererPlugin
    """
    def add_icon(self, icon_info): # real signature unknown; restored from __doc__
        """ add_icon(self, icon_info:RygelCore.IconInfo) """
        pass

    def add_resource(self, resource_info): # real signature unknown; restored from __doc__
        """ add_resource(self, resource_info:RygelCore.ResourceInfo) """
        pass

    def apply_hacks(self, device, description_path): # real signature unknown; restored from __doc__
        """ apply_hacks(self, device:RygelCore.RootDevice, description_path:str) """
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

    def do_apply_hacks(self, *args, **kwargs): # real signature unknown
        """ apply_hacks(self, device:RygelCore.RootDevice, description_path:str) """
        pass

    def do_get_player(self, *args, **kwargs): # real signature unknown
        """ get_player(self) -> RygelRenderer.MediaPlayer """
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

    def get_active(self): # real signature unknown; restored from __doc__
        """ get_active(self) -> bool """
        return False

    def get_capabilities(self): # real signature unknown; restored from __doc__
        """ get_capabilities(self) -> RygelCore.PluginCapabilities """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> GUPnP.ResourceFactory """
        pass

    def get_default_icons(self): # real signature unknown; restored from __doc__
        """ get_default_icons(self) -> Gee.ArrayList """
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_desc_path(self): # real signature unknown; restored from __doc__
        """ get_desc_path(self) -> str """
        return ""

    def get_icon_infos(self): # real signature unknown; restored from __doc__
        """ get_icon_infos(self) -> Gee.ArrayList """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_player(self): # real signature unknown; restored from __doc__
        """ get_player(self) -> RygelRenderer.MediaPlayer """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol_info(self): # real signature unknown; restored from __doc__
        """ get_protocol_info(self) -> str """
        return ""

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_resource_infos(self): # real signature unknown; restored from __doc__
        """ get_resource_infos(self) -> Gee.ArrayList """
        pass

    def get_supported_profiles(self): # real signature unknown; restored from __doc__
        """ get_supported_profiles(self) -> list """
        return []

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
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

    def new(self, name, title=None, description=None, capabilities): # real signature unknown; restored from __doc__
        """ new(name:str, title:str=None, description:str=None, capabilities:RygelCore.PluginCapabilities) -> RygelRenderer.MediaRendererPlugin """
        pass

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

    def register_resource_proxy_type(self, upnp_type, type): # real signature unknown; restored from __doc__
        """ register_resource_proxy_type(self, upnp_type:str, type:GType) """
        pass

    def register_resource_type(self, upnp_type, type): # real signature unknown; restored from __doc__
        """ register_resource_type(self, upnp_type:str, type:GType) """
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

    def set_active(self, value): # real signature unknown; restored from __doc__
        """ set_active(self, value:bool) """
        pass

    def set_capabilities(self, value): # real signature unknown; restored from __doc__
        """ set_capabilities(self, value:RygelCore.PluginCapabilities) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_supported_profiles(self, value): # real signature unknown; restored from __doc__
        """ set_supported_profiles(self, value:list) """
        pass

    def set_title(self, value): # real signature unknown; restored from __doc__
        """ set_title(self, value:str) """
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

    def unregister_resource_proxy_type(self, upnp_type): # real signature unknown; restored from __doc__
        """ unregister_resource_proxy_type(self, upnp_type:str) -> bool """
        return False

    def unregister_resource_type(self, upnp_type): # real signature unknown; restored from __doc__
        """ unregister_resource_type(self, upnp_type:str) -> bool """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ff61581fc40>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MediaRendererPlugin), '__module__': 'gi.repository.RygelRenderer', '__gtype__': <GType RygelMediaRendererPlugin (94146099922208)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_player': gi.FunctionInfo(get_player), 'get_protocol_info': gi.FunctionInfo(get_protocol_info), 'get_supported_profiles': gi.FunctionInfo(get_supported_profiles), 'set_supported_profiles': gi.FunctionInfo(set_supported_profiles), 'do_get_player': gi.VFuncInfo(get_player), 'parent_instance': <property object at 0x7ff61584dcc0>, 'priv': <property object at 0x7ff61584ddb0>})"
    __gdoc__ = 'Object RygelMediaRendererPlugin\n\nProperties from RygelMediaRendererPlugin:\n  supported-profiles -> gpointer: supported-profiles\n    supported-profiles\n\nProperties from RygelPlugin:\n  capabilities -> RygelPluginCapabilities: capabilities\n    capabilities\n  name -> gchararray: name\n    name\n  title -> gchararray: title\n    title\n  description -> gchararray: description\n    description\n  desc-path -> gchararray: desc-path\n    desc-path\n  active -> gboolean: active\n    active\n  resource-infos -> GeeArrayList: resource-infos\n    resource-infos\n  icon-infos -> GeeArrayList: icon-infos\n    icon-infos\n  default-icons -> GeeArrayList: default-icons\n    default-icons\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType RygelMediaRendererPlugin (94146099922208)>'
    __info__ = ObjectInfo(MediaRendererPlugin)


class MediaRendererPluginClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MediaRendererPluginClass()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    get_controller = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_player = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MediaRendererPluginClass), '__module__': 'gi.repository.RygelRenderer', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MediaRendererPluginClass' objects>, '__weakref__': <attribute '__weakref__' of 'MediaRendererPluginClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ff61584df40>, 'get_player': <property object at 0x7ff61584f090>, 'get_controller': <property object at 0x7ff61584f180>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MediaRendererPluginClass)


class MediaRendererPluginPrivate(__gi.Struct):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MediaRendererPluginPrivate), '__module__': 'gi.repository.RygelRenderer', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MediaRendererPluginPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'MediaRendererPluginPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MediaRendererPluginPrivate)


class MediaRendererPrivate(__gi.Struct):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MediaRendererPrivate), '__module__': 'gi.repository.RygelRenderer', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MediaRendererPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'MediaRendererPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MediaRendererPrivate)


class PlayerController(__gobject.GInterface):
    # no doc
    def get_can_pause(self): # real signature unknown; restored from __doc__
        """ get_can_pause(self) -> bool """
        return False

    def get_current_transport_actions(self): # real signature unknown; restored from __doc__
        """ get_current_transport_actions(self) -> str """
        return ""

    def get_metadata(self): # real signature unknown; restored from __doc__
        """ get_metadata(self) -> str """
        return ""

    def get_next_metadata(self): # real signature unknown; restored from __doc__
        """ get_next_metadata(self) -> str """
        return ""

    def get_next_uri(self): # real signature unknown; restored from __doc__
        """ get_next_uri(self) -> str """
        return ""

    def get_n_tracks(self): # real signature unknown; restored from __doc__
        """ get_n_tracks(self) -> int """
        return 0

    def get_playback_state(self): # real signature unknown; restored from __doc__
        """ get_playback_state(self) -> str """
        return ""

    def get_play_mode(self): # real signature unknown; restored from __doc__
        """ get_play_mode(self) -> str """
        return ""

    def get_track(self): # real signature unknown; restored from __doc__
        """ get_track(self) -> int """
        return 0

    def get_track_metadata(self): # real signature unknown; restored from __doc__
        """ get_track_metadata(self) -> str """
        return ""

    def get_track_uri(self): # real signature unknown; restored from __doc__
        """ get_track_uri(self) -> str """
        return ""

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def is_play_mode_valid(self, play_mode): # real signature unknown; restored from __doc__
        """ is_play_mode_valid(self, play_mode:str) -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool """
        return False

    def previous(self): # real signature unknown; restored from __doc__
        """ previous(self) -> bool """
        return False

    def set_metadata(self, value): # real signature unknown; restored from __doc__
        """ set_metadata(self, value:str) """
        pass

    def set_next_metadata(self, value): # real signature unknown; restored from __doc__
        """ set_next_metadata(self, value:str) """
        pass

    def set_next_playlist_uri(self, uri, metadata, collection): # real signature unknown; restored from __doc__
        """ set_next_playlist_uri(self, uri:str, metadata:str, collection:GUPnPAV.MediaCollection) """
        pass

    def set_next_single_play_uri(self, uri, metadata, mime=None, features=None): # real signature unknown; restored from __doc__
        """ set_next_single_play_uri(self, uri:str, metadata:str, mime:str=None, features:str=None) """
        pass

    def set_next_uri(self, value): # real signature unknown; restored from __doc__
        """ set_next_uri(self, value:str) """
        pass

    def set_n_tracks(self, value): # real signature unknown; restored from __doc__
        """ set_n_tracks(self, value:int) """
        pass

    def set_playback_state(self, value): # real signature unknown; restored from __doc__
        """ set_playback_state(self, value:str) """
        pass

    def set_playlist_uri(self, uri, metadata, collection): # real signature unknown; restored from __doc__
        """ set_playlist_uri(self, uri:str, metadata:str, collection:GUPnPAV.MediaCollection) """
        pass

    def set_play_mode(self, value): # real signature unknown; restored from __doc__
        """ set_play_mode(self, value:str) """
        pass

    def set_single_play_uri(self, uri, metadata, mime=None, features=None): # real signature unknown; restored from __doc__
        """ set_single_play_uri(self, uri:str, metadata:str, mime:str=None, features:str=None) """
        pass

    def set_track(self, value): # real signature unknown; restored from __doc__
        """ set_track(self, value:int) """
        pass

    def set_track_metadata(self, value): # real signature unknown; restored from __doc__
        """ set_track_metadata(self, value:str) """
        pass

    def set_track_uri(self, value): # real signature unknown; restored from __doc__
        """ set_track_uri(self, value:str) """
        pass

    def set_uri(self, value): # real signature unknown; restored from __doc__
        """ set_uri(self, value:str) """
        pass

    def unescape(self, input): # real signature unknown; restored from __doc__
        """ unescape(self, input:str) -> str """
        return ""

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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(PlayerController), '__module__': 'gi.repository.RygelRenderer', '__gtype__': <GType RygelPlayerController (94146100040272)>, '__dict__': <attribute '__dict__' of 'PlayerController' objects>, '__weakref__': <attribute '__weakref__' of 'PlayerController' objects>, '__doc__': None, '__gsignals__': {}, 'next': gi.FunctionInfo(next), 'previous': gi.FunctionInfo(previous), 'set_single_play_uri': gi.FunctionInfo(set_single_play_uri), 'set_playlist_uri': gi.FunctionInfo(set_playlist_uri), 'set_next_single_play_uri': gi.FunctionInfo(set_next_single_play_uri), 'set_next_playlist_uri': gi.FunctionInfo(set_next_playlist_uri), 'is_play_mode_valid': gi.FunctionInfo(is_play_mode_valid), 'unescape': gi.FunctionInfo(unescape), 'get_playback_state': gi.FunctionInfo(get_playback_state), 'set_playback_state': gi.FunctionInfo(set_playback_state), 'get_n_tracks': gi.FunctionInfo(get_n_tracks), 'set_n_tracks': gi.FunctionInfo(set_n_tracks), 'get_track': gi.FunctionInfo(get_track), 'set_track': gi.FunctionInfo(set_track), 'get_uri': gi.FunctionInfo(get_uri), 'set_uri': gi.FunctionInfo(set_uri), 'get_metadata': gi.FunctionInfo(get_metadata), 'set_metadata': gi.FunctionInfo(set_metadata), 'get_track_uri': gi.FunctionInfo(get_track_uri), 'set_track_uri': gi.FunctionInfo(set_track_uri), 'get_track_metadata': gi.FunctionInfo(get_track_metadata), 'set_track_metadata': gi.FunctionInfo(set_track_metadata), 'get_next_uri': gi.FunctionInfo(get_next_uri), 'set_next_uri': gi.FunctionInfo(set_next_uri), 'get_next_metadata': gi.FunctionInfo(get_next_metadata), 'set_next_metadata': gi.FunctionInfo(set_next_metadata), 'get_current_transport_actions': gi.FunctionInfo(get_current_transport_actions), 'get_play_mode': gi.FunctionInfo(get_play_mode), 'set_play_mode': gi.FunctionInfo(set_play_mode), 'get_can_pause': gi.FunctionInfo(get_can_pause)})"
    __gdoc__ = 'Interface RygelPlayerController\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType RygelPlayerController (94146100040272)>'
    __info__ = InterfaceInfo(PlayerController)


class PlayerControllerIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        PlayerControllerIface()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    get_can_pause = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_current_transport_actions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_next_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_next_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_tracks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_playback_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_play_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_track = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_track_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_track_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_play_mode_valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    previous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_next_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_next_playlist_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_next_single_play_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_next_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_n_tracks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_playback_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_playlist_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_play_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_single_play_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_track = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_track_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_track_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PlayerControllerIface), '__module__': 'gi.repository.RygelRenderer', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PlayerControllerIface' objects>, '__weakref__': <attribute '__weakref__' of 'PlayerControllerIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7ff61584f810>, 'next': <property object at 0x7ff61584f900>, 'previous': <property object at 0x7ff61584f9f0>, 'set_single_play_uri': <property object at 0x7ff61584fb30>, 'set_playlist_uri': <property object at 0x7ff61584fc20>, 'set_next_single_play_uri': <property object at 0x7ff61584fd10>, 'set_next_playlist_uri': <property object at 0x7ff61584fe00>, 'is_play_mode_valid': <property object at 0x7ff61584fef0>, 'get_playback_state': <property object at 0x7ff615853040>, 'set_playback_state': <property object at 0x7ff615853130>, 'get_n_tracks': <property object at 0x7ff6158531d0>, 'set_n_tracks': <property object at 0x7ff6158532c0>, 'get_track': <property object at 0x7ff6158533b0>, 'set_track': <property object at 0x7ff6158534a0>, 'get_uri': <property object at 0x7ff615853590>, 'set_uri': <property object at 0x7ff615853680>, 'get_metadata': <property object at 0x7ff615853770>, 'set_metadata': <property object at 0x7ff615853860>, 'get_track_uri': <property object at 0x7ff615853950>, 'set_track_uri': <property object at 0x7ff615853a40>, 'get_track_metadata': <property object at 0x7ff615853b80>, 'set_track_metadata': <property object at 0x7ff615853c70>, 'get_next_uri': <property object at 0x7ff615853d10>, 'set_next_uri': <property object at 0x7ff615853e00>, 'get_next_metadata': <property object at 0x7ff615853f40>, 'set_next_metadata': <property object at 0x7ff615854090>, 'get_current_transport_actions': <property object at 0x7ff615854180>, 'get_play_mode': <property object at 0x7ff615854220>, 'set_play_mode': <property object at 0x7ff615854310>, 'get_can_pause': <property object at 0x7ff615854400>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PlayerControllerIface)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7ff615abf1f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7ff615abf280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7ff615abf310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7ff615abf3a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7ff6166fbd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/RygelRenderer-2.6.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.RygelRenderer', loader=<gi.importer.DynamicImporter object at 0x7ff6166fbd00>)"

