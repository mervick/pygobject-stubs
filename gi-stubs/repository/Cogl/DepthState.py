# encoding: utf-8
# module gi.repository.Cogl
# from /usr/lib64/girepository-1.0/Cogl-1.0.typelib
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
import gobject as __gobject


class DepthState(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DepthState()
    """
    def get_range(self, near_val, far_val): # real signature unknown; restored from __doc__
        """ get_range(self, near_val:float, far_val:float) """
        pass

    def get_test_enabled(self): # real signature unknown; restored from __doc__
        """ get_test_enabled(self) -> int """
        return 0

    def get_test_function(self): # real signature unknown; restored from __doc__
        """ get_test_function(self) -> Cogl.DepthTestFunction """
        pass

    def get_write_enabled(self): # real signature unknown; restored from __doc__
        """ get_write_enabled(self) -> int """
        return 0

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def set_range(self, near_val, far_val): # real signature unknown; restored from __doc__
        """ set_range(self, near_val:float, far_val:float) """
        pass

    def set_test_enabled(self, enable): # real signature unknown; restored from __doc__
        """ set_test_enabled(self, enable:int) """
        pass

    def set_test_function(self, function): # real signature unknown; restored from __doc__
        """ set_test_function(self, function:Cogl.DepthTestFunction) """
        pass

    def set_write_enabled(self, enable): # real signature unknown; restored from __doc__
        """ set_write_enabled(self, enable:int) """
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

    private_member_magic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding9 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_range_far = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_range_near = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_test_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_test_function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_write_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DepthState), '__module__': 'gi.repository.Cogl', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DepthState' objects>, '__weakref__': <attribute '__weakref__' of 'DepthState' objects>, '__doc__': None, 'private_member_magic': <property object at 0x7fba89016ae0>, 'private_member_test_enabled': <property object at 0x7fba89016bd0>, 'private_member_test_function': <property object at 0x7fba89016d10>, 'private_member_write_enabled': <property object at 0x7fba89016e50>, 'private_member_range_near': <property object at 0x7fba89016f90>, 'private_member_range_far': <property object at 0x7fba89019130>, 'private_member_padding0': <property object at 0x7fba89019270>, 'private_member_padding1': <property object at 0x7fba89019360>, 'private_member_padding2': <property object at 0x7fba89019450>, 'private_member_padding3': <property object at 0x7fba89019540>, 'private_member_padding4': <property object at 0x7fba89019680>, 'private_member_padding5': <property object at 0x7fba890197c0>, 'private_member_padding6': <property object at 0x7fba89019900>, 'private_member_padding7': <property object at 0x7fba89019a40>, 'private_member_padding8': <property object at 0x7fba89019b80>, 'private_member_padding9': <property object at 0x7fba89019cc0>, 'get_range': gi.FunctionInfo(get_range), 'get_test_enabled': gi.FunctionInfo(get_test_enabled), 'get_test_function': gi.FunctionInfo(get_test_function), 'get_write_enabled': gi.FunctionInfo(get_write_enabled), 'init': gi.FunctionInfo(init), 'set_range': gi.FunctionInfo(set_range), 'set_test_enabled': gi.FunctionInfo(set_test_enabled), 'set_test_function': gi.FunctionInfo(set_test_function), 'set_write_enabled': gi.FunctionInfo(set_write_enabled)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DepthState)


