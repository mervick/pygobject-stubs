# encoding: utf-8
# module gi.repository.Polkit
# from /usr/lib64/girepository-1.0/Polkit-1.0.typelib
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

_namespace = 'Polkit'

_version = '1.0'

__weakref__ = None

# functions

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def identity_from_string(p_str): # real signature unknown; restored from __doc__
    """ identity_from_string(str:str) -> Polkit.Identity or None """
    pass

def implicit_authorization_from_string(string, out_implicit_authorization): # real signature unknown; restored from __doc__
    """ implicit_authorization_from_string(string:str, out_implicit_authorization:Polkit.ImplicitAuthorization) -> bool """
    return False

def implicit_authorization_to_string(implicit_authorization): # real signature unknown; restored from __doc__
    """ implicit_authorization_to_string(implicit_authorization:Polkit.ImplicitAuthorization) -> str """
    return ""

def subject_from_string(p_str): # real signature unknown; restored from __doc__
    """ subject_from_string(str:str) -> Polkit.Subject """
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

from .ActionDescription import ActionDescription
from .ActionDescriptionClass import ActionDescriptionClass
from .Authority import Authority
from .AuthorityClass import AuthorityClass
from .AuthorityFeatures import AuthorityFeatures
from .AuthorizationResult import AuthorizationResult
from .AuthorizationResultClass import AuthorizationResultClass
from .CheckAuthorizationFlags import CheckAuthorizationFlags
from .Details import Details
from .DetailsClass import DetailsClass
from .Error import Error
from .Identity import Identity
from .IdentityIface import IdentityIface
from .ImplicitAuthorization import ImplicitAuthorization
from .Permission import Permission
from .Subject import Subject
from .SubjectIface import SubjectIface
from .SystemBusName import SystemBusName
from .SystemBusNameClass import SystemBusNameClass
from .TemporaryAuthorization import TemporaryAuthorization
from .TemporaryAuthorizationClass import TemporaryAuthorizationClass
from .UnixGroup import UnixGroup
from .UnixGroupClass import UnixGroupClass
from .UnixNetgroup import UnixNetgroup
from .UnixNetgroupClass import UnixNetgroupClass
from .UnixProcess import UnixProcess
from .UnixProcessClass import UnixProcessClass
from .UnixSession import UnixSession
from .UnixSessionClass import UnixSessionClass
from .UnixUser import UnixUser
from .UnixUserClass import UnixUserClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f9827e81d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Polkit-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Polkit', loader=<gi.importer.DynamicImporter object at 0x7f9827e81d00>)"

