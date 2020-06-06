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


class GdbusSmsIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GdbusSmsIface()
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

    get_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_delivery_report_request = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_delivery_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_discharge_timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_message_reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_pdu_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_service_category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_smsc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_storage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_teleservice_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_validity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_send = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_store = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GdbusSmsIface), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GdbusSmsIface' objects>, '__weakref__': <attribute '__weakref__' of 'GdbusSmsIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f6943894360>, 'handle_send': <property object at 0x7f6943894450>, 'handle_store': <property object at 0x7f6943894540>, 'get_class': <property object at 0x7f6943894630>, 'get_data': <property object at 0x7f6943894720>, 'get_delivery_report_request': <property object at 0x7f6943894860>, 'get_delivery_state': <property object at 0x7f69438949a0>, 'get_discharge_timestamp': <property object at 0x7f6943894ae0>, 'get_message_reference': <property object at 0x7f6943894c20>, 'get_number': <property object at 0x7f6943894d10>, 'get_pdu_type': <property object at 0x7f6943894e00>, 'get_service_category': <property object at 0x7f6943894f40>, 'get_smsc': <property object at 0x7f6943896090>, 'get_state': <property object at 0x7f6943896180>, 'get_storage': <property object at 0x7f6943896270>, 'get_teleservice_id': <property object at 0x7f69438963b0>, 'get_text': <property object at 0x7f69438964a0>, 'get_timestamp': <property object at 0x7f6943896590>, 'get_validity': <property object at 0x7f6943896680>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GdbusSmsIface)


