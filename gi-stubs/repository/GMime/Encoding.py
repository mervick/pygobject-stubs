# encoding: utf-8
# module gi.repository.GMime
# from /usr/lib64/girepository-1.0/GMime-3.0.typelib
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


class Encoding(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Encoding()
    """
    def base64_decode_step(self, inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
        """ base64_decode_step(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
        return 0

    def base64_encode_close(self, inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
        """ base64_encode_close(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
        return 0

    def base64_encode_step(self, inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
        """ base64_encode_step(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
        return 0

    def flush(self, inbuf, inlen, outbuf): # real signature unknown; restored from __doc__
        """ flush(self, inbuf:str, inlen:int, outbuf:str) -> int """
        return 0

    def init_decode(self, encoding): # real signature unknown; restored from __doc__
        """ init_decode(self, encoding:GMime.ContentEncoding) """
        pass

    def init_encode(self, encoding): # real signature unknown; restored from __doc__
        """ init_encode(self, encoding:GMime.ContentEncoding) """
        pass

    def outlen(self, inlen): # real signature unknown; restored from __doc__
        """ outlen(self, inlen:int) -> int """
        return 0

    def quoted_decode_step(self, inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
        """ quoted_decode_step(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
        return 0

    def quoted_encode_close(self, inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
        """ quoted_encode_close(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
        return 0

    def quoted_encode_step(self, inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
        """ quoted_encode_step(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def step(self, inbuf, inlen, outbuf): # real signature unknown; restored from __doc__
        """ step(self, inbuf:str, inlen:int, outbuf:str) -> int """
        return 0

    def uudecode_step(self, inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
        """ uudecode_step(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
        return 0

    def uuencode_close(self, inbuf, inlen, outbuf, uubuf, state, save): # real signature unknown; restored from __doc__
        """ uuencode_close(inbuf:int, inlen:int, outbuf:int, uubuf:int, state:int, save:int) -> int """
        return 0

    def uuencode_step(self, inbuf, inlen, outbuf, uubuf, state, save): # real signature unknown; restored from __doc__
        """ uuencode_step(inbuf:int, inlen:int, outbuf:int, uubuf:int, state:int, save:int) -> int """
        return 0

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

    encode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    save = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uubuf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Encoding), '__module__': 'gi.repository.GMime', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Encoding' objects>, '__weakref__': <attribute '__weakref__' of 'Encoding' objects>, '__doc__': None, 'encoding': <property object at 0x7fc9708d5770>, 'uubuf': <property object at 0x7fc9708d5860>, 'encode': <property object at 0x7fc9708d5950>, 'save': <property object at 0x7fc9708d5a40>, 'state': <property object at 0x7fc9708d5b30>, 'flush': gi.FunctionInfo(flush), 'init_decode': gi.FunctionInfo(init_decode), 'init_encode': gi.FunctionInfo(init_encode), 'outlen': gi.FunctionInfo(outlen), 'reset': gi.FunctionInfo(reset), 'step': gi.FunctionInfo(step), 'base64_decode_step': gi.FunctionInfo(base64_decode_step), 'base64_encode_close': gi.FunctionInfo(base64_encode_close), 'base64_encode_step': gi.FunctionInfo(base64_encode_step), 'quoted_decode_step': gi.FunctionInfo(quoted_decode_step), 'quoted_encode_close': gi.FunctionInfo(quoted_encode_close), 'quoted_encode_step': gi.FunctionInfo(quoted_encode_step), 'uudecode_step': gi.FunctionInfo(uudecode_step), 'uuencode_close': gi.FunctionInfo(uuencode_close), 'uuencode_step': gi.FunctionInfo(uuencode_step)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Encoding)


