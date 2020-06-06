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


class References(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        References()
        new() -> GMime.References
    """
    def append(self, msgid): # real signature unknown; restored from __doc__
        """ append(self, msgid:str) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GMime.References """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_message_id(self, index): # real signature unknown; restored from __doc__
        """ get_message_id(self, index:int) -> str """
        return ""

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GMime.References """
        pass

    def parse(self, options=None, text): # real signature unknown; restored from __doc__
        """ parse(options:GMime.ParserOptions=None, text:str) -> GMime.References """
        pass

    def set_message_id(self, index, msgid): # real signature unknown; restored from __doc__
        """ set_message_id(self, index:int, msgid:str) """
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> GMime.References """
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

    array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(References), '__module__': 'gi.repository.GMime', '__gtype__': <GType GMimeReferences (94235496201056)>, '__dict__': <attribute '__dict__' of 'References' objects>, '__weakref__': <attribute '__weakref__' of 'References' objects>, '__doc__': None, 'array': <property object at 0x7fc97074c4a0>, 'new': gi.FunctionInfo(new), 'append': gi.FunctionInfo(append), 'clear': gi.FunctionInfo(clear), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_message_id': gi.FunctionInfo(get_message_id), 'length': gi.FunctionInfo(length), 'set_message_id': gi.FunctionInfo(set_message_id), 'parse': gi.FunctionInfo(parse), '__new__': <staticmethod object at 0x7fc970741ee0>, '__init__': <function nothing at 0x7fc970afcee0>})"
    __gtype__ = None # (!) real value is '<GType GMimeReferences (94235496201056)>'
    __info__ = StructInfo(References)


