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


# Variables with simple values

AUTH_NAMESZ = 15
AUTH_TIMEOUT = 15

CONN_INTERNET = 1
CONN_IPC = 2
CONN_UNIX = 0

DEFAULT_PORT = 21490

DEFAUTH_NAME = 'GNU-SECURE'

EOT_CHR = 92
EOT_STR = '\x04'

FALSE = 0

GLIBTOP_CMND_CPU = 2
GLIBTOP_CMND_FSUSAGE = 21
GLIBTOP_CMND_LOADAVG = 6
GLIBTOP_CMND_MEM = 3
GLIBTOP_CMND_MOUNTLIST = 20

GLIBTOP_CMND_MSG_LIMITS = 8

GLIBTOP_CMND_NETLIST = 24
GLIBTOP_CMND_NETLOAD = 22
GLIBTOP_CMND_PPP = 23
GLIBTOP_CMND_PROCLIST = 10

GLIBTOP_CMND_PROC_AFFINITY = 27
GLIBTOP_CMND_PROC_ARGS = 18
GLIBTOP_CMND_PROC_IO = 28
GLIBTOP_CMND_PROC_KERNEL = 16
GLIBTOP_CMND_PROC_MAP = 19
GLIBTOP_CMND_PROC_MEM = 13

GLIBTOP_CMND_PROC_OPEN_FILES = 25

GLIBTOP_CMND_PROC_SEGMENT = 17
GLIBTOP_CMND_PROC_SIGNAL = 15
GLIBTOP_CMND_PROC_STATE = 11
GLIBTOP_CMND_PROC_TIME = 14
GLIBTOP_CMND_PROC_UID = 12
GLIBTOP_CMND_PROC_WD = 26

GLIBTOP_CMND_QUIT = 0

GLIBTOP_CMND_SEM_LIMITS = 9

GLIBTOP_CMND_SHM_LIMITS = 7

GLIBTOP_CMND_SWAP = 4
GLIBTOP_CMND_SYSDEPS = 1
GLIBTOP_CMND_UPTIME = 5

GLIBTOP_CPU_FREQUENCY = 5
GLIBTOP_CPU_IDLE = 4
GLIBTOP_CPU_IOWAIT = 12
GLIBTOP_CPU_IRQ = 13
GLIBTOP_CPU_NICE = 2
GLIBTOP_CPU_SOFTIRQ = 14
GLIBTOP_CPU_SYS = 3
GLIBTOP_CPU_TOTAL = 0
GLIBTOP_CPU_USER = 1

GLIBTOP_ERROR_METHOD_ABORT = 3
GLIBTOP_ERROR_METHOD_IGNORE = 0
GLIBTOP_ERROR_METHOD_WARN = 2

GLIBTOP_ERROR_METHOD_WARN_ONCE = 1

GLIBTOP_EXCLUDE_IDLE = 4096
GLIBTOP_EXCLUDE_NOTTY = 16384
GLIBTOP_EXCLUDE_SYSTEM = 8192

GLIBTOP_FEATURES_EXCEPT = 8

GLIBTOP_FEATURES_NO_SERVER = 4

GLIBTOP_FILE_ENTRY_FD = 0

GLIBTOP_FILE_ENTRY_INETSOCKET_DST_HOST = 3
GLIBTOP_FILE_ENTRY_INETSOCKET_DST_PORT = 4

GLIBTOP_FILE_ENTRY_NAME = 1
GLIBTOP_FILE_ENTRY_TYPE = 2

GLIBTOP_FSUSAGE_BAVAIL = 2
GLIBTOP_FSUSAGE_BFREE = 1
GLIBTOP_FSUSAGE_BLOCKS = 0

GLIBTOP_FSUSAGE_BLOCK_SIZE = 5

GLIBTOP_FSUSAGE_FFREE = 4
GLIBTOP_FSUSAGE_FILES = 3
GLIBTOP_FSUSAGE_READ = 6
GLIBTOP_FSUSAGE_WRITE = 7

GLIBTOP_INIT_NO_INIT = 2
GLIBTOP_INIT_NO_OPEN = 1

