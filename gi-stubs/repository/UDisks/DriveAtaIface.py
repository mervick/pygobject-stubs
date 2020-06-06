# encoding: utf-8
# module gi.repository.UDisks
# from /usr/lib64/girepository-1.0/UDisks-2.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class DriveAtaIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DriveAtaIface()
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

    get_aam_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_aam_supported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_aam_vendor_recommended_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_apm_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_apm_supported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_pm_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_pm_supported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_read_lookahead_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_read_lookahead_supported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_security_enhanced_erase_unit_minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_security_erase_unit_minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_security_frozen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_failing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_num_attributes_failed_in_the_past = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_num_attributes_failing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_num_bad_sectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_power_on_seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_selftest_percent_remaining = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_selftest_status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_supported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_temperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smart_updated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_write_cache_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_write_cache_supported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_pm_get_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_pm_standby = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_pm_wakeup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_security_erase_unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_smart_get_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_smart_selftest_abort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_smart_selftest_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_smart_set_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_smart_update = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DriveAtaIface), '__module__': 'gi.repository.UDisks', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DriveAtaIface' objects>, '__weakref__': <attribute '__weakref__' of 'DriveAtaIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f13a8167040>, 'handle_pm_get_state': <property object at 0x7f13a8167180>, 'handle_pm_standby': <property object at 0x7f13a81672c0>, 'handle_pm_wakeup': <property object at 0x7f13a8167400>, 'handle_security_erase_unit': <property object at 0x7f13a8167540>, 'handle_smart_get_attributes': <property object at 0x7f13a8167680>, 'handle_smart_selftest_abort': <property object at 0x7f13a81677c0>, 'handle_smart_selftest_start': <property object at 0x7f13a8167900>, 'handle_smart_update': <property object at 0x7f13a8167a40>, 'get_aam_enabled': <property object at 0x7f13a8167b30>, 'get_aam_supported': <property object at 0x7f13a8167c70>, 'get_aam_vendor_recommended_value': <property object at 0x7f13a8167d60>, 'get_apm_enabled': <property object at 0x7f13a8167e50>, 'get_apm_supported': <property object at 0x7f13a8167f90>, 'get_pm_enabled': <property object at 0x7f13a81690e0>, 'get_pm_supported': <property object at 0x7f13a8169220>, 'get_security_enhanced_erase_unit_minutes': <property object at 0x7f13a8169310>, 'get_security_erase_unit_minutes': <property object at 0x7f13a8169450>, 'get_security_frozen': <property object at 0x7f13a8169590>, 'get_smart_enabled': <property object at 0x7f13a81696d0>, 'get_smart_failing': <property object at 0x7f13a8169810>, 'get_smart_num_attributes_failed_in_the_past': <property object at 0x7f13a8169900>, 'get_smart_num_attributes_failing': <property object at 0x7f13a81699f0>, 'get_smart_num_bad_sectors': <property object at 0x7f13a8169b30>, 'get_smart_power_on_seconds': <property object at 0x7f13a8169c70>, 'get_smart_selftest_percent_remaining': <property object at 0x7f13a8169d60>, 'get_smart_selftest_status': <property object at 0x7f13a8169ea0>, 'get_smart_supported': <property object at 0x7f13a816a040>, 'get_smart_temperature': <property object at 0x7f13a816a180>, 'get_smart_updated': <property object at 0x7f13a816a2c0>, 'handle_smart_set_enabled': <property object at 0x7f13a816a400>, 'get_write_cache_enabled': <property object at 0x7f13a816a540>, 'get_write_cache_supported': <property object at 0x7f13a816a680>, 'get_read_lookahead_enabled': <property object at 0x7f13a816a7c0>, 'get_read_lookahead_supported': <property object at 0x7f13a816a900>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DriveAtaIface)


