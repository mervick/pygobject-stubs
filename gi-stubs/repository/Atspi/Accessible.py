# encoding: utf-8
# module gi.repository.Atspi
# from /usr/lib64/girepository-1.0/Atspi-2.0.typelib
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

from .Action import Action

from .Collection import Collection

from .Component import Component

from .Document import Document

from .EditableText import EditableText

from .Hypertext import Hypertext

from .Image import Image

from .Selection import Selection

from .Table import Table

from .TableCell import TableCell

from .Text import Text

from .Value import Value

class Accessible(Object, Action, Collection, Component, Document, EditableText, Hypertext, Image, Selection, Table, TableCell, Text, Value):
    """
    :Constructors:
    
    ::
    
        Accessible(**properties)
    """
    def add_column_selection(self, column): # real signature unknown; restored from __doc__
        """ add_column_selection(self, column:int) -> bool """
        return False

    def add_row_selection(self, row): # real signature unknown; restored from __doc__
        """ add_row_selection(self, row:int) -> bool """
        return False

    def add_selection(self, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ add_selection(self, start_offset:int, end_offset:int) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_cache(self): # real signature unknown; restored from __doc__
        """ clear_cache(self) """
        pass

    def clear_selection(self): # real signature unknown; restored from __doc__
        """ clear_selection(self) -> bool """
        return False

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

    def contains(self, x, y, ctype): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, ctype:Atspi.CoordType) -> bool """
        return False

    def copy_text(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ copy_text(self, start_pos:int, end_pos:int) -> bool """
        return False

    def cut_text(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ cut_text(self, start_pos:int, end_pos:int) -> bool """
        return False

    def delete_text(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ delete_text(self, start_pos:int, end_pos:int) -> bool """
        return False

    def deselect_child(self, child_index): # real signature unknown; restored from __doc__
        """ deselect_child(self, child_index:int) -> bool """
        return False

    def deselect_selected_child(self, selected_child_index): # real signature unknown; restored from __doc__
        """ deselect_selected_child(self, selected_child_index:int) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_action(self, i): # real signature unknown; restored from __doc__
        """ do_action(self, i:int) -> bool """
        return False

    def do_region_changed(self, *args, **kwargs): # real signature unknown
        """ region_changed(self, current_offset:int, last_offset:int) """
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

    def get_accessible_at(self, row, column): # real signature unknown; restored from __doc__
        """ get_accessible_at(self, row:int, column:int) -> Atspi.Accessible """
        pass

    def get_accessible_at_point(self, x, y, ctype): # real signature unknown; restored from __doc__
        """ get_accessible_at_point(self, x:int, y:int, ctype:Atspi.CoordType) -> Atspi.Accessible or None """
        pass

    def get_accessible_id(self): # real signature unknown; restored from __doc__
        """ get_accessible_id(self) -> str """
        return ""

    def get_action_description(self, i): # real signature unknown; restored from __doc__
        """ get_action_description(self, i:int) -> str """
        return ""

    def get_action_iface(self): # real signature unknown; restored from __doc__
        """ get_action_iface(self) -> Atspi.Action """
        pass

    def get_action_name(self, i): # real signature unknown; restored from __doc__
        """ get_action_name(self, i:int) -> str """
        return ""

    def get_active_descendant(self): # real signature unknown; restored from __doc__
        """ get_active_descendant(self) -> Atspi.Accessible """
        pass

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_application(self): # real signature unknown; restored from __doc__
        """ get_application(self) -> Atspi.Accessible """
        pass

    def get_atspi_version(self): # real signature unknown; restored from __doc__
        """ get_atspi_version(self) -> str """
        return ""

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> dict """
        return {}

    def get_attributes_as_array(self): # real signature unknown; restored from __doc__
        """ get_attributes_as_array(self) -> list """
        return []

    def get_attribute_run(self, offset, include_defaults): # real signature unknown; restored from __doc__
        """ get_attribute_run(self, offset:int, include_defaults:bool) -> dict, start_offset:int, end_offset:int """
        return {}

    def get_bounded_ranges(self, x, y, width, height, type, clipTypeX, clipTypeY): # real signature unknown; restored from __doc__
        """ get_bounded_ranges(self, x:int, y:int, width:int, height:int, type:Atspi.CoordType, clipTypeX:Atspi.TextClipType, clipTypeY:Atspi.TextClipType) -> list """
        return []

    def get_caption(self): # real signature unknown; restored from __doc__
        """ get_caption(self) -> Atspi.Accessible """
        pass

    def get_caret_offset(self): # real signature unknown; restored from __doc__
        """ get_caret_offset(self) -> int """
        return 0

    def get_character_at_offset(self, offset): # real signature unknown; restored from __doc__
        """ get_character_at_offset(self, offset:int) -> int """
        return 0

    def get_character_count(self): # real signature unknown; restored from __doc__
        """ get_character_count(self) -> int """
        return 0

    def get_character_extents(self, offset, type): # real signature unknown; restored from __doc__
        """ get_character_extents(self, offset:int, type:Atspi.CoordType) -> Atspi.Rect """
        pass

    def get_child_at_index(self, child_index): # real signature unknown; restored from __doc__
        """ get_child_at_index(self, child_index:int) -> Atspi.Accessible """
        pass

    def get_child_count(self): # real signature unknown; restored from __doc__
        """ get_child_count(self) -> int """
        return 0

    def get_collection_iface(self): # real signature unknown; restored from __doc__
        """ get_collection_iface(self) -> Atspi.Collection """
        pass

    def get_column_at_index(self, index): # real signature unknown; restored from __doc__
        """ get_column_at_index(self, index:int) -> int """
        return 0

    def get_column_description(self, column): # real signature unknown; restored from __doc__
        """ get_column_description(self, column:int) -> str """
        return ""

    def get_column_extent_at(self, row, column): # real signature unknown; restored from __doc__
        """ get_column_extent_at(self, row:int, column:int) -> int """
        return 0

    def get_column_header(self, column): # real signature unknown; restored from __doc__
        """ get_column_header(self, column:int) -> Atspi.Accessible """
        pass

    def get_column_header_cells(self): # real signature unknown; restored from __doc__
        """ get_column_header_cells(self) -> list """
        return []

    def get_column_index(self): # real signature unknown; restored from __doc__
        """ get_column_index(self) -> int """
        return 0

    def get_column_span(self): # real signature unknown; restored from __doc__
        """ get_column_span(self) -> int """
        return 0

    def get_component_iface(self): # real signature unknown; restored from __doc__
        """ get_component_iface(self) -> Atspi.Component """
        pass

    def get_current_page_number(self): # real signature unknown; restored from __doc__
        """ get_current_page_number(self) -> int """
        return 0

    def get_current_value(self): # real signature unknown; restored from __doc__
        """ get_current_value(self) -> float """
        return 0.0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_attributes(self): # real signature unknown; restored from __doc__
        """ get_default_attributes(self) -> dict """
        return {}

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_document_attributes(self): # real signature unknown; restored from __doc__
        """ get_document_attributes(self) -> dict """
        return {}

    def get_document_attribute_value(self, attribute): # real signature unknown; restored from __doc__
        """ get_document_attribute_value(self, attribute:str) -> str """
        return ""

    def get_document_iface(self): # real signature unknown; restored from __doc__
        """ get_document_iface(self) -> Atspi.Document """
        pass

    def get_editable_text_iface(self): # real signature unknown; restored from __doc__
        """ get_editable_text_iface(self) -> Atspi.EditableText """
        pass

    def get_extents(self, ctype): # real signature unknown; restored from __doc__
        """ get_extents(self, ctype:Atspi.CoordType) -> Atspi.Rect """
        pass

    def get_hyperlink(self): # real signature unknown; restored from __doc__
        """ get_hyperlink(self) -> Atspi.Hyperlink """
        pass

    def get_hypertext_iface(self): # real signature unknown; restored from __doc__
        """ get_hypertext_iface(self) -> Atspi.Hypertext """
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> int """
        return 0

    def get_image_description(self): # real signature unknown; restored from __doc__
        """ get_image_description(self) -> str """
        return ""

    def get_image_extents(self, ctype): # real signature unknown; restored from __doc__
        """ get_image_extents(self, ctype:Atspi.CoordType) -> Atspi.Rect """
        pass

    def get_image_iface(self): # real signature unknown; restored from __doc__
        """ get_image_iface(self) -> Atspi.Image """
        pass

    def get_image_locale(self): # real signature unknown; restored from __doc__
        """ get_image_locale(self) -> str """
        return ""

    def get_image_position(self, ctype): # real signature unknown; restored from __doc__
        """ get_image_position(self, ctype:Atspi.CoordType) -> Atspi.Point """
        pass

    def get_image_size(self): # real signature unknown; restored from __doc__
        """ get_image_size(self) -> Atspi.Point """
        pass

    def get_index_at(self, row, column): # real signature unknown; restored from __doc__
        """ get_index_at(self, row:int, column:int) -> int """
        return 0

    def get_index_in_parent(self): # real signature unknown; restored from __doc__
        """ get_index_in_parent(self) -> int """
        return 0

    def get_interfaces(self): # real signature unknown; restored from __doc__
        """ get_interfaces(self) -> list """
        return []

    def get_key_binding(self, i): # real signature unknown; restored from __doc__
        """ get_key_binding(self, i:int) -> str """
        return ""

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atspi.ComponentLayer """
        pass

    def get_link(self, link_index): # real signature unknown; restored from __doc__
        """ get_link(self, link_index:int) -> Atspi.Hyperlink or None """
        pass

    def get_link_index(self, character_offset): # real signature unknown; restored from __doc__
        """ get_link_index(self, character_offset:int) -> int """
        return 0

    def get_locale(self): # real signature unknown; restored from __doc__
        """ get_locale(self) -> str """
        return ""

    def get_localized_name(self, i): # real signature unknown; restored from __doc__
        """ get_localized_name(self, i:int) -> str """
        return ""

    def get_localized_role_name(self): # real signature unknown; restored from __doc__
        """ get_localized_role_name(self) -> str """
        return ""

    def get_matches(self, rule, sortby, count, traverse): # real signature unknown; restored from __doc__
        """ get_matches(self, rule:Atspi.MatchRule, sortby:Atspi.CollectionSortOrder, count:int, traverse:bool) -> list """
        return []

    def get_matches_from(self, current_object, rule, sortby, tree, count, traverse): # real signature unknown; restored from __doc__
        """ get_matches_from(self, current_object:Atspi.Accessible, rule:Atspi.MatchRule, sortby:Atspi.CollectionSortOrder, tree:Atspi.CollectionTreeTraversalType, count:int, traverse:bool) -> list """
        return []

    def get_matches_to(self, current_object, rule, sortby, tree, limit_scope, count, traverse): # real signature unknown; restored from __doc__
        """ get_matches_to(self, current_object:Atspi.Accessible, rule:Atspi.MatchRule, sortby:Atspi.CollectionSortOrder, tree:Atspi.CollectionTreeTraversalType, limit_scope:bool, count:int, traverse:bool) -> list """
        return []

    def get_maximum_value(self): # real signature unknown; restored from __doc__
        """ get_maximum_value(self) -> float """
        return 0.0

    def get_mdi_z_order(self): # real signature unknown; restored from __doc__
        """ get_mdi_z_order(self) -> int """
        return 0

    def get_minimum_increment(self): # real signature unknown; restored from __doc__
        """ get_minimum_increment(self) -> float """
        return 0.0

    def get_minimum_value(self): # real signature unknown; restored from __doc__
        """ get_minimum_value(self) -> float """
        return 0.0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_actions(self): # real signature unknown; restored from __doc__
        """ get_n_actions(self) -> int """
        return 0

    def get_n_columns(self): # real signature unknown; restored from __doc__
        """ get_n_columns(self) -> int """
        return 0

    def get_n_links(self): # real signature unknown; restored from __doc__
        """ get_n_links(self) -> int """
        return 0

    def get_n_rows(self): # real signature unknown; restored from __doc__
        """ get_n_rows(self) -> int """
        return 0

    def get_n_selected_children(self): # real signature unknown; restored from __doc__
        """ get_n_selected_children(self) -> int """
        return 0

    def get_n_selected_columns(self): # real signature unknown; restored from __doc__
        """ get_n_selected_columns(self) -> int """
        return 0

    def get_n_selected_rows(self): # real signature unknown; restored from __doc__
        """ get_n_selected_rows(self) -> int """
        return 0

    def get_n_selections(self): # real signature unknown; restored from __doc__
        """ get_n_selections(self) -> int """
        return 0

    def get_object_locale(self): # real signature unknown; restored from __doc__
        """ get_object_locale(self) -> str """
        return ""

    def get_offset_at_point(self, x, y, type): # real signature unknown; restored from __doc__
        """ get_offset_at_point(self, x:int, y:int, type:Atspi.CoordType) -> int """
        return 0

    def get_page_count(self): # real signature unknown; restored from __doc__
        """ get_page_count(self) -> int """
        return 0

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Atspi.Accessible or None """
        pass

    def get_position(self, ctype): # real signature unknown; restored from __doc__
        """ get_position(self, ctype:Atspi.CoordType) -> Atspi.Point """
        pass

    def get_process_id(self): # real signature unknown; restored from __doc__
        """ get_process_id(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_range_extents(self, start_offset, end_offset, type): # real signature unknown; restored from __doc__
        """ get_range_extents(self, start_offset:int, end_offset:int, type:Atspi.CoordType) -> Atspi.Rect """
        pass

    def get_relation_set(self): # real signature unknown; restored from __doc__
        """ get_relation_set(self) -> list """
        return []

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> Atspi.Role """
        pass

    def get_role_name(self): # real signature unknown; restored from __doc__
        """ get_role_name(self) -> str """
        return ""

    def get_row_at_index(self, index): # real signature unknown; restored from __doc__
        """ get_row_at_index(self, index:int) -> int """
        return 0

    def get_row_column_extents_at_index(self, index): # real signature unknown; restored from __doc__
        """ get_row_column_extents_at_index(self, index:int) -> bool, row:int, col:int, row_extents:int, col_extents:int, is_selected:bool """
        return False

    def get_row_column_span(self): # real signature unknown; restored from __doc__
        """ get_row_column_span(self) -> row:int, column:int, row_span:int, column_span:int """
        pass

    def get_row_description(self, row): # real signature unknown; restored from __doc__
        """ get_row_description(self, row:int) -> str """
        return ""

    def get_row_extent_at(self, row, column): # real signature unknown; restored from __doc__
        """ get_row_extent_at(self, row:int, column:int) -> int """
        return 0

    def get_row_header(self, row): # real signature unknown; restored from __doc__
        """ get_row_header(self, row:int) -> Atspi.Accessible """
        pass

    def get_row_header_cells(self): # real signature unknown; restored from __doc__
        """ get_row_header_cells(self) -> list """
        return []

    def get_row_span(self): # real signature unknown; restored from __doc__
        """ get_row_span(self) -> int """
        return 0

    def get_selected_child(self, selected_child_index): # real signature unknown; restored from __doc__
        """ get_selected_child(self, selected_child_index:int) -> Atspi.Accessible """
        pass

    def get_selected_columns(self): # real signature unknown; restored from __doc__
        """ get_selected_columns(self) -> list """
        return []

    def get_selected_rows(self): # real signature unknown; restored from __doc__
        """ get_selected_rows(self) -> list """
        return []

    def get_selection(self, selection_num): # real signature unknown; restored from __doc__
        """ get_selection(self, selection_num:int) -> Atspi.Range """
        pass

    def get_selection_iface(self): # real signature unknown; restored from __doc__
        """ get_selection_iface(self) -> Atspi.Selection """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> Atspi.Point """
        pass

    def get_state_set(self): # real signature unknown; restored from __doc__
        """ get_state_set(self) -> Atspi.StateSet """
        pass

    def get_string_at_offset(self, offset, granularity): # real signature unknown; restored from __doc__
        """ get_string_at_offset(self, offset:int, granularity:Atspi.TextGranularity) -> Atspi.TextRange """
        pass

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> Atspi.Accessible """
        pass

    def get_table(self): # real signature unknown; restored from __doc__
        """ get_table(self) -> Atspi.Accessible """
        pass

    def get_table_cell(self): # real signature unknown; restored from __doc__
        """ get_table_cell(self) -> Atspi.TableCell """
        pass

    def get_table_iface(self): # real signature unknown; restored from __doc__
        """ get_table_iface(self) -> Atspi.Table """
        pass

    def get_text(self, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ get_text(self, start_offset:int, end_offset:int) -> str """
        return ""

    def get_text_after_offset(self, offset, type): # real signature unknown; restored from __doc__
        """ get_text_after_offset(self, offset:int, type:Atspi.TextBoundaryType) -> Atspi.TextRange """
        pass

    def get_text_attributes(self, offset): # real signature unknown; restored from __doc__
        """ get_text_attributes(self, offset:int) -> dict, start_offset:int, end_offset:int """
        return {}

    def get_text_attribute_value(self, offset, attribute_name): # real signature unknown; restored from __doc__
        """ get_text_attribute_value(self, offset:int, attribute_name:str) -> str or None """
        return ""

    def get_text_at_offset(self, offset, type): # real signature unknown; restored from __doc__
        """ get_text_at_offset(self, offset:int, type:Atspi.TextBoundaryType) -> Atspi.TextRange """
        pass

    def get_text_before_offset(self, offset, type): # real signature unknown; restored from __doc__
        """ get_text_before_offset(self, offset:int, type:Atspi.TextBoundaryType) -> Atspi.TextRange """
        pass

    def get_text_iface(self): # real signature unknown; restored from __doc__
        """ get_text_iface(self) -> Atspi.Text """
        pass

    def get_toolkit_name(self): # real signature unknown; restored from __doc__
        """ get_toolkit_name(self) -> str """
        return ""

    def get_toolkit_version(self): # real signature unknown; restored from __doc__
        """ get_toolkit_version(self) -> str """
        return ""

    def get_value_iface(self): # real signature unknown; restored from __doc__
        """ get_value_iface(self) -> Atspi.Value """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
        return False

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

    def insert_text(self, position, text, length): # real signature unknown; restored from __doc__
        """ insert_text(self, position:int, text:str, length:int) -> bool """
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

    def is_ancestor_of(self, test): # real signature unknown; restored from __doc__
        """ is_ancestor_of(self, test:Atspi.Accessible) -> bool """
        return False

    def is_child_selected(self, child_index): # real signature unknown; restored from __doc__
        """ is_child_selected(self, child_index:int) -> bool """
        return False

    def is_column_selected(self, column): # real signature unknown; restored from __doc__
        """ is_column_selected(self, column:int) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_row_selected(self, row): # real signature unknown; restored from __doc__
        """ is_row_selected(self, row:int) -> bool """
        return False

    def is_selected(self, row, column): # real signature unknown; restored from __doc__
        """ is_selected(self, row:int, column:int) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

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

    def paste_text(self, position): # real signature unknown; restored from __doc__
        """ paste_text(self, position:int) -> bool """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_column_selection(self, column): # real signature unknown; restored from __doc__
        """ remove_column_selection(self, column:int) -> bool """
        return False

    def remove_row_selection(self, row): # real signature unknown; restored from __doc__
        """ remove_row_selection(self, row:int) -> bool """
        return False

    def remove_selection(self, selection_num): # real signature unknown; restored from __doc__
        """ remove_selection(self, selection_num:int) -> bool """
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

    def scroll_substring_to(self, start_offset, end_offset, type): # real signature unknown; restored from __doc__
        """ scroll_substring_to(self, start_offset:int, end_offset:int, type:Atspi.ScrollType) -> bool """
        return False

    def scroll_substring_to_point(self, start_offset, end_offset, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_substring_to_point(self, start_offset:int, end_offset:int, coords:Atspi.CoordType, x:int, y:int) -> bool """
        return False

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atspi.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atspi.CoordType, x:int, y:int) -> bool """
        return False

    def select_all(self): # real signature unknown; restored from __doc__
        """ select_all(self) -> bool """
        return False

    def select_child(self, child_index): # real signature unknown; restored from __doc__
        """ select_child(self, child_index:int) -> bool """
        return False

    def set_cache_mask(self, mask): # real signature unknown; restored from __doc__
        """ set_cache_mask(self, mask:Atspi.Cache) """
        pass

    def set_caret_offset(self, new_offset): # real signature unknown; restored from __doc__
        """ set_caret_offset(self, new_offset:int) -> bool """
        return False

    def set_current_value(self, new_value): # real signature unknown; restored from __doc__
        """ set_current_value(self, new_value:float) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_extents(self, x, y, width, height, ctype): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, ctype:Atspi.CoordType) -> bool """
        return False

    def set_position(self, x, y, ctype): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, ctype:Atspi.CoordType) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_selection(self, selection_num, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ set_selection(self, selection_num:int, start_offset:int, end_offset:int) -> bool """
        return False

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
        return False

    def set_text_contents(self, new_contents): # real signature unknown; restored from __doc__
        """ set_text_contents(self, new_contents:str) -> bool """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    accessible_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    app = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cached_properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f9872e81400>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Accessible), '__module__': 'gi.repository.Atspi', '__gtype__': <GType AtspiAccessible (94141573267936)>, '__doc__': None, '__gsignals__': {}, 'clear_cache': gi.FunctionInfo(clear_cache), 'get_accessible_id': gi.FunctionInfo(get_accessible_id), 'get_action_iface': gi.FunctionInfo(get_action_iface), 'get_application': gi.FunctionInfo(get_application), 'get_atspi_version': gi.FunctionInfo(get_atspi_version), 'get_attributes': gi.FunctionInfo(get_attributes), 'get_attributes_as_array': gi.FunctionInfo(get_attributes_as_array), 'get_child_at_index': gi.FunctionInfo(get_child_at_index), 'get_child_count': gi.FunctionInfo(get_child_count), 'get_collection_iface': gi.FunctionInfo(get_collection_iface), 'get_component_iface': gi.FunctionInfo(get_component_iface), 'get_description': gi.FunctionInfo(get_description), 'get_document_iface': gi.FunctionInfo(get_document_iface), 'get_editable_text_iface': gi.FunctionInfo(get_editable_text_iface), 'get_hyperlink': gi.FunctionInfo(get_hyperlink), 'get_hypertext_iface': gi.FunctionInfo(get_hypertext_iface), 'get_id': gi.FunctionInfo(get_id), 'get_image_iface': gi.FunctionInfo(get_image_iface), 'get_index_in_parent': gi.FunctionInfo(get_index_in_parent), 'get_interfaces': gi.FunctionInfo(get_interfaces), 'get_localized_role_name': gi.FunctionInfo(get_localized_role_name), 'get_name': gi.FunctionInfo(get_name), 'get_object_locale': gi.FunctionInfo(get_object_locale), 'get_parent': gi.FunctionInfo(get_parent), 'get_process_id': gi.FunctionInfo(get_process_id), 'get_relation_set': gi.FunctionInfo(get_relation_set), 'get_role': gi.FunctionInfo(get_role), 'get_role_name': gi.FunctionInfo(get_role_name), 'get_selection_iface': gi.FunctionInfo(get_selection_iface), 'get_state_set': gi.FunctionInfo(get_state_set), 'get_table_iface': gi.FunctionInfo(get_table_iface), 'get_table_cell': gi.FunctionInfo(get_table_cell), 'get_text_iface': gi.FunctionInfo(get_text_iface), 'get_toolkit_name': gi.FunctionInfo(get_toolkit_name), 'get_toolkit_version': gi.FunctionInfo(get_toolkit_version), 'get_value_iface': gi.FunctionInfo(get_value_iface), 'set_cache_mask': gi.FunctionInfo(set_cache_mask), 'do_region_changed': gi.VFuncInfo(region_changed), 'parent': <property object at 0x7f9872e92c20>, 'accessible_parent': <property object at 0x7f9872e92d60>, 'children': <property object at 0x7f9872e92e50>, 'role': <property object at 0x7f9872e92f40>, 'interfaces': <property object at 0x7f9872e96090>, 'name': <property object at 0x7f9872e96180>, 'description': <property object at 0x7f9872e96270>, 'states': <property object at 0x7f9872e96360>, 'attributes': <property object at 0x7f9872e96450>, 'cached_properties': <property object at 0x7f9872e96590>, 'priv': <property object at 0x7f9872e96680>})"
    __gdoc__ = 'Object AtspiAccessible\n\nSignals from AtspiAccessible:\n  region-changed (gint, gint)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtspiAccessible (94141573267936)>'
    __info__ = ObjectInfo(Accessible)


