# encoding: utf-8
# module gi.repository.Colord
# from /usr/lib64/girepository-1.0/Colord-1.0.typelib
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
import gobject as __gobject


# Variables with simple values

CLIENT_PROPERTY_DAEMON_VERSION = 'DaemonVersion'

CLIENT_PROPERTY_SYSTEM_MODEL = 'SystemModel'
CLIENT_PROPERTY_SYSTEM_VENDOR = 'SystemVendor'

DEVICE_METADATA_OUTPUT_EDID_MD5 = 'OutputEdidMd5'

DEVICE_METADATA_OUTPUT_PRIORITY = 'OutputPriority'

DEVICE_METADATA_OUTPUT_PRIORITY_PRIMARY = 'primary'
DEVICE_METADATA_OUTPUT_PRIORITY_SECONDARY = 'secondary'

DEVICE_METADATA_OWNER_CMDLINE = 'OwnerCmdline'

DEVICE_METADATA_XRANDR_NAME = 'XRANDR_name'

DEVICE_PROPERTY_COLORSPACE = 'Colorspace'
DEVICE_PROPERTY_CREATED = 'Created'
DEVICE_PROPERTY_EMBEDDED = 'Embedded'
DEVICE_PROPERTY_ENABLED = 'Enabled'
DEVICE_PROPERTY_FORMAT = 'Format'
DEVICE_PROPERTY_ID = 'DeviceId'
DEVICE_PROPERTY_KIND = 'Kind'
DEVICE_PROPERTY_METADATA = 'Metadata'
DEVICE_PROPERTY_MODE = 'Mode'
DEVICE_PROPERTY_MODEL = 'Model'
DEVICE_PROPERTY_MODIFIED = 'Modified'
DEVICE_PROPERTY_OWNER = 'Owner'
DEVICE_PROPERTY_PROFILES = 'Profiles'

DEVICE_PROPERTY_PROFILING_INHIBITORS = 'ProfilingInhibitors'

DEVICE_PROPERTY_SCOPE = 'Scope'
DEVICE_PROPERTY_SEAT = 'Seat'
DEVICE_PROPERTY_SERIAL = 'Serial'
DEVICE_PROPERTY_VENDOR = 'Vendor'

PIXEL_FORMAT_ARGB32 = 278681
PIXEL_FORMAT_BGRA32 = 279705
PIXEL_FORMAT_CMYK32 = 393249
PIXEL_FORMAT_RGB24 = 262169
PIXEL_FORMAT_RGBA32 = 262297
PIXEL_FORMAT_UNKNOWN = 0

PROFILE_METADATA_ACCURACY_DE76_AVG = 'ACCURACY_dE76_avg'
PROFILE_METADATA_ACCURACY_DE76_MAX = 'ACCURACY_dE76_max'
PROFILE_METADATA_ACCURACY_DE76_RMS = 'ACCURACY_dE76_rms'

PROFILE_METADATA_CMF_BINARY = 'CMF_binary'
PROFILE_METADATA_CMF_PRODUCT = 'CMF_product'
PROFILE_METADATA_CMF_VERSION = 'CMF_version'

PROFILE_METADATA_CONNECTION_TYPE = 'CONNECTION_type'

PROFILE_METADATA_CONNECTION_TYPE_DISPLAYPORT = 'displayport'
PROFILE_METADATA_CONNECTION_TYPE_DVI = 'dvi'
PROFILE_METADATA_CONNECTION_TYPE_HDMI = 'hdmi'
PROFILE_METADATA_CONNECTION_TYPE_INTERNAL = 'internal'
PROFILE_METADATA_CONNECTION_TYPE_VGA = 'vga'

PROFILE_METADATA_DATA_SOURCE = 'DATA_source'

PROFILE_METADATA_DATA_SOURCE_CALIB = 'calib'
PROFILE_METADATA_DATA_SOURCE_EDID = 'edid'
PROFILE_METADATA_DATA_SOURCE_STANDARD = 'standard'
PROFILE_METADATA_DATA_SOURCE_TEST = 'test'

PROFILE_METADATA_EDID_MD5 = 'EDID_md5'
PROFILE_METADATA_EDID_MNFT = 'EDID_mnft'
PROFILE_METADATA_EDID_MODEL = 'EDID_model'
PROFILE_METADATA_EDID_SERIAL = 'EDID_serial'
PROFILE_METADATA_EDID_VENDOR = 'EDID_manufacturer'

PROFILE_METADATA_FILE_CHECKSUM = 'FILE_checksum'

PROFILE_METADATA_LICENSE = 'License'

PROFILE_METADATA_MAPPING_DEVICE_ID = 'MAPPING_device_id'

PROFILE_METADATA_MAPPING_FORMAT = 'MAPPING_format'
PROFILE_METADATA_MAPPING_QUALIFIER = 'MAPPING_qualifier'

PROFILE_METADATA_MEASUREMENT_DEVICE = 'MEASUREMENT_device'

PROFILE_METADATA_QUALITY = 'Quality'

