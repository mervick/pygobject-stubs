# encoding: utf-8
# module gi.repository.Vips
# from /usr/lib64/girepository-1.0/Vips-8.0.typelib
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

ARGUMENT_OPTIONAL_INPUT = 18
ARGUMENT_OPTIONAL_OUTPUT = 34

ARGUMENT_REQUIRED_INPUT = 19
ARGUMENT_REQUIRED_OUTPUT = 35

A_X0 = 109.8503
A_Y0 = 100.0
A_Z0 = 35.5849

B_X0 = 99.072
B_Y0 = 100.0
B_Z0 = 85.223

C_X0 = 98.07
C_Y0 = 100.0
C_Z0 = 118.23

D3250_X0 = 105.659
D3250_Y0 = 100.0
D3250_Z0 = 45.8501

D50_X0 = 96.425
D50_Y0 = 100.0
D50_Z0 = 82.468

D55_X0 = 95.6831
D55_Y0 = 100.0
D55_Z0 = 92.0871

D65_X0 = 95.047
D65_Y0 = 100.0
D65_Z0 = 108.8827

D75_X0 = 94.9682
D75_Y0 = 100.0
D75_Z0 = 122.571

D93_X0 = 89.74
D93_Y0 = 100.0
D93_Z0 = 130.77

E_X0 = 100.0
E_Y0 = 100.0
E_Z0 = 100.0

INTERPOLATE_SCALE = 1
INTERPOLATE_SHIFT = 12

MAGIC_INTEL = -1230573048
MAGIC_SPARC = 150120118

MAX_COORD = 10000000

META_EXIF_NAME = 'exif-data'

META_ICC_NAME = 'icc-profile-data'

META_IMAGEDESCRIPTION = 'image-description'

META_IPTC_NAME = 'iptc-data'

META_LOADER = 'vips-loader'

META_N_PAGES = 'n-pages'

META_ORIENTATION = 'orientation'

META_PAGE_HEIGHT = 'page-height'

META_PHOTOSHOP_NAME = 'photoshop-data'

META_RESOLUTION_UNIT = 'resolution-unit'

META_SEQUENTIAL = 'vips-sequential'

META_XMP_NAME = 'xmp-data'

TRANSFORM_SCALE = 1
TRANSFORM_SHIFT = 6

_namespace = 'Vips'

_version = '8.0'

__weakref__ = None

# functions

def add_option_entries(option_group): # real signature unknown; restored from __doc__
    """ add_option_entries(option_group:GLib.OptionGroup) """
    pass

def autorot_get_angle(image): # real signature unknown; restored from __doc__
    """ autorot_get_angle(image:Vips.Image) -> Vips.Angle """
    pass

def band_format_is8bit(format): # real signature unknown; restored from __doc__
    """ band_format_is8bit(format:Vips.BandFormat) -> bool """
    return False

def band_format_iscomplex(format): # real signature unknown; restored from __doc__
    """ band_format_iscomplex(format:Vips.BandFormat) -> bool """
    return False

def band_format_isfloat(format): # real signature unknown; restored from __doc__
    """ band_format_isfloat(format:Vips.BandFormat) -> bool """
    return False

def band_format_isint(format): # real signature unknown; restored from __doc__
    """ band_format_isint(format:Vips.BandFormat) -> bool """
    return False

def band_format_isuint(format): # real signature unknown; restored from __doc__
    """ band_format_isuint(format:Vips.BandFormat) -> bool """
    return False

def blob_copy(data): # real signature unknown; restored from __doc__
    """ blob_copy(data:list) -> Vips.Blob """
    pass

def cache_drop_all(): # real signature unknown; restored from __doc__
    """ cache_drop_all() """
    pass

def cache_get_max(): # real signature unknown; restored from __doc__
    """ cache_get_max() -> int """
    return 0

def cache_get_max_files(): # real signature unknown; restored from __doc__
    """ cache_get_max_files() -> int """
    return 0

