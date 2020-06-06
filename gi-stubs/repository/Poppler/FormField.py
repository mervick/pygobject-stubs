# encoding: utf-8
# module gi.repository.Poppler
# from /usr/lib64/girepository-1.0/Poppler-0.18.typelib
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


class FormField(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        FormField(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def button_get_button_type(self): # real signature unknown; restored from __doc__
        """ button_get_button_type(self) -> Poppler.FormButtonType """
        pass

    def button_get_state(self): # real signature unknown; restored from __doc__
        """ button_get_state(self) -> bool """
        return False

    def button_set_state(self, state): # real signature unknown; restored from __doc__
        """ button_set_state(self, state:bool) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def choice_can_select_multiple(self): # real signature unknown; restored from __doc__
        """ choice_can_select_multiple(self) -> bool """
        return False

    def choice_commit_on_change(self): # real signature unknown; restored from __doc__
        """ choice_commit_on_change(self) -> bool """
        return False

    def choice_do_spell_check(self): # real signature unknown; restored from __doc__
        """ choice_do_spell_check(self) -> bool """
        return False

    def choice_get_choice_type(self): # real signature unknown; restored from __doc__
        """ choice_get_choice_type(self) -> Poppler.FormChoiceType """
        pass

    def choice_get_item(self, index): # real signature unknown; restored from __doc__
        """ choice_get_item(self, index:int) -> str """
        return ""

    def choice_get_n_items(self): # real signature unknown; restored from __doc__
        """ choice_get_n_items(self) -> int """
        return 0

    def choice_get_text(self): # real signature unknown; restored from __doc__
        """ choice_get_text(self) -> str """
        return ""

    def choice_is_editable(self): # real signature unknown; restored from __doc__
        """ choice_is_editable(self) -> bool """
        return False

    def choice_is_item_selected(self, index): # real signature unknown; restored from __doc__
        """ choice_is_item_selected(self, index:int) -> bool """
        return False

    def choice_select_item(self, index): # real signature unknown; restored from __doc__
        """ choice_select_item(self, index:int) """
        pass

    def choice_set_text(self, text): # real signature unknown; restored from __doc__
        """ choice_set_text(self, text:str) """
        pass

    def choice_toggle_item(self, index): # real signature unknown; restored from __doc__
        """ choice_toggle_item(self, index:int) """
        pass

    def choice_unselect_all(self): # real signature unknown; restored from __doc__
        """ choice_unselect_all(self) """
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

    def get_action(self): # real signature unknown; restored from __doc__
        """ get_action(self) -> Poppler.Action """
        pass

    def get_additional_action(self, type): # real signature unknown; restored from __doc__
        """ get_additional_action(self, type:Poppler.AdditionalActionType) -> Poppler.Action """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_field_type(self): # real signature unknown; restored from __doc__
        """ get_field_type(self) -> Poppler.FormFieldType """
        pass

    def get_font_size(self): # real signature unknown; restored from __doc__
        """ get_font_size(self) -> float """
        return 0.0

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> int """
        return 0

    def get_mapping_name(self): # real signature unknown; restored from __doc__
        """ get_mapping_name(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_partial_name(self): # real signature unknown; restored from __doc__
        """ get_partial_name(self) -> str """
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

    def is_read_only(self): # real signature unknown; restored from __doc__
        """ is_read_only(self) -> bool """
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def text_do_scroll(self): # real signature unknown; restored from __doc__
        """ text_do_scroll(self) -> bool """
        return False

    def text_do_spell_check(self): # real signature unknown; restored from __doc__
        """ text_do_spell_check(self) -> bool """
        return False

    def text_get_max_len(self): # real signature unknown; restored from __doc__
        """ text_get_max_len(self) -> int """
        return 0

    def text_get_text(self): # real signature unknown; restored from __doc__
        """ text_get_text(self) -> str """
        return ""

    def text_get_text_type(self): # real signature unknown; restored from __doc__
        """ text_get_text_type(self) -> Poppler.FormTextType """
        pass

    def text_is_password(self): # real signature unknown; restored from __doc__
        """ text_is_password(self) -> bool """
        return False

    def text_is_rich_text(self): # real signature unknown; restored from __doc__
        """ text_is_rich_text(self) -> bool """
        return False

    def text_set_text(self, text): # real signature unknown; restored from __doc__
        """ text_set_text(self, text:str) """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f57e5e63c40>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(FormField), '__module__': 'gi.repository.Poppler', '__gtype__': <GType PopplerFormField (94391899079856)>, '__doc__': None, '__gsignals__': {}, 'button_get_button_type': gi.FunctionInfo(button_get_button_type), 'button_get_state': gi.FunctionInfo(button_get_state), 'button_set_state': gi.FunctionInfo(button_set_state), 'choice_can_select_multiple': gi.FunctionInfo(choice_can_select_multiple), 'choice_commit_on_change': gi.FunctionInfo(choice_commit_on_change), 'choice_do_spell_check': gi.FunctionInfo(choice_do_spell_check), 'choice_get_choice_type': gi.FunctionInfo(choice_get_choice_type), 'choice_get_item': gi.FunctionInfo(choice_get_item), 'choice_get_n_items': gi.FunctionInfo(choice_get_n_items), 'choice_get_text': gi.FunctionInfo(choice_get_text), 'choice_is_editable': gi.FunctionInfo(choice_is_editable), 'choice_is_item_selected': gi.FunctionInfo(choice_is_item_selected), 'choice_select_item': gi.FunctionInfo(choice_select_item), 'choice_set_text': gi.FunctionInfo(choice_set_text), 'choice_toggle_item': gi.FunctionInfo(choice_toggle_item), 'choice_unselect_all': gi.FunctionInfo(choice_unselect_all), 'get_action': gi.FunctionInfo(get_action), 'get_additional_action': gi.FunctionInfo(get_additional_action), 'get_field_type': gi.FunctionInfo(get_field_type), 'get_font_size': gi.FunctionInfo(get_font_size), 'get_id': gi.FunctionInfo(get_id), 'get_mapping_name': gi.FunctionInfo(get_mapping_name), 'get_name': gi.FunctionInfo(get_name), 'get_partial_name': gi.FunctionInfo(get_partial_name), 'is_read_only': gi.FunctionInfo(is_read_only), 'text_do_scroll': gi.FunctionInfo(text_do_scroll), 'text_do_spell_check': gi.FunctionInfo(text_do_spell_check), 'text_get_max_len': gi.FunctionInfo(text_get_max_len), 'text_get_text': gi.FunctionInfo(text_get_text), 'text_get_text_type': gi.FunctionInfo(text_get_text_type), 'text_is_password': gi.FunctionInfo(text_is_password), 'text_is_rich_text': gi.FunctionInfo(text_is_rich_text), 'text_set_text': gi.FunctionInfo(text_set_text)})"
    __gdoc__ = 'Object PopplerFormField\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PopplerFormField (94391899079856)>'
    __info__ = ObjectInfo(FormField)


