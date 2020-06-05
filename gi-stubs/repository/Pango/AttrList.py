# encoding: utf-8
# module gi.repository.Pango
# from /usr/lib64/girepository-1.0/Pango-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


class AttrList(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> Pango.AttrList
    """
    def change(self, attr): # real signature unknown; restored from __doc__
        """ change(self, attr:Pango.Attribute) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Pango.AttrList or None """
        pass

    def filter(self, func, data=None): # real signature unknown; restored from __doc__
        """ filter(self, func:Pango.AttrFilterFunc, data=None) -> Pango.AttrList or None """
        pass

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_iterator(self): # real signature unknown; restored from __doc__
        """ get_iterator(self) -> Pango.AttrIterator """
        pass

    def insert(self, attr): # real signature unknown; restored from __doc__
        """ insert(self, attr:Pango.Attribute) """
        pass

    def insert_before(self, attr): # real signature unknown; restored from __doc__
        """ insert_before(self, attr:Pango.Attribute) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Pango.AttrList """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Pango.AttrList """
        pass

    def splice(self, other, pos, len): # real signature unknown; restored from __doc__
        """ splice(self, other:Pango.AttrList, pos:int, len:int) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def update(self, pos, remove, add): # real signature unknown; restored from __doc__
        """ update(self, pos:int, remove:int, add:int) """
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
        """ new() -> Pango.AttrList """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AttrList), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoAttrList (94752680787664)>, '__dict__': <attribute '__dict__' of 'AttrList' objects>, '__weakref__': <attribute '__weakref__' of 'AttrList' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'change': gi.FunctionInfo(change), 'copy': gi.FunctionInfo(copy), 'filter': gi.FunctionInfo(filter), 'get_attributes': gi.FunctionInfo(get_attributes), 'get_iterator': gi.FunctionInfo(get_iterator), 'insert': gi.FunctionInfo(insert), 'insert_before': gi.FunctionInfo(insert_before), 'ref': gi.FunctionInfo(ref), 'splice': gi.FunctionInfo(splice), 'unref': gi.FunctionInfo(unref), 'update': gi.FunctionInfo(update), '__new__': <staticmethod object at 0x7f24746df7c0>, '__init__': <function nothing at 0x7f2474a83430>})"
    __gtype__ = None # (!) real value is '<GType PangoAttrList (94752680787664)>'
    __info__ = StructInfo(AttrList)


