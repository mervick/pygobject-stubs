# encoding: utf-8
# module gi.repository.EvinceDocument
# from /usr/lib64/girepository-1.0/EvinceDocument-3.0.typelib
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


class DocumentInfo(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        DocumentInfo()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EvinceDocument.DocumentInfo """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
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

    author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    creation_date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    creator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fields_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    license = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linearized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modified_date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_pages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    paper_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    paper_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    permissions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    producer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ui_hints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DocumentInfo), '__module__': 'gi.repository.EvinceDocument', '__gtype__': <GType EvDocumentInfo (94742334128832)>, '__dict__': <attribute '__dict__' of 'DocumentInfo' objects>, '__weakref__': <attribute '__weakref__' of 'DocumentInfo' objects>, '__doc__': None, 'title': <property object at 0x7f6ab165ae50>, 'format': <property object at 0x7f6ab165af40>, 'author': <property object at 0x7f6ab165b090>, 'subject': <property object at 0x7f6ab165b180>, 'keywords': <property object at 0x7f6ab165b270>, 'creator': <property object at 0x7f6ab165b360>, 'producer': <property object at 0x7f6ab165b450>, 'linearized': <property object at 0x7f6ab165b540>, 'security': <property object at 0x7f6ab165b630>, 'creation_date': <property object at 0x7f6ab165b720>, 'modified_date': <property object at 0x7f6ab165b810>, 'layout': <property object at 0x7f6ab165b900>, 'mode': <property object at 0x7f6ab165b9f0>, 'ui_hints': <property object at 0x7f6ab165bae0>, 'permissions': <property object at 0x7f6ab165bbd0>, 'n_pages': <property object at 0x7f6ab165bcc0>, 'paper_height': <property object at 0x7f6ab165bdb0>, 'paper_width': <property object at 0x7f6ab165bea0>, 'license': <property object at 0x7f6ab165bf90>, 'fields_mask': <property object at 0x7f6ab165c0e0>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free)})"
    __gtype__ = None # (!) real value is '<GType EvDocumentInfo (94742334128832)>'
    __info__ = StructInfo(DocumentInfo)


