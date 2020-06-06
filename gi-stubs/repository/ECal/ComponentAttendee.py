# encoding: utf-8
# module gi.repository.ECal
# from /usr/lib64/girepository-1.0/ECal-2.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class ComponentAttendee(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> ECal.ComponentAttendee
        new_from_property(property:ICalGLib.Property) -> ECal.ComponentAttendee or None
        new_full(value:str=None, member:str=None, cutype:ICalGLib.ParameterCutype, role:ICalGLib.ParameterRole, partstat:ICalGLib.ParameterPartstat, rsvp:bool, delegatedfrom:str=None, delegatedto:str=None, sentby:str=None, cn:str=None, language:str=None) -> ECal.ComponentAttendee
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> ECal.ComponentAttendee """
        pass

    def fill_property(self, property): # real signature unknown; restored from __doc__
        """ fill_property(self, property:ICalGLib.Property) -> property:ICalGLib.Property """
        return property(*(), **{})

    def get_as_property(self): # real signature unknown; restored from __doc__
        """ get_as_property(self) -> ICalGLib.Property """
        pass

    def get_cn(self): # real signature unknown; restored from __doc__
        """ get_cn(self) -> str or None """
        return ""

    def get_cutype(self): # real signature unknown; restored from __doc__
        """ get_cutype(self) -> ICalGLib.ParameterCutype """
        pass

    def get_delegatedfrom(self): # real signature unknown; restored from __doc__
        """ get_delegatedfrom(self) -> str or None """
        return ""

    def get_delegatedto(self): # real signature unknown; restored from __doc__
        """ get_delegatedto(self) -> str or None """
        return ""

    def get_language(self): # real signature unknown; restored from __doc__
        """ get_language(self) -> str or None """
        return ""

    def get_member(self): # real signature unknown; restored from __doc__
        """ get_member(self) -> str or None """
        return ""

    def get_parameter_bag(self): # real signature unknown; restored from __doc__
        """ get_parameter_bag(self) -> ECal.ComponentParameterBag """
        pass

    def get_partstat(self): # real signature unknown; restored from __doc__
        """ get_partstat(self) -> ICalGLib.ParameterPartstat """
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> ICalGLib.ParameterRole """
        pass

    def get_rsvp(self): # real signature unknown; restored from __doc__
        """ get_rsvp(self) -> bool """
        return False

    def get_sentby(self): # real signature unknown; restored from __doc__
        """ get_sentby(self) -> str or None """
        return ""

    def get_value(self): # real signature unknown; restored from __doc__
        """ get_value(self) -> str or None """
        return ""

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> ECal.ComponentAttendee """
        pass

    def new_from_property(self, property): # real signature unknown; restored from __doc__
        """ new_from_property(property:ICalGLib.Property) -> ECal.ComponentAttendee or None """
        pass

    def new_full(self, value=None, member=None, cutype, role, partstat, rsvp, delegatedfrom=None, delegatedto=None, sentby=None, cn=None, language=None): # real signature unknown; restored from __doc__
        """ new_full(value:str=None, member:str=None, cutype:ICalGLib.ParameterCutype, role:ICalGLib.ParameterRole, partstat:ICalGLib.ParameterPartstat, rsvp:bool, delegatedfrom:str=None, delegatedto:str=None, sentby:str=None, cn:str=None, language:str=None) -> ECal.ComponentAttendee """
        pass

    def set_cn(self, cn=None): # real signature unknown; restored from __doc__
        """ set_cn(self, cn:str=None) """
        pass

    def set_cutype(self, cutype): # real signature unknown; restored from __doc__
        """ set_cutype(self, cutype:ICalGLib.ParameterCutype) """
        pass

    def set_delegatedfrom(self, delegatedfrom=None): # real signature unknown; restored from __doc__
        """ set_delegatedfrom(self, delegatedfrom:str=None) """
        pass

    def set_delegatedto(self, delegatedto=None): # real signature unknown; restored from __doc__
        """ set_delegatedto(self, delegatedto:str=None) """
        pass

    def set_from_property(self, property): # real signature unknown; restored from __doc__
        """ set_from_property(self, property:ICalGLib.Property) """
        pass

    def set_language(self, language=None): # real signature unknown; restored from __doc__
        """ set_language(self, language:str=None) """
        pass

    def set_member(self, member=None): # real signature unknown; restored from __doc__
        """ set_member(self, member:str=None) """
        pass

    def set_partstat(self, partstat): # real signature unknown; restored from __doc__
        """ set_partstat(self, partstat:ICalGLib.ParameterPartstat) """
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:ICalGLib.ParameterRole) """
        pass

    def set_rsvp(self, rsvp): # real signature unknown; restored from __doc__
        """ set_rsvp(self, rsvp:bool) """
        pass

    def set_sentby(self, sentby=None): # real signature unknown; restored from __doc__
        """ set_sentby(self, sentby:str=None) """
        pass

    def set_value(self, value=None): # real signature unknown; restored from __doc__
        """ set_value(self, value:str=None) """
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
        """ new() -> ECal.ComponentAttendee """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ComponentAttendee), '__module__': 'gi.repository.ECal', '__gtype__': <GType ECalComponentAttendee (94764814871184)>, '__dict__': <attribute '__dict__' of 'ComponentAttendee' objects>, '__weakref__': <attribute '__weakref__' of 'ComponentAttendee' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_from_property': gi.FunctionInfo(new_from_property), 'new_full': gi.FunctionInfo(new_full), 'copy': gi.FunctionInfo(copy), 'fill_property': gi.FunctionInfo(fill_property), 'get_as_property': gi.FunctionInfo(get_as_property), 'get_cn': gi.FunctionInfo(get_cn), 'get_cutype': gi.FunctionInfo(get_cutype), 'get_delegatedfrom': gi.FunctionInfo(get_delegatedfrom), 'get_delegatedto': gi.FunctionInfo(get_delegatedto), 'get_language': gi.FunctionInfo(get_language), 'get_member': gi.FunctionInfo(get_member), 'get_parameter_bag': gi.FunctionInfo(get_parameter_bag), 'get_partstat': gi.FunctionInfo(get_partstat), 'get_role': gi.FunctionInfo(get_role), 'get_rsvp': gi.FunctionInfo(get_rsvp), 'get_sentby': gi.FunctionInfo(get_sentby), 'get_value': gi.FunctionInfo(get_value), 'set_cn': gi.FunctionInfo(set_cn), 'set_cutype': gi.FunctionInfo(set_cutype), 'set_delegatedfrom': gi.FunctionInfo(set_delegatedfrom), 'set_delegatedto': gi.FunctionInfo(set_delegatedto), 'set_from_property': gi.FunctionInfo(set_from_property), 'set_language': gi.FunctionInfo(set_language), 'set_member': gi.FunctionInfo(set_member), 'set_partstat': gi.FunctionInfo(set_partstat), 'set_role': gi.FunctionInfo(set_role), 'set_rsvp': gi.FunctionInfo(set_rsvp), 'set_sentby': gi.FunctionInfo(set_sentby), 'set_value': gi.FunctionInfo(set_value), '__new__': <staticmethod object at 0x7fe5cce05940>, '__init__': <function nothing at 0x7fe5cd0d7ee0>})"
    __gtype__ = None # (!) real value is '<GType ECalComponentAttendee (94764814871184)>'
    __info__ = StructInfo(ComponentAttendee)


