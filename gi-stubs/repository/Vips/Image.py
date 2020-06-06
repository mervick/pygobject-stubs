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

class Image(Object):
    """
    :Constructors:
    
    ::
    
        Image(**properties)
        matrix_from_array(width:int, height:int, array:list) -> Vips.Image
        memory() -> Vips.Image
        new() -> Vips.Image
        new_from_file_RW(filename:str) -> Vips.Image
        new_from_file_raw(filename:str, xsize:int, ysize:int, bands:int, offset:int) -> Vips.Image
        new_from_image(image:Vips.Image, c:list) -> Vips.Image
        new_from_image1(image:Vips.Image, c:float) -> Vips.Image
        new_from_memory(data:list, width:int, height:int, bands:int, format:Vips.BandFormat) -> Vips.Image
        new_from_memory_copy(data:list, width:int, height:int, bands:int, format:Vips.BandFormat) -> Vips.Image
        new_matrix(width:int, height:int) -> Vips.Image
        new_matrix_from_array(width:int, height:int, array:list) -> Vips.Image
        new_memory() -> Vips.Image
        new_temp_file(format:str) -> Vips.Image
    """
    def argument_isset(self, name): # real signature unknown; restored from __doc__
        """ argument_isset(self, name:str) -> bool """
        return False

    def argument_needsstring(self, name): # real signature unknown; restored from __doc__
        """ argument_needsstring(self, name:str) -> bool """
        return False

    def autorot_remove_angle(self): # real signature unknown; restored from __doc__
        """ autorot_remove_angle(self) """
        pass

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

    def do_eval(self, *args, **kwargs): # real signature unknown
        """ eval(self, progress:Vips.Progress) """
        pass

    def do_invalidate(self, *args, **kwargs): # real signature unknown
        """ invalidate(self) """
        pass

    def do_minimise(self, *args, **kwargs): # real signature unknown
        """ minimise(self) """
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

    def do_posteval(self, *args, **kwargs): # real signature unknown
        """ posteval(self, progress:Vips.Progress) """
        pass

    def do_preclose(self, *args, **kwargs): # real signature unknown
        """ preclose(self) """
        pass

    def do_preeval(self, *args, **kwargs): # real signature unknown
        """ preeval(self, progress:Vips.Progress) """
        pass

    def do_rewind(self, *args, **kwargs): # real signature unknown
        """ rewind(self) """
        pass

    def do_written(self, *args, **kwargs): # real signature unknown
        """ written(self, result:int) """
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

    def foreign_load_invalidate(self): # real signature unknown; restored from __doc__
        """ foreign_load_invalidate(self) """
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

    def icc_ac2rc(self, profile_filename): # real signature unknown; restored from __doc__
        """ icc_ac2rc(self, profile_filename:str) -> int, out:Vips.Image """
        return 0

    def image_copy_memory(self): # real signature unknown; restored from __doc__
        """ image_copy_memory(self) -> Vips.Image """
        pass

    def image_decode(self): # real signature unknown; restored from __doc__
        """ image_decode(self) -> int, out:Vips.Image """
        return 0

    def image_decode_predict(self): # real signature unknown; restored from __doc__
        """ image_decode_predict(self) -> int, bands:int, format:Vips.BandFormat """
        return 0

    def image_encode(self, coding): # real signature unknown; restored from __doc__
        """ image_encode(self, coding:Vips.Coding) -> int, out:Vips.Image """
        return 0

    def image_get(self, name): # real signature unknown; restored from __doc__
        """ image_get(self, name:str) -> value_copy:GObject.Value """
        pass

    def image_get_area(self, name): # real signature unknown; restored from __doc__
        """ image_get_area(self, name:str) -> int, data """
        return 0

    def image_get_as_string(self, name, out): # real signature unknown; restored from __doc__
        """ image_get_as_string(self, name:str, out:str) -> int """
        return 0

    def image_get_bands(self): # real signature unknown; restored from __doc__
        """ image_get_bands(self) -> int """
        return 0

    def image_get_blob(self, name, data=None, length): # real signature unknown; restored from __doc__
        """ image_get_blob(self, name:str, data=None, length:int) -> int """
        return 0

    def image_get_coding(self): # real signature unknown; restored from __doc__
        """ image_get_coding(self) -> Vips.Coding """
        pass

    def image_get_data(self): # real signature unknown; restored from __doc__
        """ image_get_data(self) """
        pass

    def image_get_double(self, name, out): # real signature unknown; restored from __doc__
        """ image_get_double(self, name:str, out:float) -> int """
        return 0

    def image_get_fields(self): # real signature unknown; restored from __doc__
        """ image_get_fields(self) -> list """
        return []

    def image_get_filename(self): # real signature unknown; restored from __doc__
        """ image_get_filename(self) -> str """
        return ""

    def image_get_format(self): # real signature unknown; restored from __doc__
        """ image_get_format(self) -> Vips.BandFormat """
        pass

    def image_get_height(self): # real signature unknown; restored from __doc__
        """ image_get_height(self) -> int """
        return 0

    def image_get_history(self): # real signature unknown; restored from __doc__
        """ image_get_history(self) -> str """
        return ""

    def image_get_image(self, name, out): # real signature unknown; restored from __doc__
        """ image_get_image(self, name:str, out:Vips.Image) -> int """
        return 0

    def image_get_int(self, name): # real signature unknown; restored from __doc__
        """ image_get_int(self, name:str) -> int, out:int """
        return 0

    def image_get_interpretation(self): # real signature unknown; restored from __doc__
        """ image_get_interpretation(self) -> Vips.Interpretation """
        pass

    def image_get_mode(self): # real signature unknown; restored from __doc__
        """ image_get_mode(self) -> str """
        return ""

    def image_get_n_pages(self): # real signature unknown; restored from __doc__
        """ image_get_n_pages(self) -> int """
        return 0

    def image_get_offset(self): # real signature unknown; restored from __doc__
        """ image_get_offset(self) -> float """
        return 0.0

    def image_get_page_height(self): # real signature unknown; restored from __doc__
        """ image_get_page_height(self) -> int """
        return 0

    def image_get_scale(self): # real signature unknown; restored from __doc__
        """ image_get_scale(self) -> float """
        return 0.0

    def image_get_string(self, name, out): # real signature unknown; restored from __doc__
        """ image_get_string(self, name:str, out:str) -> int """
        return 0

    def image_get_typeof(self, name): # real signature unknown; restored from __doc__
        """ image_get_typeof(self, name:str) -> GType """
        pass

    def image_get_width(self): # real signature unknown; restored from __doc__
        """ image_get_width(self) -> int """
        return 0

    def image_get_xoffset(self): # real signature unknown; restored from __doc__
        """ image_get_xoffset(self) -> int """
        return 0

    def image_get_xres(self): # real signature unknown; restored from __doc__
        """ image_get_xres(self) -> float """
        return 0.0

    def image_get_yoffset(self): # real signature unknown; restored from __doc__
        """ image_get_yoffset(self) -> int """
        return 0

    def image_get_yres(self): # real signature unknown; restored from __doc__
        """ image_get_yres(self) -> float """
        return 0.0

    def image_guess_format(self): # real signature unknown; restored from __doc__
        """ image_guess_format(self) -> Vips.BandFormat """
        pass

    def image_guess_interpretation(self): # real signature unknown; restored from __doc__
        """ image_guess_interpretation(self) -> Vips.Interpretation """
        pass

    def image_hasalpha(self): # real signature unknown; restored from __doc__
        """ image_hasalpha(self) -> bool """
        return False

    def image_history_args(self, name, argv): # real signature unknown; restored from __doc__
        """ image_history_args(self, name:str, argv:list) -> int """
        return 0

    def image_init_fields(self, xsize, ysize, bands, format, coding, interpretation, xres, yres): # real signature unknown; restored from __doc__
        """ image_init_fields(self, xsize:int, ysize:int, bands:int, format:Vips.BandFormat, coding:Vips.Coding, interpretation:Vips.Interpretation, xres:float, yres:float) """
        pass

    def image_inplace(self): # real signature unknown; restored from __doc__
        """ image_inplace(self) -> int """
        return 0

    def image_invalidate_all(self): # real signature unknown; restored from __doc__
        """ image_invalidate_all(self) """
        pass

    def image_isfile(self): # real signature unknown; restored from __doc__
        """ image_isfile(self) -> bool """
        return False

    def image_iskilled(self): # real signature unknown; restored from __doc__
        """ image_iskilled(self) -> bool """
        return False

    def image_isMSBfirst(self): # real signature unknown; restored from __doc__
        """ image_isMSBfirst(self) -> bool """
        return False

    def image_ispartial(self): # real signature unknown; restored from __doc__
        """ image_ispartial(self) -> bool """
        return False

    def image_map(self, fn=None, a=None): # real signature unknown; restored from __doc__
        """ image_map(self, fn:Vips.ImageMapFn=None, a=None) """
        pass

    def image_minimise_all(self): # real signature unknown; restored from __doc__
        """ image_minimise_all(self) """
        pass

    def image_pio_input(self): # real signature unknown; restored from __doc__
        """ image_pio_input(self) -> int """
        return 0

    def image_pio_output(self): # real signature unknown; restored from __doc__
        """ image_pio_output(self) -> int """
        return 0

    def image_print_field(self, field): # real signature unknown; restored from __doc__
        """ image_print_field(self, field:str) """
        pass

    def image_remove(self, name): # real signature unknown; restored from __doc__
        """ image_remove(self, name:str) -> bool """
        return False

    def image_set(self, name, value): # real signature unknown; restored from __doc__
        """ image_set(self, name:str, value:GObject.Value) """
        pass

    def image_set_area(self, name, free_fn, data=None): # real signature unknown; restored from __doc__
        """ image_set_area(self, name:str, free_fn:Vips.CallbackFn, data=None) """
        pass

    def image_set_blob(self, name, free_fn, data=None, length): # real signature unknown; restored from __doc__
        """ image_set_blob(self, name:str, free_fn:Vips.CallbackFn, data=None, length:int) """
        pass

    def image_set_blob_copy(self, name, data=None, length): # real signature unknown; restored from __doc__
        """ image_set_blob_copy(self, name:str, data=None, length:int) """
        pass

    def image_set_delete_on_close(self, delete_on_close): # real signature unknown; restored from __doc__
        """ image_set_delete_on_close(self, delete_on_close:bool) """
        pass

    def image_set_double(self, name, d): # real signature unknown; restored from __doc__
        """ image_set_double(self, name:str, d:float) """
        pass

    def image_set_image(self, name, im): # real signature unknown; restored from __doc__
        """ image_set_image(self, name:str, im:Vips.Image) """
        pass

    def image_set_int(self, name, i): # real signature unknown; restored from __doc__
        """ image_set_int(self, name:str, i:int) """
        pass

    def image_set_kill(self, kill): # real signature unknown; restored from __doc__
        """ image_set_kill(self, kill:bool) """
        pass

    def image_set_progress(self, progress): # real signature unknown; restored from __doc__
        """ image_set_progress(self, progress:bool) """
        pass

    def image_set_string(self, name, p_str): # real signature unknown; restored from __doc__
        """ image_set_string(self, name:str, str:str) """
        pass

    def image_wio_input(self): # real signature unknown; restored from __doc__
        """ image_wio_input(self) -> int """
        return 0

    def image_write(self): # real signature unknown; restored from __doc__
        """ image_write(self) -> int, out:Vips.Image """
        return 0

    def image_write_line(self, ypos, linebuffer): # real signature unknown; restored from __doc__
        """ image_write_line(self, ypos:int, linebuffer:int) -> int """
        return 0

    def image_write_prepare(self): # real signature unknown; restored from __doc__
        """ image_write_prepare(self) -> int """
        return 0

    def image_write_to_memory(self): # real signature unknown; restored from __doc__
        """ image_write_to_memory(self) -> list, size:int """
        return []

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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def local_cb(self, gobject): # real signature unknown; restored from __doc__
        """ local_cb(self, gobject:GObject.Object) """
        pass

    def matrix_from_array(self, width, height, array): # real signature unknown; restored from __doc__
        """ matrix_from_array(width:int, height:int, array:list) -> Vips.Image """
        pass

    def memory(self): # real signature unknown; restored from __doc__
        """ memory() -> Vips.Image """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Vips.Image """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_file_raw(self, filename, xsize, ysize, bands, offset): # real signature unknown; restored from __doc__
        """ new_from_file_raw(filename:str, xsize:int, ysize:int, bands:int, offset:int) -> Vips.Image """
        pass

    def new_from_file_RW(self, filename): # real signature unknown; restored from __doc__
        """ new_from_file_RW(filename:str) -> Vips.Image """
        pass

    def new_from_image(self, image, c): # real signature unknown; restored from __doc__
        """ new_from_image(image:Vips.Image, c:list) -> Vips.Image """
        pass

    def new_from_image1(self, image, c): # real signature unknown; restored from __doc__
        """ new_from_image1(image:Vips.Image, c:float) -> Vips.Image """
        pass

    def new_from_memory(self, data, width, height, bands, format): # real signature unknown; restored from __doc__
        """ new_from_memory(data:list, width:int, height:int, bands:int, format:Vips.BandFormat) -> Vips.Image """
        pass

    def new_from_memory_copy(self, data, width, height, bands, format): # real signature unknown; restored from __doc__
        """ new_from_memory_copy(data:list, width:int, height:int, bands:int, format:Vips.BandFormat) -> Vips.Image """
        pass

    def new_from_string(self, object_class, p): # real signature unknown; restored from __doc__
        """ new_from_string(object_class:Vips.ObjectClass, p:str) -> Vips.Object """
        pass

    def new_matrix(self, width, height): # real signature unknown; restored from __doc__
        """ new_matrix(width:int, height:int) -> Vips.Image """
        pass

    def new_matrix_from_array(self, width, height, array): # real signature unknown; restored from __doc__
        """ new_matrix_from_array(width:int, height:int, array:list) -> Vips.Image """
        pass

    def new_memory(self): # real signature unknown; restored from __doc__
        """ new_memory() -> Vips.Image """
        pass

    def new_temp_file(self, format): # real signature unknown; restored from __doc__
        """ new_temp_file(format:str) -> Vips.Image """
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

    def reorder_margin_hint(self, margin): # real signature unknown; restored from __doc__
        """ reorder_margin_hint(self, margin:int) """
        pass

    def reorder_prepare_many(self, regions, r): # real signature unknown; restored from __doc__
        """ reorder_prepare_many(self, regions:list, r:Vips.Rect) -> int """
        return 0

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

    BandFmt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Bands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    baseaddr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Bbits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    client1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    client2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Coding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    constructed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_on_close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_on_close_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dhint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    downstream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generate_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hint_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Hist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    history_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kill = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    local_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    magic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    meta_traverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nickname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    postclose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    preclose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    progress_signal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    regions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sizeof_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sslock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    static_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    upstream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    windows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Xoffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Xres = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Xres_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Xsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Yoffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Yres = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Yres_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Ysize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f4183986bb0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Image), '__module__': 'gi.repository.Vips', '__gtype__': <GType VipsImage (94317410513712)>, '__doc__': None, '__gsignals__': {}, 'matrix_from_array': gi.FunctionInfo(matrix_from_array), 'memory': gi.FunctionInfo(memory), 'new': gi.FunctionInfo(new), 'new_from_file_RW': gi.FunctionInfo(new_from_file_RW), 'new_from_file_raw': gi.FunctionInfo(new_from_file_raw), 'new_from_image': gi.FunctionInfo(new_from_image), 'new_from_image1': gi.FunctionInfo(new_from_image1), 'new_from_memory': gi.FunctionInfo(new_from_memory), 'new_from_memory_copy': gi.FunctionInfo(new_from_memory_copy), 'new_matrix': gi.FunctionInfo(new_matrix), 'new_matrix_from_array': gi.FunctionInfo(new_matrix_from_array), 'new_memory': gi.FunctionInfo(new_memory), 'new_temp_file': gi.FunctionInfo(new_temp_file), 'autorot_remove_angle': gi.FunctionInfo(autorot_remove_angle), 'foreign_load_invalidate': gi.FunctionInfo(foreign_load_invalidate), 'icc_ac2rc': gi.FunctionInfo(icc_ac2rc), 'image_copy_memory': gi.FunctionInfo(image_copy_memory), 'image_decode': gi.FunctionInfo(image_decode), 'image_decode_predict': gi.FunctionInfo(image_decode_predict), 'image_encode': gi.FunctionInfo(image_encode), 'image_get': gi.FunctionInfo(image_get), 'image_get_area': gi.FunctionInfo(image_get_area), 'image_get_as_string': gi.FunctionInfo(image_get_as_string), 'image_get_bands': gi.FunctionInfo(image_get_bands), 'image_get_blob': gi.FunctionInfo(image_get_blob), 'image_get_coding': gi.FunctionInfo(image_get_coding), 'image_get_data': gi.FunctionInfo(image_get_data), 'image_get_double': gi.FunctionInfo(image_get_double), 'image_get_fields': gi.FunctionInfo(image_get_fields), 'image_get_filename': gi.FunctionInfo(image_get_filename), 'image_get_format': gi.FunctionInfo(image_get_format), 'image_get_height': gi.FunctionInfo(image_get_height), 'image_get_history': gi.FunctionInfo(image_get_history), 'image_get_image': gi.FunctionInfo(image_get_image), 'image_get_int': gi.FunctionInfo(image_get_int), 'image_get_interpretation': gi.FunctionInfo(image_get_interpretation), 'image_get_mode': gi.FunctionInfo(image_get_mode), 'image_get_n_pages': gi.FunctionInfo(image_get_n_pages), 'image_get_offset': gi.FunctionInfo(image_get_offset), 'image_get_page_height': gi.FunctionInfo(image_get_page_height), 'image_get_scale': gi.FunctionInfo(image_get_scale), 'image_get_string': gi.FunctionInfo(image_get_string), 'image_get_typeof': gi.FunctionInfo(image_get_typeof), 'image_get_width': gi.FunctionInfo(image_get_width), 'image_get_xoffset': gi.FunctionInfo(image_get_xoffset), 'image_get_xres': gi.FunctionInfo(image_get_xres), 'image_get_yoffset': gi.FunctionInfo(image_get_yoffset), 'image_get_yres': gi.FunctionInfo(image_get_yres), 'image_guess_format': gi.FunctionInfo(image_guess_format), 'image_guess_interpretation': gi.FunctionInfo(image_guess_interpretation), 'image_hasalpha': gi.FunctionInfo(image_hasalpha), 'image_history_args': gi.FunctionInfo(image_history_args), 'image_init_fields': gi.FunctionInfo(image_init_fields), 'image_inplace': gi.FunctionInfo(image_inplace), 'image_invalidate_all': gi.FunctionInfo(image_invalidate_all), 'image_isMSBfirst': gi.FunctionInfo(image_isMSBfirst), 'image_isfile': gi.FunctionInfo(image_isfile), 'image_iskilled': gi.FunctionInfo(image_iskilled), 'image_ispartial': gi.FunctionInfo(image_ispartial), 'image_map': gi.FunctionInfo(image_map), 'image_minimise_all': gi.FunctionInfo(image_minimise_all), 'image_pio_input': gi.FunctionInfo(image_pio_input), 'image_pio_output': gi.FunctionInfo(image_pio_output), 'image_print_field': gi.FunctionInfo(image_print_field), 'image_remove': gi.FunctionInfo(image_remove), 'image_set': gi.FunctionInfo(image_set), 'image_set_area': gi.FunctionInfo(image_set_area), 'image_set_blob': gi.FunctionInfo(image_set_blob), 'image_set_blob_copy': gi.FunctionInfo(image_set_blob_copy), 'image_set_delete_on_close': gi.FunctionInfo(image_set_delete_on_close), 'image_set_double': gi.FunctionInfo(image_set_double), 'image_set_image': gi.FunctionInfo(image_set_image), 'image_set_int': gi.FunctionInfo(image_set_int), 'image_set_kill': gi.FunctionInfo(image_set_kill), 'image_set_progress': gi.FunctionInfo(image_set_progress), 'image_set_string': gi.FunctionInfo(image_set_string), 'image_wio_input': gi.FunctionInfo(image_wio_input), 'image_write': gi.FunctionInfo(image_write), 'image_write_line': gi.FunctionInfo(image_write_line), 'image_write_prepare': gi.FunctionInfo(image_write_prepare), 'image_write_to_memory': gi.FunctionInfo(image_write_to_memory), 'reorder_margin_hint': gi.FunctionInfo(reorder_margin_hint), 'reorder_prepare_many': gi.FunctionInfo(reorder_prepare_many), 'do_eval': gi.VFuncInfo(eval), 'do_invalidate': gi.VFuncInfo(invalidate), 'do_minimise': gi.VFuncInfo(minimise), 'do_posteval': gi.VFuncInfo(posteval), 'do_preeval': gi.VFuncInfo(preeval), 'do_written': gi.VFuncInfo(written), 'parent_instance': <property object at 0x7f41868e5e50>, 'Xsize': <property object at 0x7f41868e5f40>, 'Ysize': <property object at 0x7f41868e9090>, 'Bands': <property object at 0x7f41868e9180>, 'BandFmt': <property object at 0x7f41868e9270>, 'Coding': <property object at 0x7f41868e9360>, 'Type': <property object at 0x7f41868e9450>, 'Xres': <property object at 0x7f41868e9540>, 'Yres': <property object at 0x7f41868e9630>, 'Xoffset': <property object at 0x7f41868e9720>, 'Yoffset': <property object at 0x7f41868e9810>, 'Length': <property object at 0x7f41868e9900>, 'Compression': <property object at 0x7f41868e99a0>, 'Level': <property object at 0x7f41868e9a90>, 'Bbits': <property object at 0x7f41868e9b80>, 'time': <property object at 0x7f41868e9c70>, 'Hist': <property object at 0x7f41868e9d60>, 'filename': <property object at 0x7f41868e9e50>, 'data': <property object at 0x7f41868e9f40>, 'kill': <property object at 0x7f41868ea090>, 'Xres_float': <property object at 0x7f41868ea180>, 'Yres_float': <property object at 0x7f41868ea270>, 'mode': <property object at 0x7f41868ea360>, 'dtype': <property object at 0x7f41868ea450>, 'fd': <property object at 0x7f41868ea540>, 'baseaddr': <property object at 0x7f41868ea630>, 'length': <property object at 0x7f41868ea720>, 'magic': <property object at 0x7f41868ea810>, 'start_fn': <property object at 0x7f41868ea900>, 'generate_fn': <property object at 0x7f41868ea9f0>, 'stop_fn': <property object at 0x7f41868eaae0>, 'client1': <property object at 0x7f41868eabd0>, 'client2': <property object at 0x7f41868eacc0>, 'sslock': <property object at 0x7f41868eadb0>, 'regions': <property object at 0x7f41868eaea0>, 'dhint': <property object at 0x7f41868eaf90>, 'meta': <property object at 0x7f41868eb0e0>, 'meta_traverse': <property object at 0x7f41868eb1d0>, 'sizeof_header': <property object at 0x7f41868eb2c0>, 'windows': <property object at 0x7f41868eb3b0>, 'upstream': <property object at 0x7f41868eb4a0>, 'downstream': <property object at 0x7f41868eb590>, 'serial': <property object at 0x7f41868eb680>, 'history_list': <property object at 0x7f41868eb770>, 'progress_signal': <property object at 0x7f41868eb860>, 'file_length': <property object at 0x7f41868eb950>, 'hint_set': <property object at 0x7f41868eba40>, 'delete_on_close': <property object at 0x7f41868ebb30>, 'delete_on_close_filename': <property object at 0x7f41868ebc70>})"
    __gdoc__ = 'Object VipsImage\n\nSignals from VipsImage:\n  invalidate ()\n  preeval (gpointer)\n  eval (gpointer)\n  posteval (gpointer)\n  written (gpointer)\n  minimise ()\n\nProperties from VipsImage:\n  width -> gint: Width\n    Image width in pixels\n  height -> gint: Height\n    Image height in pixels\n  bands -> gint: Bands\n    Number of bands in image\n  format -> VipsBandFormat: Format\n    Pixel format in image\n  coding -> VipsCoding: Coding\n    Pixel coding\n  interpretation -> VipsInterpretation: Interpretation\n    Pixel interpretation\n  xres -> gdouble: Xres\n    Horizontal resolution in pixels/mm\n  yres -> gdouble: Yres\n    Vertical resolution in pixels/mm\n  xoffset -> gint: Xoffset\n    Horizontal offset of origin\n  yoffset -> gint: Yoffset\n    Vertical offset of origin\n  filename -> gchararray: Filename\n    Image filename\n  mode -> gchararray: Mode\n    Open mode\n  kill -> gboolean: Kill\n    Block evaluation on this image\n  demand -> VipsDemandStyle: Demand style\n    Preferred demand style for this image\n  sizeof-header -> guint64: Size of header\n    Offset in bytes from start of file\n  foreign-buffer -> gpointer: Foreign buffer\n    Pointer to foreign pixels\n\nSignals from VipsObject:\n  postbuild () -> gint\n  preclose ()\n  close ()\n  postclose ()\n\nProperties from VipsObject:\n  nickname -> gchararray: Nickname\n    Class nickname\n  description -> gchararray: Description\n    Class description\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType VipsImage (94317410513712)>'
    __info__ = ObjectInfo(Image)


