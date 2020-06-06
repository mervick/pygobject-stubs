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


class GLShader(__gi_repository_Gst.Object):
    """
    :Constructors:
    
    ::
    
        GLShader(**properties)
        new(context:GstGL.GLContext) -> GstGL.GLShader
        new_default(context:GstGL.GLContext) -> GstGL.GLShader
    """
    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def attach(self, stage): # real signature unknown; restored from __doc__
        """ attach(self, stage:GstGL.GLSLStage) -> bool """
        return False

    def attach_unlocked(self, stage): # real signature unknown; restored from __doc__
        """ attach_unlocked(self, stage:GstGL.GLSLStage) -> bool """
        return False

    def bind_attribute_location(self, index, name): # real signature unknown; restored from __doc__
        """ bind_attribute_location(self, index:int, name:str) """
        pass

    def bind_frag_data_location(self, index, name): # real signature unknown; restored from __doc__
        """ bind_frag_data_location(self, index:int, name:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_uniqueness(self, p_list, name): # real signature unknown; restored from __doc__
        """ check_uniqueness(list:list, name:str) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def compile_attach_stage(self, stage): # real signature unknown; restored from __doc__
        """ compile_attach_stage(self, stage:GstGL.GLSLStage) -> bool """
        return False

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

    def default_deep_notify(self, p_object, orig, pspec, excluded_props=None): # real signature unknown; restored from __doc__
        """ default_deep_notify(object:GObject.Object, orig:Gst.Object, pspec:GObject.ParamSpec, excluded_props:list=None) """
        pass

    def default_error(self, error, debug=None): # real signature unknown; restored from __doc__
        """ default_error(self, error:error, debug:str=None) """
        pass

    def detach(self, stage): # real signature unknown; restored from __doc__
        """ detach(self, stage:GstGL.GLSLStage) """
        pass

    def detach_unlocked(self, stage): # real signature unknown; restored from __doc__
        """ detach_unlocked(self, stage:GstGL.GLSLStage) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
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

    def get_attribute_location(self, name): # real signature unknown; restored from __doc__
        """ get_attribute_location(self, name:str) -> int """
        return 0

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def get_program_handle(self): # real signature unknown; restored from __doc__
        """ get_program_handle(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
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

    def is_linked(self): # real signature unknown; restored from __doc__
        """ is_linked(self) -> bool """
        return False

    def link(self): # real signature unknown; restored from __doc__
        """ link(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, context): # real signature unknown; restored from __doc__
        """ new(context:GstGL.GLContext) -> GstGL.GLShader """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_default(self, context): # real signature unknown; restored from __doc__
        """ new_default(context:GstGL.GLContext) -> GstGL.GLShader """
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

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def release_unlocked(self): # real signature unknown; restored from __doc__
        """ release_unlocked(self) """
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

    def set_uniform_1f(self, name, value): # real signature unknown; restored from __doc__
        """ set_uniform_1f(self, name:str, value:float) """
        pass

    def set_uniform_1fv(self, name, value): # real signature unknown; restored from __doc__
        """ set_uniform_1fv(self, name:str, value:list) """
        pass

    def set_uniform_1i(self, name, value): # real signature unknown; restored from __doc__
        """ set_uniform_1i(self, name:str, value:int) """
        pass

    def set_uniform_1iv(self, name, value): # real signature unknown; restored from __doc__
        """ set_uniform_1iv(self, name:str, value:list) """
        pass

    def set_uniform_2f(self, name, v0, v1): # real signature unknown; restored from __doc__
        """ set_uniform_2f(self, name:str, v0:float, v1:float) """
        pass

    def set_uniform_2fv(self, name, value): # real signature unknown; restored from __doc__
        """ set_uniform_2fv(self, name:str, value:list) """
        pass

    def set_uniform_2i(self, name, v0, v1): # real signature unknown; restored from __doc__
        """ set_uniform_2i(self, name:str, v0:int, v1:int) """
        pass

    def set_uniform_2iv(self, name, value): # real signature unknown; restored from __doc__
        """ set_uniform_2iv(self, name:str, value:list) """
        pass

    def set_uniform_3f(self, name, v0, v1, v2): # real signature unknown; restored from __doc__
        """ set_uniform_3f(self, name:str, v0:float, v1:float, v2:float) """
        pass

    def set_uniform_3fv(self, name, value): # real signature unknown; restored from __doc__
        """ set_uniform_3fv(self, name:str, value:list) """
        pass

    def set_uniform_3i(self, name, v0, v1, v2): # real signature unknown; restored from __doc__
        """ set_uniform_3i(self, name:str, v0:int, v1:int, v2:int) """
        pass

    def set_uniform_3iv(self, name, value): # real signature unknown; restored from __doc__
        """ set_uniform_3iv(self, name:str, value:list) """
        pass

    def set_uniform_4f(self, name, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ set_uniform_4f(self, name:str, v0:float, v1:float, v2:float, v3:float) """
        pass

    def set_uniform_4fv(self, name, value): # real signature unknown; restored from __doc__
        """ set_uniform_4fv(self, name:str, value:list) """
        pass

    def set_uniform_4i(self, name, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ set_uniform_4i(self, name:str, v0:int, v1:int, v2:int, v3:int) """
        pass

    def set_uniform_4iv(self, name, value): # real signature unknown; restored from __doc__
        """ set_uniform_4iv(self, name:str, value:list) """
        pass

    def set_uniform_matrix_2fv(self, name, count, transpose, value): # real signature unknown; restored from __doc__
        """ set_uniform_matrix_2fv(self, name:str, count:int, transpose:bool, value:float) """
        pass

    def set_uniform_matrix_2x3fv(self, name, count, transpose, value): # real signature unknown; restored from __doc__
        """ set_uniform_matrix_2x3fv(self, name:str, count:int, transpose:bool, value:float) """
        pass

    def set_uniform_matrix_2x4fv(self, name, count, transpose, value): # real signature unknown; restored from __doc__
        """ set_uniform_matrix_2x4fv(self, name:str, count:int, transpose:bool, value:float) """
        pass

    def set_uniform_matrix_3fv(self, name, count, transpose, value): # real signature unknown; restored from __doc__
        """ set_uniform_matrix_3fv(self, name:str, count:int, transpose:bool, value:float) """
        pass

    def set_uniform_matrix_3x2fv(self, name, count, transpose, value): # real signature unknown; restored from __doc__
        """ set_uniform_matrix_3x2fv(self, name:str, count:int, transpose:bool, value:float) """
        pass

    def set_uniform_matrix_3x4fv(self, name, count, transpose, value): # real signature unknown; restored from __doc__
        """ set_uniform_matrix_3x4fv(self, name:str, count:int, transpose:bool, value:float) """
        pass

    def set_uniform_matrix_4fv(self, name, count, transpose, value): # real signature unknown; restored from __doc__
        """ set_uniform_matrix_4fv(self, name:str, count:int, transpose:bool, value:float) """
        pass

    def set_uniform_matrix_4x2fv(self, name, count, transpose, value): # real signature unknown; restored from __doc__
        """ set_uniform_matrix_4x2fv(self, name:str, count:int, transpose:bool, value:float) """
        pass

    def set_uniform_matrix_4x3fv(self, name, count, transpose, value): # real signature unknown; restored from __doc__
        """ set_uniform_matrix_4x3fv(self, name:str, count:int, transpose:bool, value:float) """
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

    def string_fragment_external_oes_get_default(self, context, version, profile): # real signature unknown; restored from __doc__
        """ string_fragment_external_oes_get_default(context:GstGL.GLContext, version:GstGL.GLSLVersion, profile:GstGL.GLSLProfile) -> str """
        return ""

    def string_fragment_get_default(self, context, version, profile): # real signature unknown; restored from __doc__
        """ string_fragment_get_default(context:GstGL.GLContext, version:GstGL.GLSLVersion, profile:GstGL.GLSLProfile) -> str """
        return ""

    def string_get_highest_precision(self, context, version, profile): # real signature unknown; restored from __doc__
        """ string_get_highest_precision(context:GstGL.GLContext, version:GstGL.GLSLVersion, profile:GstGL.GLSLProfile) -> str """
        return ""

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def use(self): # real signature unknown; restored from __doc__
        """ use(self) """
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

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f56a38baac0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(GLShader), '__module__': 'gi.repository.GstGL', '__gtype__': <GType GstGLShader (93979012478000)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_default': gi.FunctionInfo(new_default), 'string_fragment_external_oes_get_default': gi.FunctionInfo(string_fragment_external_oes_get_default), 'string_fragment_get_default': gi.FunctionInfo(string_fragment_get_default), 'string_get_highest_precision': gi.FunctionInfo(string_get_highest_precision), 'attach': gi.FunctionInfo(attach), 'attach_unlocked': gi.FunctionInfo(attach_unlocked), 'bind_attribute_location': gi.FunctionInfo(bind_attribute_location), 'bind_frag_data_location': gi.FunctionInfo(bind_frag_data_location), 'compile_attach_stage': gi.FunctionInfo(compile_attach_stage), 'detach': gi.FunctionInfo(detach), 'detach_unlocked': gi.FunctionInfo(detach_unlocked), 'get_attribute_location': gi.FunctionInfo(get_attribute_location), 'get_program_handle': gi.FunctionInfo(get_program_handle), 'is_linked': gi.FunctionInfo(is_linked), 'link': gi.FunctionInfo(link), 'release': gi.FunctionInfo(release), 'release_unlocked': gi.FunctionInfo(release_unlocked), 'set_uniform_1f': gi.FunctionInfo(set_uniform_1f), 'set_uniform_1fv': gi.FunctionInfo(set_uniform_1fv), 'set_uniform_1i': gi.FunctionInfo(set_uniform_1i), 'set_uniform_1iv': gi.FunctionInfo(set_uniform_1iv), 'set_uniform_2f': gi.FunctionInfo(set_uniform_2f), 'set_uniform_2fv': gi.FunctionInfo(set_uniform_2fv), 'set_uniform_2i': gi.FunctionInfo(set_uniform_2i), 'set_uniform_2iv': gi.FunctionInfo(set_uniform_2iv), 'set_uniform_3f': gi.FunctionInfo(set_uniform_3f), 'set_uniform_3fv': gi.FunctionInfo(set_uniform_3fv), 'set_uniform_3i': gi.FunctionInfo(set_uniform_3i), 'set_uniform_3iv': gi.FunctionInfo(set_uniform_3iv), 'set_uniform_4f': gi.FunctionInfo(set_uniform_4f), 'set_uniform_4fv': gi.FunctionInfo(set_uniform_4fv), 'set_uniform_4i': gi.FunctionInfo(set_uniform_4i), 'set_uniform_4iv': gi.FunctionInfo(set_uniform_4iv), 'set_uniform_matrix_2fv': gi.FunctionInfo(set_uniform_matrix_2fv), 'set_uniform_matrix_2x3fv': gi.FunctionInfo(set_uniform_matrix_2x3fv), 'set_uniform_matrix_2x4fv': gi.FunctionInfo(set_uniform_matrix_2x4fv), 'set_uniform_matrix_3fv': gi.FunctionInfo(set_uniform_matrix_3fv), 'set_uniform_matrix_3x2fv': gi.FunctionInfo(set_uniform_matrix_3x2fv), 'set_uniform_matrix_3x4fv': gi.FunctionInfo(set_uniform_matrix_3x4fv), 'set_uniform_matrix_4fv': gi.FunctionInfo(set_uniform_matrix_4fv), 'set_uniform_matrix_4x2fv': gi.FunctionInfo(set_uniform_matrix_4x2fv), 'set_uniform_matrix_4x3fv': gi.FunctionInfo(set_uniform_matrix_4x3fv), 'use': gi.FunctionInfo(use), 'parent': <property object at 0x7f56a3a2e950>, 'context': <property object at 0x7f56a3a2ea40>, 'priv': <property object at 0x7f56a3a2eb30>, '_padding': <property object at 0x7f56a3a2ec20>})"
    __gdoc__ = 'Object GstGLShader\n\nProperties from GstGLShader:\n  linked -> gboolean: Linked\n    Shader link status\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstGLShader (93979012478000)>'
    __info__ = ObjectInfo(GLShader)