GLIBTOP_IPC_MSGMAP = 1
GLIBTOP_IPC_MSGMAX = 2
GLIBTOP_IPC_MSGMNB = 3
GLIBTOP_IPC_MSGMNI = 4
GLIBTOP_IPC_MSGPOOL = 0
GLIBTOP_IPC_MSGSSZ = 5
GLIBTOP_IPC_MSGTQL = 6
GLIBTOP_IPC_SEMAEM = 9
GLIBTOP_IPC_SEMMAP = 0
GLIBTOP_IPC_SEMMNI = 1
GLIBTOP_IPC_SEMMNS = 2
GLIBTOP_IPC_SEMMNU = 3
GLIBTOP_IPC_SEMMSL = 4
GLIBTOP_IPC_SEMOPM = 5
GLIBTOP_IPC_SEMUME = 6
GLIBTOP_IPC_SEMUSZ = 7
GLIBTOP_IPC_SEMVMX = 8
GLIBTOP_IPC_SHMALL = 4
GLIBTOP_IPC_SHMMAX = 0
GLIBTOP_IPC_SHMMIN = 1
GLIBTOP_IPC_SHMMNI = 2
GLIBTOP_IPC_SHMSEG = 3

GLIBTOP_KERN_PROC_ALL = 0
GLIBTOP_KERN_PROC_MASK = 15
GLIBTOP_KERN_PROC_PGRP = 2
GLIBTOP_KERN_PROC_PID = 1
GLIBTOP_KERN_PROC_RUID = 6
GLIBTOP_KERN_PROC_SESSION = 3
GLIBTOP_KERN_PROC_TTY = 4
GLIBTOP_KERN_PROC_UID = 5

GLIBTOP_LOADAVG_LAST_PID = 3

GLIBTOP_LOADAVG_LOADAVG = 0

GLIBTOP_LOADAVG_NR_RUNNING = 1
GLIBTOP_LOADAVG_NR_TASKS = 2

GLIBTOP_MAP_ENTRY_DEVICE = 5
GLIBTOP_MAP_ENTRY_END = 1
GLIBTOP_MAP_ENTRY_FILENAME = 6
GLIBTOP_MAP_ENTRY_INODE = 4
GLIBTOP_MAP_ENTRY_OFFSET = 2
GLIBTOP_MAP_ENTRY_PERM = 3

GLIBTOP_MAP_ENTRY_PRIVATE_CLEAN = 11
GLIBTOP_MAP_ENTRY_PRIVATE_DIRTY = 12

GLIBTOP_MAP_ENTRY_PSS = 13
GLIBTOP_MAP_ENTRY_RSS = 8

GLIBTOP_MAP_ENTRY_SHARED_CLEAN = 9
GLIBTOP_MAP_ENTRY_SHARED_DIRTY = 10

GLIBTOP_MAP_ENTRY_SIZE = 7
GLIBTOP_MAP_ENTRY_START = 0
GLIBTOP_MAP_ENTRY_SWAP = 14

GLIBTOP_MAP_FILENAME_LEN = 215

GLIBTOP_MAP_PERM_EXECUTE = 4
GLIBTOP_MAP_PERM_PRIVATE = 16
GLIBTOP_MAP_PERM_READ = 1
GLIBTOP_MAP_PERM_SHARED = 8
GLIBTOP_MAP_PERM_WRITE = 2

GLIBTOP_MAX_CMND = 29
GLIBTOP_MAX_CPU = 18
GLIBTOP_MAX_FSUSAGE = 8
GLIBTOP_MAX_GROUPS = 64
GLIBTOP_MAX_LOADAVG = 4

GLIBTOP_MAX_MAP_ENTRY = 15

GLIBTOP_MAX_MEM = 8
GLIBTOP_MAX_MOUNTLIST = 3

GLIBTOP_MAX_MSG_LIMITS = 7

GLIBTOP_MAX_NETLIST = 1
GLIBTOP_MAX_NETLOAD = 18

GLIBTOP_MAX_OPEN_FILE_ENTRY = 5

GLIBTOP_MAX_PPP = 3
GLIBTOP_MAX_PROCLIST = 3

GLIBTOP_MAX_PROC_AFFINITY = 2
GLIBTOP_MAX_PROC_ARGS = 1
GLIBTOP_MAX_PROC_IO = 3
GLIBTOP_MAX_PROC_KERNEL = 9
GLIBTOP_MAX_PROC_MAP = 3
GLIBTOP_MAX_PROC_MEM = 6

