# encoding: utf-8
# module gi.repository.Goa
# from /usr/lib64/girepository-1.0/Goa-1.0.typelib
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

ERROR_NUM_ENTRIES = 6

_namespace = 'Goa'

_version = '1.0'

__weakref__ = None

# functions

def account_interface_info(): # real signature unknown; restored from __doc__
    """ account_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def account_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ account_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def calendar_interface_info(): # real signature unknown; restored from __doc__
    """ calendar_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def calendar_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ calendar_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def chat_interface_info(): # real signature unknown; restored from __doc__
    """ chat_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def chat_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ chat_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def check_version(required_major, required_minor, required_micro): # real signature unknown; restored from __doc__
    """ check_version(required_major:int, required_minor:int, required_micro:int) -> str """
    return ""

def contacts_interface_info(): # real signature unknown; restored from __doc__
    """ contacts_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def contacts_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ contacts_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def documents_interface_info(): # real signature unknown; restored from __doc__
    """ documents_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def documents_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ documents_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def exchange_interface_info(): # real signature unknown; restored from __doc__
    """ exchange_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def exchange_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ exchange_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def files_interface_info(): # real signature unknown; restored from __doc__
    """ files_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def files_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ files_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def mail_interface_info(): # real signature unknown; restored from __doc__
    """ mail_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def mail_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ mail_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def manager_interface_info(): # real signature unknown; restored from __doc__
    """ manager_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def manager_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ manager_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def maps_interface_info(): # real signature unknown; restored from __doc__
    """ maps_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def maps_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ maps_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def media_server_interface_info(): # real signature unknown; restored from __doc__
    """ media_server_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def media_server_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ media_server_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def music_interface_info(): # real signature unknown; restored from __doc__
    """ music_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def music_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ music_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def oauth2_based_interface_info(): # real signature unknown; restored from __doc__
    """ oauth2_based_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def oauth2_based_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ oauth2_based_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def oauth_based_interface_info(): # real signature unknown; restored from __doc__
    """ oauth_based_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def oauth_based_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ oauth_based_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def password_based_interface_info(): # real signature unknown; restored from __doc__
    """ password_based_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def password_based_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ password_based_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def photos_interface_info(): # real signature unknown; restored from __doc__
    """ photos_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def photos_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ photos_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def printers_interface_info(): # real signature unknown; restored from __doc__
    """ printers_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def printers_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ printers_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def read_later_interface_info(): # real signature unknown; restored from __doc__
    """ read_later_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def read_later_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ read_later_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def ticketing_interface_info(): # real signature unknown; restored from __doc__
    """ ticketing_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def ticketing_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ ticketing_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def todo_interface_info(): # real signature unknown; restored from __doc__
    """ todo_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def todo_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ todo_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
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

