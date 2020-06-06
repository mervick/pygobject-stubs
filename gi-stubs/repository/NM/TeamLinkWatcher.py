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


class TeamLinkWatcher(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_arp_ping(init_wait:int, interval:int, missed_max:int, target_host:str, source_host:str, flags:NM.TeamLinkWatcherArpPingFlags) -> NM.TeamLinkWatcher
        new_arp_ping2(init_wait:int, interval:int, missed_max:int, vlanid:int, target_host:str, source_host:str, flags:NM.TeamLinkWatcherArpPingFlags) -> NM.TeamLinkWatcher
        new_ethtool(delay_up:int, delay_down:int) -> NM.TeamLinkWatcher
        new_nsna_ping(init_wait:int, interval:int, missed_max:int, target_host:str) -> NM.TeamLinkWatcher
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> NM.TeamLinkWatcher """
        pass

    def equal(self, other): # real signature unknown; restored from __doc__
        """ equal(self, other:NM.TeamLinkWatcher) -> bool """
        return False

    def get_delay_down(self): # real signature unknown; restored from __doc__
        """ get_delay_down(self) -> int """
        return 0

    def get_delay_up(self): # real signature unknown; restored from __doc__
        """ get_delay_up(self) -> int """
        return 0

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> NM.TeamLinkWatcherArpPingFlags """
        pass

    def get_init_wait(self): # real signature unknown; restored from __doc__
        """ get_init_wait(self) -> int """
        return 0

    def get_interval(self): # real signature unknown; restored from __doc__
        """ get_interval(self) -> int """
        return 0

    def get_missed_max(self): # real signature unknown; restored from __doc__
        """ get_missed_max(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_source_host(self): # real signature unknown; restored from __doc__
        """ get_source_host(self) -> str """
        return ""

    def get_target_host(self): # real signature unknown; restored from __doc__
        """ get_target_host(self) -> str """
        return ""

    def get_vlanid(self): # real signature unknown; restored from __doc__
        """ get_vlanid(self) -> int """
        return 0

    def new_arp_ping(self, init_wait, interval, missed_max, target_host, source_host, flags): # real signature unknown; restored from __doc__
        """ new_arp_ping(init_wait:int, interval:int, missed_max:int, target_host:str, source_host:str, flags:NM.TeamLinkWatcherArpPingFlags) -> NM.TeamLinkWatcher """
        pass

    def new_arp_ping2(self, init_wait, interval, missed_max, vlanid, target_host, source_host, flags): # real signature unknown; restored from __doc__
        """ new_arp_ping2(init_wait:int, interval:int, missed_max:int, vlanid:int, target_host:str, source_host:str, flags:NM.TeamLinkWatcherArpPingFlags) -> NM.TeamLinkWatcher """
        pass

    def new_ethtool(self, delay_up, delay_down): # real signature unknown; restored from __doc__
        """ new_ethtool(delay_up:int, delay_down:int) -> NM.TeamLinkWatcher """
        pass

    def new_nsna_ping(self, init_wait, interval, missed_max, target_host): # real signature unknown; restored from __doc__
        """ new_nsna_ping(init_wait:int, interval:int, missed_max:int, target_host:str) -> NM.TeamLinkWatcher """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TeamLinkWatcher), '__module__': 'gi.repository.NM', '__gtype__': <GType NMTeamLinkWatcher (94741104674000)>, '__dict__': <attribute '__dict__' of 'TeamLinkWatcher' objects>, '__weakref__': <attribute '__weakref__' of 'TeamLinkWatcher' objects>, '__doc__': None, 'new_arp_ping': gi.FunctionInfo(new_arp_ping), 'new_arp_ping2': gi.FunctionInfo(new_arp_ping2), 'new_ethtool': gi.FunctionInfo(new_ethtool), 'new_nsna_ping': gi.FunctionInfo(new_nsna_ping), 'dup': gi.FunctionInfo(dup), 'equal': gi.FunctionInfo(equal), 'get_delay_down': gi.FunctionInfo(get_delay_down), 'get_delay_up': gi.FunctionInfo(get_delay_up), 'get_flags': gi.FunctionInfo(get_flags), 'get_init_wait': gi.FunctionInfo(get_init_wait), 'get_interval': gi.FunctionInfo(get_interval), 'get_missed_max': gi.FunctionInfo(get_missed_max), 'get_name': gi.FunctionInfo(get_name), 'get_source_host': gi.FunctionInfo(get_source_host), 'get_target_host': gi.FunctionInfo(get_target_host), 'get_vlanid': gi.FunctionInfo(get_vlanid), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType NMTeamLinkWatcher (94741104674000)>'
    __info__ = StructInfo(TeamLinkWatcher)


