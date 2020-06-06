# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class ElementClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ElementClass()
    """
    def add_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ add_metadata(self, key:str, value:str) """
        pass

    def add_pad_template(self, templ): # real signature unknown; restored from __doc__
        """ add_pad_template(self, templ:Gst.PadTemplate) """
        pass

    def add_static_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ add_static_metadata(self, key:str, value:str) """
        pass

    def add_static_pad_template(self, static_templ): # real signature unknown; restored from __doc__
        """ add_static_pad_template(self, static_templ:Gst.StaticPadTemplate) """
        pass

    def add_static_pad_template_with_gtype(self, static_templ, pad_type): # real signature unknown; restored from __doc__
        """ add_static_pad_template_with_gtype(self, static_templ:Gst.StaticPadTemplate, pad_type:GType) """
        pass

    def get_metadata(self, key): # real signature unknown; restored from __doc__
        """ get_metadata(self, key:str) -> str """
        return ""

    def get_pad_template(self, name): # real signature unknown; restored from __doc__
        """ get_pad_template(self, name:str) -> Gst.PadTemplate or None """
        pass

    def get_pad_template_list(self): # real signature unknown; restored from __doc__
        """ get_pad_template_list(self) -> list """
        return []

    def set_metadata(self, longname, classification, description, author): # real signature unknown; restored from __doc__
        """ set_metadata(self, longname:str, classification:str, description:str, author:str) """
        pass

    def set_static_metadata(self, longname, classification, description, author): # real signature unknown; restored from __doc__
        """ set_static_metadata(self, longname:str, classification:str, description:str, author:str) """
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

    change_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    elementfactory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    no_more_pads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numpadtemplates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padtemplates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_templ_cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    post_message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    provide_clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    release_pad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    request_new_pad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    send_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_bus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ElementClass), '__module__': 'gi.repository.Gst', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ElementClass' objects>, '__weakref__': <attribute '__weakref__' of 'ElementClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f4260549bd0>, 'metadata': <property object at 0x7f4260549cc0>, 'elementfactory': <property object at 0x7f4260549db0>, 'padtemplates': <property object at 0x7f4260549ea0>, 'numpadtemplates': <property object at 0x7f4260549f90>, 'pad_templ_cookie': <property object at 0x7f426054e130>, 'pad_added': <property object at 0x7f426054e220>, 'pad_removed': <property object at 0x7f426054e310>, 'no_more_pads': <property object at 0x7f426054e400>, 'request_new_pad': <property object at 0x7f426054e4f0>, 'release_pad': <property object at 0x7f426054e5e0>, 'get_state': <property object at 0x7f426054e6d0>, 'set_state': <property object at 0x7f426054e7c0>, 'change_state': <property object at 0x7f426054e8b0>, 'state_changed': <property object at 0x7f426054e950>, 'set_bus': <property object at 0x7f426054ea40>, 'provide_clock': <property object at 0x7f426054eb30>, 'set_clock': <property object at 0x7f426054ec20>, 'send_event': <property object at 0x7f426054ed10>, 'query': <property object at 0x7f426054ee00>, 'post_message': <property object at 0x7f426054eef0>, 'set_context': <property object at 0x7f4260550040>, '_gst_reserved': <property object at 0x7f4260550130>, 'add_metadata': gi.FunctionInfo(add_metadata), 'add_pad_template': gi.FunctionInfo(add_pad_template), 'add_static_metadata': gi.FunctionInfo(add_static_metadata), 'add_static_pad_template': gi.FunctionInfo(add_static_pad_template), 'add_static_pad_template_with_gtype': gi.FunctionInfo(add_static_pad_template_with_gtype), 'get_metadata': gi.FunctionInfo(get_metadata), 'get_pad_template': gi.FunctionInfo(get_pad_template), 'get_pad_template_list': gi.FunctionInfo(get_pad_template_list), 'set_metadata': gi.FunctionInfo(set_metadata), 'set_static_metadata': gi.FunctionInfo(set_static_metadata)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ElementClass)


