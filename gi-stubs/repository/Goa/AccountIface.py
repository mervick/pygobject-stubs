# encoding: utf-8
# module gi.repository.Goa
# from /usr/lib64/girepository-1.0/Goa-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class AccountIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        AccountIface()
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

    get_attention_needed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_calendar_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_chat_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_contacts_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_documents_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_files_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_identity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_is_locked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_is_temporary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mail_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_maps_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_music_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_photos_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_presentation_identity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_printers_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_provider_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_provider_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_provider_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_read_later_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_ticketing_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_todo_disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_ensure_credentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AccountIface), '__module__': 'gi.repository.Goa', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AccountIface' objects>, '__weakref__': <attribute '__weakref__' of 'AccountIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f37f4cfff40>, 'handle_ensure_credentials': <property object at 0x7f37f4cfb040>, 'handle_remove': <property object at 0x7f37f4cfb090>, 'get_attention_needed': <property object at 0x7f37f4cfb130>, 'get_calendar_disabled': <property object at 0x7f37f4cfb270>, 'get_chat_disabled': <property object at 0x7f37f4cfb3b0>, 'get_contacts_disabled': <property object at 0x7f37f4cfb4f0>, 'get_documents_disabled': <property object at 0x7f37f4cfb630>, 'get_id': <property object at 0x7f37f4cfb720>, 'get_identity': <property object at 0x7f37f4cfb810>, 'get_is_temporary': <property object at 0x7f37f4cfb950>, 'get_mail_disabled': <property object at 0x7f37f4cfba90>, 'get_presentation_identity': <property object at 0x7f37f4cfbbd0>, 'get_provider_icon': <property object at 0x7f37f4cfbd10>, 'get_provider_name': <property object at 0x7f37f4cfbe50>, 'get_provider_type': <property object at 0x7f37f4cfbf90>, 'get_ticketing_disabled': <property object at 0x7f37f4d00130>, 'get_files_disabled': <property object at 0x7f37f4d00270>, 'get_photos_disabled': <property object at 0x7f37f4d003b0>, 'get_printers_disabled': <property object at 0x7f37f4d004f0>, 'get_read_later_disabled': <property object at 0x7f37f4d00630>, 'get_maps_disabled': <property object at 0x7f37f4d00770>, 'get_is_locked': <property object at 0x7f37f4d00860>, 'get_music_disabled': <property object at 0x7f37f4d009a0>, 'get_todo_disabled': <property object at 0x7f37f4d00ae0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AccountIface)


