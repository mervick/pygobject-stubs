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


class ComponentAlarm(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> ECal.ComponentAlarm
        new_from_component(component:ICalGLib.Component) -> ECal.ComponentAlarm or None
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> ECal.ComponentAlarm """
        pass

    def fill_component(self, component): # real signature unknown; restored from __doc__
        """ fill_component(self, component:ICalGLib.Component) """
        pass

    def get_action(self): # real signature unknown; restored from __doc__
        """ get_action(self) -> ECal.ComponentAlarmAction """
        pass

    def get_as_component(self): # real signature unknown; restored from __doc__
        """ get_as_component(self) -> ICalGLib.Component """
        pass

    def get_attachments(self): # real signature unknown; restored from __doc__
        """ get_attachments(self) -> list or None """
        return []

    def get_attendees(self): # real signature unknown; restored from __doc__
        """ get_attendees(self) -> list or None """
        return []

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> ECal.ComponentText or None """
        pass

    def get_property_bag(self): # real signature unknown; restored from __doc__
        """ get_property_bag(self) -> ECal.ComponentPropertyBag """
        pass

    def get_repeat(self): # real signature unknown; restored from __doc__
        """ get_repeat(self) -> ECal.ComponentAlarmRepeat or None """
        pass

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> ECal.ComponentText or None """
        pass

    def get_trigger(self): # real signature unknown; restored from __doc__
        """ get_trigger(self) -> ECal.ComponentAlarmTrigger or None """
        pass

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str or None """
        return ""

    def has_attachments(self): # real signature unknown; restored from __doc__
        """ has_attachments(self) -> bool """
        return False

    def has_attendees(self): # real signature unknown; restored from __doc__
        """ has_attendees(self) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> ECal.ComponentAlarm """
        pass

    def new_from_component(self, component): # real signature unknown; restored from __doc__
        """ new_from_component(component:ICalGLib.Component) -> ECal.ComponentAlarm or None """
        pass

    def set_action(self, action): # real signature unknown; restored from __doc__
        """ set_action(self, action:ECal.ComponentAlarmAction) """
        pass

    def set_attachments(self, attachments=None): # real signature unknown; restored from __doc__
        """ set_attachments(self, attachments:list=None) """
        pass

    def set_attendees(self, attendees=None): # real signature unknown; restored from __doc__
        """ set_attendees(self, attendees:list=None) """
        pass

    def set_description(self, description=None): # real signature unknown; restored from __doc__
        """ set_description(self, description:ECal.ComponentText=None) """
        pass

    def set_from_component(self, component): # real signature unknown; restored from __doc__
        """ set_from_component(self, component:ICalGLib.Component) """
        pass

    def set_repeat(self, repeat=None): # real signature unknown; restored from __doc__
        """ set_repeat(self, repeat:ECal.ComponentAlarmRepeat=None) """
        pass

    def set_summary(self, summary=None): # real signature unknown; restored from __doc__
        """ set_summary(self, summary:ECal.ComponentText=None) """
        pass

    def set_trigger(self, trigger=None): # real signature unknown; restored from __doc__
        """ set_trigger(self, trigger:ECal.ComponentAlarmTrigger=None) """
        pass

    def set_uid(self, uid=None): # real signature unknown; restored from __doc__
        """ set_uid(self, uid:str=None) """
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
        """ new() -> ECal.ComponentAlarm """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ComponentAlarm), '__module__': 'gi.repository.ECal', '__gtype__': <GType ECalComponentAlarm (94764814838832)>, '__dict__': <attribute '__dict__' of 'ComponentAlarm' objects>, '__weakref__': <attribute '__weakref__' of 'ComponentAlarm' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_from_component': gi.FunctionInfo(new_from_component), 'copy': gi.FunctionInfo(copy), 'fill_component': gi.FunctionInfo(fill_component), 'get_action': gi.FunctionInfo(get_action), 'get_as_component': gi.FunctionInfo(get_as_component), 'get_attachments': gi.FunctionInfo(get_attachments), 'get_attendees': gi.FunctionInfo(get_attendees), 'get_description': gi.FunctionInfo(get_description), 'get_property_bag': gi.FunctionInfo(get_property_bag), 'get_repeat': gi.FunctionInfo(get_repeat), 'get_summary': gi.FunctionInfo(get_summary), 'get_trigger': gi.FunctionInfo(get_trigger), 'get_uid': gi.FunctionInfo(get_uid), 'has_attachments': gi.FunctionInfo(has_attachments), 'has_attendees': gi.FunctionInfo(has_attendees), 'set_action': gi.FunctionInfo(set_action), 'set_attachments': gi.FunctionInfo(set_attachments), 'set_attendees': gi.FunctionInfo(set_attendees), 'set_description': gi.FunctionInfo(set_description), 'set_from_component': gi.FunctionInfo(set_from_component), 'set_repeat': gi.FunctionInfo(set_repeat), 'set_summary': gi.FunctionInfo(set_summary), 'set_trigger': gi.FunctionInfo(set_trigger), 'set_uid': gi.FunctionInfo(set_uid), '__new__': <staticmethod object at 0x7fe5cce055e0>, '__init__': <function nothing at 0x7fe5cd0d7ee0>})"
    __gtype__ = None # (!) real value is '<GType ECalComponentAlarm (94764814838832)>'
    __info__ = StructInfo(ComponentAlarm)


