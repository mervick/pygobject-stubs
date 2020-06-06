# encoding: utf-8
# module gi.repository.Clutter
# from /usr/lib64/girepository-1.0/Clutter-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .Texture import Texture

class CairoTexture(Texture):
    """
    :Constructors:
    
    ::
    
        CairoTexture(**properties)
        new(width:int, height:int) -> Clutter.Actor
    """
    def add_action(self, action): # real signature unknown; restored from __doc__
        """ add_action(self, action:Clutter.Action) """
        pass

    def add_action_with_name(self, name, action): # real signature unknown; restored from __doc__
        """ add_action_with_name(self, name:str, action:Clutter.Action) """
        pass

    def add_actor(self, actor): # real signature unknown; restored from __doc__
        """ add_actor(self, actor:Clutter.Actor) """
        pass

    def add_child(self, child): # real signature unknown; restored from __doc__
        """ add_child(self, child:Clutter.Actor) """
        pass

    def add_constraint(self, constraint): # real signature unknown; restored from __doc__
        """ add_constraint(self, constraint:Clutter.Constraint) """
        pass

    def add_constraint_with_name(self, name, constraint): # real signature unknown; restored from __doc__
        """ add_constraint_with_name(self, name:str, constraint:Clutter.Constraint) """
        pass

    def add_effect(self, effect): # real signature unknown; restored from __doc__
        """ add_effect(self, effect:Clutter.Effect) """
        pass

    def add_effect_with_name(self, name, effect): # real signature unknown; restored from __doc__
        """ add_effect_with_name(self, name:str, effect:Clutter.Effect) """
        pass

    def add_transition(self, name, transition): # real signature unknown; restored from __doc__
        """ add_transition(self, name:str, transition:Clutter.Transition) """
        pass

    def allocate(self, box, flags): # real signature unknown; restored from __doc__
        """ allocate(self, box:Clutter.ActorBox, flags:Clutter.AllocationFlags) """
        pass

    def allocate_align_fill(self, box, x_align, y_align, x_fill, y_fill, flags): # real signature unknown; restored from __doc__
        """ allocate_align_fill(self, box:Clutter.ActorBox, x_align:float, y_align:float, x_fill:bool, y_fill:bool, flags:Clutter.AllocationFlags) """
        pass

    def allocate_available_size(self, x, y, available_width, available_height, flags): # real signature unknown; restored from __doc__
        """ allocate_available_size(self, x:float, y:float, available_width:float, available_height:float, flags:Clutter.AllocationFlags) """
        pass

    def allocate_preferred_size(self, flags): # real signature unknown; restored from __doc__
        """ allocate_preferred_size(self, flags:Clutter.AllocationFlags) """
        pass

    def animatev(self, mode, duration, properties, values): # real signature unknown; restored from __doc__
        """ animatev(self, mode:int, duration:int, properties:list, values:list) -> Clutter.Animation """
        pass

    def animate_property(self, animation, property_name, initial_value, final_value, progress, value): # real signature unknown; restored from __doc__
        """ animate_property(self, animation:Clutter.Animation, property_name:str, initial_value:GObject.Value, final_value:GObject.Value, progress:float, value:GObject.Value) -> bool """
        return False

    def animate_with_alphav(self, alpha, properties, values): # real signature unknown; restored from __doc__
        """ animate_with_alphav(self, alpha:Clutter.Alpha, properties:list, values:list) -> Clutter.Animation """
        pass

    def animate_with_timelinev(self, mode, timeline, properties, values): # real signature unknown; restored from __doc__
        """ animate_with_timelinev(self, mode:int, timeline:Clutter.Timeline, properties:list, values:list) -> Clutter.Animation """
        pass

    def apply_relative_transform_to_point(self, ancestor=None, point): # real signature unknown; restored from __doc__
        """ apply_relative_transform_to_point(self, ancestor:Clutter.Actor=None, point:Clutter.Vertex) -> vertex:Clutter.Vertex """
        pass

    def apply_transform_to_point(self, point): # real signature unknown; restored from __doc__
        """ apply_transform_to_point(self, point:Clutter.Vertex) -> vertex:Clutter.Vertex """
        pass

    def bind_model(self, model=None, create_child_func, user_data=None): # real signature unknown; restored from __doc__
        """ bind_model(self, model:Gio.ListModel=None, create_child_func:Clutter.ActorCreateChildFunc, user_data=None) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def child_get_property(self, child, property, value): # real signature unknown; restored from __doc__
        """ child_get_property(self, child:Clutter.Actor, property:str, value:GObject.Value) """
        pass

    def child_notify(self, child, pspec): # real signature unknown; restored from __doc__
        """ child_notify(self, child:Clutter.Actor, pspec:GObject.ParamSpec) """
        pass

    def child_set_property(self, child, property, value): # real signature unknown; restored from __doc__
        """ child_set_property(self, child:Clutter.Actor, property:str, value:GObject.Value) """
        pass

    def class_find_child_property(self, klass, property_name): # real signature unknown; restored from __doc__
        """ class_find_child_property(klass:GObject.ObjectClass, property_name:str) -> GObject.ParamSpec """
        pass

    def class_list_child_properties(self, klass): # real signature unknown; restored from __doc__
        """ class_list_child_properties(klass:GObject.ObjectClass) -> list, n_properties:int """
        return []

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clear_actions(self): # real signature unknown; restored from __doc__
        """ clear_actions(self) """
        pass

    def clear_constraints(self): # real signature unknown; restored from __doc__
        """ clear_constraints(self) """
        pass

    def clear_effects(self): # real signature unknown; restored from __doc__
        """ clear_effects(self) """
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

    def contains(self, descendant): # real signature unknown; restored from __doc__
        """ contains(self, descendant:Clutter.Actor) -> bool """
        return False

    def continue_paint(self): # real signature unknown; restored from __doc__
        """ continue_paint(self) """
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> cairo.Context """
        pass

    def create_child_meta(self, actor): # real signature unknown; restored from __doc__
        """ create_child_meta(self, actor:Clutter.Actor) """
        pass

    def create_pango_context(self): # real signature unknown; restored from __doc__
        """ create_pango_context(self) -> Pango.Context """
        pass

    def create_pango_layout(self, text=None): # real signature unknown; restored from __doc__
        """ create_pango_layout(self, text:str=None) -> Pango.Layout """
        pass

    def create_region(self, x_offset, y_offset, width, height): # real signature unknown; restored from __doc__
        """ create_region(self, x_offset:int, y_offset:int, width:int, height:int) -> cairo.Context """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def destroy_all_children(self): # real signature unknown; restored from __doc__
        """ destroy_all_children(self) """
        pass

    def destroy_child_meta(self, actor): # real signature unknown; restored from __doc__
        """ destroy_child_meta(self, actor:Clutter.Actor) """
        pass

    def detach_animation(self): # real signature unknown; restored from __doc__
        """ detach_animation(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_allocate(self, *args, **kwargs): # real signature unknown
        """ allocate(self, box:Clutter.ActorBox, flags:Clutter.AllocationFlags) """
        pass

    def do_apply_transform(self, *args, **kwargs): # real signature unknown
        """ apply_transform(self, matrix:Clutter.Matrix) """
        pass

    def do_button_press_event(self, *args, **kwargs): # real signature unknown
        """ button_press_event(self, event:Clutter.ButtonEvent) -> bool """
        pass

    def do_button_release_event(self, *args, **kwargs): # real signature unknown
        """ button_release_event(self, event:Clutter.ButtonEvent) -> bool """
        pass

    def do_captured_event(self, *args, **kwargs): # real signature unknown
        """ captured_event(self, event:Clutter.Event) -> bool """
        pass

    def do_create_surface(self, *args, **kwargs): # real signature unknown
        """ create_surface(self, width:int, height:int) -> cairo.Surface """
        pass

    def do_destroy(self, *args, **kwargs): # real signature unknown
        """ destroy(self) """
        pass

    def do_draw(self, *args, **kwargs): # real signature unknown
        """ draw(self, cr:cairo.Context) -> bool """
        pass

    def do_enter_event(self, *args, **kwargs): # real signature unknown
        """ enter_event(self, event:Clutter.CrossingEvent) -> bool """
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event:Clutter.Event) -> bool """
        pass

    def do_get_accessible(self, *args, **kwargs): # real signature unknown
        """ get_accessible(self) -> Atk.Object """
        pass

    def do_get_paint_volume(self, *args, **kwargs): # real signature unknown
        """ get_paint_volume(self, volume:Clutter.PaintVolume) -> bool """
        pass

    def do_get_preferred_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height(self, for_width:float) -> min_height_p:float, natural_height_p:float """
        pass

    def do_get_preferred_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width(self, for_height:float) -> min_width_p:float, natural_width_p:float """
        pass

    def do_has_overlaps(self, *args, **kwargs): # real signature unknown
        """ has_overlaps(self) -> bool """
        pass

    def do_hide(self, *args, **kwargs): # real signature unknown
        """ hide(self) """
        pass

    def do_hide_all(self, *args, **kwargs): # real signature unknown
        """ hide_all(self) """
        pass

    def do_key_focus_in(self, *args, **kwargs): # real signature unknown
        """ key_focus_in(self) """
        pass

    def do_key_focus_out(self, *args, **kwargs): # real signature unknown
        """ key_focus_out(self) """
        pass

    def do_key_press_event(self, *args, **kwargs): # real signature unknown
        """ key_press_event(self, event:Clutter.KeyEvent) -> bool """
        pass

    def do_key_release_event(self, *args, **kwargs): # real signature unknown
        """ key_release_event(self, event:Clutter.KeyEvent) -> bool """
        pass

    def do_leave_event(self, *args, **kwargs): # real signature unknown
        """ leave_event(self, event:Clutter.CrossingEvent) -> bool """
        pass

    def do_load_finished(self, *args, **kwargs): # real signature unknown
        """ load_finished(self, error:error) """
        pass

    def do_map(self, *args, **kwargs): # real signature unknown
        """ map(self) """
        pass

    def do_motion_event(self, *args, **kwargs): # real signature unknown
        """ motion_event(self, event:Clutter.MotionEvent) -> bool """
        pass

    def do_paint(self, *args, **kwargs): # real signature unknown
        """ paint(self) """
        pass

    def do_paint_node(self, *args, **kwargs): # real signature unknown
        """ paint_node(self, root:Clutter.PaintNode) """
        pass

    def do_parent_set(self, *args, **kwargs): # real signature unknown
        """ parent_set(self, old_parent:Clutter.Actor) """
        pass

    def do_pick(self, *args, **kwargs): # real signature unknown
        """ pick(self, color:Clutter.Color) """
        pass

    def do_pixbuf_change(self, *args, **kwargs): # real signature unknown
        """ pixbuf_change(self) """
        pass

    def do_queue_redraw(self, *args, **kwargs): # real signature unknown
        """ queue_redraw(self, leaf_that_queued:Clutter.Actor) """
        pass

    def do_queue_relayout(self, *args, **kwargs): # real signature unknown
        """ queue_relayout(self) """
        pass

    def do_realize(self, *args, **kwargs): # real signature unknown
        """ realize(self) """
        pass

    def do_scroll_event(self, *args, **kwargs): # real signature unknown
        """ scroll_event(self, event:Clutter.ScrollEvent) -> bool """
        pass

    def do_show(self, *args, **kwargs): # real signature unknown
        """ show(self) """
        pass

    def do_show_all(self, *args, **kwargs): # real signature unknown
        """ show_all(self) """
        pass

    def do_size_change(self, *args, **kwargs): # real signature unknown
        """ size_change(self, width:int, height:int) """
        pass

    def do_touch_event(self, *args, **kwargs): # real signature unknown
        """ touch_event(self, event:Clutter.TouchEvent) -> bool """
        pass

    def do_unmap(self, *args, **kwargs): # real signature unknown
        """ unmap(self) """
        pass

    def do_unrealize(self, *args, **kwargs): # real signature unknown
        """ unrealize(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def event(self, event, capture): # real signature unknown; restored from __doc__
        """ event(self, event:Clutter.Event, capture:bool) -> bool """
        return False

    def find_child_by_name(self, child_name): # real signature unknown; restored from __doc__
        """ find_child_by_name(self, child_name:str) -> Clutter.Actor """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, callback:Clutter.Callback, user_data=None) """
        pass

    def foreach_with_internals(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_with_internals(self, callback:Clutter.Callback, user_data=None) """
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

    def get_abs_allocation_vertices(self): # real signature unknown; restored from __doc__
        """ get_abs_allocation_vertices(self) -> verts:list """
        pass

    def get_accessible(self): # real signature unknown; restored from __doc__
        """ get_accessible(self) -> Atk.Object """
        pass

    def get_action(self, name): # real signature unknown; restored from __doc__
        """ get_action(self, name:str) -> Clutter.Action """
        pass

    def get_actions(self): # real signature unknown; restored from __doc__
        """ get_actions(self) -> list """
        return []

    def get_allocation_box(self): # real signature unknown; restored from __doc__
        """ get_allocation_box(self) -> box:Clutter.ActorBox """
        pass

    def get_allocation_geometry(self): # real signature unknown; restored from __doc__
        """ get_allocation_geometry(self) -> geom:Clutter.Geometry """
        pass

    def get_allocation_vertices(self, ancestor=None): # real signature unknown; restored from __doc__
        """ get_allocation_vertices(self, ancestor:Clutter.Actor=None) -> verts:list """
        pass

    def get_anchor_point(self): # real signature unknown; restored from __doc__
        """ get_anchor_point(self) -> anchor_x:float, anchor_y:float """
        pass

    def get_anchor_point_gravity(self): # real signature unknown; restored from __doc__
        """ get_anchor_point_gravity(self) -> Clutter.Gravity """
        pass

    def get_animation(self): # real signature unknown; restored from __doc__
        """ get_animation(self) -> Clutter.Animation """
        pass

    def get_auto_resize(self): # real signature unknown; restored from __doc__
        """ get_auto_resize(self) -> bool """
        return False

    def get_background_color(self): # real signature unknown; restored from __doc__
        """ get_background_color(self) -> color:Clutter.Color """
        pass

    def get_base_size(self): # real signature unknown; restored from __doc__
        """ get_base_size(self) -> width:int, height:int """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_child_at_index(self, index_): # real signature unknown; restored from __doc__
        """ get_child_at_index(self, index_:int) -> Clutter.Actor """
        pass

    def get_child_meta(self, actor): # real signature unknown; restored from __doc__
        """ get_child_meta(self, actor:Clutter.Actor) -> Clutter.ChildMeta """
        pass

    def get_child_transform(self): # real signature unknown; restored from __doc__
        """ get_child_transform(self) -> transform:Clutter.Matrix """
        pass

    def get_clip(self): # real signature unknown; restored from __doc__
        """ get_clip(self) -> xoff:float, yoff:float, width:float, height:float """
        pass

    def get_clip_to_allocation(self): # real signature unknown; restored from __doc__
        """ get_clip_to_allocation(self) -> bool """
        return False

    def get_cogl_material(self): # real signature unknown; restored from __doc__
        """ get_cogl_material(self) """
        pass

    def get_cogl_texture(self): # real signature unknown; restored from __doc__
        """ get_cogl_texture(self) """
        pass

    def get_constraint(self, name): # real signature unknown; restored from __doc__
        """ get_constraint(self, name:str) -> Clutter.Constraint """
        pass

    def get_constraints(self): # real signature unknown; restored from __doc__
        """ get_constraints(self) -> list """
        return []

    def get_content(self): # real signature unknown; restored from __doc__
        """ get_content(self) -> Clutter.Content """
        pass

    def get_content_box(self): # real signature unknown; restored from __doc__
        """ get_content_box(self) -> box:Clutter.ActorBox """
        pass

    def get_content_gravity(self): # real signature unknown; restored from __doc__
        """ get_content_gravity(self) -> Clutter.ContentGravity """
        pass

    def get_content_repeat(self): # real signature unknown; restored from __doc__
        """ get_content_repeat(self) -> Clutter.ContentRepeat """
        pass

    def get_content_scaling_filters(self): # real signature unknown; restored from __doc__
        """ get_content_scaling_filters(self) -> min_filter:Clutter.ScalingFilter, mag_filter:Clutter.ScalingFilter """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_paint_volume(self): # real signature unknown; restored from __doc__
        """ get_default_paint_volume(self) -> Clutter.PaintVolume """
        pass

    def get_depth(self): # real signature unknown; restored from __doc__
        """ get_depth(self) -> float """
        return 0.0

    def get_easing_delay(self): # real signature unknown; restored from __doc__
        """ get_easing_delay(self) -> int """
        return 0

    def get_easing_duration(self): # real signature unknown; restored from __doc__
        """ get_easing_duration(self) -> int """
        return 0

    def get_easing_mode(self): # real signature unknown; restored from __doc__
        """ get_easing_mode(self) -> Clutter.AnimationMode """
        pass

    def get_effect(self, name): # real signature unknown; restored from __doc__
        """ get_effect(self, name:str) -> Clutter.Effect """
        pass

    def get_effects(self): # real signature unknown; restored from __doc__
        """ get_effects(self) -> list """
        return []

    def get_filter_quality(self): # real signature unknown; restored from __doc__
        """ get_filter_quality(self) -> Clutter.TextureQuality """
        pass

    def get_first_child(self): # real signature unknown; restored from __doc__
        """ get_first_child(self) -> Clutter.Actor """
        pass

    def get_fixed_position_set(self): # real signature unknown; restored from __doc__
        """ get_fixed_position_set(self) -> bool """
        return False

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Clutter.ActorFlags """
        pass

    def get_geometry(self): # real signature unknown; restored from __doc__
        """ get_geometry(self) -> geometry:Clutter.Geometry """
        pass

    def get_gid(self): # real signature unknown; restored from __doc__
        """ get_gid(self) -> int """
        return 0

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> float """
        return 0.0

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_initial_state(self, property_name, value): # real signature unknown; restored from __doc__
        """ get_initial_state(self, property_name:str, value:GObject.Value) """
        pass

    def get_keep_aspect_ratio(self): # real signature unknown; restored from __doc__
        """ get_keep_aspect_ratio(self) -> bool """
        return False

    def get_last_child(self): # real signature unknown; restored from __doc__
        """ get_last_child(self) -> Clutter.Actor """
        pass

    def get_layout_manager(self): # real signature unknown; restored from __doc__
        """ get_layout_manager(self) -> Clutter.LayoutManager """
        pass

    def get_load_async(self): # real signature unknown; restored from __doc__
        """ get_load_async(self) -> bool """
        return False

    def get_load_data_async(self): # real signature unknown; restored from __doc__
        """ get_load_data_async(self) -> bool """
        return False

    def get_margin(self): # real signature unknown; restored from __doc__
        """ get_margin(self) -> margin:Clutter.Margin """
        pass

    def get_margin_bottom(self): # real signature unknown; restored from __doc__
        """ get_margin_bottom(self) -> float """
        return 0.0

    def get_margin_left(self): # real signature unknown; restored from __doc__
        """ get_margin_left(self) -> float """
        return 0.0

    def get_margin_right(self): # real signature unknown; restored from __doc__
        """ get_margin_right(self) -> float """
        return 0.0

    def get_margin_top(self): # real signature unknown; restored from __doc__
        """ get_margin_top(self) -> float """
        return 0.0

    def get_max_tile_waste(self): # real signature unknown; restored from __doc__
        """ get_max_tile_waste(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_next_sibling(self): # real signature unknown; restored from __doc__
        """ get_next_sibling(self) -> Clutter.Actor """
        pass

    def get_n_children(self): # real signature unknown; restored from __doc__
        """ get_n_children(self) -> int """
        return 0

    def get_offscreen_redirect(self): # real signature unknown; restored from __doc__
        """ get_offscreen_redirect(self) -> Clutter.OffscreenRedirect """
        pass

    def get_opacity(self): # real signature unknown; restored from __doc__
        """ get_opacity(self) -> int """
        return 0

    def get_paint_box(self): # real signature unknown; restored from __doc__
        """ get_paint_box(self) -> bool, box:Clutter.ActorBox """
        return False

    def get_paint_opacity(self): # real signature unknown; restored from __doc__
        """ get_paint_opacity(self) -> int """
        return 0

    def get_paint_visibility(self): # real signature unknown; restored from __doc__
        """ get_paint_visibility(self) -> bool """
        return False

    def get_paint_volume(self): # real signature unknown; restored from __doc__
        """ get_paint_volume(self) -> Clutter.PaintVolume """
        pass

    def get_pango_context(self): # real signature unknown; restored from __doc__
        """ get_pango_context(self) -> Pango.Context """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Clutter.Actor """
        pass

    def get_pick_with_alpha(self): # real signature unknown; restored from __doc__
        """ get_pick_with_alpha(self) -> bool """
        return False

    def get_pivot_point(self): # real signature unknown; restored from __doc__
        """ get_pivot_point(self) -> pivot_x:float, pivot_y:float """
        pass

    def get_pivot_point_z(self): # real signature unknown; restored from __doc__
        """ get_pivot_point_z(self) -> float """
        return 0.0

    def get_pixel_format(self): # real signature unknown; restored from __doc__
        """ get_pixel_format(self) -> Cogl.PixelFormat """
        pass

    def get_position(self): # real signature unknown; restored from __doc__
        """ get_position(self) -> x:float, y:float """
        return x

    def get_preferred_height(self, for_width): # real signature unknown; restored from __doc__
        """ get_preferred_height(self, for_width:float) -> min_height_p:float, natural_height_p:float """
        pass

    def get_preferred_size(self): # real signature unknown; restored from __doc__
        """ get_preferred_size(self) -> min_width_p:float, min_height_p:float, natural_width_p:float, natural_height_p:float """
        pass

    def get_preferred_width(self, for_height): # real signature unknown; restored from __doc__
        """ get_preferred_width(self, for_height:float) -> min_width_p:float, natural_width_p:float """
        pass

    def get_previous_sibling(self): # real signature unknown; restored from __doc__
        """ get_previous_sibling(self) -> Clutter.Actor """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_reactive(self): # real signature unknown; restored from __doc__
        """ get_reactive(self) -> bool """
        return False

    def get_repeat(self): # real signature unknown; restored from __doc__
        """ get_repeat(self) -> repeat_x:bool, repeat_y:bool """
        pass

    def get_request_mode(self): # real signature unknown; restored from __doc__
        """ get_request_mode(self) -> Clutter.RequestMode """
        pass

    def get_rotation(self, axis): # real signature unknown; restored from __doc__
        """ get_rotation(self, axis:Clutter.RotateAxis) -> float, x:float, y:float, z:float """
        return 0.0

    def get_rotation_angle(self, axis): # real signature unknown; restored from __doc__
        """ get_rotation_angle(self, axis:Clutter.RotateAxis) -> float """
        return 0.0

    def get_scale(self): # real signature unknown; restored from __doc__
        """ get_scale(self) -> scale_x:float, scale_y:float """
        pass

    def get_scale_center(self): # real signature unknown; restored from __doc__
        """ get_scale_center(self) -> center_x:float, center_y:float """
        pass

    def get_scale_gravity(self): # real signature unknown; restored from __doc__
        """ get_scale_gravity(self) -> Clutter.Gravity """
        pass

    def get_scale_z(self): # real signature unknown; restored from __doc__
        """ get_scale_z(self) -> float """
        return 0.0

    def get_shader(self): # real signature unknown; restored from __doc__
        """ get_shader(self) -> Clutter.Shader """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:float, height:float """
        pass

    def get_stage(self): # real signature unknown; restored from __doc__
        """ get_stage(self) -> Clutter.Stage """
        pass

    def get_surface_size(self): # real signature unknown; restored from __doc__
        """ get_surface_size(self) -> width:int, height:int """
        pass

    def get_sync_size(self): # real signature unknown; restored from __doc__
        """ get_sync_size(self) -> bool """
        return False

    def get_text_direction(self): # real signature unknown; restored from __doc__
        """ get_text_direction(self) -> Clutter.TextDirection """
        pass

    def get_transform(self): # real signature unknown; restored from __doc__
        """ get_transform(self) -> transform:Clutter.Matrix """
        pass

    def get_transformation_matrix(self): # real signature unknown; restored from __doc__
        """ get_transformation_matrix(self) -> matrix:Clutter.Matrix """
        pass

    def get_transformed_paint_volume(self, relative_to_ancestor): # real signature unknown; restored from __doc__
        """ get_transformed_paint_volume(self, relative_to_ancestor:Clutter.Actor) -> Clutter.PaintVolume """
        pass

    def get_transformed_position(self): # real signature unknown; restored from __doc__
        """ get_transformed_position(self) -> x:float, y:float """
        return x

    def get_transformed_size(self): # real signature unknown; restored from __doc__
        """ get_transformed_size(self) -> width:float, height:float """
        pass

    def get_transition(self, name): # real signature unknown; restored from __doc__
        """ get_transition(self, name:str) -> Clutter.Transition """
        pass

    def get_translation(self): # real signature unknown; restored from __doc__
        """ get_translation(self) -> translate_x:float, translate_y:float, translate_z:float """
        pass

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> float """
        return 0.0

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> float """
        return 0.0

    def get_x_align(self): # real signature unknown; restored from __doc__
        """ get_x_align(self) -> Clutter.ActorAlign """
        pass

    def get_x_expand(self): # real signature unknown; restored from __doc__
        """ get_x_expand(self) -> bool """
        return False

    def get_y(self): # real signature unknown; restored from __doc__
        """ get_y(self) -> float """
        return 0.0

    def get_y_align(self): # real signature unknown; restored from __doc__
        """ get_y_align(self) -> Clutter.ActorAlign """
        pass

    def get_y_expand(self): # real signature unknown; restored from __doc__
        """ get_y_expand(self) -> bool """
        return False

    def get_z_position(self): # real signature unknown; restored from __doc__
        """ get_z_position(self) -> float """
        return 0.0

    def get_z_rotation_gravity(self): # real signature unknown; restored from __doc__
        """ get_z_rotation_gravity(self) -> Clutter.Gravity """
        pass

    def grab_key_focus(self): # real signature unknown; restored from __doc__
        """ grab_key_focus(self) """
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

    def has_actions(self): # real signature unknown; restored from __doc__
        """ has_actions(self) -> bool """
        return False

    def has_allocation(self): # real signature unknown; restored from __doc__
        """ has_allocation(self) -> bool """
        return False

    def has_clip(self): # real signature unknown; restored from __doc__
        """ has_clip(self) -> bool """
        return False

    def has_constraints(self): # real signature unknown; restored from __doc__
        """ has_constraints(self) -> bool """
        return False

    def has_effects(self): # real signature unknown; restored from __doc__
        """ has_effects(self) -> bool """
        return False

    def has_key_focus(self): # real signature unknown; restored from __doc__
        """ has_key_focus(self) -> bool """
        return False

    def has_overlaps(self): # real signature unknown; restored from __doc__
        """ has_overlaps(self) -> bool """
        return False

    def has_pointer(self): # real signature unknown; restored from __doc__
        """ has_pointer(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hide_all(self): # real signature unknown; restored from __doc__
        """ hide_all(self) """
        pass

    def insert_child_above(self, child, sibling=None): # real signature unknown; restored from __doc__
        """ insert_child_above(self, child:Clutter.Actor, sibling:Clutter.Actor=None) """
        pass

    def insert_child_at_index(self, child, index_): # real signature unknown; restored from __doc__
        """ insert_child_at_index(self, child:Clutter.Actor, index_:int) """
        pass

    def insert_child_below(self, child, sibling=None): # real signature unknown; restored from __doc__
        """ insert_child_below(self, child:Clutter.Actor, sibling:Clutter.Actor=None) """
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

    def interpolate_value(self, property_name, interval, progress): # real signature unknown; restored from __doc__
        """ interpolate_value(self, property_name:str, interval:Clutter.Interval, progress:float) -> bool, value:GObject.Value """
        return False

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def invalidate_rectangle(self, rect=None): # real signature unknown; restored from __doc__
        """ invalidate_rectangle(self, rect:cairo.RectangleInt=None) """
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_in_clone_paint(self): # real signature unknown; restored from __doc__
        """ is_in_clone_paint(self) -> bool """
        return False

    def is_mapped(self): # real signature unknown; restored from __doc__
        """ is_mapped(self) -> bool """
        return False

    def is_realized(self): # real signature unknown; restored from __doc__
        """ is_realized(self) -> bool """
        return False

    def is_rotated(self): # real signature unknown; restored from __doc__
        """ is_rotated(self) -> bool """
        return False

    def is_scaled(self): # real signature unknown; restored from __doc__
        """ is_scaled(self) -> bool """
        return False

    def is_visible(self): # real signature unknown; restored from __doc__
        """ is_visible(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lower(self, above=None): # real signature unknown; restored from __doc__
        """ lower(self, above:Clutter.Actor=None) """
        pass

    def lower_bottom(self): # real signature unknown; restored from __doc__
        """ lower_bottom(self) """
        pass

    def lower_child(self, actor, sibling=None): # real signature unknown; restored from __doc__
        """ lower_child(self, actor:Clutter.Actor, sibling:Clutter.Actor=None) """
        pass

    def map(self): # real signature unknown; restored from __doc__
        """ map(self) """
        pass

    def move_anchor_point(self, anchor_x, anchor_y): # real signature unknown; restored from __doc__
        """ move_anchor_point(self, anchor_x:float, anchor_y:float) """
        pass

    def move_anchor_point_from_gravity(self, gravity): # real signature unknown; restored from __doc__
        """ move_anchor_point_from_gravity(self, gravity:Clutter.Gravity) """
        pass

    def move_by(self, dx, dy): # real signature unknown; restored from __doc__
        """ move_by(self, dx:float, dy:float) """
        pass

    def needs_expand(self, orientation): # real signature unknown; restored from __doc__
        """ needs_expand(self, orientation:Clutter.Orientation) -> bool """
        return False

    def new(self, width, height): # real signature unknown; restored from __doc__
        """ new(width:int, height:int) -> Clutter.Actor """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_actor(self, actor): # real signature unknown; restored from __doc__
        """ new_from_actor(actor:Clutter.Actor) -> Clutter.Actor """
        pass

    def new_from_file(self, filename): # real signature unknown; restored from __doc__
        """ new_from_file(filename:str) -> Clutter.Actor """
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

    def paint(self): # real signature unknown; restored from __doc__
        """ paint(self) """
        pass

    def parse_custom_node(self, script, value, name, node): # real signature unknown; restored from __doc__
        """ parse_custom_node(self, script:Clutter.Script, value:GObject.Value, name:str, node:Json.Node) -> bool """
        return False

    def pop_internal(self): # real signature unknown; restored from __doc__
        """ pop_internal(self) """
        pass

    def push_internal(self): # real signature unknown; restored from __doc__
        """ push_internal(self) """
        pass

    def queue_redraw(self): # real signature unknown; restored from __doc__
        """ queue_redraw(self) """
        pass

    def queue_redraw_with_clip(self, clip=None): # real signature unknown; restored from __doc__
        """ queue_redraw_with_clip(self, clip:cairo.RectangleInt=None) """
        pass

    def queue_relayout(self): # real signature unknown; restored from __doc__
        """ queue_relayout(self) """
        pass

    def raise_(self, below=None): # real signature unknown; restored from __doc__
        """ raise_(self, below:Clutter.Actor=None) """
        pass

    def raise_child(self, actor, sibling=None): # real signature unknown; restored from __doc__
        """ raise_child(self, actor:Clutter.Actor, sibling:Clutter.Actor=None) """
        pass

    def raise_top(self): # real signature unknown; restored from __doc__
        """ raise_top(self) """
        pass

    def realize(self): # real signature unknown; restored from __doc__
        """ realize(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_action(self, action): # real signature unknown; restored from __doc__
        """ remove_action(self, action:Clutter.Action) """
        pass

    def remove_action_by_name(self, name): # real signature unknown; restored from __doc__
        """ remove_action_by_name(self, name:str) """
        pass

    def remove_actor(self, actor): # real signature unknown; restored from __doc__
        """ remove_actor(self, actor:Clutter.Actor) """
        pass

    def remove_all_children(self): # real signature unknown; restored from __doc__
        """ remove_all_children(self) """
        pass

    def remove_all_transitions(self): # real signature unknown; restored from __doc__
        """ remove_all_transitions(self) """
        pass

    def remove_child(self, child): # real signature unknown; restored from __doc__
        """ remove_child(self, child:Clutter.Actor) """
        pass

    def remove_clip(self): # real signature unknown; restored from __doc__
        """ remove_clip(self) """
        pass

    def remove_constraint(self, constraint): # real signature unknown; restored from __doc__
        """ remove_constraint(self, constraint:Clutter.Constraint) """
        pass

    def remove_constraint_by_name(self, name): # real signature unknown; restored from __doc__
        """ remove_constraint_by_name(self, name:str) """
        pass

    def remove_effect(self, effect): # real signature unknown; restored from __doc__
        """ remove_effect(self, effect:Clutter.Effect) """
        pass

    def remove_effect_by_name(self, name): # real signature unknown; restored from __doc__
        """ remove_effect_by_name(self, name:str) """
        pass

    def remove_transition(self, name): # real signature unknown; restored from __doc__
        """ remove_transition(self, name:str) """
        pass

    def reparent(self, new_parent): # real signature unknown; restored from __doc__
        """ reparent(self, new_parent:Clutter.Actor) """
        pass

    def replace_child(self, old_child, new_child): # real signature unknown; restored from __doc__
        """ replace_child(self, old_child:Clutter.Actor, new_child:Clutter.Actor) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def restore_easing_state(self): # real signature unknown; restored from __doc__
        """ restore_easing_state(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def save_easing_state(self): # real signature unknown; restored from __doc__
        """ save_easing_state(self) """
        pass

    def set_allocation(self, box, flags): # real signature unknown; restored from __doc__
        """ set_allocation(self, box:Clutter.ActorBox, flags:Clutter.AllocationFlags) """
        pass

    def set_anchor_point(self, anchor_x, anchor_y): # real signature unknown; restored from __doc__
        """ set_anchor_point(self, anchor_x:float, anchor_y:float) """
        pass

    def set_anchor_point_from_gravity(self, gravity): # real signature unknown; restored from __doc__
        """ set_anchor_point_from_gravity(self, gravity:Clutter.Gravity) """
        pass

    def set_area_from_rgb_data(self, data, has_alpha, x, y, width, height, rowstride, bpp, flags): # real signature unknown; restored from __doc__
        """ set_area_from_rgb_data(self, data:list, has_alpha:bool, x:int, y:int, width:int, height:int, rowstride:int, bpp:int, flags:Clutter.TextureFlags) -> bool """
        return False

    def set_auto_resize(self, value): # real signature unknown; restored from __doc__
        """ set_auto_resize(self, value:bool) """
        pass

    def set_background_color(self, color=None): # real signature unknown; restored from __doc__
        """ set_background_color(self, color:Clutter.Color=None) """
        pass

    def set_child_above_sibling(self, child, sibling=None): # real signature unknown; restored from __doc__
        """ set_child_above_sibling(self, child:Clutter.Actor, sibling:Clutter.Actor=None) """
        pass

    def set_child_at_index(self, child, index_): # real signature unknown; restored from __doc__
        """ set_child_at_index(self, child:Clutter.Actor, index_:int) """
        pass

    def set_child_below_sibling(self, child, sibling=None): # real signature unknown; restored from __doc__
        """ set_child_below_sibling(self, child:Clutter.Actor, sibling:Clutter.Actor=None) """
        pass

    def set_child_transform(self, transform=None): # real signature unknown; restored from __doc__
        """ set_child_transform(self, transform:Clutter.Matrix=None) """
        pass

    def set_clip(self, xoff, yoff, width, height): # real signature unknown; restored from __doc__
        """ set_clip(self, xoff:float, yoff:float, width:float, height:float) """
        pass

    def set_clip_to_allocation(self, clip_set): # real signature unknown; restored from __doc__
        """ set_clip_to_allocation(self, clip_set:bool) """
        pass

    def set_cogl_material(self, cogl_material): # real signature unknown; restored from __doc__
        """ set_cogl_material(self, cogl_material) """
        pass

    def set_cogl_texture(self, cogl_tex): # real signature unknown; restored from __doc__
        """ set_cogl_texture(self, cogl_tex) """
        pass

    def set_content(self, content=None): # real signature unknown; restored from __doc__
        """ set_content(self, content:Clutter.Content=None) """
        pass

    def set_content_gravity(self, gravity): # real signature unknown; restored from __doc__
        """ set_content_gravity(self, gravity:Clutter.ContentGravity) """
        pass

    def set_content_repeat(self, repeat): # real signature unknown; restored from __doc__
        """ set_content_repeat(self, repeat:Clutter.ContentRepeat) """
        pass

    def set_content_scaling_filters(self, min_filter, mag_filter): # real signature unknown; restored from __doc__
        """ set_content_scaling_filters(self, min_filter:Clutter.ScalingFilter, mag_filter:Clutter.ScalingFilter) """
        pass

    def set_custom_property(self, script, name, value): # real signature unknown; restored from __doc__
        """ set_custom_property(self, script:Clutter.Script, name:str, value:GObject.Value) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_depth(self, depth): # real signature unknown; restored from __doc__
        """ set_depth(self, depth:float) """
        pass

    def set_easing_delay(self, msecs): # real signature unknown; restored from __doc__
        """ set_easing_delay(self, msecs:int) """
        pass

    def set_easing_duration(self, msecs): # real signature unknown; restored from __doc__
        """ set_easing_duration(self, msecs:int) """
        pass

    def set_easing_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_easing_mode(self, mode:Clutter.AnimationMode) """
        pass

    def set_filter_quality(self, filter_quality): # real signature unknown; restored from __doc__
        """ set_filter_quality(self, filter_quality:Clutter.TextureQuality) """
        pass

    def set_final_state(self, property_name, value): # real signature unknown; restored from __doc__
        """ set_final_state(self, property_name:str, value:GObject.Value) """
        pass

    def set_fixed_position_set(self, is_set): # real signature unknown; restored from __doc__
        """ set_fixed_position_set(self, is_set:bool) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:Clutter.ActorFlags) """
        pass

    def set_from_file(self, filename): # real signature unknown; restored from __doc__
        """ set_from_file(self, filename:str) -> bool """
        return False

    def set_from_rgb_data(self, data, has_alpha, width, height, rowstride, bpp, flags): # real signature unknown; restored from __doc__
        """ set_from_rgb_data(self, data:list, has_alpha:bool, width:int, height:int, rowstride:int, bpp:int, flags:Clutter.TextureFlags) -> bool """
        return False

    def set_from_yuv_data(self, data, width, height, flags): # real signature unknown; restored from __doc__
        """ set_from_yuv_data(self, data:list, width:int, height:int, flags:Clutter.TextureFlags) -> bool """
        return False

    def set_geometry(self, geometry): # real signature unknown; restored from __doc__
        """ set_geometry(self, geometry:Clutter.Geometry) """
        pass

    def set_height(self, height): # real signature unknown; restored from __doc__
        """ set_height(self, height:float) """
        pass

    def set_id(self, id_): # real signature unknown; restored from __doc__
        """ set_id(self, id_:str) """
        pass

    def set_keep_aspect_ratio(self, keep_aspect): # real signature unknown; restored from __doc__
        """ set_keep_aspect_ratio(self, keep_aspect:bool) """
        pass

    def set_layout_manager(self, manager=None): # real signature unknown; restored from __doc__
        """ set_layout_manager(self, manager:Clutter.LayoutManager=None) """
        pass

    def set_load_async(self, load_async): # real signature unknown; restored from __doc__
        """ set_load_async(self, load_async:bool) """
        pass

    def set_load_data_async(self, load_async): # real signature unknown; restored from __doc__
        """ set_load_data_async(self, load_async:bool) """
        pass

    def set_margin(self, margin): # real signature unknown; restored from __doc__
        """ set_margin(self, margin:Clutter.Margin) """
        pass

    def set_margin_bottom(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_bottom(self, margin:float) """
        pass

    def set_margin_left(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_left(self, margin:float) """
        pass

    def set_margin_right(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_right(self, margin:float) """
        pass

    def set_margin_top(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_top(self, margin:float) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_offscreen_redirect(self, redirect): # real signature unknown; restored from __doc__
        """ set_offscreen_redirect(self, redirect:Clutter.OffscreenRedirect) """
        pass

    def set_opacity(self, opacity): # real signature unknown; restored from __doc__
        """ set_opacity(self, opacity:int) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Clutter.Actor) """
        pass

    def set_pick_with_alpha(self, pick_with_alpha): # real signature unknown; restored from __doc__
        """ set_pick_with_alpha(self, pick_with_alpha:bool) """
        pass

    def set_pivot_point(self, pivot_x, pivot_y): # real signature unknown; restored from __doc__
        """ set_pivot_point(self, pivot_x:float, pivot_y:float) """
        pass

    def set_pivot_point_z(self, pivot_z): # real signature unknown; restored from __doc__
        """ set_pivot_point_z(self, pivot_z:float) """
        pass

    def set_position(self, x, y): # real signature unknown; restored from __doc__
        """ set_position(self, x:float, y:float) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_reactive(self, reactive): # real signature unknown; restored from __doc__
        """ set_reactive(self, reactive:bool) """
        pass

    def set_repeat(self, repeat_x, repeat_y): # real signature unknown; restored from __doc__
        """ set_repeat(self, repeat_x:bool, repeat_y:bool) """
        pass

    def set_request_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_request_mode(self, mode:Clutter.RequestMode) """
        pass

    def set_rotation(self, axis, angle, x, y, z): # real signature unknown; restored from __doc__
        """ set_rotation(self, axis:Clutter.RotateAxis, angle:float, x:float, y:float, z:float) """
        pass

    def set_rotation_angle(self, axis, angle): # real signature unknown; restored from __doc__
        """ set_rotation_angle(self, axis:Clutter.RotateAxis, angle:float) """
        pass

    def set_scale(self, scale_x, scale_y): # real signature unknown; restored from __doc__
        """ set_scale(self, scale_x:float, scale_y:float) """
        pass

    def set_scale_full(self, scale_x, scale_y, center_x, center_y): # real signature unknown; restored from __doc__
        """ set_scale_full(self, scale_x:float, scale_y:float, center_x:float, center_y:float) """
        pass

    def set_scale_with_gravity(self, scale_x, scale_y, gravity): # real signature unknown; restored from __doc__
        """ set_scale_with_gravity(self, scale_x:float, scale_y:float, gravity:Clutter.Gravity) """
        pass

    def set_scale_z(self, scale_z): # real signature unknown; restored from __doc__
        """ set_scale_z(self, scale_z:float) """
        pass

    def set_shader(self, shader=None): # real signature unknown; restored from __doc__
        """ set_shader(self, shader:Clutter.Shader=None) -> bool """
        return False

    def set_shader_param(self, param, value): # real signature unknown; restored from __doc__
        """ set_shader_param(self, param:str, value:GObject.Value) """
        pass

    def set_shader_param_float(self, param, value): # real signature unknown; restored from __doc__
        """ set_shader_param_float(self, param:str, value:float) """
        pass

    def set_shader_param_int(self, param, value): # real signature unknown; restored from __doc__
        """ set_shader_param_int(self, param:str, value:int) """
        pass

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:float, height:float) """
        pass

    def set_surface_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_surface_size(self, width:int, height:int) """
        pass

    def set_sync_size(self, sync_size): # real signature unknown; restored from __doc__
        """ set_sync_size(self, sync_size:bool) """
        pass

    def set_text_direction(self, text_dir): # real signature unknown; restored from __doc__
        """ set_text_direction(self, text_dir:Clutter.TextDirection) """
        pass

    def set_transform(self, transform=None): # real signature unknown; restored from __doc__
        """ set_transform(self, transform:Clutter.Matrix=None) """
        pass

    def set_translation(self, translate_x, translate_y, translate_z): # real signature unknown; restored from __doc__
        """ set_translation(self, translate_x:float, translate_y:float, translate_z:float) """
        pass

    def set_width(self, width): # real signature unknown; restored from __doc__
        """ set_width(self, width:float) """
        pass

    def set_x(self, x): # real signature unknown; restored from __doc__
        """ set_x(self, x:float) """
        pass

    def set_x_align(self, x_align): # real signature unknown; restored from __doc__
        """ set_x_align(self, x_align:Clutter.ActorAlign) """
        pass

    def set_x_expand(self, expand): # real signature unknown; restored from __doc__
        """ set_x_expand(self, expand:bool) """
        pass

    def set_y(self, y): # real signature unknown; restored from __doc__
        """ set_y(self, y:float) """
        pass

    def set_y_align(self, y_align): # real signature unknown; restored from __doc__
        """ set_y_align(self, y_align:Clutter.ActorAlign) """
        pass

    def set_y_expand(self, expand): # real signature unknown; restored from __doc__
        """ set_y_expand(self, expand:bool) """
        pass

    def set_z_position(self, z_position): # real signature unknown; restored from __doc__
        """ set_z_position(self, z_position:float) """
        pass

    def set_z_rotation_from_gravity(self, angle, gravity): # real signature unknown; restored from __doc__
        """ set_z_rotation_from_gravity(self, angle:float, gravity:Clutter.Gravity) """
        pass

    def should_pick_paint(self): # real signature unknown; restored from __doc__
        """ should_pick_paint(self) -> bool """
        return False

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def show_all(self): # real signature unknown; restored from __doc__
        """ show_all(self) """
        pass

    def sort_depth_order(self): # real signature unknown; restored from __doc__
        """ sort_depth_order(self) """
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

    def transform_stage_point(self, x, y): # real signature unknown; restored from __doc__
        """ transform_stage_point(self, x:float, y:float) -> bool, x_out:float, y_out:float """
        return False

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unrealize(self): # real signature unknown; restored from __doc__
        """ unrealize(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unset_flags(self, flags): # real signature unknown; restored from __doc__
        """ unset_flags(self, flags:Clutter.ActorFlags) """
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

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f5413425a00>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(CairoTexture), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterCairoTexture (94911696044544)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'clear': gi.FunctionInfo(clear), 'create': gi.FunctionInfo(create), 'create_region': gi.FunctionInfo(create_region), 'get_auto_resize': gi.FunctionInfo(get_auto_resize), 'get_surface_size': gi.FunctionInfo(get_surface_size), 'invalidate': gi.FunctionInfo(invalidate), 'invalidate_rectangle': gi.FunctionInfo(invalidate_rectangle), 'set_auto_resize': gi.FunctionInfo(set_auto_resize), 'set_surface_size': gi.FunctionInfo(set_surface_size), 'do_create_surface': gi.VFuncInfo(create_surface), 'do_draw': gi.VFuncInfo(draw), 'parent_instance': <property object at 0x7f5413dbf4f0>, 'priv': <property object at 0x7f5413dbf5e0>})"
    __gdoc__ = 'Object ClutterCairoTexture\n\nSignals from ClutterCairoTexture:\n  create-surface (guint, guint) -> CairoSurface\n  draw (CairoContext) -> gboolean\n\nProperties from ClutterCairoTexture:\n  surface-width -> guint: Surface Width\n    The width of the Cairo surface\n  surface-height -> guint: Surface Height\n    The height of the Cairo surface\n  auto-resize -> gboolean: Auto Resize\n    Whether the surface should match the allocation\n\nSignals from ClutterContainer:\n  actor-added (ClutterActor)\n  actor-removed (ClutterActor)\n  child-notify (ClutterActor, GParam)\n\nSignals from ClutterTexture:\n  size-change (gint, gint)\n  pixbuf-change ()\n  load-finished (GError)\n\nProperties from ClutterTexture:\n  disable-slicing -> gboolean: Disable Slicing\n    Forces the underlying texture to be singular and not made of smaller space saving individual textures\n  tile-waste -> gint: Tile Waste\n    Maximum waste area of a sliced texture\n  pixel-format -> CoglPixelFormat: Pixel Format\n    The Cogl pixel format to use\n  sync-size -> gboolean: Sync size of actor\n    Auto sync size of actor to underlying pixbuf dimensions\n  repeat-y -> gboolean: Vertical repeat\n    Repeat the contents rather than scaling them vertically\n  repeat-x -> gboolean: Horizontal repeat\n    Repeat the contents rather than scaling them horizontally\n  filter-quality -> ClutterTextureQuality: Filter Quality\n    Rendering quality used when drawing the texture\n  cogl-texture -> CoglHandle: Cogl Texture\n    The underlying Cogl texture handle used to draw this actor\n  cogl-material -> CoglHandle: Cogl Material\n    The underlying Cogl material handle used to draw this actor\n  filename -> gchararray: Filename\n    The path of the file containing the image data\n  keep-aspect-ratio -> gboolean: Keep Aspect Ratio\n    Keep the aspect ratio of the texture when requesting the preferred width or height\n  load-async -> gboolean: Load asynchronously\n    Load files inside a thread to avoid blocking when loading images from disk\n  load-data-async -> gboolean: Load data asynchronously\n    Decode image data files inside a thread to reduce blocking when loading images from disk\n  pick-with-alpha -> gboolean: Pick With Alpha\n    Shape actor with alpha channel when picking\n\nSignals from ClutterContainer:\n  actor-added (ClutterActor)\n  actor-removed (ClutterActor)\n  child-notify (ClutterActor, GParam)\n\nSignals from ClutterActor:\n  destroy ()\n  show ()\n  hide ()\n  parent-set (ClutterActor)\n  queue-redraw (ClutterActor)\n  queue-relayout ()\n  event (ClutterEvent) -> gboolean\n  button-press-event (ClutterEvent) -> gboolean\n  button-release-event (ClutterEvent) -> gboolean\n  scroll-event (ClutterEvent) -> gboolean\n  key-press-event (ClutterEvent) -> gboolean\n  key-release-event (ClutterEvent) -> gboolean\n  motion-event (ClutterEvent) -> gboolean\n  key-focus-in ()\n  key-focus-out ()\n  enter-event (ClutterEvent) -> gboolean\n  leave-event (ClutterEvent) -> gboolean\n  captured-event (ClutterEvent) -> gboolean\n  paint ()\n  realize ()\n  unrealize ()\n  pick (ClutterColor)\n  allocation-changed (ClutterActorBox, ClutterAllocationFlags)\n  transitions-completed ()\n  transition-stopped (gchararray, gboolean)\n  touch-event (ClutterEvent) -> gboolean\n\nProperties from ClutterActor:\n  name -> gchararray: Name\n    Name of the actor\n  x -> gfloat: X coordinate\n    X coordinate of the actor\n  y -> gfloat: Y coordinate\n    Y coordinate of the actor\n  width -> gfloat: Width\n    Width of the actor\n  height -> gfloat: Height\n    Height of the actor\n  position -> ClutterPoint: Position\n    The position of the origin of the actor\n  size -> ClutterSize: Size\n    The size of the actor\n  fixed-x -> gfloat: Fixed X\n    Forced X position of the actor\n  fixed-y -> gfloat: Fixed Y\n    Forced Y position of the actor\n  fixed-position-set -> gboolean: Fixed position set\n    Whether to use fixed positioning for the actor\n  min-width -> gfloat: Min Width\n    Forced minimum width request for the actor\n  min-width-set -> gboolean: Minimum width set\n    Whether to use the min-width property\n  min-height -> gfloat: Min Height\n    Forced minimum height request for the actor\n  min-height-set -> gboolean: Minimum height set\n    Whether to use the min-height property\n  natural-width -> gfloat: Natural Width\n    Forced natural width request for the actor\n  natural-width-set -> gboolean: Natural width set\n    Whether to use the natural-width property\n  natural-height -> gfloat: Natural Height\n    Forced natural height request for the actor\n  natural-height-set -> gboolean: Natural height set\n    Whether to use the natural-height property\n  request-mode -> ClutterRequestMode: Request Mode\n    The actor’s request mode\n  allocation -> ClutterActorBox: Allocation\n    The actor’s allocation\n  depth -> gfloat: Depth\n    Position on the Z axis\n  z-position -> gfloat: Z Position\n    The actor’s position on the Z axis\n  clip -> ClutterGeometry: Clip\n    The clip region for the actor\n  clip-rect -> ClutterRect: Clip Rectangle\n    The visible region of the actor\n  has-clip -> gboolean: Has Clip\n    Whether the actor has a clip set\n  clip-to-allocation -> gboolean: Clip to Allocation\n    Sets the clip region to track the actor’s allocation\n  opacity -> guint: Opacity\n    Opacity of an actor\n  offscreen-redirect -> ClutterOffscreenRedirect: Offscreen redirect\n    Flags controlling when to flatten the actor into a single image\n  visible -> gboolean: Visible\n    Whether the actor is visible or not\n  mapped -> gboolean: Mapped\n    Whether the actor will be painted\n  realized -> gboolean: Realized\n    Whether the actor has been realized\n  reactive -> gboolean: Reactive\n    Whether the actor is reactive to events\n  pivot-point -> ClutterPoint: Pivot Point\n    The point around which the scaling and rotation occur\n  pivot-point-z -> gfloat: Pivot Point Z\n    Z component of the pivot point\n  scale-x -> gdouble: Scale X\n    Scale factor on the X axis\n  scale-y -> gdouble: Scale Y\n    Scale factor on the Y axis\n  scale-z -> gdouble: Scale Z\n    Scale factor on the Z axis\n  scale-center-x -> gfloat: Scale Center X\n    Horizontal scale center\n  scale-center-y -> gfloat: Scale Center Y\n    Vertical scale center\n  scale-gravity -> ClutterGravity: Scale Gravity\n    The center of scaling\n  rotation-angle-x -> gdouble: Rotation Angle X\n    The rotation angle on the X axis\n  rotation-angle-y -> gdouble: Rotation Angle Y\n    The rotation angle on the Y axis\n  rotation-angle-z -> gdouble: Rotation Angle Z\n    The rotation angle on the Z axis\n  rotation-center-x -> ClutterVertex: Rotation Center X\n    The rotation center on the X axis\n  rotation-center-y -> ClutterVertex: Rotation Center Y\n    The rotation center on the Y axis\n  rotation-center-z -> ClutterVertex: Rotation Center Z\n    The rotation center on the Z axis\n  rotation-center-z-gravity -> ClutterGravity: Rotation Center Z Gravity\n    Center point for rotation around the Z axis\n  anchor-x -> gfloat: Anchor X\n    X coordinate of the anchor point\n  anchor-y -> gfloat: Anchor Y\n    Y coordinate of the anchor point\n  anchor-gravity -> ClutterGravity: Anchor Gravity\n    The anchor point as a ClutterGravity\n  translation-x -> gfloat: Translation X\n    Translation along the X axis\n  translation-y -> gfloat: Translation Y\n    Translation along the Y axis\n  translation-z -> gfloat: Translation Z\n    Translation along the Z axis\n  transform -> ClutterMatrix: Transform\n    Transformation matrix\n  transform-set -> gboolean: Transform Set\n    Whether the transform property is set\n  child-transform -> ClutterMatrix: Child Transform\n    Children transformation matrix\n  child-transform-set -> gboolean: Child Transform Set\n    Whether the child-transform property is set\n  show-on-set-parent -> gboolean: Show on set parent\n    Whether the actor is shown when parented\n  text-direction -> ClutterTextDirection: Text Direction\n    Direction of the text\n  has-pointer -> gboolean: Has Pointer\n    Whether the actor contains the pointer of an input device\n  actions -> ClutterAction: Actions\n    Adds an action to the actor\n  constraints -> ClutterConstraint: Constraints\n    Adds a constraint to the actor\n  effect -> ClutterEffect: Effect\n    Add an effect to be applied on the actor\n  layout-manager -> ClutterLayoutManager: Layout Manager\n    The object controlling the layout of an actor’s children\n  x-expand -> gboolean: X Expand\n    Whether extra horizontal space should be assigned to the actor\n  y-expand -> gboolean: Y Expand\n    Whether extra vertical space should be assigned to the actor\n  x-align -> ClutterActorAlign: X Alignment\n    The alignment of the actor on the X axis within its allocation\n  y-align -> ClutterActorAlign: Y Alignment\n    The alignment of the actor on the Y axis within its allocation\n  margin-top -> gfloat: Margin Top\n    Extra space at the top\n  margin-bottom -> gfloat: Margin Bottom\n    Extra space at the bottom\n  margin-left -> gfloat: Margin Left\n    Extra space at the left\n  margin-right -> gfloat: Margin Right\n    Extra space at the right\n  background-color -> ClutterColor: Background color\n    The actor’s background color\n  background-color-set -> gboolean: Background Color Set\n    Whether the background color is set\n  first-child -> ClutterActor: First Child\n    The actor’s first child\n  last-child -> ClutterActor: Last Child\n    The actor’s last child\n  content -> ClutterContent: Content\n    Delegate object for painting the actor’s content\n  content-gravity -> ClutterContentGravity: Content Gravity\n    Alignment of the actor’s content\n  content-box -> ClutterActorBox: Content Box\n    The bounding box of the actor’s content\n  minification-filter -> ClutterScalingFilter: Minification Filter\n    The filter used when reducing the size of the content\n  magnification-filter -> ClutterScalingFilter: Magnification Filter\n    The filter used when increasing the size of the content\n  content-repeat -> ClutterContentRepeat: Content Repeat\n    The repeat policy for the actor’s content\n\nSignals from ClutterContainer:\n  actor-added (ClutterActor)\n  actor-removed (ClutterActor)\n  child-notify (ClutterActor, GParam)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ClutterCairoTexture (94911696044544)>'
    __info__ = ObjectInfo(CairoTexture)


