# encoding: utf-8
# module gi.repository.GtkSource
# from /usr/lib64/girepository-1.0/GtkSource-3.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class PrintCompositor(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        PrintCompositor(**properties)
        new(buffer:GtkSource.Buffer) -> GtkSource.PrintCompositor
        new_from_view(view:GtkSource.View) -> GtkSource.PrintCompositor
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

    def draw_page(self, context, page_nr): # real signature unknown; restored from __doc__
        """ draw_page(self, context:Gtk.PrintContext, page_nr:int) """
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

    def get_body_font_name(self): # real signature unknown; restored from __doc__
        """ get_body_font_name(self) -> str """
        return ""

    def get_bottom_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_bottom_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_buffer(self): # real signature unknown; restored from __doc__
        """ get_buffer(self) -> GtkSource.Buffer """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_footer_font_name(self): # real signature unknown; restored from __doc__
        """ get_footer_font_name(self) -> str """
        return ""

    def get_header_font_name(self): # real signature unknown; restored from __doc__
        """ get_header_font_name(self) -> str """
        return ""

    def get_highlight_syntax(self): # real signature unknown; restored from __doc__
        """ get_highlight_syntax(self) -> bool """
        return False

    def get_left_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_left_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_line_numbers_font_name(self): # real signature unknown; restored from __doc__
        """ get_line_numbers_font_name(self) -> str """
        return ""

    def get_n_pages(self): # real signature unknown; restored from __doc__
        """ get_n_pages(self) -> int """
        return 0

    def get_pagination_progress(self): # real signature unknown; restored from __doc__
        """ get_pagination_progress(self) -> float """
        return 0.0

    def get_print_footer(self): # real signature unknown; restored from __doc__
        """ get_print_footer(self) -> bool """
        return False

    def get_print_header(self): # real signature unknown; restored from __doc__
        """ get_print_header(self) -> bool """
        return False

    def get_print_line_numbers(self): # real signature unknown; restored from __doc__
        """ get_print_line_numbers(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_right_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_right_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_tab_width(self): # real signature unknown; restored from __doc__
        """ get_tab_width(self) -> int """
        return 0

    def get_top_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_top_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_wrap_mode(self): # real signature unknown; restored from __doc__
        """ get_wrap_mode(self) -> Gtk.WrapMode """
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

    def new(self, buffer): # real signature unknown; restored from __doc__
        """ new(buffer:GtkSource.Buffer) -> GtkSource.PrintCompositor """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_view(self, view): # real signature unknown; restored from __doc__
        """ new_from_view(view:GtkSource.View) -> GtkSource.PrintCompositor """
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

    def paginate(self, context): # real signature unknown; restored from __doc__
        """ paginate(self, context:Gtk.PrintContext) -> bool """
        return False

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

    def set_body_font_name(self, font_name): # real signature unknown; restored from __doc__
        """ set_body_font_name(self, font_name:str) """
        pass

    def set_bottom_margin(self, margin, unit): # real signature unknown; restored from __doc__
        """ set_bottom_margin(self, margin:float, unit:Gtk.Unit) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_footer_font_name(self, font_name=None): # real signature unknown; restored from __doc__
        """ set_footer_font_name(self, font_name:str=None) """
        pass

    def set_footer_format(self, separator, left=None, center=None, right=None): # real signature unknown; restored from __doc__
        """ set_footer_format(self, separator:bool, left:str=None, center:str=None, right:str=None) """
        pass

    def set_header_font_name(self, font_name=None): # real signature unknown; restored from __doc__
        """ set_header_font_name(self, font_name:str=None) """
        pass

    def set_header_format(self, separator, left=None, center=None, right=None): # real signature unknown; restored from __doc__
        """ set_header_format(self, separator:bool, left:str=None, center:str=None, right:str=None) """
        pass

    def set_highlight_syntax(self, highlight): # real signature unknown; restored from __doc__
        """ set_highlight_syntax(self, highlight:bool) """
        pass

    def set_left_margin(self, margin, unit): # real signature unknown; restored from __doc__
        """ set_left_margin(self, margin:float, unit:Gtk.Unit) """
        pass

    def set_line_numbers_font_name(self, font_name=None): # real signature unknown; restored from __doc__
        """ set_line_numbers_font_name(self, font_name:str=None) """
        pass

    def set_print_footer(self, print_): # real signature unknown; restored from __doc__
        """ set_print_footer(self, print_:bool) """
        pass

    def set_print_header(self, print_): # real signature unknown; restored from __doc__
        """ set_print_header(self, print_:bool) """
        pass

    def set_print_line_numbers(self, interval): # real signature unknown; restored from __doc__
        """ set_print_line_numbers(self, interval:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_right_margin(self, margin, unit): # real signature unknown; restored from __doc__
        """ set_right_margin(self, margin:float, unit:Gtk.Unit) """
        pass

    def set_tab_width(self, width): # real signature unknown; restored from __doc__
        """ set_tab_width(self, width:int) """
        pass

    def set_top_margin(self, margin, unit): # real signature unknown; restored from __doc__
        """ set_top_margin(self, margin:float, unit:Gtk.Unit) """
        pass

    def set_wrap_mode(self, wrap_mode): # real signature unknown; restored from __doc__
        """ set_wrap_mode(self, wrap_mode:Gtk.WrapMode) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f77ca3579d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(PrintCompositor), '__module__': 'gi.repository.GtkSource', '__gtype__': <GType GtkSourcePrintCompositor (94260244221296)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_view': gi.FunctionInfo(new_from_view), 'draw_page': gi.FunctionInfo(draw_page), 'get_body_font_name': gi.FunctionInfo(get_body_font_name), 'get_bottom_margin': gi.FunctionInfo(get_bottom_margin), 'get_buffer': gi.FunctionInfo(get_buffer), 'get_footer_font_name': gi.FunctionInfo(get_footer_font_name), 'get_header_font_name': gi.FunctionInfo(get_header_font_name), 'get_highlight_syntax': gi.FunctionInfo(get_highlight_syntax), 'get_left_margin': gi.FunctionInfo(get_left_margin), 'get_line_numbers_font_name': gi.FunctionInfo(get_line_numbers_font_name), 'get_n_pages': gi.FunctionInfo(get_n_pages), 'get_pagination_progress': gi.FunctionInfo(get_pagination_progress), 'get_print_footer': gi.FunctionInfo(get_print_footer), 'get_print_header': gi.FunctionInfo(get_print_header), 'get_print_line_numbers': gi.FunctionInfo(get_print_line_numbers), 'get_right_margin': gi.FunctionInfo(get_right_margin), 'get_tab_width': gi.FunctionInfo(get_tab_width), 'get_top_margin': gi.FunctionInfo(get_top_margin), 'get_wrap_mode': gi.FunctionInfo(get_wrap_mode), 'paginate': gi.FunctionInfo(paginate), 'set_body_font_name': gi.FunctionInfo(set_body_font_name), 'set_bottom_margin': gi.FunctionInfo(set_bottom_margin), 'set_footer_font_name': gi.FunctionInfo(set_footer_font_name), 'set_footer_format': gi.FunctionInfo(set_footer_format), 'set_header_font_name': gi.FunctionInfo(set_header_font_name), 'set_header_format': gi.FunctionInfo(set_header_format), 'set_highlight_syntax': gi.FunctionInfo(set_highlight_syntax), 'set_left_margin': gi.FunctionInfo(set_left_margin), 'set_line_numbers_font_name': gi.FunctionInfo(set_line_numbers_font_name), 'set_print_footer': gi.FunctionInfo(set_print_footer), 'set_print_header': gi.FunctionInfo(set_print_header), 'set_print_line_numbers': gi.FunctionInfo(set_print_line_numbers), 'set_right_margin': gi.FunctionInfo(set_right_margin), 'set_tab_width': gi.FunctionInfo(set_tab_width), 'set_top_margin': gi.FunctionInfo(set_top_margin), 'set_wrap_mode': gi.FunctionInfo(set_wrap_mode), 'parent_instance': <property object at 0x7f77ca6e0d60>, 'priv': <property object at 0x7f77ca6e0e50>})"
    __gdoc__ = 'Object GtkSourcePrintCompositor\n\nProperties from GtkSourcePrintCompositor:\n  buffer -> GtkSourceBuffer: Source Buffer\n    The GtkSourceBuffer object to print\n  tab-width -> guint: Tab Width\n    Width of a tab character expressed in spaces\n  wrap-mode -> GtkWrapMode: Wrap Mode\n    \n  highlight-syntax -> gboolean: Highlight Syntax\n    \n  print-line-numbers -> guint: Print Line Numbers\n    \n  print-header -> gboolean: Print Header\n    \n  print-footer -> gboolean: Print Footer\n    \n  body-font-name -> gchararray: Body Font Name\n    \n  line-numbers-font-name -> gchararray: Line Numbers Font Name\n    \n  header-font-name -> gchararray: Header Font Name\n    \n  footer-font-name -> gchararray: Footer Font Name\n    \n  n-pages -> gint: Number of pages\n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkSourcePrintCompositor (94260244221296)>'
    __info__ = ObjectInfo(PrintCompositor)


