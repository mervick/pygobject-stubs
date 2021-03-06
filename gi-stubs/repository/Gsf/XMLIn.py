# encoding: utf-8
# module gi.repository.Gsf
# from /usr/lib64/girepository-1.0/Gsf-1.typelib
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


class XMLIn(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        XMLIn()
    """
    def check_ns(self, p_str, ns_id): # real signature unknown; restored from __doc__
        """ check_ns(self, str:str, ns_id:int) -> str or None """
        return ""

    def get_input(self): # real signature unknown; restored from __doc__
        """ get_input(self) -> Gsf.Input """
        pass

    def namecmp(self, p_str, ns_id, name): # real signature unknown; restored from __doc__
        """ namecmp(self, str:str, ns_id:int, name:str) -> bool """
        return False

    def push_state(self, doc, new_state=None, dtor, attrs): # real signature unknown; restored from __doc__
        """ push_state(self, doc:Gsf.XMLInDoc, new_state=None, dtor:Gsf.XMLInExtDtor, attrs:list) """
        pass

    def set_silent_unknowns(self, silent): # real signature unknown; restored from __doc__
        """ set_silent_unknowns(self, silent:bool) """
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

    content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    doc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(XMLIn), '__module__': 'gi.repository.Gsf', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'XMLIn' objects>, '__weakref__': <attribute '__weakref__' of 'XMLIn' objects>, '__doc__': None, 'user_state': <property object at 0x7f95c4745400>, 'content': <property object at 0x7f95c47454f0>, 'doc': <property object at 0x7f95c47455e0>, 'node': <property object at 0x7f95c47456d0>, 'node_stack': <property object at 0x7f95c47457c0>, 'check_ns': gi.FunctionInfo(check_ns), 'get_input': gi.FunctionInfo(get_input), 'namecmp': gi.FunctionInfo(namecmp), 'push_state': gi.FunctionInfo(push_state), 'set_silent_unknowns': gi.FunctionInfo(set_silent_unknowns)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(XMLIn)


