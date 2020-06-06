# encoding: utf-8
# module gi.repository.GstBase
# from /usr/lib64/girepository-1.0/GstBase-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gobject as __gobject


# Variables with simple values

BASE_PARSE_FLAG_DRAINING = 2

BASE_PARSE_FLAG_LOST_SYNC = 1

BASE_TRANSFORM_SINK_NAME = 'sink'

BASE_TRANSFORM_SRC_NAME = 'src'

_namespace = 'GstBase'

_version = '1.0'

__weakref__ = None

# functions

def type_find_helper(src, size): # real signature unknown; restored from __doc__
    """ type_find_helper(src:Gst.Pad, size:int) -> Gst.Caps or None """
    pass

def type_find_helper_for_buffer(obj=None, buf): # real signature unknown; restored from __doc__
    """ type_find_helper_for_buffer(obj:Gst.Object=None, buf:Gst.Buffer) -> Gst.Caps or None, prob:Gst.TypeFindProbability """
    pass

def type_find_helper_for_buffer_with_extension(obj=None, buf, extension=None): # real signature unknown; restored from __doc__
    """ type_find_helper_for_buffer_with_extension(obj:Gst.Object=None, buf:Gst.Buffer, extension:str=None) -> Gst.Caps or None, prob:Gst.TypeFindProbability """
    pass

def type_find_helper_for_data(obj=None, data): # real signature unknown; restored from __doc__
    """ type_find_helper_for_data(obj:Gst.Object=None, data:list) -> Gst.Caps or None, prob:Gst.TypeFindProbability """
    pass

def type_find_helper_for_data_with_extension(obj=None, data, extension=None): # real signature unknown; restored from __doc__
    """ type_find_helper_for_data_with_extension(obj:Gst.Object=None, data:list, extension:str=None) -> Gst.Caps or None, prob:Gst.TypeFindProbability """
    pass

def type_find_helper_for_extension(obj=None, extension): # real signature unknown; restored from __doc__
    """ type_find_helper_for_extension(obj:Gst.Object=None, extension:str) -> Gst.Caps or None """
    pass

def type_find_helper_get_range(obj, parent=None, func, size, extension=None): # real signature unknown; restored from __doc__
    """ type_find_helper_get_range(obj:Gst.Object, parent:Gst.Object=None, func:GstBase.TypeFindHelperGetRangeFunction, size:int, extension:str=None) -> Gst.Caps or None, prob:Gst.TypeFindProbability """
    pass

def type_find_helper_get_range_full(obj, parent=None, func, size, extension=None): # real signature unknown; restored from __doc__
    """ type_find_helper_get_range_full(obj:Gst.Object, parent:Gst.Object=None, func:GstBase.TypeFindHelperGetRangeFunction, size:int, extension:str=None) -> Gst.FlowReturn, caps:Gst.Caps, prob:Gst.TypeFindProbability """
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

from .Adapter import Adapter
from .AdapterClass import AdapterClass
from .Aggregator import Aggregator
from .AggregatorClass import AggregatorClass
from .AggregatorPad import AggregatorPad
from .AggregatorPadClass import AggregatorPadClass
from .AggregatorPadPrivate import AggregatorPadPrivate
from .AggregatorPrivate import AggregatorPrivate
from .BaseParse import BaseParse
from .BaseParseClass import BaseParseClass
from .BaseParseFrame import BaseParseFrame
from .BaseParseFrameFlags import BaseParseFrameFlags
from .BaseParsePrivate import BaseParsePrivate
from .BaseSink import BaseSink
from .BaseSinkClass import BaseSinkClass
from .BaseSinkPrivate import BaseSinkPrivate
from .BaseSrc import BaseSrc
from .BaseSrcClass import BaseSrcClass
from .BaseSrcFlags import BaseSrcFlags
from .BaseSrcPrivate import BaseSrcPrivate
from .BaseTransform import BaseTransform
from .BaseTransformClass import BaseTransformClass
from .BaseTransformPrivate import BaseTransformPrivate
from .BitReader import BitReader
from .BitWriter import BitWriter
from .ByteReader import ByteReader
from .ByteWriter import ByteWriter
from .CollectData import CollectData
from .CollectDataPrivate import CollectDataPrivate
from .CollectPads import CollectPads
from .CollectPadsClass import CollectPadsClass
from .CollectPadsPrivate import CollectPadsPrivate
from .CollectPadsStateFlags import CollectPadsStateFlags
from .DataQueue import DataQueue
from .DataQueueClass import DataQueueClass
from .DataQueuePrivate import DataQueuePrivate
from .FlowCombiner import FlowCombiner
from .PushSrc import PushSrc
from .PushSrcClass import PushSrcClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f9fb8a19d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GstBase-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GstBase', loader=<gi.importer.DynamicImporter object at 0x7f9fb8a19d00>)"

