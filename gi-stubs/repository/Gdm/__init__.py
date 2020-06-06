# encoding: utf-8
# module gi.repository.Gdm
# from /usr/lib64/girepository-1.0/Gdm-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


# Variables with simple values

_namespace = 'Gdm'

_version = '1.0'

__weakref__ = None

# functions

def chooser_interface_info(): # real signature unknown; restored from __doc__
    """ chooser_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def chooser_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ chooser_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def get_session_ids(): # real signature unknown; restored from __doc__
    """ get_session_ids() -> list """
    return []

def get_session_name_and_description(id): # real signature unknown; restored from __doc__
    """ get_session_name_and_description(id:str) -> str, description:str """
    return ""

def goto_login_session_sync(cancellable=None): # real signature unknown; restored from __doc__
    """ goto_login_session_sync(cancellable:Gio.Cancellable=None) -> bool """
    return False

def greeter_interface_info(): # real signature unknown; restored from __doc__
    """ greeter_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def greeter_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ greeter_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def manager_interface_info(): # real signature unknown; restored from __doc__
    """ manager_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def manager_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ manager_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def remote_greeter_interface_info(): # real signature unknown; restored from __doc__
    """ remote_greeter_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def remote_greeter_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ remote_greeter_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def user_verifier_choice_list_interface_info(): # real signature unknown; restored from __doc__
    """ user_verifier_choice_list_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def user_verifier_choice_list_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ user_verifier_choice_list_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def user_verifier_interface_info(): # real signature unknown; restored from __doc__
    """ user_verifier_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def user_verifier_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ user_verifier_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def worker_manager_interface_info(): # real signature unknown; restored from __doc__
    """ worker_manager_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def worker_manager_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ worker_manager_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
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

from .Chooser import Chooser
from .ChooserIface import ChooserIface
from .ChooserProxy import ChooserProxy
from .ChooserProxyClass import ChooserProxyClass
from .ChooserProxyPrivate import ChooserProxyPrivate
from .ChooserSkeleton import ChooserSkeleton
from .ChooserSkeletonClass import ChooserSkeletonClass
from .ChooserSkeletonPrivate import ChooserSkeletonPrivate
from .Client import Client
from .ClientClass import ClientClass
from .ClientError import ClientError
from .Greeter import Greeter
from .GreeterIface import GreeterIface
from .GreeterProxy import GreeterProxy
from .GreeterProxyClass import GreeterProxyClass
from .GreeterProxyPrivate import GreeterProxyPrivate
from .GreeterSkeleton import GreeterSkeleton
from .GreeterSkeletonClass import GreeterSkeletonClass
from .GreeterSkeletonPrivate import GreeterSkeletonPrivate
from .Manager import Manager
from .ManagerIface import ManagerIface
from .ManagerProxy import ManagerProxy
from .ManagerProxyClass import ManagerProxyClass
from .ManagerProxyPrivate import ManagerProxyPrivate
from .ManagerSkeleton import ManagerSkeleton
from .ManagerSkeletonClass import ManagerSkeletonClass
from .ManagerSkeletonPrivate import ManagerSkeletonPrivate
from .RemoteGreeter import RemoteGreeter
from .RemoteGreeterIface import RemoteGreeterIface
from .RemoteGreeterProxy import RemoteGreeterProxy
from .RemoteGreeterProxyClass import RemoteGreeterProxyClass
from .RemoteGreeterProxyPrivate import RemoteGreeterProxyPrivate
from .RemoteGreeterSkeleton import RemoteGreeterSkeleton
from .RemoteGreeterSkeletonClass import RemoteGreeterSkeletonClass
from .RemoteGreeterSkeletonPrivate import RemoteGreeterSkeletonPrivate
from .UserVerifier import UserVerifier
from .UserVerifierChoiceList import UserVerifierChoiceList
from .UserVerifierChoiceListIface import UserVerifierChoiceListIface
from .UserVerifierChoiceListProxy import UserVerifierChoiceListProxy
from .UserVerifierChoiceListProxyClass import UserVerifierChoiceListProxyClass
from .UserVerifierChoiceListProxyPrivate import UserVerifierChoiceListProxyPrivate
from .UserVerifierChoiceListSkeleton import UserVerifierChoiceListSkeleton
from .UserVerifierChoiceListSkeletonClass import UserVerifierChoiceListSkeletonClass
from .UserVerifierChoiceListSkeletonPrivate import UserVerifierChoiceListSkeletonPrivate
from .UserVerifierIface import UserVerifierIface
from .UserVerifierProxy import UserVerifierProxy
from .UserVerifierProxyClass import UserVerifierProxyClass
from .UserVerifierProxyPrivate import UserVerifierProxyPrivate
from .UserVerifierSkeleton import UserVerifierSkeleton
from .UserVerifierSkeletonClass import UserVerifierSkeletonClass
from .UserVerifierSkeletonPrivate import UserVerifierSkeletonPrivate
from .WorkerManager import WorkerManager
from .WorkerManagerIface import WorkerManagerIface
from .WorkerManagerProxy import WorkerManagerProxy
from .WorkerManagerProxyClass import WorkerManagerProxyClass
from .WorkerManagerProxyPrivate import WorkerManagerProxyPrivate
from .WorkerManagerSkeleton import WorkerManagerSkeleton
from .WorkerManagerSkeletonClass import WorkerManagerSkeletonClass
from .WorkerManagerSkeletonPrivate import WorkerManagerSkeletonPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f26efeb4d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Gdm-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gdm', loader=<gi.importer.DynamicImporter object at 0x7f26efeb4d00>)"

