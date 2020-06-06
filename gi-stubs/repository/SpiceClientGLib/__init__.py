# encoding: utf-8
# module gi.repository.SpiceClientGLib
# from /usr/lib64/girepository-1.0/SpiceClientGLib-2.0.typelib
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


# Variables with simple values

GTK_MAJOR_VERSION = 0

GTK_MICRO_VERSION = 0

GTK_MINOR_VERSION = 38

_namespace = 'SpiceClientGLib'

_version = '2.0'

__weakref__ = None

# functions

def client_error_quark(): # real signature unknown; restored from __doc__
    """ client_error_quark() -> int """
    return 0

def display_change_preferred_compression(channel, compression): # real signature unknown; restored from __doc__
    """ display_change_preferred_compression(channel:SpiceClientGLib.Channel, compression:int) """
    pass

def display_change_preferred_video_codec_type(channel, codec_type): # real signature unknown; restored from __doc__
    """ display_change_preferred_video_codec_type(channel:SpiceClientGLib.Channel, codec_type:int) """
    pass

def display_get_gl_scanout(channel): # real signature unknown; restored from __doc__
    """ display_get_gl_scanout(channel:SpiceClientGLib.DisplayChannel) -> SpiceClientGLib.GlScanout """
    pass

def display_get_primary(channel, surface_id, primary): # real signature unknown; restored from __doc__
    """ display_get_primary(channel:SpiceClientGLib.Channel, surface_id:int, primary:SpiceClientGLib.DisplayPrimary) -> bool """
    return False

def display_gl_draw_done(channel): # real signature unknown; restored from __doc__
    """ display_gl_draw_done(channel:SpiceClientGLib.DisplayChannel) """
    pass

def get_option_group(): # real signature unknown; restored from __doc__
    """ get_option_group() -> GLib.OptionGroup """
    pass

def inputs_button_press(channel, button, button_state): # real signature unknown; restored from __doc__
    """ inputs_button_press(channel:SpiceClientGLib.InputsChannel, button:int, button_state:int) """
    pass

def inputs_button_release(channel, button, button_state): # real signature unknown; restored from __doc__
    """ inputs_button_release(channel:SpiceClientGLib.InputsChannel, button:int, button_state:int) """
    pass

def inputs_key_press(channel, scancode): # real signature unknown; restored from __doc__
    """ inputs_key_press(channel:SpiceClientGLib.InputsChannel, scancode:int) """
    pass

def inputs_key_press_and_release(channel, scancode): # real signature unknown; restored from __doc__
    """ inputs_key_press_and_release(channel:SpiceClientGLib.InputsChannel, scancode:int) """
    pass

def inputs_key_release(channel, scancode): # real signature unknown; restored from __doc__
    """ inputs_key_release(channel:SpiceClientGLib.InputsChannel, scancode:int) """
    pass

def inputs_motion(channel, dx, dy, button_state): # real signature unknown; restored from __doc__
    """ inputs_motion(channel:SpiceClientGLib.InputsChannel, dx:int, dy:int, button_state:int) """
    pass

def inputs_position(channel, x, y, display, button_state): # real signature unknown; restored from __doc__
    """ inputs_position(channel:SpiceClientGLib.InputsChannel, x:int, y:int, display:int, button_state:int) """
    pass

def inputs_set_key_locks(channel, locks): # real signature unknown; restored from __doc__
    """ inputs_set_key_locks(channel:SpiceClientGLib.InputsChannel, locks:int) """
    pass

def main_agent_test_capability(channel, cap): # real signature unknown; restored from __doc__
    """ main_agent_test_capability(channel:SpiceClientGLib.MainChannel, cap:int) -> bool """
    return False

def main_clipboard_grab(channel, types, ntypes): # real signature unknown; restored from __doc__
    """ main_clipboard_grab(channel:SpiceClientGLib.MainChannel, types:int, ntypes:int) """
    pass

