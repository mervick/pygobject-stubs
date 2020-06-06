# encoding: utf-8
# module gi.repository.ModemManager
# from /usr/lib64/girepository-1.0/ModemManager-1.0.typelib
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


class GdbusModemIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GdbusModemIface()
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

    get_access_technologies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_bearers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_carrier_configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_carrier_configuration_revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_current_bands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_current_capabilities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_current_modes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_device_identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_drivers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_equipment_identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_hardware_revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_manufacturer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_max_active_bearers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_max_bearers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_own_numbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_plugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_ports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_power_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_primary_port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_signal_quality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_state_failed_reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_supported_bands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_supported_capabilities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_supported_ip_families = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_supported_modes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_unlock_required = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_unlock_retries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_create_bearer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_delete_bearer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_enable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_factory_reset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_list_bearers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_reset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_current_bands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_current_capabilities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_current_modes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_power_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GdbusModemIface), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GdbusModemIface' objects>, '__weakref__': <attribute '__weakref__' of 'GdbusModemIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f69438e1d10>, 'handle_command': <property object at 0x7f69438e1e00>, 'handle_create_bearer': <property object at 0x7f69438e1f40>, 'handle_delete_bearer': <property object at 0x7f69438e60e0>, 'handle_enable': <property object at 0x7f69438e61d0>, 'handle_factory_reset': <property object at 0x7f69438e6310>, 'handle_list_bearers': <property object at 0x7f69438e6400>, 'handle_reset': <property object at 0x7f69438e64f0>, 'handle_set_current_bands': <property object at 0x7f69438e6630>, 'handle_set_current_capabilities': <property object at 0x7f69438e6770>, 'handle_set_current_modes': <property object at 0x7f69438e68b0>, 'handle_set_power_state': <property object at 0x7f69438e69f0>, 'get_access_technologies': <property object at 0x7f69438e6b30>, 'get_bearers': <property object at 0x7f69438e6c20>, 'get_carrier_configuration': <property object at 0x7f69438e6d60>, 'get_carrier_configuration_revision': <property object at 0x7f69438e6e50>, 'get_current_bands': <property object at 0x7f69438e6f90>, 'get_current_capabilities': <property object at 0x7f69438e7130>, 'get_current_modes': <property object at 0x7f69438e7270>, 'get_device': <property object at 0x7f69438e7360>, 'get_device_identifier': <property object at 0x7f69438e74a0>, 'get_drivers': <property object at 0x7f69438e7590>, 'get_equipment_identifier': <property object at 0x7f69438e76d0>, 'get_hardware_revision': <property object at 0x7f69438e7810>, 'get_manufacturer': <property object at 0x7f69438e7950>, 'get_max_active_bearers': <property object at 0x7f69438e7a90>, 'get_max_bearers': <property object at 0x7f69438e7b80>, 'get_model': <property object at 0x7f69438e7c70>, 'get_own_numbers': <property object at 0x7f69438e7d60>, 'get_plugin': <property object at 0x7f69438e7e50>, 'get_ports': <property object at 0x7f69438e7f40>, 'get_power_state': <property object at 0x7f69438e8090>, 'get_primary_port': <property object at 0x7f69438e81d0>, 'get_revision': <property object at 0x7f69438e82c0>, 'get_signal_quality': <property object at 0x7f69438e8400>, 'get_sim': <property object at 0x7f69438e84a0>, 'get_state': <property object at 0x7f69438e8590>, 'get_state_failed_reason': <property object at 0x7f69438e86d0>, 'get_supported_bands': <property object at 0x7f69438e8810>, 'get_supported_capabilities': <property object at 0x7f69438e8950>, 'get_supported_ip_families': <property object at 0x7f69438e8a90>, 'get_supported_modes': <property object at 0x7f69438e8bd0>, 'get_unlock_required': <property object at 0x7f69438e8d10>, 'get_unlock_retries': <property object at 0x7f69438e8e50>, 'state_changed': <property object at 0x7f69438e8f40>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GdbusModemIface)


