# encoding: utf-8
# module gi.repository.Vips
# from /usr/lib64/girepository-1.0/Vips-8.0.typelib
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
import gobject as __gobject


class ObjectClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ObjectClass()
    """
    def install_argument(self, pspec, flags, priority, offset): # real signature unknown; restored from __doc__
        """ install_argument(self, pspec:GObject.ParamSpec, flags:Vips.ArgumentFlags, priority:int, offset:int) """
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

    argument_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    argument_table_traverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    argument_table_traverse_gtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    build = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deprecated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dump = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    new_from_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nickname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    output_needs_arg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    output_to_arg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    postbuild = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    postclose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    preclose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rewind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sanity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    summary_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    to_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vips_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vips_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vips_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vips_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ObjectClass), '__module__': 'gi.repository.Vips', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ObjectClass' objects>, '__weakref__': <attribute '__weakref__' of 'ObjectClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f41868f1400>, 'build': <property object at 0x7f41868f14f0>, 'postbuild': <property object at 0x7f41868f15e0>, 'summary_class': <property object at 0x7f41868f16d0>, 'summary': <property object at 0x7f41868f17c0>, 'dump': <property object at 0x7f41868f18b0>, 'sanity': <property object at 0x7f41868f19a0>, 'rewind': <property object at 0x7f41868f1a90>, 'preclose': <property object at 0x7f41868f1b80>, 'close': <property object at 0x7f41868f1c70>, 'postclose': <property object at 0x7f41868f1d60>, 'new_from_string': <property object at 0x7f41868f1e50>, 'to_string': <property object at 0x7f41868f1f40>, 'output_needs_arg': <property object at 0x7f41868f20e0>, 'output_to_arg': <property object at 0x7f41868f21d0>, 'nickname': <property object at 0x7f41868f22c0>, 'description': <property object at 0x7f41868f23b0>, 'argument_table': <property object at 0x7f41868f24a0>, 'argument_table_traverse': <property object at 0x7f41868f25e0>, 'argument_table_traverse_gtype': <property object at 0x7f41868f2720>, 'deprecated': <property object at 0x7f41868f2810>, '_vips_reserved1': <property object at 0x7f41868f2900>, '_vips_reserved2': <property object at 0x7f41868f29f0>, '_vips_reserved3': <property object at 0x7f41868f2ae0>, '_vips_reserved4': <property object at 0x7f41868f2bd0>, 'install_argument': gi.FunctionInfo(install_argument)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ObjectClass)


