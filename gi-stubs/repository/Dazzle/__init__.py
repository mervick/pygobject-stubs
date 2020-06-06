# encoding: utf-8
# module gi.repository.Dazzle
# from /usr/lib64/girepository-1.0/Dazzle-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


# Variables with simple values

COUNTER_REQUIRES_ATOMIC = 1

DOCK_BIN_STYLE_CLASS_PINNED = 'pinned'

ENABLE_TRACE = 0

MAJOR_VERSION = 3

MICRO_VERSION = 0

MINOR_VERSION = 36

VERSION_S = '3.36.0'

_namespace = 'Dazzle'

_version = '1.0'

__weakref__ = None

# functions

def cairo_region_create_from_clip_extents(cr): # real signature unknown; restored from __doc__
    """ cairo_region_create_from_clip_extents(cr:cairo.Context) -> cairo.Region """
    pass

def cairo_rounded_rectangle(cr, rect, x_radius, y_radius): # real signature unknown; restored from __doc__
    """ cairo_rounded_rectangle(cr:cairo.Context, rect:Gdk.Rectangle, x_radius:int, y_radius:int) """
    pass

def cancellable_chain(self=None, other=None): # real signature unknown; restored from __doc__
    """ cancellable_chain(self:Gio.Cancellable=None, other:Gio.Cancellable=None) -> Gio.Cancellable or None """
    pass

def counter_arena_get_default(): # real signature unknown; restored from __doc__
    """ counter_arena_get_default() -> Dazzle.CounterArena """
    pass

def dnd_get_uri_list(selection_data): # real signature unknown; restored from __doc__
    """ dnd_get_uri_list(selection_data:Gtk.SelectionData) -> list """
    return []

def file_manager_show(file): # real signature unknown; restored from __doc__
    """ file_manager_show(file:Gio.File) -> bool """
    return False

def frame_source_add(frames_per_sec, callback, user_data=None): # real signature unknown; restored from __doc__
    """ frame_source_add(frames_per_sec:int, callback:GLib.SourceFunc, user_data=None) -> int """
    return 0

def frame_source_add_full(priority, frames_per_sec, callback, user_data=None): # real signature unknown; restored from __doc__
    """ frame_source_add_full(priority:int, frames_per_sec:int, callback:GLib.SourceFunc, user_data=None) -> int """
    return 0

def fuzzy_highlight(p_str, query, case_sensitive): # real signature unknown; restored from __doc__
    """ fuzzy_highlight(str:str, query:str, case_sensitive:bool) -> str """
    return ""

def get_current_cpu_call(): # real signature unknown; restored from __doc__
    """ get_current_cpu_call() -> int """
    return 0

def gtk_list_store_insert_sorted(store, key=None, compare_column, compare_func, compare_data=None): # real signature unknown; restored from __doc__
    """ gtk_list_store_insert_sorted(store:Gtk.ListStore, key=None, compare_column:int, compare_func:GLib.CompareDataFunc, compare_data=None) -> iter:Gtk.TreeIter """
    pass

def gtk_text_buffer_remove_tag(buffer, tag, start, end, minimal_damage): # real signature unknown; restored from __doc__
    """ gtk_text_buffer_remove_tag(buffer:Gtk.TextBuffer, tag:Gtk.TextTag, start:Gtk.TextIter, end:Gtk.TextIter, minimal_damage:bool) """
    pass

def gtk_widget_action(widget, group, name, param): # real signature unknown; restored from __doc__
    """ gtk_widget_action(widget:Gtk.Widget, group:str, name:str, param:GLib.Variant) -> bool """
    return False

def gtk_widget_action_with_string(widget, group, name, param): # real signature unknown; restored from __doc__
    """ gtk_widget_action_with_string(widget:Gtk.Widget, group:str, name:str, param:str) -> bool """
    return False

def gtk_widget_add_style_class(widget, class_name): # real signature unknown; restored from __doc__
    """ gtk_widget_add_style_class(widget:Gtk.Widget, class_name:str) """
    pass

