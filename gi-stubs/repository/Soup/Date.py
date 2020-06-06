# encoding: utf-8
# module gi.repository.Soup
# from /usr/lib64/girepository-1.0/Soup-2.4.typelib
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


class Date(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Date()
        new(year:int, month:int, day:int, hour:int, minute:int, second:int) -> Soup.Date
        new_from_now(offset_seconds:int) -> Soup.Date
        new_from_string(date_string:str) -> Soup.Date or None
        new_from_time_t(when:int) -> Soup.Date
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Soup.Date """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_day(self): # real signature unknown; restored from __doc__
        """ get_day(self) -> int """
        return 0

    def get_hour(self): # real signature unknown; restored from __doc__
        """ get_hour(self) -> int """
        return 0

    def get_minute(self): # real signature unknown; restored from __doc__
        """ get_minute(self) -> int """
        return 0

    def get_month(self): # real signature unknown; restored from __doc__
        """ get_month(self) -> int """
        return 0

    def get_offset(self): # real signature unknown; restored from __doc__
        """ get_offset(self) -> int """
        return 0

    def get_second(self): # real signature unknown; restored from __doc__
        """ get_second(self) -> int """
        return 0

    def get_utc(self): # real signature unknown; restored from __doc__
        """ get_utc(self) -> int """
        return 0

    def get_year(self): # real signature unknown; restored from __doc__
        """ get_year(self) -> int """
        return 0

    def is_past(self): # real signature unknown; restored from __doc__
        """ is_past(self) -> bool """
        return False

    def new(self, year, month, day, hour, minute, second): # real signature unknown; restored from __doc__
        """ new(year:int, month:int, day:int, hour:int, minute:int, second:int) -> Soup.Date """
        pass

    def new_from_now(self, offset_seconds): # real signature unknown; restored from __doc__
        """ new_from_now(offset_seconds:int) -> Soup.Date """
        pass

    def new_from_string(self, date_string): # real signature unknown; restored from __doc__
        """ new_from_string(date_string:str) -> Soup.Date or None """
        pass

    def new_from_time_t(self, when): # real signature unknown; restored from __doc__
        """ new_from_time_t(when:int) -> Soup.Date """
        pass

    def to_string(self, format): # real signature unknown; restored from __doc__
        """ to_string(self, format:Soup.DateFormat) -> str """
        return ""

    def to_timeval(self): # real signature unknown; restored from __doc__
        """ to_timeval(self) -> time:GLib.TimeVal """
        pass

    def to_time_t(self): # real signature unknown; restored from __doc__
        """ to_time_t(self) -> int """
        return 0

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

    def __init__(self): # real signature unknown; restored from __doc__
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

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    utc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Date), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupDate (94750594694032)>, '__dict__': <attribute '__dict__' of 'Date' objects>, '__weakref__': <attribute '__weakref__' of 'Date' objects>, '__doc__': None, 'year': <property object at 0x7f8e48617ef0>, 'month': <property object at 0x7f8e47ed1040>, 'day': <property object at 0x7f8e47ed1130>, 'hour': <property object at 0x7f8e47ed1220>, 'minute': <property object at 0x7f8e47ed1310>, 'second': <property object at 0x7f8e47ed1400>, 'utc': <property object at 0x7f8e47ed14f0>, 'offset': <property object at 0x7f8e47ed15e0>, 'new': gi.FunctionInfo(new), 'new_from_now': gi.FunctionInfo(new_from_now), 'new_from_string': gi.FunctionInfo(new_from_string), 'new_from_time_t': gi.FunctionInfo(new_from_time_t), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_day': gi.FunctionInfo(get_day), 'get_hour': gi.FunctionInfo(get_hour), 'get_minute': gi.FunctionInfo(get_minute), 'get_month': gi.FunctionInfo(get_month), 'get_offset': gi.FunctionInfo(get_offset), 'get_second': gi.FunctionInfo(get_second), 'get_utc': gi.FunctionInfo(get_utc), 'get_year': gi.FunctionInfo(get_year), 'is_past': gi.FunctionInfo(is_past), 'to_string': gi.FunctionInfo(to_string), 'to_time_t': gi.FunctionInfo(to_time_t), 'to_timeval': gi.FunctionInfo(to_timeval)})"
    __gtype__ = None # (!) real value is '<GType SoupDate (94750594694032)>'
    __info__ = StructInfo(Date)


