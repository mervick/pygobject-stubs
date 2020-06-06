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


class ComponentAlarms(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(comp) -> ECal.ComponentAlarms
    """
    def add_instance(self, instance): # real signature unknown; restored from __doc__
        """ add_instance(self, instance:ECal.ComponentAlarmInstance) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> ECal.ComponentAlarms """
        pass

    def get_component(self): # real signature unknown; restored from __doc__
        """ get_component(self) """
        pass

    def get_instances(self): # real signature unknown; restored from __doc__
        """ get_instances(self) -> list or None """
        return []

    def new(self, comp): # real signature unknown; restored from __doc__
        """ new(comp) -> ECal.ComponentAlarms """
        pass

    def remove_instance(self, instance): # real signature unknown; restored from __doc__
        """ remove_instance(self, instance:ECal.ComponentAlarmInstance) -> bool """
        return False

    def set_instances(self, instances=None): # real signature unknown; restored from __doc__
        """ set_instances(self, instances:list=None) """
        pass

    def take_instance(self, instance): # real signature unknown; restored from __doc__
        """ take_instance(self, instance:ECal.ComponentAlarmInstance) """
        pass

    def take_instances(self, instances=None): # real signature unknown; restored from __doc__
        """ take_instances(self, instances:list=None) """
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
        """ new(comp) -> ECal.ComponentAlarms """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ComponentAlarms), '__module__': 'gi.repository.ECal', '__gtype__': <GType ECalComponentAlarms (94764814869936)>, '__dict__': <attribute '__dict__' of 'ComponentAlarms' objects>, '__weakref__': <attribute '__weakref__' of 'ComponentAlarms' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'add_instance': gi.FunctionInfo(add_instance), 'copy': gi.FunctionInfo(copy), 'get_component': gi.FunctionInfo(get_component), 'get_instances': gi.FunctionInfo(get_instances), 'remove_instance': gi.FunctionInfo(remove_instance), 'set_instances': gi.FunctionInfo(set_instances), 'take_instance': gi.FunctionInfo(take_instance), 'take_instances': gi.FunctionInfo(take_instances), '__new__': <staticmethod object at 0x7fe5cce05850>, '__init__': <function nothing at 0x7fe5cd0d7ee0>})"
    __gtype__ = None # (!) real value is '<GType ECalComponentAlarms (94764814869936)>'
    __info__ = StructInfo(ComponentAlarms)


