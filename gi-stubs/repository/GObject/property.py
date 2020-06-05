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


from .object import object

class property(object):
    """
    Creates a new Property which when used in conjunction with
        GObject subclass will create a Python property accessor for the
        GObject ParamSpec.
    
        :param callable getter:
            getter to get the value of the property
        :param callable setter:
            setter to set the value of the property
        :param type type:
            type of property
        :param default:
            default value, must match the property type.
        :param str nick:
            short description
        :param str blurb:
            long description
        :param GObject.ParamFlags flags:
            parameter flags
        :keyword minimum:
            minimum allowed value (int, float, long only)
        :keyword maximum:
            maximum allowed value (int, float, long only)
    
        .. code-block:: python
    
             class MyObject(GObject.Object):
                 prop = GObject.Property(type=str)
    
             obj = MyObject()
             obj.prop = 'value'
    
             obj.prop  # now is 'value'
    
        The API is similar to the builtin :py:func:`property`:
    
        .. code-block:: python
    
            class AnotherObject(GObject.Object):
                value = 0
    
                @GObject.Property
                def prop(self):
                    'Read only property.'
                    return 1
    
                @GObject.Property(type=int)
                def propInt(self):
                    'Read-write integer property.'
                    return self.value
    
                @propInt.setter
                def propInt(self, value):
                    self.value = value
    """
    def getter(self, fget): # reliably restored by inspect
        """ Set the getter function to fget. For use as a decorator. """
        pass

    def get_pspec_args(self): # reliably restored by inspect
        # no doc
        pass

    def setter(self, fset): # reliably restored by inspect
        """ Set the setter function to fset. For use as a decorator. """
        pass

    def _check_default(self): # reliably restored by inspect
        # no doc
        pass

    def _default_getter(self, instance): # reliably restored by inspect
        # no doc
        pass

    def _default_setter(self, instance, value): # reliably restored by inspect
        # no doc
        pass

    def _get_default(self, default): # reliably restored by inspect
        # no doc
        pass

    def _get_maximum(self): # reliably restored by inspect
        # no doc
        pass

    def _get_minimum(self): # reliably restored by inspect
        # no doc
        pass

    def _readonly_setter(self, instance, value): # reliably restored by inspect
        # no doc
        pass

    def _type_from_python(self, type_): # reliably restored by inspect
        # no doc
        pass

    def _writeonly_getter(self, instance): # reliably restored by inspect
        # no doc
        pass

    def __call__(self, fget): # reliably restored by inspect
        """ Allows application of the getter along with init arguments. """
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

    def __get__(self, instance, klass): # reliably restored by inspect
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

    def __init__(self, getter=None, setter=None, type=None, default=None, nick=None, blurb=None, flags=3, minimum=None, maximum=None): # reliably restored by inspect
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

    def __set__(self, instance, value): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _default_lookup = {
        None:  # (!) real value is '<GType gint (24)>'
            0
        ,
        None:  # (!) real value is '<GType guint (28)>'
            0
        ,
        None:  # (!) real value is '<GType glong (32)>'
            0
        ,
        None:  # (!) real value is '<GType gulong (36)>'
            0
        ,
        None:  # (!) real value is '<GType gint64 (40)>'
            0
        ,
        None:  # (!) real value is '<GType guint64 (44)>'
            0
        ,
        None:  # (!) real value is '<GType gfloat (56)>'
            0.0
        ,
        None:  # (!) real value is '<GType gdouble (60)>'
            0.0
        ,
        None:  # (!) real value is '<GType gchararray (64)>'
            ''
        ,
    }
    _max_value_lookup = {
        None:  # (!) real value is '<GType gint (24)>'
            2147483647
        ,
        None:  # (!) real value is '<GType guint (28)>'
            4294967295
        ,
        None:  # (!) real value is '<GType glong (32)>'
            9223372036854775807
        ,
        None:  # (!) real value is '<GType gulong (36)>'
            18446744073709551615
        ,
        None:  # (!) real value is '<GType gint64 (40)>'
            9223372036854775807
        ,
        None:  # (!) real value is '<GType guint64 (44)>'
            18446744073709551615
        ,
        None:  # (!) real value is '<GType gfloat (56)>'
            3.4028234663852886e+38
        ,
        None:  # (!) real value is '<GType gdouble (60)>'
            1.7976931348623157e+308
        ,
    }
    _min_value_lookup = {
        None:  # (!) real value is '<GType gint (24)>'
            -2147483648
        ,
        None:  # (!) real value is '<GType guint (28)>'
            0
        ,
        None:  # (!) real value is '<GType glong (32)>'
            -9223372036854775808
        ,
        None:  # (!) real value is '<GType gulong (36)>'
            0
        ,
        None:  # (!) real value is '<GType gint64 (40)>'
            -9223372036854775808
        ,
        None:  # (!) real value is '<GType guint64 (44)>'
            0
        ,
        None:  # (!) real value is '<GType gfloat (56)>'
            -3.4028234663852886e+38
        ,
        None:  # (!) real value is '<GType gdouble (60)>'
            -1.7976931348623157e+308
        ,
    }
    _type_from_pytype_lookup = {
        int: 
            None # (!) real value is '<GType gint (24)>'
        ,
        bool: 
            None # (!) real value is '<GType gboolean (20)>'
        ,
        float: 
            None # (!) real value is '<GType gdouble (60)>'
        ,
        str: 
            None # (!) real value is '<GType gchararray (64)>'
        ,
        object: 
            None # (!) real value is '<GType PyObject (93895378949056)>'
        ,
    }
    __class__ = type
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'gi._propertyhelper\', \'__doc__\': "Creates a new Property which when used in conjunction with\\n    GObject subclass will create a Python property accessor for the\\n    GObject ParamSpec.\\n\\n    :param callable getter:\\n        getter to get the value of the property\\n    :param callable setter:\\n        setter to set the value of the property\\n    :param type type:\\n        type of property\\n    :param default:\\n        default value, must match the property type.\\n    :param str nick:\\n        short description\\n    :param str blurb:\\n        long description\\n    :param GObject.ParamFlags flags:\\n        parameter flags\\n    :keyword minimum:\\n        minimum allowed value (int, float, long only)\\n    :keyword maximum:\\n        maximum allowed value (int, float, long only)\\n\\n    .. code-block:: python\\n\\n         class MyObject(GObject.Object):\\n             prop = GObject.Property(type=str)\\n\\n         obj = MyObject()\\n         obj.prop = \'value\'\\n\\n         obj.prop  # now is \'value\'\\n\\n    The API is similar to the builtin :py:func:`property`:\\n\\n    .. code-block:: python\\n\\n        class AnotherObject(GObject.Object):\\n            value = 0\\n\\n            @GObject.Property\\n            def prop(self):\\n                \'Read only property.\'\\n                return 1\\n\\n            @GObject.Property(type=int)\\n            def propInt(self):\\n                \'Read-write integer property.\'\\n                return self.value\\n\\n            @propInt.setter\\n            def propInt(self, value):\\n                self.value = value\\n    ", \'_type_from_pytype_lookup\': {<class \'int\'>: <GType gint (24)>, <class \'bool\'>: <GType gboolean (20)>, <class \'float\'>: <GType gdouble (60)>, <class \'str\'>: <GType gchararray (64)>, <class \'object\'>: <GType PyObject (93895378949056)>}, \'_min_value_lookup\': {<GType guint (28)>: 0, <GType gulong (36)>: 0, <GType guint64 (44)>: 0, <GType gfloat (56)>: -3.4028234663852886e+38, <GType gdouble (60)>: -1.7976931348623157e+308, <GType gint (24)>: -2147483648, <GType glong (32)>: -9223372036854775808, <GType gint64 (40)>: -9223372036854775808}, \'_max_value_lookup\': {<GType guint (28)>: 4294967295, <GType gulong (36)>: 18446744073709551615, <GType gint64 (40)>: 9223372036854775807, <GType guint64 (44)>: 18446744073709551615, <GType gfloat (56)>: 3.4028234663852886e+38, <GType gdouble (60)>: 1.7976931348623157e+308, <GType gint (24)>: 2147483647, <GType glong (32)>: 9223372036854775807}, \'_default_lookup\': {<GType gint (24)>: 0, <GType guint (28)>: 0, <GType glong (32)>: 0, <GType gulong (36)>: 0, <GType gint64 (40)>: 0, <GType guint64 (44)>: 0, <GType gchararray (64)>: \'\', <GType gfloat (56)>: 0.0, <GType gdouble (60)>: 0.0}, \'__metaclass__\': <class \'gi._propertyhelper.Property.__metaclass__\'>, \'__init__\': <function Property.__init__ at 0x7f7c28dfb5e0>, \'__repr__\': <function Property.__repr__ at 0x7f7c28dfb700>, \'__get__\': <function Property.__get__ at 0x7f7c28dfb790>, \'__set__\': <function Property.__set__ at 0x7f7c28dfb820>, \'__call__\': <function Property.__call__ at 0x7f7c28dfb8b0>, \'getter\': <function Property.getter at 0x7f7c28dfb940>, \'setter\': <function Property.setter at 0x7f7c28dfb9d0>, \'_type_from_python\': <function Property._type_from_python at 0x7f7c28dfba60>, \'_get_default\': <function Property._get_default at 0x7f7c28dfbaf0>, \'_check_default\': <function Property._check_default at 0x7f7c28dfbb80>, \'_get_minimum\': <function Property._get_minimum at 0x7f7c28dfbc10>, \'_get_maximum\': <function Property._get_maximum at 0x7f7c28dfbca0>, \'_default_setter\': <function Property._default_setter at 0x7f7c28dfbd30>, \'_default_getter\': <function Property._default_getter at 0x7f7c28dfbdc0>, \'_readonly_setter\': <function Property._readonly_setter at 0x7f7c28dfbe50>, \'_writeonly_getter\': <function Property._writeonly_getter at 0x7f7c28dfbee0>, \'get_pspec_args\': <function Property.get_pspec_args at 0x7f7c28dfbf70>, \'__dict__\': <attribute \'__dict__\' of \'Property\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Property\' objects>})'
    __metaclass__ = None # (!) real value is "<class 'gi._propertyhelper.Property.__metaclass__'>"


