# encoding: utf-8
# module gi.repository.Colorhug
# from /usr/lib64/girepository-1.0/Colorhug-1.0.typelib
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

BUFFER_INPUT_CMD = 0
BUFFER_INPUT_DATA = 1

BUFFER_OUTPUT_CMD = 1
BUFFER_OUTPUT_DATA = 2
BUFFER_OUTPUT_RETVAL = 0

CALIBRATION_DESCRIPTION_LEN = 23

CALIBRATION_INDEX_CRT = 1

CALIBRATION_INDEX_FACTORY_ONLY = 0

CALIBRATION_INDEX_LCD = 0
CALIBRATION_INDEX_LED = 3
CALIBRATION_INDEX_MAX = 6
CALIBRATION_INDEX_PROJECTOR = 2

CALIBRATION_MAX = 64
CALIBRATION_SPECTRAL = 65535

CALIBRATION_TYPE_ALL = 255
CALIBRATION_TYPE_CRT = 2
CALIBRATION_TYPE_LCD = 1
CALIBRATION_TYPE_LED = 8
CALIBRATION_TYPE_PROJECTOR = 4

CCD_SPECTRAL_RESOLUTION = 1024

CMD_BOOT_FLASH = 39

CMD_CLEAR_ERROR = 97

CMD_ERASE_FLASH = 41

CMD_GET_ADC_CALIBRATION_NEG = 82
CMD_GET_ADC_CALIBRATION_POS = 81

CMD_GET_CALIBRATION = 9

CMD_GET_CALIBRATION_MAP = 46

CMD_GET_CCD_CALIBRATION = 83

CMD_GET_COLOR_SELECT = 1

CMD_GET_DAC_VALUE = 60

CMD_GET_DARK_OFFSETS = 15

CMD_GET_ERROR = 96

CMD_GET_FIRMWARE_VERSION = 7

CMD_GET_HARDWARE_VERSION = 48

CMD_GET_ILLUMINANTS = 21

CMD_GET_INTEGRAL_TIME = 5

CMD_GET_LEDS = 13

CMD_GET_MEASURE_MODE = 55

CMD_GET_MULTIPLIER = 3

CMD_GET_OWNER_EMAIL = 19
CMD_GET_OWNER_NAME = 17

CMD_GET_PCB_ERRATA = 51

CMD_GET_POST_SCALE = 42

CMD_GET_PRE_SCALE = 44

CMD_GET_REMOTE_HASH = 53

CMD_GET_SERIAL_NUMBER = 11

CMD_GET_TEMPERATURE = 59

CMD_LOAD_SRAM = 65

CMD_READ_FLASH = 37
CMD_READ_SRAM = 56

CMD_RESET = 36

CMD_SAVE_SRAM = 66

CMD_SELF_TEST = 64

CMD_SET_CALIBRATION = 10

CMD_SET_CALIBRATION_MAP = 47

CMD_SET_CCD_CALIBRATION = 84

CMD_SET_COLOR_SELECT = 2

CMD_SET_CRYPTO_KEY = 112

CMD_SET_DAC_VALUE = 61

CMD_SET_DARK_OFFSETS = 16

CMD_SET_FLASH_SUCCESS = 40

CMD_SET_ILLUMINANTS = 22

CMD_SET_INTEGRAL_TIME = 6

CMD_SET_LEDS = 14

CMD_SET_MEASURE_MODE = 54

CMD_SET_MULTIPLIER = 4

CMD_SET_OWNER_EMAIL = 20
CMD_SET_OWNER_NAME = 18

CMD_SET_PCB_ERRATA = 50

CMD_SET_POST_SCALE = 43

CMD_SET_PRE_SCALE = 45

CMD_SET_REMOTE_HASH = 52

CMD_SET_SERIAL_NUMBER = 12

CMD_TAKE_READINGS = 34

CMD_TAKE_READING_ARRAY = 49
CMD_TAKE_READING_RAW = 33
CMD_TAKE_READING_SPECTRAL = 85
CMD_TAKE_READING_XYZ = 35

CMD_WRITE_EEPROM = 32
CMD_WRITE_FLASH = 38
CMD_WRITE_SRAM = 57

DEVICE_GUID_COLORHUG = '40338ceb-b966-4eae-adae-9c32edfcc484'
DEVICE_GUID_COLORHUG2 = '2082b5e0-7a64-478a-b1b2-e3404fab6dad'

DEVICE_GUID_COLORHUG_ALS = '84f40464-9272-4ef7-9399-cd95f12da696'
DEVICE_GUID_COLORHUG_PLUS = '6d6f05a9-3ecb-43a2-bcbb-3844f1825366'

DEVICE_USB_TIMEOUT = 10000

EEPROM_ADDR_RUNCODE = 16384

EEPROM_ADDR_RUNCODE_ALS = 8192

EP0_TRANSFER_SIZE = 64

EP0_TRANSFER_SIZE_V2 = 1024

FIRMWARE_ID_TOKEN1 = '40338ceb'
FIRMWARE_ID_TOKEN2 = '2082b5e0'

FIRMWARE_ID_TOKEN_ALS = '84f40464'
FIRMWARE_ID_TOKEN_PLUS = '6d6f05a9'

FLASH_ERASE_BLOCK_SIZE = 1024

FLASH_RECONNECT_TIMEOUT = 5000

FLASH_TRANSFER_BLOCK_SIZE = 32

FLASH_WRITE_BLOCK_SIZE = 64

INTEGRAL_TIME_VALUE_100MS = 14848
INTEGRAL_TIME_VALUE_200MS = 29952
INTEGRAL_TIME_VALUE_50MS = 7936
INTEGRAL_TIME_VALUE_5MS = 768
INTEGRAL_TIME_VALUE_MAX = 65535

OWNER_LENGTH_MAX = 60

USB_CONFIG = 1

USB_HID_EP = 1

USB_HID_EP_IN = 128
USB_HID_EP_OUT = 0
USB_HID_EP_SIZE = 64

USB_INTERFACE = 0

USB_PID_BOOTLOADER = 4096
USB_PID_BOOTLOADER2 = 4101

USB_PID_BOOTLOADER_ALS = 4102
USB_PID_BOOTLOADER_DFU = 4106
USB_PID_BOOTLOADER_PLUS = 4099

USB_PID_FIRMWARE = 4097
USB_PID_FIRMWARE2 = 4100

USB_PID_FIRMWARE_ALS = 4103

USB_PID_FIRMWARE_ALS_SENSOR_HID = 4104

USB_PID_FIRMWARE_DFU = 4105
USB_PID_FIRMWARE_PLUS = 4098

USB_PID_LEGACY = 63706

USB_VID = 10047

USB_VID_LEGACY = 1240

WRITE_EEPROM_MAGIC = 'Un1c0rn2'

_namespace = 'Colorhug'

_version = '1.0'

__weakref__ = None

# functions

def color_select_to_string(color_select): # real signature unknown; restored from __doc__
    """ color_select_to_string(color_select:Colorhug.ColorSelect) -> str """
    return ""

