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


class Poll(__gi.Struct):
    # no doc
    def add_fd(self, fd): # real signature unknown; restored from __doc__
        """ add_fd(self, fd:Gst.PollFD) -> bool """
        return False

    def fd_can_read(self, fd): # real signature unknown; restored from __doc__
        """ fd_can_read(self, fd:Gst.PollFD) -> bool """
        return False

    def fd_can_write(self, fd): # real signature unknown; restored from __doc__
        """ fd_can_write(self, fd:Gst.PollFD) -> bool """
        return False

    def fd_ctl_pri(self, fd, active): # real signature unknown; restored from __doc__
        """ fd_ctl_pri(self, fd:Gst.PollFD, active:bool) -> bool """
        return False

    def fd_ctl_read(self, fd, active): # real signature unknown; restored from __doc__
        """ fd_ctl_read(self, fd:Gst.PollFD, active:bool) -> bool """
        return False

    def fd_ctl_write(self, fd, active): # real signature unknown; restored from __doc__
        """ fd_ctl_write(self, fd:Gst.PollFD, active:bool) -> bool """
        return False

    def fd_has_closed(self, fd): # real signature unknown; restored from __doc__
        """ fd_has_closed(self, fd:Gst.PollFD) -> bool """
        return False

    def fd_has_error(self, fd): # real signature unknown; restored from __doc__
        """ fd_has_error(self, fd:Gst.PollFD) -> bool """
        return False

    def fd_has_pri(self, fd): # real signature unknown; restored from __doc__
        """ fd_has_pri(self, fd:Gst.PollFD) -> bool """
        return False

    def fd_ignored(self, fd): # real signature unknown; restored from __doc__
        """ fd_ignored(self, fd:Gst.PollFD) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_read_gpollfd(self, fd): # real signature unknown; restored from __doc__
        """ get_read_gpollfd(self, fd:GLib.PollFD) """
        pass

    def read_control(self): # real signature unknown; restored from __doc__
        """ read_control(self) -> bool """
        return False

    def remove_fd(self, fd): # real signature unknown; restored from __doc__
        """ remove_fd(self, fd:Gst.PollFD) -> bool """
        return False

    def restart(self): # real signature unknown; restored from __doc__
        """ restart(self) """
        pass

    def set_controllable(self, controllable): # real signature unknown; restored from __doc__
        """ set_controllable(self, controllable:bool) -> bool """
        return False

    def set_flushing(self, flushing): # real signature unknown; restored from __doc__
        """ set_flushing(self, flushing:bool) """
        pass

    def wait(self, timeout): # real signature unknown; restored from __doc__
        """ wait(self, timeout:int) -> int """
        return 0

    def write_control(self): # real signature unknown; restored from __doc__
        """ write_control(self) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Poll), '__module__': 'gi.repository.Gst', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Poll' objects>, '__weakref__': <attribute '__weakref__' of 'Poll' objects>, '__doc__': None, 'add_fd': gi.FunctionInfo(add_fd), 'fd_can_read': gi.FunctionInfo(fd_can_read), 'fd_can_write': gi.FunctionInfo(fd_can_write), 'fd_ctl_pri': gi.FunctionInfo(fd_ctl_pri), 'fd_ctl_read': gi.FunctionInfo(fd_ctl_read), 'fd_ctl_write': gi.FunctionInfo(fd_ctl_write), 'fd_has_closed': gi.FunctionInfo(fd_has_closed), 'fd_has_error': gi.FunctionInfo(fd_has_error), 'fd_has_pri': gi.FunctionInfo(fd_has_pri), 'fd_ignored': gi.FunctionInfo(fd_ignored), 'free': gi.FunctionInfo(free), 'get_read_gpollfd': gi.FunctionInfo(get_read_gpollfd), 'read_control': gi.FunctionInfo(read_control), 'remove_fd': gi.FunctionInfo(remove_fd), 'restart': gi.FunctionInfo(restart), 'set_controllable': gi.FunctionInfo(set_controllable), 'set_flushing': gi.FunctionInfo(set_flushing), 'wait': gi.FunctionInfo(wait), 'write_control': gi.FunctionInfo(write_control)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Poll)


