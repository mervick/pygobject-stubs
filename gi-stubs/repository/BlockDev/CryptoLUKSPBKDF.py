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


from .CryptoLUKSPBKDF import CryptoLUKSPBKDF

class CryptoLUKSPBKDF(CryptoLUKSPBKDF):
    """
    :Constructors:
    
    ::
    
        CryptoLUKSPBKDF()
        new(type:str=None, hash:str=None, max_memory_kb:int, iterations:int, time_ms:int, parallel_threads:int) -> BlockDev.CryptoLUKSPBKDF
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def new(self, type=None, hash=None, max_memory_kb, iterations, time_ms, parallel_threads): # real signature unknown; restored from __doc__
        """ new(type:str=None, hash:str=None, max_memory_kb:int, iterations:int, time_ms:int, parallel_threads:int) -> BlockDev.CryptoLUKSPBKDF """
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

    def __init__(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, type=None, hash=None, max_memory_kb=0, iterations=0, time_ms=0, parallel_threads=0): # reliably restored by inspect
        # no doc
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

    hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iterations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_memory_kb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parallel_threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_ms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.BlockDev', '__new__': <staticmethod object at 0x7fa27bbc51f0>, '__init__': <function CryptoLUKSPBKDF.__init__ at 0x7fa27bbc4af0>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType BDCryptoLUKSPBKDF (94066389118848)>'
    __info__ = StructInfo(CryptoLUKSPBKDF)


