# encoding: utf-8
# module gi.repository.GLib
# from /usr/lib64/girepository-1.0/GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # /usr/lib64/python3.8/site-packages/gi/_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides', '__doc__': None, 'USER_DIRECTORY_DESKTOP': <gi.overrides._DeprecatedAttribute object at 0x7f1d2c7212b0>, 'USER_DIRECTORY_DOCUMENTS': <gi.overrides._DeprecatedAttribute object at 0x7f1d2c753d90>, 'USER_DIRECTORY_DOWNLOAD': <gi.overrides._DeprecatedAttribute object at 0x7f1d2bafc1c0>, 'USER_DIRECTORY_MUSIC': <gi.overrides._DeprecatedAttribute object at 0x7f1d2bafc6a0>, 'USER_DIRECTORY_PICTURES': <gi.overrides._DeprecatedAttribute object at 0x7f1d2bafcca0>, 'USER_DIRECTORY_PUBLIC_SHARE': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccaaf70>, 'USER_DIRECTORY_TEMPLATES': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccaafd0>, 'USER_DIRECTORY_VIDEOS': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc070>, 'IO_FLAG_APPEND': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc100>, 'IO_FLAG_GET_MASK': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc190>, 'IO_FLAG_IS_READABLE': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc220>, 'IO_FLAG_IS_SEEKABLE': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc2b0>, 'IO_FLAG_MASK': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc340>, 'IO_FLAG_NONBLOCK': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc3d0>, 'IO_FLAG_SET_MASK': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc460>, 'IO_FLAG_IS_WRITEABLE': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc4f0>, 'IO_STATUS_AGAIN': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc580>, 'IO_STATUS_EOF': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc610>, 'IO_STATUS_ERROR': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc6a0>, 'IO_STATUS_NORMAL': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc730>, 'SPAWN_CHILD_INHERITS_STDIN': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc7c0>, 'SPAWN_DO_NOT_REAP_CHILD': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc850>, 'SPAWN_FILE_AND_ARGV_ZERO': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc8e0>, 'SPAWN_LEAVE_DESCRIPTORS_OPEN': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccc970>, 'SPAWN_SEARCH_PATH': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccca00>, 'SPAWN_STDERR_TO_DEV_NULL': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccca90>, 'SPAWN_STDOUT_TO_DEV_NULL': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccccb20>, 'OPTION_FLAG_HIDDEN': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccccbb0>, 'OPTION_FLAG_IN_MAIN': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccccc40>, 'OPTION_FLAG_REVERSE': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccccd0>, 'OPTION_FLAG_NO_ARG': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccccd60>, 'OPTION_FLAG_FILENAME': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccccdf0>, 'OPTION_FLAG_OPTIONAL_ARG': <gi.overrides._DeprecatedAttribute object at 0x7f1d2cccce80>, 'OPTION_FLAG_NOALIAS': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccccf10>, 'OPTION_ERROR_UNKNOWN_OPTION': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccccfa0>, 'OPTION_ERROR_BAD_VALUE': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccd1070>, 'OPTION_ERROR_FAILED': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccd1100>, 'unix_signal_add_full': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccd1190>, 'glib_version': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccd1220>, 'pyglib_version': <gi.overrides._DeprecatedAttribute object at 0x7f1d2ccd12b0>})"


