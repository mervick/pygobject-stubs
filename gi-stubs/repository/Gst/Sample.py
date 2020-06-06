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


class Sample(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(buffer:Gst.Buffer=None, caps:Gst.Caps=None, segment:Gst.Segment=None, info:Gst.Structure=None) -> Gst.Sample
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_buffer(self): # real signature unknown; restored from __doc__
        """ get_buffer(self) -> Gst.Buffer or None """
        pass

    def get_buffer_list(self): # real signature unknown; restored from __doc__
        """ get_buffer_list(self) -> Gst.BufferList or None """
        pass

    def get_caps(self): # real signature unknown; restored from __doc__
        """ get_caps(self) -> Gst.Caps or None """
        pass

    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info(self) -> Gst.Structure or None """
        pass

    def get_segment(self): # real signature unknown; restored from __doc__
        """ get_segment(self) -> Gst.Segment """
        pass

    def new(self, buffer=None, caps=None, segment=None, info=None): # real signature unknown; restored from __doc__
        """ new(buffer:Gst.Buffer=None, caps:Gst.Caps=None, segment:Gst.Segment=None, info:Gst.Structure=None) -> Gst.Sample """
        pass

    def set_buffer(self, buffer): # real signature unknown; restored from __doc__
        """ set_buffer(self, buffer:Gst.Buffer) """
        pass

    def set_buffer_list(self, buffer_list): # real signature unknown; restored from __doc__
        """ set_buffer_list(self, buffer_list:Gst.BufferList) """
        pass

    def set_caps(self, caps): # real signature unknown; restored from __doc__
        """ set_caps(self, caps:Gst.Caps) """
        pass

    def set_info(self, info): # real signature unknown; restored from __doc__
        """ set_info(self, info:Gst.Structure) -> bool """
        return False

    def set_segment(self, segment): # real signature unknown; restored from __doc__
        """ set_segment(self, segment:Gst.Segment) """
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
        """ new(buffer:Gst.Buffer=None, caps:Gst.Caps=None, segment:Gst.Segment=None, info:Gst.Structure=None) -> Gst.Sample """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Sample), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstSample (94058977932000)>, '__dict__': <attribute '__dict__' of 'Sample' objects>, '__weakref__': <attribute '__weakref__' of 'Sample' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'get_buffer': gi.FunctionInfo(get_buffer), 'get_buffer_list': gi.FunctionInfo(get_buffer_list), 'get_caps': gi.FunctionInfo(get_caps), 'get_info': gi.FunctionInfo(get_info), 'get_segment': gi.FunctionInfo(get_segment), 'set_buffer': gi.FunctionInfo(set_buffer), 'set_buffer_list': gi.FunctionInfo(set_buffer_list), 'set_caps': gi.FunctionInfo(set_caps), 'set_info': gi.FunctionInfo(set_info), 'set_segment': gi.FunctionInfo(set_segment), '__new__': <staticmethod object at 0x7f4260507d90>, '__init__': <function nothing at 0x7f4260937ee0>})"
    __gtype__ = None # (!) real value is '<GType GstSample (94058977932000)>'
    __info__ = StructInfo(Sample)