def gtk_widget_find_child_typed(widget, type): # real signature unknown; restored from __doc__
    """ gtk_widget_find_child_typed(widget:Gtk.Widget, type:GType) -> Gtk.Widget or None """
    pass

def gtk_widget_get_relative(widget, relative_type): # real signature unknown; restored from __doc__
    """ gtk_widget_get_relative(widget:Gtk.Widget, relative_type:GType) -> Gtk.Widget or None """
    pass

def gtk_widget_hide_with_fade(widget): # real signature unknown; restored from __doc__
    """ gtk_widget_hide_with_fade(widget:Gtk.Widget) """
    pass

def gtk_widget_is_ancestor_or_relative(widget, ancestor): # real signature unknown; restored from __doc__
    """ gtk_widget_is_ancestor_or_relative(widget:Gtk.Widget, ancestor:Gtk.Widget) -> bool """
    return False

def gtk_widget_mux_action_groups(widget, from_widget, mux_key=None): # real signature unknown; restored from __doc__
    """ gtk_widget_mux_action_groups(widget:Gtk.Widget, from_widget:Gtk.Widget, mux_key:str=None) """
    pass

def gtk_widget_remove_style_class(widget, class_name): # real signature unknown; restored from __doc__
    """ gtk_widget_remove_style_class(widget:Gtk.Widget, class_name:str) """
    pass

def gtk_widget_show_with_fade(widget): # real signature unknown; restored from __doc__
    """ gtk_widget_show_with_fade(widget:Gtk.Widget) """
    pass

def g_date_time_format_for_display(self): # real signature unknown; restored from __doc__
    """ g_date_time_format_for_display(self:GLib.DateTime) -> str """
    return ""

def g_time_span_to_label(span): # real signature unknown; restored from __doc__
    """ g_time_span_to_label(span:int) -> str """
    return ""

def g_time_span_to_label_mapping(binding, from_value, to_value, user_data=None): # real signature unknown; restored from __doc__
    """ g_time_span_to_label_mapping(binding:GObject.Binding, from_value:GObject.Value, to_value:GObject.Value, user_data=None) -> bool """
    return False

def g_variant_hash(data=None): # real signature unknown; restored from __doc__
    """ g_variant_hash(data=None) -> int """
    return 0

def levenshtein(needle, haystack): # real signature unknown; restored from __doc__
    """ levenshtein(needle:str, haystack:str) -> int """
    return 0

def overlay_add_child(self, child, type): # real signature unknown; restored from __doc__
    """ overlay_add_child(self:Dazzle.DockOverlay, child:Gtk.Widget, type:str) """
    pass

def pango_font_description_to_css(font_desc): # real signature unknown; restored from __doc__
    """ pango_font_description_to_css(font_desc:Pango.FontDescription) -> str """
    return ""

def rgba_shade(rgba, k): # real signature unknown; restored from __doc__
    """ rgba_shade(rgba:Gdk.RGBA, k:float) -> dst:Gdk.RGBA """
    pass

def shortcut_chord_equal(data1=None, data2=None): # real signature unknown; restored from __doc__
    """ shortcut_chord_equal(data1=None, data2=None) -> bool """
    return False

def shortcut_chord_hash(data=None): # real signature unknown; restored from __doc__
    """ shortcut_chord_hash(data=None) -> int """
    return 0

def shortcut_chord_table_get_type(): # real signature unknown; restored from __doc__
    """ shortcut_chord_table_get_type() -> GType """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .Animation import Animation
