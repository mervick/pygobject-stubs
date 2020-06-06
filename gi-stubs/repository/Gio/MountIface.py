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


class MountIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MountIface()
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

    can_eject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_unmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_with_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_with_operation_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_default_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_drive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sort_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_symbolic_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    guess_content_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    guess_content_type_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    guess_content_type_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pre_unmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remount_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmounted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_with_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_with_operation_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MountIface), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MountIface' objects>, '__weakref__': <attribute '__weakref__' of 'MountIface' objects>, '__doc__': None, 'g_iface': <property object at 0x7f4b8800ef90>, 'changed': <property object at 0x7f4b880110e0>, 'unmounted': <property object at 0x7f4b880111d0>, 'get_root': <property object at 0x7f4b880112c0>, 'get_name': <property object at 0x7f4b880113b0>, 'get_icon': <property object at 0x7f4b880114a0>, 'get_uuid': <property object at 0x7f4b88011590>, 'get_volume': <property object at 0x7f4b88011680>, 'get_drive': <property object at 0x7f4b88011770>, 'can_unmount': <property object at 0x7f4b88011860>, 'can_eject': <property object at 0x7f4b88011950>, 'unmount': <property object at 0x7f4b88011a40>, 'unmount_finish': <property object at 0x7f4b88011b30>, 'eject': <property object at 0x7f4b88011c20>, 'eject_finish': <property object at 0x7f4b88011d10>, 'remount': <property object at 0x7f4b88011e00>, 'remount_finish': <property object at 0x7f4b88011ef0>, 'guess_content_type': <property object at 0x7f4b88012090>, 'guess_content_type_finish': <property object at 0x7f4b88012180>, 'guess_content_type_sync': <property object at 0x7f4b88012270>, 'pre_unmount': <property object at 0x7f4b88012310>, 'unmount_with_operation': <property object at 0x7f4b88012450>, 'unmount_with_operation_finish': <property object at 0x7f4b88012540>, 'eject_with_operation': <property object at 0x7f4b88012630>, 'eject_with_operation_finish': <property object at 0x7f4b88012720>, 'get_default_location': <property object at 0x7f4b88012810>, 'get_sort_key': <property object at 0x7f4b880128b0>, 'get_symbolic_icon': <property object at 0x7f4b880129f0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MountIface)


