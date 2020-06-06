# encoding: utf-8
# module gi.repository.GcrUi
# from /usr/lib64/girepository-1.0/GcrUi-3.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gcr as __gi_repository_Gcr
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


from .Renderer import Renderer

class CertificateRenderer(__gi_overrides_GObject.Object, __gi_repository_Gcr.Certificate, __gi_repository_Gcr.Comparable, Renderer):
    """
    :Constructors:
    
    ::
    
        CertificateRenderer(**properties)
        new(certificate:Gcr.Certificate) -> GcrUi.CertificateRenderer
        new_for_attributes(label:str=None, attrs=None) -> GcrUi.CertificateRenderer
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compare(self, first=None, other=None): # real signature unknown; restored from __doc__
        """ compare(first:Gcr.Comparable=None, other:Gcr.Comparable=None) -> int """
        return 0

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, label=None, attrs): # real signature unknown; restored from __doc__
        """ create(label:str=None, attrs:Gck.Attributes) -> GcrUi.Renderer or None """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_data_changed(self): # real signature unknown; restored from __doc__
        """ emit_data_changed(self) """
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> Gck.Attributes or None """
        pass

    def get_basic_constraints(self): # real signature unknown; restored from __doc__
        """ get_basic_constraints(self) -> bool, is_ca:bool, path_len:int """
        return False

    def get_certificate(self): # real signature unknown; restored from __doc__
        """ get_certificate(self) -> Gcr.Certificate """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_der_data(self): # real signature unknown; restored from __doc__
        """ get_der_data(self) -> list, n_data:int """
        return []

    def get_expiry_date(self): # real signature unknown; restored from __doc__
        """ get_expiry_date(self) -> GLib.Date """
        pass

    def get_fingerprint(self, type): # real signature unknown; restored from __doc__
        """ get_fingerprint(self, type:GLib.ChecksumType) -> list, n_length:int """
        return []

    def get_fingerprint_hex(self, type): # real signature unknown; restored from __doc__
        """ get_fingerprint_hex(self, type:GLib.ChecksumType) -> str """
        return ""

    def get_issued_date(self): # real signature unknown; restored from __doc__
        """ get_issued_date(self) -> GLib.Date """
        pass

    def get_issuer_cn(self): # real signature unknown; restored from __doc__
        """ get_issuer_cn(self) -> str """
        return ""

    def get_issuer_dn(self): # real signature unknown; restored from __doc__
        """ get_issuer_dn(self) -> str """
        return ""

    def get_issuer_name(self): # real signature unknown; restored from __doc__
        """ get_issuer_name(self) -> str """
        return ""

    def get_issuer_part(self, part): # real signature unknown; restored from __doc__
        """ get_issuer_part(self, part:str) -> str or None """
        return ""

    def get_issuer_raw(self): # real signature unknown; restored from __doc__
        """ get_issuer_raw(self) -> list, n_data:int """
        return []

    def get_key_size(self): # real signature unknown; restored from __doc__
        """ get_key_size(self) -> int """
        return 0

    def get_markup_text(self): # real signature unknown; restored from __doc__
        """ get_markup_text(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_serial_number(self): # real signature unknown; restored from __doc__
        """ get_serial_number(self) -> list, n_length:int """
        return []

    def get_serial_number_hex(self): # real signature unknown; restored from __doc__
        """ get_serial_number_hex(self) -> str """
        return ""

    def get_subject_cn(self): # real signature unknown; restored from __doc__
        """ get_subject_cn(self) -> str """
        return ""

    def get_subject_dn(self): # real signature unknown; restored from __doc__
        """ get_subject_dn(self) -> str """
        return ""

    def get_subject_name(self): # real signature unknown; restored from __doc__
        """ get_subject_name(self) -> str """
        return ""

    def get_subject_part(self, part): # real signature unknown; restored from __doc__
        """ get_subject_part(self, part:str) -> str or None """
        return ""

    def get_subject_raw(self): # real signature unknown; restored from __doc__
        """ get_subject_raw(self) -> list, n_data:int """
        return []

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_issuer(self, issuer): # real signature unknown; restored from __doc__
        """ is_issuer(self, issuer:Gcr.Certificate) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def mixin_emit_notify(self): # real signature unknown; restored from __doc__
        """ mixin_emit_notify(self) """
        pass

    def new(self, certificate): # real signature unknown; restored from __doc__
        """ new(certificate:Gcr.Certificate) -> GcrUi.CertificateRenderer """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_for_attributes(self, label=None, attrs=None): # real signature unknown; restored from __doc__
        """ new_for_attributes(label:str=None, attrs=None) -> GcrUi.CertificateRenderer """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def popuplate_popup(self, viewer, menu): # real signature unknown; restored from __doc__
        """ popuplate_popup(self, viewer:GcrUi.Viewer, menu:Gtk.Menu) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register(self, renderer_type, attrs): # real signature unknown; restored from __doc__
        """ register(renderer_type:GType, attrs:Gck.Attributes) """
        pass

    def register_well_known(self): # real signature unknown; restored from __doc__
        """ register_well_known() """
        pass

    def render_view(self, viewer): # real signature unknown; restored from __doc__
        """ render_view(self, viewer:GcrUi.Viewer) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_attributes(self, attrs=None): # real signature unknown; restored from __doc__
        """ set_attributes(self, attrs:Gck.Attributes=None) """
        pass

    def set_certificate(self, certificate=None): # real signature unknown; restored from __doc__
        """ set_certificate(self, certificate:Gcr.Certificate=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fa329996df0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(CertificateRenderer), '__module__': 'gi.repository.GcrUi', '__gtype__': <GType GcrCertificateRenderer (94715180823952)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_for_attributes': gi.FunctionInfo(new_for_attributes), 'get_certificate': gi.FunctionInfo(get_certificate), 'set_certificate': gi.FunctionInfo(set_certificate), 'parent': <property object at 0x7fa32999bea0>, 'pv': <property object at 0x7fa32999bef0>})"
    __gdoc__ = 'Object GcrCertificateRenderer\n\nProperties from GcrCertificateRenderer:\n  certificate -> GcrCertificate: Certificate\n    Certificate to display.\n  label -> gchararray: Label\n    Certificate Label\n  attributes -> GckAttributes: Attributes\n    Certificate pkcs11 attributes\n\nSignals from GcrRenderer:\n  data-changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GcrCertificateRenderer (94715180823952)>'
    __info__ = ObjectInfo(CertificateRenderer)


