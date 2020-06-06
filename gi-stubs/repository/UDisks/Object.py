# encoding: utf-8
# module gi.repository.UDisks
# from /usr/lib64/girepository-1.0/UDisks-2.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class Object(__gobject.GInterface):
    # no doc
    def get_block(self): # real signature unknown; restored from __doc__
        """ get_block(self) -> UDisks.Block or None """
        pass

    def get_drive(self): # real signature unknown; restored from __doc__
        """ get_drive(self) -> UDisks.Drive or None """
        pass

    def get_drive_ata(self): # real signature unknown; restored from __doc__
        """ get_drive_ata(self) -> UDisks.DriveAta or None """
        pass

    def get_encrypted(self): # real signature unknown; restored from __doc__
        """ get_encrypted(self) -> UDisks.Encrypted or None """
        pass

    def get_filesystem(self): # real signature unknown; restored from __doc__
        """ get_filesystem(self) -> UDisks.Filesystem or None """
        pass

    def get_job(self): # real signature unknown; restored from __doc__
        """ get_job(self) -> UDisks.Job or None """
        pass

    def get_loop(self): # real signature unknown; restored from __doc__
        """ get_loop(self) -> UDisks.Loop or None """
        pass

    def get_manager(self): # real signature unknown; restored from __doc__
        """ get_manager(self) -> UDisks.Manager or None """
        pass

    def get_mdraid(self): # real signature unknown; restored from __doc__
        """ get_mdraid(self) -> UDisks.MDRaid or None """
        pass

    def get_partition(self): # real signature unknown; restored from __doc__
        """ get_partition(self) -> UDisks.Partition or None """
        pass

    def get_partition_table(self): # real signature unknown; restored from __doc__
        """ get_partition_table(self) -> UDisks.PartitionTable or None """
        pass

    def get_swapspace(self): # real signature unknown; restored from __doc__
        """ get_swapspace(self) -> UDisks.Swapspace or None """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Object), '__module__': 'gi.repository.UDisks', '__gtype__': <GType UDisksObject (93969722472064)>, '__dict__': <attribute '__dict__' of 'Object' objects>, '__weakref__': <attribute '__weakref__' of 'Object' objects>, '__doc__': None, '__gsignals__': {}, 'get_block': gi.FunctionInfo(get_block), 'get_drive': gi.FunctionInfo(get_drive), 'get_drive_ata': gi.FunctionInfo(get_drive_ata), 'get_encrypted': gi.FunctionInfo(get_encrypted), 'get_filesystem': gi.FunctionInfo(get_filesystem), 'get_job': gi.FunctionInfo(get_job), 'get_loop': gi.FunctionInfo(get_loop), 'get_manager': gi.FunctionInfo(get_manager), 'get_mdraid': gi.FunctionInfo(get_mdraid), 'get_partition': gi.FunctionInfo(get_partition), 'get_partition_table': gi.FunctionInfo(get_partition_table), 'get_swapspace': gi.FunctionInfo(get_swapspace)})"
    __gdoc__ = 'Interface UDisksObject\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UDisksObject (93969722472064)>'
    __info__ = InterfaceInfo(Object)


