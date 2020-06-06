# encoding: utf-8
# module gi.repository.Soup
# from /usr/lib64/girepository-1.0/Soup-2.4.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class MessageBody(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        MessageBody()
        new() -> Soup.MessageBody
    """
    def append(self, data): # real signature unknown; restored from __doc__
        """ append(self, data:list) """
        pass

    def append_buffer(self, buffer): # real signature unknown; restored from __doc__
        """ append_buffer(self, buffer:Soup.Buffer) """
        pass

    def complete(self): # real signature unknown; restored from __doc__
        """ complete(self) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def flatten(self): # real signature unknown; restored from __doc__
        """ flatten(self) -> Soup.Buffer """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_accumulate(self): # real signature unknown; restored from __doc__
        """ get_accumulate(self) -> bool """
        return False

    def get_chunk(self, offset): # real signature unknown; restored from __doc__
        """ get_chunk(self, offset:int) -> Soup.Buffer or None """
        pass

    def got_chunk(self, chunk): # real signature unknown; restored from __doc__
        """ got_chunk(self, chunk:Soup.Buffer) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Soup.MessageBody """
        pass

    def set_accumulate(self, accumulate): # real signature unknown; restored from __doc__
        """ set_accumulate(self, accumulate:bool) """
        pass

    def truncate(self): # real signature unknown; restored from __doc__
        """ truncate(self) """
        pass

    def wrote_chunk(self, chunk): # real signature unknown; restored from __doc__
        """ wrote_chunk(self, chunk:Soup.Buffer) """
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
        """ new() -> Soup.MessageBody """
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

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MessageBody), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupMessageBody (94750594804400)>, '__dict__': <attribute '__dict__' of 'MessageBody' objects>, '__weakref__': <attribute '__weakref__' of 'MessageBody' objects>, '__doc__': None, 'data': <property object at 0x7f8e47ee1810>, 'length': <property object at 0x7f8e47ee1900>, 'new': gi.FunctionInfo(new), 'append_buffer': gi.FunctionInfo(append_buffer), 'append': gi.FunctionInfo(append), 'complete': gi.FunctionInfo(complete), 'flatten': gi.FunctionInfo(flatten), 'free': gi.FunctionInfo(free), 'get_accumulate': gi.FunctionInfo(get_accumulate), 'get_chunk': gi.FunctionInfo(get_chunk), 'got_chunk': gi.FunctionInfo(got_chunk), 'set_accumulate': gi.FunctionInfo(set_accumulate), 'truncate': gi.FunctionInfo(truncate), 'wrote_chunk': gi.FunctionInfo(wrote_chunk), '__new__': <staticmethod object at 0x7f8e47ed3dc0>, '__init__': <function nothing at 0x7f8e4884dee0>})"
    __gtype__ = None # (!) real value is '<GType SoupMessageBody (94750594804400)>'
    __info__ = StructInfo(MessageBody)