def main_clipboard_notify(channel, type, data, size): # real signature unknown; restored from __doc__
    """ main_clipboard_notify(channel:SpiceClientGLib.MainChannel, type:int, data:int, size:int) """
    pass

def main_clipboard_release(channel): # real signature unknown; restored from __doc__
    """ main_clipboard_release(channel:SpiceClientGLib.MainChannel) """
    pass

def main_clipboard_request(channel, type): # real signature unknown; restored from __doc__
    """ main_clipboard_request(channel:SpiceClientGLib.MainChannel, type:int) """
    pass

def main_clipboard_selection_grab(channel, selection, types, ntypes): # real signature unknown; restored from __doc__
    """ main_clipboard_selection_grab(channel:SpiceClientGLib.MainChannel, selection:int, types:int, ntypes:int) """
    pass

def main_clipboard_selection_notify(channel, selection, type, data, size): # real signature unknown; restored from __doc__
    """ main_clipboard_selection_notify(channel:SpiceClientGLib.MainChannel, selection:int, type:int, data:int, size:int) """
    pass

def main_clipboard_selection_release(channel, selection): # real signature unknown; restored from __doc__
    """ main_clipboard_selection_release(channel:SpiceClientGLib.MainChannel, selection:int) """
    pass

def main_clipboard_selection_request(channel, selection, type): # real signature unknown; restored from __doc__
    """ main_clipboard_selection_request(channel:SpiceClientGLib.MainChannel, selection:int, type:int) """
    pass