def cache_get_max_mem(): # real signature unknown; restored from __doc__
    """ cache_get_max_mem() -> int """
    return 0

def cache_get_size(): # real signature unknown; restored from __doc__
    """ cache_get_size() -> int """
    return 0

def cache_operation_add(operation): # real signature unknown; restored from __doc__
    """ cache_operation_add(operation:Vips.Operation) """
    pass

def cache_operation_build(operation): # real signature unknown; restored from __doc__
    """ cache_operation_build(operation:Vips.Operation) -> Vips.Operation """
    pass

def cache_operation_lookup(operation): # real signature unknown; restored from __doc__
    """ cache_operation_lookup(operation:Vips.Operation) -> Vips.Operation """
    pass

def cache_print(): # real signature unknown; restored from __doc__
    """ cache_print() """
    pass

def cache_set_dump(dump): # real signature unknown; restored from __doc__
    """ cache_set_dump(dump:bool) """
    pass

def cache_set_max(max): # real signature unknown; restored from __doc__
    """ cache_set_max(max:int) """
    pass

def cache_set_max_files(max_files): # real signature unknown; restored from __doc__
    """ cache_set_max_files(max_files:int) """
    pass

def cache_set_max_mem(max_mem): # real signature unknown; restored from __doc__
    """ cache_set_max_mem(max_mem:int) """
    pass

def cache_set_trace(trace): # real signature unknown; restored from __doc__
    """ cache_set_trace(trace:bool) """
    pass

def call_argv(operation, argc, argv): # real signature unknown; restored from __doc__
    """ call_argv(operation:Vips.Operation, argc:int, argv:str) -> int """
    return 0

def call_options(group, operation): # real signature unknown; restored from __doc__
    """ call_options(group:GLib.OptionGroup, operation:Vips.Operation) """
    pass

def check_8or16(domain, im): # real signature unknown; restored from __doc__
    """ check_8or16(domain:str, im:Vips.Image) -> int """
    return 0

def check_bandno(domain, im, bandno): # real signature unknown; restored from __doc__
    """ check_bandno(domain:str, im:Vips.Image, bandno:int) -> int """
    return 0

def check_bands(domain, im, bands): # real signature unknown; restored from __doc__
    """ check_bands(domain:str, im:Vips.Image, bands:int) -> int """
    return 0

def check_bands_1or3(domain, im): # real signature unknown; restored from __doc__
    """ check_bands_1or3(domain:str, im:Vips.Image) -> int """
    return 0

def check_bands_1orn(domain, im1, im2): # real signature unknown; restored from __doc__
    """ check_bands_1orn(domain:str, im1:Vips.Image, im2:Vips.Image) -> int """
    return 0

def check_bands_1orn_unary(domain, im, n): # real signature unknown; restored from __doc__
    """ check_bands_1orn_unary(domain:str, im:Vips.Image, n:int) -> int """
    return 0

def check_bands_atleast(domain, im, bands): # real signature unknown; restored from __doc__
    """ check_bands_atleast(domain:str, im:Vips.Image, bands:int) -> int """
    return 0

def check_bands_same(domain, im1, im2): # real signature unknown; restored from __doc__
    """ check_bands_same(domain:str, im1:Vips.Image, im2:Vips.Image) -> int """
    return 0

def check_coding(domain, im, coding): # real signature unknown; restored from __doc__
    """ check_coding(domain:str, im:Vips.Image, coding:Vips.Coding) -> int """
    return 0

def check_coding_known(domain, im): # real signature unknown; restored from __doc__
    """ check_coding_known(domain:str, im:Vips.Image) -> int """
    return 0

def check_coding_noneorlabq(domain, im): # real signature unknown; restored from __doc__
    """ check_coding_noneorlabq(domain:str, im:Vips.Image) -> int """
    return 0

def check_coding_same(domain, im1, im2): # real signature unknown; restored from __doc__
    """ check_coding_same(domain:str, im1:Vips.Image, im2:Vips.Image) -> int """
    return 0

