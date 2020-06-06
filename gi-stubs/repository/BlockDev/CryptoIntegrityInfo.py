# encoding: utf-8
# module gi.repository.BlockDev
# from /usr/lib64/girepository-1.0/BlockDev-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.BlockDev as __gi_overrides_BlockDev
import gobject as __gobject


class CryptoIntegrityInfo(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        CryptoIntegrityInfo()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> BlockDev.CryptoIntegrityInfo """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interleave_sectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    journal_crypt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    journal_integrity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    journal_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sector_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tag_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CryptoIntegrityInfo), '__module__': 'gi.repository.BlockDev', '__gtype__': <GType BDCryptoIntegrityInfo (94066389605440)>, '__dict__': <attribute '__dict__' of 'CryptoIntegrityInfo' objects>, '__weakref__': <attribute '__weakref__' of 'CryptoIntegrityInfo' objects>, '__doc__': None, 'algorithm': <property object at 0x7fa27ba0ebd0>, 'key_size': <property object at 0x7fa27ba0ecc0>, 'sector_size': <property object at 0x7fa27ba0edb0>, 'tag_size': <property object at 0x7fa27ba0eea0>, 'interleave_sectors': <property object at 0x7fa27ba10040>, 'journal_size': <property object at 0x7fa27ba10130>, 'journal_crypt': <property object at 0x7fa27ba10220>, 'journal_integrity': <property object at 0x7fa27ba10360>, 'copy': gi.FunctionInfo(copy)})"
    __gtype__ = None # (!) real value is '<GType BDCryptoIntegrityInfo (94066389605440)>'
    __info__ = StructInfo(CryptoIntegrityInfo)