PROFILE_METADATA_QUALITY_HIGH = 'high'
PROFILE_METADATA_QUALITY_LOW = 'low'
PROFILE_METADATA_QUALITY_MEDIUM = 'medium'

PROFILE_METADATA_SCREEN_BRIGHTNESS = 'SCREEN_brightness'
PROFILE_METADATA_SCREEN_SURFACE = 'SCREEN_surface'

PROFILE_METADATA_SCREEN_SURFACE_GLOSSY = 'glossy'
PROFILE_METADATA_SCREEN_SURFACE_MATTE = 'matte'

PROFILE_METADATA_STANDARD_SPACE = 'STANDARD_space'

PROFILE_PROPERTY_COLORSPACE = 'Colorspace'
PROFILE_PROPERTY_CREATED = 'Created'
PROFILE_PROPERTY_FILENAME = 'Filename'
PROFILE_PROPERTY_FORMAT = 'Format'

PROFILE_PROPERTY_HAS_VCGT = 'HasVcgt'

PROFILE_PROPERTY_ID = 'ProfileId'

PROFILE_PROPERTY_IS_SYSTEM_WIDE = 'IsSystemWide'

PROFILE_PROPERTY_KIND = 'Kind'
PROFILE_PROPERTY_METADATA = 'Metadata'
PROFILE_PROPERTY_OWNER = 'Owner'
PROFILE_PROPERTY_QUALIFIER = 'Qualifier'
PROFILE_PROPERTY_SCOPE = 'Scope'
PROFILE_PROPERTY_TITLE = 'Title'
PROFILE_PROPERTY_WARNINGS = 'Warnings'

SENSOR_METADATA_IMAGE_ATTACH = 'ImageAttach'
SENSOR_METADATA_IMAGE_CALIBRATE = 'ImageCalibrate'
SENSOR_METADATA_IMAGE_SCREEN = 'ImageScreen'

SENSOR_PROPERTY_CAPABILITIES = 'Capabilities'
SENSOR_PROPERTY_EMBEDDED = 'Embedded'
SENSOR_PROPERTY_ID = 'SensorId'
SENSOR_PROPERTY_KIND = 'Kind'
SENSOR_PROPERTY_LOCKED = 'Locked'
SENSOR_PROPERTY_METADATA = 'Metadata'
SENSOR_PROPERTY_MODE = 'Mode'
SENSOR_PROPERTY_MODEL = 'Model'
SENSOR_PROPERTY_NATIVE = 'Native'
SENSOR_PROPERTY_OPTIONS = 'Options'
SENSOR_PROPERTY_SERIAL = 'Serial'
SENSOR_PROPERTY_STATE = 'State'
SENSOR_PROPERTY_VENDOR = 'Vendor'

_namespace = 'Colord'

_version = '1.0'

__weakref__ = None

# functions

def colorspace_from_string(colorspace): # real signature unknown; restored from __doc__
    """ colorspace_from_string(colorspace:str) -> Colord.Colorspace """
    pass

def colorspace_to_string(colorspace): # real signature unknown; restored from __doc__
    """ colorspace_to_string(colorspace:Colord.Colorspace) -> str """
    return ""

def color_get_blackbody_rgb(temp, result): # real signature unknown; restored from __doc__
    """ color_get_blackbody_rgb(temp:int, result:Colord.ColorRGB) -> bool """
    return False

def color_get_blackbody_rgb_full(temp, result, flags): # real signature unknown; restored from __doc__
    """ color_get_blackbody_rgb_full(temp:float, result:Colord.ColorRGB, flags:Colord.ColorBlackbodyFlags) -> bool """
    return False

def color_rgb8_to_rgb(src, dest): # real signature unknown; restored from __doc__
    """ color_rgb8_to_rgb(src:Colord.ColorRGB8, dest:Colord.ColorRGB) """
    pass

def color_rgb_array_interpolate(array, new_length): # real signature unknown; restored from __doc__
    """ color_rgb_array_interpolate(array:list, new_length:int) -> list """
    return []

def color_rgb_array_is_monotonic(array): # real signature unknown; restored from __doc__
    """ color_rgb_array_is_monotonic(array:list) -> bool """
    return False

def color_rgb_array_new(): # real signature unknown; restored from __doc__
    """ color_rgb_array_new() -> list """
    return []

def mat33_clear(src): # real signature unknown; restored from __doc__
    """ mat33_clear(src:Colord.Mat3x3) """
    pass

def mat33_copy(src, dest): # real signature unknown; restored from __doc__
    """ mat33_copy(src:Colord.Mat3x3, dest:Colord.Mat3x3) """
    pass

def mat33_determinant(src): # real signature unknown; restored from __doc__
    """ mat33_determinant(src:Colord.Mat3x3) -> float """
    return 0.0

def mat33_get_data(src): # real signature unknown; restored from __doc__
    """ mat33_get_data(src:Colord.Mat3x3) -> float """
    return 0.0