def check_complex(domain, im): # real signature unknown; restored from __doc__
    """ check_complex(domain:str, im:Vips.Image) -> int """
    return 0

def check_format(domain, im, fmt): # real signature unknown; restored from __doc__
    """ check_format(domain:str, im:Vips.Image, fmt:Vips.BandFormat) -> int """
    return 0

def check_format_same(domain, im1, im2): # real signature unknown; restored from __doc__
    """ check_format_same(domain:str, im1:Vips.Image, im2:Vips.Image) -> int """
    return 0

def check_hist(domain, im): # real signature unknown; restored from __doc__
    """ check_hist(domain:str, im:Vips.Image) -> int """
    return 0

def check_int(domain, im): # real signature unknown; restored from __doc__
    """ check_int(domain:str, im:Vips.Image) -> int """
    return 0

def check_matrix(domain, im): # real signature unknown; restored from __doc__
    """ check_matrix(domain:str, im:Vips.Image) -> int, out:Vips.Image """
    return 0

def check_mono(domain, im): # real signature unknown; restored from __doc__
    """ check_mono(domain:str, im:Vips.Image) -> int """
    return 0

def check_noncomplex(domain, im): # real signature unknown; restored from __doc__
    """ check_noncomplex(domain:str, im:Vips.Image) -> int """
    return 0

def check_oddsquare(domain, im): # real signature unknown; restored from __doc__
    """ check_oddsquare(domain:str, im:Vips.Image) -> int """
    return 0

def check_precision_intfloat(domain, precision): # real signature unknown; restored from __doc__
    """ check_precision_intfloat(domain:str, precision:Vips.Precision) -> int """
    return 0

def check_separable(domain, im): # real signature unknown; restored from __doc__
    """ check_separable(domain:str, im:Vips.Image) -> int """
    return 0

def check_size_same(domain, im1, im2): # real signature unknown; restored from __doc__
    """ check_size_same(domain:str, im1:Vips.Image, im2:Vips.Image) -> int """
    return 0

def check_twocomponents(domain, im): # real signature unknown; restored from __doc__
    """ check_twocomponents(domain:str, im:Vips.Image) -> int """
    return 0

def check_u8or16(domain, im): # real signature unknown; restored from __doc__
    """ check_u8or16(domain:str, im:Vips.Image) -> int """
    return 0

def check_u8or16orf(domain, im): # real signature unknown; restored from __doc__
    """ check_u8or16orf(domain:str, im:Vips.Image) -> int """
    return 0

def check_uint(domain, im): # real signature unknown; restored from __doc__
    """ check_uint(domain:str, im:Vips.Image) -> int """
    return 0

def check_uintorf(domain, im): # real signature unknown; restored from __doc__
    """ check_uintorf(domain:str, im:Vips.Image) -> int """
    return 0

def check_uncoded(domain, im): # real signature unknown; restored from __doc__
    """ check_uncoded(domain:str, im:Vips.Image) -> int """
    return 0

def check_vector(domain, n, im): # real signature unknown; restored from __doc__
    """ check_vector(domain:str, n:int, im:Vips.Image) -> int """
    return 0

def check_vector_length(domain, n, len): # real signature unknown; restored from __doc__
    """ check_vector_length(domain:str, n:int, len:int) -> int """
    return 0

def class_find(basename, nickname): # real signature unknown; restored from __doc__
    """ class_find(basename:str, nickname:str) -> Vips.ObjectClass """
    pass

def colourspace_issupported(image): # real signature unknown; restored from __doc__
    """ colourspace_issupported(image:Vips.Image) -> bool """
    return False

def col_ab2Ch(a, b, C, h): # real signature unknown; restored from __doc__
    """ col_ab2Ch(a:float, b:float, C:float, h:float) """
    pass

def col_ab2h(a, b): # real signature unknown; restored from __doc__
    """ col_ab2h(a:float, b:float) -> float """
    return 0.0

