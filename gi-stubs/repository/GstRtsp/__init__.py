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


# Variables with simple values

RTSP_DEFAULT_PORT = 554

_namespace = 'GstRtsp'

_version = '1.0'

__weakref__ = None

# functions

def rtsp_auth_credentials_free(credentials): # real signature unknown; restored from __doc__
    """ rtsp_auth_credentials_free(credentials:GstRtsp.RTSPAuthCredential) """
    pass

def rtsp_connection_accept(socket, cancellable=None): # real signature unknown; restored from __doc__
    """ rtsp_connection_accept(socket:Gio.Socket, cancellable:Gio.Cancellable=None) -> GstRtsp.RTSPResult, conn:GstRtsp.RTSPConnection """
    pass

def rtsp_connection_create(url): # real signature unknown; restored from __doc__
    """ rtsp_connection_create(url:GstRtsp.RTSPUrl) -> GstRtsp.RTSPResult, conn:GstRtsp.RTSPConnection """
    pass

def rtsp_connection_create_from_socket(socket, ip, port, initial_buffer): # real signature unknown; restored from __doc__
    """ rtsp_connection_create_from_socket(socket:Gio.Socket, ip:str, port:int, initial_buffer:str) -> GstRtsp.RTSPResult, conn:GstRtsp.RTSPConnection """
    pass

def rtsp_find_header_field(header): # real signature unknown; restored from __doc__
    """ rtsp_find_header_field(header:str) -> GstRtsp.RTSPHeaderField """
    pass

def rtsp_find_method(method): # real signature unknown; restored from __doc__
    """ rtsp_find_method(method:str) -> GstRtsp.RTSPMethod """
    pass

def rtsp_generate_digest_auth_response(algorithm=None, method, realm, username, password, uri, nonce): # real signature unknown; restored from __doc__
    """ rtsp_generate_digest_auth_response(algorithm:str=None, method:str, realm:str, username:str, password:str, uri:str, nonce:str) -> str """
    return ""

def rtsp_generate_digest_auth_response_from_md5(algorithm=None, method, md5, uri, nonce): # real signature unknown; restored from __doc__
    """ rtsp_generate_digest_auth_response_from_md5(algorithm:str=None, method:str, md5:str, uri:str, nonce:str) -> str """
    return ""

def rtsp_header_allow_multiple(field): # real signature unknown; restored from __doc__
    """ rtsp_header_allow_multiple(field:GstRtsp.RTSPHeaderField) -> bool """
    return False

def rtsp_header_as_text(field): # real signature unknown; restored from __doc__
    """ rtsp_header_as_text(field:GstRtsp.RTSPHeaderField) -> str """
    return ""

def rtsp_message_new(): # real signature unknown; restored from __doc__
    """ rtsp_message_new() -> GstRtsp.RTSPResult, msg:GstRtsp.RTSPMessage """
    pass

def rtsp_message_new_data(channel): # real signature unknown; restored from __doc__
    """ rtsp_message_new_data(channel:int) -> GstRtsp.RTSPResult, msg:GstRtsp.RTSPMessage """
    pass

def rtsp_message_new_request(method, uri): # real signature unknown; restored from __doc__
    """ rtsp_message_new_request(method:GstRtsp.RTSPMethod, uri:str) -> GstRtsp.RTSPResult, msg:GstRtsp.RTSPMessage """
    pass

def rtsp_message_new_response(code, reason=None, request=None): # real signature unknown; restored from __doc__
    """ rtsp_message_new_response(code:GstRtsp.RTSPStatusCode, reason:str=None, request:GstRtsp.RTSPMessage=None) -> GstRtsp.RTSPResult, msg:GstRtsp.RTSPMessage """
    pass

def rtsp_method_as_text(method): # real signature unknown; restored from __doc__
    """ rtsp_method_as_text(method:GstRtsp.RTSPMethod) -> str """
    return ""

def rtsp_options_as_text(options): # real signature unknown; restored from __doc__
    """ rtsp_options_as_text(options:GstRtsp.RTSPMethod) -> str """
    return ""

def rtsp_options_from_text(options): # real signature unknown; restored from __doc__
    """ rtsp_options_from_text(options:str) -> GstRtsp.RTSPMethod """
    pass

