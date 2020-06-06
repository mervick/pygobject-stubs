# encoding: utf-8
# module gi.repository.GObject
# from /usr/lib64/girepository-1.0/GObject-2.0.typelib
# by generator 1.147
# no doc

# imports
from gi.repository.GLib import (GError, IO_ERR, IO_FLAG_APPEND, 
    IO_FLAG_GET_MASK, IO_FLAG_IS_READABLE, IO_FLAG_IS_SEEKABLE, 
    IO_FLAG_IS_WRITEABLE, IO_FLAG_MASK, IO_FLAG_NONBLOCK, IO_FLAG_SET_MASK, 
    IO_HUP, IO_IN, IO_NVAL, IO_OUT, IO_PRI, IO_STATUS_AGAIN, IO_STATUS_EOF, 
    IO_STATUS_ERROR, IO_STATUS_NORMAL, OPTION_ERROR_BAD_VALUE, 
    OPTION_ERROR_FAILED, OPTION_ERROR_UNKNOWN_OPTION, OPTION_FLAG_FILENAME, 
    OPTION_FLAG_HIDDEN, OPTION_FLAG_IN_MAIN, OPTION_FLAG_NOALIAS, 
    OPTION_FLAG_NO_ARG, OPTION_FLAG_OPTIONAL_ARG, OPTION_FLAG_REVERSE, 
    SPAWN_CHILD_INHERITS_STDIN, SPAWN_DO_NOT_REAP_CHILD, 
    SPAWN_FILE_AND_ARGV_ZERO, SPAWN_LEAVE_DESCRIPTORS_OPEN, SPAWN_SEARCH_PATH, 
    SPAWN_STDERR_TO_DEV_NULL, SPAWN_STDOUT_TO_DEV_NULL, 
    filename_display_basename, filename_display_name, get_application_name, 
    get_prgname, main_context_default, main_depth, set_application_name, 
    set_prgname, source_remove, uri_list_extract_uris)

from gi._gi import (GObjectWeakRef, OptionContext, OptionGroup, Pid, 
    add_emission_hook, list_properties, new, signal_new, spawn_async, 
    type_register)

from gobject import (GBoxed, GEnum, GFlags, GInterface, GParamSpec, GPointer, 
    GType, Warning)

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GLib as __gi_repository_GLib
import gi._signalhelper as __gi__signalhelper
import gobject as __gobject


