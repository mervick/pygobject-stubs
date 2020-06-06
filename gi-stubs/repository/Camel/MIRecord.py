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


class MIRecord(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MIRecord()
    """
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

    attachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dirty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dreceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dsent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    followup_completed_on = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    followup_due_by = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    followup_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    from_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    important = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    junk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    labels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mlist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    msg_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    part = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replied = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usertags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MIRecord), '__module__': 'gi.repository.Camel', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MIRecord' objects>, '__weakref__': <attribute '__weakref__' of 'MIRecord' objects>, '__doc__': None, 'uid': <property object at 0x7f7b34f6ca40>, 'flags': <property object at 0x7f7b34f6cb30>, 'msg_type': <property object at 0x7f7b34f6cc20>, 'dirty': <property object at 0x7f7b34f6cd10>, 'read': <property object at 0x7f7b34f6ce00>, 'deleted': <property object at 0x7f7b34f6cef0>, 'replied': <property object at 0x7f7b34f71040>, 'important': <property object at 0x7f7b34f71130>, 'junk': <property object at 0x7f7b34f71220>, 'attachment': <property object at 0x7f7b34f71310>, 'size': <property object at 0x7f7b34f71400>, 'dsent': <property object at 0x7f7b34f714f0>, 'dreceived': <property object at 0x7f7b34f715e0>, 'subject': <property object at 0x7f7b34f716d0>, 'from_': <property object at 0x7f7b34f717c0>, 'to': <property object at 0x7f7b34f718b0>, 'cc': <property object at 0x7f7b34f719a0>, 'mlist': <property object at 0x7f7b34f71a90>, 'followup_flag': <property object at 0x7f7b34f71b80>, 'followup_completed_on': <property object at 0x7f7b34f71cc0>, 'followup_due_by': <property object at 0x7f7b34f71db0>, 'part': <property object at 0x7f7b34f71ea0>, 'labels': <property object at 0x7f7b34f71f90>, 'usertags': <property object at 0x7f7b34f72090>, 'cinfo': <property object at 0x7f7b34f72180>, 'bdata': <property object at 0x7f7b34f72270>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MIRecord)


