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


class GdbusModem3gppIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GdbusModem3gppIface()
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

    get_enabled_facility_locks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_eps_ue_mode_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_imei = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_initial_eps_bearer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_initial_eps_bearer_settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_operator_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_operator_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_pco = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_registration_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_subscription_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_register = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_scan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_eps_ue_mode_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_initial_eps_bearer_settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GdbusModem3gppIface), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GdbusModem3gppIface' objects>, '__weakref__': <attribute '__weakref__' of 'GdbusModem3gppIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f69438d3c70>, 'handle_register': <property object at 0x7f69438d3d60>, 'handle_scan': <property object at 0x7f69438d3e50>, 'handle_set_eps_ue_mode_operation': <property object at 0x7f69438d3f40>, 'handle_set_initial_eps_bearer_settings': <property object at 0x7f69438d5090>, 'get_enabled_facility_locks': <property object at 0x7f69438d51d0>, 'get_eps_ue_mode_operation': <property object at 0x7f69438d5310>, 'get_imei': <property object at 0x7f69438d5400>, 'get_initial_eps_bearer': <property object at 0x7f69438d5540>, 'get_initial_eps_bearer_settings': <property object at 0x7f69438d5680>, 'get_operator_code': <property object at 0x7f69438d57c0>, 'get_operator_name': <property object at 0x7f69438d5900>, 'get_pco': <property object at 0x7f69438d59f0>, 'get_registration_state': <property object at 0x7f69438d5b30>, 'get_subscription_state': <property object at 0x7f69438d5c70>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GdbusModem3gppIface)


