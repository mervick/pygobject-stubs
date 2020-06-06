# encoding: utf-8
# module gi.repository.GstBase
# from /usr/lib64/girepository-1.0/GstBase-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gobject as __gobject


class BaseTransformClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BaseTransformClass()
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

    accept_caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    before_transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    decide_allocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fixate_caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generate_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_unit_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    passthrough_on_same_caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prepare_output_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    propose_allocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sink_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    submit_input_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_ip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_ip_on_passthrough = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BaseTransformClass), '__module__': 'gi.repository.GstBase', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BaseTransformClass' objects>, '__weakref__': <attribute '__weakref__' of 'BaseTransformClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f9fb7bc8270>, 'passthrough_on_same_caps': <property object at 0x7f9fb7bc83b0>, 'transform_ip_on_passthrough': <property object at 0x7f9fb7bc84f0>, 'transform_caps': <property object at 0x7f9fb7bc85e0>, 'fixate_caps': <property object at 0x7f9fb7bc86d0>, 'accept_caps': <property object at 0x7f9fb7bc87c0>, 'set_caps': <property object at 0x7f9fb7bc88b0>, 'query': <property object at 0x7f9fb7bc89a0>, 'decide_allocation': <property object at 0x7f9fb7bc8ae0>, 'filter_meta': <property object at 0x7f9fb7bc8b80>, 'propose_allocation': <property object at 0x7f9fb7bc8cc0>, 'transform_size': <property object at 0x7f9fb7bc8d60>, 'get_unit_size': <property object at 0x7f9fb7bc8e50>, 'start': <property object at 0x7f9fb7bc8f40>, 'stop': <property object at 0x7f9fb7bca090>, 'sink_event': <property object at 0x7f9fb7bca180>, 'src_event': <property object at 0x7f9fb7bca270>, 'prepare_output_buffer': <property object at 0x7f9fb7bca3b0>, 'copy_metadata': <property object at 0x7f9fb7bca4a0>, 'transform_meta': <property object at 0x7f9fb7bca590>, 'before_transform': <property object at 0x7f9fb7bca6d0>, 'transform': <property object at 0x7f9fb7bca7c0>, 'transform_ip': <property object at 0x7f9fb7bca8b0>, 'submit_input_buffer': <property object at 0x7f9fb7bca9f0>, 'generate_output': <property object at 0x7f9fb7bcaae0>, '_gst_reserved': <property object at 0x7f9fb7bcabd0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BaseTransformClass)


