# encoding: utf-8
# module gi.repository.Gio
# from /usr/lib64/girepository-1.0/Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class UnixMountPoint(__gi.Boxed):
    # no doc
    def compare(self, mount2): # real signature unknown; restored from __doc__
        """ compare(self, mount2:Gio.UnixMountPoint) -> int """
        return 0

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gio.UnixMountPoint """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_device_path(self): # real signature unknown; restored from __doc__
        """ get_device_path(self) -> str """
        return ""

    def get_fs_type(self): # real signature unknown; restored from __doc__
        """ get_fs_type(self) -> str """
        return ""

    def get_mount_path(self): # real signature unknown; restored from __doc__
        """ get_mount_path(self) -> str """
        return ""

    def get_options(self): # real signature unknown; restored from __doc__
        """ get_options(self) -> str """
        return ""

    def guess_can_eject(self): # real signature unknown; restored from __doc__
        """ guess_can_eject(self) -> bool """
        return False

    def guess_icon(self): # real signature unknown; restored from __doc__
        """ guess_icon(self) -> Gio.Icon """
        pass

    def guess_name(self): # real signature unknown; restored from __doc__
        """ guess_name(self) -> str """
        return ""

    def guess_symbolic_icon(self): # real signature unknown; restored from __doc__
        """ guess_symbolic_icon(self) -> Gio.Icon """
        pass

    def is_loopback(self): # real signature unknown; restored from __doc__
        """ is_loopback(self) -> bool """
        return False

    def is_readonly(self): # real signature unknown; restored from __doc__
        """ is_readonly(self) -> bool """
        return False

    def is_user_mountable(self): # real signature unknown; restored from __doc__
        """ is_user_mountable(self) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(UnixMountPoint), '__module__': 'gi.repository.Gio', '__gtype__': <GType GUnixMountPoint (94125582914240)>, '__dict__': <attribute '__dict__' of 'UnixMountPoint' objects>, '__weakref__': <attribute '__weakref__' of 'UnixMountPoint' objects>, '__doc__': None, 'compare': gi.FunctionInfo(compare), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_device_path': gi.FunctionInfo(get_device_path), 'get_fs_type': gi.FunctionInfo(get_fs_type), 'get_mount_path': gi.FunctionInfo(get_mount_path), 'get_options': gi.FunctionInfo(get_options), 'guess_can_eject': gi.FunctionInfo(guess_can_eject), 'guess_icon': gi.FunctionInfo(guess_icon), 'guess_name': gi.FunctionInfo(guess_name), 'guess_symbolic_icon': gi.FunctionInfo(guess_symbolic_icon), 'is_loopback': gi.FunctionInfo(is_loopback), 'is_readonly': gi.FunctionInfo(is_readonly), 'is_user_mountable': gi.FunctionInfo(is_user_mountable)})"
    __gtype__ = None # (!) real value is '<GType GUnixMountPoint (94125582914240)>'
    __info__ = StructInfo(UnixMountPoint)


