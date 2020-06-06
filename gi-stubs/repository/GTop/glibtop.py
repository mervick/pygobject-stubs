# encoding: utf-8
# module gi.repository.GTop
# from /usr/lib64/girepository-1.0/GTop-2.0.typelib
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


class glibtop(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        glibtop()
    """
    def call_l(self, command, send_size, send_buf=None, recv_size, recv_buf=None): # real signature unknown; restored from __doc__
        """ call_l(self, command:int, send_size:int, send_buf=None, recv_size:int, recv_buf=None) """
        pass

    def call_s(self, command, send_size, send_buf=None, recv_size, recv_buf=None): # real signature unknown; restored from __doc__
        """ call_s(self, command:int, send_size:int, send_buf=None, recv_size:int, recv_buf=None) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close() """
        pass

    def close_p(self): # real signature unknown; restored from __doc__
        """ close_p(self) """
        pass

    def close_r(self): # real signature unknown; restored from __doc__
        """ close_r(self) """
        pass

    def close_s(self): # real signature unknown; restored from __doc__
        """ close_s(self) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_cpu(self, buf): # real signature unknown; restored from __doc__
        """ get_cpu(buf:GTop.glibtop_cpu) """
        pass

    def get_cpu_l(self, buf): # real signature unknown; restored from __doc__
        """ get_cpu_l(self, buf:GTop.glibtop_cpu) """
        pass

    def get_cpu_s(self, buf): # real signature unknown; restored from __doc__
        """ get_cpu_s(self, buf:GTop.glibtop_cpu) """
        pass

    def get_fsusage(self, buf, mount_dir): # real signature unknown; restored from __doc__
        """ get_fsusage(buf:GTop.glibtop_fsusage, mount_dir:str) """
        pass

    def get_fsusage_l(self, buf, mount_dir): # real signature unknown; restored from __doc__
        """ get_fsusage_l(self, buf:GTop.glibtop_fsusage, mount_dir:str) """
        pass

    def get_fsusage_s(self, buf, mount_dir): # real signature unknown; restored from __doc__
        """ get_fsusage_s(self, buf:GTop.glibtop_fsusage, mount_dir:str) """
        pass

    def get_loadavg(self, buf): # real signature unknown; restored from __doc__
        """ get_loadavg(buf:GTop.glibtop_loadavg) """
        pass

    def get_loadavg_l(self, buf): # real signature unknown; restored from __doc__
        """ get_loadavg_l(self, buf:GTop.glibtop_loadavg) """
        pass

    def get_loadavg_s(self, buf): # real signature unknown; restored from __doc__
        """ get_loadavg_s(self, buf:GTop.glibtop_loadavg) """
        pass

    def get_mem(self, buf): # real signature unknown; restored from __doc__
        """ get_mem(buf:GTop.glibtop_mem) """
        pass

    def get_mem_l(self, buf): # real signature unknown; restored from __doc__
        """ get_mem_l(self, buf:GTop.glibtop_mem) """
        pass

    def get_mem_s(self, buf): # real signature unknown; restored from __doc__
        """ get_mem_s(self, buf:GTop.glibtop_mem) """
        pass

    def get_mountlist(self, buf, all_fs): # real signature unknown; restored from __doc__
        """ get_mountlist(buf:GTop.glibtop_mountlist, all_fs:int) -> list """
        return []

    def get_mountlist_l(self, all_fs): # real signature unknown; restored from __doc__
        """ get_mountlist_l(self, all_fs:int) -> list, buf:GTop.glibtop_mountlist """
        return []

    def get_mountlist_s(self, all_fs): # real signature unknown; restored from __doc__
        """ get_mountlist_s(self, all_fs:int) -> list, buf:GTop.glibtop_mountlist """
        return []

    def get_msg_limits(self, buf): # real signature unknown; restored from __doc__
        """ get_msg_limits(buf:GTop.glibtop_msg_limits) """
        pass

    def get_msg_limits_l(self, buf): # real signature unknown; restored from __doc__
        """ get_msg_limits_l(self, buf:GTop.glibtop_msg_limits) """
        pass

    def get_msg_limits_s(self, buf): # real signature unknown; restored from __doc__
        """ get_msg_limits_s(self, buf:GTop.glibtop_msg_limits) """
        pass

    def get_netlist(self, buf): # real signature unknown; restored from __doc__
        """ get_netlist(buf:GTop.glibtop_netlist) -> list """
        return []

    def get_netlist_l(self, buf): # real signature unknown; restored from __doc__
        """ get_netlist_l(self, buf:GTop.glibtop_netlist) -> list """
        return []

    def get_netlist_s(self, buf): # real signature unknown; restored from __doc__
        """ get_netlist_s(self, buf:GTop.glibtop_netlist) -> list """
        return []

    def get_netload(self, buf, interface): # real signature unknown; restored from __doc__
        """ get_netload(buf:GTop.glibtop_netload, interface:str) """
        pass

    def get_netload_l(self, buf, interface): # real signature unknown; restored from __doc__
        """ get_netload_l(self, buf:GTop.glibtop_netload, interface:str) """
        pass

    def get_netload_s(self, buf, interface): # real signature unknown; restored from __doc__
        """ get_netload_s(self, buf:GTop.glibtop_netload, interface:str) """
        pass

    def get_parameter_l(self, parameter, data_ptr=None, data_size): # real signature unknown; restored from __doc__
        """ get_parameter_l(self, parameter:int, data_ptr=None, data_size:int) -> int """
        return 0

    def get_ppp(self, buf, device): # real signature unknown; restored from __doc__
        """ get_ppp(buf:GTop.glibtop_ppp, device:int) """
        pass

    def get_ppp_l(self, buf, device): # real signature unknown; restored from __doc__
        """ get_ppp_l(self, buf:GTop.glibtop_ppp, device:int) """
        pass

    def get_ppp_s(self, buf, device): # real signature unknown; restored from __doc__
        """ get_ppp_s(self, buf:GTop.glibtop_ppp, device:int) """
        pass

    def get_proclist(self, buf, which, arg): # real signature unknown; restored from __doc__
        """ get_proclist(buf:GTop.glibtop_proclist, which:int, arg:int) -> list """
        return []

    def get_proclist_l(self, buf, which, arg): # real signature unknown; restored from __doc__
        """ get_proclist_l(self, buf:GTop.glibtop_proclist, which:int, arg:int) -> list """
        return []

    def get_proclist_s(self, buf, which, arg): # real signature unknown; restored from __doc__
        """ get_proclist_s(self, buf:GTop.glibtop_proclist, which:int, arg:int) -> list """
        return []

    def get_proc_affinity(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_affinity(buf:GTop.glibtop_proc_affinity, pid:int) -> int """
        return 0

    def get_proc_affinity_l(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_affinity_l(self, buf:GTop.glibtop_proc_affinity, pid:int) -> int """
        return 0

    def get_proc_affinity_s(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_affinity_s(self, buf:GTop.glibtop_proc_affinity, pid:int) -> int """
        return 0

    def get_proc_args(self, buf, pid, max_len): # real signature unknown; restored from __doc__
        """ get_proc_args(buf:GTop.glibtop_proc_args, pid:int, max_len:int) -> str """
        return ""

    def get_proc_args_l(self, buf, pid, max_len): # real signature unknown; restored from __doc__
        """ get_proc_args_l(self, buf:GTop.glibtop_proc_args, pid:int, max_len:int) -> str """
        return ""

    def get_proc_args_s(self, buf, pid, max_len): # real signature unknown; restored from __doc__
        """ get_proc_args_s(self, buf:GTop.glibtop_proc_args, pid:int, max_len:int) -> str """
        return ""

    def get_proc_argv(self, buf, pid, max_len): # real signature unknown; restored from __doc__
        """ get_proc_argv(buf:GTop.glibtop_proc_args, pid:int, max_len:int) -> list """
        return []

    def get_proc_io(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_io(buf:GTop.glibtop_proc_io, pid:int) """
        pass

    def get_proc_io_l(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_io_l(self, buf:GTop.glibtop_proc_io, pid:int) """
        pass

    def get_proc_io_s(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_io_s(self, buf:GTop.glibtop_proc_io, pid:int) """
        pass

    def get_proc_kernel(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_kernel(buf:GTop.glibtop_proc_kernel, pid:int) """
        pass

    def get_proc_kernel_l(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_kernel_l(self, buf:GTop.glibtop_proc_kernel, pid:int) """
        pass

    def get_proc_kernel_s(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_kernel_s(self, buf:GTop.glibtop_proc_kernel, pid:int) """
        pass

    def get_proc_map(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_map(buf:GTop.glibtop_proc_map, pid:int) -> list """
        return []

    def get_proc_map_l(self, pid): # real signature unknown; restored from __doc__
        """ get_proc_map_l(self, pid:int) -> list, buf:GTop.glibtop_proc_map """
        return []

    def get_proc_map_s(self, pid): # real signature unknown; restored from __doc__
        """ get_proc_map_s(self, pid:int) -> list, buf:GTop.glibtop_proc_map """
        return []

    def get_proc_mem(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_mem(buf:GTop.glibtop_proc_mem, pid:int) """
        pass

    def get_proc_mem_l(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_mem_l(self, buf:GTop.glibtop_proc_mem, pid:int) """
        pass

    def get_proc_mem_s(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_mem_s(self, buf:GTop.glibtop_proc_mem, pid:int) """
        pass

    def get_proc_open_files(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_open_files(buf:GTop.glibtop_proc_open_files, pid:int) -> list """
        return []

    def get_proc_open_files_l(self, pid): # real signature unknown; restored from __doc__
        """ get_proc_open_files_l(self, pid:int) -> list, buf:GTop.glibtop_proc_open_files """
        return []

    def get_proc_open_files_s(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_open_files_s(self, buf:GTop.glibtop_proc_open_files, pid:int) -> GTop.glibtop_open_files_entry """
        pass

    def get_proc_segment(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_segment(buf:GTop.glibtop_proc_segment, pid:int) """
        pass

    def get_proc_segment_l(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_segment_l(self, buf:GTop.glibtop_proc_segment, pid:int) """
        pass

    def get_proc_segment_s(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_segment_s(self, buf:GTop.glibtop_proc_segment, pid:int) """
        pass

    def get_proc_signal(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_signal(buf:GTop.glibtop_proc_signal, pid:int) """
        pass

    def get_proc_signal_l(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_signal_l(self, buf:GTop.glibtop_proc_signal, pid:int) """
        pass

    def get_proc_signal_s(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_signal_s(self, buf:GTop.glibtop_proc_signal, pid:int) """
        pass

    def get_proc_state(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_state(buf:GTop.glibtop_proc_state, pid:int) """
        pass

    def get_proc_state_l(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_state_l(self, buf:GTop.glibtop_proc_state, pid:int) """
        pass

    def get_proc_state_s(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_state_s(self, buf:GTop.glibtop_proc_state, pid:int) """
        pass

    def get_proc_time(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_time(buf:GTop.glibtop_proc_time, pid:int) """
        pass

    def get_proc_time_l(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_time_l(self, buf:GTop.glibtop_proc_time, pid:int) """
        pass

    def get_proc_time_s(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_time_s(self, buf:GTop.glibtop_proc_time, pid:int) """
        pass

    def get_proc_uid(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_uid(buf:GTop.glibtop_proc_uid, pid:int) """
        pass

    def get_proc_uid_l(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_uid_l(self, buf:GTop.glibtop_proc_uid, pid:int) """
        pass

    def get_proc_uid_s(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_uid_s(self, buf:GTop.glibtop_proc_uid, pid:int) """
        pass

    def get_proc_wd(self, buf, pid): # real signature unknown; restored from __doc__
        """ get_proc_wd(buf:GTop.glibtop_proc_wd, pid:int) -> list """
        return []

    def get_sem_limits(self, buf): # real signature unknown; restored from __doc__
        """ get_sem_limits(buf:GTop.glibtop_sem_limits) """
        pass

    def get_sem_limits_l(self, buf): # real signature unknown; restored from __doc__
        """ get_sem_limits_l(self, buf:GTop.glibtop_sem_limits) """
        pass

    def get_sem_limits_s(self, buf): # real signature unknown; restored from __doc__
        """ get_sem_limits_s(self, buf:GTop.glibtop_sem_limits) """
        pass

    def get_shm_limits(self, buf): # real signature unknown; restored from __doc__
        """ get_shm_limits(buf:GTop.glibtop_shm_limits) """
        pass

    def get_shm_limits_l(self, buf): # real signature unknown; restored from __doc__
        """ get_shm_limits_l(self, buf:GTop.glibtop_shm_limits) """
        pass

    def get_shm_limits_s(self, buf): # real signature unknown; restored from __doc__
        """ get_shm_limits_s(self, buf:GTop.glibtop_shm_limits) """
        pass

    def get_swap(self, buf): # real signature unknown; restored from __doc__
        """ get_swap(buf:GTop.glibtop_swap) """
        pass

    def get_swap_l(self, buf): # real signature unknown; restored from __doc__
        """ get_swap_l(self, buf:GTop.glibtop_swap) """
        pass

    def get_swap_s(self, buf): # real signature unknown; restored from __doc__
        """ get_swap_s(self, buf:GTop.glibtop_swap) """
        pass

    def get_sysdeps(self, buf): # real signature unknown; restored from __doc__
        """ get_sysdeps(buf:GTop.glibtop_sysdeps) """
        pass

    def get_sysdeps_r(self, buf): # real signature unknown; restored from __doc__
        """ get_sysdeps_r(self, buf:GTop.glibtop_sysdeps) """
        pass

    def get_sysinfo(self): # real signature unknown; restored from __doc__
        """ get_sysinfo() -> GTop.glibtop_sysinfo """
        pass

    def get_sysinfo_s(self): # real signature unknown; restored from __doc__
        """ get_sysinfo_s(self) -> GTop.glibtop_sysinfo """
        pass

    def get_uptime(self, buf): # real signature unknown; restored from __doc__
        """ get_uptime(buf:GTop.glibtop_uptime) """
        pass

    def get_uptime_l(self, buf): # real signature unknown; restored from __doc__
        """ get_uptime_l(self, buf:GTop.glibtop_uptime) """
        pass

    def get_uptime_s(self, buf): # real signature unknown; restored from __doc__
        """ get_uptime_s(self, buf:GTop.glibtop_uptime) """
        pass

    def init(self): # real signature unknown; restored from __doc__
        """ init() -> GTop.glibtop """
        pass

    def init_p(self, features, flags): # real signature unknown; restored from __doc__
        """ init_p(self, features:int, flags:int) """
        pass

    def init_r(self, features, flags): # real signature unknown; restored from __doc__
        """ init_r(features:int, flags:int) -> GTop.glibtop, server_ptr:GTop.glibtop """
        pass

    def init_s(self, features, flags): # real signature unknown; restored from __doc__
        """ init_s(features:int, flags:int) -> GTop.glibtop, server_ptr:GTop.glibtop """
        pass

    def internet_addr(self, host): # real signature unknown; restored from __doc__
        """ internet_addr(host:str) -> int """
        return 0

    def make_connection(self, hostarg, portarg, s): # real signature unknown; restored from __doc__
        """ make_connection(hostarg:str, portarg:int, s:int) -> int """
        return 0

    def open_l(self, program_name, features, flags): # real signature unknown; restored from __doc__
        """ open_l(self, program_name:str, features:int, flags:int) """
        pass

    def open_p(self, program_name, features, flags): # real signature unknown; restored from __doc__
        """ open_p(self, program_name:str, features:int, flags:int) """
        pass

    def open_s(self, program_name, features, flags): # real signature unknown; restored from __doc__
        """ open_s(self, program_name:str, features:int, flags:int) """
        pass

    def set_parameter_l(self, parameter, data_ptr=None, data_size): # real signature unknown; restored from __doc__
        """ set_parameter_l(self, parameter:int, data_ptr=None, data_size:int) """
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

    egid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    euid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    features = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    machine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ncpu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    os_version_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    real_ncpu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    required = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_rsh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    socket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sysdeps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(glibtop), '__module__': 'gi.repository.GTop', '__gtype__': <GType glibtop (94880753217472)>, '__dict__': <attribute '__dict__' of 'glibtop' objects>, '__weakref__': <attribute '__weakref__' of 'glibtop' objects>, '__doc__': None, 'flags': <property object at 0x7f9700c70e50>, 'method': <property object at 0x7f9700c70f40>, 'error_method': <property object at 0x7f9700c64090>, 'input': <property object at 0x7f9700c64180>, 'output': <property object at 0x7f9700c64270>, 'socket': <property object at 0x7f9700c64360>, 'ncpu': <property object at 0x7f9700c64450>, 'real_ncpu': <property object at 0x7f9700c64540>, 'os_version_code': <property object at 0x7f9700c64630>, 'name': <property object at 0x7f9700c64720>, 'server_command': <property object at 0x7f9700c64810>, 'server_host': <property object at 0x7f9700c64900>, 'server_user': <property object at 0x7f9700c649f0>, 'server_rsh': <property object at 0x7f9700c64ae0>, 'features': <property object at 0x7f9700c64bd0>, 'server_port': <property object at 0x7f9700c64cc0>, 'sysdeps': <property object at 0x7f9700c64db0>, 'required': <property object at 0x7f9700c64ea0>, 'pid': <property object at 0x7f9700c64f90>, 'uid': <property object at 0x7f9700c650e0>, 'euid': <property object at 0x7f9700c651d0>, 'gid': <property object at 0x7f9700c652c0>, 'egid': <property object at 0x7f9700c653b0>, 'machine': <property object at 0x7f9700c654a0>, 'call_l': gi.FunctionInfo(call_l), 'call_s': gi.FunctionInfo(call_s), 'close_p': gi.FunctionInfo(close_p), 'close_r': gi.FunctionInfo(close_r), 'close_s': gi.FunctionInfo(close_s), 'get_cpu_l': gi.FunctionInfo(get_cpu_l), 'get_cpu_s': gi.FunctionInfo(get_cpu_s), 'get_fsusage_l': gi.FunctionInfo(get_fsusage_l), 'get_fsusage_s': gi.FunctionInfo(get_fsusage_s), 'get_loadavg_l': gi.FunctionInfo(get_loadavg_l), 'get_loadavg_s': gi.FunctionInfo(get_loadavg_s), 'get_mem_l': gi.FunctionInfo(get_mem_l), 'get_mem_s': gi.FunctionInfo(get_mem_s), 'get_mountlist_l': gi.FunctionInfo(get_mountlist_l), 'get_mountlist_s': gi.FunctionInfo(get_mountlist_s), 'get_msg_limits_l': gi.FunctionInfo(get_msg_limits_l), 'get_msg_limits_s': gi.FunctionInfo(get_msg_limits_s), 'get_netlist_l': gi.FunctionInfo(get_netlist_l), 'get_netlist_s': gi.FunctionInfo(get_netlist_s), 'get_netload_l': gi.FunctionInfo(get_netload_l), 'get_netload_s': gi.FunctionInfo(get_netload_s), 'get_parameter_l': gi.FunctionInfo(get_parameter_l), 'get_ppp_l': gi.FunctionInfo(get_ppp_l), 'get_ppp_s': gi.FunctionInfo(get_ppp_s), 'get_proc_affinity_l': gi.FunctionInfo(get_proc_affinity_l), 'get_proc_affinity_s': gi.FunctionInfo(get_proc_affinity_s), 'get_proc_args_l': gi.FunctionInfo(get_proc_args_l), 'get_proc_args_s': gi.FunctionInfo(get_proc_args_s), 'get_proc_io_l': gi.FunctionInfo(get_proc_io_l), 'get_proc_io_s': gi.FunctionInfo(get_proc_io_s), 'get_proc_kernel_l': gi.FunctionInfo(get_proc_kernel_l), 'get_proc_kernel_s': gi.FunctionInfo(get_proc_kernel_s), 'get_proc_map_l': gi.FunctionInfo(get_proc_map_l), 'get_proc_map_s': gi.FunctionInfo(get_proc_map_s), 'get_proc_mem_l': gi.FunctionInfo(get_proc_mem_l), 'get_proc_mem_s': gi.FunctionInfo(get_proc_mem_s), 'get_proc_open_files_l': gi.FunctionInfo(get_proc_open_files_l), 'get_proc_open_files_s': gi.FunctionInfo(get_proc_open_files_s), 'get_proc_segment_l': gi.FunctionInfo(get_proc_segment_l), 'get_proc_segment_s': gi.FunctionInfo(get_proc_segment_s), 'get_proc_signal_l': gi.FunctionInfo(get_proc_signal_l), 'get_proc_signal_s': gi.FunctionInfo(get_proc_signal_s), 'get_proc_state_l': gi.FunctionInfo(get_proc_state_l), 'get_proc_state_s': gi.FunctionInfo(get_proc_state_s), 'get_proc_time_l': gi.FunctionInfo(get_proc_time_l), 'get_proc_time_s': gi.FunctionInfo(get_proc_time_s), 'get_proc_uid_l': gi.FunctionInfo(get_proc_uid_l), 'get_proc_uid_s': gi.FunctionInfo(get_proc_uid_s), 'get_proclist_l': gi.FunctionInfo(get_proclist_l), 'get_proclist_s': gi.FunctionInfo(get_proclist_s), 'get_sem_limits_l': gi.FunctionInfo(get_sem_limits_l), 'get_sem_limits_s': gi.FunctionInfo(get_sem_limits_s), 'get_shm_limits_l': gi.FunctionInfo(get_shm_limits_l), 'get_shm_limits_s': gi.FunctionInfo(get_shm_limits_s), 'get_swap_l': gi.FunctionInfo(get_swap_l), 'get_swap_s': gi.FunctionInfo(get_swap_s), 'get_sysdeps_r': gi.FunctionInfo(get_sysdeps_r), 'get_sysinfo_s': gi.FunctionInfo(get_sysinfo_s), 'get_uptime_l': gi.FunctionInfo(get_uptime_l), 'get_uptime_s': gi.FunctionInfo(get_uptime_s), 'init_p': gi.FunctionInfo(init_p), 'open_l': gi.FunctionInfo(open_l), 'open_p': gi.FunctionInfo(open_p), 'open_s': gi.FunctionInfo(open_s), 'set_parameter_l': gi.FunctionInfo(set_parameter_l), 'close': gi.FunctionInfo(close), 'get_cpu': gi.FunctionInfo(get_cpu), 'get_fsusage': gi.FunctionInfo(get_fsusage), 'get_loadavg': gi.FunctionInfo(get_loadavg), 'get_mem': gi.FunctionInfo(get_mem), 'get_mountlist': gi.FunctionInfo(get_mountlist), 'get_msg_limits': gi.FunctionInfo(get_msg_limits), 'get_netlist': gi.FunctionInfo(get_netlist), 'get_netload': gi.FunctionInfo(get_netload), 'get_ppp': gi.FunctionInfo(get_ppp), 'get_proc_affinity': gi.FunctionInfo(get_proc_affinity), 'get_proc_args': gi.FunctionInfo(get_proc_args), 'get_proc_argv': gi.FunctionInfo(get_proc_argv), 'get_proc_io': gi.FunctionInfo(get_proc_io), 'get_proc_kernel': gi.FunctionInfo(get_proc_kernel), 'get_proc_map': gi.FunctionInfo(get_proc_map), 'get_proc_mem': gi.FunctionInfo(get_proc_mem), 'get_proc_open_files': gi.FunctionInfo(get_proc_open_files), 'get_proc_segment': gi.FunctionInfo(get_proc_segment), 'get_proc_signal': gi.FunctionInfo(get_proc_signal), 'get_proc_state': gi.FunctionInfo(get_proc_state), 'get_proc_time': gi.FunctionInfo(get_proc_time), 'get_proc_uid': gi.FunctionInfo(get_proc_uid), 'get_proc_wd': gi.FunctionInfo(get_proc_wd), 'get_proclist': gi.FunctionInfo(get_proclist), 'get_sem_limits': gi.FunctionInfo(get_sem_limits), 'get_shm_limits': gi.FunctionInfo(get_shm_limits), 'get_swap': gi.FunctionInfo(get_swap), 'get_sysdeps': gi.FunctionInfo(get_sysdeps), 'get_sysinfo': gi.FunctionInfo(get_sysinfo), 'get_uptime': gi.FunctionInfo(get_uptime), 'init': gi.FunctionInfo(init), 'init_r': gi.FunctionInfo(init_r), 'init_s': gi.FunctionInfo(init_s), 'internet_addr': gi.FunctionInfo(internet_addr), 'make_connection': gi.FunctionInfo(make_connection)})"
    __gtype__ = None # (!) real value is '<GType glibtop (94880753217472)>'
    __info__ = StructInfo(glibtop)


