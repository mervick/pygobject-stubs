# encoding: utf-8
# module gi.repository.GstSdp
# from /usr/lib64/girepository-1.0/GstSdp-1.0.typelib
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

MIKEY_VERSION = 1

SDP_BWTYPE_AS = 'AS'
SDP_BWTYPE_CT = 'CT'

SDP_BWTYPE_EXT_PREFIX = 'X-'

SDP_BWTYPE_RR = 'RR'
SDP_BWTYPE_RS = 'RS'
SDP_BWTYPE_TIAS = 'TIAS'

_namespace = 'GstSdp'

_version = '1.0'

__weakref__ = None

# functions

def sdp_address_is_multicast(nettype, addrtype, addr): # real signature unknown; restored from __doc__
    """ sdp_address_is_multicast(nettype:str, addrtype:str, addr:str) -> bool """
    return False

def sdp_make_keymgmt(uri, base64): # real signature unknown; restored from __doc__
    """ sdp_make_keymgmt(uri:str, base64:str) -> str """
    return ""

def sdp_media_new(): # real signature unknown; restored from __doc__
    """ sdp_media_new() -> GstSdp.SDPResult, media:GstSdp.SDPMedia """
    pass

def sdp_media_set_media_from_caps(caps, media): # real signature unknown; restored from __doc__
    """ sdp_media_set_media_from_caps(caps:Gst.Caps, media:GstSdp.SDPMedia) -> GstSdp.SDPResult """
    pass

def sdp_message_as_uri(scheme, msg): # real signature unknown; restored from __doc__
    """ sdp_message_as_uri(scheme:str, msg:GstSdp.SDPMessage) -> str """
    return ""

def sdp_message_new(): # real signature unknown; restored from __doc__
    """ sdp_message_new() -> GstSdp.SDPResult, msg:GstSdp.SDPMessage """
    pass

def sdp_message_new_from_text(text): # real signature unknown; restored from __doc__
    """ sdp_message_new_from_text(text:str) -> GstSdp.SDPResult, msg:GstSdp.SDPMessage """
    pass

def sdp_message_parse_buffer(data, msg): # real signature unknown; restored from __doc__
    """ sdp_message_parse_buffer(data:list, msg:GstSdp.SDPMessage) -> GstSdp.SDPResult """
    pass

def sdp_message_parse_uri(uri, msg): # real signature unknown; restored from __doc__
    """ sdp_message_parse_uri(uri:str, msg:GstSdp.SDPMessage) -> GstSdp.SDPResult """
    pass

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

from .MIKEYCacheType import MIKEYCacheType
from .MIKEYDecryptInfo import MIKEYDecryptInfo
from .MIKEYEncAlg import MIKEYEncAlg
from .MIKEYEncryptInfo import MIKEYEncryptInfo
from .MIKEYKeyDataType import MIKEYKeyDataType
from .MIKEYKVType import MIKEYKVType
from .MIKEYMacAlg import MIKEYMacAlg
from .MIKEYMapSRTP import MIKEYMapSRTP
from .MIKEYMapType import MIKEYMapType
from .MIKEYMessage import MIKEYMessage
from .MIKEYPayload import MIKEYPayload
from .MIKEYPayloadKEMAC import MIKEYPayloadKEMAC
from .MIKEYPayloadKeyData import MIKEYPayloadKeyData
from .MIKEYPayloadPKE import MIKEYPayloadPKE
from .MIKEYPayloadRAND import MIKEYPayloadRAND
from .MIKEYPayloadSP import MIKEYPayloadSP
from .MIKEYPayloadSPParam import MIKEYPayloadSPParam
from .MIKEYPayloadT import MIKEYPayloadT
from .MIKEYPayloadType import MIKEYPayloadType
from .MIKEYPRFFunc import MIKEYPRFFunc
from .MIKEYSecProto import MIKEYSecProto
from .MIKEYSecSRTP import MIKEYSecSRTP
from .MIKEYTSType import MIKEYTSType
from .MIKEYType import MIKEYType
from .SDPAttribute import SDPAttribute
from .SDPBandwidth import SDPBandwidth
from .SDPConnection import SDPConnection
from .SDPKey import SDPKey
from .SDPMedia import SDPMedia
from .SDPMessage import SDPMessage
from .SDPOrigin import SDPOrigin
from .SDPResult import SDPResult
from .SDPTime import SDPTime
from .SDPZone import SDPZone
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f89a6e9ad00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GstSdp-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GstSdp', loader=<gi.importer.DynamicImporter object at 0x7f89a6e9ad00>)"

