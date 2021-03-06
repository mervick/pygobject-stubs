# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


from .SourceExtension import SourceExtension

class SourceMailComposition(SourceExtension):
    """
    :Constructors:
    
    ::
    
        SourceMailComposition(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def dup_bcc(self): # real signature unknown; restored from __doc__
        """ dup_bcc(self) -> list """
        return []

    def dup_cc(self): # real signature unknown; restored from __doc__
        """ dup_cc(self) -> list """
        return []

    def dup_drafts_folder(self): # real signature unknown; restored from __doc__
        """ dup_drafts_folder(self) -> str """
        return ""

    def dup_language(self): # real signature unknown; restored from __doc__
        """ dup_language(self) -> str """
        return ""

    def dup_templates_folder(self): # real signature unknown; restored from __doc__
        """ dup_templates_folder(self) -> str """
        return ""

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

    def get_bcc(self): # real signature unknown; restored from __doc__
        """ get_bcc(self) -> list """
        return []

    def get_cc(self): # real signature unknown; restored from __doc__
        """ get_cc(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_drafts_folder(self): # real signature unknown; restored from __doc__
        """ get_drafts_folder(self) -> str """
        return ""

    def get_language(self): # real signature unknown; restored from __doc__
        """ get_language(self) -> str or None """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_reply_style(self): # real signature unknown; restored from __doc__
        """ get_reply_style(self) -> EDataServer.SourceMailCompositionReplyStyle """
        pass

    def get_sign_imip(self): # real signature unknown; restored from __doc__
        """ get_sign_imip(self) -> bool """
        return False

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> EDataServer.Source """
        pass

    def get_start_bottom(self): # real signature unknown; restored from __doc__
        """ get_start_bottom(self) -> EDataServer.ThreeState """
        pass

    def get_templates_folder(self): # real signature unknown; restored from __doc__
        """ get_templates_folder(self) -> str """
        return ""

    def get_top_signature(self): # real signature unknown; restored from __doc__
        """ get_top_signature(self) -> EDataServer.ThreeState """
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

    def property_lock(self): # real signature unknown; restored from __doc__
        """ property_lock(self) """
        pass

    def property_unlock(self): # real signature unknown; restored from __doc__
        """ property_unlock(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_source(self): # real signature unknown; restored from __doc__
        """ ref_source(self) -> EDataServer.Source """
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

    def set_bcc(self, bcc): # real signature unknown; restored from __doc__
        """ set_bcc(self, bcc:list) """
        pass

    def set_cc(self, cc): # real signature unknown; restored from __doc__
        """ set_cc(self, cc:list) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_drafts_folder(self, drafts_folder=None): # real signature unknown; restored from __doc__
        """ set_drafts_folder(self, drafts_folder:str=None) """
        pass

    def set_language(self, language=None): # real signature unknown; restored from __doc__
        """ set_language(self, language:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_reply_style(self, reply_style): # real signature unknown; restored from __doc__
        """ set_reply_style(self, reply_style:EDataServer.SourceMailCompositionReplyStyle) """
        pass

    def set_sign_imip(self, sign_imip): # real signature unknown; restored from __doc__
        """ set_sign_imip(self, sign_imip:bool) """
        pass

    def set_start_bottom(self, start_bottom): # real signature unknown; restored from __doc__
        """ set_start_bottom(self, start_bottom:EDataServer.ThreeState) """
        pass

    def set_templates_folder(self, templates_folder=None): # real signature unknown; restored from __doc__
        """ set_templates_folder(self, templates_folder:str=None) """
        pass

    def set_top_signature(self, top_signature): # real signature unknown; restored from __doc__
        """ set_top_signature(self, top_signature:EDataServer.ThreeState) """
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

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f626e645910>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SourceMailComposition), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType ESourceMailComposition (94877537188656)>, '__doc__': None, '__gsignals__': {}, 'dup_bcc': gi.FunctionInfo(dup_bcc), 'dup_cc': gi.FunctionInfo(dup_cc), 'dup_drafts_folder': gi.FunctionInfo(dup_drafts_folder), 'dup_language': gi.FunctionInfo(dup_language), 'dup_templates_folder': gi.FunctionInfo(dup_templates_folder), 'get_bcc': gi.FunctionInfo(get_bcc), 'get_cc': gi.FunctionInfo(get_cc), 'get_drafts_folder': gi.FunctionInfo(get_drafts_folder), 'get_language': gi.FunctionInfo(get_language), 'get_reply_style': gi.FunctionInfo(get_reply_style), 'get_sign_imip': gi.FunctionInfo(get_sign_imip), 'get_start_bottom': gi.FunctionInfo(get_start_bottom), 'get_templates_folder': gi.FunctionInfo(get_templates_folder), 'get_top_signature': gi.FunctionInfo(get_top_signature), 'set_bcc': gi.FunctionInfo(set_bcc), 'set_cc': gi.FunctionInfo(set_cc), 'set_drafts_folder': gi.FunctionInfo(set_drafts_folder), 'set_language': gi.FunctionInfo(set_language), 'set_reply_style': gi.FunctionInfo(set_reply_style), 'set_sign_imip': gi.FunctionInfo(set_sign_imip), 'set_start_bottom': gi.FunctionInfo(set_start_bottom), 'set_templates_folder': gi.FunctionInfo(set_templates_folder), 'set_top_signature': gi.FunctionInfo(set_top_signature), 'parent': <property object at 0x7f626e9354a0>, 'priv': <property object at 0x7f626e935590>})"
    __gdoc__ = 'Object ESourceMailComposition\n\nProperties from ESourceMailComposition:\n  bcc -> GStrv: Bcc\n    Recipients to blind carbon-copy\n  cc -> GStrv: Cc\n    Recipients to carbon-copy\n  drafts-folder -> gchararray: Drafts Folder\n    Preferred folder for draft messages\n  reply-style -> ESourceMailCompositionReplyStyle: Reply Style\n    What reply style to prefer\n  sign-imip -> gboolean: Sign iMIP\n    Include iMIP messages when signing\n  templates-folder -> gchararray: Templates Folder\n    Preferred folder for message templates\n  start-bottom -> EThreeState: Start Bottom\n    Whether start at bottom on reply or forward\n  top-signature -> EThreeState: Top Signature\n    Whether place signature at the top on reply or forward\n  language -> gchararray: Language\n    Preferred language\n\nProperties from ESourceExtension:\n  source -> ESource: Source\n    The ESource being extended\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ESourceMailComposition (94877537188656)>'
    __info__ = ObjectInfo(SourceMailComposition)