class __class__(__gi_overrides.OverridesProxyModule):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, introspection_module): # reliably restored by inspect
        # no doc
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides', '__doc__': None, 'markup_escape_text': <gi.overrides._DeprecatedAttribute object at 0x7fe46c70af10>, 'get_application_name': <gi.overrides._DeprecatedAttribute object at 0x7fe46c03e250>, 'set_application_name': <gi.overrides._DeprecatedAttribute object at 0x7fe46cc5deb0>, 'get_prgname': <gi.overrides._DeprecatedAttribute object at 0x7fe46cc61550>, 'set_prgname': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b22b0>, 'main_depth': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b22e0>, 'filename_display_basename': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2340>, 'filename_display_name': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b23a0>, 'filename_from_utf8': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2400>, 'uri_list_extract_uris': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2460>, 'MainLoop': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b24f0>, 'MainContext': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2580>, 'main_context_default': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2610>, 'source_remove': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b26a0>, 'Source': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2730>, 'Idle': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b27c0>, 'Timeout': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2850>, 'PollFD': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b28e0>, 'idle_add': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2970>, 'timeout_add': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2a00>, 'timeout_add_seconds': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2a90>, 'io_add_watch': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2b20>, 'child_watch_add': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2bb0>, 'get_current_time': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2c40>, 'spawn_async': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2cd0>, 'PRIORITY_DEFAULT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2d60>, 'PRIORITY_DEFAULT_IDLE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2df0>, 'PRIORITY_HIGH': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2e80>, 'PRIORITY_HIGH_IDLE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2f10>, 'PRIORITY_LOW': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b2fa0>, 'IO_IN': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6070>, 'IO_OUT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6100>, 'IO_PRI': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6190>, 'IO_ERR': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6220>, 'IO_HUP': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b62b0>, 'IO_NVAL': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6340>, 'IO_STATUS_ERROR': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b63d0>, 'IO_STATUS_NORMAL': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6460>, 'IO_STATUS_EOF': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b64f0>, 'IO_STATUS_AGAIN': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6580>, 'IO_FLAG_APPEND': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6610>, 'IO_FLAG_NONBLOCK': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b66a0>, 'IO_FLAG_IS_READABLE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6730>, 'IO_FLAG_IS_WRITEABLE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b67c0>, 'IO_FLAG_IS_SEEKABLE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6850>, 'IO_FLAG_MASK': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b68e0>, 'IO_FLAG_GET_MASK': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6970>, 'IO_FLAG_SET_MASK': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6a00>, 'SPAWN_LEAVE_DESCRIPTORS_OPEN': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6a90>, 'SPAWN_DO_NOT_REAP_CHILD': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6b20>, 'SPAWN_SEARCH_PATH': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6bb0>, 'SPAWN_STDOUT_TO_DEV_NULL': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6c40>, 'SPAWN_STDERR_TO_DEV_NULL': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6cd0>, 'SPAWN_CHILD_INHERITS_STDIN': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6d60>, 'SPAWN_FILE_AND_ARGV_ZERO': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6df0>, 'OPTION_FLAG_HIDDEN': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6e80>, 'OPTION_FLAG_IN_MAIN': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6f10>, 'OPTION_FLAG_REVERSE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b6fa0>, 'OPTION_FLAG_NO_ARG': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9070>, 'OPTION_FLAG_FILENAME': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9100>, 'OPTION_FLAG_OPTIONAL_ARG': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9190>, 'OPTION_FLAG_NOALIAS': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9220>, 'OPTION_ERROR_UNKNOWN_OPTION': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b92b0>, 'OPTION_ERROR_BAD_VALUE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9340>, 'OPTION_ERROR_FAILED': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b93d0>, 'OPTION_REMAINING': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9460>, 'glib_version': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b94f0>, 'G_MININT8': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9580>, 'G_MAXINT8': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9610>, 'G_MAXUINT8': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b96a0>, 'G_MININT16': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9730>, 'G_MAXINT16': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b97c0>, 'G_MAXUINT16': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9850>, 'G_MININT32': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b98e0>, 'G_MAXINT32': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9970>, 'G_MAXUINT32': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9a00>, 'G_MININT64': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9a90>, 'G_MAXINT64': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9b20>, 'G_MAXUINT64': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9bb0>, 'G_MINFLOAT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9c40>, 'G_MAXFLOAT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9cd0>, 'G_MINDOUBLE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9d60>, 'G_MAXDOUBLE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9df0>, 'G_MINSHORT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9e80>, 'G_MAXSHORT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9f10>, 'G_MAXUSHORT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9b9fa0>, 'G_MININT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba070>, 'G_MAXINT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba100>, 'G_MAXUINT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba190>, 'G_MINLONG': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba220>, 'G_MAXLONG': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba2b0>, 'G_MAXULONG': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba340>, 'G_MAXSIZE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba3d0>, 'G_MINSSIZE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba460>, 'G_MAXSSIZE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba4f0>, 'G_MINOFFSET': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba580>, 'G_MAXOFFSET': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba610>, 'Pid': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba6a0>, 'GError': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba730>, 'OptionGroup': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba7c0>, 'OptionContext': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba850>, 'PARAM_CONSTRUCT': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba8e0>, 'PARAM_CONSTRUCT_ONLY': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9ba970>, 'PARAM_LAX_VALIDATION': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9baa00>, 'PARAM_READABLE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9baa90>, 'PARAM_WRITABLE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9bab20>, 'PARAM_READWRITE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9babb0>, 'SIGNAL_ACTION': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9bac40>, 'SIGNAL_DETAILED': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9bacd0>, 'SIGNAL_NO_HOOKS': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9bad60>, 'SIGNAL_NO_RECURSE': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9badf0>, 'SIGNAL_RUN_CLEANUP': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9bae80>, 'SIGNAL_RUN_FIRST': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9baf10>, 'SIGNAL_RUN_LAST': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9bafa0>, 'property': <gi.overrides._DeprecatedAttribute object at 0x7fe46b9be070>})"


