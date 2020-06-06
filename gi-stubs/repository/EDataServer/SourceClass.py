# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


class SourceClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        SourceClass()
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

    authenticate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    credentials_required = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_oauth2_access_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_oauth2_access_token_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_oauth2_access_token_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    invoke_authenticate_impl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    invoke_credentials_required_impl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remote_create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remote_create_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remote_create_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remote_delete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remote_delete_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remote_delete_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unset_last_credentials_required_arguments_impl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SourceClass), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'SourceClass' objects>, '__weakref__': <attribute '__weakref__' of 'SourceClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f626e91fe00>, 'changed': <property object at 0x7f626e91fef0>, 'credentials_required': <property object at 0x7f626e923090>, 'authenticate': <property object at 0x7f626e923180>, 'remove_sync': <property object at 0x7f626e923270>, 'remove': <property object at 0x7f626e923360>, 'remove_finish': <property object at 0x7f626e923450>, 'write_sync': <property object at 0x7f626e923540>, 'write': <property object at 0x7f626e923630>, 'write_finish': <property object at 0x7f626e923720>, 'remote_create_sync': <property object at 0x7f626e923860>, 'remote_create': <property object at 0x7f626e923900>, 'remote_create_finish': <property object at 0x7f626e923a40>, 'remote_delete_sync': <property object at 0x7f626e923b30>, 'remote_delete': <property object at 0x7f626e923bd0>, 'remote_delete_finish': <property object at 0x7f626e923d10>, 'get_oauth2_access_token_sync': <property object at 0x7f626e923e00>, 'get_oauth2_access_token': <property object at 0x7f626e923ef0>, 'get_oauth2_access_token_finish': <property object at 0x7f626e922040>, 'invoke_credentials_required_impl': <property object at 0x7f626e9220e0>, 'invoke_authenticate_impl': <property object at 0x7f626e922220>, 'unset_last_credentials_required_arguments_impl': <property object at 0x7f626e922310>, 'reserved': <property object at 0x7f626e922400>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(SourceClass)