GLIBTOP_MAX_PROC_OPEN_FILES = 3

GLIBTOP_MAX_PROC_SEGMENT = 8
GLIBTOP_MAX_PROC_SIGNAL = 4
GLIBTOP_MAX_PROC_STATE = 9
GLIBTOP_MAX_PROC_TIME = 11
GLIBTOP_MAX_PROC_UID = 18
GLIBTOP_MAX_PROC_WD = 3

GLIBTOP_MAX_SEM_LIMITS = 10

GLIBTOP_MAX_SHM_LIMITS = 5

GLIBTOP_MAX_SWAP = 5
GLIBTOP_MAX_SYSDEPS = 28
GLIBTOP_MAX_SYSINFO = 2
GLIBTOP_MAX_UPTIME = 3

GLIBTOP_MEM_BUFFER = 4
GLIBTOP_MEM_CACHED = 5
GLIBTOP_MEM_FREE = 2
GLIBTOP_MEM_LOCKED = 7
GLIBTOP_MEM_SHARED = 3
GLIBTOP_MEM_TOTAL = 0
GLIBTOP_MEM_USED = 1
GLIBTOP_MEM_USER = 6

GLIBTOP_METHOD_DIRECT = 1
GLIBTOP_METHOD_INET = 3
GLIBTOP_METHOD_PIPE = 2
GLIBTOP_METHOD_UNIX = 4

GLIBTOP_MOUNTENTRY_LEN = 79

GLIBTOP_MOUNTLIST_NUMBER = 0
GLIBTOP_MOUNTLIST_SIZE = 2
GLIBTOP_MOUNTLIST_TOTAL = 1

GLIBTOP_NCPU = 1024

GLIBTOP_NETLIST_NUMBER = 0

GLIBTOP_NETLOAD_ADDRESS = 3
GLIBTOP_NETLOAD_ADDRESS6 = 14

GLIBTOP_NETLOAD_BYTES_IN = 7
GLIBTOP_NETLOAD_BYTES_OUT = 8
GLIBTOP_NETLOAD_BYTES_TOTAL = 9

GLIBTOP_NETLOAD_COLLISIONS = 13

GLIBTOP_NETLOAD_ERRORS_IN = 10
GLIBTOP_NETLOAD_ERRORS_OUT = 11
GLIBTOP_NETLOAD_ERRORS_TOTAL = 12

GLIBTOP_NETLOAD_HWADDRESS = 17

GLIBTOP_NETLOAD_IF_FLAGS = 0

GLIBTOP_NETLOAD_MTU = 1

GLIBTOP_NETLOAD_PACKETS_IN = 4
GLIBTOP_NETLOAD_PACKETS_OUT = 5
GLIBTOP_NETLOAD_PACKETS_TOTAL = 6

GLIBTOP_NETLOAD_PREFIX6 = 15
GLIBTOP_NETLOAD_SCOPE6 = 16
GLIBTOP_NETLOAD_SUBNET = 2

GLIBTOP_OPEN_DEST_HOST_LEN = 46

GLIBTOP_OPEN_FILENAME_LEN = 215

GLIBTOP_PARAM_COMMAND = 3

GLIBTOP_PARAM_ERROR_METHOD = 6

GLIBTOP_PARAM_FEATURES = 2
GLIBTOP_PARAM_HOST = 4
GLIBTOP_PARAM_METHOD = 1
GLIBTOP_PARAM_PORT = 5
GLIBTOP_PARAM_REQUIRED = 7

GLIBTOP_PPP_BYTES_IN = 1
GLIBTOP_PPP_BYTES_OUT = 2

GLIBTOP_PPP_STATE = 0

GLIBTOP_PROCESS_DEAD = 64
GLIBTOP_PROCESS_INTERRUPTIBLE = 2
GLIBTOP_PROCESS_RUNNING = 1
GLIBTOP_PROCESS_STOPPED = 16
GLIBTOP_PROCESS_SWAPPING = 32
GLIBTOP_PROCESS_UNINTERRUPTIBLE = 4
GLIBTOP_PROCESS_ZOMBIE = 8

GLIBTOP_PROCLIST_NUMBER = 0
GLIBTOP_PROCLIST_SIZE = 2
GLIBTOP_PROCLIST_TOTAL = 1

