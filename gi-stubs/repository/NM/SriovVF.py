# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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


class SriovVF(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(index:int) -> NM.SriovVF
    """
    def add_vlan(self, vlan_id): # real signature unknown; restored from __doc__
        """ add_vlan(self, vlan_id:int) -> bool """
        return False

    def attribute_validate(self, name, value): # real signature unknown; restored from __doc__
        """ attribute_validate(name:str, value:GLib.Variant) -> bool, known:bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> NM.SriovVF """
        pass

    def equal(self, other): # real signature unknown; restored from __doc__
        """ equal(self, other:NM.SriovVF) -> bool """
        return False

    def get_attribute(self, name): # real signature unknown; restored from __doc__
        """ get_attribute(self, name:str) -> GLib.Variant """
        pass

    def get_attribute_names(self): # real signature unknown; restored from __doc__
        """ get_attribute_names(self) -> list """
        return []

    def get_index(self): # real signature unknown; restored from __doc__
        """ get_index(self) -> int """
        return 0

    def get_vlan_ids(self): # real signature unknown; restored from __doc__
        """ get_vlan_ids(self) -> list, length:int """
        return []

    def get_vlan_protocol(self, vlan_id): # real signature unknown; restored from __doc__
        """ get_vlan_protocol(self, vlan_id:int) -> NM.SriovVFVlanProtocol """
        pass

    def get_vlan_qos(self, vlan_id): # real signature unknown; restored from __doc__
        """ get_vlan_qos(self, vlan_id:int) -> int """
        return 0

    def new(self, index): # real signature unknown; restored from __doc__
        """ new(index:int) -> NM.SriovVF """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) """
        pass

    def remove_vlan(self, vlan_id): # real signature unknown; restored from __doc__
        """ remove_vlan(self, vlan_id:int) -> bool """
        return False

    def set_attribute(self, name, value=None): # real signature unknown; restored from __doc__
        """ set_attribute(self, name:str, value:GLib.Variant=None) """
        pass

    def set_vlan_protocol(self, vlan_id, protocol): # real signature unknown; restored from __doc__
        """ set_vlan_protocol(self, vlan_id:int, protocol:NM.SriovVFVlanProtocol) """
        pass

    def set_vlan_qos(self, vlan_id, qos): # real signature unknown; restored from __doc__
        """ set_vlan_qos(self, vlan_id:int, qos:int) """
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
        """ new(index:int) -> NM.SriovVF """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SriovVF), '__module__': 'gi.repository.NM', '__gtype__': <GType NMSriovVF (94741104653264)>, '__dict__': <attribute '__dict__' of 'SriovVF' objects>, '__weakref__': <attribute '__weakref__' of 'SriovVF' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'add_vlan': gi.FunctionInfo(add_vlan), 'dup': gi.FunctionInfo(dup), 'equal': gi.FunctionInfo(equal), 'get_attribute': gi.FunctionInfo(get_attribute), 'get_attribute_names': gi.FunctionInfo(get_attribute_names), 'get_index': gi.FunctionInfo(get_index), 'get_vlan_ids': gi.FunctionInfo(get_vlan_ids), 'get_vlan_protocol': gi.FunctionInfo(get_vlan_protocol), 'get_vlan_qos': gi.FunctionInfo(get_vlan_qos), 'ref': gi.FunctionInfo(ref), 'remove_vlan': gi.FunctionInfo(remove_vlan), 'set_attribute': gi.FunctionInfo(set_attribute), 'set_vlan_protocol': gi.FunctionInfo(set_vlan_protocol), 'set_vlan_qos': gi.FunctionInfo(set_vlan_qos), 'unref': gi.FunctionInfo(unref), 'attribute_validate': gi.FunctionInfo(attribute_validate), '__new__': <staticmethod object at 0x7fb9b8497520>, '__init__': <function nothing at 0x7fb9b8f70ee0>})"
    __gtype__ = None # (!) real value is '<GType NMSriovVF (94741104653264)>'
    __info__ = StructInfo(SriovVF)


