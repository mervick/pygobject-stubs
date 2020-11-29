# encoding: utf-8
# module gi.repository.Unity
# from /usr/lib/girepository-1.0/Unity-7.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Unity as __gi_overrides_Unity
import gi.repository.Dee as __gi_repository_Dee
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .Preview import Preview

class PaymentPreview(Preview):
    """
    :Constructors:
    
    ::
    
        PaymentPreview(**properties)
        new(title:str, subtitle:str, image:Gio.Icon=None) -> Unity.PaymentPreview
        for_type(title:str, subtitle:str, image:Gio.Icon=None, type:Unity.PaymentPreviewType) -> Unity.PaymentPreview
        for_application(title:str, subtitle:str, image:Gio.Icon=None) -> Unity.PaymentPreview
        for_music(title:str, subtitle:str, image:Gio.Icon=None) -> Unity.PaymentPreview
        for_error(title:str, subtitle:str, image:Gio.Icon=None) -> Unity.PaymentPreview
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

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
        # no doc
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        # no doc
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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
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
        # no doc
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
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

    def __dir__(self): # real signature unknown; restored from __doc__
        """
        __dir__() -> list
        default dir() implementation
        """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ default object formatter """
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
        """ helper for pickle """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """
        __sizeof__() -> int
        size of object in memory, in bytes
        """
        return 0

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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    add_action = gi.FunctionInfo(add_action)
    add_info = gi.FunctionInfo(add_info)
    do_serialize_as = gi.VFuncInfo(serialize_as)
    externalize = gi.FunctionInfo(externalize)
    for_application = gi.FunctionInfo(for_application)
    for_error = gi.FunctionInfo(for_error)
    for_music = gi.FunctionInfo(for_music)
    for_type = gi.FunctionInfo(for_type)
    getv = gi.FunctionInfo(getv)
    get_description_markup = gi.FunctionInfo(get_description_markup)
    get_email = gi.FunctionInfo(get_email)
    get_header = gi.FunctionInfo(get_header)
    get_image = gi.FunctionInfo(get_image)
    get_image_source_uri = gi.FunctionInfo(get_image_source_uri)
    get_payment_method = gi.FunctionInfo(get_payment_method)
    get_preview_type = gi.FunctionInfo(get_preview_type)
    get_purchase_prize = gi.FunctionInfo(get_purchase_prize)
    get_purchase_type = gi.FunctionInfo(get_purchase_type)
    get_subtitle = gi.FunctionInfo(get_subtitle)
    get_title = gi.FunctionInfo(get_title)
    is_floating = gi.FunctionInfo(is_floating)
    new = gi.FunctionInfo(new)
    newv = gi.FunctionInfo(newv)
    notify = gi.FunctionInfo(notify)
    parse = gi.FunctionInfo(parse)
    parse_external = gi.FunctionInfo(parse_external)
    props = None # (!) real value is '<gi._gi.GProps object at 0x7f0cf0d03fd0>'
    serialize = gi.FunctionInfo(serialize)
    serialize_as = gi.FunctionInfo(serialize_as)
    set_description_markup = gi.FunctionInfo(set_description_markup)
    set_email = gi.FunctionInfo(set_email)
    set_header = gi.FunctionInfo(set_header)
    set_image = gi.FunctionInfo(set_image)
    set_image_source_uri = gi.FunctionInfo(set_image_source_uri)
    set_payment_method = gi.FunctionInfo(set_payment_method)
    set_preview_type = gi.FunctionInfo(set_preview_type)
    set_purchase_prize = gi.FunctionInfo(set_purchase_prize)
    set_purchase_type = gi.FunctionInfo(set_purchase_type)
    set_subtitle = gi.FunctionInfo(set_subtitle)
    set_title = gi.FunctionInfo(set_title)
    thaw_notify = gi.FunctionInfo(thaw_notify)
    _force_floating = gi.FunctionInfo(force_floating)
    _ref = gi.FunctionInfo(ref)
    _ref_sink = gi.FunctionInfo(ref_sink)
    _unref = gi.FunctionInfo(unref)
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(PaymentPreview), '__module__': 'gi.repository.Unity', '__gtype__': <GType UnityPaymentPreview (26943632)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'for_type': gi.FunctionInfo(for_type), 'for_application': gi.FunctionInfo(for_application), 'for_music': gi.FunctionInfo(for_music), 'for_error': gi.FunctionInfo(for_error), 'get_header': gi.FunctionInfo(get_header), 'set_header': gi.FunctionInfo(set_header), 'get_email': gi.FunctionInfo(get_email), 'set_email': gi.FunctionInfo(set_email), 'get_payment_method': gi.FunctionInfo(get_payment_method), 'set_payment_method': gi.FunctionInfo(set_payment_method), 'get_purchase_prize': gi.FunctionInfo(get_purchase_prize), 'set_purchase_prize': gi.FunctionInfo(set_purchase_prize), 'get_purchase_type': gi.FunctionInfo(get_purchase_type), 'set_purchase_type': gi.FunctionInfo(set_purchase_type), 'get_preview_type': gi.FunctionInfo(get_preview_type), 'set_preview_type': gi.FunctionInfo(set_preview_type), 'parent_instance': <property object at 0x7f0cf0e4f188>, 'priv': <property object at 0x7f0cf0e4f1d8>})"
    __gdoc__ = 'Object UnityPaymentPreview\n\nProperties from UnityPaymentPreview:\n  header -> gchararray: header\n    header\n  email -> gchararray: email\n    email\n  payment-method -> gchararray: payment-method\n    payment-method\n  purchase-prize -> gchararray: purchase-prize\n    purchase-prize\n  purchase-type -> gchararray: purchase-type\n    purchase-type\n  preview-type -> UnityPaymentPreviewType: preview-type\n    preview-type\n\nProperties from UnityPreview:\n  title -> gchararray: title\n    title\n  subtitle -> gchararray: subtitle\n    subtitle\n  description-markup -> gchararray: description-markup\n    description-markup\n  image-source-uri -> gchararray: image-source-uri\n    image-source-uri\n  image -> GIcon: image\n    image\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UnityPaymentPreview (26943632)>'
    __info__ = ObjectInfo(PaymentPreview)


