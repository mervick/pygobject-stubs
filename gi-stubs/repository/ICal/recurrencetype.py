# encoding: utf-8
# module gi.repository.ICal
# from /usr/lib64/girepository-1.0/ICal-3.0.typelib
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
import gobject as __gobject


class recurrencetype(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        recurrencetype()
    """
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

    by_day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    by_hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    by_minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    by_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    by_month_day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    by_second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    by_set_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    by_week_no = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    by_year_day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rscale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    until = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    week_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(recurrencetype), '__module__': 'gi.repository.ICal', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'recurrencetype' objects>, '__weakref__': <attribute '__weakref__' of 'recurrencetype' objects>, '__doc__': None, 'freq': <property object at 0x7f3849ae95e0>, 'until': <property object at 0x7f3849ae96d0>, 'count': <property object at 0x7f3849ae97c0>, 'interval': <property object at 0x7f3849ae98b0>, 'week_start': <property object at 0x7f3849ae99a0>, 'by_second': <property object at 0x7f3849ae9a90>, 'by_minute': <property object at 0x7f3849ae9b80>, 'by_hour': <property object at 0x7f3849ae9c70>, 'by_day': <property object at 0x7f3849ae9d60>, 'by_month_day': <property object at 0x7f3849ae9e50>, 'by_year_day': <property object at 0x7f3849ae9f40>, 'by_week_no': <property object at 0x7f3849aea090>, 'by_month': <property object at 0x7f3849aea180>, 'by_set_pos': <property object at 0x7f3849aea270>, 'rscale': <property object at 0x7f3849aea360>, 'skip': <property object at 0x7f3849aea450>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(recurrencetype)


