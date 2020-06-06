# encoding: utf-8
# module gi.repository.EvinceView
# from /usr/lib64/girepository-1.0/EvinceView-3.0.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class DocumentModel(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        DocumentModel(**properties)
        new() -> EvinceView.DocumentModel
        new_with_document(document:EvinceDocument.Document) -> EvinceView.DocumentModel
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
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
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

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_continuous(self): # real signature unknown; restored from __doc__
        """ get_continuous(self) -> bool """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_document(self): # real signature unknown; restored from __doc__
        """ get_document(self) -> EvinceDocument.Document """
        pass

    def get_dual_page(self): # real signature unknown; restored from __doc__
        """ get_dual_page(self) -> bool """
        return False

    def get_dual_page_odd_pages_left(self): # real signature unknown; restored from __doc__
        """ get_dual_page_odd_pages_left(self) -> bool """
        return False

    def get_fullscreen(self): # real signature unknown; restored from __doc__
        """ get_fullscreen(self) -> bool """
        return False

    def get_inverted_colors(self): # real signature unknown; restored from __doc__
        """ get_inverted_colors(self) -> bool """
        return False

    def get_max_scale(self): # real signature unknown; restored from __doc__
        """ get_max_scale(self) -> float """
        return 0.0

    def get_min_scale(self): # real signature unknown; restored from __doc__
        """ get_min_scale(self) -> float """
        return 0.0

    def get_page(self): # real signature unknown; restored from __doc__
        """ get_page(self) -> int """
        return 0

    def get_page_layout(self): # real signature unknown; restored from __doc__
        """ get_page_layout(self) -> EvinceView.PageLayout """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rotation(self): # real signature unknown; restored from __doc__
        """ get_rotation(self) -> int """
        return 0

    def get_rtl(self): # real signature unknown; restored from __doc__
        """ get_rtl(self) -> bool """
        return False

    def get_scale(self): # real signature unknown; restored from __doc__
        """ get_scale(self) -> float """
        return 0.0

    def get_sizing_mode(self): # real signature unknown; restored from __doc__
        """ get_sizing_mode(self) -> EvinceView.SizingMode """
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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> EvinceView.DocumentModel """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_document(self, document): # real signature unknown; restored from __doc__
        """ new_with_document(document:EvinceDocument.Document) -> EvinceView.DocumentModel """
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

    def set_continuous(self, continuous): # real signature unknown; restored from __doc__
        """ set_continuous(self, continuous:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_document(self, document): # real signature unknown; restored from __doc__
        """ set_document(self, document:EvinceDocument.Document) """
        pass

    def set_dual_page(self, dual_page): # real signature unknown; restored from __doc__
        """ set_dual_page(self, dual_page:bool) """
        pass

    def set_dual_page_odd_pages_left(self, odd_left): # real signature unknown; restored from __doc__
        """ set_dual_page_odd_pages_left(self, odd_left:bool) """
        pass

    def set_fullscreen(self, fullscreen): # real signature unknown; restored from __doc__
        """ set_fullscreen(self, fullscreen:bool) """
        pass

    def set_inverted_colors(self, inverted_colors): # real signature unknown; restored from __doc__
        """ set_inverted_colors(self, inverted_colors:bool) """
        pass

    def set_max_scale(self, max_scale): # real signature unknown; restored from __doc__
        """ set_max_scale(self, max_scale:float) """
        pass

    def set_min_scale(self, min_scale): # real signature unknown; restored from __doc__
        """ set_min_scale(self, min_scale:float) """
        pass

    def set_page(self, page): # real signature unknown; restored from __doc__
        """ set_page(self, page:int) """
        pass

    def set_page_by_label(self, page_label): # real signature unknown; restored from __doc__
        """ set_page_by_label(self, page_label:str) """
        pass

    def set_page_layout(self, layout): # real signature unknown; restored from __doc__
        """ set_page_layout(self, layout:EvinceView.PageLayout) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_rotation(self, rotation): # real signature unknown; restored from __doc__
        """ set_rotation(self, rotation:int) """
        pass

    def set_rtl(self, rtl): # real signature unknown; restored from __doc__
        """ set_rtl(self, rtl:bool) """
        pass

    def set_scale(self, scale): # real signature unknown; restored from __doc__
        """ set_scale(self, scale:float) """
        pass

    def set_sizing_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_sizing_mode(self, mode:EvinceView.SizingMode) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb1d661d370>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DocumentModel), '__module__': 'gi.repository.EvinceView', '__gtype__': <GType EvDocumentModel (94181028608672)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_with_document': gi.FunctionInfo(new_with_document), 'get_continuous': gi.FunctionInfo(get_continuous), 'get_document': gi.FunctionInfo(get_document), 'get_dual_page': gi.FunctionInfo(get_dual_page), 'get_dual_page_odd_pages_left': gi.FunctionInfo(get_dual_page_odd_pages_left), 'get_fullscreen': gi.FunctionInfo(get_fullscreen), 'get_inverted_colors': gi.FunctionInfo(get_inverted_colors), 'get_max_scale': gi.FunctionInfo(get_max_scale), 'get_min_scale': gi.FunctionInfo(get_min_scale), 'get_page': gi.FunctionInfo(get_page), 'get_page_layout': gi.FunctionInfo(get_page_layout), 'get_rotation': gi.FunctionInfo(get_rotation), 'get_rtl': gi.FunctionInfo(get_rtl), 'get_scale': gi.FunctionInfo(get_scale), 'get_sizing_mode': gi.FunctionInfo(get_sizing_mode), 'set_continuous': gi.FunctionInfo(set_continuous), 'set_document': gi.FunctionInfo(set_document), 'set_dual_page': gi.FunctionInfo(set_dual_page), 'set_dual_page_odd_pages_left': gi.FunctionInfo(set_dual_page_odd_pages_left), 'set_fullscreen': gi.FunctionInfo(set_fullscreen), 'set_inverted_colors': gi.FunctionInfo(set_inverted_colors), 'set_max_scale': gi.FunctionInfo(set_max_scale), 'set_min_scale': gi.FunctionInfo(set_min_scale), 'set_page': gi.FunctionInfo(set_page), 'set_page_by_label': gi.FunctionInfo(set_page_by_label), 'set_page_layout': gi.FunctionInfo(set_page_layout), 'set_rotation': gi.FunctionInfo(set_rotation), 'set_rtl': gi.FunctionInfo(set_rtl), 'set_scale': gi.FunctionInfo(set_scale), 'set_sizing_mode': gi.FunctionInfo(set_sizing_mode)})"
    __gdoc__ = 'Object EvDocumentModel\n\nSignals from EvDocumentModel:\n  page-changed (gint, gint)\n\nProperties from EvDocumentModel:\n  document -> EvDocument: Document\n    The current document\n  page -> gint: Page\n    Current page\n  rotation -> gint: Rotation\n    Current rotation angle\n  inverted-colors -> gboolean: Inverted Colors\n    Whether document is displayed with inverted colors\n  scale -> gdouble: Scale\n    Current scale factor\n  sizing-mode -> EvSizingMode: Sizing Mode\n    Current sizing mode\n  continuous -> gboolean: Continuous\n    Whether document is displayed in continuous mode\n  dual-page -> gboolean: Dual Page\n    Whether document is displayed in dual page mode\n  dual-odd-left -> gboolean: Odd Pages Left\n    Whether odd pages are displayed on left side in dual mode\n  rtl -> gboolean: Right to Left\n    Whether the document is written from right to left\n  fullscreen -> gboolean: Fullscreen\n    Whether document is displayed in fullscreen mode\n  min-scale -> gdouble: Minimum Scale\n    Minium scale factor\n  max-scale -> gdouble: Maximum Scale\n    Maximum scale factor\n  page-layout -> EvPageLayout: Page Layout\n    Current page layout\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EvDocumentModel (94181028608672)>'
    __info__ = ObjectInfo(DocumentModel)


