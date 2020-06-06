# encoding: utf-8
# module gi.repository.EDataBook
# from /usr/lib64/girepository-1.0/EDataBook-1.2.typelib
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
import gi.repository.EBackend as __gi_repository_EBackend
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


# Variables with simple values

BOOK_SQL_IS_POPULATED_KEY = 'eds-reserved-namespace-is-populated'

BOOK_SQL_SYNC_DATA_KEY = 'eds-reserved-namespace-sync-data'

EDS_ADDRESS_BOOK_MODULES = 'EDS_ADDRESS_BOOK_MODULES'

EDS_SUBPROCESS_BOOK_PATH = 'EDS_SUBPROCESS_BOOK_PATH'

XIMIAN_VCARD = 'BEGIN:VCARD\nX-EVOLUTION-FILE-AS:Novell Ximian Group\nADR;TYPE=WORK:;Suite 500;8 Cambridge Center;Cambridge;MA;02142;USA\nLABEL;TYPE=WORK:8 Cambridge Center, Suite 500\\nCambridge\\, MA\\n02142\\nUSA\nTEL;WORK;VOICE:(617) 613-2000\nTEL;WORK;FAX:(617) 613-2001\nEMAIL;INTERNET:hello@ximian.com\nURL:http://www.ximian.com/\nORG:Novell;Ximian Group\nPHOTO;ENCODING=b;TYPE=JPEG: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\nEND:VCARD'

_namespace = 'EDataBook'

_version = '1.2'

__weakref__ = None

# functions

def book_cache_search_data_free(data=None): # real signature unknown; restored from __doc__
    """ book_cache_search_data_free(data=None) """
    pass

def book_meta_backend_info_free(ptr=None): # real signature unknown; restored from __doc__
    """ book_meta_backend_info_free(ptr=None) """
    pass

def ebsql_get_contact_extra_unlocked(ebsql, uid): # real signature unknown; restored from __doc__
    """ ebsql_get_contact_extra_unlocked(ebsql:EDataBook.BookSqlite, uid:str) -> bool, ret_extra:str """
    return False

def ebsql_get_contact_unlocked(ebsql, uid, meta_contact): # real signature unknown; restored from __doc__
    """ ebsql_get_contact_unlocked(ebsql:EDataBook.BookSqlite, uid:str, meta_contact:bool) -> bool, contact:EBookContacts.Contact """
    return False

def ebsql_get_vcard_unlocked(ebsql, uid, meta_contact): # real signature unknown; restored from __doc__
    """ ebsql_get_vcard_unlocked(ebsql:EDataBook.BookSqlite, uid:str, meta_contact:bool) -> bool, ret_vcard:str """
    return False

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

from .BookBackend import BookBackend
from .BookBackendClass import BookBackendClass
from .BookBackendFactory import BookBackendFactory
from .BookBackendFactoryClass import BookBackendFactoryClass
from .BookBackendFactoryPrivate import BookBackendFactoryPrivate
from .BookBackendPrivate import BookBackendPrivate
from .BookBackendSExp import BookBackendSExp
from .BookBackendSExpClass import BookBackendSExpClass
from .BookBackendSExpPrivate import BookBackendSExpPrivate
from .BookBackendSync import BookBackendSync
from .BookBackendSyncClass import BookBackendSyncClass
from .BookBackendSyncPrivate import BookBackendSyncPrivate
from .BookCache import BookCache
from .BookCacheClass import BookCacheClass
from .BookCacheCursor import BookCacheCursor
from .BookCacheCursorOrigin import BookCacheCursorOrigin
from .BookCacheCursorStepFlags import BookCacheCursorStepFlags
from .BookCachePrivate import BookCachePrivate
from .BookCacheSearchData import BookCacheSearchData
from .BookMetaBackend import BookMetaBackend
from .BookMetaBackendClass import BookMetaBackendClass
from .BookMetaBackendInfo import BookMetaBackendInfo
from .BookMetaBackendPrivate import BookMetaBackendPrivate
from .BookSqlite import BookSqlite
from .BookSqliteClass import BookSqliteClass
from .BookSqliteError import BookSqliteError
from .BookSqlitePrivate import BookSqlitePrivate
from .bSqlChangeType import bSqlChangeType
from .bSqlCursor import bSqlCursor
from .bSqlCursorOrigin import bSqlCursorOrigin
from .bSqlCursorStepFlags import bSqlCursorStepFlags
from .bSqlLockType import bSqlLockType
from .bSqlSearchData import bSqlSearchData
from .bSqlUnlockAction import bSqlUnlockAction
from .DataBook import DataBook
from .DataBookClass import DataBookClass
from .DataBookCursor import DataBookCursor
from .DataBookCursorCache import DataBookCursorCache
from .DataBookCursorCacheClass import DataBookCursorCacheClass
from .DataBookCursorCachePrivate import DataBookCursorCachePrivate
from .DataBookCursorClass import DataBookCursorClass
from .DataBookCursorPrivate import DataBookCursorPrivate
from .DataBookCursorSqlite import DataBookCursorSqlite
from .DataBookCursorSqliteClass import DataBookCursorSqliteClass
from .DataBookCursorSqlitePrivate import DataBookCursorSqlitePrivate
from .DataBookDirect import DataBookDirect
from .DataBookDirectClass import DataBookDirectClass
from .DataBookDirectPrivate import DataBookDirectPrivate
from .DataBookFactory import DataBookFactory
from .DataBookFactoryClass import DataBookFactoryClass
from .DataBookFactoryPrivate import DataBookFactoryPrivate
from .DataBookPrivate import DataBookPrivate
from .DataBookView import DataBookView
from .DataBookViewClass import DataBookViewClass
from .DataBookViewPrivate import DataBookViewPrivate
from .SubprocessBookFactory import SubprocessBookFactory
from .SubprocessBookFactoryClass import SubprocessBookFactoryClass
from .SubprocessBookFactoryPrivate import SubprocessBookFactoryPrivate
from .SystemLocaleWatcher import SystemLocaleWatcher
from .SystemLocaleWatcherClass import SystemLocaleWatcherClass
from .SystemLocaleWatcherPrivate import SystemLocaleWatcherPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f09d50a3d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/EDataBook-1.2.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.EDataBook', loader=<gi.importer.DynamicImporter object at 0x7f09d50a3d00>)"

