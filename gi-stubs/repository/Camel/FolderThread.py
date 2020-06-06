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


class FolderThread(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        FolderThread()
        new(folder:Camel.Folder, uids:list, thread_subject:bool) -> Camel.FolderThread
    """
    def apply(self, uids): # real signature unknown; restored from __doc__
        """ apply(self, uids:list) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def new(self, folder, uids, thread_subject): # real signature unknown; restored from __doc__
        """ new(folder:Camel.Folder, uids:list, thread_subject:bool) -> Camel.FolderThread """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Camel.FolderThread """
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

    folder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_chunks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FolderThread), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelFolderThread (94124523715200)>, '__dict__': <attribute '__dict__' of 'FolderThread' objects>, '__weakref__': <attribute '__weakref__' of 'FolderThread' objects>, '__doc__': None, 'refcount': <property object at 0x7f7b34fd9090>, 'subject': <property object at 0x7f7b34fd9180>, 'tree': <property object at 0x7f7b34fd9270>, 'node_chunks': <property object at 0x7f7b34fd9360>, 'folder': <property object at 0x7f7b34fd9450>, 'summary': <property object at 0x7f7b34fd9540>, 'new': gi.FunctionInfo(new), 'apply': gi.FunctionInfo(apply), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType CamelFolderThread (94124523715200)>'
    __info__ = StructInfo(FolderThread)


