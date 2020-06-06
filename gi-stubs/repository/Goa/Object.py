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


class Object(__gobject.GInterface):
    # no doc
    def get_account(self): # real signature unknown; restored from __doc__
        """ get_account(self) -> Goa.Account or None """
        pass

    def get_calendar(self): # real signature unknown; restored from __doc__
        """ get_calendar(self) -> Goa.Calendar or None """
        pass

    def get_chat(self): # real signature unknown; restored from __doc__
        """ get_chat(self) -> Goa.Chat or None """
        pass

    def get_contacts(self): # real signature unknown; restored from __doc__
        """ get_contacts(self) -> Goa.Contacts or None """
        pass

    def get_documents(self): # real signature unknown; restored from __doc__
        """ get_documents(self) -> Goa.Documents or None """
        pass

    def get_exchange(self): # real signature unknown; restored from __doc__
        """ get_exchange(self) -> Goa.Exchange or None """
        pass

    def get_files(self): # real signature unknown; restored from __doc__
        """ get_files(self) -> Goa.Files or None """
        pass

    def get_mail(self): # real signature unknown; restored from __doc__
        """ get_mail(self) -> Goa.Mail or None """
        pass

    def get_manager(self): # real signature unknown; restored from __doc__
        """ get_manager(self) -> Goa.Manager or None """
        pass

    def get_maps(self): # real signature unknown; restored from __doc__
        """ get_maps(self) -> Goa.Maps or None """
        pass

    def get_media_server(self): # real signature unknown; restored from __doc__
        """ get_media_server(self) -> Goa.MediaServer or None """
        pass

    def get_music(self): # real signature unknown; restored from __doc__
        """ get_music(self) -> Goa.Music or None """
        pass

    def get_oauth2_based(self): # real signature unknown; restored from __doc__
        """ get_oauth2_based(self) -> Goa.OAuth2Based or None """
        pass

    def get_oauth_based(self): # real signature unknown; restored from __doc__
        """ get_oauth_based(self) -> Goa.OAuthBased or None """
        pass

    def get_password_based(self): # real signature unknown; restored from __doc__
        """ get_password_based(self) -> Goa.PasswordBased or None """
        pass

    def get_photos(self): # real signature unknown; restored from __doc__
        """ get_photos(self) -> Goa.Photos or None """
        pass

    def get_printers(self): # real signature unknown; restored from __doc__
        """ get_printers(self) -> Goa.Printers or None """
        pass

    def get_read_later(self): # real signature unknown; restored from __doc__
        """ get_read_later(self) -> Goa.ReadLater or None """
        pass

    def get_ticketing(self): # real signature unknown; restored from __doc__
        """ get_ticketing(self) -> Goa.Ticketing or None """
        pass

    def get_todo(self): # real signature unknown; restored from __doc__
        """ get_todo(self) -> Goa.Todo or None """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Object), '__module__': 'gi.repository.Goa', '__gtype__': <GType GoaObject (94357271042464)>, '__dict__': <attribute '__dict__' of 'Object' objects>, '__weakref__': <attribute '__weakref__' of 'Object' objects>, '__doc__': None, '__gsignals__': {}, 'get_account': gi.FunctionInfo(get_account), 'get_calendar': gi.FunctionInfo(get_calendar), 'get_chat': gi.FunctionInfo(get_chat), 'get_contacts': gi.FunctionInfo(get_contacts), 'get_documents': gi.FunctionInfo(get_documents), 'get_exchange': gi.FunctionInfo(get_exchange), 'get_files': gi.FunctionInfo(get_files), 'get_mail': gi.FunctionInfo(get_mail), 'get_manager': gi.FunctionInfo(get_manager), 'get_maps': gi.FunctionInfo(get_maps), 'get_media_server': gi.FunctionInfo(get_media_server), 'get_music': gi.FunctionInfo(get_music), 'get_oauth2_based': gi.FunctionInfo(get_oauth2_based), 'get_oauth_based': gi.FunctionInfo(get_oauth_based), 'get_password_based': gi.FunctionInfo(get_password_based), 'get_photos': gi.FunctionInfo(get_photos), 'get_printers': gi.FunctionInfo(get_printers), 'get_read_later': gi.FunctionInfo(get_read_later), 'get_ticketing': gi.FunctionInfo(get_ticketing), 'get_todo': gi.FunctionInfo(get_todo)})"
    __gdoc__ = 'Interface GoaObject\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GoaObject (94357271042464)>'
    __info__ = InterfaceInfo(Object)


