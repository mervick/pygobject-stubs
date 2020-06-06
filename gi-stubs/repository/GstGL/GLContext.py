# encoding: utf-8
# module gi.repository.GstGL
# from /usr/lib64/girepository-1.0/GstGL-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


class GLContext(__gi_repository_Gst.Object):
    """
    :Constructors:
    
    ::
    
        GLContext(**properties)
        new(display:GstGL.GLDisplay) -> GstGL.GLContext
        new_wrapped(display:GstGL.GLDisplay, handle:int, context_type:GstGL.GLPlatform, available_apis:GstGL.GLAPI) -> GstGL.GLContext
    """
    def activate(self, activate): # real signature unknown; restored from __doc__
        """ activate(self, activate:bool) -> bool """
        return False

    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_share(self, other_context): # real signature unknown; restored from __doc__
        """ can_share(self, other_context:GstGL.GLContext) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_feature(self, feature): # real signature unknown; restored from __doc__
        """ check_feature(self, feature:str) -> bool """
        return False

    def check_framebuffer_status(self, fbo_target): # real signature unknown; restored from __doc__
        """ check_framebuffer_status(self, fbo_target:int) -> bool """
        return False

    def check_gl_version(self, api, maj, min): # real signature unknown; restored from __doc__
        """ check_gl_version(self, api:GstGL.GLAPI, maj:int, min:int) -> bool """
        return False

    def check_uniqueness(self, p_list, name): # real signature unknown; restored from __doc__
        """ check_uniqueness(list:list, name:str) -> bool """
        return False

    def clear_framebuffer(self): # real signature unknown; restored from __doc__
        """ clear_framebuffer(self) """
        pass

    def clear_shader(self): # real signature unknown; restored from __doc__
        """ clear_shader(self) """
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

    def create(self, other_context=None): # real signature unknown; restored from __doc__
        """ create(self, other_context:GstGL.GLContext=None) -> bool """
        return False

    def default_deep_notify(self, p_object, orig, pspec, excluded_props=None): # real signature unknown; restored from __doc__
        """ default_deep_notify(object:GObject.Object, orig:Gst.Object, pspec:GObject.ParamSpec, excluded_props:list=None) """
        pass

    def default_error(self, error, debug=None): # real signature unknown; restored from __doc__
        """ default_error(self, error:error, debug:str=None) """
        pass

    def default_get_proc_address(self, gl_api, name): # real signature unknown; restored from __doc__
        """ default_get_proc_address(gl_api:GstGL.GLAPI, name:str) """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self, activate:bool) -> bool """
        pass

    def do_check_feature(self, *args, **kwargs): # real signature unknown
        """ check_feature(self, feature:str) -> bool """
        pass

    def do_choose_format(self, *args, **kwargs): # real signature unknown
        """ choose_format(self) -> bool """
        pass

    def do_create_context(self, *args, **kwargs): # real signature unknown
        """ create_context(self, gl_api:GstGL.GLAPI, other_context:GstGL.GLContext) -> bool """
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def do_destroy_context(self, *args, **kwargs): # real signature unknown
        """ destroy_context(self) """
        pass

    def do_get_gl_api(self, *args, **kwargs): # real signature unknown
        """ get_gl_api(self) -> GstGL.GLAPI """
        pass

    def do_get_gl_context(self, *args, **kwargs): # real signature unknown
        """ get_gl_context(self) -> int """
        pass

    def do_get_gl_platform(self, *args, **kwargs): # real signature unknown
        """ get_gl_platform(self) -> GstGL.GLPlatform """
        pass

    def do_get_gl_platform_version(self, *args, **kwargs): # real signature unknown
        """ get_gl_platform_version(self) -> major:int, minor:int """
        pass

    def do_swap_buffers(self, *args, **kwargs): # real signature unknown
        """ swap_buffers(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def fill_info(self): # real signature unknown; restored from __doc__
        """ fill_info(self) -> bool """
        return False

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

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_current(self): # real signature unknown; restored from __doc__
        """ get_current() -> GstGL.GLContext """
        pass

    def get_current_gl_api(self, platform): # real signature unknown; restored from __doc__
        """ get_current_gl_api(platform:GstGL.GLPlatform) -> GstGL.GLAPI, major:int, minor:int """
        pass

    def get_current_gl_context(self, context_type): # real signature unknown; restored from __doc__
        """ get_current_gl_context(context_type:GstGL.GLPlatform) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> GstGL.GLDisplay """
        pass

    def get_gl_api(self): # real signature unknown; restored from __doc__
        """ get_gl_api(self) -> GstGL.GLAPI """
        pass

    def get_gl_context(self): # real signature unknown; restored from __doc__
        """ get_gl_context(self) -> int """
        return 0

    def get_gl_platform(self): # real signature unknown; restored from __doc__
        """ get_gl_platform(self) -> GstGL.GLPlatform """
        pass

    def get_gl_platform_version(self): # real signature unknown; restored from __doc__
        """ get_gl_platform_version(self) -> major:int, minor:int """
        pass

    def get_gl_version(self): # real signature unknown; restored from __doc__
        """ get_gl_version(self) -> maj:int, min:int """
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.Object or None """
        pass

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str """
        return ""

    def get_proc_address(self, name): # real signature unknown; restored from __doc__
        """ get_proc_address(self, name:str) """
        pass

    def get_proc_address_with_platform(self, context_type, gl_api, name): # real signature unknown; restored from __doc__
        """ get_proc_address_with_platform(context_type:GstGL.GLPlatform, gl_api:GstGL.GLAPI, name:str) """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_thread(self): # real signature unknown; restored from __doc__
        """ get_thread(self) -> GLib.Thread """
        pass

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
        pass

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> GstGL.GLWindow or None """
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

    def has_active_control_bindings(self): # real signature unknown; restored from __doc__
        """ has_active_control_bindings(self) -> bool """
        return False

    def has_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_as_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_parent(self, parent): # real signature unknown; restored from __doc__
        """ has_as_parent(self, parent:Gst.Object) -> bool """
        return False

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

    def is_shared(self): # real signature unknown; restored from __doc__
        """ is_shared(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, display): # real signature unknown; restored from __doc__
        """ new(display:GstGL.GLDisplay) -> GstGL.GLContext """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_wrapped(self, display, handle, context_type, available_apis): # real signature unknown; restored from __doc__
        """ new_wrapped(display:GstGL.GLDisplay, handle:int, context_type:GstGL.GLPlatform, available_apis:GstGL.GLAPI) -> GstGL.GLContext """
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

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gst.Object """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ remove_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def replace(self, oldobj=None, newobj=None): # real signature unknown; restored from __doc__
        """ replace(oldobj:Gst.Object=None, newobj:Gst.Object=None) -> bool, oldobj:Gst.Object """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_control_bindings_disabled(self, disabled): # real signature unknown; restored from __doc__
        """ set_control_bindings_disabled(self, disabled:bool) """
        pass

    def set_control_binding_disabled(self, property_name, disabled): # real signature unknown; restored from __doc__
        """ set_control_binding_disabled(self, property_name:str, disabled:bool) """
        pass

    def set_control_rate(self, control_rate): # real signature unknown; restored from __doc__
        """ set_control_rate(self, control_rate:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_shared_with(self, share): # real signature unknown; restored from __doc__
        """ set_shared_with(self, share:GstGL.GLContext) """
        pass

    def set_window(self, window): # real signature unknown; restored from __doc__
        """ set_window(self, window:GstGL.GLWindow) -> bool """
        return False

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

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def supports_glsl_profile_version(self, version, profile): # real signature unknown; restored from __doc__
        """ supports_glsl_profile_version(self, version:GstGL.GLSLVersion, profile:GstGL.GLSLProfile) -> bool """
        return False

    def supports_precision(self, version, profile): # real signature unknown; restored from __doc__
        """ supports_precision(self, version:GstGL.GLSLVersion, profile:GstGL.GLSLProfile) -> bool """
        return False

    def supports_precision_highp(self, version, profile): # real signature unknown; restored from __doc__
        """ supports_precision_highp(self, version:GstGL.GLSLVersion, profile:GstGL.GLSLProfile) -> bool """
        return False

    def swap_buffers(self): # real signature unknown; restored from __doc__
        """ swap_buffers(self) """
        pass

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def thread_add(self, func, data=None): # real signature unknown; restored from __doc__
        """ thread_add(self, func:GstGL.GLContextThreadFunc, data=None) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gl_vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f56a39f7fd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(GLContext), '__module__': 'gi.repository.GstGL', '__gtype__': <GType GstGLContext (93979012351760)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_wrapped': gi.FunctionInfo(new_wrapped), 'default_get_proc_address': gi.FunctionInfo(default_get_proc_address), 'get_current': gi.FunctionInfo(get_current), 'get_current_gl_api': gi.FunctionInfo(get_current_gl_api), 'get_current_gl_context': gi.FunctionInfo(get_current_gl_context), 'get_proc_address_with_platform': gi.FunctionInfo(get_proc_address_with_platform), 'activate': gi.FunctionInfo(activate), 'can_share': gi.FunctionInfo(can_share), 'check_feature': gi.FunctionInfo(check_feature), 'check_framebuffer_status': gi.FunctionInfo(check_framebuffer_status), 'check_gl_version': gi.FunctionInfo(check_gl_version), 'clear_framebuffer': gi.FunctionInfo(clear_framebuffer), 'clear_shader': gi.FunctionInfo(clear_shader), 'create': gi.FunctionInfo(create), 'destroy': gi.FunctionInfo(destroy), 'fill_info': gi.FunctionInfo(fill_info), 'get_display': gi.FunctionInfo(get_display), 'get_gl_api': gi.FunctionInfo(get_gl_api), 'get_gl_context': gi.FunctionInfo(get_gl_context), 'get_gl_platform': gi.FunctionInfo(get_gl_platform), 'get_gl_platform_version': gi.FunctionInfo(get_gl_platform_version), 'get_gl_version': gi.FunctionInfo(get_gl_version), 'get_proc_address': gi.FunctionInfo(get_proc_address), 'get_thread': gi.FunctionInfo(get_thread), 'get_window': gi.FunctionInfo(get_window), 'is_shared': gi.FunctionInfo(is_shared), 'set_shared_with': gi.FunctionInfo(set_shared_with), 'set_window': gi.FunctionInfo(set_window), 'supports_glsl_profile_version': gi.FunctionInfo(supports_glsl_profile_version), 'supports_precision': gi.FunctionInfo(supports_precision), 'supports_precision_highp': gi.FunctionInfo(supports_precision_highp), 'swap_buffers': gi.FunctionInfo(swap_buffers), 'thread_add': gi.FunctionInfo(thread_add), 'do_activate': gi.VFuncInfo(activate), 'do_check_feature': gi.VFuncInfo(check_feature), 'do_choose_format': gi.VFuncInfo(choose_format), 'do_create_context': gi.VFuncInfo(create_context), 'do_destroy_context': gi.VFuncInfo(destroy_context), 'do_get_gl_api': gi.VFuncInfo(get_gl_api), 'do_get_gl_context': gi.VFuncInfo(get_gl_context), 'do_get_gl_platform': gi.VFuncInfo(get_gl_platform), 'do_get_gl_platform_version': gi.VFuncInfo(get_gl_platform_version), 'do_swap_buffers': gi.VFuncInfo(swap_buffers), 'parent': <property object at 0x7f56a3ff0310>, 'display': <property object at 0x7f56a3ff0450>, 'window': <property object at 0x7f56a3ff0540>, 'gl_vtable': <property object at 0x7f56a3ff0630>, 'priv': <property object at 0x7f56a3ff0720>, '_reserved': <property object at 0x7f56a3ff0810>})"
    __gdoc__ = 'Object GstGLContext\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstGLContext (93979012351760)>'
    __info__ = ObjectInfo(GLContext)