GLIBTOP_PROC_AFFINITY_ALL = 1
GLIBTOP_PROC_AFFINITY_NUMBER = 0

GLIBTOP_PROC_ARGS_SIZE = 0

GLIBTOP_PROC_IO_DISK_RBYTES = 2
GLIBTOP_PROC_IO_DISK_RCHAR = 0
GLIBTOP_PROC_IO_DISK_WBYTES = 3
GLIBTOP_PROC_IO_DISK_WCHAR = 1

GLIBTOP_PROC_KERNEL_CMAJ_FLT = 4

GLIBTOP_PROC_KERNEL_CMIN_FLT = 3

GLIBTOP_PROC_KERNEL_KSTK_EIP = 6
GLIBTOP_PROC_KERNEL_KSTK_ESP = 5

GLIBTOP_PROC_KERNEL_K_FLAGS = 0

GLIBTOP_PROC_KERNEL_MAJ_FLT = 2

GLIBTOP_PROC_KERNEL_MIN_FLT = 1

GLIBTOP_PROC_KERNEL_NWCHAN = 7
GLIBTOP_PROC_KERNEL_WCHAN = 8

GLIBTOP_PROC_MAP_NUMBER = 0
GLIBTOP_PROC_MAP_SIZE = 2
GLIBTOP_PROC_MAP_TOTAL = 1

GLIBTOP_PROC_MEM_RESIDENT = 2
GLIBTOP_PROC_MEM_RSS = 4

GLIBTOP_PROC_MEM_RSS_RLIM = 5

GLIBTOP_PROC_MEM_SHARE = 3
GLIBTOP_PROC_MEM_SIZE = 0
GLIBTOP_PROC_MEM_VSIZE = 1

GLIBTOP_PROC_OPEN_FILES_NUMBER = 0
GLIBTOP_PROC_OPEN_FILES_SIZE = 2
GLIBTOP_PROC_OPEN_FILES_TOTAL = 1

GLIBTOP_PROC_SEGMENT_DATA_RSS = 2

GLIBTOP_PROC_SEGMENT_DIRTY_SIZE = 4

GLIBTOP_PROC_SEGMENT_END_CODE = 6

GLIBTOP_PROC_SEGMENT_SHLIB_RSS = 1

GLIBTOP_PROC_SEGMENT_STACK_RSS = 3

GLIBTOP_PROC_SEGMENT_START_CODE = 5
GLIBTOP_PROC_SEGMENT_START_STACK = 7

GLIBTOP_PROC_SEGMENT_TEXT_RSS = 0

GLIBTOP_PROC_SIGNAL_BLOCKED = 1
GLIBTOP_PROC_SIGNAL_SIGCATCH = 3
GLIBTOP_PROC_SIGNAL_SIGIGNORE = 2
GLIBTOP_PROC_SIGNAL_SIGNAL = 0

GLIBTOP_PROC_STATE_CMD = 0
GLIBTOP_PROC_STATE_GID = 3

GLIBTOP_PROC_STATE_HAS_CPU = 6

GLIBTOP_PROC_STATE_LAST_PROCESSOR = 8

GLIBTOP_PROC_STATE_PROCESSOR = 7
GLIBTOP_PROC_STATE_RGID = 5
GLIBTOP_PROC_STATE_RUID = 4
GLIBTOP_PROC_STATE_STATE = 1
GLIBTOP_PROC_STATE_UID = 2

GLIBTOP_PROC_TIME_CSTIME = 5
GLIBTOP_PROC_TIME_CUTIME = 4
GLIBTOP_PROC_TIME_FREQUENCY = 8

GLIBTOP_PROC_TIME_IT_REAL_VALUE = 7

GLIBTOP_PROC_TIME_RTIME = 1

GLIBTOP_PROC_TIME_START_TIME = 0

GLIBTOP_PROC_TIME_STIME = 3
GLIBTOP_PROC_TIME_TIMEOUT = 6
GLIBTOP_PROC_TIME_UTIME = 2

GLIBTOP_PROC_TIME_XCPU_STIME = 10
GLIBTOP_PROC_TIME_XCPU_UTIME = 9

