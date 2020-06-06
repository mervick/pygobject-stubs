# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .DataWrapper import DataWrapper

class Multipart(DataWrapper):
    """
    :Constructors:
    
    ::
    
        Multipart(**properties)
        new() -> Camel.Multipart
    """
    def add_part(self, part): # real signature unknown; restored from __doc__
        """ add_part(self, part:Camel.MimePart) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def calculate_decoded_size_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ calculate_decoded_size_sync(self, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def calculate_size_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ calculate_size_sync(self, cancellable:Gio.Cancellable=None) -> int """
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

    def construct_from_input_stream(self, input_stream, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ construct_from_input_stream(self, input_stream:Gio.InputStream, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def construct_from_input_stream_finish(self, result): # real signature unknown; restored from __doc__
        """ construct_from_input_stream_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def construct_from_input_stream_sync(self, input_stream, cancellable=None): # real signature unknown; restored from __doc__
        """ construct_from_input_stream_sync(self, input_stream:Gio.InputStream, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def construct_from_parser(self, parser): # real signature unknown; restored from __doc__
        """ construct_from_parser(self, parser:Camel.MimeParser) -> int """
        return 0

    def construct_from_stream(self, stream, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ construct_from_stream(self, stream:Camel.Stream, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def construct_from_stream_finish(self, result): # real signature unknown; restored from __doc__
        """ construct_from_stream_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def construct_from_stream_sync(self, stream, cancellable=None): # real signature unknown; restored from __doc__
        """ construct_from_stream_sync(self, stream:Camel.Stream, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def decode_to_output_stream(self, output_stream, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ decode_to_output_stream(self, output_stream:Gio.OutputStream, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def decode_to_output_stream_finish(self, result): # real signature unknown; restored from __doc__
        """ decode_to_output_stream_finish(self, result:Gio.AsyncResult) -> int """
        return 0

    def decode_to_output_stream_sync(self, output_stream, cancellable=None): # real signature unknown; restored from __doc__
        """ decode_to_output_stream_sync(self, output_stream:Gio.OutputStream, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def decode_to_stream(self, stream, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ decode_to_stream(self, stream:Camel.Stream, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def decode_to_stream_finish(self, result): # real signature unknown; restored from __doc__
        """ decode_to_stream_finish(self, result:Gio.AsyncResult) -> int """
        return 0

    def decode_to_stream_sync(self, stream, cancellable=None): # real signature unknown; restored from __doc__
        """ decode_to_stream_sync(self, stream:Camel.Stream, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_add_part(self, *args, **kwargs): # real signature unknown
        """ add_part(self, part:Camel.MimePart) """
        pass

    def do_construct_from_input_stream_sync(self, *args, **kwargs): # real signature unknown
        """ construct_from_input_stream_sync(self, input_stream:Gio.InputStream, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_construct_from_parser(self, *args, **kwargs): # real signature unknown
        """ construct_from_parser(self, parser:Camel.MimeParser) -> int """
        pass

    def do_construct_from_stream_sync(self, *args, **kwargs): # real signature unknown
        """ construct_from_stream_sync(self, stream:Camel.Stream, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_decode_to_output_stream_sync(self, *args, **kwargs): # real signature unknown
        """ decode_to_output_stream_sync(self, output_stream:Gio.OutputStream, cancellable:Gio.Cancellable=None) -> int """
        pass

    def do_decode_to_stream_sync(self, *args, **kwargs): # real signature unknown
        """ decode_to_stream_sync(self, stream:Camel.Stream, cancellable:Gio.Cancellable=None) -> int """
        pass

    def do_get_boundary(self, *args, **kwargs): # real signature unknown
        """ get_boundary(self) -> str """
        pass

    def do_get_mime_type(self, *args, **kwargs): # real signature unknown
        """ get_mime_type(self) -> str """
        pass

    def do_get_mime_type_field(self, *args, **kwargs): # real signature unknown
        """ get_mime_type_field(self) -> Camel.ContentType """
        pass

    def do_get_number(self, *args, **kwargs): # real signature unknown
        """ get_number(self) -> int """
        pass

    def do_get_part(self, *args, **kwargs): # real signature unknown
        """ get_part(self, index:int) -> Camel.MimePart """
        pass

    def do_is_offline(self, *args, **kwargs): # real signature unknown
        """ is_offline(self) -> bool """
        pass

    def do_set_boundary(self, *args, **kwargs): # real signature unknown
        """ set_boundary(self, boundary:str=None) """
        pass

    def do_set_mime_type(self, *args, **kwargs): # real signature unknown
        """ set_mime_type(self, mime_type:str) """
        pass

    def do_set_mime_type_field(self, *args, **kwargs): # real signature unknown
        """ set_mime_type_field(self, mime_type:Camel.ContentType=None) """
        pass

    def do_write_to_output_stream_sync(self, *args, **kwargs): # real signature unknown
        """ write_to_output_stream_sync(self, output_stream:Gio.OutputStream, cancellable:Gio.Cancellable=None) -> int """
        pass

    def do_write_to_stream_sync(self, *args, **kwargs): # real signature unknown
        """ write_to_stream_sync(self, stream:Camel.Stream, cancellable:Gio.Cancellable=None) -> int """
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

    def get_boundary(self): # real signature unknown; restored from __doc__
        """ get_boundary(self) -> str """
        return ""

    def get_byte_array(self): # real signature unknown; restored from __doc__
        """ get_byte_array(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_encoding(self): # real signature unknown; restored from __doc__
        """ get_encoding(self) -> Camel.TransferEncoding """
        pass

    def get_mime_type(self): # real signature unknown; restored from __doc__
        """ get_mime_type(self) -> str """
        return ""

    def get_mime_type_field(self): # real signature unknown; restored from __doc__
        """ get_mime_type_field(self) -> Camel.ContentType """
        pass

    def get_number(self): # real signature unknown; restored from __doc__
        """ get_number(self) -> int """
        return 0

    def get_part(self, index): # real signature unknown; restored from __doc__
        """ get_part(self, index:int) -> Camel.MimePart """
        pass

    def get_postface(self): # real signature unknown; restored from __doc__
        """ get_postface(self) -> str """
        return ""

    def get_preface(self): # real signature unknown; restored from __doc__
        """ get_preface(self) -> str """
        return ""

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

    def is_offline(self): # real signature unknown; restored from __doc__
        """ is_offline(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Camel.Multipart """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
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

    def set_boundary(self, boundary=None): # real signature unknown; restored from __doc__
        """ set_boundary(self, boundary:str=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_encoding(self, encoding): # real signature unknown; restored from __doc__
        """ set_encoding(self, encoding:Camel.TransferEncoding) """
        pass

    def set_mime_type(self, mime_type): # real signature unknown; restored from __doc__
        """ set_mime_type(self, mime_type:str) """
        pass

    def set_mime_type_field(self, mime_type=None): # real signature unknown; restored from __doc__
        """ set_mime_type_field(self, mime_type:Camel.ContentType=None) """
        pass

    def set_offline(self, offline): # real signature unknown; restored from __doc__
        """ set_offline(self, offline:bool) """
        pass

    def set_postface(self, postface): # real signature unknown; restored from __doc__
        """ set_postface(self, postface:str) """
        pass

    def set_preface(self, preface): # real signature unknown; restored from __doc__
        """ set_preface(self, preface:str) """
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

    def take_mime_type_field(self, mime_type=None): # real signature unknown; restored from __doc__
        """ take_mime_type_field(self, mime_type:Camel.ContentType=None) """
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

    def write_to_output_stream(self, output_stream, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ write_to_output_stream(self, output_stream:Gio.OutputStream, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def write_to_output_stream_finish(self, result): # real signature unknown; restored from __doc__
        """ write_to_output_stream_finish(self, result:Gio.AsyncResult) -> int """
        return 0

    def write_to_output_stream_sync(self, output_stream, cancellable=None): # real signature unknown; restored from __doc__
        """ write_to_output_stream_sync(self, output_stream:Gio.OutputStream, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def write_to_stream(self, stream, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ write_to_stream(self, stream:Camel.Stream, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def write_to_stream_finish(self, result): # real signature unknown; restored from __doc__
        """ write_to_stream_finish(self, result:Gio.AsyncResult) -> int """
        return 0

    def write_to_stream_sync(self, stream, cancellable=None): # real signature unknown; restored from __doc__
        """ write_to_stream_sync(self, stream:Camel.Stream, cancellable:Gio.Cancellable=None) -> int """
        return 0

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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f7b34b5d5e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Multipart), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelMultipart (94124524008304)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_part': gi.FunctionInfo(add_part), 'construct_from_parser': gi.FunctionInfo(construct_from_parser), 'get_boundary': gi.FunctionInfo(get_boundary), 'get_number': gi.FunctionInfo(get_number), 'get_part': gi.FunctionInfo(get_part), 'get_postface': gi.FunctionInfo(get_postface), 'get_preface': gi.FunctionInfo(get_preface), 'set_boundary': gi.FunctionInfo(set_boundary), 'set_postface': gi.FunctionInfo(set_postface), 'set_preface': gi.FunctionInfo(set_preface), 'do_add_part': gi.VFuncInfo(add_part), 'do_construct_from_parser': gi.VFuncInfo(construct_from_parser), 'do_get_boundary': gi.VFuncInfo(get_boundary), 'do_get_number': gi.VFuncInfo(get_number), 'do_get_part': gi.VFuncInfo(get_part), 'do_set_boundary': gi.VFuncInfo(set_boundary), 'parent': <property object at 0x7f7b34f9a680>, 'priv': <property object at 0x7f7b34f9a7c0>})"
    __gdoc__ = 'Object CamelMultipart\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CamelMultipart (94124524008304)>'
    __info__ = ObjectInfo(Multipart)


