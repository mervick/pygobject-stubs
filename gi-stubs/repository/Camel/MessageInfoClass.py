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


class MessageInfoClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MessageInfoClass()
    """
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

    clone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dup_user_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dup_user_tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_cc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_date_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_date_sent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_from = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_message_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mlist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_references = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_user_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_user_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_user_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_user_tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    load = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    save = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_cc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_date_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_date_sent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_from = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_message_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_mlist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_user_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_user_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    take_headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    take_references = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    take_user_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    take_user_tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MessageInfoClass), '__module__': 'gi.repository.Camel', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MessageInfoClass' objects>, '__weakref__': <attribute '__weakref__' of 'MessageInfoClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f7b34f79b80>, 'clone': <property object at 0x7f7b34f79c70>, 'load': <property object at 0x7f7b34f79d60>, 'save': <property object at 0x7f7b34f79e50>, 'get_flags': <property object at 0x7f7b34f79f40>, 'set_flags': <property object at 0x7f7b34f7b090>, 'get_user_flag': <property object at 0x7f7b34f7b180>, 'set_user_flag': <property object at 0x7f7b34f7b270>, 'get_user_flags': <property object at 0x7f7b34f7b360>, 'dup_user_flags': <property object at 0x7f7b34f7b450>, 'take_user_flags': <property object at 0x7f7b34f7b540>, 'get_user_tag': <property object at 0x7f7b34f7b630>, 'set_user_tag': <property object at 0x7f7b34f7b720>, 'get_user_tags': <property object at 0x7f7b34f7b810>, 'dup_user_tags': <property object at 0x7f7b34f7b900>, 'take_user_tags': <property object at 0x7f7b34f7b9f0>, 'get_subject': <property object at 0x7f7b34f7bae0>, 'set_subject': <property object at 0x7f7b34f7bbd0>, 'get_from': <property object at 0x7f7b34f7bcc0>, 'set_from': <property object at 0x7f7b34f7bdb0>, 'get_to': <property object at 0x7f7b34f7bea0>, 'set_to': <property object at 0x7f7b34f7bf90>, 'get_cc': <property object at 0x7f7b34f7c0e0>, 'set_cc': <property object at 0x7f7b34f7c1d0>, 'get_mlist': <property object at 0x7f7b34f7c2c0>, 'set_mlist': <property object at 0x7f7b34f7c3b0>, 'get_size': <property object at 0x7f7b34f7c4a0>, 'set_size': <property object at 0x7f7b34f7c590>, 'get_date_sent': <property object at 0x7f7b34f7c680>, 'set_date_sent': <property object at 0x7f7b34f7c770>, 'get_date_received': <property object at 0x7f7b34f7c8b0>, 'set_date_received': <property object at 0x7f7b34f7c9a0>, 'get_message_id': <property object at 0x7f7b34f7ca40>, 'set_message_id': <property object at 0x7f7b34f7cb30>, 'get_references': <property object at 0x7f7b34f7cc20>, 'take_references': <property object at 0x7f7b34f7cd10>, 'get_headers': <property object at 0x7f7b34f7ce00>, 'take_headers': <property object at 0x7f7b34f7cef0>, 'reserved': <property object at 0x7f7b34f7d040>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MessageInfoClass)