GLIBTOP_PROC_UID_EGID = 3
GLIBTOP_PROC_UID_EUID = 1
GLIBTOP_PROC_UID_FSGID = 7
GLIBTOP_PROC_UID_FSUID = 6
GLIBTOP_PROC_UID_GID = 2
GLIBTOP_PROC_UID_GROUPS = 17
GLIBTOP_PROC_UID_NGROUPS = 16
GLIBTOP_PROC_UID_NICE = 15
GLIBTOP_PROC_UID_PGRP = 10
GLIBTOP_PROC_UID_PID = 8
GLIBTOP_PROC_UID_PPID = 9
GLIBTOP_PROC_UID_PRIORITY = 14
GLIBTOP_PROC_UID_SESSION = 11
GLIBTOP_PROC_UID_SGID = 5
GLIBTOP_PROC_UID_SUID = 4
GLIBTOP_PROC_UID_TPGID = 13
GLIBTOP_PROC_UID_TTY = 12
GLIBTOP_PROC_UID_UID = 0

GLIBTOP_PROC_WD_EXE = 2

GLIBTOP_PROC_WD_EXE_LEN = 215

GLIBTOP_PROC_WD_NUMBER = 0
GLIBTOP_PROC_WD_ROOT = 1

GLIBTOP_PROC_WD_ROOT_LEN = 215

GLIBTOP_SWAP_FREE = 2
GLIBTOP_SWAP_PAGEIN = 3
GLIBTOP_SWAP_PAGEOUT = 4
GLIBTOP_SWAP_TOTAL = 0
GLIBTOP_SWAP_USED = 1

GLIBTOP_SYSDEPS_ALL = 0
GLIBTOP_SYSDEPS_CPU = 1
GLIBTOP_SYSDEPS_FEATURES = 0
GLIBTOP_SYSDEPS_FSUSAGE = 20
GLIBTOP_SYSDEPS_LOADAVG = 5
GLIBTOP_SYSDEPS_MEM = 2
GLIBTOP_SYSDEPS_MOUNTLIST = 19

GLIBTOP_SYSDEPS_MSG_LIMITS = 7

GLIBTOP_SYSDEPS_NETLIST = 23
GLIBTOP_SYSDEPS_NETLOAD = 21
GLIBTOP_SYSDEPS_PPP = 22
GLIBTOP_SYSDEPS_PROCLIST = 9

GLIBTOP_SYSDEPS_PROC_AFFINITY = 26
GLIBTOP_SYSDEPS_PROC_ARGS = 17
GLIBTOP_SYSDEPS_PROC_IO = 27
GLIBTOP_SYSDEPS_PROC_KERNEL = 15
GLIBTOP_SYSDEPS_PROC_MAP = 18
GLIBTOP_SYSDEPS_PROC_MEM = 12

GLIBTOP_SYSDEPS_PROC_OPEN_FILES = 24

GLIBTOP_SYSDEPS_PROC_SEGMENT = 16
GLIBTOP_SYSDEPS_PROC_SIGNAL = 14
GLIBTOP_SYSDEPS_PROC_STATE = 10
GLIBTOP_SYSDEPS_PROC_TIME = 13
GLIBTOP_SYSDEPS_PROC_UID = 11
GLIBTOP_SYSDEPS_PROC_WD = 25

GLIBTOP_SYSDEPS_SEM_LIMITS = 8

GLIBTOP_SYSDEPS_SHM_LIMITS = 6

GLIBTOP_SYSDEPS_SWAP = 3
GLIBTOP_SYSDEPS_UPTIME = 4

GLIBTOP_SYSINFO_CPUINFO = 1
GLIBTOP_SYSINFO_NCPU = 0

GLIBTOP_UPTIME_BOOT_TIME = 2

GLIBTOP_UPTIME_IDLETIME = 1
GLIBTOP_UPTIME_UPTIME = 0

GLIBTOP_XCPU_FLAGS = 11
GLIBTOP_XCPU_IDLE = 10
GLIBTOP_XCPU_IOWAIT = 15
GLIBTOP_XCPU_IRQ = 16
GLIBTOP_XCPU_NICE = 8
GLIBTOP_XCPU_SOFTIRQ = 17
GLIBTOP_XCPU_SYS = 9
GLIBTOP_XCPU_TOTAL = 6
GLIBTOP_XCPU_USER = 7

HOSTNAMSZ = 255

LIBGTOP_MAJOR_VERSION = 2

