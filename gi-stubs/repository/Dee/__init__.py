# encoding: utf-8
# module gi.repository.Dee
# from /usr/lib/girepository-1.0/Dee-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Dee as __gi_overrides_Dee
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


# Variables with simple values

PEER_DBUS_IFACE = 'com.canonical.Dee.Peer'

SEQUENCE_MODEL_DBUS_IFACE = 'com.canonical.Dee.Model'

SHARED_MODEL_DBUS_IFACE = 'com.canonical.Dee.Model'

_namespace = 'Dee'

_version = '1.0'

__path__ = '/usr/lib/girepository-1.0/Dee-1.0.typelib'

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
    """ default object formatter """
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
    """ helper for pickle """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ helper for pickle """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(): # real signature unknown; restored from __doc__
    """
    __sizeof__() -> int
    size of object in memory, in bytes
    """
    return 0

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

from .Analyzer import Analyzer
from .AnalyzerClass import AnalyzerClass
from .AnalyzerPrivate import AnalyzerPrivate
from .Peer import Peer
from .Client import Client
from .ClientClass import ClientClass
from .ClientPrivate import ClientPrivate
from .ResourceManager import ResourceManager
from .FileResourceManager import FileResourceManager
from .FileResourceManagerClass import FileResourceManagerClass
from .Filter import Filter
from .Model import Model
from .Serializable import Serializable
from .SerializableModel import SerializableModel
from .ProxyModel import ProxyModel
from .FilterModel import FilterModel
from .FilterModelClass import FilterModelClass
from .FilterModelPrivate import FilterModelPrivate
from .ResultSet import ResultSet
from .GListResultSet import GListResultSet
from .GListResultSetClass import GListResultSetClass
from .Index import Index
from .HashIndex import HashIndex
from .HashIndexClass import HashIndexClass
from .HashIndexPrivate import HashIndexPrivate
from .ICUError import ICUError
from .ICUTermFilter import ICUTermFilter
from .IndexClass import IndexClass
from .IndexPrivate import IndexPrivate
from .ModelIface import ModelIface
from .ModelIter import ModelIter
from .ModelReader import ModelReader
from .ModelTag import ModelTag
from .PeerClass import PeerClass
from .PeerPrivate import PeerPrivate
from .ProxyModelClass import ProxyModelClass
from .ProxyModelPrivate import ProxyModelPrivate
from .ResourceManagerIface import ResourceManagerIface
from .ResultSetIface import ResultSetIface
from .SequenceModel import SequenceModel
from .SequenceModelClass import SequenceModelClass
from .SequenceModelPrivate import SequenceModelPrivate
from .SerializableIface import SerializableIface
from .SerializableModelClass import SerializableModelClass
from .SerializableModelPrivate import SerializableModelPrivate
from .Server import Server
from .ServerClass import ServerClass
from .ServerPrivate import ServerPrivate
from .SharedModel import SharedModel
from .SharedModelAccessMode import SharedModelAccessMode
from .SharedModelClass import SharedModelClass
from .SharedModelError import SharedModelError
from .SharedModelFlushMode import SharedModelFlushMode
from .SharedModelPrivate import SharedModelPrivate
from .TermList import TermList
from .TermListClass import TermListClass
from .TermListPrivate import TermListPrivate
from .TermMatchFlag import TermMatchFlag
from .TextAnalyzer import TextAnalyzer
from .TextAnalyzerClass import TextAnalyzerClass
from .TextAnalyzerPrivate import TextAnalyzerPrivate
from .Transaction import Transaction
from .TransactionClass import TransactionClass
from .TransactionError import TransactionError
from .TransactionPrivate import TransactionPrivate
from .TreeIndex import TreeIndex
from .TreeIndexClass import TreeIndexClass
from .TreeIndexPrivate import TreeIndexPrivate
from .__class__ import __class__
# variables with complex values

filter_new = gi.FunctionInfo(filter_new)

filter_new_collator = gi.FunctionInfo(filter_new_collator)

filter_new_collator_desc = gi.FunctionInfo(filter_new_collator_desc)

filter_new_for_any_column = gi.FunctionInfo(filter_new_for_any_column)

filter_new_for_key_column = gi.FunctionInfo(filter_new_for_key_column)

filter_new_regex = gi.FunctionInfo(filter_new_regex)

filter_new_sort = gi.FunctionInfo(filter_new_sort)

icu_error_quark = gi.FunctionInfo(icu_error_quark)

model_reader_new = gi.FunctionInfo(model_reader_new)

model_reader_new_for_int32_column = gi.FunctionInfo(model_reader_new_for_int32_column)

model_reader_new_for_string_column = gi.FunctionInfo(model_reader_new_for_string_column)

model_reader_new_for_uint32_column = gi.FunctionInfo(model_reader_new_for_uint32_column)

resource_manager_get_default = gi.FunctionInfo(resource_manager_get_default)

serializable_parse = gi.FunctionInfo(serializable_parse)

serializable_parse_external = gi.FunctionInfo(serializable_parse_external)

_introspection_module = None # (!) real value is "<IntrospectionModule 'Dee' from '/usr/lib/girepository-1.0/Dee-1.0.typelib'>"

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f5a321534a8>'

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Dee', loader=<gi.importer.DynamicImporter object at 0x7f5a321534a8>)"

