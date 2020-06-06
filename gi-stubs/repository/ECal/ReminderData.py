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


class ReminderData(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(source_uid:str, component:ECal.Component, instance:ECal.ComponentAlarmInstance) -> ECal.ReminderData
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> ECal.ReminderData """
        pass

    def free(self, rd=None): # real signature unknown; restored from __doc__
        """ free(rd=None) """
        pass

    def get_component(self): # real signature unknown; restored from __doc__
        """ get_component(self) -> ECal.Component """
        pass

    def get_instance(self): # real signature unknown; restored from __doc__
        """ get_instance(self) -> ECal.ComponentAlarmInstance """
        pass

    def get_source_uid(self): # real signature unknown; restored from __doc__
        """ get_source_uid(self) -> str """
        return ""

    def new(self, source_uid, component, instance): # real signature unknown; restored from __doc__
        """ new(source_uid:str, component:ECal.Component, instance:ECal.ComponentAlarmInstance) -> ECal.ReminderData """
        pass

    def set_component(self, component): # real signature unknown; restored from __doc__
        """ set_component(self, component:ECal.Component) """
        pass

    def set_instance(self, instance): # real signature unknown; restored from __doc__
        """ set_instance(self, instance:ECal.ComponentAlarmInstance) """
        pass

    def set_source_uid(self, source_uid): # real signature unknown; restored from __doc__
        """ set_source_uid(self, source_uid:str) """
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
        """ new(source_uid:str, component:ECal.Component, instance:ECal.ComponentAlarmInstance) -> ECal.ReminderData """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ReminderData), '__module__': 'gi.repository.ECal', '__gtype__': <GType EReminderData (94764814936592)>, '__dict__': <attribute '__dict__' of 'ReminderData' objects>, '__weakref__': <attribute '__weakref__' of 'ReminderData' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'get_component': gi.FunctionInfo(get_component), 'get_instance': gi.FunctionInfo(get_instance), 'get_source_uid': gi.FunctionInfo(get_source_uid), 'set_component': gi.FunctionInfo(set_component), 'set_instance': gi.FunctionInfo(set_instance), 'set_source_uid': gi.FunctionInfo(set_source_uid), 'free': gi.FunctionInfo(free), '__new__': <staticmethod object at 0x7fe5c99d9070>, '__init__': <function nothing at 0x7fe5cd0d7ee0>})"
    __gtype__ = None # (!) real value is '<GType EReminderData (94764814936592)>'
    __info__ = StructInfo(ReminderData)


