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


class ComponentDateTime(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(value:ICalGLib.Time, tzid:str=None) -> ECal.ComponentDateTime
        new_take(value:ICalGLib.Time, tzid:str=None) -> ECal.ComponentDateTime
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> ECal.ComponentDateTime """
        pass

    def get_tzid(self): # real signature unknown; restored from __doc__
        """ get_tzid(self) -> str or None """
        return ""

    def get_value(self): # real signature unknown; restored from __doc__
        """ get_value(self) -> ICalGLib.Time """
        pass

    def new(self, value, tzid=None): # real signature unknown; restored from __doc__
        """ new(value:ICalGLib.Time, tzid:str=None) -> ECal.ComponentDateTime """
        pass

    def new_take(self, value, tzid=None): # real signature unknown; restored from __doc__
        """ new_take(value:ICalGLib.Time, tzid:str=None) -> ECal.ComponentDateTime """
        pass

    def set(self, value, tzid=None): # real signature unknown; restored from __doc__
        """ set(self, value:ICalGLib.Time, tzid:str=None) """
        pass

    def set_tzid(self, tzid=None): # real signature unknown; restored from __doc__
        """ set_tzid(self, tzid:str=None) """
        pass

    def set_value(self, value): # real signature unknown; restored from __doc__
        """ set_value(self, value:ICalGLib.Time) """
        pass

    def take_tzid(self, tzid=None): # real signature unknown; restored from __doc__
        """ take_tzid(self, tzid:str=None) """
        pass

    def take_value(self, value): # real signature unknown; restored from __doc__
        """ take_value(self, value:ICalGLib.Time) """
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
        """ new(value:ICalGLib.Time, tzid:str=None) -> ECal.ComponentDateTime """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ComponentDateTime), '__module__': 'gi.repository.ECal', '__gtype__': <GType ECalComponentDateTime (94764814886144)>, '__dict__': <attribute '__dict__' of 'ComponentDateTime' objects>, '__weakref__': <attribute '__weakref__' of 'ComponentDateTime' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_take': gi.FunctionInfo(new_take), 'copy': gi.FunctionInfo(copy), 'get_tzid': gi.FunctionInfo(get_tzid), 'get_value': gi.FunctionInfo(get_value), 'set': gi.FunctionInfo(set), 'set_tzid': gi.FunctionInfo(set_tzid), 'set_value': gi.FunctionInfo(set_value), 'take_tzid': gi.FunctionInfo(take_tzid), 'take_value': gi.FunctionInfo(take_value), '__new__': <staticmethod object at 0x7fe5cce05a60>, '__init__': <function nothing at 0x7fe5cd0d7ee0>})"
    __gtype__ = None # (!) real value is '<GType ECalComponentDateTime (94764814886144)>'
    __info__ = StructInfo(ComponentDateTime)


