# encoding: utf-8
# module gi.repository.BraseroBurn
# from /usr/lib64/girepository-1.0/BraseroBurn-3.1.typelib
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


class BurnSession(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        BurnSession(**properties)
        new() -> BraseroBurn.BurnSession
    """
    def add_flag(self, flags): # real signature unknown; restored from __doc__
        """ add_flag(self, flags:BraseroBurn.BurnFlag) """
        pass

    def add_track(self, new_track=None, sibling=None): # real signature unknown; restored from __doc__
        """ add_track(self, new_track:BraseroBurn.Track=None, sibling:BraseroBurn.Track=None) -> BraseroBurn.BurnResult """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_blank(self): # real signature unknown; restored from __doc__
        """ can_blank(self) -> BraseroBurn.BurnResult """
        pass

    def can_burn(self, check_flags): # real signature unknown; restored from __doc__
        """ can_burn(self, check_flags:bool) -> BraseroBurn.BurnResult """
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

    def do_get_output_format(self, *args, **kwargs): # real signature unknown
        """ get_output_format(self) -> BraseroBurn.ImageFormat """
        pass

    def do_get_output_path(self, *args, **kwargs): # real signature unknown
        """ get_output_path(self, image:str, toc:str) -> BraseroBurn.BurnResult """
        pass

    def do_set_output_image(self, *args, **kwargs): # real signature unknown
        """ set_output_image(self, format:BraseroBurn.ImageFormat, image:str, toc:str) -> BraseroBurn.BurnResult """
        pass

    def do_tag_changed(self, *args, **kwargs): # real signature unknown
        """ tag_changed(self, tag:str) """
        pass

    def do_track_added(self, *args, **kwargs): # real signature unknown
        """ track_added(self, track:BraseroBurn.Track) """
        pass

    def do_track_changed(self, *args, **kwargs): # real signature unknown
        """ track_changed(self, track:BraseroBurn.Track) """
        pass

    def do_track_removed(self, *args, **kwargs): # real signature unknown
        """ track_removed(self, track:BraseroBurn.Track, former_position:int) """
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

    def get_blank_flags(self, supported, compulsory): # real signature unknown; restored from __doc__
        """ get_blank_flags(self, supported:BraseroBurn.BurnFlag, compulsory:BraseroBurn.BurnFlag) -> BraseroBurn.BurnResult """
        pass

    def get_burn_flags(self, supported, compulsory): # real signature unknown; restored from __doc__
        """ get_burn_flags(self, supported:BraseroBurn.BurnFlag, compulsory:BraseroBurn.BurnFlag) -> BraseroBurn.BurnResult """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_output_format(self): # real signature unknown; restored from __doc__
        """ get_default_output_format(self) -> BraseroBurn.ImageFormat """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> BraseroBurn.BurnFlag """
        pass

    def get_input_type(self, type): # real signature unknown; restored from __doc__
        """ get_input_type(self, type:BraseroBurn.TrackType) -> BraseroBurn.BurnResult """
        pass

    def get_label(self): # real signature unknown; restored from __doc__
        """ get_label(self) -> str """
        return ""

    def get_output(self): # real signature unknown; restored from __doc__
        """ get_output(self) -> BraseroBurn.BurnResult, image:str, toc:str """
        pass

    def get_output_format(self): # real signature unknown; restored from __doc__
        """ get_output_format(self) -> BraseroBurn.ImageFormat """
        pass

    def get_output_type(self, output): # real signature unknown; restored from __doc__
        """ get_output_type(self, output:BraseroBurn.TrackType) -> BraseroBurn.BurnResult """
        pass

    def get_possible_output_formats(self, formats): # real signature unknown; restored from __doc__
        """ get_possible_output_formats(self, formats:BraseroBurn.ImageFormat) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rate(self): # real signature unknown; restored from __doc__
        """ get_rate(self) -> int """
        return 0

    def get_size(self, blocks, bytes): # real signature unknown; restored from __doc__
        """ get_size(self, blocks:int, bytes:int) -> BraseroBurn.BurnResult """
        pass

    def get_status(self, status): # real signature unknown; restored from __doc__
        """ get_status(self, status:BraseroBurn.Status) -> BraseroBurn.BurnResult """
        pass

    def get_strict_support(self): # real signature unknown; restored from __doc__
        """ get_strict_support(self) -> bool """
        return False

    def get_tmpdir(self): # real signature unknown; restored from __doc__
        """ get_tmpdir(self) -> str """
        return ""

    def get_tracks(self): # real signature unknown; restored from __doc__
        """ get_tracks(self) -> list """
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

    def input_supported(self, input, check_flags): # real signature unknown; restored from __doc__
        """ input_supported(self, input:BraseroBurn.TrackType, check_flags:bool) -> BraseroBurn.BurnResult """
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

    def move_track(self, track, sibling=None): # real signature unknown; restored from __doc__
        """ move_track(self, track:BraseroBurn.Track, sibling:BraseroBurn.Track=None) -> BraseroBurn.BurnResult """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> BraseroBurn.BurnSession """
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

    def output_supported(self, output): # real signature unknown; restored from __doc__
        """ output_supported(self, output:BraseroBurn.TrackType) -> BraseroBurn.BurnResult """
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

    def remove_flag(self, flags): # real signature unknown; restored from __doc__
        """ remove_flag(self, flags:BraseroBurn.BurnFlag) """
        pass

    def remove_track(self, track): # real signature unknown; restored from __doc__
        """ remove_track(self, track:BraseroBurn.Track) -> BraseroBurn.BurnResult """
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

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:BraseroBurn.BurnFlag) """
        pass

    def set_image_output_format(self, format): # real signature unknown; restored from __doc__
        """ set_image_output_format(self, format:BraseroBurn.ImageFormat) -> BraseroBurn.BurnResult """
        pass

    def set_image_output_full(self, format, image=None, toc=None): # real signature unknown; restored from __doc__
        """ set_image_output_full(self, format:BraseroBurn.ImageFormat, image:str=None, toc:str=None) -> BraseroBurn.BurnResult """
        pass

    def set_label(self, label=None): # real signature unknown; restored from __doc__
        """ set_label(self, label:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_rate(self, rate): # real signature unknown; restored from __doc__
        """ set_rate(self, rate:int) -> BraseroBurn.BurnResult """
        pass

    def set_strict_support(self, strict_check): # real signature unknown; restored from __doc__
        """ set_strict_support(self, strict_check:bool) """
        pass

    def set_tmpdir(self, path): # real signature unknown; restored from __doc__
        """ set_tmpdir(self, path:str) -> BraseroBurn.BurnResult """
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

    def tag_add(self, tag, value): # real signature unknown; restored from __doc__
        """ tag_add(self, tag:str, value:GObject.Value) -> BraseroBurn.BurnResult """
        pass

    def tag_add_int(self, tag, value): # real signature unknown; restored from __doc__
        """ tag_add_int(self, tag:str, value:int) -> BraseroBurn.BurnResult """
        pass

    def tag_lookup(self, tag, value): # real signature unknown; restored from __doc__
        """ tag_lookup(self, tag:str, value:GObject.Value) -> BraseroBurn.BurnResult """
        pass

    def tag_lookup_int(self, tag): # real signature unknown; restored from __doc__
        """ tag_lookup_int(self, tag:str) -> int """
        return 0

    def tag_remove(self, tag): # real signature unknown; restored from __doc__
        """ tag_remove(self, tag:str) -> BraseroBurn.BurnResult """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fdd613b4250>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(BurnSession), '__module__': 'gi.repository.BraseroBurn', '__gtype__': <GType BraseroBurnSession (94320849280944)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_flag': gi.FunctionInfo(add_flag), 'add_track': gi.FunctionInfo(add_track), 'can_blank': gi.FunctionInfo(can_blank), 'can_burn': gi.FunctionInfo(can_burn), 'get_blank_flags': gi.FunctionInfo(get_blank_flags), 'get_burn_flags': gi.FunctionInfo(get_burn_flags), 'get_default_output_format': gi.FunctionInfo(get_default_output_format), 'get_flags': gi.FunctionInfo(get_flags), 'get_input_type': gi.FunctionInfo(get_input_type), 'get_label': gi.FunctionInfo(get_label), 'get_output': gi.FunctionInfo(get_output), 'get_output_format': gi.FunctionInfo(get_output_format), 'get_output_type': gi.FunctionInfo(get_output_type), 'get_possible_output_formats': gi.FunctionInfo(get_possible_output_formats), 'get_rate': gi.FunctionInfo(get_rate), 'get_size': gi.FunctionInfo(get_size), 'get_status': gi.FunctionInfo(get_status), 'get_strict_support': gi.FunctionInfo(get_strict_support), 'get_tmpdir': gi.FunctionInfo(get_tmpdir), 'get_tracks': gi.FunctionInfo(get_tracks), 'input_supported': gi.FunctionInfo(input_supported), 'move_track': gi.FunctionInfo(move_track), 'output_supported': gi.FunctionInfo(output_supported), 'remove_flag': gi.FunctionInfo(remove_flag), 'remove_track': gi.FunctionInfo(remove_track), 'set_flags': gi.FunctionInfo(set_flags), 'set_image_output_format': gi.FunctionInfo(set_image_output_format), 'set_image_output_full': gi.FunctionInfo(set_image_output_full), 'set_label': gi.FunctionInfo(set_label), 'set_rate': gi.FunctionInfo(set_rate), 'set_strict_support': gi.FunctionInfo(set_strict_support), 'set_tmpdir': gi.FunctionInfo(set_tmpdir), 'tag_add': gi.FunctionInfo(tag_add), 'tag_add_int': gi.FunctionInfo(tag_add_int), 'tag_lookup': gi.FunctionInfo(tag_lookup), 'tag_lookup_int': gi.FunctionInfo(tag_lookup_int), 'tag_remove': gi.FunctionInfo(tag_remove), 'do_get_output_format': gi.VFuncInfo(get_output_format), 'do_get_output_path': gi.VFuncInfo(get_output_path), 'do_set_output_image': gi.VFuncInfo(set_output_image), 'do_tag_changed': gi.VFuncInfo(tag_changed), 'do_track_added': gi.VFuncInfo(track_added), 'do_track_changed': gi.VFuncInfo(track_changed), 'do_track_removed': gi.VFuncInfo(track_removed), 'parent': <property object at 0x7fdd61352ae0>})"
    __gdoc__ = 'Object BraseroBurnSession\n\nSignals from BraseroBurnSession:\n  output-changed (BraseroMedium)\n  track-added (BraseroTrack)\n  track-removed (BraseroTrack, guint)\n  track-changed (BraseroTrack)\n  tag-changed (gchararray)\n\nProperties from BraseroBurnSession:\n  tmpdir -> gchararray: Temporary directory\n    The path to the temporary directory\n  speed -> gint64: Burning speed\n    The speed at which a disc should be burned\n  flags -> gint: Burning flags\n    The flags that will be used to burn\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType BraseroBurnSession (94320849280944)>'
    __info__ = ObjectInfo(BurnSession)


