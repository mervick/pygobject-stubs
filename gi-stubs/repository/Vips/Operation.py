# encoding: utf-8
# module gi.repository.Vips
# from /usr/lib64/girepository-1.0/Vips-8.0.typelib
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
import gobject as __gobject


from .Object import Object

class Operation(Object):
    """
    :Constructors:
    
    ::
    
        Operation(**properties)
        new(name:str) -> Vips.Operation
    """
    def argument_isset(self, name): # real signature unknown; restored from __doc__
        """ argument_isset(self, name:str) -> bool """
        return False

    def argument_needsstring(self, name): # real signature unknown; restored from __doc__
        """ argument_needsstring(self, name:str) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def build(self): # real signature unknown; restored from __doc__
        """ build(self) -> int """
        return 0

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

    def do_build(self, *args, **kwargs): # real signature unknown
        """ build(self) -> int """
        pass

    def do_close(self, *args, **kwargs): # real signature unknown
        """ close(self) """
        pass

    def do_get_flags(self, *args, **kwargs): # real signature unknown
        """ get_flags(self) -> Vips.OperationFlags """
        pass

    def do_invalidate(self, *args, **kwargs): # real signature unknown
        """ invalidate(self) """
        pass

    def do_output_to_arg(self, *args, **kwargs): # real signature unknown
        """ output_to_arg(self, string:str) -> int """
        pass

    def do_postbuild(self, *args, **kwargs): # real signature unknown
        """ postbuild(self) -> int """
        pass

    def do_postclose(self, *args, **kwargs): # real signature unknown
        """ postclose(self) """
        pass

    def do_preclose(self, *args, **kwargs): # real signature unknown
        """ preclose(self) """
        pass

    def do_rewind(self, *args, **kwargs): # real signature unknown
        """ rewind(self) """
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

    def get_argument_flags(self, name): # real signature unknown; restored from __doc__
        """ get_argument_flags(self, name:str) -> Vips.ArgumentFlags """
        pass

    def get_argument_priority(self, name): # real signature unknown; restored from __doc__
        """ get_argument_priority(self, name:str) -> int """
        return 0

    def get_argument_to_string(self, name, arg): # real signature unknown; restored from __doc__
        """ get_argument_to_string(self, name:str, arg:str) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Vips.OperationFlags """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, gobject, property_id, value, pspec): # real signature unknown; restored from __doc__
        """ get_property(gobject:GObject.Object, property_id:int, value:GObject.Value, pspec:GObject.ParamSpec) """
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

    def install_argument(self, pspec, flags, priority, offset): # real signature unknown; restored from __doc__
        """ install_argument(self, pspec:GObject.ParamSpec, flags:Vips.ArgumentFlags, priority:int, offset:int) """
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

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def local_cb(self, gobject): # real signature unknown; restored from __doc__
        """ local_cb(self, gobject:GObject.Object) """
        pass

    def new(self, name): # real signature unknown; restored from __doc__
        """ new(name:str) -> Vips.Operation """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_string(self, object_class, p): # real signature unknown; restored from __doc__
        """ new_from_string(object_class:Vips.ObjectClass, p:str) -> Vips.Object """
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

    def print_all(self): # real signature unknown; restored from __doc__
        """ print_all() """
        pass

    def print_dump(self): # real signature unknown; restored from __doc__
        """ print_dump(self) """
        pass

    def print_name(self): # real signature unknown; restored from __doc__
        """ print_name(self) """
        pass

    def print_summary(self): # real signature unknown; restored from __doc__
        """ print_summary(self) """
        pass

    def print_summary_class(self, klass): # real signature unknown; restored from __doc__
        """ print_summary_class(klass:Vips.ObjectClass) """
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

    def rewind(self): # real signature unknown; restored from __doc__
        """ rewind(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def sanity(self): # real signature unknown; restored from __doc__
        """ sanity(self) -> bool """
        return False

    def sanity_all(self): # real signature unknown; restored from __doc__
        """ sanity_all() """
        pass

    def set_argument_from_string(self, name, value): # real signature unknown; restored from __doc__
        """ set_argument_from_string(self, name:str, value:str) -> int """
        return 0

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_from_string(self, string): # real signature unknown; restored from __doc__
        """ set_from_string(self, string:str) -> int """
        return 0

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, gobject, property_id, value, pspec): # real signature unknown; restored from __doc__
        """ set_property(gobject:GObject.Object, property_id:int, value:GObject.Value, pspec:GObject.ParamSpec) """
        pass

    def set_required(self, value): # real signature unknown; restored from __doc__
        """ set_required(self, value:str) -> int """
        return 0

    def set_static(self, static_object): # real signature unknown; restored from __doc__
        """ set_static(self, static_object:bool) """
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

    def unref_outputs(self): # real signature unknown; restored from __doc__
        """ unref_outputs(self) """
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

    argument_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    constructed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    found_hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    local_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nickname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    postclose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    preclose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    static_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f41839b41f0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Operation), '__module__': 'gi.repository.Vips', '__gtype__': <GType VipsOperation (94317410484064)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_flags': gi.FunctionInfo(get_flags), 'invalidate': gi.FunctionInfo(invalidate), 'do_get_flags': gi.VFuncInfo(get_flags), 'do_invalidate': gi.VFuncInfo(invalidate), 'parent_instance': <property object at 0x7f41868d9b80>, 'hash': <property object at 0x7f41868d9c70>, 'found_hash': <property object at 0x7f41868d9d60>, 'pixels': <property object at 0x7f41868d9e50>})"
    __gdoc__ = 'Object VipsOperation\n\nSignals from VipsOperation:\n  invalidate ()\n\nSignals from VipsObject:\n  postbuild () -> gint\n  preclose ()\n  close ()\n  postclose ()\n\nProperties from VipsObject:\n  nickname -> gchararray: Nickname\n    Class nickname\n  description -> gchararray: Description\n    Class description\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType VipsOperation (94317410484064)>'
    __info__ = ObjectInfo(Operation)


