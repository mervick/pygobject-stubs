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


class BurnClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BurnClass()
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

    action_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ask_disable_joliet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blank_failure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_failure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert_media_request = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    install_missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    location_request = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    progress_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    warn_audio_to_appendable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    warn_data_loss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    warn_previous_session_loss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    warn_rewritable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BurnClass), '__module__': 'gi.repository.BraseroBurn', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BurnClass' objects>, '__weakref__': <attribute '__weakref__' of 'BurnClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fdd6134aea0>, 'insert_media_request': <property object at 0x7fdd6134af40>, 'eject_failure': <property object at 0x7fdd6134af90>, 'blank_failure': <property object at 0x7fdd6134c0e0>, 'location_request': <property object at 0x7fdd6134c220>, 'ask_disable_joliet': <property object at 0x7fdd6134c360>, 'warn_data_loss': <property object at 0x7fdd6134c450>, 'warn_previous_session_loss': <property object at 0x7fdd6134c590>, 'warn_audio_to_appendable': <property object at 0x7fdd6134c6d0>, 'warn_rewritable': <property object at 0x7fdd6134c7c0>, 'dummy_success': <property object at 0x7fdd6134c8b0>, 'progress_changed': <property object at 0x7fdd6134c9f0>, 'action_changed': <property object at 0x7fdd6134cae0>, 'install_missing': <property object at 0x7fdd6134cbd0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BurnClass)