def mat33_init(dest, m00, m01, m02, m10, m11, m12, m20, m21, m22): # real signature unknown; restored from __doc__
    """ mat33_init(dest:Colord.Mat3x3, m00:float, m01:float, m02:float, m10:float, m11:float, m12:float, m20:float, m21:float, m22:float) """
    pass

def mat33_matrix_multiply(mat_src1, mat_src2, mat_dest): # real signature unknown; restored from __doc__
    """ mat33_matrix_multiply(mat_src1:Colord.Mat3x3, mat_src2:Colord.Mat3x3, mat_dest:Colord.Mat3x3) """
    pass

def mat33_normalize(src, dest): # real signature unknown; restored from __doc__
    """ mat33_normalize(src:Colord.Mat3x3, dest:Colord.Mat3x3) """
    pass

def mat33_reciprocal(src, dest): # real signature unknown; restored from __doc__
    """ mat33_reciprocal(src:Colord.Mat3x3, dest:Colord.Mat3x3) -> bool """
    return False

def mat33_scalar_multiply(mat_src, value, mat_dest): # real signature unknown; restored from __doc__
    """ mat33_scalar_multiply(mat_src:Colord.Mat3x3, value:float, mat_dest:Colord.Mat3x3) """
    pass

def mat33_set_identity(src): # real signature unknown; restored from __doc__
    """ mat33_set_identity(src:Colord.Mat3x3) """
    pass

def mat33_to_string(src): # real signature unknown; restored from __doc__
    """ mat33_to_string(src:Colord.Mat3x3) -> str """
    return ""

def mat33_vector_multiply(mat_src, vec_src, vec_dest): # real signature unknown; restored from __doc__
    """ mat33_vector_multiply(mat_src:Colord.Mat3x3, vec_src:Colord.Vec3, vec_dest:Colord.Vec3) """
    pass

def object_scope_from_string(object_scope): # real signature unknown; restored from __doc__
    """ object_scope_from_string(object_scope:str) -> Colord.ObjectScope """
    pass

def object_scope_to_string(object_scope): # real signature unknown; restored from __doc__
    """ object_scope_to_string(object_scope:Colord.ObjectScope) -> str """
    return ""

def pixel_format_from_string(pixel_format): # real signature unknown; restored from __doc__
    """ pixel_format_from_string(pixel_format:str) -> int """
    return 0

def pixel_format_to_string(pixel_format): # real signature unknown; restored from __doc__
    """ pixel_format_to_string(pixel_format:int) -> str """
    return ""

def rendering_intent_from_string(rendering_intent): # real signature unknown; restored from __doc__
    """ rendering_intent_from_string(rendering_intent:str) -> Colord.RenderingIntent """
    pass

def rendering_intent_to_string(rendering_intent): # real signature unknown; restored from __doc__
    """ rendering_intent_to_string(rendering_intent:Colord.RenderingIntent) -> str """
    return ""

def standard_space_from_string(standard_space): # real signature unknown; restored from __doc__
    """ standard_space_from_string(standard_space:str) -> Colord.StandardSpace """
    pass

def standard_space_to_string(standard_space): # real signature unknown; restored from __doc__
    """ standard_space_to_string(standard_space:Colord.StandardSpace) -> str """
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

from .Client import Client
from .ClientClass import ClientClass
from .ClientError import ClientError
from .ColorBlackbodyFlags import ColorBlackbodyFlags
from .ColorLab import ColorLab
from .ColorRGB import ColorRGB
from .ColorRGB8 import ColorRGB8
from .Colorspace import Colorspace
from .ColorSwatch import ColorSwatch
from .ColorUVW import ColorUVW
from .ColorXYZ import ColorXYZ
from .ColorYxy import ColorYxy
from .Device import Device
from .DeviceClass import DeviceClass
from .DeviceError import DeviceError
from .DeviceKind import DeviceKind
from .DeviceMode import DeviceMode
from .DeviceRelation import DeviceRelation
from .Edid import Edid
from .EdidClass import EdidClass
from .Icc import Icc
from .IccClass import IccClass
from .IccError import IccError
from .IccLoadFlags import IccLoadFlags
from .IccSaveFlags import IccSaveFlags
from .It8 import It8
from .It8Class import It8Class
from .It8Error import It8Error
from .It8Kind import It8Kind
from .Mat3x3 import Mat3x3
from .ObjectScope import ObjectScope
from .Profile import Profile
from .ProfileClass import ProfileClass
from .ProfileError import ProfileError
from .ProfileKind import ProfileKind
from .ProfileQuality import ProfileQuality
from .ProfileWarning import ProfileWarning
from .RenderingIntent import RenderingIntent
from .Sensor import Sensor
from .SensorCap import SensorCap
from .SensorClass import SensorClass
from .SensorError import SensorError
from .SensorKind import SensorKind
from .SensorState import SensorState
from .Spectrum import Spectrum
from .StandardSpace import StandardSpace
from .Vec3 import Vec3
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f09141e8d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Colord-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Colord', loader=<gi.importer.DynamicImporter object at 0x7f09141e8d00>)"