def col_C2Ccmc(C): # real signature unknown; restored from __doc__
    """ col_C2Ccmc(C:float) -> float """
    return 0.0

def col_Ccmc2C(Ccmc): # real signature unknown; restored from __doc__
    """ col_Ccmc2C(Ccmc:float) -> float """
    return 0.0

def col_Ch2ab(C, h, a, b): # real signature unknown; restored from __doc__
    """ col_Ch2ab(C:float, h:float, a:float, b:float) """
    pass

def col_Ch2hcmc(C, h): # real signature unknown; restored from __doc__
    """ col_Ch2hcmc(C:float, h:float) -> float """
    return 0.0

def col_Chcmc2h(C, hcmc): # real signature unknown; restored from __doc__
    """ col_Chcmc2h(C:float, hcmc:float) -> float """
    return 0.0

def col_dE00(L1, a1, b1, L2, a2, b2): # real signature unknown; restored from __doc__
    """ col_dE00(L1:float, a1:float, b1:float, L2:float, a2:float, b2:float) -> float """
    return 0.0

def col_L2Lcmc(L): # real signature unknown; restored from __doc__
    """ col_L2Lcmc(L:float) -> float """
    return 0.0

def col_Lab2XYZ(L, a, b): # real signature unknown; restored from __doc__
    """ col_Lab2XYZ(L:float, a:float, b:float) -> X:float, Y:float, Z:float """
    pass

def col_Lcmc2L(Lcmc): # real signature unknown; restored from __doc__
    """ col_Lcmc2L(Lcmc:float) -> float """
    return 0.0

def col_make_tables_CMC(): # real signature unknown; restored from __doc__
    """ col_make_tables_CMC() """
    pass

def col_scRGB2BW_16(R, G, B, g, og): # real signature unknown; restored from __doc__
    """ col_scRGB2BW_16(R:float, G:float, B:float, g:int, og:int) -> int """
    return 0

def col_scRGB2BW_8(R, G, B, g, og): # real signature unknown; restored from __doc__
    """ col_scRGB2BW_8(R:float, G:float, B:float, g:int, og:int) -> int """
    return 0

def col_scRGB2sRGB_16(R, G, B, r, g, b, og): # real signature unknown; restored from __doc__
    """ col_scRGB2sRGB_16(R:float, G:float, B:float, r:int, g:int, b:int, og:int) -> int """
    return 0

def col_scRGB2sRGB_8(R, G, B, r, g, b, og): # real signature unknown; restored from __doc__
    """ col_scRGB2sRGB_8(R:float, G:float, B:float, r:int, g:int, b:int, og:int) -> int """
    return 0

def col_scRGB2XYZ(R, G, B, X, Y, Z): # real signature unknown; restored from __doc__
    """ col_scRGB2XYZ(R:float, G:float, B:float, X:float, Y:float, Z:float) -> int """
    return 0

def col_sRGB2scRGB_16(r, g, b, R, G, B): # real signature unknown; restored from __doc__
    """ col_sRGB2scRGB_16(r:int, g:int, b:int, R:float, G:float, B:float) -> int """
    return 0

def col_sRGB2scRGB_16_noclip(r, g, b, R, G, B): # real signature unknown; restored from __doc__
    """ col_sRGB2scRGB_16_noclip(r:int, g:int, b:int, R:float, G:float, B:float) -> int """
    return 0

def col_sRGB2scRGB_8(r, g, b, R, G, B): # real signature unknown; restored from __doc__
    """ col_sRGB2scRGB_8(r:int, g:int, b:int, R:float, G:float, B:float) -> int """
    return 0

def col_sRGB2scRGB_8_noclip(r, g, b, R, G, B): # real signature unknown; restored from __doc__
    """ col_sRGB2scRGB_8_noclip(r:int, g:int, b:int, R:float, G:float, B:float) -> int """
    return 0

