# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


class MessageContentInfo(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        MessageContentInfo()
        new() -> Camel.MessageContentInfo
        new_from_headers(headers:Camel.NameValueArray) -> Camel.MessageContentInfo
        new_from_message(mime_part:Camel.MimePart) -> Camel.MessageContentInfo
        new_from_parser(parser:Camel.MimeParser) -> Camel.MessageContentInfo
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Camel.MessageContentInfo """
        pass

    def dump(self, depth): # real signature unknown; restored from __doc__
        """ dump(self, depth:int) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Camel.MessageContentInfo """
        pass

    def new_from_headers(self, headers): # real signature unknown; restored from __doc__
        """ new_from_headers(headers:Camel.NameValueArray) -> Camel.MessageContentInfo """
        pass

    def new_from_message(self, mime_part): # real signature unknown; restored from __doc__
        """ new_from_message(mime_part:Camel.MimePart) -> Camel.MessageContentInfo """
        pass

    def new_from_parser(self, parser): # real signature unknown; restored from __doc__
        """ new_from_parser(parser:Camel.MimeParser) -> Camel.MessageContentInfo """
        pass

    def traverse(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ traverse(self, func:Camel.MessageContentInfoTraverseCallback, user_data=None) -> bool """
        return False

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
        """ new() -> Camel.MessageContentInfo """
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

    childs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    disposition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MessageContentInfo), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelMessageContentInfo (94124523620144)>, '__dict__': <attribute '__dict__' of 'MessageContentInfo' objects>, '__weakref__': <attribute '__weakref__' of 'MessageContentInfo' objects>, '__doc__': None, 'next': <property object at 0x7f7b34f746d0>, 'childs': <property object at 0x7f7b34f747c0>, 'parent': <property object at 0x7f7b34f748b0>, 'type': <property object at 0x7f7b34f749a0>, 'disposition': <property object at 0x7f7b34f74a90>, 'id': <property object at 0x7f7b34f74b80>, 'description': <property object at 0x7f7b34f74c70>, 'encoding': <property object at 0x7f7b34f74d60>, 'size': <property object at 0x7f7b34f74e50>, 'new': gi.FunctionInfo(new), 'new_from_headers': gi.FunctionInfo(new_from_headers), 'new_from_message': gi.FunctionInfo(new_from_message), 'new_from_parser': gi.FunctionInfo(new_from_parser), 'copy': gi.FunctionInfo(copy), 'dump': gi.FunctionInfo(dump), 'free': gi.FunctionInfo(free), 'traverse': gi.FunctionInfo(traverse), '__new__': <staticmethod object at 0x7f7b34f70790>, '__init__': <function nothing at 0x7f7b37797ee0>})"
    __gtype__ = None # (!) real value is '<GType CamelMessageContentInfo (94124523620144)>'
    __info__ = StructInfo(MessageContentInfo)


