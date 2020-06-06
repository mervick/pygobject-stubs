# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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
import gobject as __gobject


class IPRoutingRule(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(addr_family:int) -> NM.IPRoutingRule
    """
    def cmp(self, other=None): # real signature unknown; restored from __doc__
        """ cmp(self, other:NM.IPRoutingRule=None) -> int """
        return 0

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def from_string(self, p_str, to_string_flags, extra_args=None): # real signature unknown; restored from __doc__
        """ from_string(str:str, to_string_flags:NM.IPRoutingRuleAsStringFlags, extra_args:dict=None) -> NM.IPRoutingRule """
        pass

    def get_action(self): # real signature unknown; restored from __doc__
        """ get_action(self) -> int """
        return 0

    def get_addr_family(self): # real signature unknown; restored from __doc__
        """ get_addr_family(self) -> int """
        return 0

    def get_destination_port_end(self): # real signature unknown; restored from __doc__
        """ get_destination_port_end(self) -> int """
        return 0

    def get_destination_port_start(self): # real signature unknown; restored from __doc__
        """ get_destination_port_start(self) -> int """
        return 0

    def get_from(self): # real signature unknown; restored from __doc__
        """ get_from(self) -> str """
        return ""

    def get_from_len(self): # real signature unknown; restored from __doc__
        """ get_from_len(self) -> int """
        return 0

    def get_fwmark(self): # real signature unknown; restored from __doc__
        """ get_fwmark(self) -> int """
        return 0

    def get_fwmask(self): # real signature unknown; restored from __doc__
        """ get_fwmask(self) -> int """
        return 0

    def get_iifname(self): # real signature unknown; restored from __doc__
        """ get_iifname(self) -> str """
        return ""

    def get_invert(self): # real signature unknown; restored from __doc__
        """ get_invert(self) -> bool """
        return False

    def get_ipproto(self): # real signature unknown; restored from __doc__
        """ get_ipproto(self) -> int """
        return 0

    def get_oifname(self): # real signature unknown; restored from __doc__
        """ get_oifname(self) -> str """
        return ""

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_source_port_end(self): # real signature unknown; restored from __doc__
        """ get_source_port_end(self) -> int """
        return 0

    def get_source_port_start(self): # real signature unknown; restored from __doc__
        """ get_source_port_start(self) -> int """
        return 0

    def get_suppress_prefixlength(self): # real signature unknown; restored from __doc__
        """ get_suppress_prefixlength(self) -> int """
        return 0

    def get_table(self): # real signature unknown; restored from __doc__
        """ get_table(self) -> int """
        return 0

    def get_to(self): # real signature unknown; restored from __doc__
        """ get_to(self) -> str """
        return ""

    def get_tos(self): # real signature unknown; restored from __doc__
        """ get_tos(self) -> int """
        return 0

    def get_to_len(self): # real signature unknown; restored from __doc__
        """ get_to_len(self) -> int """
        return 0

    def is_sealed(self): # real signature unknown; restored from __doc__
        """ is_sealed(self) -> bool """
        return False

    def new(self, addr_family): # real signature unknown; restored from __doc__
        """ new(addr_family:int) -> NM.IPRoutingRule """
        pass

    def new_clone(self): # real signature unknown; restored from __doc__
        """ new_clone(self) -> NM.IPRoutingRule """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> NM.IPRoutingRule """
        pass

    def seal(self): # real signature unknown; restored from __doc__
        """ seal(self) """
        pass

    def set_action(self, action): # real signature unknown; restored from __doc__
        """ set_action(self, action:int) """
        pass

    def set_destination_port(self, start, end): # real signature unknown; restored from __doc__
        """ set_destination_port(self, start:int, end:int) """
        pass

    def set_from(self, from_=None, len): # real signature unknown; restored from __doc__
        """ set_from(self, from_:str=None, len:int) """
        pass

    def set_fwmark(self, fwmark, fwmask): # real signature unknown; restored from __doc__
        """ set_fwmark(self, fwmark:int, fwmask:int) """
        pass

    def set_iifname(self, iifname=None): # real signature unknown; restored from __doc__
        """ set_iifname(self, iifname:str=None) """
        pass

    def set_invert(self, invert): # real signature unknown; restored from __doc__
        """ set_invert(self, invert:bool) """
        pass

    def set_ipproto(self, ipproto): # real signature unknown; restored from __doc__
        """ set_ipproto(self, ipproto:int) """
        pass

    def set_oifname(self, oifname=None): # real signature unknown; restored from __doc__
        """ set_oifname(self, oifname:str=None) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
        pass

    def set_source_port(self, start, end): # real signature unknown; restored from __doc__
        """ set_source_port(self, start:int, end:int) """
        pass

    def set_suppress_prefixlength(self, suppress_prefixlength): # real signature unknown; restored from __doc__
        """ set_suppress_prefixlength(self, suppress_prefixlength:int) """
        pass

    def set_table(self, table): # real signature unknown; restored from __doc__
        """ set_table(self, table:int) """
        pass

    def set_to(self, to=None, len): # real signature unknown; restored from __doc__
        """ set_to(self, to:str=None, len:int) """
        pass

    def set_tos(self, tos): # real signature unknown; restored from __doc__
        """ set_tos(self, tos:int) """
        pass

    def to_string(self, to_string_flags, extra_args=None): # real signature unknown; restored from __doc__
        """ to_string(self, to_string_flags:NM.IPRoutingRuleAsStringFlags, extra_args:dict=None) -> str """
        return ""

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def validate(self): # real signature unknown; restored from __doc__
        """ validate(self) -> bool """
        return False

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
        """ new(addr_family:int) -> NM.IPRoutingRule """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(IPRoutingRule), '__module__': 'gi.repository.NM', '__gtype__': <GType NMIPRoutingRule (94741104323424)>, '__dict__': <attribute '__dict__' of 'IPRoutingRule' objects>, '__weakref__': <attribute '__weakref__' of 'IPRoutingRule' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'cmp': gi.FunctionInfo(cmp), 'get_action': gi.FunctionInfo(get_action), 'get_addr_family': gi.FunctionInfo(get_addr_family), 'get_destination_port_end': gi.FunctionInfo(get_destination_port_end), 'get_destination_port_start': gi.FunctionInfo(get_destination_port_start), 'get_from': gi.FunctionInfo(get_from), 'get_from_len': gi.FunctionInfo(get_from_len), 'get_fwmark': gi.FunctionInfo(get_fwmark), 'get_fwmask': gi.FunctionInfo(get_fwmask), 'get_iifname': gi.FunctionInfo(get_iifname), 'get_invert': gi.FunctionInfo(get_invert), 'get_ipproto': gi.FunctionInfo(get_ipproto), 'get_oifname': gi.FunctionInfo(get_oifname), 'get_priority': gi.FunctionInfo(get_priority), 'get_source_port_end': gi.FunctionInfo(get_source_port_end), 'get_source_port_start': gi.FunctionInfo(get_source_port_start), 'get_suppress_prefixlength': gi.FunctionInfo(get_suppress_prefixlength), 'get_table': gi.FunctionInfo(get_table), 'get_to': gi.FunctionInfo(get_to), 'get_to_len': gi.FunctionInfo(get_to_len), 'get_tos': gi.FunctionInfo(get_tos), 'is_sealed': gi.FunctionInfo(is_sealed), 'new_clone': gi.FunctionInfo(new_clone), 'ref': gi.FunctionInfo(ref), 'seal': gi.FunctionInfo(seal), 'set_action': gi.FunctionInfo(set_action), 'set_destination_port': gi.FunctionInfo(set_destination_port), 'set_from': gi.FunctionInfo(set_from), 'set_fwmark': gi.FunctionInfo(set_fwmark), 'set_iifname': gi.FunctionInfo(set_iifname), 'set_invert': gi.FunctionInfo(set_invert), 'set_ipproto': gi.FunctionInfo(set_ipproto), 'set_oifname': gi.FunctionInfo(set_oifname), 'set_priority': gi.FunctionInfo(set_priority), 'set_source_port': gi.FunctionInfo(set_source_port), 'set_suppress_prefixlength': gi.FunctionInfo(set_suppress_prefixlength), 'set_table': gi.FunctionInfo(set_table), 'set_to': gi.FunctionInfo(set_to), 'set_tos': gi.FunctionInfo(set_tos), 'to_string': gi.FunctionInfo(to_string), 'unref': gi.FunctionInfo(unref), 'validate': gi.FunctionInfo(validate), 'from_string': gi.FunctionInfo(from_string), '__new__': <staticmethod object at 0x7fb9b8cb7490>, '__init__': <function nothing at 0x7fb9b8f70ee0>})"
    __gtype__ = None # (!) real value is '<GType NMIPRoutingRule (94741104323424)>'
    __info__ = StructInfo(IPRoutingRule)


