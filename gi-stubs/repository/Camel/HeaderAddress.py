# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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
import gobject as __gobject


class HeaderAddress(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        HeaderAddress()
        new() -> Camel.HeaderAddress
        new_group(name:str) -> Camel.HeaderAddress
        new_name(name:str, addr:str) -> Camel.HeaderAddress
    """
    def add_member(self, member): # real signature unknown; restored from __doc__
        """ add_member(self, member:Camel.HeaderAddress) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def decode(self, in_, charset): # real signature unknown; restored from __doc__
        """ decode(in_:str, charset:str) -> Camel.HeaderAddress """
        pass

    def fold(self, in_, headerlen): # real signature unknown; restored from __doc__
        """ fold(in_:str, headerlen:int) -> str """
        return ""

    def list_append(self, addrlistp, addr): # real signature unknown; restored from __doc__
        """ list_append(addrlistp:list, addr:Camel.HeaderAddress) """
        pass

    def list_append_list(self, addrlistp, addrs): # real signature unknown; restored from __doc__
        """ list_append_list(addrlistp:list, addrs:list) """
        pass

    def list_clear(self, addrlistp): # real signature unknown; restored from __doc__
        """ list_clear(addrlistp:list) """
        pass

    def list_encode(self, addrlist): # real signature unknown; restored from __doc__
        """ list_encode(addrlist:list) -> str """
        return ""

    def list_format(self, addrlist): # real signature unknown; restored from __doc__
        """ list_format(addrlist:list) -> str """
        return ""

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Camel.HeaderAddress """
        pass

    def new_group(self, name): # real signature unknown; restored from __doc__
        """ new_group(name:str) -> Camel.HeaderAddress """
        pass

    def new_name(self, name, addr): # real signature unknown; restored from __doc__
        """ new_name(name:str, addr:str) -> Camel.HeaderAddress """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Camel.HeaderAddress """
        pass

    def set_addr(self, addr): # real signature unknown; restored from __doc__
        """ set_addr(self, addr:str) """
        pass

    def set_members(self, group): # real signature unknown; restored from __doc__
        """ set_members(self, group:list) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(*args, **kwargs): # reliably restored by inspect
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
        """ new() -> Camel.HeaderAddress """
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

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(HeaderAddress), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelHeaderAddress (94124523736192)>, '__dict__': <attribute '__dict__' of 'HeaderAddress' objects>, '__weakref__': <attribute '__weakref__' of 'HeaderAddress' objects>, '__doc__': None, 'next': <property object at 0x7f7b34fde270>, 'type': <property object at 0x7f7b34fde360>, 'name': <property object at 0x7f7b34fde450>, 'refcount': <property object at 0x7f7b34fde540>, 'new': gi.FunctionInfo(new), 'new_group': gi.FunctionInfo(new_group), 'new_name': gi.FunctionInfo(new_name), 'add_member': gi.FunctionInfo(add_member), 'ref': gi.FunctionInfo(ref), 'set_addr': gi.FunctionInfo(set_addr), 'set_members': gi.FunctionInfo(set_members), 'set_name': gi.FunctionInfo(set_name), 'unref': gi.FunctionInfo(unref), 'decode': gi.FunctionInfo(decode), 'fold': gi.FunctionInfo(fold), 'list_append': gi.FunctionInfo(list_append), 'list_append_list': gi.FunctionInfo(list_append_list), 'list_clear': gi.FunctionInfo(list_clear), 'list_encode': gi.FunctionInfo(list_encode), 'list_format': gi.FunctionInfo(list_format), '__new__': <staticmethod object at 0x7f7b34fdd1f0>, '__init__': <function nothing at 0x7f7b37797ee0>})"
    __gtype__ = None # (!) real value is '<GType CamelHeaderAddress (94124523736192)>'
    __info__ = StructInfo(HeaderAddress)


