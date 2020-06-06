# encoding: utf-8
# module gi.repository.GUPnPDLNA
# from /usr/lib64/girepository-1.0/GUPnPDLNA-2.0.typelib
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


# Variables with simple values

_namespace = 'GUPnPDLNA'

_version = '2.0'

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

from .AudioInformation import AudioInformation
from .AudioInformationClass import AudioInformationClass
from .AudioInformationPrivate import AudioInformationPrivate
from .BoolValue import BoolValue
from .ContainerInformation import ContainerInformation
from .ContainerInformationClass import ContainerInformationClass
from .ContainerInformationPrivate import ContainerInformationPrivate
from .Fraction import Fraction
from .FractionRange import FractionRange
from .FractionValue import FractionValue
from .ImageInformation import ImageInformation
from .ImageInformationClass import ImageInformationClass
from .ImageInformationPrivate import ImageInformationPrivate
from .Information import Information
from .InformationClass import InformationClass
from .InformationPrivate import InformationPrivate
from .IntRange import IntRange
from .IntValue import IntValue
from .Profile import Profile
from .ProfileClass import ProfileClass
from .ProfileGuesser import ProfileGuesser
from .ProfileGuesserClass import ProfileGuesserClass
from .ProfileGuesserPrivate import ProfileGuesserPrivate
from .ProfilePrivate import ProfilePrivate
from .Restriction import Restriction
from .StringValue import StringValue
from .ValueList import ValueList
from .ValueState import ValueState
from .VideoInformation import VideoInformation
from .VideoInformationClass import VideoInformationClass
from .VideoInformationPrivate import VideoInformationPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f6785571d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GUPnPDLNA-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GUPnPDLNA', loader=<gi.importer.DynamicImporter object at 0x7f6785571d00>)"

