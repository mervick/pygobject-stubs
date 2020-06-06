# encoding: utf-8
# module gi.repository.GdkX11
# from /usr/lib64/girepository-1.0/GdkX11-2.0.typelib
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
import gi.overrides.Gdk as __gi_overrides_Gdk
import gi.repository.Gdk as __gi_repository_Gdk


# Variables with simple values

_namespace = 'GdkX11'

_version = '3.0'

__weakref__ = None

# functions

def x11_atom_to_xatom(atom): # real signature unknown; restored from __doc__
    """ x11_atom_to_xatom(atom:Gdk.Atom) -> int """
    return 0

def x11_atom_to_xatom_for_display(display, atom): # real signature unknown; restored from __doc__
    """ x11_atom_to_xatom_for_display(display:GdkX11.X11Display, atom:Gdk.Atom) -> int """
    return 0

def x11_device_get_id(device): # real signature unknown; restored from __doc__
    """ x11_device_get_id(device:GdkX11.X11DeviceCore) -> int """
    return 0

def x11_device_manager_lookup(device_manager, device_id): # real signature unknown; restored from __doc__
    """ x11_device_manager_lookup(device_manager:GdkX11.X11DeviceManagerCore, device_id:int) -> GdkX11.X11DeviceCore or None """
    pass

def x11_free_compound_text(ctext): # real signature unknown; restored from __doc__
    """ x11_free_compound_text(ctext:int) """
    pass

def x11_free_text_list(p_list): # real signature unknown; restored from __doc__
    """ x11_free_text_list(list:str) """
    pass

def x11_get_default_root_xwindow(): # real signature unknown; restored from __doc__
    """ x11_get_default_root_xwindow() -> int """
    return 0

def x11_get_default_screen(): # real signature unknown; restored from __doc__
    """ x11_get_default_screen() -> int """
    return 0

def x11_get_default_xdisplay(): # real signature unknown; restored from __doc__
    """ x11_get_default_xdisplay() -> xlib.Display """
    pass

def x11_get_parent_relative_pattern(): # real signature unknown; restored from __doc__
    """ x11_get_parent_relative_pattern() -> cairo.Pattern """
    pass

def x11_get_server_time(window): # real signature unknown; restored from __doc__
    """ x11_get_server_time(window:GdkX11.X11Window) -> int """
    return 0

def x11_get_xatom_by_name(atom_name): # real signature unknown; restored from __doc__
    """ x11_get_xatom_by_name(atom_name:str) -> int """
    return 0

def x11_get_xatom_by_name_for_display(display, atom_name): # real signature unknown; restored from __doc__
    """ x11_get_xatom_by_name_for_display(display:GdkX11.X11Display, atom_name:str) -> int """
    return 0

def x11_get_xatom_name(xatom): # real signature unknown; restored from __doc__
    """ x11_get_xatom_name(xatom:int) -> str """
    return ""

def x11_get_xatom_name_for_display(display, xatom): # real signature unknown; restored from __doc__
    """ x11_get_xatom_name_for_display(display:GdkX11.X11Display, xatom:int) -> str """
    return ""

def x11_grab_server(): # real signature unknown; restored from __doc__
    """ x11_grab_server() """
    pass

def x11_lookup_xdisplay(xdisplay): # real signature unknown; restored from __doc__
    """ x11_lookup_xdisplay(xdisplay:xlib.Display) -> GdkX11.X11Display """
    pass

def x11_register_standard_event_type(display, event_base, n_events): # real signature unknown; restored from __doc__
    """ x11_register_standard_event_type(display:GdkX11.X11Display, event_base:int, n_events:int) """
    pass

def x11_set_sm_client_id(sm_client_id=None): # real signature unknown; restored from __doc__
    """ x11_set_sm_client_id(sm_client_id:str=None) """
    pass

def x11_ungrab_server(): # real signature unknown; restored from __doc__
    """ x11_ungrab_server() """
    pass

def x11_xatom_to_atom(xatom): # real signature unknown; restored from __doc__
    """ x11_xatom_to_atom(xatom:int) -> Gdk.Atom """
    pass

def x11_xatom_to_atom_for_display(display, xatom): # real signature unknown; restored from __doc__
    """ x11_xatom_to_atom_for_display(display:GdkX11.X11Display, xatom:int) -> Gdk.Atom """
    pass

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

from .X11AppLaunchContext import X11AppLaunchContext
from .X11AppLaunchContextClass import X11AppLaunchContextClass
from .X11Cursor import X11Cursor
from .X11CursorClass import X11CursorClass
from .X11DeviceCore import X11DeviceCore
from .X11DeviceCoreClass import X11DeviceCoreClass
from .X11DeviceManagerCore import X11DeviceManagerCore
from .X11DeviceManagerCoreClass import X11DeviceManagerCoreClass
from .X11DeviceManagerXI2 import X11DeviceManagerXI2
from .X11DeviceManagerXI2Class import X11DeviceManagerXI2Class
from .X11DeviceXI2 import X11DeviceXI2
from .X11DeviceXI2Class import X11DeviceXI2Class
from .X11Display import X11Display
from .X11DisplayClass import X11DisplayClass
from .X11DisplayManager import X11DisplayManager
from .X11DisplayManagerClass import X11DisplayManagerClass
from .X11DragContext import X11DragContext
from .X11DragContextClass import X11DragContextClass
from .X11GLContext import X11GLContext
from .X11GLContextClass import X11GLContextClass
from .X11Keymap import X11Keymap
from .X11KeymapClass import X11KeymapClass
from .X11Monitor import X11Monitor
from .X11MonitorClass import X11MonitorClass
from .X11Screen import X11Screen
from .X11ScreenClass import X11ScreenClass
from .X11Visual import X11Visual
from .X11VisualClass import X11VisualClass
from .X11Window import X11Window
from .X11WindowClass import X11WindowClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f08a2bc4d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GdkX11-3.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GdkX11', loader=<gi.importer.DynamicImporter object at 0x7f08a2bc4d00>)"