from .Account import Account
from .AccountIface import AccountIface
from .AccountProxy import AccountProxy
from .AccountProxyClass import AccountProxyClass
from .AccountProxyPrivate import AccountProxyPrivate
from .AccountSkeleton import AccountSkeleton
from .AccountSkeletonClass import AccountSkeletonClass
from .AccountSkeletonPrivate import AccountSkeletonPrivate
from .Calendar import Calendar
from .CalendarIface import CalendarIface
from .CalendarProxy import CalendarProxy
from .CalendarProxyClass import CalendarProxyClass
from .CalendarProxyPrivate import CalendarProxyPrivate
from .CalendarSkeleton import CalendarSkeleton
from .CalendarSkeletonClass import CalendarSkeletonClass
from .CalendarSkeletonPrivate import CalendarSkeletonPrivate
from .Chat import Chat
from .ChatIface import ChatIface
from .ChatProxy import ChatProxy
from .ChatProxyClass import ChatProxyClass
from .ChatProxyPrivate import ChatProxyPrivate
from .ChatSkeleton import ChatSkeleton
from .ChatSkeletonClass import ChatSkeletonClass
from .ChatSkeletonPrivate import ChatSkeletonPrivate
from .Client import Client
from .ClientClass import ClientClass
from .Contacts import Contacts
from .ContactsIface import ContactsIface
from .ContactsProxy import ContactsProxy
from .ContactsProxyClass import ContactsProxyClass
from .ContactsProxyPrivate import ContactsProxyPrivate
from .ContactsSkeleton import ContactsSkeleton
from .ContactsSkeletonClass import ContactsSkeletonClass
from .ContactsSkeletonPrivate import ContactsSkeletonPrivate
from .Documents import Documents
from .DocumentsIface import DocumentsIface
from .DocumentsProxy import DocumentsProxy
from .DocumentsProxyClass import DocumentsProxyClass
from .DocumentsProxyPrivate import DocumentsProxyPrivate
from .DocumentsSkeleton import DocumentsSkeleton
from .DocumentsSkeletonClass import DocumentsSkeletonClass
from .DocumentsSkeletonPrivate import DocumentsSkeletonPrivate
from .Error import Error
from .Exchange import Exchange
from .ExchangeIface import ExchangeIface
from .ExchangeProxy import ExchangeProxy
from .ExchangeProxyClass import ExchangeProxyClass
from .ExchangeProxyPrivate import ExchangeProxyPrivate
from .ExchangeSkeleton import ExchangeSkeleton
from .ExchangeSkeletonClass import ExchangeSkeletonClass
from .ExchangeSkeletonPrivate import ExchangeSkeletonPrivate
from .Files import Files
from .FilesIface import FilesIface
from .FilesProxy import FilesProxy
from .FilesProxyClass import FilesProxyClass
from .FilesProxyPrivate import FilesProxyPrivate
from .FilesSkeleton import FilesSkeleton
from .FilesSkeletonClass import FilesSkeletonClass
from .FilesSkeletonPrivate import FilesSkeletonPrivate
from .Mail import Mail
from .MailIface import MailIface
from .MailProxy import MailProxy
from .MailProxyClass import MailProxyClass
from .MailProxyPrivate import MailProxyPrivate
from .MailSkeleton import MailSkeleton
from .MailSkeletonClass import MailSkeletonClass
from .MailSkeletonPrivate import MailSkeletonPrivate
from .Manager import Manager
from .ManagerIface import ManagerIface
from .ManagerProxy import ManagerProxy
from .ManagerProxyClass import ManagerProxyClass
from .ManagerProxyPrivate import ManagerProxyPrivate
from .ManagerSkeleton import ManagerSkeleton
from .ManagerSkeletonClass import ManagerSkeletonClass
from .ManagerSkeletonPrivate import ManagerSkeletonPrivate
from .Maps import Maps
from .MapsIface import MapsIface
from .MapsProxy import MapsProxy
from .MapsProxyClass import MapsProxyClass
from .MapsProxyPrivate import MapsProxyPrivate
from .MapsSkeleton import MapsSkeleton
from .MapsSkeletonClass import MapsSkeletonClass
from .MapsSkeletonPrivate import MapsSkeletonPrivate
from .MediaServer import MediaServer
from .MediaServerIface import MediaServerIface
from .MediaServerProxy import MediaServerProxy
from .MediaServerProxyClass import MediaServerProxyClass
from .MediaServerProxyPrivate import MediaServerProxyPrivate
from .MediaServerSkeleton import MediaServerSkeleton
from .MediaServerSkeletonClass import MediaServerSkeletonClass
from .MediaServerSkeletonPrivate import MediaServerSkeletonPrivate
from .Music import Music
from .MusicIface import MusicIface
from .MusicProxy import MusicProxy
from .MusicProxyClass import MusicProxyClass
from .MusicProxyPrivate import MusicProxyPrivate
from .MusicSkeleton import MusicSkeleton
from .MusicSkeletonClass import MusicSkeletonClass
from .MusicSkeletonPrivate import MusicSkeletonPrivate
from .OAuth2Based import OAuth2Based
from .OAuth2BasedIface import OAuth2BasedIface
from .OAuth2BasedProxy import OAuth2BasedProxy
from .OAuth2BasedProxyClass import OAuth2BasedProxyClass
from .OAuth2BasedProxyPrivate import OAuth2BasedProxyPrivate
from .OAuth2BasedSkeleton import OAuth2BasedSkeleton
from .OAuth2BasedSkeletonClass import OAuth2BasedSkeletonClass
from .OAuth2BasedSkeletonPrivate import OAuth2BasedSkeletonPrivate
from .OAuthBased import OAuthBased
from .OAuthBasedIface import OAuthBasedIface
from .OAuthBasedProxy import OAuthBasedProxy
from .OAuthBasedProxyClass import OAuthBasedProxyClass
from .OAuthBasedProxyPrivate import OAuthBasedProxyPrivate
from .OAuthBasedSkeleton import OAuthBasedSkeleton
from .OAuthBasedSkeletonClass import OAuthBasedSkeletonClass
from .OAuthBasedSkeletonPrivate import OAuthBasedSkeletonPrivate
from .Object import Object
from .ObjectIface import ObjectIface
from .ObjectManagerClient import ObjectManagerClient
from .ObjectManagerClientClass import ObjectManagerClientClass
from .ObjectManagerClientPrivate import ObjectManagerClientPrivate
from .ObjectProxy import ObjectProxy
from .ObjectProxyClass import ObjectProxyClass
from .ObjectProxyPrivate import ObjectProxyPrivate
from .ObjectSkeleton import ObjectSkeleton
from .ObjectSkeletonClass import ObjectSkeletonClass
from .ObjectSkeletonPrivate import ObjectSkeletonPrivate
from .PasswordBased import PasswordBased
from .PasswordBasedIface import PasswordBasedIface
from .PasswordBasedProxy import PasswordBasedProxy
from .PasswordBasedProxyClass import PasswordBasedProxyClass
from .PasswordBasedProxyPrivate import PasswordBasedProxyPrivate
from .PasswordBasedSkeleton import PasswordBasedSkeleton
from .PasswordBasedSkeletonClass import PasswordBasedSkeletonClass
from .PasswordBasedSkeletonPrivate import PasswordBasedSkeletonPrivate
from .Photos import Photos
from .PhotosIface import PhotosIface
from .PhotosProxy import PhotosProxy
from .PhotosProxyClass import PhotosProxyClass
from .PhotosProxyPrivate import PhotosProxyPrivate
from .PhotosSkeleton import PhotosSkeleton
from .PhotosSkeletonClass import PhotosSkeletonClass
from .PhotosSkeletonPrivate import PhotosSkeletonPrivate
from .Printers import Printers
from .PrintersIface import PrintersIface
from .PrintersProxy import PrintersProxy
from .PrintersProxyClass import PrintersProxyClass
from .PrintersProxyPrivate import PrintersProxyPrivate
from .PrintersSkeleton import PrintersSkeleton
from .PrintersSkeletonClass import PrintersSkeletonClass
from .PrintersSkeletonPrivate import PrintersSkeletonPrivate
from .ReadLater import ReadLater
from .ReadLaterIface import ReadLaterIface
from .ReadLaterProxy import ReadLaterProxy
from .ReadLaterProxyClass import ReadLaterProxyClass
from .ReadLaterProxyPrivate import ReadLaterProxyPrivate
from .ReadLaterSkeleton import ReadLaterSkeleton
from .ReadLaterSkeletonClass import ReadLaterSkeletonClass
from .ReadLaterSkeletonPrivate import ReadLaterSkeletonPrivate
from .Ticketing import Ticketing
from .TicketingIface import TicketingIface
from .TicketingProxy import TicketingProxy
from .TicketingProxyClass import TicketingProxyClass
from .TicketingProxyPrivate import TicketingProxyPrivate
from .TicketingSkeleton import TicketingSkeleton
from .TicketingSkeletonClass import TicketingSkeletonClass
from .TicketingSkeletonPrivate import TicketingSkeletonPrivate
from .Todo import Todo
from .TodoIface import TodoIface
from .TodoProxy import TodoProxy
from .TodoProxyClass import TodoProxyClass
from .TodoProxyPrivate import TodoProxyPrivate
from .TodoSkeleton import TodoSkeleton
from .TodoSkeletonClass import TodoSkeletonClass
from .TodoSkeletonPrivate import TodoSkeletonPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f37f5b78d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Goa-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Goa', loader=<gi.importer.DynamicImporter object at 0x7f37f5b78d00>)"

