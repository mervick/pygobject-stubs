# encoding: utf-8
# module gi.repository.EBookContacts
# from /usr/lib64/girepository-1.0/EBookContacts-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gobject as __gobject


class PhoneNumber(__gi.Boxed):
    # no doc
    def compare(self, second_number): # real signature unknown; restored from __doc__
        """ compare(self, second_number:EBookContacts.PhoneNumber) -> EBookContacts.PhoneNumberMatch """
        pass

    def compare_strings(self, first_number, second_number): # real signature unknown; restored from __doc__
        """ compare_strings(first_number:str, second_number:str) -> EBookContacts.PhoneNumberMatch """
        pass

    def compare_strings_with_region(self, first_number, second_number, region_code=None): # real signature unknown; restored from __doc__
        """ compare_strings_with_region(first_number:str, second_number:str, region_code:str=None) -> EBookContacts.PhoneNumberMatch """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EBookContacts.PhoneNumber """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_string(self, phone_number, region_code=None): # real signature unknown; restored from __doc__
        """ from_string(phone_number:str, region_code:str=None) -> EBookContacts.PhoneNumber """
        pass

    def get_country_code(self, source): # real signature unknown; restored from __doc__
        """ get_country_code(self, source:EBookContacts.PhoneNumberCountrySource) -> int """
        return 0

    def get_country_code_for_region(self, region_code=None): # real signature unknown; restored from __doc__
        """ get_country_code_for_region(region_code:str=None) -> int """
        return 0

    def get_default_region(self): # real signature unknown; restored from __doc__
        """ get_default_region() -> str """
        return ""

    def get_national_number(self): # real signature unknown; restored from __doc__
        """ get_national_number(self) -> str """
        return ""

    def is_supported(self): # real signature unknown; restored from __doc__
        """ is_supported() -> bool """
        return False

    def to_string(self, format): # real signature unknown; restored from __doc__
        """ to_string(self, format:EBookContacts.PhoneNumberFormat) -> str """
        return ""

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PhoneNumber), '__module__': 'gi.repository.EBookContacts', '__gtype__': <GType EPhoneNumber (94769385607920)>, '__dict__': <attribute '__dict__' of 'PhoneNumber' objects>, '__weakref__': <attribute '__weakref__' of 'PhoneNumber' objects>, '__doc__': None, 'compare': gi.FunctionInfo(compare), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_country_code': gi.FunctionInfo(get_country_code), 'get_national_number': gi.FunctionInfo(get_national_number), 'to_string': gi.FunctionInfo(to_string), 'compare_strings': gi.FunctionInfo(compare_strings), 'compare_strings_with_region': gi.FunctionInfo(compare_strings_with_region), 'error_quark': gi.FunctionInfo(error_quark), 'from_string': gi.FunctionInfo(from_string), 'get_country_code_for_region': gi.FunctionInfo(get_country_code_for_region), 'get_default_region': gi.FunctionInfo(get_default_region), 'is_supported': gi.FunctionInfo(is_supported)})"
    __gtype__ = None # (!) real value is '<GType EPhoneNumber (94769385607920)>'
    __info__ = StructInfo(PhoneNumber)


