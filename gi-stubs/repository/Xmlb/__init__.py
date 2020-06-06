# encoding: utf-8
# module gi.repository.Xmlb
# from /usr/lib64/girepository-1.0/Xmlb-1.0.typelib
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

_namespace = 'Xmlb'

_version = '1.0'

__weakref__ = None

# functions

def opcode_kind_from_string(p_str): # real signature unknown; restored from __doc__
    """ opcode_kind_from_string(str:str) -> Xmlb.OpcodeKind """
    pass

def opcode_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ opcode_kind_to_string(kind:Xmlb.OpcodeKind) -> str """
    return ""

def string_escape(p_str): # real signature unknown; restored from __doc__
    """ string_escape(str:str) -> str """
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

from .Builder import Builder
from .BuilderClass import BuilderClass
from .BuilderCompileFlags import BuilderCompileFlags
from .BuilderFixup import BuilderFixup
from .BuilderFixupClass import BuilderFixupClass
from .BuilderNode import BuilderNode
from .BuilderNodeClass import BuilderNodeClass
from .BuilderNodeFlags import BuilderNodeFlags
from .BuilderSource import BuilderSource
from .BuilderSourceClass import BuilderSourceClass
from .BuilderSourceCtx import BuilderSourceCtx
from .BuilderSourceCtxClass import BuilderSourceCtxClass
from .BuilderSourceFlags import BuilderSourceFlags
from .Machine import Machine
from .MachineClass import MachineClass
from .MachineDebugFlags import MachineDebugFlags
from .MachineParseFlags import MachineParseFlags
from .Node import Node
from .NodeClass import NodeClass
from .NodeExportFlags import NodeExportFlags
from .Opcode import Opcode
from .OpcodeFlags import OpcodeFlags
from .OpcodeKind import OpcodeKind
from .Query import Query
from .QueryClass import QueryClass
from .QueryFlags import QueryFlags
from .Silo import Silo
from .SiloClass import SiloClass
from .SiloLoadFlags import SiloLoadFlags
from .SiloProfileFlags import SiloProfileFlags
from .Stack import Stack
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fe59ef23d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Xmlb-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Xmlb', loader=<gi.importer.DynamicImporter object at 0x7fe59ef23d00>)"

