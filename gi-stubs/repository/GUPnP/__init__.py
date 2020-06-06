# encoding: utf-8
# module gi.repository.GUPnP
# from /usr/lib64/girepository-1.0/GUPnP-1.0.typelib
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
import gi.repository.GSSDP as __gi_repository_GSSDP
import gobject as __gobject


# Variables with simple values

_namespace = 'GUPnP'

_version = '1.0'

__weakref__ = None

# functions

def control_error_quark(): # real signature unknown; restored from __doc__
    """ control_error_quark() -> int """
    return 0

def eventing_error_quark(): # real signature unknown; restored from __doc__
    """ eventing_error_quark() -> int """
    return 0

def get_uuid(): # real signature unknown; restored from __doc__
    """ get_uuid() -> str """
    return ""

def server_error_quark(): # real signature unknown; restored from __doc__
    """ server_error_quark() -> int """
    return 0

def xml_error_quark(): # real signature unknown; restored from __doc__
    """ xml_error_quark() -> int """
    return 0

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

from .Acl import Acl
from .AclInterface import AclInterface
from .BinBase64 import BinBase64
from .BinHex import BinHex
from .Context import Context
from .ContextClass import ContextClass
from .ContextManager import ContextManager
from .ContextManagerClass import ContextManagerClass
from .ContextManagerPrivate import ContextManagerPrivate
from .ContextPrivate import ContextPrivate
from .ControlError import ControlError
from .ControlPoint import ControlPoint
from .ControlPointClass import ControlPointClass
from .ControlPointPrivate import ControlPointPrivate
from .Date import Date
from .DateTime import DateTime
from .DateTimeTZ import DateTimeTZ
from .DeviceInfo import DeviceInfo
from .Device import Device
from .DeviceClass import DeviceClass
from .DeviceInfoClass import DeviceInfoClass
from .DeviceInfoPrivate import DeviceInfoPrivate
from .DevicePrivate import DevicePrivate
from .DeviceProxy import DeviceProxy
from .DeviceProxyClass import DeviceProxyClass
from .DeviceProxyPrivate import DeviceProxyPrivate
from .EventingError import EventingError
from .ResourceFactory import ResourceFactory
from .ResourceFactoryClass import ResourceFactoryClass
from .ResourceFactoryPrivate import ResourceFactoryPrivate
from .RootDevice import RootDevice
from .RootDeviceClass import RootDeviceClass
from .RootDevicePrivate import RootDevicePrivate
from .ServerError import ServerError
from .ServiceInfo import ServiceInfo
from .Service import Service
from .ServiceAction import ServiceAction
from .ServiceActionArgDirection import ServiceActionArgDirection
from .ServiceActionArgInfo import ServiceActionArgInfo
from .ServiceActionInfo import ServiceActionInfo
from .ServiceClass import ServiceClass
from .ServiceInfoClass import ServiceInfoClass
from .ServiceInfoPrivate import ServiceInfoPrivate
from .ServiceIntrospection import ServiceIntrospection
from .ServiceIntrospectionClass import ServiceIntrospectionClass
from .ServiceIntrospectionPrivate import ServiceIntrospectionPrivate
from .ServicePrivate import ServicePrivate
from .ServiceProxy import ServiceProxy
from .ServiceProxyAction import ServiceProxyAction
from .ServiceProxyClass import ServiceProxyClass
from .ServiceProxyPrivate import ServiceProxyPrivate
from .ServiceStateVariableInfo import ServiceStateVariableInfo
from .Time import Time
from .TimeTZ import TimeTZ
from .URI import URI
from .UUID import UUID
from .WhiteList import WhiteList
from .WhiteListClass import WhiteListClass
from .WhiteListPrivate import WhiteListPrivate
from .XMLDoc import XMLDoc
from .XMLDocClass import XMLDocClass
from .XMLError import XMLError
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f24eb1fed00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GUPnP-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GUPnP', loader=<gi.importer.DynamicImporter object at 0x7f24eb1fed00>)"

