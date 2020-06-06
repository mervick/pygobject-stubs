# encoding: utf-8
# module gi.repository.Gcr
# from /usr/lib64/girepository-1.0/Gcr-3.typelib
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
import gi.repository.Gck as __gi_repository_Gck
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class Prompt(__gobject.GInterface):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def confirm(self, cancellable=None): # real signature unknown; restored from __doc__
        """ confirm(self, cancellable:Gio.Cancellable=None) -> Gcr.PromptReply """
        pass

    def confirm_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ confirm_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def confirm_finish(self, result): # real signature unknown; restored from __doc__
        """ confirm_finish(self, result:Gio.AsyncResult) -> Gcr.PromptReply """
        pass

    def confirm_run(self, cancellable=None): # real signature unknown; restored from __doc__
        """ confirm_run(self, cancellable:Gio.Cancellable=None) -> Gcr.PromptReply """
        pass

    def get_caller_window(self): # real signature unknown; restored from __doc__
        """ get_caller_window(self) -> str """
        return ""

    def get_cancel_label(self): # real signature unknown; restored from __doc__
        """ get_cancel_label(self) -> str """
        return ""

    def get_choice_chosen(self): # real signature unknown; restored from __doc__
        """ get_choice_chosen(self) -> bool """
        return False

    def get_choice_label(self): # real signature unknown; restored from __doc__
        """ get_choice_label(self) -> str """
        return ""

    def get_continue_label(self): # real signature unknown; restored from __doc__
        """ get_continue_label(self) -> str """
        return ""

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_message(self): # real signature unknown; restored from __doc__
        """ get_message(self) -> str """
        return ""

    def get_password_new(self): # real signature unknown; restored from __doc__
        """ get_password_new(self) -> bool """
        return False

    def get_password_strength(self): # real signature unknown; restored from __doc__
        """ get_password_strength(self) -> int """
        return 0

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_warning(self): # real signature unknown; restored from __doc__
        """ get_warning(self) -> str """
        return ""

    def password(self, cancellable=None): # real signature unknown; restored from __doc__
        """ password(self, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def password_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ password_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def password_finish(self, result): # real signature unknown; restored from __doc__
        """ password_finish(self, result:Gio.AsyncResult) -> str """
        return ""

    def password_run(self, cancellable=None): # real signature unknown; restored from __doc__
        """ password_run(self, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def set_caller_window(self, window_id): # real signature unknown; restored from __doc__
        """ set_caller_window(self, window_id:str) """
        pass

    def set_cancel_label(self, cancel_label): # real signature unknown; restored from __doc__
        """ set_cancel_label(self, cancel_label:str) """
        pass

    def set_choice_chosen(self, chosen): # real signature unknown; restored from __doc__
        """ set_choice_chosen(self, chosen:bool) """
        pass

    def set_choice_label(self, choice_label=None): # real signature unknown; restored from __doc__
        """ set_choice_label(self, choice_label:str=None) """
        pass

    def set_continue_label(self, continue_label): # real signature unknown; restored from __doc__
        """ set_continue_label(self, continue_label:str) """
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_message(self, message): # real signature unknown; restored from __doc__
        """ set_message(self, message:str) """
        pass

    def set_password_new(self, new_password): # real signature unknown; restored from __doc__
        """ set_password_new(self, new_password:bool) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_warning(self, warning=None): # real signature unknown; restored from __doc__
        """ set_warning(self, warning:str=None) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Prompt), '__module__': 'gi.repository.Gcr', '__gtype__': <GType GcrPrompt (94112497415680)>, '__dict__': <attribute '__dict__' of 'Prompt' objects>, '__weakref__': <attribute '__weakref__' of 'Prompt' objects>, '__doc__': None, '__gsignals__': {}, 'close': gi.FunctionInfo(close), 'confirm': gi.FunctionInfo(confirm), 'confirm_async': gi.FunctionInfo(confirm_async), 'confirm_finish': gi.FunctionInfo(confirm_finish), 'confirm_run': gi.FunctionInfo(confirm_run), 'get_caller_window': gi.FunctionInfo(get_caller_window), 'get_cancel_label': gi.FunctionInfo(get_cancel_label), 'get_choice_chosen': gi.FunctionInfo(get_choice_chosen), 'get_choice_label': gi.FunctionInfo(get_choice_label), 'get_continue_label': gi.FunctionInfo(get_continue_label), 'get_description': gi.FunctionInfo(get_description), 'get_message': gi.FunctionInfo(get_message), 'get_password_new': gi.FunctionInfo(get_password_new), 'get_password_strength': gi.FunctionInfo(get_password_strength), 'get_title': gi.FunctionInfo(get_title), 'get_warning': gi.FunctionInfo(get_warning), 'password': gi.FunctionInfo(password), 'password_async': gi.FunctionInfo(password_async), 'password_finish': gi.FunctionInfo(password_finish), 'password_run': gi.FunctionInfo(password_run), 'reset': gi.FunctionInfo(reset), 'set_caller_window': gi.FunctionInfo(set_caller_window), 'set_cancel_label': gi.FunctionInfo(set_cancel_label), 'set_choice_chosen': gi.FunctionInfo(set_choice_chosen), 'set_choice_label': gi.FunctionInfo(set_choice_label), 'set_continue_label': gi.FunctionInfo(set_continue_label), 'set_description': gi.FunctionInfo(set_description), 'set_message': gi.FunctionInfo(set_message), 'set_password_new': gi.FunctionInfo(set_password_new), 'set_title': gi.FunctionInfo(set_title), 'set_warning': gi.FunctionInfo(set_warning)})"
    __gdoc__ = 'Interface GcrPrompt\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GcrPrompt (94112497415680)>'
    __info__ = InterfaceInfo(Prompt)