def col_XYZ2Lab(X, Y, Z, L, a, b): # real signature unknown; restored from __doc__
    """ col_XYZ2Lab(X:float, Y:float, Z:float, L:float, a:float, b:float) """
    pass

def col_XYZ2scRGB(X, Y, Z, R, G, B): # real signature unknown; restored from __doc__
    """ col_XYZ2scRGB(X:float, Y:float, Z:float, R:float, G:float, B:float) -> int """
    return 0

def concurrency_get(): # real signature unknown; restored from __doc__
    """ concurrency_get() -> int """
    return 0

def concurrency_set(concurrency): # real signature unknown; restored from __doc__
    """ concurrency_set(concurrency:int) """
    pass

def error_buffer(): # real signature unknown; restored from __doc__
    """ error_buffer() -> str """
    return ""

def error_clear(): # real signature unknown; restored from __doc__
    """ error_clear() """
    pass

def error_freeze(): # real signature unknown; restored from __doc__
    """ error_freeze() """
    pass

def error_g(): # real signature unknown; restored from __doc__
    """ error_g() """
    pass

def error_thaw(): # real signature unknown; restored from __doc__
    """ error_thaw() """
    pass

def filename_get_filename(vips_filename): # real signature unknown; restored from __doc__
    """ filename_get_filename(vips_filename:str) -> str """
    return ""

def filename_get_options(vips_filename): # real signature unknown; restored from __doc__
    """ filename_get_options(vips_filename:str) -> str """
    return ""

def foreign_flags(loader, filename): # real signature unknown; restored from __doc__
    """ foreign_flags(loader:str, filename:str) -> Vips.ForeignFlags """
    pass

def format_sizeof(format): # real signature unknown; restored from __doc__
    """ format_sizeof(format:Vips.BandFormat) -> int """
    return 0

def free(buf=None): # real signature unknown; restored from __doc__
    """ free(buf=None) -> int """
    return 0

def get_argv0(): # real signature unknown; restored from __doc__
    """ get_argv0() -> str """
    return ""

def get_disc_threshold(): # real signature unknown; restored from __doc__
    """ get_disc_threshold() -> int """
    return 0

def guess_libdir(argv0, env_name): # real signature unknown; restored from __doc__
    """ guess_libdir(argv0:str, env_name:str) -> str """
    return ""

def guess_prefix(argv0, env_name): # real signature unknown; restored from __doc__
    """ guess_prefix(argv0:str, env_name:str) -> str """
    return ""

def g_error(): # real signature unknown; restored from __doc__
    """ g_error() """
    pass

def icc_is_compatible_profile(image, data=None, data_length): # real signature unknown; restored from __doc__
    """ icc_is_compatible_profile(image:Vips.Image, data=None, data_length:int) -> bool """
    return False

def icc_present(): # real signature unknown; restored from __doc__
    """ icc_present() -> int """
    return 0

def init(argv0): # real signature unknown; restored from __doc__
    """ init(argv0:str) -> int """
    return 0

def leak_set(leak): # real signature unknown; restored from __doc__
    """ leak_set(leak:bool) """
    pass

def malloc(p_object=None, size): # real signature unknown; restored from __doc__
    """ malloc(object:Vips.Object=None, size:int) """
    pass

def nickname_find(type): # real signature unknown; restored from __doc__
    """ nickname_find(type:GType) -> str """
    return ""

def path_filename7(path): # real signature unknown; restored from __doc__
    """ path_filename7(path:str) -> str """
    return ""

def path_mode7(path): # real signature unknown; restored from __doc__
    """ path_mode7(path:str) -> str """
    return ""

def progress_set(progress): # real signature unknown; restored from __doc__
    """ progress_set(progress:bool) """
    pass

def pythagoras(L1, a1, b1, L2, a2, b2): # real signature unknown; restored from __doc__
    """ pythagoras(L1:float, a1:float, b1:float, L2:float, a2:float, b2:float) -> float """
    return 0.0

def shutdown(): # real signature unknown; restored from __doc__
    """ shutdown() """
    pass

