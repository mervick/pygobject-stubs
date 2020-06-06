# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class DateTime(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(tzoffset:float, year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> Gst.DateTime
        new_from_g_date_time(dt:GLib.DateTime) -> Gst.DateTime or None
        new_from_iso8601_string(string:str) -> Gst.DateTime or None
        new_from_unix_epoch_local_time(secs:int) -> Gst.DateTime
        new_from_unix_epoch_utc(secs:int) -> Gst.DateTime
        new_local_time(year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> Gst.DateTime
        new_now_local_time() -> Gst.DateTime
        new_now_utc() -> Gst.DateTime
        new_y(year:int) -> Gst.DateTime
        new_ym(year:int, month:int) -> Gst.DateTime
        new_ymd(year:int, month:int, day:int) -> Gst.DateTime
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_day(self): # real signature unknown; restored from __doc__
        """ get_day(self) -> int """
        return 0

    def get_hour(self): # real signature unknown; restored from __doc__
        """ get_hour(self) -> int """
        return 0

    def get_microsecond(self): # real signature unknown; restored from __doc__
        """ get_microsecond(self) -> int """
        return 0

    def get_minute(self): # real signature unknown; restored from __doc__
        """ get_minute(self) -> int """
        return 0

    def get_month(self): # real signature unknown; restored from __doc__
        """ get_month(self) -> int """
        return 0

    def get_second(self): # real signature unknown; restored from __doc__
        """ get_second(self) -> int """
        return 0

    def get_time_zone_offset(self): # real signature unknown; restored from __doc__
        """ get_time_zone_offset(self) -> float """
        return 0.0

    def get_year(self): # real signature unknown; restored from __doc__
        """ get_year(self) -> int """
        return 0

    def has_day(self): # real signature unknown; restored from __doc__
        """ has_day(self) -> bool """
        return False

    def has_month(self): # real signature unknown; restored from __doc__
        """ has_month(self) -> bool """
        return False

    def has_second(self): # real signature unknown; restored from __doc__
        """ has_second(self) -> bool """
        return False

    def has_time(self): # real signature unknown; restored from __doc__
        """ has_time(self) -> bool """
        return False

    def has_year(self): # real signature unknown; restored from __doc__
        """ has_year(self) -> bool """
        return False

    def new(self, tzoffset, year, month, day, hour, minute, seconds): # real signature unknown; restored from __doc__
        """ new(tzoffset:float, year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> Gst.DateTime """
        pass

    def new_from_g_date_time(self, dt): # real signature unknown; restored from __doc__
        """ new_from_g_date_time(dt:GLib.DateTime) -> Gst.DateTime or None """
        pass

    def new_from_iso8601_string(self, string): # real signature unknown; restored from __doc__
        """ new_from_iso8601_string(string:str) -> Gst.DateTime or None """
        pass

    def new_from_unix_epoch_local_time(self, secs): # real signature unknown; restored from __doc__
        """ new_from_unix_epoch_local_time(secs:int) -> Gst.DateTime """
        pass

    def new_from_unix_epoch_utc(self, secs): # real signature unknown; restored from __doc__
        """ new_from_unix_epoch_utc(secs:int) -> Gst.DateTime """
        pass

    def new_local_time(self, year, month, day, hour, minute, seconds): # real signature unknown; restored from __doc__
        """ new_local_time(year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> Gst.DateTime """
        pass

    def new_now_local_time(self): # real signature unknown; restored from __doc__
        """ new_now_local_time() -> Gst.DateTime """
        pass

    def new_now_utc(self): # real signature unknown; restored from __doc__
        """ new_now_utc() -> Gst.DateTime """
        pass

    def new_y(self, year): # real signature unknown; restored from __doc__
        """ new_y(year:int) -> Gst.DateTime """
        pass

    def new_ym(self, year, month): # real signature unknown; restored from __doc__
        """ new_ym(year:int, month:int) -> Gst.DateTime """
        pass

    def new_ymd(self, year, month, day): # real signature unknown; restored from __doc__
        """ new_ymd(year:int, month:int, day:int) -> Gst.DateTime """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gst.DateTime """
        pass

    def to_g_date_time(self): # real signature unknown; restored from __doc__
        """ to_g_date_time(self) -> GLib.DateTime or None """
        pass

    def to_iso8601_string(self): # real signature unknown; restored from __doc__
        """ to_iso8601_string(self) -> str or None """
        return ""

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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
        """ new(tzoffset:float, year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> Gst.DateTime """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DateTime), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstDateTime (94058977208256)>, '__dict__': <attribute '__dict__' of 'DateTime' objects>, '__weakref__': <attribute '__weakref__' of 'DateTime' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_from_g_date_time': gi.FunctionInfo(new_from_g_date_time), 'new_from_iso8601_string': gi.FunctionInfo(new_from_iso8601_string), 'new_from_unix_epoch_local_time': gi.FunctionInfo(new_from_unix_epoch_local_time), 'new_from_unix_epoch_utc': gi.FunctionInfo(new_from_unix_epoch_utc), 'new_local_time': gi.FunctionInfo(new_local_time), 'new_now_local_time': gi.FunctionInfo(new_now_local_time), 'new_now_utc': gi.FunctionInfo(new_now_utc), 'new_y': gi.FunctionInfo(new_y), 'new_ym': gi.FunctionInfo(new_ym), 'new_ymd': gi.FunctionInfo(new_ymd), 'get_day': gi.FunctionInfo(get_day), 'get_hour': gi.FunctionInfo(get_hour), 'get_microsecond': gi.FunctionInfo(get_microsecond), 'get_minute': gi.FunctionInfo(get_minute), 'get_month': gi.FunctionInfo(get_month), 'get_second': gi.FunctionInfo(get_second), 'get_time_zone_offset': gi.FunctionInfo(get_time_zone_offset), 'get_year': gi.FunctionInfo(get_year), 'has_day': gi.FunctionInfo(has_day), 'has_month': gi.FunctionInfo(has_month), 'has_second': gi.FunctionInfo(has_second), 'has_time': gi.FunctionInfo(has_time), 'has_year': gi.FunctionInfo(has_year), 'ref': gi.FunctionInfo(ref), 'to_g_date_time': gi.FunctionInfo(to_g_date_time), 'to_iso8601_string': gi.FunctionInfo(to_iso8601_string), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod object at 0x7f426072e160>, '__init__': <function nothing at 0x7f4260937ee0>})"
    __gtype__ = None # (!) real value is '<GType GstDateTime (94058977208256)>'
    __info__ = StructInfo(DateTime)


