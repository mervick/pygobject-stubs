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


class ComponentAlarmTrigger(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_absolute(absolute_time:ICalGLib.Time) -> ECal.ComponentAlarmTrigger
        new_from_property(property:ICalGLib.Property) -> ECal.ComponentAlarmTrigger or None
        new_relative(kind:ECal.ComponentAlarmTriggerKind, duration:ICalGLib.Duration) -> ECal.ComponentAlarmTrigger
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> ECal.ComponentAlarmTrigger """
        pass

    def fill_property(self, property): # real signature unknown; restored from __doc__
        """ fill_property(self, property:ICalGLib.Property) -> property:ICalGLib.Property """
        return property(*(), **{})

    def get_absolute_time(self): # real signature unknown; restored from __doc__
        """ get_absolute_time(self) -> ICalGLib.Time or None """
        pass

    def get_as_property(self): # real signature unknown; restored from __doc__
        """ get_as_property(self) -> ICalGLib.Property """
        pass

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> ICalGLib.Duration or None """
        pass

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> ECal.ComponentAlarmTriggerKind """
        pass

    def get_parameter_bag(self): # real signature unknown; restored from __doc__
        """ get_parameter_bag(self) -> ECal.ComponentParameterBag """
        pass

    def new_absolute(self, absolute_time): # real signature unknown; restored from __doc__
        """ new_absolute(absolute_time:ICalGLib.Time) -> ECal.ComponentAlarmTrigger """
        pass

    def new_from_property(self, property): # real signature unknown; restored from __doc__
        """ new_from_property(property:ICalGLib.Property) -> ECal.ComponentAlarmTrigger or None """
        pass

    def new_relative(self, kind, duration): # real signature unknown; restored from __doc__
        """ new_relative(kind:ECal.ComponentAlarmTriggerKind, duration:ICalGLib.Duration) -> ECal.ComponentAlarmTrigger """
        pass

    def set_absolute(self, absolute_time): # real signature unknown; restored from __doc__
        """ set_absolute(self, absolute_time:ICalGLib.Time) """
        pass

    def set_absolute_time(self, absolute_time): # real signature unknown; restored from __doc__
        """ set_absolute_time(self, absolute_time:ICalGLib.Time) """
        pass

    def set_duration(self, duration): # real signature unknown; restored from __doc__
        """ set_duration(self, duration:ICalGLib.Duration) """
        pass

    def set_from_property(self, property): # real signature unknown; restored from __doc__
        """ set_from_property(self, property:ICalGLib.Property) """
        pass

    def set_kind(self, kind): # real signature unknown; restored from __doc__
        """ set_kind(self, kind:ECal.ComponentAlarmTriggerKind) """
        pass

    def set_relative(self, kind, duration): # real signature unknown; restored from __doc__
        """ set_relative(self, kind:ECal.ComponentAlarmTriggerKind, duration:ICalGLib.Duration) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ComponentAlarmTrigger), '__module__': 'gi.repository.ECal', '__gtype__': <GType ECalComponentAlarmTrigger (94764814863520)>, '__dict__': <attribute '__dict__' of 'ComponentAlarmTrigger' objects>, '__weakref__': <attribute '__weakref__' of 'ComponentAlarmTrigger' objects>, '__doc__': None, 'new_absolute': gi.FunctionInfo(new_absolute), 'new_from_property': gi.FunctionInfo(new_from_property), 'new_relative': gi.FunctionInfo(new_relative), 'copy': gi.FunctionInfo(copy), 'fill_property': gi.FunctionInfo(fill_property), 'get_absolute_time': gi.FunctionInfo(get_absolute_time), 'get_as_property': gi.FunctionInfo(get_as_property), 'get_duration': gi.FunctionInfo(get_duration), 'get_kind': gi.FunctionInfo(get_kind), 'get_parameter_bag': gi.FunctionInfo(get_parameter_bag), 'set_absolute': gi.FunctionInfo(set_absolute), 'set_absolute_time': gi.FunctionInfo(set_absolute_time), 'set_duration': gi.FunctionInfo(set_duration), 'set_from_property': gi.FunctionInfo(set_from_property), 'set_kind': gi.FunctionInfo(set_kind), 'set_relative': gi.FunctionInfo(set_relative)})"
    __gtype__ = None # (!) real value is '<GType ECalComponentAlarmTrigger (94764814863520)>'
    __info__ = StructInfo(ComponentAlarmTrigger)


