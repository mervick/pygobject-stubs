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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides', '__doc__': None, 'markup_escape_text': <gi.overrides._DeprecatedAttribute object at 0x7f7c29495df0>, 'get_application_name': <gi.overrides._DeprecatedAttribute object at 0x7f7c294add60>, 'set_application_name': <gi.overrides._DeprecatedAttribute object at 0x7f7c29a2dac0>, 'get_prgname': <gi.overrides._DeprecatedAttribute object at 0x7f7c29a31160>, 'set_prgname': <gi.overrides._DeprecatedAttribute object at 0x7f7c29a31ee0>, 'main_depth': <gi.overrides._DeprecatedAttribute object at 0x7f7c29a31f10>, 'filename_display_basename': <gi.overrides._DeprecatedAttribute object at 0x7f7c29a31c10>, 'filename_display_name': <gi.overrides._DeprecatedAttribute object at 0x7f7c29a31fa0>, 'filename_from_utf8': <gi.overrides._DeprecatedAttribute object at 0x7f7c29a318e0>, 'uri_list_extract_uris': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741070>, 'MainLoop': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741100>, 'MainContext': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741190>, 'main_context_default': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741220>, 'source_remove': <gi.overrides._DeprecatedAttribute object at 0x7f7c287412b0>, 'Source': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741340>, 'Idle': <gi.overrides._DeprecatedAttribute object at 0x7f7c287413d0>, 'Timeout': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741460>, 'PollFD': <gi.overrides._DeprecatedAttribute object at 0x7f7c287414f0>, 'idle_add': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741580>, 'timeout_add': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741610>, 'timeout_add_seconds': <gi.overrides._DeprecatedAttribute object at 0x7f7c287416a0>, 'io_add_watch': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741730>, 'child_watch_add': <gi.overrides._DeprecatedAttribute object at 0x7f7c287417c0>, 'get_current_time': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741850>, 'spawn_async': <gi.overrides._DeprecatedAttribute object at 0x7f7c287418e0>, 'PRIORITY_DEFAULT': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741970>, 'PRIORITY_DEFAULT_IDLE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741a00>, 'PRIORITY_HIGH': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741a90>, 'PRIORITY_HIGH_IDLE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741b20>, 'PRIORITY_LOW': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741bb0>, 'IO_IN': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741c40>, 'IO_OUT': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741cd0>, 'IO_PRI': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741d60>, 'IO_ERR': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741df0>, 'IO_HUP': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741e80>, 'IO_NVAL': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741f10>, 'IO_STATUS_ERROR': <gi.overrides._DeprecatedAttribute object at 0x7f7c28741fa0>, 'IO_STATUS_NORMAL': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745070>, 'IO_STATUS_EOF': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745100>, 'IO_STATUS_AGAIN': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745190>, 'IO_FLAG_APPEND': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745220>, 'IO_FLAG_NONBLOCK': <gi.overrides._DeprecatedAttribute object at 0x7f7c287452b0>, 'IO_FLAG_IS_READABLE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745340>, 'IO_FLAG_IS_WRITEABLE': <gi.overrides._DeprecatedAttribute object at 0x7f7c287453d0>, 'IO_FLAG_IS_SEEKABLE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745460>, 'IO_FLAG_MASK': <gi.overrides._DeprecatedAttribute object at 0x7f7c287454f0>, 'IO_FLAG_GET_MASK': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745580>, 'IO_FLAG_SET_MASK': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745610>, 'SPAWN_LEAVE_DESCRIPTORS_OPEN': <gi.overrides._DeprecatedAttribute object at 0x7f7c287456a0>, 'SPAWN_DO_NOT_REAP_CHILD': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745730>, 'SPAWN_SEARCH_PATH': <gi.overrides._DeprecatedAttribute object at 0x7f7c287457c0>, 'SPAWN_STDOUT_TO_DEV_NULL': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745850>, 'SPAWN_STDERR_TO_DEV_NULL': <gi.overrides._DeprecatedAttribute object at 0x7f7c287458e0>, 'SPAWN_CHILD_INHERITS_STDIN': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745970>, 'SPAWN_FILE_AND_ARGV_ZERO': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745a00>, 'OPTION_FLAG_HIDDEN': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745a90>, 'OPTION_FLAG_IN_MAIN': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745b20>, 'OPTION_FLAG_REVERSE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745bb0>, 'OPTION_FLAG_NO_ARG': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745c40>, 'OPTION_FLAG_FILENAME': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745cd0>, 'OPTION_FLAG_OPTIONAL_ARG': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745d60>, 'OPTION_FLAG_NOALIAS': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745df0>, 'OPTION_ERROR_UNKNOWN_OPTION': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745e80>, 'OPTION_ERROR_BAD_VALUE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745f10>, 'OPTION_ERROR_FAILED': <gi.overrides._DeprecatedAttribute object at 0x7f7c28745fa0>, 'OPTION_REMAINING': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747070>, 'glib_version': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747100>, 'G_MININT8': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747190>, 'G_MAXINT8': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747220>, 'G_MAXUINT8': <gi.overrides._DeprecatedAttribute object at 0x7f7c287472b0>, 'G_MININT16': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747340>, 'G_MAXINT16': <gi.overrides._DeprecatedAttribute object at 0x7f7c287473d0>, 'G_MAXUINT16': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747460>, 'G_MININT32': <gi.overrides._DeprecatedAttribute object at 0x7f7c287474f0>, 'G_MAXINT32': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747580>, 'G_MAXUINT32': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747610>, 'G_MININT64': <gi.overrides._DeprecatedAttribute object at 0x7f7c287476a0>, 'G_MAXINT64': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747730>, 'G_MAXUINT64': <gi.overrides._DeprecatedAttribute object at 0x7f7c287477c0>, 'G_MINFLOAT': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747850>, 'G_MAXFLOAT': <gi.overrides._DeprecatedAttribute object at 0x7f7c287478e0>, 'G_MINDOUBLE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747970>, 'G_MAXDOUBLE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747a00>, 'G_MINSHORT': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747a90>, 'G_MAXSHORT': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747b20>, 'G_MAXUSHORT': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747bb0>, 'G_MININT': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747c40>, 'G_MAXINT': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747cd0>, 'G_MAXUINT': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747d60>, 'G_MINLONG': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747df0>, 'G_MAXLONG': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747e80>, 'G_MAXULONG': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747f10>, 'G_MAXSIZE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28747fa0>, 'G_MINSSIZE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749070>, 'G_MAXSSIZE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749100>, 'G_MINOFFSET': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749190>, 'G_MAXOFFSET': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749220>, 'Pid': <gi.overrides._DeprecatedAttribute object at 0x7f7c287492b0>, 'GError': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749340>, 'OptionGroup': <gi.overrides._DeprecatedAttribute object at 0x7f7c287493d0>, 'OptionContext': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749460>, 'PARAM_CONSTRUCT': <gi.overrides._DeprecatedAttribute object at 0x7f7c287494f0>, 'PARAM_CONSTRUCT_ONLY': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749580>, 'PARAM_LAX_VALIDATION': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749610>, 'PARAM_READABLE': <gi.overrides._DeprecatedAttribute object at 0x7f7c287496a0>, 'PARAM_WRITABLE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749730>, 'PARAM_READWRITE': <gi.overrides._DeprecatedAttribute object at 0x7f7c287497c0>, 'SIGNAL_ACTION': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749850>, 'SIGNAL_DETAILED': <gi.overrides._DeprecatedAttribute object at 0x7f7c287498e0>, 'SIGNAL_NO_HOOKS': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749970>, 'SIGNAL_NO_RECURSE': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749a00>, 'SIGNAL_RUN_CLEANUP': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749a90>, 'SIGNAL_RUN_FIRST': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749b20>, 'SIGNAL_RUN_LAST': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749bb0>, 'property': <gi.overrides._DeprecatedAttribute object at 0x7f7c28749c40>})"


