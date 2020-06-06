# encoding: utf-8
# module gi.repository.GMime
# from /usr/lib64/girepository-1.0/GMime-3.0.typelib
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


class ParserOptions(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> GMime.ParserOptions
    """
    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> GMime.ParserOptions """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_address_compliance_mode(self): # real signature unknown; restored from __doc__
        """ get_address_compliance_mode(self) -> GMime.RfcComplianceMode """
        pass

    def get_allow_addresses_without_domain(self): # real signature unknown; restored from __doc__
        """ get_allow_addresses_without_domain(self) -> bool """
        return False

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> GMime.ParserOptions """
        pass

    def get_fallback_charsets(self): # real signature unknown; restored from __doc__
        """ get_fallback_charsets(self) -> list """
        return []

    def get_parameter_compliance_mode(self): # real signature unknown; restored from __doc__
        """ get_parameter_compliance_mode(self) -> GMime.RfcComplianceMode """
        pass

    def get_rfc2047_compliance_mode(self): # real signature unknown; restored from __doc__
        """ get_rfc2047_compliance_mode(self) -> GMime.RfcComplianceMode """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GMime.ParserOptions """
        pass

    def set_address_compliance_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_address_compliance_mode(self, mode:GMime.RfcComplianceMode) """
        pass

    def set_allow_addresses_without_domain(self, allow): # real signature unknown; restored from __doc__
        """ set_allow_addresses_without_domain(self, allow:bool) """
        pass

    def set_fallback_charsets(self, charsets): # real signature unknown; restored from __doc__
        """ set_fallback_charsets(self, charsets:str) """
        pass

    def set_parameter_compliance_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_parameter_compliance_mode(self, mode:GMime.RfcComplianceMode) """
        pass

    def set_rfc2047_compliance_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_rfc2047_compliance_mode(self, mode:GMime.RfcComplianceMode) """
        pass

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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> GMime.ParserOptions """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ParserOptions), '__module__': 'gi.repository.GMime', '__gtype__': <GType GMimeParserOptions (94235496173424)>, '__dict__': <attribute '__dict__' of 'ParserOptions' objects>, '__weakref__': <attribute '__weakref__' of 'ParserOptions' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'clone': gi.FunctionInfo(clone), 'free': gi.FunctionInfo(free), 'get_address_compliance_mode': gi.FunctionInfo(get_address_compliance_mode), 'get_allow_addresses_without_domain': gi.FunctionInfo(get_allow_addresses_without_domain), 'get_fallback_charsets': gi.FunctionInfo(get_fallback_charsets), 'get_parameter_compliance_mode': gi.FunctionInfo(get_parameter_compliance_mode), 'get_rfc2047_compliance_mode': gi.FunctionInfo(get_rfc2047_compliance_mode), 'set_address_compliance_mode': gi.FunctionInfo(set_address_compliance_mode), 'set_allow_addresses_without_domain': gi.FunctionInfo(set_allow_addresses_without_domain), 'set_fallback_charsets': gi.FunctionInfo(set_fallback_charsets), 'set_parameter_compliance_mode': gi.FunctionInfo(set_parameter_compliance_mode), 'set_rfc2047_compliance_mode': gi.FunctionInfo(set_rfc2047_compliance_mode), 'get_default': gi.FunctionInfo(get_default), '__new__': <staticmethod object at 0x7fc970741b50>, '__init__': <function nothing at 0x7fc970afcee0>})"
    __gtype__ = None # (!) real value is '<GType GMimeParserOptions (94235496173424)>'
    __info__ = StructInfo(ParserOptions)


