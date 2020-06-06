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


class DocumentFonts(__gobject.GInterface):
    # no doc
    def fill_model(self, model): # real signature unknown; restored from __doc__
        """ fill_model(self, model:Gtk.TreeModel) """
        pass

    def get_fonts_summary(self): # real signature unknown; restored from __doc__
        """ get_fonts_summary(self) -> str """
        return ""

    def get_progress(self): # real signature unknown; restored from __doc__
        """ get_progress(self) -> float """
        return 0.0

    def scan(self, n_pages): # real signature unknown; restored from __doc__
        """ scan(self, n_pages:int) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(DocumentFonts), '__module__': 'gi.repository.EvinceDocument', '__gtype__': <GType EvDocumentFonts (94742333685600)>, '__dict__': <attribute '__dict__' of 'DocumentFonts' objects>, '__weakref__': <attribute '__weakref__' of 'DocumentFonts' objects>, '__doc__': None, '__gsignals__': {}, 'fill_model': gi.FunctionInfo(fill_model), 'get_fonts_summary': gi.FunctionInfo(get_fonts_summary), 'get_progress': gi.FunctionInfo(get_progress), 'scan': gi.FunctionInfo(scan)})"
    __gdoc__ = 'Interface EvDocumentFonts\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EvDocumentFonts (94742333685600)>'
    __info__ = InterfaceInfo(DocumentFonts)


