# encoding: utf-8
# module gi.repository.WebKit2
# from /usr/lib64/girepository-1.0/WebKit2-4.0.typelib
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
import gobject as __gobject


class WebViewClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        WebViewClass()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    authenticate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context_menu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context_menu_dismissed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    decide_policy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enter_fullscreen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insecure_content_detected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leave_fullscreen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    load_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    load_failed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    load_failed_with_tls_errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mouse_target_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    permission_request = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    print_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ready_to_show = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resource_load_started = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    run_as_modal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    run_color_chooser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    run_file_chooser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    script_dialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_notification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_option_menu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    submit_form = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_message_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    web_process_crashed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    web_process_terminated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _webkit_reserved0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WebViewClass), '__module__': 'gi.repository.WebKit2', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'WebViewClass' objects>, '__weakref__': <attribute '__weakref__' of 'WebViewClass' objects>, '__doc__': None, 'parent': <property object at 0x7fc3e718e5e0>, 'load_changed': <property object at 0x7fc3e718e6d0>, 'load_failed': <property object at 0x7fc3e718e7c0>, 'create': <property object at 0x7fc3e718e8b0>, 'ready_to_show': <property object at 0x7fc3e718e9a0>, 'run_as_modal': <property object at 0x7fc3e718ea90>, 'close': <property object at 0x7fc3e718eb80>, 'script_dialog': <property object at 0x7fc3e718ec70>, 'decide_policy': <property object at 0x7fc3e718ed60>, 'permission_request': <property object at 0x7fc3e718eea0>, 'mouse_target_changed': <property object at 0x7fc3e7191040>, 'print_': <property object at 0x7fc3e7191130>, 'resource_load_started': <property object at 0x7fc3e7191270>, 'enter_fullscreen': <property object at 0x7fc3e7191360>, 'leave_fullscreen': <property object at 0x7fc3e71914a0>, 'run_file_chooser': <property object at 0x7fc3e71915e0>, 'context_menu': <property object at 0x7fc3e71916d0>, 'context_menu_dismissed': <property object at 0x7fc3e7191810>, 'submit_form': <property object at 0x7fc3e7191900>, 'insecure_content_detected': <property object at 0x7fc3e7191a40>, 'web_process_crashed': <property object at 0x7fc3e7191b80>, 'authenticate': <property object at 0x7fc3e7191c70>, 'load_failed_with_tls_errors': <property object at 0x7fc3e7191db0>, 'show_notification': <property object at 0x7fc3e7191ef0>, 'run_color_chooser': <property object at 0x7fc3e7192090>, 'show_option_menu': <property object at 0x7fc3e71921d0>, 'web_process_terminated': <property object at 0x7fc3e7192310>, 'user_message_received': <property object at 0x7fc3e7192450>, '_webkit_reserved0': <property object at 0x7fc3e7192540>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(WebViewClass)


