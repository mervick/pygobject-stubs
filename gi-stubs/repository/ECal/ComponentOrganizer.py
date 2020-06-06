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


class ComponentOrganizer(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> ECal.ComponentOrganizer
        new_from_property(property:ICalGLib.Property) -> ECal.ComponentOrganizer or None
        new_full(value:str=None, sentby:str=None, cn:str=None, language:str=None) -> ECal.ComponentOrganizer
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> ECal.ComponentOrganizer """
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

    def get_language(self): # real signature unknown; restored from __doc__
        """ get_language(self) -> str or None """
        return ""

    def get_parameter_bag(self): # real signature unknown; restored from __doc__
        """ get_parameter_bag(self) -> ECal.ComponentParameterBag """
        pass

    def get_sentby(self): # real signature unknown; restored from __doc__
        """ get_sentby(self) -> str or None """
        return ""

    def get_value(self): # real signature unknown; restored from __doc__
        """ get_value(self) -> str or None """
        return ""

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> ECal.ComponentOrganizer """
        pass

    def new_from_property(self, property): # real signature unknown; restored from __doc__
        """ new_from_property(property:ICalGLib.Property) -> ECal.ComponentOrganizer or None """
        pass

    def new_full(self, value=None, sentby=None, cn=None, language=None): # real signature unknown; restored from __doc__
        """ new_full(value:str=None, sentby:str=None, cn:str=None, language:str=None) -> ECal.ComponentOrganizer """
        pass

    def set_cn(self, cn=None): # real signature unknown; restored from __doc__
        """ set_cn(self, cn:str=None) """
        pass

    def set_from_property(self, property): # real signature unknown; restored from __doc__
        """ set_from_property(self, property:ICalGLib.Property) """
        pass

    def set_language(self, language=None): # real signature unknown; restored from __doc__
        """ set_language(self, language:str=None) """
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
        """ new() -> ECal.ComponentOrganizer """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ComponentOrganizer), '__module__': 'gi.repository.ECal', '__gtype__': <GType ECalComponentOrganizer (94764814891552)>, '__dict__': <attribute '__dict__' of 'ComponentOrganizer' objects>, '__weakref__': <attribute '__weakref__' of 'ComponentOrganizer' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_from_property': gi.FunctionInfo(new_from_property), 'new_full': gi.FunctionInfo(new_full), 'copy': gi.FunctionInfo(copy), 'fill_property': gi.FunctionInfo(fill_property), 'get_as_property': gi.FunctionInfo(get_as_property), 'get_cn': gi.FunctionInfo(get_cn), 'get_language': gi.FunctionInfo(get_language), 'get_parameter_bag': gi.FunctionInfo(get_parameter_bag), 'get_sentby': gi.FunctionInfo(get_sentby), 'get_value': gi.FunctionInfo(get_value), 'set_cn': gi.FunctionInfo(set_cn), 'set_from_property': gi.FunctionInfo(set_from_property), 'set_language': gi.FunctionInfo(set_language), 'set_sentby': gi.FunctionInfo(set_sentby), 'set_value': gi.FunctionInfo(set_value), '__new__': <staticmethod object at 0x7fe5cce05be0>, '__init__': <function nothing at 0x7fe5cd0d7ee0>})"
    __gtype__ = None # (!) real value is '<GType ECalComponentOrganizer (94764814891552)>'
    __info__ = StructInfo(ComponentOrganizer)


