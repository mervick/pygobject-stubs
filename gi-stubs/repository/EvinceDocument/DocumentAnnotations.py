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


class DocumentAnnotations(__gobject.GInterface):
    # no doc
    def add_annotation(self, annot, rect): # real signature unknown; restored from __doc__
        """ add_annotation(self, annot:EvinceDocument.Annotation, rect:EvinceDocument.Rectangle) """
        pass

    def can_add_annotation(self): # real signature unknown; restored from __doc__
        """ can_add_annotation(self) -> bool """
        return False

    def can_remove_annotation(self): # real signature unknown; restored from __doc__
        """ can_remove_annotation(self) -> bool """
        return False

    def document_is_modified(self): # real signature unknown; restored from __doc__
        """ document_is_modified(self) -> bool """
        return False

    def get_annotations(self, page): # real signature unknown; restored from __doc__
        """ get_annotations(self, page:EvinceDocument.Page) -> EvinceDocument.MappingList """
        pass

    def remove_annotation(self, annot): # real signature unknown; restored from __doc__
        """ remove_annotation(self, annot:EvinceDocument.Annotation) """
        pass

    def save_annotation(self, annot, mask): # real signature unknown; restored from __doc__
        """ save_annotation(self, annot:EvinceDocument.Annotation, mask:EvinceDocument.AnnotationsSaveMask) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(DocumentAnnotations), '__module__': 'gi.repository.EvinceDocument', '__gtype__': <GType EvDocumentAnnotations (94742333871056)>, '__dict__': <attribute '__dict__' of 'DocumentAnnotations' objects>, '__weakref__': <attribute '__weakref__' of 'DocumentAnnotations' objects>, '__doc__': None, '__gsignals__': {}, 'add_annotation': gi.FunctionInfo(add_annotation), 'can_add_annotation': gi.FunctionInfo(can_add_annotation), 'can_remove_annotation': gi.FunctionInfo(can_remove_annotation), 'document_is_modified': gi.FunctionInfo(document_is_modified), 'get_annotations': gi.FunctionInfo(get_annotations), 'remove_annotation': gi.FunctionInfo(remove_annotation), 'save_annotation': gi.FunctionInfo(save_annotation)})"
    __gdoc__ = 'Interface EvDocumentAnnotations\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EvDocumentAnnotations (94742333871056)>'
    __info__ = InterfaceInfo(DocumentAnnotations)


