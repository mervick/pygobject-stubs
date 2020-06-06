# encoding: utf-8
# module gi.repository.GstRtsp
# from /usr/lib64/girepository-1.0/GstRtsp-1.0.typelib
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
import gobject as __gobject


class RTSPConnection(__gi.Struct):
    # no doc
    def accept(self, socket, cancellable=None): # real signature unknown; restored from __doc__
        """ accept(socket:Gio.Socket, cancellable:Gio.Cancellable=None) -> GstRtsp.RTSPResult, conn:GstRtsp.RTSPConnection """
        pass

    def clear_auth_params(self): # real signature unknown; restored from __doc__
        """ clear_auth_params(self) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> GstRtsp.RTSPResult """
        pass

    def connect(self, timeout): # real signature unknown; restored from __doc__
        """ connect(self, timeout:GLib.TimeVal) -> GstRtsp.RTSPResult """
        pass

    def connect_with_response(self, timeout, response): # real signature unknown; restored from __doc__
        """ connect_with_response(self, timeout:GLib.TimeVal, response:GstRtsp.RTSPMessage) -> GstRtsp.RTSPResult """
        pass

    def create(self, url): # real signature unknown; restored from __doc__
        """ create(url:GstRtsp.RTSPUrl) -> GstRtsp.RTSPResult, conn:GstRtsp.RTSPConnection """
        pass

    def create_from_socket(self, socket, ip, port, initial_buffer): # real signature unknown; restored from __doc__
        """ create_from_socket(socket:Gio.Socket, ip:str, port:int, initial_buffer:str) -> GstRtsp.RTSPResult, conn:GstRtsp.RTSPConnection """
        pass

    def do_tunnel(self, conn2): # real signature unknown; restored from __doc__
        """ do_tunnel(self, conn2:GstRtsp.RTSPConnection) -> GstRtsp.RTSPResult """
        pass

    def flush(self, flush): # real signature unknown; restored from __doc__
        """ flush(self, flush:bool) -> GstRtsp.RTSPResult """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) -> GstRtsp.RTSPResult """
        pass

    def get_ip(self): # real signature unknown; restored from __doc__
        """ get_ip(self) -> str """
        return ""

    def get_read_socket(self): # real signature unknown; restored from __doc__
        """ get_read_socket(self) -> Gio.Socket """
        pass

    def get_remember_session_id(self): # real signature unknown; restored from __doc__
        """ get_remember_session_id(self) -> bool """
        return False

    def get_tls(self): # real signature unknown; restored from __doc__
        """ get_tls(self) -> Gio.TlsConnection """
        pass

    def get_tls_database(self): # real signature unknown; restored from __doc__
        """ get_tls_database(self) -> Gio.TlsDatabase """
        pass

    def get_tls_interaction(self): # real signature unknown; restored from __doc__
        """ get_tls_interaction(self) -> Gio.TlsInteraction """
        pass

    def get_tls_validation_flags(self): # real signature unknown; restored from __doc__
        """ get_tls_validation_flags(self) -> Gio.TlsCertificateFlags """
        pass

    def get_tunnelid(self): # real signature unknown; restored from __doc__
        """ get_tunnelid(self) -> str """
        return ""

    def get_url(self): # real signature unknown; restored from __doc__
        """ get_url(self) -> GstRtsp.RTSPUrl """
        pass

    def get_write_socket(self): # real signature unknown; restored from __doc__
        """ get_write_socket(self) -> Gio.Socket """
        pass

    def is_tunneled(self): # real signature unknown; restored from __doc__
        """ is_tunneled(self) -> bool """
        return False

    def next_timeout(self, timeout): # real signature unknown; restored from __doc__
        """ next_timeout(self, timeout:GLib.TimeVal) -> GstRtsp.RTSPResult """
        pass

    def poll(self, events, revents, timeout): # real signature unknown; restored from __doc__
        """ poll(self, events:GstRtsp.RTSPEvent, revents:GstRtsp.RTSPEvent, timeout:GLib.TimeVal) -> GstRtsp.RTSPResult """
        pass

    def read(self, data, size, timeout): # real signature unknown; restored from __doc__
        """ read(self, data:int, size:int, timeout:GLib.TimeVal) -> GstRtsp.RTSPResult """
        pass

    def receive(self, message, timeout): # real signature unknown; restored from __doc__
        """ receive(self, message:GstRtsp.RTSPMessage, timeout:GLib.TimeVal) -> GstRtsp.RTSPResult """
        pass

    def reset_timeout(self): # real signature unknown; restored from __doc__
        """ reset_timeout(self) -> GstRtsp.RTSPResult """
        pass

    def send(self, message, timeout): # real signature unknown; restored from __doc__
        """ send(self, message:GstRtsp.RTSPMessage, timeout:GLib.TimeVal) -> GstRtsp.RTSPResult """
        pass

    def send_messages(self, messages, timeout): # real signature unknown; restored from __doc__
        """ send_messages(self, messages:list, timeout:GLib.TimeVal) -> GstRtsp.RTSPResult """
        pass

    def set_accept_certificate_func(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ set_accept_certificate_func(self, func:GstRtsp.RTSPConnectionAcceptCertificateFunc, user_data=None) """
        pass

    def set_auth(self, method, user, pass_): # real signature unknown; restored from __doc__
        """ set_auth(self, method:GstRtsp.RTSPAuthMethod, user:str, pass_:str) -> GstRtsp.RTSPResult """
        pass

    def set_auth_param(self, param, value): # real signature unknown; restored from __doc__
        """ set_auth_param(self, param:str, value:str) """
        pass

    def set_http_mode(self, enable): # real signature unknown; restored from __doc__
        """ set_http_mode(self, enable:bool) """
        pass

    def set_ip(self, ip): # real signature unknown; restored from __doc__
        """ set_ip(self, ip:str) """
        pass

    def set_proxy(self, host, port): # real signature unknown; restored from __doc__
        """ set_proxy(self, host:str, port:int) -> GstRtsp.RTSPResult """
        pass

    def set_qos_dscp(self, qos_dscp): # real signature unknown; restored from __doc__
        """ set_qos_dscp(self, qos_dscp:int) -> GstRtsp.RTSPResult """
        pass

    def set_remember_session_id(self, remember): # real signature unknown; restored from __doc__
        """ set_remember_session_id(self, remember:bool) """
        pass

    def set_tls_database(self, database): # real signature unknown; restored from __doc__
        """ set_tls_database(self, database:Gio.TlsDatabase) """
        pass

    def set_tls_interaction(self, interaction): # real signature unknown; restored from __doc__
        """ set_tls_interaction(self, interaction:Gio.TlsInteraction) """
        pass

    def set_tls_validation_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_tls_validation_flags(self, flags:Gio.TlsCertificateFlags) -> bool """
        return False

    def set_tunneled(self, tunneled): # real signature unknown; restored from __doc__
        """ set_tunneled(self, tunneled:bool) """
        pass

    def write(self, data, size, timeout): # real signature unknown; restored from __doc__
        """ write(self, data:int, size:int, timeout:GLib.TimeVal) -> GstRtsp.RTSPResult """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RTSPConnection), '__module__': 'gi.repository.GstRtsp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RTSPConnection' objects>, '__weakref__': <attribute '__weakref__' of 'RTSPConnection' objects>, '__doc__': None, 'clear_auth_params': gi.FunctionInfo(clear_auth_params), 'close': gi.FunctionInfo(close), 'connect': gi.FunctionInfo(connect), 'connect_with_response': gi.FunctionInfo(connect_with_response), 'do_tunnel': gi.FunctionInfo(do_tunnel), 'flush': gi.FunctionInfo(flush), 'free': gi.FunctionInfo(free), 'get_ip': gi.FunctionInfo(get_ip), 'get_read_socket': gi.FunctionInfo(get_read_socket), 'get_remember_session_id': gi.FunctionInfo(get_remember_session_id), 'get_tls': gi.FunctionInfo(get_tls), 'get_tls_database': gi.FunctionInfo(get_tls_database), 'get_tls_interaction': gi.FunctionInfo(get_tls_interaction), 'get_tls_validation_flags': gi.FunctionInfo(get_tls_validation_flags), 'get_tunnelid': gi.FunctionInfo(get_tunnelid), 'get_url': gi.FunctionInfo(get_url), 'get_write_socket': gi.FunctionInfo(get_write_socket), 'is_tunneled': gi.FunctionInfo(is_tunneled), 'next_timeout': gi.FunctionInfo(next_timeout), 'poll': gi.FunctionInfo(poll), 'read': gi.FunctionInfo(read), 'receive': gi.FunctionInfo(receive), 'reset_timeout': gi.FunctionInfo(reset_timeout), 'send': gi.FunctionInfo(send), 'send_messages': gi.FunctionInfo(send_messages), 'set_accept_certificate_func': gi.FunctionInfo(set_accept_certificate_func), 'set_auth': gi.FunctionInfo(set_auth), 'set_auth_param': gi.FunctionInfo(set_auth_param), 'set_http_mode': gi.FunctionInfo(set_http_mode), 'set_ip': gi.FunctionInfo(set_ip), 'set_proxy': gi.FunctionInfo(set_proxy), 'set_qos_dscp': gi.FunctionInfo(set_qos_dscp), 'set_remember_session_id': gi.FunctionInfo(set_remember_session_id), 'set_tls_database': gi.FunctionInfo(set_tls_database), 'set_tls_interaction': gi.FunctionInfo(set_tls_interaction), 'set_tls_validation_flags': gi.FunctionInfo(set_tls_validation_flags), 'set_tunneled': gi.FunctionInfo(set_tunneled), 'write': gi.FunctionInfo(write), 'accept': gi.FunctionInfo(accept), 'create': gi.FunctionInfo(create), 'create_from_socket': gi.FunctionInfo(create_from_socket)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RTSPConnection)


