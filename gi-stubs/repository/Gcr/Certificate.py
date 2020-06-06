# encoding: utf-8
# module gi.repository.Gcr
# from /usr/lib64/girepository-1.0/Gcr-3.typelib
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
import gi.repository.Gck as __gi_repository_Gck
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class Certificate(__gobject.GInterface):
    # no doc
    def compare(self, first=None, other=None): # real signature unknown; restored from __doc__
        """ compare(first:Gcr.Comparable=None, other:Gcr.Comparable=None) -> int """
        return 0

    def get_basic_constraints(self): # real signature unknown; restored from __doc__
        """ get_basic_constraints(self) -> bool, is_ca:bool, path_len:int """
        return False

    def get_der_data(self): # real signature unknown; restored from __doc__
        """ get_der_data(self) -> list, n_data:int """
        return []

    def get_expiry_date(self): # real signature unknown; restored from __doc__
        """ get_expiry_date(self) -> GLib.Date """
        pass

    def get_fingerprint(self, type): # real signature unknown; restored from __doc__
        """ get_fingerprint(self, type:GLib.ChecksumType) -> list, n_length:int """
        return []

    def get_fingerprint_hex(self, type): # real signature unknown; restored from __doc__
        """ get_fingerprint_hex(self, type:GLib.ChecksumType) -> str """
        return ""

    def get_issued_date(self): # real signature unknown; restored from __doc__
        """ get_issued_date(self) -> GLib.Date """
        pass

    def get_issuer_cn(self): # real signature unknown; restored from __doc__
        """ get_issuer_cn(self) -> str """
        return ""

    def get_issuer_dn(self): # real signature unknown; restored from __doc__
        """ get_issuer_dn(self) -> str """
        return ""

    def get_issuer_name(self): # real signature unknown; restored from __doc__
        """ get_issuer_name(self) -> str """
        return ""

    def get_issuer_part(self, part): # real signature unknown; restored from __doc__
        """ get_issuer_part(self, part:str) -> str or None """
        return ""

    def get_issuer_raw(self): # real signature unknown; restored from __doc__
        """ get_issuer_raw(self) -> list, n_data:int """
        return []

    def get_key_size(self): # real signature unknown; restored from __doc__
        """ get_key_size(self) -> int """
        return 0

    def get_markup_text(self): # real signature unknown; restored from __doc__
        """ get_markup_text(self) -> str """
        return ""

    def get_serial_number(self): # real signature unknown; restored from __doc__
        """ get_serial_number(self) -> list, n_length:int """
        return []

    def get_serial_number_hex(self): # real signature unknown; restored from __doc__
        """ get_serial_number_hex(self) -> str """
        return ""

    def get_subject_cn(self): # real signature unknown; restored from __doc__
        """ get_subject_cn(self) -> str """
        return ""

    def get_subject_dn(self): # real signature unknown; restored from __doc__
        """ get_subject_dn(self) -> str """
        return ""

    def get_subject_name(self): # real signature unknown; restored from __doc__
        """ get_subject_name(self) -> str """
        return ""

    def get_subject_part(self, part): # real signature unknown; restored from __doc__
        """ get_subject_part(self, part:str) -> str or None """
        return ""

    def get_subject_raw(self): # real signature unknown; restored from __doc__
        """ get_subject_raw(self) -> list, n_data:int """
        return []

    def is_issuer(self, issuer): # real signature unknown; restored from __doc__
        """ is_issuer(self, issuer:Gcr.Certificate) -> bool """
        return False

    def mixin_emit_notify(self): # real signature unknown; restored from __doc__
        """ mixin_emit_notify(self) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Certificate), '__module__': 'gi.repository.Gcr', '__gtype__': <GType GcrCertificate (94112497378416)>, '__dict__': <attribute '__dict__' of 'Certificate' objects>, '__weakref__': <attribute '__weakref__' of 'Certificate' objects>, '__doc__': None, '__gsignals__': {}, 'compare': gi.FunctionInfo(compare), 'get_basic_constraints': gi.FunctionInfo(get_basic_constraints), 'get_der_data': gi.FunctionInfo(get_der_data), 'get_expiry_date': gi.FunctionInfo(get_expiry_date), 'get_fingerprint': gi.FunctionInfo(get_fingerprint), 'get_fingerprint_hex': gi.FunctionInfo(get_fingerprint_hex), 'get_issued_date': gi.FunctionInfo(get_issued_date), 'get_issuer_cn': gi.FunctionInfo(get_issuer_cn), 'get_issuer_dn': gi.FunctionInfo(get_issuer_dn), 'get_issuer_name': gi.FunctionInfo(get_issuer_name), 'get_issuer_part': gi.FunctionInfo(get_issuer_part), 'get_issuer_raw': gi.FunctionInfo(get_issuer_raw), 'get_key_size': gi.FunctionInfo(get_key_size), 'get_markup_text': gi.FunctionInfo(get_markup_text), 'get_serial_number': gi.FunctionInfo(get_serial_number), 'get_serial_number_hex': gi.FunctionInfo(get_serial_number_hex), 'get_subject_cn': gi.FunctionInfo(get_subject_cn), 'get_subject_dn': gi.FunctionInfo(get_subject_dn), 'get_subject_name': gi.FunctionInfo(get_subject_name), 'get_subject_part': gi.FunctionInfo(get_subject_part), 'get_subject_raw': gi.FunctionInfo(get_subject_raw), 'is_issuer': gi.FunctionInfo(is_issuer), 'mixin_emit_notify': gi.FunctionInfo(mixin_emit_notify)})"
    __gdoc__ = 'Interface GcrCertificate\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GcrCertificate (94112497378416)>'
    __info__ = InterfaceInfo(Certificate)


