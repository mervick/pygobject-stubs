# encoding: utf-8
# module gi.repository.Gee
# from /usr/lib64/girepository-1.0/Gee-0.8.typelib
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

_namespace = 'Gee'

_version = '0.8'

__weakref__ = None

# functions

def async_task(_callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
    """ async_task(_callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
    pass

def async_task_finish(_res_): # real signature unknown; restored from __doc__
    """ async_task_finish(_res_:Gio.AsyncResult) """
    pass

def functions_get_compare_func_for(t): # real signature unknown; restored from __doc__
    """ functions_get_compare_func_for(t:GType) -> GLib.CompareDataFunc, result_target, result_target_destroy_notify:GLib.DestroyNotify """
    pass

def functions_get_equal_func_for(t): # real signature unknown; restored from __doc__
    """ functions_get_equal_func_for(t:GType) -> Gee.EqualDataFunc, result_target, result_target_destroy_notify:GLib.DestroyNotify """
    pass

def functions_get_hash_func_for(t): # real signature unknown; restored from __doc__
    """ functions_get_hash_func_for(t:GType) -> Gee.HashDataFunc, result_target, result_target_destroy_notify:GLib.DestroyNotify """
    pass

def hazard_pointer_policy_is_blocking(): # real signature unknown; restored from __doc__
    """ hazard_pointer_policy_is_blocking() -> bool """
    return False

def hazard_pointer_policy_is_concrete(): # real signature unknown; restored from __doc__
    """ hazard_pointer_policy_is_concrete() -> bool """
    return False

def hazard_pointer_policy_is_safe(): # real signature unknown; restored from __doc__
    """ hazard_pointer_policy_is_safe() -> bool """
    return False

def hazard_pointer_policy_to_concrete(): # real signature unknown; restored from __doc__
    """ hazard_pointer_policy_to_concrete() -> Gee.HazardPointerPolicy """
    pass

def task(g_type, g_dup_func, g_destroy_func, task, task_target=None): # real signature unknown; restored from __doc__
    """ task(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, task:Gee.Task, task_target=None) -> Gee.Future """
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

from .Collection import Collection
from .Iterable import Iterable
from .Traversable import Traversable
from .AbstractCollection import AbstractCollection
from .List import List
from .AbstractList import AbstractList
from .BidirList import BidirList
from .AbstractBidirList import AbstractBidirList
from .AbstractBidirListClass import AbstractBidirListClass
from .AbstractBidirListPrivate import AbstractBidirListPrivate
from .Map import Map
from .AbstractMap import AbstractMap
from .SortedMap import SortedMap
from .AbstractSortedMap import AbstractSortedMap
from .BidirSortedMap import BidirSortedMap
from .AbstractBidirSortedMap import AbstractBidirSortedMap
from .AbstractBidirSortedMapClass import AbstractBidirSortedMapClass
from .AbstractBidirSortedMapPrivate import AbstractBidirSortedMapPrivate
from .Set import Set
from .AbstractSet import AbstractSet
from .SortedSet import SortedSet
from .AbstractSortedSet import AbstractSortedSet
from .BidirSortedSet import BidirSortedSet
from .AbstractBidirSortedSet import AbstractBidirSortedSet
from .AbstractBidirSortedSetClass import AbstractBidirSortedSetClass
from .AbstractBidirSortedSetPrivate import AbstractBidirSortedSetPrivate
from .AbstractCollectionClass import AbstractCollectionClass
from .AbstractCollectionPrivate import AbstractCollectionPrivate
from .AbstractListClass import AbstractListClass
from .AbstractListPrivate import AbstractListPrivate
from .AbstractMapClass import AbstractMapClass
from .AbstractMapPrivate import AbstractMapPrivate
from .MultiMap import MultiMap
from .AbstractMultiMap import AbstractMultiMap
from .AbstractMultiMapClass import AbstractMultiMapClass
from .AbstractMultiMapPrivate import AbstractMultiMapPrivate
from .MultiSet import MultiSet
from .AbstractMultiSet import AbstractMultiSet
from .AbstractMultiSetClass import AbstractMultiSetClass
from .AbstractMultiSetPrivate import AbstractMultiSetPrivate
from .Queue import Queue
from .AbstractQueue import AbstractQueue
from .AbstractQueueClass import AbstractQueueClass
from .AbstractQueuePrivate import AbstractQueuePrivate
from .AbstractSetClass import AbstractSetClass
from .AbstractSetPrivate import AbstractSetPrivate
from .AbstractSortedMapClass import AbstractSortedMapClass
from .AbstractSortedMapPrivate import AbstractSortedMapPrivate
from .AbstractSortedSetClass import AbstractSortedSetClass
from .AbstractSortedSetPrivate import AbstractSortedSetPrivate
from .ArrayList import ArrayList
from .ArrayListClass import ArrayListClass
from .ArrayListPrivate import ArrayListPrivate
from .Deque import Deque
from .ArrayQueue import ArrayQueue
from .ArrayQueueClass import ArrayQueueClass
from .ArrayQueuePrivate import ArrayQueuePrivate
from .BidirIterator import BidirIterator
from .BidirIteratorIface import BidirIteratorIface
from .BidirListIface import BidirListIface
from .BidirListIterator import BidirListIterator
from .BidirListIteratorIface import BidirListIteratorIface
from .BidirMapIterator import BidirMapIterator
from .BidirMapIteratorIface import BidirMapIteratorIface
from .BidirSortedMapIface import BidirSortedMapIface
from .BidirSortedSetIface import BidirSortedSetIface
from .CollectionIface import CollectionIface
from .Comparable import Comparable
from .ComparableIface import ComparableIface
from .ConcurrentList import ConcurrentList
from .ConcurrentListClass import ConcurrentListClass
from .ConcurrentListPrivate import ConcurrentListPrivate
from .ConcurrentSet import ConcurrentSet
from .ConcurrentSetClass import ConcurrentSetClass
from .ConcurrentSetPrivate import ConcurrentSetPrivate
from .ConcurrentSetRangeType import ConcurrentSetRangeType
from .DequeIface import DequeIface
from .Future import Future
from .FutureError import FutureError
from .FutureIface import FutureIface
from .Hashable import Hashable
from .HashableIface import HashableIface
from .HashMap import HashMap
from .HashMapClass import HashMapClass
from .HashMapPrivate import HashMapPrivate
from .HashMultiMap import HashMultiMap
from .HashMultiMapClass import HashMultiMapClass
from .HashMultiMapPrivate import HashMultiMapPrivate
from .HashMultiSet import HashMultiSet
from .HashMultiSetClass import HashMultiSetClass
from .HashMultiSetPrivate import HashMultiSetPrivate
from .HashSet import HashSet
from .HashSetClass import HashSetClass
from .HashSetPrivate import HashSetPrivate
from .HazardPointer import HazardPointer
from .HazardPointerContext import HazardPointerContext
from .HazardPointerPolicy import HazardPointerPolicy
from .HazardPointerReleasePolicy import HazardPointerReleasePolicy
from .IterableIface import IterableIface
from .Iterator import Iterator
from .IteratorIface import IteratorIface
from .Lazy import Lazy
from .LazyClass import LazyClass
from .LazyPrivate import LazyPrivate
from .LinkedList import LinkedList
from .LinkedListClass import LinkedListClass
from .LinkedListPrivate import LinkedListPrivate
from .ListIface import ListIface
from .ListIterator import ListIterator
from .ListIteratorIface import ListIteratorIface
from .MapEntry import MapEntry
from .MapEntryClass import MapEntryClass
from .MapEntryPrivate import MapEntryPrivate
from .MapIface import MapIface
from .MapIterator import MapIterator
from .MapIteratorIface import MapIteratorIface
from .MultiMapIface import MultiMapIface
from .MultiSetIface import MultiSetIface
from .PriorityQueue import PriorityQueue
from .PriorityQueueClass import PriorityQueueClass
from .PriorityQueuePrivate import PriorityQueuePrivate
from .Promise import Promise
from .PromiseClass import PromiseClass
from .PromisePrivate import PromisePrivate
from .QueueIface import QueueIface
from .SetIface import SetIface
from .SortedMapIface import SortedMapIface
from .SortedSetIface import SortedSetIface
from .TraversableIface import TraversableIface
from .TraversableStream import TraversableStream
from .TreeMap import TreeMap
from .TreeMapClass import TreeMapClass
from .TreeMapPrivate import TreeMapPrivate
from .TreeMultiMap import TreeMultiMap
from .TreeMultiMapClass import TreeMultiMapClass
from .TreeMultiMapPrivate import TreeMultiMapPrivate
from .TreeMultiSet import TreeMultiSet
from .TreeMultiSetClass import TreeMultiSetClass
from .TreeMultiSetPrivate import TreeMultiSetPrivate
from .TreeSet import TreeSet
from .TreeSetClass import TreeSetClass
from .TreeSetPrivate import TreeSetPrivate
from .UnrolledLinkedList import UnrolledLinkedList
from .UnrolledLinkedListClass import UnrolledLinkedListClass
from .UnrolledLinkedListPrivate import UnrolledLinkedListPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f6a88b15d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Gee-0.8.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gee', loader=<gi.importer.DynamicImporter object at 0x7f6a88b15d00>)"

