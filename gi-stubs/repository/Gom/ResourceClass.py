# encoding: utf-8
# module gi.repository.Gom
# from /usr/lib64/girepository-1.0/Gom-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class ResourceClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ResourceClass()
    """
    def set_notnull(self, property_name): # real signature unknown; restored from __doc__
        """ set_notnull(self, property_name:str) """
        pass

    def set_primary_key(self, primary_key): # real signature unknown; restored from __doc__
        """ set_primary_key(self, primary_key:str) """
        pass

    def set_property_from_bytes(self, property_name, from_bytes_func): # real signature unknown; restored from __doc__
        """ set_property_from_bytes(self, property_name:str, from_bytes_func:Gom.ResourceFromBytesFunc) """
        pass

    def set_property_new_in_version(self, property_name, version): # real signature unknown; restored from __doc__
        """ set_property_new_in_version(self, property_name:str, version:int) """
        pass

    def set_property_set_mapped(self, property_name, is_mapped): # real signature unknown; restored from __doc__
        """ set_property_set_mapped(self, property_name:str, is_mapped:bool) """
        pass

    def set_property_to_bytes(self, property_name, to_bytes_func): # real signature unknown; restored from __doc__
        """ set_property_to_bytes(self, property_name:str, to_bytes_func:Gom.ResourceToBytesFunc) """
        pass

    def set_reference(self, property_name, ref_table_name, ref_property_name): # real signature unknown; restored from __doc__
        """ set_reference(self, property_name:str, ref_table_name:str, ref_property_name:str) """
        pass

    def set_table(self, table): # real signature unknown; restored from __doc__
        """ set_table(self, table:str) """
        pass

    def set_unique(self, property_name): # real signature unknown; restored from __doc__
        """ set_unique(self, property_name:str) """
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    primary_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ResourceClass), '__module__': 'gi.repository.Gom', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ResourceClass' objects>, '__weakref__': <attribute '__weakref__' of 'ResourceClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7ff300be0130>, 'primary_key': <property object at 0x7ff300be0220>, 'table': <property object at 0x7ff300be0310>, 'set_notnull': gi.FunctionInfo(set_notnull), 'set_primary_key': gi.FunctionInfo(set_primary_key), 'set_property_from_bytes': gi.FunctionInfo(set_property_from_bytes), 'set_property_new_in_version': gi.FunctionInfo(set_property_new_in_version), 'set_property_set_mapped': gi.FunctionInfo(set_property_set_mapped), 'set_property_to_bytes': gi.FunctionInfo(set_property_to_bytes), 'set_reference': gi.FunctionInfo(set_reference), 'set_table': gi.FunctionInfo(set_table), 'set_unique': gi.FunctionInfo(set_unique)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ResourceClass)