def command_to_string(cmd): # real signature unknown; restored from __doc__
    """ command_to_string(cmd:int) -> str """
    return ""

def device_check_firmware(device, data, data_len): # real signature unknown; restored from __doc__
    """ device_check_firmware(device:GUsb.Device, data:int, data_len:int) -> bool """
    return False

def device_close(device): # real signature unknown; restored from __doc__
    """ device_close(device:GUsb.Device) -> bool """
    return False

def device_error_quark(): # real signature unknown; restored from __doc__
    """ device_error_quark() -> int """
    return 0

def device_get_adc_calibration_neg(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_adc_calibration_neg(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool, value:float """
    return False

def device_get_adc_calibration_pos(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_adc_calibration_pos(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool, value:float """
    return False

def device_get_ccd_calibration(device, nm_start, c0, c1, c2, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_ccd_calibration(device:GUsb.Device, nm_start:float, c0:float, c1:float, c2:float, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_get_error(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_error(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool, status:Colorhug.Error, cmd:int """
    return False

def device_get_guid(device): # real signature unknown; restored from __doc__
    """ device_get_guid(device:GUsb.Device) -> str """
    return ""

def device_get_illuminants(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_illuminants(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool, value:Colorhug.Illuminant """
    return False

def device_get_integral_time(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_integral_time(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool, value:int """
    return False

def device_get_leds(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_leds(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool, value:Colorhug.StatusLed """
    return False

def device_get_mode(device): # real signature unknown; restored from __doc__
    """ device_get_mode(device:GUsb.Device) -> Colorhug.DeviceMode """
    pass

def device_get_pcb_errata(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_pcb_errata(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool, value:Colorhug.PcbErrata """
    return False

def device_get_runcode_address(device): # real signature unknown; restored from __doc__
    """ device_get_runcode_address(device:GUsb.Device) -> int """
    return 0

def device_get_serial_number(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_serial_number(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool, value:int """
    return False

def device_get_spectrum(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_spectrum(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> Colord.Spectrum """
    pass

def device_get_spectrum_full(device, kind, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_spectrum_full(device:GUsb.Device, kind:Colorhug.SpectrumKind, cancellable:Gio.Cancellable=None) -> Colord.Spectrum """
    pass

def device_get_temperature(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_get_temperature(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool, value:float """
    return False

def device_is_colorhug(device): # real signature unknown; restored from __doc__
    """ device_is_colorhug(device:GUsb.Device) -> bool """
    return False

def device_load_sram(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_load_sram(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_mode_from_firmware(data, data_len): # real signature unknown; restored from __doc__
    """ device_mode_from_firmware(data:int, data_len:int) -> Colorhug.DeviceMode """
    pass

def device_mode_to_string(device_mode): # real signature unknown; restored from __doc__
    """ device_mode_to_string(device_mode:Colorhug.DeviceMode) -> str """
    return ""

def device_open(device): # real signature unknown; restored from __doc__
    """ device_open(device:GUsb.Device) -> bool """
    return False

def device_open_full(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_open_full(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_read_sram(device, addr, len, cancellable=None): # real signature unknown; restored from __doc__
    """ device_read_sram(device:GUsb.Device, addr:int, len:int, cancellable:Gio.Cancellable=None) -> GLib.Bytes """
    pass

def device_save_sram(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_save_sram(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_self_test(device, cancellable=None): # real signature unknown; restored from __doc__
    """ device_self_test(device:GUsb.Device, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_set_ccd_calibration(device, nm_start, c0, c1, c2, cancellable=None): # real signature unknown; restored from __doc__
    """ device_set_ccd_calibration(device:GUsb.Device, nm_start:float, c0:float, c1:float, c2:float, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_set_crypto_key(device, keys, cancellable=None): # real signature unknown; restored from __doc__
    """ device_set_crypto_key(device:GUsb.Device, keys:int, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_set_illuminants(device, value, cancellable=None): # real signature unknown; restored from __doc__
    """ device_set_illuminants(device:GUsb.Device, value:Colorhug.Illuminant, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_set_integral_time(device, value, cancellable=None): # real signature unknown; restored from __doc__
    """ device_set_integral_time(device:GUsb.Device, value:int, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_set_leds(device, value, cancellable=None): # real signature unknown; restored from __doc__
    """ device_set_leds(device:GUsb.Device, value:Colorhug.StatusLed, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_set_pcb_errata(device, value, cancellable=None): # real signature unknown; restored from __doc__
    """ device_set_pcb_errata(device:GUsb.Device, value:Colorhug.PcbErrata, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_set_serial_number(device, value, cancellable=None): # real signature unknown; restored from __doc__
    """ device_set_serial_number(device:GUsb.Device, value:int, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_set_spectrum_full(device, kind, sp, cancellable=None): # real signature unknown; restored from __doc__
    """ device_set_spectrum_full(device:GUsb.Device, kind:Colorhug.SpectrumKind, sp:Colord.Spectrum, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_take_reading_spectral(device, value, cancellable=None): # real signature unknown; restored from __doc__
    """ device_take_reading_spectral(device:GUsb.Device, value:Colorhug.SpectrumKind, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_take_reading_xyz(device, calibration_idx, cancellable=None): # real signature unknown; restored from __doc__
    """ device_take_reading_xyz(device:GUsb.Device, calibration_idx:int, cancellable:Gio.Cancellable=None) -> Colord.ColorXYZ """
    pass

def device_write_command(device, cmd, buffer_in, buffer_in_len, buffer_out, buffer_out_len, cancellable=None): # real signature unknown; restored from __doc__
    """ device_write_command(device:GUsb.Device, cmd:int, buffer_in:int, buffer_in_len:int, buffer_out:int, buffer_out_len:int, cancellable:Gio.Cancellable=None) -> bool """
    return False

def device_write_command_async(device, cmd, buffer_in, buffer_in_len, buffer_out, buffer_out_len, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ device_write_command_async(device:GUsb.Device, cmd:int, buffer_in:int, buffer_in_len:int, buffer_out:int, buffer_out_len:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def device_write_command_finish(device, res): # real signature unknown; restored from __doc__
    """ device_write_command_finish(device:GUsb.Device, res:Gio.AsyncResult) -> bool """
    return False

def device_write_sram(device, addr, data, cancellable=None): # real signature unknown; restored from __doc__
    """ device_write_sram(device:GUsb.Device, addr:int, data:GLib.Bytes, cancellable:Gio.Cancellable=None) -> bool """
    return False

def measure_mode_to_string(measure_mode): # real signature unknown; restored from __doc__
    """ measure_mode_to_string(measure_mode:Colorhug.MeasureMode) -> str """
    return ""

def multiplier_to_string(multiplier): # real signature unknown; restored from __doc__
    """ multiplier_to_string(multiplier:Colorhug.FreqScale) -> str """
    return ""

def sha1_parse(value, sha1): # real signature unknown; restored from __doc__
    """ sha1_parse(value:str, sha1:Colorhug.Sha1) -> bool """
    return False

def strerror(error_enum): # real signature unknown; restored from __doc__
    """ strerror(error_enum:Colorhug.Error) -> str """
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

class ColorSelect(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BLUE = 2
    GREEN = 3
    RED = 0
    WHITE = 1
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colorhug', '__dict__': <attribute '__dict__' of 'ColorSelect' objects>, '__doc__': None, '__gtype__': <GType PyColorhugColorSelect (94847217335104)>, '__enum_values__': {0: <enum CH_COLOR_SELECT_RED of type Colorhug.ColorSelect>, 1: <enum CH_COLOR_SELECT_WHITE of type Colorhug.ColorSelect>, 2: <enum CH_COLOR_SELECT_BLUE of type Colorhug.ColorSelect>, 3: <enum CH_COLOR_SELECT_GREEN of type Colorhug.ColorSelect>}, '__info__': gi.EnumInfo(ColorSelect), 'RED': <enum CH_COLOR_SELECT_RED of type Colorhug.ColorSelect>, 'WHITE': <enum CH_COLOR_SELECT_WHITE of type Colorhug.ColorSelect>, 'BLUE': <enum CH_COLOR_SELECT_BLUE of type Colorhug.ColorSelect>, 'GREEN': <enum CH_COLOR_SELECT_GREEN of type Colorhug.ColorSelect>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }
    __gtype__ = None # (!) real value is '<GType PyColorhugColorSelect (94847217335104)>'
    __info__ = gi.EnumInfo(ColorSelect)


class DeviceMode(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BOOTLOADER = 2
    BOOTLOADER2 = 7
    BOOTLOADER_ALS = 8
    BOOTLOADER_PLUS = 4
    FIRMWARE = 3
    FIRMWARE2 = 6
    FIRMWARE_ALS = 9
    FIRMWARE_PLUS = 5
    LEGACY = 1
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colorhug', '__dict__': <attribute '__dict__' of 'DeviceMode' objects>, '__doc__': None, '__gtype__': <GType PyColorhugDeviceMode (94847217737328)>, '__enum_values__': {0: <enum CH_DEVICE_MODE_UNKNOWN of type Colorhug.DeviceMode>, 1: <enum CH_DEVICE_MODE_LEGACY of type Colorhug.DeviceMode>, 2: <enum CH_DEVICE_MODE_BOOTLOADER of type Colorhug.DeviceMode>, 3: <enum CH_DEVICE_MODE_FIRMWARE of type Colorhug.DeviceMode>, 4: <enum CH_DEVICE_MODE_BOOTLOADER_PLUS of type Colorhug.DeviceMode>, 5: <enum CH_DEVICE_MODE_FIRMWARE_PLUS of type Colorhug.DeviceMode>, 6: <enum CH_DEVICE_MODE_FIRMWARE2 of type Colorhug.DeviceMode>, 7: <enum CH_DEVICE_MODE_BOOTLOADER2 of type Colorhug.DeviceMode>, 8: <enum CH_DEVICE_MODE_BOOTLOADER_ALS of type Colorhug.DeviceMode>, 9: <enum CH_DEVICE_MODE_FIRMWARE_ALS of type Colorhug.DeviceMode>}, '__info__': gi.EnumInfo(DeviceMode), 'UNKNOWN': <enum CH_DEVICE_MODE_UNKNOWN of type Colorhug.DeviceMode>, 'LEGACY': <enum CH_DEVICE_MODE_LEGACY of type Colorhug.DeviceMode>, 'BOOTLOADER': <enum CH_DEVICE_MODE_BOOTLOADER of type Colorhug.DeviceMode>, 'FIRMWARE': <enum CH_DEVICE_MODE_FIRMWARE of type Colorhug.DeviceMode>, 'BOOTLOADER_PLUS': <enum CH_DEVICE_MODE_BOOTLOADER_PLUS of type Colorhug.DeviceMode>, 'FIRMWARE_PLUS': <enum CH_DEVICE_MODE_FIRMWARE_PLUS of type Colorhug.DeviceMode>, 'FIRMWARE2': <enum CH_DEVICE_MODE_FIRMWARE2 of type Colorhug.DeviceMode>, 'BOOTLOADER2': <enum CH_DEVICE_MODE_BOOTLOADER2 of type Colorhug.DeviceMode>, 'BOOTLOADER_ALS': <enum CH_DEVICE_MODE_BOOTLOADER_ALS of type Colorhug.DeviceMode>, 'FIRMWARE_ALS': <enum CH_DEVICE_MODE_FIRMWARE_ALS of type Colorhug.DeviceMode>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
    }
    __gtype__ = None # (!) real value is '<GType PyColorhugDeviceMode (94847217737328)>'
    __info__ = gi.EnumInfo(DeviceMode)


class DeviceQueue(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        DeviceQueue(**properties)
        new() -> Colorhug.DeviceQueue
    """
    def add(self, device, cmd, buffer_in, buffer_in_len, buffer_out, buffer_out_len): # real signature unknown; restored from __doc__
        """ add(self, device:GUsb.Device, cmd:int, buffer_in:int, buffer_in_len:int, buffer_out:int, buffer_out_len:int) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def boot_flash(self, device): # real signature unknown; restored from __doc__
        """ boot_flash(self, device:GUsb.Device) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_calibration(self, device, calibration_index): # real signature unknown; restored from __doc__
        """ clear_calibration(self, device:GUsb.Device, calibration_index:int) """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_device_failed(self, *args, **kwargs): # real signature unknown
        """ device_failed(self, device:GUsb.Device, error_message:str) """
        pass

    def do_progress_changed(self, *args, **kwargs): # real signature unknown
        """ progress_changed(self, percentage:int) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def erase_flash(self, device, address, len): # real signature unknown; restored from __doc__
        """ erase_flash(self, device:GUsb.Device, address:int, len:int) """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_adc_vref_neg(self, device, vref): # real signature unknown; restored from __doc__
        """ get_adc_vref_neg(self, device:GUsb.Device, vref:float) """
        pass

    def get_adc_vref_pos(self, device, vref): # real signature unknown; restored from __doc__
        """ get_adc_vref_pos(self, device:GUsb.Device, vref:float) """
        pass

    def get_calibration(self, device, calibration_index, calibration, types, description): # real signature unknown; restored from __doc__
        """ get_calibration(self, device:GUsb.Device, calibration_index:int, calibration:Colord.Mat3x3, types:int, description:str) """
        pass

    def get_calibration_map(self, device, calibration_map): # real signature unknown; restored from __doc__
        """ get_calibration_map(self, device:GUsb.Device, calibration_map:int) """
        pass

    def get_ccd_calibration(self, device, indexes): # real signature unknown; restored from __doc__
        """ get_ccd_calibration(self, device:GUsb.Device, indexes:int) """
        pass

    def get_color_select(self, device, color_select): # real signature unknown; restored from __doc__
        """ get_color_select(self, device:GUsb.Device, color_select:Colorhug.ColorSelect) """
        pass

    def get_dac_value(self, device, dac_value): # real signature unknown; restored from __doc__
        """ get_dac_value(self, device:GUsb.Device, dac_value:float) """
        pass

    def get_dark_offsets(self, device, value): # real signature unknown; restored from __doc__
        """ get_dark_offsets(self, device:GUsb.Device, value:Colord.ColorRGB) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_firmware_ver(self, device, major, minor, micro): # real signature unknown; restored from __doc__
        """ get_firmware_ver(self, device:GUsb.Device, major:int, minor:int, micro:int) """
        pass

    def get_hardware_version(self, device, hw_version): # real signature unknown; restored from __doc__
        """ get_hardware_version(self, device:GUsb.Device, hw_version:int) """
        pass

    def get_integral_time(self, device, integral_time): # real signature unknown; restored from __doc__
        """ get_integral_time(self, device:GUsb.Device, integral_time:int) """
        pass

    def get_leds(self, device, leds): # real signature unknown; restored from __doc__
        """ get_leds(self, device:GUsb.Device, leds:int) """
        pass

    def get_measure_mode(self, device, measure_mode): # real signature unknown; restored from __doc__
        """ get_measure_mode(self, device:GUsb.Device, measure_mode:Colorhug.MeasureMode) """
        pass

    def get_multiplier(self, device, multiplier): # real signature unknown; restored from __doc__
        """ get_multiplier(self, device:GUsb.Device, multiplier:Colorhug.FreqScale) """
        pass

    def get_owner_email(self, device, email): # real signature unknown; restored from __doc__
        """ get_owner_email(self, device:GUsb.Device, email:str) """
        pass

    def get_owner_name(self, device, name): # real signature unknown; restored from __doc__
        """ get_owner_name(self, device:GUsb.Device, name:str) """
        pass

    def get_pcb_errata(self, device, pcb_errata): # real signature unknown; restored from __doc__
        """ get_pcb_errata(self, device:GUsb.Device, pcb_errata:int) """
        pass

    def get_post_scale(self, device, post_scale): # real signature unknown; restored from __doc__
        """ get_post_scale(self, device:GUsb.Device, post_scale:float) """
        pass

    def get_pre_scale(self, device, pre_scale): # real signature unknown; restored from __doc__
        """ get_pre_scale(self, device:GUsb.Device, pre_scale:float) """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_remote_hash(self, device, remote_hash): # real signature unknown; restored from __doc__
        """ get_remote_hash(self, device:GUsb.Device, remote_hash:Colorhug.Sha1) """
        pass

    def get_serial_number(self, device, serial_number): # real signature unknown; restored from __doc__
        """ get_serial_number(self, device:GUsb.Device, serial_number:int) """
        pass

    def get_temperature(self, device, temperature): # real signature unknown; restored from __doc__
        """ get_temperature(self, device:GUsb.Device, temperature:float) """
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Colorhug.DeviceQueue """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def process(self, process_flags, cancellable=None): # real signature unknown; restored from __doc__
        """ process(self, process_flags:Colorhug.DeviceQueueProcessFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def process_async(self, process_flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ process_async(self, process_flags:Colorhug.DeviceQueueProcessFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def process_finish(self, res): # real signature unknown; restored from __doc__
        """ process_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def read_firmware(self, device, data, len): # real signature unknown; restored from __doc__
        """ read_firmware(self, device:GUsb.Device, data:int, len:int) """
        pass

    def read_flash(self, device, address, data, len): # real signature unknown; restored from __doc__
        """ read_flash(self, device:GUsb.Device, address:int, data:int, len:int) """
        pass

    def read_sram(self, device, address, data, len): # real signature unknown; restored from __doc__
        """ read_sram(self, device:GUsb.Device, address:int, data:int, len:int) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset(self, device): # real signature unknown; restored from __doc__
        """ reset(self, device:GUsb.Device) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def self_test(self, device): # real signature unknown; restored from __doc__
        """ self_test(self, device:GUsb.Device) """
        pass

    def set_calibration(self, device, calibration_index, calibration, types, description): # real signature unknown; restored from __doc__
        """ set_calibration(self, device:GUsb.Device, calibration_index:int, calibration:Colord.Mat3x3, types:int, description:str) """
        pass

    def set_calibration_ccmx(self, device, calibration_index, ccmx): # real signature unknown; restored from __doc__
        """ set_calibration_ccmx(self, device:GUsb.Device, calibration_index:int, ccmx:Colord.It8) -> bool """
        return False

    def set_calibration_map(self, device, calibration_map): # real signature unknown; restored from __doc__
        """ set_calibration_map(self, device:GUsb.Device, calibration_map:int) """
        pass

    def set_ccd_calibration(self, device, indexes): # real signature unknown; restored from __doc__
        """ set_ccd_calibration(self, device:GUsb.Device, indexes:int) """
        pass

    def set_color_select(self, device, color_select): # real signature unknown; restored from __doc__
        """ set_color_select(self, device:GUsb.Device, color_select:Colorhug.ColorSelect) """
        pass

    def set_dac_value(self, device, dac_value): # real signature unknown; restored from __doc__
        """ set_dac_value(self, device:GUsb.Device, dac_value:float) """
        pass

    def set_dark_offsets(self, device, value): # real signature unknown; restored from __doc__
        """ set_dark_offsets(self, device:GUsb.Device, value:Colord.ColorRGB) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_flash_success(self, device, value): # real signature unknown; restored from __doc__
        """ set_flash_success(self, device:GUsb.Device, value:int) """
        pass

    def set_integral_time(self, device, integral_time): # real signature unknown; restored from __doc__
        """ set_integral_time(self, device:GUsb.Device, integral_time:int) """
        pass

    def set_leds(self, device, leds, repeat, on_time, off_time): # real signature unknown; restored from __doc__
        """ set_leds(self, device:GUsb.Device, leds:int, repeat:int, on_time:int, off_time:int) """
        pass

    def set_measure_mode(self, device, measure_mode): # real signature unknown; restored from __doc__
        """ set_measure_mode(self, device:GUsb.Device, measure_mode:Colorhug.MeasureMode) """
        pass

    def set_multiplier(self, device, multiplier): # real signature unknown; restored from __doc__
        """ set_multiplier(self, device:GUsb.Device, multiplier:Colorhug.FreqScale) """
        pass

    def set_owner_email(self, device, email): # real signature unknown; restored from __doc__
        """ set_owner_email(self, device:GUsb.Device, email:str) """
        pass

    def set_owner_name(self, device, name): # real signature unknown; restored from __doc__
        """ set_owner_name(self, device:GUsb.Device, name:str) """
        pass

    def set_pcb_errata(self, device, pcb_errata): # real signature unknown; restored from __doc__
        """ set_pcb_errata(self, device:GUsb.Device, pcb_errata:int) """
        pass

    def set_post_scale(self, device, post_scale): # real signature unknown; restored from __doc__
        """ set_post_scale(self, device:GUsb.Device, post_scale:float) """
        pass

    def set_pre_scale(self, device, pre_scale): # real signature unknown; restored from __doc__
        """ set_pre_scale(self, device:GUsb.Device, pre_scale:float) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_remote_hash(self, device, remote_hash): # real signature unknown; restored from __doc__
        """ set_remote_hash(self, device:GUsb.Device, remote_hash:Colorhug.Sha1) """
        pass

    def set_serial_number(self, device, serial_number): # real signature unknown; restored from __doc__
        """ set_serial_number(self, device:GUsb.Device, serial_number:int) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def take_readings(self, device, value): # real signature unknown; restored from __doc__
        """ take_readings(self, device:GUsb.Device, value:Colord.ColorRGB) """
        pass

    def take_readings_xyz(self, device, calibration_index, value): # real signature unknown; restored from __doc__
        """ take_readings_xyz(self, device:GUsb.Device, calibration_index:int, value:Colord.ColorXYZ) """
        pass

    def take_reading_array(self, device, reading_array): # real signature unknown; restored from __doc__
        """ take_reading_array(self, device:GUsb.Device, reading_array:int) """
        pass

    def take_reading_raw(self, device, take_reading): # real signature unknown; restored from __doc__
        """ take_reading_raw(self, device:GUsb.Device, take_reading:int) """
        pass

    def take_reading_spectral(self, device, sram_addr): # real signature unknown; restored from __doc__
        """ take_reading_spectral(self, device:GUsb.Device, sram_addr:int) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def verify_firmware(self, device, data, len): # real signature unknown; restored from __doc__
        """ verify_firmware(self, device:GUsb.Device, data:int, len:int) """
        pass

    def verify_flash(self, device, address, data, len): # real signature unknown; restored from __doc__
        """ verify_flash(self, device:GUsb.Device, address:int, data:int, len:int) """
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write_eeprom(self, device, magic): # real signature unknown; restored from __doc__
        """ write_eeprom(self, device:GUsb.Device, magic:str) """
        pass

    def write_firmware(self, device, data, len): # real signature unknown; restored from __doc__
        """ write_firmware(self, device:GUsb.Device, data:int, len:int) """
        pass

    def write_flash(self, device, address, data, len): # real signature unknown; restored from __doc__
        """ write_flash(self, device:GUsb.Device, address:int, data:int, len:int) """
        pass

    def write_sram(self, device, address, data, len): # real signature unknown; restored from __doc__
        """ write_sram(self, device:GUsb.Device, address:int, data:int, len:int) """
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7feaead08bb0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DeviceQueue), '__module__': 'gi.repository.Colorhug', '__gtype__': <GType ChDeviceQueue (94847217362720)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add': gi.FunctionInfo(add), 'boot_flash': gi.FunctionInfo(boot_flash), 'clear_calibration': gi.FunctionInfo(clear_calibration), 'erase_flash': gi.FunctionInfo(erase_flash), 'get_adc_vref_neg': gi.FunctionInfo(get_adc_vref_neg), 'get_adc_vref_pos': gi.FunctionInfo(get_adc_vref_pos), 'get_calibration': gi.FunctionInfo(get_calibration), 'get_calibration_map': gi.FunctionInfo(get_calibration_map), 'get_ccd_calibration': gi.FunctionInfo(get_ccd_calibration), 'get_color_select': gi.FunctionInfo(get_color_select), 'get_dac_value': gi.FunctionInfo(get_dac_value), 'get_dark_offsets': gi.FunctionInfo(get_dark_offsets), 'get_firmware_ver': gi.FunctionInfo(get_firmware_ver), 'get_hardware_version': gi.FunctionInfo(get_hardware_version), 'get_integral_time': gi.FunctionInfo(get_integral_time), 'get_leds': gi.FunctionInfo(get_leds), 'get_measure_mode': gi.FunctionInfo(get_measure_mode), 'get_multiplier': gi.FunctionInfo(get_multiplier), 'get_owner_email': gi.FunctionInfo(get_owner_email), 'get_owner_name': gi.FunctionInfo(get_owner_name), 'get_pcb_errata': gi.FunctionInfo(get_pcb_errata), 'get_post_scale': gi.FunctionInfo(get_post_scale), 'get_pre_scale': gi.FunctionInfo(get_pre_scale), 'get_remote_hash': gi.FunctionInfo(get_remote_hash), 'get_serial_number': gi.FunctionInfo(get_serial_number), 'get_temperature': gi.FunctionInfo(get_temperature), 'process': gi.FunctionInfo(process), 'process_async': gi.FunctionInfo(process_async), 'process_finish': gi.FunctionInfo(process_finish), 'read_firmware': gi.FunctionInfo(read_firmware), 'read_flash': gi.FunctionInfo(read_flash), 'read_sram': gi.FunctionInfo(read_sram), 'reset': gi.FunctionInfo(reset), 'self_test': gi.FunctionInfo(self_test), 'set_calibration': gi.FunctionInfo(set_calibration), 'set_calibration_ccmx': gi.FunctionInfo(set_calibration_ccmx), 'set_calibration_map': gi.FunctionInfo(set_calibration_map), 'set_ccd_calibration': gi.FunctionInfo(set_ccd_calibration), 'set_color_select': gi.FunctionInfo(set_color_select), 'set_dac_value': gi.FunctionInfo(set_dac_value), 'set_dark_offsets': gi.FunctionInfo(set_dark_offsets), 'set_flash_success': gi.FunctionInfo(set_flash_success), 'set_integral_time': gi.FunctionInfo(set_integral_time), 'set_leds': gi.FunctionInfo(set_leds), 'set_measure_mode': gi.FunctionInfo(set_measure_mode), 'set_multiplier': gi.FunctionInfo(set_multiplier), 'set_owner_email': gi.FunctionInfo(set_owner_email), 'set_owner_name': gi.FunctionInfo(set_owner_name), 'set_pcb_errata': gi.FunctionInfo(set_pcb_errata), 'set_post_scale': gi.FunctionInfo(set_post_scale), 'set_pre_scale': gi.FunctionInfo(set_pre_scale), 'set_remote_hash': gi.FunctionInfo(set_remote_hash), 'set_serial_number': gi.FunctionInfo(set_serial_number), 'take_reading_array': gi.FunctionInfo(take_reading_array), 'take_reading_raw': gi.FunctionInfo(take_reading_raw), 'take_reading_spectral': gi.FunctionInfo(take_reading_spectral), 'take_readings': gi.FunctionInfo(take_readings), 'take_readings_xyz': gi.FunctionInfo(take_readings_xyz), 'verify_firmware': gi.FunctionInfo(verify_firmware), 'verify_flash': gi.FunctionInfo(verify_flash), 'write_eeprom': gi.FunctionInfo(write_eeprom), 'write_firmware': gi.FunctionInfo(write_firmware), 'write_flash': gi.FunctionInfo(write_flash), 'write_sram': gi.FunctionInfo(write_sram), 'do_device_failed': gi.VFuncInfo(device_failed), 'do_progress_changed': gi.VFuncInfo(progress_changed), 'parent_instance': <property object at 0x7feaead034f0>})"
    __gdoc__ = 'Object ChDeviceQueue\n\nSignals from ChDeviceQueue:\n  device-failed (GObject, gchararray)\n  progress-changed (guint)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ChDeviceQueue (94847217362720)>'
    __info__ = ObjectInfo(DeviceQueue)


class DeviceQueueClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DeviceQueueClass()
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

    device_failed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    progress_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ch_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ch_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ch_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ch_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ch_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DeviceQueueClass), '__module__': 'gi.repository.Colorhug', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DeviceQueueClass' objects>, '__weakref__': <attribute '__weakref__' of 'DeviceQueueClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7feaead03630>, 'device_failed': <property object at 0x7feaead03680>, 'progress_changed': <property object at 0x7feaead03720>, '_ch_reserved1': <property object at 0x7feaead03810>, '_ch_reserved2': <property object at 0x7feaead03900>, '_ch_reserved3': <property object at 0x7feaead039f0>, '_ch_reserved4': <property object at 0x7feaead03ae0>, '_ch_reserved5': <property object at 0x7feaead03bd0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DeviceQueueClass)


class DeviceQueueProcessFlags(__gobject.GFlags):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CONTINUE_ERRORS = 1
    NONE = 0
    NONFATAL_ERRORS = 2
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colorhug', '__dict__': <attribute '__dict__' of 'DeviceQueueProcessFlags' objects>, '__doc__': None, '__gtype__': <GType PyColorhugDeviceQueueProcessFlags (94847217445072)>, '__flags_values__': {0: <flags 0 of type Colorhug.DeviceQueueProcessFlags>, 1: <flags CH_DEVICE_QUEUE_PROCESS_FLAGS_CONTINUE_ERRORS of type Colorhug.DeviceQueueProcessFlags>, 2: <flags CH_DEVICE_QUEUE_PROCESS_FLAGS_NONFATAL_ERRORS of type Colorhug.DeviceQueueProcessFlags>}, '__info__': gi.EnumInfo(DeviceQueueProcessFlags), 'NONE': <flags 0 of type Colorhug.DeviceQueueProcessFlags>, 'CONTINUE_ERRORS': <flags CH_DEVICE_QUEUE_PROCESS_FLAGS_CONTINUE_ERRORS of type Colorhug.DeviceQueueProcessFlags>, 'NONFATAL_ERRORS': <flags CH_DEVICE_QUEUE_PROCESS_FLAGS_NONFATAL_ERRORS of type Colorhug.DeviceQueueProcessFlags>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is '<GType PyColorhugDeviceQueueProcessFlags (94847217445072)>'
    __info__ = gi.EnumInfo(DeviceQueueProcessFlags)


class Error(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DEVICE_DEACTIVATED = 17
    I2C_SLAVE_ADDRESS = 33
    I2C_SLAVE_CONFIG = 34
    INCOMPLETE_REQUEST = 18
    INVALID_ADDRESS = 7
    INVALID_CALIBRATION = 25
    INVALID_CHECKSUM = 9
    INVALID_LENGTH = 8
    INVALID_VALUE = 10
    NONE = 0
    NOT_IMPLEMENTED = 3
    NO_CALIBRATION = 12
    NO_SERIAL = 5
    OUT_OF_MEMORY = 27
    OVERFLOW_ADDITION = 14
    OVERFLOW_MULTIPLY = 13
    OVERFLOW_SENSOR = 15
    OVERFLOW_STACK = 16
    SELF_TEST_ADC_VDD = 30
    SELF_TEST_ADC_VREF = 32
    SELF_TEST_ADC_VSS = 31
    SELF_TEST_BLUE = 22
    SELF_TEST_COLOR_SELECT = 23
    SELF_TEST_EEPROM = 35
    SELF_TEST_GREEN = 21
    SELF_TEST_I2C = 29
    SELF_TEST_MULTIPLIER = 24
    SELF_TEST_RED = 20
    SELF_TEST_SENSOR = 19
    SELF_TEST_TEMPERATURE = 28
    SRAM_FAILED = 26
    UNDERFLOW_SENSOR = 4
    UNKNOWN_CMD = 1
    UNKNOWN_CMD_FOR_BOOTLOADER = 11
    WATCHDOG = 6
    WRONG_UNLOCK_CODE = 2
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colorhug', '__dict__': <attribute '__dict__' of 'Error' objects>, '__doc__': None, '__gtype__': <GType PyColorhugError (94847217620272)>, '__enum_values__': {0: <enum CH_ERROR_NONE of type Colorhug.Error>, 1: <enum CH_ERROR_UNKNOWN_CMD of type Colorhug.Error>, 2: <enum CH_ERROR_WRONG_UNLOCK_CODE of type Colorhug.Error>, 3: <enum CH_ERROR_NOT_IMPLEMENTED of type Colorhug.Error>, 4: <enum CH_ERROR_UNDERFLOW_SENSOR of type Colorhug.Error>, 5: <enum CH_ERROR_NO_SERIAL of type Colorhug.Error>, 6: <enum CH_ERROR_WATCHDOG of type Colorhug.Error>, 7: <enum CH_ERROR_INVALID_ADDRESS of type Colorhug.Error>, 8: <enum CH_ERROR_INVALID_LENGTH of type Colorhug.Error>, 9: <enum CH_ERROR_INVALID_CHECKSUM of type Colorhug.Error>, 10: <enum CH_ERROR_INVALID_VALUE of type Colorhug.Error>, 11: <enum CH_ERROR_UNKNOWN_CMD_FOR_BOOTLOADER of type Colorhug.Error>, 12: <enum CH_ERROR_NO_CALIBRATION of type Colorhug.Error>, 13: <enum CH_ERROR_OVERFLOW_MULTIPLY of type Colorhug.Error>, 14: <enum CH_ERROR_OVERFLOW_ADDITION of type Colorhug.Error>, 15: <enum CH_ERROR_OVERFLOW_SENSOR of type Colorhug.Error>, 16: <enum CH_ERROR_OVERFLOW_STACK of type Colorhug.Error>, 17: <enum CH_ERROR_DEVICE_DEACTIVATED of type Colorhug.Error>, 18: <enum CH_ERROR_INCOMPLETE_REQUEST of type Colorhug.Error>, 19: <enum CH_ERROR_SELF_TEST_SENSOR of type Colorhug.Error>, 20: <enum CH_ERROR_SELF_TEST_RED of type Colorhug.Error>, 21: <enum CH_ERROR_SELF_TEST_GREEN of type Colorhug.Error>, 22: <enum CH_ERROR_SELF_TEST_BLUE of type Colorhug.Error>, 23: <enum CH_ERROR_SELF_TEST_COLOR_SELECT of type Colorhug.Error>, 24: <enum CH_ERROR_SELF_TEST_MULTIPLIER of type Colorhug.Error>, 25: <enum CH_ERROR_INVALID_CALIBRATION of type Colorhug.Error>, 26: <enum CH_ERROR_SRAM_FAILED of type Colorhug.Error>, 27: <enum CH_ERROR_OUT_OF_MEMORY of type Colorhug.Error>, 28: <enum CH_ERROR_SELF_TEST_TEMPERATURE of type Colorhug.Error>, 29: <enum CH_ERROR_SELF_TEST_I2C of type Colorhug.Error>, 30: <enum CH_ERROR_SELF_TEST_ADC_VDD of type Colorhug.Error>, 31: <enum CH_ERROR_SELF_TEST_ADC_VSS of type Colorhug.Error>, 32: <enum CH_ERROR_SELF_TEST_ADC_VREF of type Colorhug.Error>, 33: <enum CH_ERROR_I2C_SLAVE_ADDRESS of type Colorhug.Error>, 34: <enum CH_ERROR_I2C_SLAVE_CONFIG of type Colorhug.Error>, 35: <enum CH_ERROR_SELF_TEST_EEPROM of type Colorhug.Error>}, '__info__': gi.EnumInfo(Error), 'NONE': <enum CH_ERROR_NONE of type Colorhug.Error>, 'UNKNOWN_CMD': <enum CH_ERROR_UNKNOWN_CMD of type Colorhug.Error>, 'WRONG_UNLOCK_CODE': <enum CH_ERROR_WRONG_UNLOCK_CODE of type Colorhug.Error>, 'NOT_IMPLEMENTED': <enum CH_ERROR_NOT_IMPLEMENTED of type Colorhug.Error>, 'UNDERFLOW_SENSOR': <enum CH_ERROR_UNDERFLOW_SENSOR of type Colorhug.Error>, 'NO_SERIAL': <enum CH_ERROR_NO_SERIAL of type Colorhug.Error>, 'WATCHDOG': <enum CH_ERROR_WATCHDOG of type Colorhug.Error>, 'INVALID_ADDRESS': <enum CH_ERROR_INVALID_ADDRESS of type Colorhug.Error>, 'INVALID_LENGTH': <enum CH_ERROR_INVALID_LENGTH of type Colorhug.Error>, 'INVALID_CHECKSUM': <enum CH_ERROR_INVALID_CHECKSUM of type Colorhug.Error>, 'INVALID_VALUE': <enum CH_ERROR_INVALID_VALUE of type Colorhug.Error>, 'UNKNOWN_CMD_FOR_BOOTLOADER': <enum CH_ERROR_UNKNOWN_CMD_FOR_BOOTLOADER of type Colorhug.Error>, 'NO_CALIBRATION': <enum CH_ERROR_NO_CALIBRATION of type Colorhug.Error>, 'OVERFLOW_MULTIPLY': <enum CH_ERROR_OVERFLOW_MULTIPLY of type Colorhug.Error>, 'OVERFLOW_ADDITION': <enum CH_ERROR_OVERFLOW_ADDITION of type Colorhug.Error>, 'OVERFLOW_SENSOR': <enum CH_ERROR_OVERFLOW_SENSOR of type Colorhug.Error>, 'OVERFLOW_STACK': <enum CH_ERROR_OVERFLOW_STACK of type Colorhug.Error>, 'DEVICE_DEACTIVATED': <enum CH_ERROR_DEVICE_DEACTIVATED of type Colorhug.Error>, 'INCOMPLETE_REQUEST': <enum CH_ERROR_INCOMPLETE_REQUEST of type Colorhug.Error>, 'SELF_TEST_SENSOR': <enum CH_ERROR_SELF_TEST_SENSOR of type Colorhug.Error>, 'SELF_TEST_RED': <enum CH_ERROR_SELF_TEST_RED of type Colorhug.Error>, 'SELF_TEST_GREEN': <enum CH_ERROR_SELF_TEST_GREEN of type Colorhug.Error>, 'SELF_TEST_BLUE': <enum CH_ERROR_SELF_TEST_BLUE of type Colorhug.Error>, 'SELF_TEST_COLOR_SELECT': <enum CH_ERROR_SELF_TEST_COLOR_SELECT of type Colorhug.Error>, 'SELF_TEST_MULTIPLIER': <enum CH_ERROR_SELF_TEST_MULTIPLIER of type Colorhug.Error>, 'INVALID_CALIBRATION': <enum CH_ERROR_INVALID_CALIBRATION of type Colorhug.Error>, 'SRAM_FAILED': <enum CH_ERROR_SRAM_FAILED of type Colorhug.Error>, 'OUT_OF_MEMORY': <enum CH_ERROR_OUT_OF_MEMORY of type Colorhug.Error>, 'SELF_TEST_TEMPERATURE': <enum CH_ERROR_SELF_TEST_TEMPERATURE of type Colorhug.Error>, 'SELF_TEST_I2C': <enum CH_ERROR_SELF_TEST_I2C of type Colorhug.Error>, 'SELF_TEST_ADC_VDD': <enum CH_ERROR_SELF_TEST_ADC_VDD of type Colorhug.Error>, 'SELF_TEST_ADC_VSS': <enum CH_ERROR_SELF_TEST_ADC_VSS of type Colorhug.Error>, 'SELF_TEST_ADC_VREF': <enum CH_ERROR_SELF_TEST_ADC_VREF of type Colorhug.Error>, 'I2C_SLAVE_ADDRESS': <enum CH_ERROR_I2C_SLAVE_ADDRESS of type Colorhug.Error>, 'I2C_SLAVE_CONFIG': <enum CH_ERROR_I2C_SLAVE_CONFIG of type Colorhug.Error>, 'SELF_TEST_EEPROM': <enum CH_ERROR_SELF_TEST_EEPROM of type Colorhug.Error>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
    }
    __gtype__ = None # (!) real value is '<GType PyColorhugError (94847217620272)>'
    __info__ = gi.EnumInfo(Error)


class FreqScale(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    0 = 0
    100 = 3
    2 = 2
    20 = 1
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colorhug', '__dict__': <attribute '__dict__' of 'FreqScale' objects>, '__doc__': None, '__gtype__': <GType PyColorhugFreqScale (94847217629680)>, '__enum_values__': {0: <enum CH_FREQ_SCALE_0 of type Colorhug.FreqScale>, 1: <enum CH_FREQ_SCALE_20 of type Colorhug.FreqScale>, 2: <enum CH_FREQ_SCALE_2 of type Colorhug.FreqScale>, 3: <enum CH_FREQ_SCALE_100 of type Colorhug.FreqScale>}, '__info__': gi.EnumInfo(FreqScale), '0': <enum CH_FREQ_SCALE_0 of type Colorhug.FreqScale>, '20': <enum CH_FREQ_SCALE_20 of type Colorhug.FreqScale>, '2': <enum CH_FREQ_SCALE_2 of type Colorhug.FreqScale>, '100': <enum CH_FREQ_SCALE_100 of type Colorhug.FreqScale>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }
    __gtype__ = None # (!) real value is '<GType PyColorhugFreqScale (94847217629680)>'
    __info__ = gi.EnumInfo(FreqScale)


class Illuminant(__gobject.GFlags):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    A = 1
    NONE = 0
    UV = 2
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colorhug', '__dict__': <attribute '__dict__' of 'Illuminant' objects>, '__doc__': None, '__gtype__': <GType PyColorhugIlluminant (94847217645888)>, '__flags_values__': {0: <flags 0 of type Colorhug.Illuminant>, 1: <flags CH_ILLUMINANT_A of type Colorhug.Illuminant>, 2: <flags CH_ILLUMINANT_UV of type Colorhug.Illuminant>}, '__info__': gi.EnumInfo(Illuminant), 'NONE': <flags 0 of type Colorhug.Illuminant>, 'A': <flags CH_ILLUMINANT_A of type Colorhug.Illuminant>, 'UV': <flags CH_ILLUMINANT_UV of type Colorhug.Illuminant>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is '<GType PyColorhugIlluminant (94847217645888)>'
    __info__ = gi.EnumInfo(Illuminant)


class MeasureMode(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DURATION = 1
    FREQUENCY = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colorhug', '__dict__': <attribute '__dict__' of 'MeasureMode' objects>, '__doc__': None, '__gtype__': <GType PyColorhugMeasureMode (94847217654032)>, '__enum_values__': {0: <enum CH_MEASURE_MODE_FREQUENCY of type Colorhug.MeasureMode>, 1: <enum CH_MEASURE_MODE_DURATION of type Colorhug.MeasureMode>}, '__info__': gi.EnumInfo(MeasureMode), 'FREQUENCY': <enum CH_MEASURE_MODE_FREQUENCY of type Colorhug.MeasureMode>, 'DURATION': <enum CH_MEASURE_MODE_DURATION of type Colorhug.MeasureMode>})"
    __enum_values__ = {
        0: 0,
        1: 1,
    }
    __gtype__ = None # (!) real value is '<GType PyColorhugMeasureMode (94847217654032)>'
    __info__ = gi.EnumInfo(MeasureMode)


class PcbErrata(__gobject.GFlags):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    NONE = 0
    NO_WELCOME = 2
    SWAPPED_LEDS = 1
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colorhug', '__dict__': <attribute '__dict__' of 'PcbErrata' objects>, '__doc__': None, '__gtype__': <GType PyColorhugPcbErrata (94847217642752)>, '__flags_values__': {0: <flags 0 of type Colorhug.PcbErrata>, 1: <flags CH_PCB_ERRATA_SWAPPED_LEDS of type Colorhug.PcbErrata>, 2: <flags CH_PCB_ERRATA_NO_WELCOME of type Colorhug.PcbErrata>}, '__info__': gi.EnumInfo(PcbErrata), 'NONE': <flags 0 of type Colorhug.PcbErrata>, 'SWAPPED_LEDS': <flags CH_PCB_ERRATA_SWAPPED_LEDS of type Colorhug.PcbErrata>, 'NO_WELCOME': <flags CH_PCB_ERRATA_NO_WELCOME of type Colorhug.PcbErrata>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is '<GType PyColorhugPcbErrata (94847217642752)>'
    __info__ = gi.EnumInfo(PcbErrata)


class Sha1(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Sha1()
    """
    def parse(self, value, sha1): # real signature unknown; restored from __doc__
        """ parse(value:str, sha1:Colorhug.Sha1) -> bool """
        return False

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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

    bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Sha1), '__module__': 'gi.repository.Colorhug', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Sha1' objects>, '__weakref__': <attribute '__weakref__' of 'Sha1' objects>, '__doc__': None, 'bytes': <property object at 0x7feaead0cae0>, 'to_string': gi.FunctionInfo(to_string), 'parse': gi.FunctionInfo(parse)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Sha1)


class SpectrumKind(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DARK_CAL = 1
    IRRADIANCE_CAL = 3
    LAST = 4
    RAW = 0
    TEMP_CAL = 2
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colorhug', '__dict__': <attribute '__dict__' of 'SpectrumKind' objects>, '__doc__': None, '__gtype__': <GType PyColorhugSpectrumKind (94847217338816)>, '__enum_values__': {0: <enum CH_SPECTRUM_KIND_RAW of type Colorhug.SpectrumKind>, 1: <enum CH_SPECTRUM_KIND_DARK_CAL of type Colorhug.SpectrumKind>, 2: <enum CH_SPECTRUM_KIND_TEMP_CAL of type Colorhug.SpectrumKind>, 3: <enum CH_SPECTRUM_KIND_IRRADIANCE_CAL of type Colorhug.SpectrumKind>, 4: <enum CH_SPECTRUM_KIND_LAST of type Colorhug.SpectrumKind>}, '__info__': gi.EnumInfo(SpectrumKind), 'RAW': <enum CH_SPECTRUM_KIND_RAW of type Colorhug.SpectrumKind>, 'DARK_CAL': <enum CH_SPECTRUM_KIND_DARK_CAL of type Colorhug.SpectrumKind>, 'TEMP_CAL': <enum CH_SPECTRUM_KIND_TEMP_CAL of type Colorhug.SpectrumKind>, 'IRRADIANCE_CAL': <enum CH_SPECTRUM_KIND_IRRADIANCE_CAL of type Colorhug.SpectrumKind>, 'LAST': <enum CH_SPECTRUM_KIND_LAST of type Colorhug.SpectrumKind>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    __gtype__ = None # (!) real value is '<GType PyColorhugSpectrumKind (94847217338816)>'
    __info__ = gi.EnumInfo(SpectrumKind)


class StatusLed(__gobject.GFlags):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BLUE = 4
    GREEN = 1
    RED = 2
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colorhug', '__dict__': <attribute '__dict__' of 'StatusLed' objects>, '__doc__': None, '__gtype__': <GType PyColorhugStatusLed (94847217774736)>, '__flags_values__': {1: <flags CH_STATUS_LED_GREEN of type Colorhug.StatusLed>, 2: <flags CH_STATUS_LED_RED of type Colorhug.StatusLed>, 4: <flags CH_STATUS_LED_BLUE of type Colorhug.StatusLed>}, '__info__': gi.EnumInfo(StatusLed), 'GREEN': <flags CH_STATUS_LED_GREEN of type Colorhug.StatusLed>, 'RED': <flags CH_STATUS_LED_RED of type Colorhug.StatusLed>, 'BLUE': <flags CH_STATUS_LED_BLUE of type Colorhug.StatusLed>})"
    __flags_values__ = {
        1: 1,
        2: 2,
        4: 4,
    }
    __gtype__ = None # (!) real value is '<GType PyColorhugStatusLed (94847217774736)>'
    __info__ = gi.EnumInfo(StatusLed)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7feaeaf531f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7feaeaf53280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7feaeaf53310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7feaeaf533a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7feaebb8fd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Colorhug-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Colorhug', loader=<gi.importer.DynamicImporter object at 0x7feaebb8fd00>)"