def strdup(p_object=None, p_str): # real signature unknown; restored from __doc__
    """ strdup(object:Vips.Object=None, str:str) -> str """
    return ""

def thread_shutdown(): # real signature unknown; restored from __doc__
    """ thread_shutdown() """
    pass

def tracked_close(fd): # real signature unknown; restored from __doc__
    """ tracked_close(fd:int) -> int """
    return 0

def tracked_free(s=None): # real signature unknown; restored from __doc__
    """ tracked_free(s=None) """
    pass

def tracked_get_allocs(): # real signature unknown; restored from __doc__
    """ tracked_get_allocs() -> int """
    return 0

def tracked_get_files(): # real signature unknown; restored from __doc__
    """ tracked_get_files() -> int """
    return 0

def tracked_get_mem(): # real signature unknown; restored from __doc__
    """ tracked_get_mem() -> int """
    return 0

def tracked_get_mem_highwater(): # real signature unknown; restored from __doc__
    """ tracked_get_mem_highwater() -> int """
    return 0

def tracked_malloc(size): # real signature unknown; restored from __doc__
    """ tracked_malloc(size:int) """
    pass

def type_depth(type): # real signature unknown; restored from __doc__
    """ type_depth(type:GType) -> int """
    return 0

def type_find(basename, nickname): # real signature unknown; restored from __doc__
    """ type_find(basename:str, nickname:str) -> GType """
    pass

def value_get_area(value, length=None): # real signature unknown; restored from __doc__
    """ value_get_area(value:GObject.Value, length:int=None) """
    pass

def value_get_array(value, n=None, type=None, sizeof_type=None): # real signature unknown; restored from __doc__
    """ value_get_array(value:GObject.Value, n:int=None, type:GType=None, sizeof_type:int=None) """
    pass

def value_get_array_double(value, n=None): # real signature unknown; restored from __doc__
    """ value_get_array_double(value:GObject.Value, n:int=None) -> float """
    return 0.0

def value_get_array_image(value, n=None): # real signature unknown; restored from __doc__
    """ value_get_array_image(value:GObject.Value, n:int=None) -> Vips.Image """
    pass

def value_get_array_int(value, n=None): # real signature unknown; restored from __doc__
    """ value_get_array_int(value:GObject.Value, n:int=None) -> int """
    return 0

def value_get_blob(value, length=None): # real signature unknown; restored from __doc__
    """ value_get_blob(value:GObject.Value, length:int=None) """
    pass

def value_get_ref_string(value, length=None): # real signature unknown; restored from __doc__
    """ value_get_ref_string(value:GObject.Value, length:int=None) -> str """
    return ""

def value_get_save_string(value): # real signature unknown; restored from __doc__
    """ value_get_save_string(value:GObject.Value) -> str """
    return ""

def value_is_null(psoec, value): # real signature unknown; restored from __doc__
    """ value_is_null(psoec:GObject.ParamSpec, value:GObject.Value) -> bool """
    return False

def value_set_area(free_fn, data=None): # real signature unknown; restored from __doc__
    """ value_set_area(free_fn:Vips.CallbackFn, data=None) -> value:GObject.Value """
    pass

def value_set_array(n, type, sizeof_type): # real signature unknown; restored from __doc__
    """ value_set_array(n:int, type:GType, sizeof_type:int) -> value:GObject.Value """
    pass

def value_set_array_double(array=None): # real signature unknown; restored from __doc__
    """ value_set_array_double(array:list=None) -> value:GObject.Value """
    pass

def value_set_array_image(n): # real signature unknown; restored from __doc__
    """ value_set_array_image(n:int) -> value:GObject.Value """
    pass

def value_set_array_int(array=None): # real signature unknown; restored from __doc__
    """ value_set_array_int(array:list=None) -> value:GObject.Value """
    pass

def value_set_array_object(n): # real signature unknown; restored from __doc__
    """ value_set_array_object(n:int) -> value:GObject.Value """
    pass

