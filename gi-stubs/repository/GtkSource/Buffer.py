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


class Buffer(__gi_overrides_Gtk.TextBuffer):
    """
    :Constructors:
    
    ::
    
        Buffer(**properties)
        new(table:Gtk.TextTagTable=None) -> GtkSource.Buffer
        new_with_language(language:GtkSource.Language) -> GtkSource.Buffer
    """
    def add_mark(self, mark, where): # real signature unknown; restored from __doc__
        """ add_mark(self, mark:Gtk.TextMark, where:Gtk.TextIter) """
        pass

    def add_selection_clipboard(self, clipboard): # real signature unknown; restored from __doc__
        """ add_selection_clipboard(self, clipboard:Gtk.Clipboard) """
        pass

    def apply_tag(self, tag, start, end): # real signature unknown; restored from __doc__
        """ apply_tag(self, tag:Gtk.TextTag, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def apply_tag_by_name(self, name, start, end): # real signature unknown; restored from __doc__
        """ apply_tag_by_name(self, name:str, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def backspace(self, iter, interactive, default_editable): # real signature unknown; restored from __doc__
        """ backspace(self, iter:Gtk.TextIter, interactive:bool, default_editable:bool) -> bool """
        return False

    def backward_iter_to_source_mark(self, iter, category=None): # real signature unknown; restored from __doc__
        """ backward_iter_to_source_mark(self, iter:Gtk.TextIter, category:str=None) -> bool, iter:Gtk.TextIter """
        return False

    def begin_not_undoable_action(self): # real signature unknown; restored from __doc__
        """ begin_not_undoable_action(self) """
        pass

    def begin_user_action(self): # real signature unknown; restored from __doc__
        """ begin_user_action(self) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_redo(self): # real signature unknown; restored from __doc__
        """ can_redo(self) -> bool """
        return False

    def can_undo(self): # real signature unknown; restored from __doc__
        """ can_undo(self) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_case(self, case_type, start, end): # real signature unknown; restored from __doc__
        """ change_case(self, case_type:GtkSource.ChangeCaseType, start:Gtk.TextIter, end:Gtk.TextIter) """
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

    def copy_clipboard(self, clipboard): # real signature unknown; restored from __doc__
        """ copy_clipboard(self, clipboard:Gtk.Clipboard) """
        pass

    def create_child_anchor(self, iter): # real signature unknown; restored from __doc__
        """ create_child_anchor(self, iter:Gtk.TextIter) -> Gtk.TextChildAnchor """
        pass

    def create_mark(self, mark_name, where, left_gravity=False): # reliably restored by inspect
        # no doc
        pass

    def create_source_mark(self, name=None, category, where): # real signature unknown; restored from __doc__
        """ create_source_mark(self, name:str=None, category:str, where:Gtk.TextIter) -> GtkSource.Mark """
        pass

    def create_tag(self, tag_name=None, **properties): # reliably restored by inspect
        """
        Creates a tag and adds it to the tag table of the TextBuffer.
        
                :param str tag_name:
                    Name of the new tag, or None
                :param **properties:
                    Keyword list of properties and their values
        
                This is equivalent to creating a Gtk.TextTag and then adding the
                tag to the buffer's tag table. The returned tag is owned by
                the buffer's tag table.
        
                If ``tag_name`` is None, the tag is anonymous.
        
                If ``tag_name`` is not None, a tag called ``tag_name`` must not already
                exist in the tag table for this buffer.
        
                Properties are passed as a keyword list of names and values (e.g.
                foreground='DodgerBlue', weight=Pango.Weight.BOLD)
        
                :returns:
                    A new tag.
        """
        pass

    def cut_clipboard(self, clipboard, default_editable): # real signature unknown; restored from __doc__
        """ cut_clipboard(self, clipboard:Gtk.Clipboard, default_editable:bool) """
        pass

    def delete(self, start, end): # real signature unknown; restored from __doc__
        """ delete(self, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def delete_interactive(self, start_iter, end_iter, default_editable): # real signature unknown; restored from __doc__
        """ delete_interactive(self, start_iter:Gtk.TextIter, end_iter:Gtk.TextIter, default_editable:bool) -> bool """
        return False

    def delete_mark(self, mark): # real signature unknown; restored from __doc__
        """ delete_mark(self, mark:Gtk.TextMark) """
        pass

    def delete_mark_by_name(self, name): # real signature unknown; restored from __doc__
        """ delete_mark_by_name(self, name:str) """
        pass

    def delete_selection(self, interactive, default_editable): # real signature unknown; restored from __doc__
        """ delete_selection(self, interactive:bool, default_editable:bool) -> bool """
        return False

    def deserialize(self, content_buffer, format, iter, data): # real signature unknown; restored from __doc__
        """ deserialize(self, content_buffer:Gtk.TextBuffer, format:Gdk.Atom, iter:Gtk.TextIter, data:list) -> bool """
        return False

    def deserialize_get_can_create_tags(self, format): # real signature unknown; restored from __doc__
        """ deserialize_get_can_create_tags(self, format:Gdk.Atom) -> bool """
        return False

    def deserialize_set_can_create_tags(self, format, can_create_tags): # real signature unknown; restored from __doc__
        """ deserialize_set_can_create_tags(self, format:Gdk.Atom, can_create_tags:bool) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_apply_tag(self, *args, **kwargs): # real signature unknown
        """ apply_tag(self, tag:Gtk.TextTag, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def do_begin_user_action(self, *args, **kwargs): # real signature unknown
        """ begin_user_action(self) """
        pass

    def do_bracket_matched(self, *args, **kwargs): # real signature unknown
        """ bracket_matched(self, iter:Gtk.TextIter, state:GtkSource.BracketMatchType) """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def do_delete_range(self, *args, **kwargs): # real signature unknown
        """ delete_range(self, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def do_end_user_action(self, *args, **kwargs): # real signature unknown
        """ end_user_action(self) """
        pass

    def do_insert_child_anchor(self, *args, **kwargs): # real signature unknown
        """ insert_child_anchor(self, iter:Gtk.TextIter, anchor:Gtk.TextChildAnchor) """
        pass

    def do_insert_pixbuf(self, *args, **kwargs): # real signature unknown
        """ insert_pixbuf(self, iter:Gtk.TextIter, pixbuf:GdkPixbuf.Pixbuf) """
        pass

    def do_insert_text(self, *args, **kwargs): # real signature unknown
        """ insert_text(self, pos:Gtk.TextIter, new_text:str, new_text_length:int) """
        pass

    def do_mark_deleted(self, *args, **kwargs): # real signature unknown
        """ mark_deleted(self, mark:Gtk.TextMark) """
        pass

    def do_mark_set(self, *args, **kwargs): # real signature unknown
        """ mark_set(self, location:Gtk.TextIter, mark:Gtk.TextMark) """
        pass

    def do_modified_changed(self, *args, **kwargs): # real signature unknown
        """ modified_changed(self) """
        pass

    def do_paste_done(self, *args, **kwargs): # real signature unknown
        """ paste_done(self, clipboard:Gtk.Clipboard) """
        pass

    def do_redo(self, *args, **kwargs): # real signature unknown
        """ redo(self) """
        pass

    def do_remove_tag(self, *args, **kwargs): # real signature unknown
        """ remove_tag(self, tag:Gtk.TextTag, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def do_undo(self, *args, **kwargs): # real signature unknown
        """ undo(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def end_not_undoable_action(self): # real signature unknown; restored from __doc__
        """ end_not_undoable_action(self) """
        pass

    def end_user_action(self): # real signature unknown; restored from __doc__
        """ end_user_action(self) """
        pass

    def ensure_highlight(self, start, end): # real signature unknown; restored from __doc__
        """ ensure_highlight(self, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def forward_iter_to_source_mark(self, iter, category=None): # real signature unknown; restored from __doc__
        """ forward_iter_to_source_mark(self, iter:Gtk.TextIter, category:str=None) -> bool, iter:Gtk.TextIter """
        return False

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

    def get_bounds(self): # real signature unknown; restored from __doc__
        """ get_bounds(self) -> start:Gtk.TextIter, end:Gtk.TextIter """
        pass

    def get_char_count(self): # real signature unknown; restored from __doc__
        """ get_char_count(self) -> int """
        return 0

    def get_context_classes_at_iter(self, iter): # real signature unknown; restored from __doc__
        """ get_context_classes_at_iter(self, iter:Gtk.TextIter) -> list """
        return []

    def get_copy_target_list(self): # real signature unknown; restored from __doc__
        """ get_copy_target_list(self) -> Gtk.TargetList """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_deserialize_formats(self): # real signature unknown; restored from __doc__
        """ get_deserialize_formats(self) -> list, n_formats:int """
        return []

    def get_end_iter(self): # real signature unknown; restored from __doc__
        """ get_end_iter(self) -> iter:Gtk.TextIter """
        pass

    def get_has_selection(self): # real signature unknown; restored from __doc__
        """ get_has_selection(self) -> bool """
        return False

    def get_highlight_matching_brackets(self): # real signature unknown; restored from __doc__
        """ get_highlight_matching_brackets(self) -> bool """
        return False

    def get_highlight_syntax(self): # real signature unknown; restored from __doc__
        """ get_highlight_syntax(self) -> bool """
        return False

    def get_implicit_trailing_newline(self): # real signature unknown; restored from __doc__
        """ get_implicit_trailing_newline(self) -> bool """
        return False

    def get_insert(self): # real signature unknown; restored from __doc__
        """ get_insert(self) -> Gtk.TextMark """
        pass

    def get_iter_at_child_anchor(self, anchor): # real signature unknown; restored from __doc__
        """ get_iter_at_child_anchor(self, anchor:Gtk.TextChildAnchor) -> iter:Gtk.TextIter """
        pass

    def get_iter_at_line(self, line_number): # real signature unknown; restored from __doc__
        """ get_iter_at_line(self, line_number:int) -> iter:Gtk.TextIter """
        pass

    def get_iter_at_line_index(self, line_number, byte_index): # real signature unknown; restored from __doc__
        """ get_iter_at_line_index(self, line_number:int, byte_index:int) -> iter:Gtk.TextIter """
        pass

    def get_iter_at_line_offset(self, line_number, char_offset): # real signature unknown; restored from __doc__
        """ get_iter_at_line_offset(self, line_number:int, char_offset:int) -> iter:Gtk.TextIter """
        pass

    def get_iter_at_mark(self, mark): # real signature unknown; restored from __doc__
        """ get_iter_at_mark(self, mark:Gtk.TextMark) -> iter:Gtk.TextIter """
        pass

    def get_iter_at_offset(self, char_offset): # real signature unknown; restored from __doc__
        """ get_iter_at_offset(self, char_offset:int) -> iter:Gtk.TextIter """
        pass

    def get_language(self): # real signature unknown; restored from __doc__
        """ get_language(self) -> GtkSource.Language or None """
        pass

    def get_line_count(self): # real signature unknown; restored from __doc__
        """ get_line_count(self) -> int """
        return 0

    def get_mark(self, name): # real signature unknown; restored from __doc__
        """ get_mark(self, name:str) -> Gtk.TextMark or None """
        pass

    def get_max_undo_levels(self): # real signature unknown; restored from __doc__
        """ get_max_undo_levels(self) -> int """
        return 0

    def get_modified(self): # real signature unknown; restored from __doc__
        """ get_modified(self) -> bool """
        return False

    def get_paste_target_list(self): # real signature unknown; restored from __doc__
        """ get_paste_target_list(self) -> Gtk.TargetList """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_selection_bound(self): # real signature unknown; restored from __doc__
        """ get_selection_bound(self) -> Gtk.TextMark """
        pass

    def get_selection_bounds(*args, **kwargs): # reliably restored by inspect
        """ get_selection_bounds(self) -> bool, start:Gtk.TextIter, end:Gtk.TextIter """
        pass

    def get_serialize_formats(self): # real signature unknown; restored from __doc__
        """ get_serialize_formats(self) -> list, n_formats:int """
        return []

    def get_slice(self, start, end, include_hidden_chars): # real signature unknown; restored from __doc__
        """ get_slice(self, start:Gtk.TextIter, end:Gtk.TextIter, include_hidden_chars:bool) -> str """
        return ""

    def get_source_marks_at_iter(self, iter, category=None): # real signature unknown; restored from __doc__
        """ get_source_marks_at_iter(self, iter:Gtk.TextIter, category:str=None) -> list """
        return []

    def get_source_marks_at_line(self, line, category=None): # real signature unknown; restored from __doc__
        """ get_source_marks_at_line(self, line:int, category:str=None) -> list """
        return []

    def get_start_iter(self): # real signature unknown; restored from __doc__
        """ get_start_iter(self) -> iter:Gtk.TextIter """
        pass

    def get_style_scheme(self): # real signature unknown; restored from __doc__
        """ get_style_scheme(self) -> GtkSource.StyleScheme or None """
        pass

    def get_tag_table(self): # real signature unknown; restored from __doc__
        """ get_tag_table(self) -> Gtk.TextTagTable """
        pass

    def get_text(self, start, end, include_hidden_chars): # real signature unknown; restored from __doc__
        """ get_text(self, start:Gtk.TextIter, end:Gtk.TextIter, include_hidden_chars:bool) -> str """
        return ""

    def get_undo_manager(self): # real signature unknown; restored from __doc__
        """ get_undo_manager(self) -> GtkSource.UndoManager or None """
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

    def insert(self, iter, text, length=-1): # reliably restored by inspect
        # no doc
        pass

    def insert_at_cursor(self, text, length=-1): # reliably restored by inspect
        # no doc
        pass

    def insert_child_anchor(self, iter, anchor): # real signature unknown; restored from __doc__
        """ insert_child_anchor(self, iter:Gtk.TextIter, anchor:Gtk.TextChildAnchor) """
        pass

    def insert_interactive(self, iter, text, len, default_editable): # real signature unknown; restored from __doc__
        """ insert_interactive(self, iter:Gtk.TextIter, text:str, len:int, default_editable:bool) -> bool """
        return False

    def insert_interactive_at_cursor(self, text, len, default_editable): # real signature unknown; restored from __doc__
        """ insert_interactive_at_cursor(self, text:str, len:int, default_editable:bool) -> bool """
        return False

    def insert_markup(self, iter, markup, len): # real signature unknown; restored from __doc__
        """ insert_markup(self, iter:Gtk.TextIter, markup:str, len:int) """
        pass

    def insert_pixbuf(self, iter, pixbuf): # real signature unknown; restored from __doc__
        """ insert_pixbuf(self, iter:Gtk.TextIter, pixbuf:GdkPixbuf.Pixbuf) """
        pass

    def insert_range(self, iter, start, end): # real signature unknown; restored from __doc__
        """ insert_range(self, iter:Gtk.TextIter, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def insert_range_interactive(self, iter, start, end, default_editable): # real signature unknown; restored from __doc__
        """ insert_range_interactive(self, iter:Gtk.TextIter, start:Gtk.TextIter, end:Gtk.TextIter, default_editable:bool) -> bool """
        return False

    def insert_with_tags(self, iter, text, *tags): # reliably restored by inspect
        # no doc
        pass

    def insert_with_tags_by_name(self, iter, text, *tags): # reliably restored by inspect
        # no doc
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

    def iter_backward_to_context_class_toggle(self, iter, context_class): # real signature unknown; restored from __doc__
        """ iter_backward_to_context_class_toggle(self, iter:Gtk.TextIter, context_class:str) -> bool, iter:Gtk.TextIter """
        return False

    def iter_forward_to_context_class_toggle(self, iter, context_class): # real signature unknown; restored from __doc__
        """ iter_forward_to_context_class_toggle(self, iter:Gtk.TextIter, context_class:str) -> bool, iter:Gtk.TextIter """
        return False

    def iter_has_context_class(self, iter, context_class): # real signature unknown; restored from __doc__
        """ iter_has_context_class(self, iter:Gtk.TextIter, context_class:str) -> bool """
        return False

    def join_lines(self, start, end): # real signature unknown; restored from __doc__
        """ join_lines(self, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def move_mark(self, mark, where): # real signature unknown; restored from __doc__
        """ move_mark(self, mark:Gtk.TextMark, where:Gtk.TextIter) """
        pass

    def move_mark_by_name(self, name, where): # real signature unknown; restored from __doc__
        """ move_mark_by_name(self, name:str, where:Gtk.TextIter) """
        pass

    def new(self, table=None): # real signature unknown; restored from __doc__
        """ new(table:Gtk.TextTagTable=None) -> GtkSource.Buffer """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_language(self, language): # real signature unknown; restored from __doc__
        """ new_with_language(language:GtkSource.Language) -> GtkSource.Buffer """
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

    def paste_clipboard(self, clipboard, override_location=None, default_editable): # real signature unknown; restored from __doc__
        """ paste_clipboard(self, clipboard:Gtk.Clipboard, override_location:Gtk.TextIter=None, default_editable:bool) """
        pass

    def place_cursor(self, where): # real signature unknown; restored from __doc__
        """ place_cursor(self, where:Gtk.TextIter) """
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register_deserialize_format(self, mime_type, function, user_data=None): # real signature unknown; restored from __doc__
        """ register_deserialize_format(self, mime_type:str, function:Gtk.TextBufferDeserializeFunc, user_data=None) -> Gdk.Atom """
        pass

    def register_deserialize_tagset(self, tagset_name=None): # real signature unknown; restored from __doc__
        """ register_deserialize_tagset(self, tagset_name:str=None) -> Gdk.Atom """
        pass

    def register_serialize_format(self, mime_type, function, user_data=None): # real signature unknown; restored from __doc__
        """ register_serialize_format(self, mime_type:str, function:Gtk.TextBufferSerializeFunc, user_data=None) -> Gdk.Atom """
        pass

    def register_serialize_tagset(self, tagset_name=None): # real signature unknown; restored from __doc__
        """ register_serialize_tagset(self, tagset_name:str=None) -> Gdk.Atom """
        pass

    def remove_all_tags(self, start, end): # real signature unknown; restored from __doc__
        """ remove_all_tags(self, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def remove_selection_clipboard(self, clipboard): # real signature unknown; restored from __doc__
        """ remove_selection_clipboard(self, clipboard:Gtk.Clipboard) """
        pass

    def remove_source_marks(self, start, end, category=None): # real signature unknown; restored from __doc__
        """ remove_source_marks(self, start:Gtk.TextIter, end:Gtk.TextIter, category:str=None) """
        pass

    def remove_tag(self, tag, start, end): # real signature unknown; restored from __doc__
        """ remove_tag(self, tag:Gtk.TextTag, start:Gtk.TextIter, end:Gtk.TextIter) """
        pass

    def remove_tag_by_name(self, name, start, end): # real signature unknown; restored from __doc__
        """ remove_tag_by_name(self, name:str, start:Gtk.TextIter, end:Gtk.TextIter) """
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

    def select_range(self, ins, bound): # real signature unknown; restored from __doc__
        """ select_range(self, ins:Gtk.TextIter, bound:Gtk.TextIter) """
        pass

    def serialize(self, content_buffer, format, start, end): # real signature unknown; restored from __doc__
        """ serialize(self, content_buffer:Gtk.TextBuffer, format:Gdk.Atom, start:Gtk.TextIter, end:Gtk.TextIter) -> list, length:int """
        return []

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_highlight_matching_brackets(self, highlight): # real signature unknown; restored from __doc__
        """ set_highlight_matching_brackets(self, highlight:bool) """
        pass

    def set_highlight_syntax(self, highlight): # real signature unknown; restored from __doc__
        """ set_highlight_syntax(self, highlight:bool) """
        pass

    def set_implicit_trailing_newline(self, implicit_trailing_newline): # real signature unknown; restored from __doc__
        """ set_implicit_trailing_newline(self, implicit_trailing_newline:bool) """
        pass

    def set_language(self, language=None): # real signature unknown; restored from __doc__
        """ set_language(self, language:GtkSource.Language=None) """
        pass

    def set_max_undo_levels(self, max_undo_levels): # real signature unknown; restored from __doc__
        """ set_max_undo_levels(self, max_undo_levels:int) """
        pass

    def set_modified(self, setting): # real signature unknown; restored from __doc__
        """ set_modified(self, setting:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_style_scheme(self, scheme=None): # real signature unknown; restored from __doc__
        """ set_style_scheme(self, scheme:GtkSource.StyleScheme=None) """
        pass

    def set_text(self, text, length=-1): # reliably restored by inspect
        # no doc
        pass

    def set_undo_manager(self, manager=None): # real signature unknown; restored from __doc__
        """ set_undo_manager(self, manager:GtkSource.UndoManager=None) """
        pass

    def sort_lines(self, start, end, flags, column): # real signature unknown; restored from __doc__
        """ sort_lines(self, start:Gtk.TextIter, end:Gtk.TextIter, flags:GtkSource.SortFlags, column:int) """
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

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unregister_deserialize_format(self, format): # real signature unknown; restored from __doc__
        """ unregister_deserialize_format(self, format:Gdk.Atom) """
        pass

    def unregister_serialize_format(self, format): # real signature unknown; restored from __doc__
        """ unregister_serialize_format(self, format:Gdk.Atom) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f77ca730d60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Buffer), '__module__': 'gi.repository.GtkSource', '__gtype__': <GType GtkSourceBuffer (94260244278416)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_with_language': gi.FunctionInfo(new_with_language), 'backward_iter_to_source_mark': gi.FunctionInfo(backward_iter_to_source_mark), 'begin_not_undoable_action': gi.FunctionInfo(begin_not_undoable_action), 'can_redo': gi.FunctionInfo(can_redo), 'can_undo': gi.FunctionInfo(can_undo), 'change_case': gi.FunctionInfo(change_case), 'create_source_mark': gi.FunctionInfo(create_source_mark), 'end_not_undoable_action': gi.FunctionInfo(end_not_undoable_action), 'ensure_highlight': gi.FunctionInfo(ensure_highlight), 'forward_iter_to_source_mark': gi.FunctionInfo(forward_iter_to_source_mark), 'get_context_classes_at_iter': gi.FunctionInfo(get_context_classes_at_iter), 'get_highlight_matching_brackets': gi.FunctionInfo(get_highlight_matching_brackets), 'get_highlight_syntax': gi.FunctionInfo(get_highlight_syntax), 'get_implicit_trailing_newline': gi.FunctionInfo(get_implicit_trailing_newline), 'get_language': gi.FunctionInfo(get_language), 'get_max_undo_levels': gi.FunctionInfo(get_max_undo_levels), 'get_source_marks_at_iter': gi.FunctionInfo(get_source_marks_at_iter), 'get_source_marks_at_line': gi.FunctionInfo(get_source_marks_at_line), 'get_style_scheme': gi.FunctionInfo(get_style_scheme), 'get_undo_manager': gi.FunctionInfo(get_undo_manager), 'iter_backward_to_context_class_toggle': gi.FunctionInfo(iter_backward_to_context_class_toggle), 'iter_forward_to_context_class_toggle': gi.FunctionInfo(iter_forward_to_context_class_toggle), 'iter_has_context_class': gi.FunctionInfo(iter_has_context_class), 'join_lines': gi.FunctionInfo(join_lines), 'redo': gi.FunctionInfo(redo), 'remove_source_marks': gi.FunctionInfo(remove_source_marks), 'set_highlight_matching_brackets': gi.FunctionInfo(set_highlight_matching_brackets), 'set_highlight_syntax': gi.FunctionInfo(set_highlight_syntax), 'set_implicit_trailing_newline': gi.FunctionInfo(set_implicit_trailing_newline), 'set_language': gi.FunctionInfo(set_language), 'set_max_undo_levels': gi.FunctionInfo(set_max_undo_levels), 'set_style_scheme': gi.FunctionInfo(set_style_scheme), 'set_undo_manager': gi.FunctionInfo(set_undo_manager), 'sort_lines': gi.FunctionInfo(sort_lines), 'undo': gi.FunctionInfo(undo), 'do_bracket_matched': gi.VFuncInfo(bracket_matched), 'do_redo': gi.VFuncInfo(redo), 'do_undo': gi.VFuncInfo(undo), 'parent_instance': <property object at 0x7f77ca6bddb0>, 'priv': <property object at 0x7f77ca6bde00>})"
    __gdoc__ = 'Object GtkSourceBuffer\n\nSignals from GtkSourceBuffer:\n  highlight-updated (GtkTextIter, GtkTextIter)\n  source-mark-updated (GtkTextMark)\n  undo ()\n  redo ()\n  bracket-matched (GtkTextIter, GtkSourceBracketMatchType)\n\nProperties from GtkSourceBuffer:\n  can-undo -> gboolean: Can undo\n    Whether Undo operation is possible\n  can-redo -> gboolean: Can redo\n    Whether Redo operation is possible\n  highlight-syntax -> gboolean: Highlight Syntax\n    Whether to highlight syntax in the buffer\n  highlight-matching-brackets -> gboolean: Highlight Matching Brackets\n    Whether to highlight matching brackets\n  max-undo-levels -> gint: Maximum Undo Levels\n    Number of undo levels for the buffer\n  language -> GtkSourceLanguage: Language\n    Language object to get highlighting patterns from\n  style-scheme -> GtkSourceStyleScheme: Style scheme\n    Style scheme\n  undo-manager -> GtkSourceUndoManager: Undo manager\n    The buffer undo manager\n  implicit-trailing-newline -> gboolean: Implicit trailing newline\n    \n\nSignals from GtkTextBuffer:\n  changed ()\n  insert-text (GtkTextIter, gchararray, gint)\n  insert-pixbuf (GtkTextIter, GdkPixbuf)\n  insert-child-anchor (GtkTextIter, GtkTextChildAnchor)\n  delete-range (GtkTextIter, GtkTextIter)\n  modified-changed ()\n  mark-set (GtkTextIter, GtkTextMark)\n  mark-deleted (GtkTextMark)\n  apply-tag (GtkTextTag, GtkTextIter, GtkTextIter)\n  remove-tag (GtkTextTag, GtkTextIter, GtkTextIter)\n  begin-user-action ()\n  end-user-action ()\n  paste-done (GtkClipboard)\n\nProperties from GtkTextBuffer:\n  tag-table -> GtkTextTagTable: Tag Table\n    Text Tag Table\n  text -> gchararray: Text\n    Current text of the buffer\n  has-selection -> gboolean: Has selection\n    Whether the buffer has some text currently selected\n  cursor-position -> gint: Cursor position\n    The position of the insert mark (as offset from the beginning of the buffer)\n  copy-target-list -> GtkTargetList: Copy target list\n    The list of targets this buffer supports for clipboard copying and DND source\n  paste-target-list -> GtkTargetList: Paste target list\n    The list of targets this buffer supports for clipboard pasting and DND destination\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkSourceBuffer (94260244278416)>'
    __info__ = ObjectInfo(Buffer)