from .AnimationClass import AnimationClass
from .AnimationMode import AnimationMode
from .Application import Application
from .ApplicationClass import ApplicationClass
from .ApplicationWindow import ApplicationWindow
from .ApplicationWindowClass import ApplicationWindowClass
from .Bin import Bin
from .BinClass import BinClass
from .BindingGroup import BindingGroup
from .BindingGroupClass import BindingGroupClass
from .BoldingLabel import BoldingLabel
from .BoldingLabelClass import BoldingLabelClass
from .Box import Box
from .BoxClass import BoxClass
from .BoxTheatric import BoxTheatric
from .BoxTheatricClass import BoxTheatricClass
from .CenteringBin import CenteringBin
from .CenteringBinClass import CenteringBinClass
from .ChildPropertyAction import ChildPropertyAction
from .ChildPropertyActionClass import ChildPropertyActionClass
from .ColumnLayout import ColumnLayout
from .ColumnLayoutClass import ColumnLayoutClass
from .Counter import Counter
from .CounterArena import CounterArena
from .CountersWindow import CountersWindow
from .CountersWindowClass import CountersWindowClass
from .CounterValue import CounterValue
from .GraphView import GraphView
from .CpuGraph import CpuGraph
from .CpuGraphClass import CpuGraphClass
from .GraphModel import GraphModel
from .CpuModel import CpuModel
from .CpuModelClass import CpuModelClass
from .CssProvider import CssProvider
from .CssProviderClass import CssProviderClass
from .DirectoryModel import DirectoryModel
from .DirectoryModelClass import DirectoryModelClass
from .DirectoryReaper import DirectoryReaper
from .DirectoryReaperClass import DirectoryReaperClass
from .Dock import Dock
from .DockItem import DockItem
from .DockBin import DockBin
from .DockBinClass import DockBinClass
from .DockRevealer import DockRevealer
from .DockBinEdge import DockBinEdge
from .DockBinEdgeClass import DockBinEdgeClass
from .DockInterface import DockInterface
from .DockItemInterface import DockItemInterface
from .DockManager import DockManager
from .DockManagerClass import DockManagerClass
from .DockOverlay import DockOverlay
from .DockOverlayClass import DockOverlayClass
from .DockOverlayEdge import DockOverlayEdge
from .DockOverlayEdgeClass import DockOverlayEdgeClass
from .MultiPaned import MultiPaned
from .DockPaned import DockPaned
from .DockPanedClass import DockPanedClass
from .DockRevealerClass import DockRevealerClass
from .DockRevealerTransitionType import DockRevealerTransitionType
from .DockStack import DockStack
from .DockStackClass import DockStackClass
from .DockTransientGrab import DockTransientGrab
from .DockTransientGrabClass import DockTransientGrabClass
from .DockWidget import DockWidget
from .DockWidgetClass import DockWidgetClass
from .DockWindow import DockWindow
from .DockWindowClass import DockWindowClass
from .ElasticBin import ElasticBin
from .ElasticBinClass import ElasticBinClass
from .EmptyState import EmptyState
from .EmptyStateClass import EmptyStateClass
from .EntryBox import EntryBox
from .EntryBoxClass import EntryBoxClass
from .FileChooserEntry import FileChooserEntry
from .FileChooserEntryClass import FileChooserEntryClass
from .FileTransfer import FileTransfer
from .FileTransferClass import FileTransferClass
from .FileTransferFlags import FileTransferFlags
from .FileTransferStat import FileTransferStat
from .FuzzyIndex import FuzzyIndex
from .FuzzyIndexBuilder import FuzzyIndexBuilder
from .FuzzyIndexBuilderClass import FuzzyIndexBuilderClass
from .FuzzyIndexClass import FuzzyIndexClass
from .FuzzyIndexCursor import FuzzyIndexCursor
from .FuzzyIndexCursorClass import FuzzyIndexCursorClass
from .FuzzyIndexMatch import FuzzyIndexMatch
from .FuzzyIndexMatchClass import FuzzyIndexMatchClass
from .FuzzyMutableIndex import FuzzyMutableIndex
from .FuzzyMutableIndexMatch import FuzzyMutableIndexMatch
from .GraphColumn import GraphColumn
from .GraphColumnClass import GraphColumnClass
from .GraphRenderer import GraphRenderer
from .GraphLineRenderer import GraphLineRenderer
from .GraphLineRendererClass import GraphLineRendererClass
from .GraphModelClass import GraphModelClass
from .GraphModelIter import GraphModelIter
from .GraphRendererInterface import GraphRendererInterface
from .GraphViewClass import GraphViewClass
from .Heap import Heap
from .JoinedMenu import JoinedMenu
from .JoinedMenuClass import JoinedMenuClass
from .ListBox import ListBox
from .ListBoxClass import ListBoxClass
from .ListBoxRow import ListBoxRow
from .ListBoxRowClass import ListBoxRowClass
from .ListModelFilter import ListModelFilter
from .ListModelFilterClass import ListModelFilterClass
from .ListStoreAdapter import ListStoreAdapter
from .ListStoreAdapterClass import ListStoreAdapterClass
from .MenuButton import MenuButton
from .MenuButtonClass import MenuButtonClass
from .MenuManager import MenuManager
from .MenuManagerClass import MenuManagerClass
from .MultiPanedClass import MultiPanedClass
from .Path import Path
from .PathBar import PathBar
from .PathBarClass import PathBarClass
from .PathClass import PathClass
from .PathElement import PathElement
from .PathElementClass import PathElementClass
from .PatternSpec import PatternSpec
from .PillBox import PillBox
from .PillBoxClass import PillBoxClass
from .Preferences import Preferences
from .PreferencesBin import PreferencesBin
from .PreferencesBinClass import PreferencesBinClass
from .PreferencesEntry import PreferencesEntry
from .PreferencesEntryClass import PreferencesEntryClass
from .PreferencesFileChooserButton import PreferencesFileChooserButton
from .PreferencesFileChooserButtonClass import PreferencesFileChooserButtonClass
from .PreferencesFlowBox import PreferencesFlowBox
from .PreferencesFlowBoxClass import PreferencesFlowBoxClass
from .PreferencesFontButton import PreferencesFontButton
from .PreferencesFontButtonClass import PreferencesFontButtonClass
from .PreferencesGroup import PreferencesGroup
from .PreferencesGroupClass import PreferencesGroupClass
from .PreferencesInterface import PreferencesInterface
from .PreferencesPage import PreferencesPage
from .PreferencesPageClass import PreferencesPageClass
from .PreferencesSpinButton import PreferencesSpinButton
from .PreferencesSpinButtonClass import PreferencesSpinButtonClass
from .PreferencesSwitch import PreferencesSwitch
from .PreferencesSwitchClass import PreferencesSwitchClass
from .PreferencesView import PreferencesView
from .PreferencesViewClass import PreferencesViewClass
from .PriorityBox import PriorityBox
from .PriorityBoxClass import PriorityBoxClass
from .ProgressButton import ProgressButton
from .ProgressButtonClass import ProgressButtonClass
from .ProgressIcon import ProgressIcon
from .ProgressIconClass import ProgressIconClass
from .ProgressMenuButton import ProgressMenuButton
from .ProgressMenuButtonClass import ProgressMenuButtonClass
from .PropertiesFlags import PropertiesFlags
from .PropertiesGroup import PropertiesGroup
from .PropertiesGroupClass import PropertiesGroupClass
from .RadioBox import RadioBox
from .RadioBoxClass import RadioBoxClass
from .ReadOnlyListModel import ReadOnlyListModel
from .ReadOnlyListModelClass import ReadOnlyListModelClass
from .RecursiveFileMonitor import RecursiveFileMonitor
from .RecursiveFileMonitorClass import RecursiveFileMonitorClass
from .Ring import Ring
from .ScrolledWindow import ScrolledWindow
from .ScrolledWindowClass import ScrolledWindowClass
from .SearchBar import SearchBar
from .SearchBarClass import SearchBarClass
from .SettingsFlagAction import SettingsFlagAction
from .SettingsFlagActionClass import SettingsFlagActionClass
from .SettingsSandwich import SettingsSandwich
from .SettingsSandwichClass import SettingsSandwichClass
from .ShortcutAccelDialog import ShortcutAccelDialog
from .ShortcutAccelDialogClass import ShortcutAccelDialogClass
from .ShortcutChord import ShortcutChord
from .ShortcutChordTable import ShortcutChordTable
from .ShortcutContext import ShortcutContext
from .ShortcutContextClass import ShortcutContextClass
from .ShortcutController import ShortcutController
from .ShortcutControllerClass import ShortcutControllerClass
from .ShortcutEntry import ShortcutEntry
from .ShortcutLabel import ShortcutLabel
from .ShortcutLabelClass import ShortcutLabelClass
from .ShortcutManager import ShortcutManager
from .ShortcutManagerClass import ShortcutManagerClass
from .ShortcutMatch import ShortcutMatch
from .ShortcutModel import ShortcutModel
from .ShortcutModelClass import ShortcutModelClass
from .ShortcutPhase import ShortcutPhase
from .ShortcutsGroup import ShortcutsGroup
from .ShortcutsGroupClass import ShortcutsGroupClass
from .ShortcutSimpleLabel import ShortcutSimpleLabel
from .ShortcutSimpleLabelClass import ShortcutSimpleLabelClass
from .ShortcutsSection import ShortcutsSection
from .ShortcutsSectionClass import ShortcutsSectionClass
from .ShortcutsShortcut import ShortcutsShortcut
from .ShortcutsShortcutClass import ShortcutsShortcutClass
from .ShortcutsWindow import ShortcutsWindow
from .ShortcutsWindowClass import ShortcutsWindowClass
from .ShortcutTheme import ShortcutTheme
from .ShortcutThemeClass import ShortcutThemeClass
from .ShortcutThemeEditor import ShortcutThemeEditor
from .ShortcutThemeEditorClass import ShortcutThemeEditorClass
from .ShortcutTooltip import ShortcutTooltip
from .ShortcutTooltipClass import ShortcutTooltipClass
from .ShortcutType import ShortcutType
from .SignalGroup import SignalGroup
from .SignalGroupClass import SignalGroupClass
from .SimpleLabel import SimpleLabel
from .SimpleLabelClass import SimpleLabelClass
from .SimplePopover import SimplePopover
from .SimplePopoverClass import SimplePopoverClass
from .Slider import Slider
from .SliderClass import SliderClass
from .SliderPosition import SliderPosition
from .StackList import StackList
from .StackListClass import StackListClass
from .StateMachine import StateMachine
from .StateMachineClass import StateMachineClass
from .Suggestion import Suggestion
from .SuggestionButton import SuggestionButton
from .SuggestionButtonClass import SuggestionButtonClass
from .SuggestionClass import SuggestionClass
from .SuggestionEntry import SuggestionEntry
from .SuggestionEntryBuffer import SuggestionEntryBuffer
from .SuggestionEntryBufferClass import SuggestionEntryBufferClass
from .SuggestionEntryClass import SuggestionEntryClass
from .SuggestionPopover import SuggestionPopover
from .SuggestionPopoverClass import SuggestionPopoverClass
from .SuggestionRow import SuggestionRow
from .SuggestionRowClass import SuggestionRowClass
from .Tab import Tab
from .TabClass import TabClass
from .TabStrip import TabStrip
from .TabStripClass import TabStripClass
from .TabStyle import TabStyle
from .TaskCache import TaskCache
from .TaskCacheClass import TaskCacheClass
from .ThemeManager import ThemeManager
from .ThemeManagerClass import ThemeManagerClass
from .ThreeGrid import ThreeGrid
from .ThreeGridClass import ThreeGridClass
from .ThreeGridColumn import ThreeGridColumn
from .Tree import Tree
from .TreeBuilder import TreeBuilder
from .TreeBuilderClass import TreeBuilderClass
from .TreeClass import TreeClass
from .TreeDropPosition import TreeDropPosition
from .TreeNode import TreeNode
from .TreeNodeClass import TreeNodeClass
from .Trie import Trie
from .WidgetActionGroup import WidgetActionGroup
from .WidgetActionGroupClass import WidgetActionGroupClass
from ._GraphColumnClass import _GraphColumnClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f3b280ffd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Dazzle-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Dazzle', loader=<gi.importer.DynamicImporter object at 0x7f3b280ffd00>)"

