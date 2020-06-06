# encoding: utf-8
# module gi.repository.GstRtsp
# from /usr/lib64/girepository-1.0/GstRtsp-1.0.typelib
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


class RTSPWatch(__gi.Struct):
    # no doc
    def attach(self, context): # real signature unknown; restored from __doc__
        """ attach(self, context:GLib.MainContext) -> int """
        return 0

    def get_send_backlog(self): # real signature unknown; restored from __doc__
        """ get_send_backlog(self) -> bytes:int, messages:int """
        return b""

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def send_message(self, message): # real signature unknown; restored from __doc__
        """ send_message(self, message:GstRtsp.RTSPMessage) -> GstRtsp.RTSPResult, id:int """
        pass

    def send_messages(self, messages): # real signature unknown; restored from __doc__
        """ send_messages(self, messages:list) -> GstRtsp.RTSPResult, id:int """
        pass

    def set_flushing(self, flushing): # real signature unknown; restored from __doc__
        """ set_flushing(self, flushing:bool) """
        pass

    def set_send_backlog(self, bytes, messages): # real signature unknown; restored from __doc__
        """ set_send_backlog(self, bytes:int, messages:int) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def wait_backlog(self, timeout): # real signature unknown; restored from __doc__
        """ wait_backlog(self, timeout:GLib.TimeVal) -> GstRtsp.RTSPResult """
        pass

    def write_data(self, data): # real signature unknown; restored from __doc__
        """ write_data(self, data:list) -> GstRtsp.RTSPResult, id:int """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RTSPWatch), '__module__': 'gi.repository.GstRtsp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RTSPWatch' objects>, '__weakref__': <attribute '__weakref__' of 'RTSPWatch' objects>, '__doc__': None, 'attach': gi.FunctionInfo(attach), 'get_send_backlog': gi.FunctionInfo(get_send_backlog), 'reset': gi.FunctionInfo(reset), 'send_message': gi.FunctionInfo(send_message), 'send_messages': gi.FunctionInfo(send_messages), 'set_flushing': gi.FunctionInfo(set_flushing), 'set_send_backlog': gi.FunctionInfo(set_send_backlog), 'unref': gi.FunctionInfo(unref), 'wait_backlog': gi.FunctionInfo(wait_backlog), 'write_data': gi.FunctionInfo(write_data)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RTSPWatch)