def main_file_copy_async(channel, sources, flags, cancellable=None, progress_callback=None, progress_callback_data=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ main_file_copy_async(channel:SpiceClientGLib.MainChannel, sources:list, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileProgressCallback=None, progress_callback_data=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def main_file_copy_finish(channel, result): # real signature unknown; restored from __doc__
    """ main_file_copy_finish(channel:SpiceClientGLib.MainChannel, result:Gio.AsyncResult) -> bool """
    return False

def main_request_mouse_mode(channel, mode): # real signature unknown; restored from __doc__
    """ main_request_mouse_mode(channel:SpiceClientGLib.MainChannel, mode:int) """
    pass

def main_send_monitor_config(channel): # real signature unknown; restored from __doc__
    """ main_send_monitor_config(channel:SpiceClientGLib.MainChannel) -> bool """
    return False

def main_set_display(channel, id, x, y, width, height): # real signature unknown; restored from __doc__
    """ main_set_display(channel:SpiceClientGLib.MainChannel, id:int, x:int, y:int, width:int, height:int) """
    pass

def main_set_display_enabled(channel, id, enabled): # real signature unknown; restored from __doc__
    """ main_set_display_enabled(channel:SpiceClientGLib.MainChannel, id:int, enabled:bool) """
    pass

def main_update_display(channel, id, x, y, width, height, update): # real signature unknown; restored from __doc__
    """ main_update_display(channel:SpiceClientGLib.MainChannel, id:int, x:int, y:int, width:int, height:int, update:bool) """
    pass

def main_update_display_enabled(channel, id, enabled, update): # real signature unknown; restored from __doc__
    """ main_update_display_enabled(channel:SpiceClientGLib.MainChannel, id:int, enabled:bool, update:bool) """
    pass

def port_event(port, event): # real signature unknown; restored from __doc__
    """ port_event(port:SpiceClientGLib.PortChannel, event:int) """
    pass

def port_write_async(port, buffer, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ port_write_async(port:SpiceClientGLib.PortChannel, buffer:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def port_write_finish(port, result): # real signature unknown; restored from __doc__
    """ port_write_finish(port:SpiceClientGLib.PortChannel, result:Gio.AsyncResult) -> int """
    return 0

def record_send_data(channel, data=None, bytes, time): # real signature unknown; restored from __doc__
    """ record_send_data(channel:SpiceClientGLib.RecordChannel, data=None, bytes:int, time:int) """
    pass

def set_session_option(session): # real signature unknown; restored from __doc__
    """ set_session_option(session:SpiceClientGLib.Session) """
    pass

def util_get_debug(): # real signature unknown; restored from __doc__
    """ util_get_debug() -> bool """
    return False

def util_get_version_string(): # real signature unknown; restored from __doc__
    """ util_get_version_string() -> str """
    return ""

def util_set_debug(enabled): # real signature unknown; restored from __doc__
    """ util_set_debug(enabled:bool) """
    pass

def uuid_to_string(uuid): # real signature unknown; restored from __doc__
    """ uuid_to_string(uuid:int) -> str """
    return ""

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

from .Audio import Audio
from .AudioClass import AudioClass
from .AudioPrivate import AudioPrivate
from .Channel import Channel
from .ChannelClass import ChannelClass
from .ChannelClassPrivate import ChannelClassPrivate
from .ChannelEvent import ChannelEvent
from .ChannelPrivate import ChannelPrivate
from .ClientError import ClientError
from .CursorChannel import CursorChannel
from .CursorChannelClass import CursorChannelClass
from .CursorChannelPrivate import CursorChannelPrivate
from .CursorShape import CursorShape
from .DisplayChannel import DisplayChannel
from .DisplayChannelClass import DisplayChannelClass
from .DisplayChannelPrivate import DisplayChannelPrivate
from .DisplayMonitorConfig import DisplayMonitorConfig
from .DisplayPrimary import DisplayPrimary
from .FileTransferTask import FileTransferTask
from .FileTransferTaskClass import FileTransferTaskClass
from .GlScanout import GlScanout
from .InputsChannel import InputsChannel
from .InputsChannelClass import InputsChannelClass
from .InputsChannelPrivate import InputsChannelPrivate
from .InputsLock import InputsLock
from .MainChannel import MainChannel
from .MainChannelClass import MainChannelClass
from .MainChannelPrivate import MainChannelPrivate
from .MsgIn import MsgIn
from .MsgOut import MsgOut
from .PlaybackChannel import PlaybackChannel
from .PlaybackChannelClass import PlaybackChannelClass
from .PlaybackChannelPrivate import PlaybackChannelPrivate
from .PortChannel import PortChannel
from .PortChannelClass import PortChannelClass
from .PortChannelPrivate import PortChannelPrivate
from .QmpPort import QmpPort
from .QmpPortClass import QmpPortClass
from .QmpPortVmAction import QmpPortVmAction
from .QmpStatus import QmpStatus
from .RecordChannel import RecordChannel
from .RecordChannelClass import RecordChannelClass
from .RecordChannelPrivate import RecordChannelPrivate
from .Session import Session
from .SessionClass import SessionClass
from .SessionMigration import SessionMigration
from .SessionPrivate import SessionPrivate
from .SessionVerify import SessionVerify
from .SmartcardChannel import SmartcardChannel
from .SmartcardChannelClass import SmartcardChannelClass
from .SmartcardChannelPrivate import SmartcardChannelPrivate
from .SmartcardManager import SmartcardManager
from .SmartcardManagerClass import SmartcardManagerClass
from .SmartcardManagerPrivate import SmartcardManagerPrivate
from .SmartcardReader import SmartcardReader
from .URI import URI
from .URIClass import URIClass
from .URIPrivate import URIPrivate
from .UsbDevice import UsbDevice
from .UsbDeviceManager import UsbDeviceManager
from .UsbDeviceManagerClass import UsbDeviceManagerClass
from .UsbDeviceManagerPrivate import UsbDeviceManagerPrivate
from .UsbredirChannel import UsbredirChannel
from .UsbredirChannelClass import UsbredirChannelClass
from .UsbredirChannelPrivate import UsbredirChannelPrivate
from .VReader import VReader
from .WebdavChannel import WebdavChannel
from .WebdavChannelClass import WebdavChannelClass
from .WebdavChannelPrivate import WebdavChannelPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f9dcf586d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/SpiceClientGLib-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.SpiceClientGLib', loader=<gi.importer.DynamicImporter object at 0x7f9dcf586d00>)"