def rtsp_range_convert_units(range, unit): # real signature unknown; restored from __doc__
    """ rtsp_range_convert_units(range:GstRtsp.RTSPTimeRange, unit:GstRtsp.RTSPRangeUnit) -> bool """
    return False

def rtsp_range_free(range): # real signature unknown; restored from __doc__
    """ rtsp_range_free(range:GstRtsp.RTSPTimeRange) """
    pass

def rtsp_range_get_times(range): # real signature unknown; restored from __doc__
    """ rtsp_range_get_times(range:GstRtsp.RTSPTimeRange) -> bool, min:int, max:int """
    return False

def rtsp_range_parse(rangestr): # real signature unknown; restored from __doc__
    """ rtsp_range_parse(rangestr:str) -> GstRtsp.RTSPResult, range:GstRtsp.RTSPTimeRange """
    pass

def rtsp_range_to_string(range): # real signature unknown; restored from __doc__
    """ rtsp_range_to_string(range:GstRtsp.RTSPTimeRange) -> str """
    return ""

def rtsp_status_as_text(code): # real signature unknown; restored from __doc__
    """ rtsp_status_as_text(code:GstRtsp.RTSPStatusCode) -> str """
    return ""

def rtsp_strresult(result): # real signature unknown; restored from __doc__
    """ rtsp_strresult(result:GstRtsp.RTSPResult) -> str """
    return ""

def rtsp_transport_get_manager(trans, option): # real signature unknown; restored from __doc__
    """ rtsp_transport_get_manager(trans:GstRtsp.RTSPTransMode, option:int) -> GstRtsp.RTSPResult, manager:str """
    pass

def rtsp_transport_get_mime(trans, mime): # real signature unknown; restored from __doc__
    """ rtsp_transport_get_mime(trans:GstRtsp.RTSPTransMode, mime:str) -> GstRtsp.RTSPResult """
    pass

def rtsp_transport_new(transport): # real signature unknown; restored from __doc__
    """ rtsp_transport_new(transport:GstRtsp.RTSPTransport) -> GstRtsp.RTSPResult """
    pass

def rtsp_transport_parse(p_str, transport): # real signature unknown; restored from __doc__
    """ rtsp_transport_parse(str:str, transport:GstRtsp.RTSPTransport) -> GstRtsp.RTSPResult """
    pass

def rtsp_url_parse(urlstr): # real signature unknown; restored from __doc__
    """ rtsp_url_parse(urlstr:str) -> GstRtsp.RTSPResult, url:GstRtsp.RTSPUrl """
    pass

def rtsp_version_as_text(version): # real signature unknown; restored from __doc__
    """ rtsp_version_as_text(version:GstRtsp.RTSPVersion) -> str """
    return ""

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .RTSPAuthCredential import RTSPAuthCredential
from .RTSPAuthMethod import RTSPAuthMethod
from .RTSPAuthParam import RTSPAuthParam
from .RTSPConnection import RTSPConnection
from .RTSPEvent import RTSPEvent
from .RTSPExtension import RTSPExtension
from .RTSPExtensionInterface import RTSPExtensionInterface
from .RTSPFamily import RTSPFamily
from .RTSPHeaderField import RTSPHeaderField
from .RTSPLowerTrans import RTSPLowerTrans
from .RTSPMessage import RTSPMessage
from .RTSPMethod import RTSPMethod
from .RTSPMsgType import RTSPMsgType
from .RTSPProfile import RTSPProfile
from .RTSPRange import RTSPRange
from .RTSPRangeUnit import RTSPRangeUnit
from .RTSPResult import RTSPResult
from .RTSPState import RTSPState
from .RTSPStatusCode import RTSPStatusCode
from .RTSPTime import RTSPTime
from .RTSPTime2 import RTSPTime2
from .RTSPTimeRange import RTSPTimeRange
from .RTSPTimeType import RTSPTimeType
from .RTSPTransMode import RTSPTransMode
from .RTSPTransport import RTSPTransport
from .RTSPUrl import RTSPUrl
from .RTSPVersion import RTSPVersion
from .RTSPWatch import RTSPWatch
from .RTSPWatchFuncs import RTSPWatchFuncs
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7ff1b4389d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GstRtsp-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GstRtsp', loader=<gi.importer.DynamicImporter object at 0x7ff1b4389d00>)"

