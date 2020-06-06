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


class OAuth2Service(__gobject.GInterface):
    # no doc
    def can_process(self, source): # real signature unknown; restored from __doc__
        """ can_process(self, source:EDataServer.Source) -> bool """
        return False

    def delete_token_sync(self, source, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_token_sync(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def extract_authorization_code(self, source, page_title, page_uri, page_content=None): # real signature unknown; restored from __doc__
        """ extract_authorization_code(self, source:EDataServer.Source, page_title:str, page_uri:str, page_content:str=None) -> bool, out_authorization_code:str """
        return False

    def get_access_token_sync(self, source, ref_source, ref_source_user_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_access_token_sync(self, source:EDataServer.Source, ref_source:EDataServer.OAuth2ServiceRefSourceFunc, ref_source_user_data=None, cancellable:Gio.Cancellable=None) -> bool, out_access_token:str, out_expires_in:int """
        return False

    def get_authentication_policy(self, source, uri): # real signature unknown; restored from __doc__
        """ get_authentication_policy(self, source:EDataServer.Source, uri:str) -> EDataServer.OAuth2ServiceNavigationPolicy """
        pass

    def get_authentication_uri(self, source): # real signature unknown; restored from __doc__
        """ get_authentication_uri(self, source:EDataServer.Source) -> str """
        return ""

    def get_client_id(self, source): # real signature unknown; restored from __doc__
        """ get_client_id(self, source:EDataServer.Source) -> str """
        return ""

    def get_client_secret(self, source): # real signature unknown; restored from __doc__
        """ get_client_secret(self, source:EDataServer.Source) -> str or None """
        return ""

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_redirect_uri(self, source): # real signature unknown; restored from __doc__
        """ get_redirect_uri(self, source:EDataServer.Source) -> str or None """
        return ""

    def get_refresh_uri(self, source): # real signature unknown; restored from __doc__
        """ get_refresh_uri(self, source:EDataServer.Source) -> str """
        return ""

    def guess_can_process(self, protocol=None, hostname=None): # real signature unknown; restored from __doc__
        """ guess_can_process(self, protocol:str=None, hostname:str=None) -> bool """
        return False

    def prepare_authentication_uri_query(self, source, uri_query): # real signature unknown; restored from __doc__
        """ prepare_authentication_uri_query(self, source:EDataServer.Source, uri_query:dict) """
        pass

    def prepare_get_token_form(self, source, authorization_code, form): # real signature unknown; restored from __doc__
        """ prepare_get_token_form(self, source:EDataServer.Source, authorization_code:str, form:dict) """
        pass

    def prepare_get_token_message(self, source, message): # real signature unknown; restored from __doc__
        """ prepare_get_token_message(self, source:EDataServer.Source, message:Soup.Message) """
        pass

    def prepare_refresh_token_form(self, source, refresh_token, form): # real signature unknown; restored from __doc__
        """ prepare_refresh_token_form(self, source:EDataServer.Source, refresh_token:str, form:dict) """
        pass

    def prepare_refresh_token_message(self, source, message): # real signature unknown; restored from __doc__
        """ prepare_refresh_token_message(self, source:EDataServer.Source, message:Soup.Message) """
        pass

    def receive_and_store_token_sync(self, source, authorization_code, ref_source, ref_source_user_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ receive_and_store_token_sync(self, source:EDataServer.Source, authorization_code:str, ref_source:EDataServer.OAuth2ServiceRefSourceFunc, ref_source_user_data=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def refresh_and_store_token_sync(self, source, refresh_token, ref_source, ref_source_user_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ refresh_and_store_token_sync(self, source:EDataServer.Source, refresh_token:str, ref_source:EDataServer.OAuth2ServiceRefSourceFunc, ref_source_user_data=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def util_set_to_form(self, form, name, value=None): # real signature unknown; restored from __doc__
        """ util_set_to_form(form:dict, name:str, value:str=None) """
        pass

    def util_take_to_form(self, form, name, value=None): # real signature unknown; restored from __doc__
        """ util_take_to_form(form:dict, name:str, value:str=None) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(OAuth2Service), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType EOAuth2Service (94877536999152)>, '__dict__': <attribute '__dict__' of 'OAuth2Service' objects>, '__weakref__': <attribute '__weakref__' of 'OAuth2Service' objects>, '__doc__': None, '__gsignals__': {}, 'util_set_to_form': gi.FunctionInfo(util_set_to_form), 'util_take_to_form': gi.FunctionInfo(util_take_to_form), 'can_process': gi.FunctionInfo(can_process), 'delete_token_sync': gi.FunctionInfo(delete_token_sync), 'extract_authorization_code': gi.FunctionInfo(extract_authorization_code), 'get_access_token_sync': gi.FunctionInfo(get_access_token_sync), 'get_authentication_policy': gi.FunctionInfo(get_authentication_policy), 'get_authentication_uri': gi.FunctionInfo(get_authentication_uri), 'get_client_id': gi.FunctionInfo(get_client_id), 'get_client_secret': gi.FunctionInfo(get_client_secret), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_flags': gi.FunctionInfo(get_flags), 'get_name': gi.FunctionInfo(get_name), 'get_redirect_uri': gi.FunctionInfo(get_redirect_uri), 'get_refresh_uri': gi.FunctionInfo(get_refresh_uri), 'guess_can_process': gi.FunctionInfo(guess_can_process), 'prepare_authentication_uri_query': gi.FunctionInfo(prepare_authentication_uri_query), 'prepare_get_token_form': gi.FunctionInfo(prepare_get_token_form), 'prepare_get_token_message': gi.FunctionInfo(prepare_get_token_message), 'prepare_refresh_token_form': gi.FunctionInfo(prepare_refresh_token_form), 'prepare_refresh_token_message': gi.FunctionInfo(prepare_refresh_token_message), 'receive_and_store_token_sync': gi.FunctionInfo(receive_and_store_token_sync), 'refresh_and_store_token_sync': gi.FunctionInfo(refresh_and_store_token_sync)})"
    __gdoc__ = 'Interface EOAuth2Service\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EOAuth2Service (94877536999152)>'
    __info__ = InterfaceInfo(OAuth2Service)