def value_set_blob(free_fn, data=None, length): # real signature unknown; restored from __doc__
    """ value_set_blob(free_fn:Vips.CallbackFn, data=None, length:int) -> value:GObject.Value """
    pass

def value_set_blob_free(data=None, length): # real signature unknown; restored from __doc__
    """ value_set_blob_free(data=None, length:int) -> value:GObject.Value """
    pass

def value_set_ref_string(p_str): # real signature unknown; restored from __doc__
    """ value_set_ref_string(str:str) -> value:GObject.Value """
    pass

def value_set_save_string(p_str): # real signature unknown; restored from __doc__
    """ value_set_save_string(str:str) -> value:GObject.Value """
    pass

def version(flag): # real signature unknown; restored from __doc__
    """ version(flag:int) -> int """
    return 0

def version_string(): # real signature unknown; restored from __doc__
    """ version_string() -> str """
    return ""

def _object_set_member(p_object, pspec, member, argument): # real signature unknown; restored from __doc__
    """ _object_set_member(object:Vips.Object, pspec:GObject.ParamSpec, member:GObject.Object, argument:GObject.Object) """
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

from .Access import Access
from .Align import Align
from .Angle import Angle
from .Angle45 import Angle45
from .Area import Area
from .Argument import Argument
from .ArgumentClass import ArgumentClass
from .ArgumentFlags import ArgumentFlags
from .ArgumentInstance import ArgumentInstance
from .ArrayDouble import ArrayDouble
from .ArrayImage import ArrayImage
from .ArrayInt import ArrayInt
from .BandFormat import BandFormat
from .BlendMode import BlendMode
from .Blob import Blob
from .Coding import Coding
from .Combine import Combine
from .CombineMode import CombineMode
from .CompassDirection import CompassDirection
from .DemandStyle import DemandStyle
from .Direction import Direction
from .Extend import Extend
from .Object import Object
from .Operation import Operation
from .Foreign import Foreign
from .ForeignClass import ForeignClass
from .ForeignDzContainer import ForeignDzContainer
from .ForeignDzDepth import ForeignDzDepth
from .ForeignDzLayout import ForeignDzLayout
from .ForeignFlags import ForeignFlags
from .ForeignLoad import ForeignLoad
from .ForeignLoadClass import ForeignLoadClass
from .ForeignPngFilter import ForeignPngFilter
from .ForeignSave import ForeignSave
from .ForeignSaveClass import ForeignSaveClass
from .ForeignTiffCompression import ForeignTiffCompression
from .ForeignTiffPredictor import ForeignTiffPredictor
from .ForeignTiffResunit import ForeignTiffResunit
from .ForeignWebpPreset import ForeignWebpPreset
from .Image import Image
from .ImageClass import ImageClass
from .ImageType import ImageType
from .Intent import Intent
from .Interesting import Interesting
from .Interpolate import Interpolate
from .InterpolateClass import InterpolateClass
from .Interpretation import Interpretation
from .Kernel import Kernel
from .ObjectClass import ObjectClass
from .OperationBoolean import OperationBoolean
from .OperationClass import OperationClass
from .OperationComplex import OperationComplex
from .OperationComplex2 import OperationComplex2
from .OperationComplexget import OperationComplexget
from .OperationFlags import OperationFlags
from .OperationMath import OperationMath
from .OperationMath2 import OperationMath2
from .OperationMorphology import OperationMorphology
from .OperationRelational import OperationRelational
from .OperationRound import OperationRound
from .PCS import PCS
from .Precision import Precision
from .Progress import Progress
from .Rect import Rect
from .RefString import RefString
from .Region import Region
from .RegionClass import RegionClass
from .RegionShrink import RegionShrink
from .Saveable import Saveable
from .SaveString import SaveString
from .Size import Size
from .Thing import Thing
from .Token import Token
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f4187706d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Vips-8.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Vips', loader=<gi.importer.DynamicImporter object at 0x7f4187706d00>)"

