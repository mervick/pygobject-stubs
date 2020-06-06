# encoding: utf-8
# module gi.repository.Gladeui
# from /usr/lib64/girepository-1.0/Gladeui-2.0.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class XmlNode(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(context:Gladeui.XmlContext, name:str) -> Gladeui.XmlNode
        new_comment(context:Gladeui.XmlContext, comment:str) -> Gladeui.XmlNode
    """
    def add_next_sibling(self, new_node): # real signature unknown; restored from __doc__
        """ add_next_sibling(self, new_node:Gladeui.XmlNode) -> Gladeui.XmlNode """
        pass

    def add_prev_sibling(self, new_node): # real signature unknown; restored from __doc__
        """ add_prev_sibling(self, new_node:Gladeui.XmlNode) -> Gladeui.XmlNode """
        pass

    def append_child(self, child): # real signature unknown; restored from __doc__
        """ append_child(self, child:Gladeui.XmlNode) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gladeui.XmlNode """
        pass

    def delete(self): # real signature unknown; restored from __doc__
        """ delete(self) """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> Gladeui.XmlNode """
        pass

    def get_children_with_comments(self): # real signature unknown; restored from __doc__
        """ get_children_with_comments(self) -> Gladeui.XmlNode """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gladeui.XmlNode """
        pass

    def is_comment(self): # real signature unknown; restored from __doc__
        """ is_comment(self) -> bool """
        return False

    def new(self, context, name): # real signature unknown; restored from __doc__
        """ new(context:Gladeui.XmlContext, name:str) -> Gladeui.XmlNode """
        pass

    def new_comment(self, context, comment): # real signature unknown; restored from __doc__
        """ new_comment(context:Gladeui.XmlContext, comment:str) -> Gladeui.XmlNode """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> Gladeui.XmlNode """
        pass

    def next_with_comments(self): # real signature unknown; restored from __doc__
        """ next_with_comments(self) -> Gladeui.XmlNode """
        pass

    def prev_with_comments(self): # real signature unknown; restored from __doc__
        """ prev_with_comments(self) -> Gladeui.XmlNode """
        pass

    def remove(self): # real signature unknown; restored from __doc__
        """ remove(self) """
        pass

    def set_property_boolean(self, name, value): # real signature unknown; restored from __doc__
        """ set_property_boolean(self, name:str, value:bool) """
        pass

    def set_property_string(self, name, string=None): # real signature unknown; restored from __doc__
        """ set_property_string(self, name:str, string:str=None) """
        pass

    def verify(self, name): # real signature unknown; restored from __doc__
        """ verify(self, name:str) -> bool """
        return False

    def verify_silent(self, name): # real signature unknown; restored from __doc__
        """ verify_silent(self, name:str) -> bool """
        return False

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
        """ new(context:Gladeui.XmlContext, name:str) -> Gladeui.XmlNode """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(XmlNode), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType GladeXmlNode (94653531318832)>, '__dict__': <attribute '__dict__' of 'XmlNode' objects>, '__weakref__': <attribute '__weakref__' of 'XmlNode' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_comment': gi.FunctionInfo(new_comment), 'add_next_sibling': gi.FunctionInfo(add_next_sibling), 'add_prev_sibling': gi.FunctionInfo(add_prev_sibling), 'append_child': gi.FunctionInfo(append_child), 'copy': gi.FunctionInfo(copy), 'delete': gi.FunctionInfo(delete), 'get_children': gi.FunctionInfo(get_children), 'get_children_with_comments': gi.FunctionInfo(get_children_with_comments), 'get_name': gi.FunctionInfo(get_name), 'get_parent': gi.FunctionInfo(get_parent), 'is_comment': gi.FunctionInfo(is_comment), 'next': gi.FunctionInfo(next), 'next_with_comments': gi.FunctionInfo(next_with_comments), 'prev_with_comments': gi.FunctionInfo(prev_with_comments), 'remove': gi.FunctionInfo(remove), 'set_property_boolean': gi.FunctionInfo(set_property_boolean), 'set_property_string': gi.FunctionInfo(set_property_string), 'verify': gi.FunctionInfo(verify), 'verify_silent': gi.FunctionInfo(verify_silent), '__new__': <staticmethod object at 0x7f1341779640>, '__init__': <function nothing at 0x7f1342e6cee0>})"
    __gtype__ = None # (!) real value is '<GType GladeXmlNode (94653531318832)>'
    __info__ = StructInfo(XmlNode)