LIBGTOP_MICRO_VERSION = 0

LIBGTOP_MINOR_VERSION = 40

MCOOKIE_NAME = 'MAGIC-1'
MCOOKIE_SCREEN = '42980'

MCOOKIE_X_NAME = 'MIT-MAGIC-COOKIE-1'

PATCHLEVEL = 2

REPLYSIZ = 300

TABLE_SIZE = 101

TRUE = 1

_namespace = 'GTop'

_version = '2.0'

__weakref__ = None

# functions

def glibtop_close(): # real signature unknown; restored from __doc__
    """ glibtop_close() """
    pass

def glibtop_get_cpu(buf): # real signature unknown; restored from __doc__
    """ glibtop_get_cpu(buf:GTop.glibtop_cpu) """
    pass

def glibtop_get_fsusage(buf, mount_dir): # real signature unknown; restored from __doc__
    """ glibtop_get_fsusage(buf:GTop.glibtop_fsusage, mount_dir:str) """
    pass

def glibtop_get_loadavg(buf): # real signature unknown; restored from __doc__
    """ glibtop_get_loadavg(buf:GTop.glibtop_loadavg) """
    pass

def glibtop_get_mem(buf): # real signature unknown; restored from __doc__
    """ glibtop_get_mem(buf:GTop.glibtop_mem) """
    pass

def glibtop_get_mountlist(buf, all_fs): # real signature unknown; restored from __doc__
    """ glibtop_get_mountlist(buf:GTop.glibtop_mountlist, all_fs:int) -> list """
    return []

def glibtop_get_msg_limits(buf): # real signature unknown; restored from __doc__
    """ glibtop_get_msg_limits(buf:GTop.glibtop_msg_limits) """
    pass

def glibtop_get_netlist(buf): # real signature unknown; restored from __doc__
    """ glibtop_get_netlist(buf:GTop.glibtop_netlist) -> list """
    return []

def glibtop_get_netload(buf, interface): # real signature unknown; restored from __doc__
    """ glibtop_get_netload(buf:GTop.glibtop_netload, interface:str) """
    pass

def glibtop_get_ppp(buf, device): # real signature unknown; restored from __doc__
    """ glibtop_get_ppp(buf:GTop.glibtop_ppp, device:int) """
    pass

def glibtop_get_proclist(buf, which, arg): # real signature unknown; restored from __doc__
    """ glibtop_get_proclist(buf:GTop.glibtop_proclist, which:int, arg:int) -> list """
    return []

