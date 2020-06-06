# encoding: utf-8
# module gi.repository.Grss
# from /usr/lib64/girepository-1.0/Grss-0.7.typelib
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


# Variables with simple values

_namespace = 'Grss'

_version = '0.7'

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

from .FeedFormatter import FeedFormatter
from .FeedAtomFormatter import FeedAtomFormatter
from .FeedAtomFormatterClass import FeedAtomFormatterClass
from .FeedAtomFormatterPrivate import FeedAtomFormatterPrivate
from .FeedChannel import FeedChannel
from .FeedChannelClass import FeedChannelClass
from .FeedChannelPrivate import FeedChannelPrivate
from .FeedEnclosure import FeedEnclosure
from .FeedEnclosureClass import FeedEnclosureClass
from .FeedEnclosurePrivate import FeedEnclosurePrivate
from .FeedFormatterClass import FeedFormatterClass
from .FeedFormatterPrivate import FeedFormatterPrivate
from .FeedItem import FeedItem
from .FeedItemClass import FeedItemClass
from .FeedItemPrivate import FeedItemPrivate
from .FeedParser import FeedParser
from .FeedParserClass import FeedParserClass
from .FeedParserPrivate import FeedParserPrivate
from .FeedRssFormatter import FeedRssFormatter
from .FeedRssFormatterClass import FeedRssFormatterClass
from .FeedRssFormatterPrivate import FeedRssFormatterPrivate
from .FeedsGroup import FeedsGroup
from .FeedsGroupClass import FeedsGroupClass
from .FeedsGroupPrivate import FeedsGroupPrivate
from .FeedsPool import FeedsPool
from .FeedsPoolClass import FeedsPoolClass
from .FeedsPoolPrivate import FeedsPoolPrivate
from .FeedsPublisher import FeedsPublisher
from .FeedsPublisherClass import FeedsPublisherClass
from .FeedsPublisherPrivate import FeedsPublisherPrivate
from .FeedsStore import FeedsStore
from .FeedsStoreClass import FeedsStoreClass
from .FeedsStorePrivate import FeedsStorePrivate
from .FeedsSubscriber import FeedsSubscriber
from .FeedsSubscriberClass import FeedsSubscriberClass
from .FeedsSubscriberPrivate import FeedsSubscriberPrivate
from .Person import Person
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f68fb764d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Grss-0.7.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Grss', loader=<gi.importer.DynamicImporter object at 0x7f68fb764d00>)"