def glibtop_get_proc_affinity(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_affinity(buf:GTop.glibtop_proc_affinity, pid:int) -> int """
    return 0

def glibtop_get_proc_args(buf, pid, max_len): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_args(buf:GTop.glibtop_proc_args, pid:int, max_len:int) -> str """
    return ""

def glibtop_get_proc_argv(buf, pid, max_len): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_argv(buf:GTop.glibtop_proc_args, pid:int, max_len:int) -> list """
    return []

def glibtop_get_proc_io(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_io(buf:GTop.glibtop_proc_io, pid:int) """
    pass

def glibtop_get_proc_kernel(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_kernel(buf:GTop.glibtop_proc_kernel, pid:int) """
    pass

def glibtop_get_proc_map(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_map(buf:GTop.glibtop_proc_map, pid:int) -> list """
    return []

def glibtop_get_proc_mem(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_mem(buf:GTop.glibtop_proc_mem, pid:int) """
    pass

def glibtop_get_proc_open_files(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_open_files(buf:GTop.glibtop_proc_open_files, pid:int) -> list """
    return []

def glibtop_get_proc_segment(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_segment(buf:GTop.glibtop_proc_segment, pid:int) """
    pass

def glibtop_get_proc_signal(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_signal(buf:GTop.glibtop_proc_signal, pid:int) """
    pass

def glibtop_get_proc_state(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_state(buf:GTop.glibtop_proc_state, pid:int) """
    pass

def glibtop_get_proc_time(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_time(buf:GTop.glibtop_proc_time, pid:int) """
    pass

def glibtop_get_proc_uid(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_uid(buf:GTop.glibtop_proc_uid, pid:int) """
    pass

def glibtop_get_proc_wd(buf, pid): # real signature unknown; restored from __doc__
    """ glibtop_get_proc_wd(buf:GTop.glibtop_proc_wd, pid:int) -> list """
    return []

def glibtop_get_sem_limits(buf): # real signature unknown; restored from __doc__
    """ glibtop_get_sem_limits(buf:GTop.glibtop_sem_limits) """
    pass

def glibtop_get_shm_limits(buf): # real signature unknown; restored from __doc__
    """ glibtop_get_shm_limits(buf:GTop.glibtop_shm_limits) """
    pass

def glibtop_get_swap(buf): # real signature unknown; restored from __doc__
    """ glibtop_get_swap(buf:GTop.glibtop_swap) """
    pass

def glibtop_get_sysdeps(buf): # real signature unknown; restored from __doc__
    """ glibtop_get_sysdeps(buf:GTop.glibtop_sysdeps) """
    pass

def glibtop_get_sysinfo(): # real signature unknown; restored from __doc__
    """ glibtop_get_sysinfo() -> GTop.glibtop_sysinfo """
    pass

def glibtop_get_uptime(buf): # real signature unknown; restored from __doc__
    """ glibtop_get_uptime(buf:GTop.glibtop_uptime) """
    pass

def glibtop_init(): # real signature unknown; restored from __doc__
    """ glibtop_init() -> GTop.glibtop """
    pass

def glibtop_init_r(features, flags): # real signature unknown; restored from __doc__
    """ glibtop_init_r(features:int, flags:int) -> GTop.glibtop, server_ptr:GTop.glibtop """
    pass

def glibtop_init_s(features, flags): # real signature unknown; restored from __doc__
    """ glibtop_init_s(features:int, flags:int) -> GTop.glibtop, server_ptr:GTop.glibtop """
    pass

def glibtop_internet_addr(host): # real signature unknown; restored from __doc__
    """ glibtop_internet_addr(host:str) -> int """
    return 0

def glibtop_make_connection(hostarg, portarg, s): # real signature unknown; restored from __doc__
    """ glibtop_make_connection(hostarg:str, portarg:int, s:int) -> int """
    return 0

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .glibtop import glibtop
from .glibtop_command import glibtop_command
from .glibtop_cpu import glibtop_cpu
from .glibtop_entry import glibtop_entry
from .glibtop_fsusage import glibtop_fsusage
from .glibtop_loadavg import glibtop_loadavg
from .glibtop_machine import glibtop_machine
from .glibtop_map_entry import glibtop_map_entry
from .glibtop_mem import glibtop_mem
from .glibtop_mountentry import glibtop_mountentry
from .glibtop_mountlist import glibtop_mountlist
from .glibtop_msg_limits import glibtop_msg_limits
from .glibtop_netlist import glibtop_netlist
from .glibtop_netload import glibtop_netload
from .glibtop_open_files_entry import glibtop_open_files_entry
from .glibtop_ppp import glibtop_ppp
from .glibtop_proclist import glibtop_proclist
from .glibtop_proc_affinity import glibtop_proc_affinity
from .glibtop_proc_args import glibtop_proc_args
from .glibtop_proc_io import glibtop_proc_io
from .glibtop_proc_kernel import glibtop_proc_kernel
from .glibtop_proc_map import glibtop_proc_map
from .glibtop_proc_mem import glibtop_proc_mem
from .glibtop_proc_open_files import glibtop_proc_open_files
from .glibtop_proc_segment import glibtop_proc_segment
from .glibtop_proc_signal import glibtop_proc_signal
from .glibtop_proc_state import glibtop_proc_state
from .glibtop_proc_time import glibtop_proc_time
from .glibtop_proc_uid import glibtop_proc_uid
from .glibtop_proc_wd import glibtop_proc_wd
from .glibtop_response import glibtop_response
from .glibtop_response_union import glibtop_response_union
from .glibtop_sem_limits import glibtop_sem_limits
from .glibtop_shm_limits import glibtop_shm_limits
from .glibtop_signame import glibtop_signame
from .glibtop_swap import glibtop_swap
from .glibtop_sysdeps import glibtop_sysdeps
from .glibtop_sysinfo import glibtop_sysinfo
from .glibtop_union import glibtop_union
from .glibtop_uptime import glibtop_uptime
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f97019e5d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GTop-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GTop', loader=<gi.importer.DynamicImporter object at 0x7f97019e5d00>)"

