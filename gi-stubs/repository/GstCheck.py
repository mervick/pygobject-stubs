# encoding: utf-8
# module gi.repository.GstCheck
# from /usr/lib64/girepository-1.0/GstCheck-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst


# Variables with simple values

_namespace = 'GstCheck'

_version = '1.0'

__weakref__ = None

# functions

def buffer_straw_get_buffer(bin, pad): # real signature unknown; restored from __doc__
    """ buffer_straw_get_buffer(bin:Gst.Element, pad:Gst.Pad) -> Gst.Buffer """
    pass

def buffer_straw_start_pipeline(bin, pad): # real signature unknown; restored from __doc__
    """ buffer_straw_start_pipeline(bin:Gst.Element, pad:Gst.Pad) """
    pass

def buffer_straw_stop_pipeline(bin, pad): # real signature unknown; restored from __doc__
    """ buffer_straw_stop_pipeline(bin:Gst.Element, pad:Gst.Pad) """
    pass

def check_abi_list(p_list, have_abi_sizes): # real signature unknown; restored from __doc__
    """ check_abi_list(list:GstCheck.CheckABIStruct, have_abi_sizes:bool) """
    pass

def check_buffer_data(buffer, data=None, size): # real signature unknown; restored from __doc__
    """ check_buffer_data(buffer:Gst.Buffer, data=None, size:int) """
    pass

def check_caps_equal(caps1, caps2): # real signature unknown; restored from __doc__
    """ check_caps_equal(caps1:Gst.Caps, caps2:Gst.Caps) """
    pass

def check_chain_func(pad, parent, buffer): # real signature unknown; restored from __doc__
    """ check_chain_func(pad:Gst.Pad, parent:Gst.Object, buffer:Gst.Buffer) -> Gst.FlowReturn """
    pass

def check_clear_log_filter(): # real signature unknown; restored from __doc__
    """ check_clear_log_filter() """
    pass

def check_drop_buffers(): # real signature unknown; restored from __doc__
    """ check_drop_buffers() """
    pass

def check_element_push_buffer(element_name, buffer_in, caps_in, buffer_out, caps_out): # real signature unknown; restored from __doc__
    """ check_element_push_buffer(element_name:str, buffer_in:Gst.Buffer, caps_in:Gst.Caps, buffer_out:Gst.Buffer, caps_out:Gst.Caps) """
    pass

def check_element_push_buffer_list(element_name, buffer_in, caps_in, buffer_out, caps_out, last_flow_return): # real signature unknown; restored from __doc__
    """ check_element_push_buffer_list(element_name:str, buffer_in:list, caps_in:Gst.Caps, buffer_out:list, caps_out:Gst.Caps, last_flow_return:Gst.FlowReturn) """
    pass

def check_init(argc, argv): # real signature unknown; restored from __doc__
    """ check_init(argc:int, argv:str) """
    pass

def check_message_error(message, type, domain, code): # real signature unknown; restored from __doc__
    """ check_message_error(message:Gst.Message, type:Gst.MessageType, domain:int, code:int) """
    pass

def check_object_destroyed_on_unref(object_to_unref=None): # real signature unknown; restored from __doc__
    """ check_object_destroyed_on_unref(object_to_unref=None) """
    pass

def check_remove_log_filter(filter): # real signature unknown; restored from __doc__
    """ check_remove_log_filter(filter:GstCheck.CheckLogFilter) """
    pass

def check_setup_element(factory): # real signature unknown; restored from __doc__
    """ check_setup_element(factory:str) -> Gst.Element """
    pass

def check_setup_events(srcpad, element, caps=None, format): # real signature unknown; restored from __doc__
    """ check_setup_events(srcpad:Gst.Pad, element:Gst.Element, caps:Gst.Caps=None, format:Gst.Format) """
    pass

def check_setup_events_with_stream_id(srcpad, element, caps=None, format, stream_id): # real signature unknown; restored from __doc__
    """ check_setup_events_with_stream_id(srcpad:Gst.Pad, element:Gst.Element, caps:Gst.Caps=None, format:Gst.Format, stream_id:str) """
    pass

def check_setup_sink_pad(element, tmpl): # real signature unknown; restored from __doc__
    """ check_setup_sink_pad(element:Gst.Element, tmpl:Gst.StaticPadTemplate) -> Gst.Pad """
    pass

def check_setup_sink_pad_by_name(element, tmpl, name): # real signature unknown; restored from __doc__
    """ check_setup_sink_pad_by_name(element:Gst.Element, tmpl:Gst.StaticPadTemplate, name:str) -> Gst.Pad """
    pass

def check_setup_sink_pad_by_name_from_template(element, tmpl, name): # real signature unknown; restored from __doc__
    """ check_setup_sink_pad_by_name_from_template(element:Gst.Element, tmpl:Gst.PadTemplate, name:str) -> Gst.Pad """
    pass

def check_setup_sink_pad_from_template(element, tmpl): # real signature unknown; restored from __doc__
    """ check_setup_sink_pad_from_template(element:Gst.Element, tmpl:Gst.PadTemplate) -> Gst.Pad """
    pass

def check_setup_src_pad(element, tmpl): # real signature unknown; restored from __doc__
    """ check_setup_src_pad(element:Gst.Element, tmpl:Gst.StaticPadTemplate) -> Gst.Pad """
    pass

def check_setup_src_pad_by_name(element, tmpl, name): # real signature unknown; restored from __doc__
    """ check_setup_src_pad_by_name(element:Gst.Element, tmpl:Gst.StaticPadTemplate, name:str) -> Gst.Pad """
    pass

def check_setup_src_pad_by_name_from_template(element, tmpl, name): # real signature unknown; restored from __doc__
    """ check_setup_src_pad_by_name_from_template(element:Gst.Element, tmpl:Gst.PadTemplate, name:str) -> Gst.Pad """
    pass

def check_setup_src_pad_from_template(element, tmpl): # real signature unknown; restored from __doc__
    """ check_setup_src_pad_from_template(element:Gst.Element, tmpl:Gst.PadTemplate) -> Gst.Pad """
    pass

def check_teardown_element(element): # real signature unknown; restored from __doc__
    """ check_teardown_element(element:Gst.Element) """
    pass

def check_teardown_pad_by_name(element, name): # real signature unknown; restored from __doc__
    """ check_teardown_pad_by_name(element:Gst.Element, name:str) """
    pass

def check_teardown_sink_pad(element): # real signature unknown; restored from __doc__
    """ check_teardown_sink_pad(element:Gst.Element) """
    pass

def check_teardown_src_pad(element): # real signature unknown; restored from __doc__
    """ check_teardown_src_pad(element:Gst.Element) """
    pass

def consistency_checker_add_pad(consist, pad): # real signature unknown; restored from __doc__
    """ consistency_checker_add_pad(consist:GstCheck.StreamConsistency, pad:Gst.Pad) -> bool """
    return False

def consistency_checker_free(consist): # real signature unknown; restored from __doc__
    """ consistency_checker_free(consist:GstCheck.StreamConsistency) """
    pass

def consistency_checker_reset(consist): # real signature unknown; restored from __doc__
    """ consistency_checker_reset(consist:GstCheck.StreamConsistency) """
    pass

def harness_stress_thread_stop(t): # real signature unknown; restored from __doc__
    """ harness_stress_thread_stop(t:GstCheck.HarnessThread) -> int """
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

class CheckABIStruct(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        CheckABIStruct()
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

    abi_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CheckABIStruct), '__module__': 'gi.repository.GstCheck', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'CheckABIStruct' objects>, '__weakref__': <attribute '__weakref__' of 'CheckABIStruct' objects>, '__doc__': None, 'name': <property object at 0x7f1803bef8b0>, 'size': <property object at 0x7f1803bef5e0>, 'abi_size': <property object at 0x7f1803bef810>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(CheckABIStruct)


class CheckLogFilter(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CheckLogFilter), '__module__': 'gi.repository.GstCheck', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'CheckLogFilter' objects>, '__weakref__': <attribute '__weakref__' of 'CheckLogFilter' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(CheckLogFilter)


class Harness(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Harness()
    """
    def add_element_sink_pad(self, sinkpad): # real signature unknown; restored from __doc__
        """ add_element_sink_pad(self, sinkpad:Gst.Pad) """
        pass

    def add_element_src_pad(self, srcpad): # real signature unknown; restored from __doc__
        """ add_element_src_pad(self, srcpad:Gst.Pad) """
        pass

    def add_probe(self, element_name, pad_name, mask, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_probe(self, element_name:str, pad_name:str, mask:Gst.PadProbeType, callback:Gst.PadProbeCallback, user_data=None) """
        pass

    def add_propose_allocation_meta(self, api, params=None): # real signature unknown; restored from __doc__
        """ add_propose_allocation_meta(self, api:GType, params:Gst.Structure=None) """
        pass

    def add_sink(self, sink_element_name): # real signature unknown; restored from __doc__
        """ add_sink(self, sink_element_name:str) """
        pass

    def add_sink_harness(self, sink_harness): # real signature unknown; restored from __doc__
        """ add_sink_harness(self, sink_harness:GstCheck.Harness) """
        pass

    def add_sink_parse(self, launchline): # real signature unknown; restored from __doc__
        """ add_sink_parse(self, launchline:str) """
        pass

    def add_src(self, src_element_name, has_clock_wait): # real signature unknown; restored from __doc__
        """ add_src(self, src_element_name:str, has_clock_wait:bool) """
        pass

    def add_src_harness(self, src_harness, has_clock_wait): # real signature unknown; restored from __doc__
        """ add_src_harness(self, src_harness:GstCheck.Harness, has_clock_wait:bool) """
        pass

    def add_src_parse(self, launchline, has_clock_wait): # real signature unknown; restored from __doc__
        """ add_src_parse(self, launchline:str, has_clock_wait:bool) """
        pass

    def buffers_in_queue(self): # real signature unknown; restored from __doc__
        """ buffers_in_queue(self) -> int """
        return 0

    def buffers_received(self): # real signature unknown; restored from __doc__
        """ buffers_received(self) -> int """
        return 0

    def crank_multiple_clock_waits(self, waits): # real signature unknown; restored from __doc__
        """ crank_multiple_clock_waits(self, waits:int) -> bool """
        return False

    def crank_single_clock_wait(self): # real signature unknown; restored from __doc__
        """ crank_single_clock_wait(self) -> bool """
        return False

    def create_buffer(self, size): # real signature unknown; restored from __doc__
        """ create_buffer(self, size:int) -> Gst.Buffer """
        pass

    def dump_to_file(self, filename): # real signature unknown; restored from __doc__
        """ dump_to_file(self, filename:str) """
        pass

    def events_in_queue(self): # real signature unknown; restored from __doc__
        """ events_in_queue(self) -> int """
        return 0

    def events_received(self): # real signature unknown; restored from __doc__
        """ events_received(self) -> int """
        return 0

    def find_element(self, element_name): # real signature unknown; restored from __doc__
        """ find_element(self, element_name:str) -> Gst.Element or None """
        pass

    def get_allocator(self): # real signature unknown; restored from __doc__
        """ get_allocator(self) -> allocator:Gst.Allocator, params:Gst.AllocationParams """
        pass

    def get_last_pushed_timestamp(self): # real signature unknown; restored from __doc__
        """ get_last_pushed_timestamp(self) -> int """
        return 0

    def get_testclock(self): # real signature unknown; restored from __doc__
        """ get_testclock(self) -> GstCheck.TestClock """
        pass

    def play(self): # real signature unknown; restored from __doc__
        """ play(self) """
        pass

    def pull(self): # real signature unknown; restored from __doc__
        """ pull(self) -> Gst.Buffer """
        pass

    def pull_event(self): # real signature unknown; restored from __doc__
        """ pull_event(self) -> Gst.Event """
        pass

    def pull_upstream_event(self): # real signature unknown; restored from __doc__
        """ pull_upstream_event(self) -> Gst.Event """
        pass

    def push(self, buffer): # real signature unknown; restored from __doc__
        """ push(self, buffer:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def push_and_pull(self, buffer): # real signature unknown; restored from __doc__
        """ push_and_pull(self, buffer:Gst.Buffer) -> Gst.Buffer """
        pass

    def push_event(self, event): # real signature unknown; restored from __doc__
        """ push_event(self, event:Gst.Event) -> bool """
        return False

    def push_from_src(self): # real signature unknown; restored from __doc__
        """ push_from_src(self) -> Gst.FlowReturn """
        pass

    def push_to_sink(self): # real signature unknown; restored from __doc__
        """ push_to_sink(self) -> Gst.FlowReturn """
        pass

    def push_upstream_event(self, event): # real signature unknown; restored from __doc__
        """ push_upstream_event(self, event:Gst.Event) -> bool """
        return False

    def query_latency(self): # real signature unknown; restored from __doc__
        """ query_latency(self) -> int """
        return 0

    def set_blocking_push_mode(self): # real signature unknown; restored from __doc__
        """ set_blocking_push_mode(self) """
        pass

    def set_caps(self, in_, out): # real signature unknown; restored from __doc__
        """ set_caps(self, in_:Gst.Caps, out:Gst.Caps) """
        pass

    def set_caps_str(self, in_, out): # real signature unknown; restored from __doc__
        """ set_caps_str(self, in_:str, out:str) """
        pass

    def set_drop_buffers(self, drop_buffers): # real signature unknown; restored from __doc__
        """ set_drop_buffers(self, drop_buffers:bool) """
        pass

    def set_forwarding(self, forwarding): # real signature unknown; restored from __doc__
        """ set_forwarding(self, forwarding:bool) """
        pass

    def set_propose_allocator(self, allocator=None, params=None): # real signature unknown; restored from __doc__
        """ set_propose_allocator(self, allocator:Gst.Allocator=None, params:Gst.AllocationParams=None) """
        pass

    def set_sink_caps(self, caps): # real signature unknown; restored from __doc__
        """ set_sink_caps(self, caps:Gst.Caps) """
        pass

    def set_sink_caps_str(self, p_str): # real signature unknown; restored from __doc__
        """ set_sink_caps_str(self, str:str) """
        pass

    def set_src_caps(self, caps): # real signature unknown; restored from __doc__
        """ set_src_caps(self, caps:Gst.Caps) """
        pass

    def set_src_caps_str(self, p_str): # real signature unknown; restored from __doc__
        """ set_src_caps_str(self, str:str) """
        pass

    def set_time(self, time): # real signature unknown; restored from __doc__
        """ set_time(self, time:int) -> bool """
        return False

    def set_upstream_latency(self, latency): # real signature unknown; restored from __doc__
        """ set_upstream_latency(self, latency:int) """
        pass

    def sink_push_many(self, pushes): # real signature unknown; restored from __doc__
        """ sink_push_many(self, pushes:int) -> Gst.FlowReturn """
        pass

    def src_crank_and_push_many(self, cranks, pushes): # real signature unknown; restored from __doc__
        """ src_crank_and_push_many(self, cranks:int, pushes:int) -> Gst.FlowReturn """
        pass

    def src_push_event(self): # real signature unknown; restored from __doc__
        """ src_push_event(self) -> bool """
        return False

    def stress_thread_stop(self, t): # real signature unknown; restored from __doc__
        """ stress_thread_stop(t:GstCheck.HarnessThread) -> int """
        return 0

    def take_all_data(self): # real signature unknown; restored from __doc__
        """ take_all_data(self) -> GLib.Bytes """
        pass

    def take_all_data_as_buffer(self): # real signature unknown; restored from __doc__
        """ take_all_data_as_buffer(self) -> Gst.Buffer """
        pass

    def teardown(self): # real signature unknown; restored from __doc__
        """ teardown(self) """
        pass

    def try_pull(self): # real signature unknown; restored from __doc__
        """ try_pull(self) -> Gst.Buffer """
        pass

    def try_pull_event(self): # real signature unknown; restored from __doc__
        """ try_pull_event(self) -> Gst.Event """
        pass

    def try_pull_upstream_event(self): # real signature unknown; restored from __doc__
        """ try_pull_upstream_event(self) -> Gst.Event """
        pass

    def upstream_events_in_queue(self): # real signature unknown; restored from __doc__
        """ upstream_events_in_queue(self) -> int """
        return 0

    def upstream_events_received(self): # real signature unknown; restored from __doc__
        """ upstream_events_received(self) -> int """
        return 0

    def use_systemclock(self): # real signature unknown; restored from __doc__
        """ use_systemclock(self) """
        pass

    def use_testclock(self): # real signature unknown; restored from __doc__
        """ use_testclock(self) """
        pass

    def wait_for_clock_id_waits(self, waits, timeout): # real signature unknown; restored from __doc__
        """ wait_for_clock_id_waits(self, waits:int, timeout:int) -> bool """
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

    element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sinkpad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sink_harness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    srcpad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_harness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Harness), '__module__': 'gi.repository.GstCheck', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Harness' objects>, '__weakref__': <attribute '__weakref__' of 'Harness' objects>, '__doc__': None, 'element': <property object at 0x7f1802855a40>, 'srcpad': <property object at 0x7f1802855b30>, 'sinkpad': <property object at 0x7f1802855c20>, 'src_harness': <property object at 0x7f1802855d10>, 'sink_harness': <property object at 0x7f1802855e00>, 'priv': <property object at 0x7f1802855ef0>, 'add_element_sink_pad': gi.FunctionInfo(add_element_sink_pad), 'add_element_src_pad': gi.FunctionInfo(add_element_src_pad), 'add_probe': gi.FunctionInfo(add_probe), 'add_propose_allocation_meta': gi.FunctionInfo(add_propose_allocation_meta), 'add_sink': gi.FunctionInfo(add_sink), 'add_sink_harness': gi.FunctionInfo(add_sink_harness), 'add_sink_parse': gi.FunctionInfo(add_sink_parse), 'add_src': gi.FunctionInfo(add_src), 'add_src_harness': gi.FunctionInfo(add_src_harness), 'add_src_parse': gi.FunctionInfo(add_src_parse), 'buffers_in_queue': gi.FunctionInfo(buffers_in_queue), 'buffers_received': gi.FunctionInfo(buffers_received), 'crank_multiple_clock_waits': gi.FunctionInfo(crank_multiple_clock_waits), 'crank_single_clock_wait': gi.FunctionInfo(crank_single_clock_wait), 'create_buffer': gi.FunctionInfo(create_buffer), 'dump_to_file': gi.FunctionInfo(dump_to_file), 'events_in_queue': gi.FunctionInfo(events_in_queue), 'events_received': gi.FunctionInfo(events_received), 'find_element': gi.FunctionInfo(find_element), 'get_allocator': gi.FunctionInfo(get_allocator), 'get_last_pushed_timestamp': gi.FunctionInfo(get_last_pushed_timestamp), 'get_testclock': gi.FunctionInfo(get_testclock), 'play': gi.FunctionInfo(play), 'pull': gi.FunctionInfo(pull), 'pull_event': gi.FunctionInfo(pull_event), 'pull_upstream_event': gi.FunctionInfo(pull_upstream_event), 'push': gi.FunctionInfo(push), 'push_and_pull': gi.FunctionInfo(push_and_pull), 'push_event': gi.FunctionInfo(push_event), 'push_from_src': gi.FunctionInfo(push_from_src), 'push_to_sink': gi.FunctionInfo(push_to_sink), 'push_upstream_event': gi.FunctionInfo(push_upstream_event), 'query_latency': gi.FunctionInfo(query_latency), 'set_blocking_push_mode': gi.FunctionInfo(set_blocking_push_mode), 'set_caps': gi.FunctionInfo(set_caps), 'set_caps_str': gi.FunctionInfo(set_caps_str), 'set_drop_buffers': gi.FunctionInfo(set_drop_buffers), 'set_forwarding': gi.FunctionInfo(set_forwarding), 'set_propose_allocator': gi.FunctionInfo(set_propose_allocator), 'set_sink_caps': gi.FunctionInfo(set_sink_caps), 'set_sink_caps_str': gi.FunctionInfo(set_sink_caps_str), 'set_src_caps': gi.FunctionInfo(set_src_caps), 'set_src_caps_str': gi.FunctionInfo(set_src_caps_str), 'set_time': gi.FunctionInfo(set_time), 'set_upstream_latency': gi.FunctionInfo(set_upstream_latency), 'sink_push_many': gi.FunctionInfo(sink_push_many), 'src_crank_and_push_many': gi.FunctionInfo(src_crank_and_push_many), 'src_push_event': gi.FunctionInfo(src_push_event), 'take_all_data_as_buffer': gi.FunctionInfo(take_all_data_as_buffer), 'take_all_data': gi.FunctionInfo(take_all_data), 'teardown': gi.FunctionInfo(teardown), 'try_pull': gi.FunctionInfo(try_pull), 'try_pull_event': gi.FunctionInfo(try_pull_event), 'try_pull_upstream_event': gi.FunctionInfo(try_pull_upstream_event), 'upstream_events_in_queue': gi.FunctionInfo(upstream_events_in_queue), 'upstream_events_received': gi.FunctionInfo(upstream_events_received), 'use_systemclock': gi.FunctionInfo(use_systemclock), 'use_testclock': gi.FunctionInfo(use_testclock), 'wait_for_clock_id_waits': gi.FunctionInfo(wait_for_clock_id_waits), 'stress_thread_stop': gi.FunctionInfo(stress_thread_stop)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Harness)


class HarnessPrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(HarnessPrivate), '__module__': 'gi.repository.GstCheck', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'HarnessPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'HarnessPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(HarnessPrivate)


class HarnessThread(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(HarnessThread), '__module__': 'gi.repository.GstCheck', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'HarnessThread' objects>, '__weakref__': <attribute '__weakref__' of 'HarnessThread' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(HarnessThread)


class StreamConsistency(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(StreamConsistency), '__module__': 'gi.repository.GstCheck', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'StreamConsistency' objects>, '__weakref__': <attribute '__weakref__' of 'StreamConsistency' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(StreamConsistency)


class TestClock(__gi_repository_Gst.Clock):
    """
    :Constructors:
    
    ::
    
        TestClock(**properties)
        new() -> Gst.Clock
        new_with_start_time(start_time:int) -> Gst.Clock
    """
    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def add_observation(self, slave, master): # real signature unknown; restored from __doc__
        """ add_observation(self, slave:int, master:int) -> bool, r_squared:float """
        return False

    def add_observation_unapplied(self, slave, master): # real signature unknown; restored from __doc__
        """ add_observation_unapplied(self, slave:int, master:int) -> bool, r_squared:float, internal:int, external:int, rate_num:int, rate_denom:int """
        return False

    def adjust_unlocked(self, internal): # real signature unknown; restored from __doc__
        """ adjust_unlocked(self, internal:int) -> int """
        return 0

    def adjust_with_calibration(self, internal_target, cinternal, cexternal, cnum, cdenom): # real signature unknown; restored from __doc__
        """ adjust_with_calibration(self, internal_target:int, cinternal:int, cexternal:int, cnum:int, cdenom:int) -> int """
        return 0

    def advance_time(self, delta): # real signature unknown; restored from __doc__
        """ advance_time(self, delta:int) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_uniqueness(self, p_list, name): # real signature unknown; restored from __doc__
        """ check_uniqueness(list:list, name:str) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def crank(self): # real signature unknown; restored from __doc__
        """ crank(self) -> bool """
        return False

    def default_deep_notify(self, p_object, orig, pspec, excluded_props=None): # real signature unknown; restored from __doc__
        """ default_deep_notify(object:GObject.Object, orig:Gst.Object, pspec:GObject.ParamSpec, excluded_props:list=None) """
        pass

    def default_error(self, error, debug=None): # real signature unknown; restored from __doc__
        """ default_error(self, error:error, debug:str=None) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_change_resolution(self, *args, **kwargs): # real signature unknown
        """ change_resolution(self, old_resolution:int, new_resolution:int) -> int """
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def do_get_internal_time(self, *args, **kwargs): # real signature unknown
        """ get_internal_time(self) -> int """
        pass

    def do_get_resolution(self, *args, **kwargs): # real signature unknown
        """ get_resolution(self) -> int """
        pass

    def do_unschedule(self, *args, **kwargs): # real signature unknown
        """ unschedule(self, entry:Gst.ClockEntry) """
        pass

    def do_wait(self, *args, **kwargs): # real signature unknown
        """ wait(self, entry:Gst.ClockEntry, jitter:int) -> Gst.ClockReturn """
        pass

    def do_wait_async(self, *args, **kwargs): # real signature unknown
        """ wait_async(self, entry:Gst.ClockEntry) -> Gst.ClockReturn """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_calibration(self): # real signature unknown; restored from __doc__
        """ get_calibration(self) -> internal:int, external:int, rate_num:int, rate_denom:int """
        pass

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_internal_time(self): # real signature unknown; restored from __doc__
        """ get_internal_time(self) -> int """
        return 0

    def get_master(self): # real signature unknown; restored from __doc__
        """ get_master(self) -> Gst.Clock or None """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_next_entry_time(self): # real signature unknown; restored from __doc__
        """ get_next_entry_time(self) -> int """
        return 0

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.Object or None """
        pass

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_resolution(self): # real signature unknown; restored from __doc__
        """ get_resolution(self) -> int """
        return 0

    def get_time(self): # real signature unknown; restored from __doc__
        """ get_time(self) -> int """
        return 0

    def get_timeout(self): # real signature unknown; restored from __doc__
        """ get_timeout(self) -> int """
        return 0

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def has_active_control_bindings(self): # real signature unknown; restored from __doc__
        """ has_active_control_bindings(self) -> bool """
        return False

    def has_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_as_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_parent(self, parent): # real signature unknown; restored from __doc__
        """ has_as_parent(self, parent:Gst.Object) -> bool """
        return False

    def has_id(self, id): # real signature unknown; restored from __doc__
        """ has_id(self, id) -> bool """
        return False

    def id_compare_func(self, id1=None, id2=None): # real signature unknown; restored from __doc__
        """ id_compare_func(id1=None, id2=None) -> int """
        return 0

    def id_get_clock(self, id): # real signature unknown; restored from __doc__
        """ id_get_clock(id) -> Gst.Clock or None """
        pass

    def id_get_time(self, id): # real signature unknown; restored from __doc__
        """ id_get_time(id) -> int """
        return 0

    def id_list_get_latest_time(self, pending_list=None): # real signature unknown; restored from __doc__
        """ id_list_get_latest_time(pending_list:list=None) -> int """
        return 0

    def id_ref(self, id): # real signature unknown; restored from __doc__
        """ id_ref(id) """
        pass

    def id_unref(self, id): # real signature unknown; restored from __doc__
        """ id_unref(id) """
        pass

    def id_unschedule(self, id): # real signature unknown; restored from __doc__
        """ id_unschedule(id) """
        pass

    def id_uses_clock(self, id, clock): # real signature unknown; restored from __doc__
        """ id_uses_clock(id, clock:Gst.Clock) -> bool """
        return False

    def id_wait(self, id): # real signature unknown; restored from __doc__
        """ id_wait(id) -> Gst.ClockReturn, jitter:int """
        pass

    def id_wait_async(self, id, func, user_data=None): # real signature unknown; restored from __doc__
        """ id_wait_async(id, func:Gst.ClockCallback, user_data=None) -> Gst.ClockReturn """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_synced(self): # real signature unknown; restored from __doc__
        """ is_synced(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gst.Clock """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_periodic_id(self, start_time, interval): # real signature unknown; restored from __doc__
        """ new_periodic_id(self, start_time:int, interval:int) """
        pass

    def new_single_shot_id(self, time): # real signature unknown; restored from __doc__
        """ new_single_shot_id(self, time:int) """
        pass

    def new_with_start_time(self, start_time): # real signature unknown; restored from __doc__
        """ new_with_start_time(start_time:int) -> Gst.Clock """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_id_count(self): # real signature unknown; restored from __doc__
        """ peek_id_count(self) -> int """
        return 0

    def peek_next_pending_id(self): # real signature unknown; restored from __doc__
        """ peek_next_pending_id(self) -> bool, pending_id """
        return False

    def periodic_id_reinit(self, id, start_time, interval): # real signature unknown; restored from __doc__
        """ periodic_id_reinit(self, id, start_time:int, interval:int) -> bool """
        return False

    def process_id_list(self, pending_list=None): # real signature unknown; restored from __doc__
        """ process_id_list(self, pending_list:list=None) -> int """
        return 0

    def process_next_clock_id(self): # real signature unknown; restored from __doc__
        """ process_next_clock_id(self) """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gst.Object """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ remove_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def replace(self, oldobj=None, newobj=None): # real signature unknown; restored from __doc__
        """ replace(oldobj:Gst.Object=None, newobj:Gst.Object=None) -> bool, oldobj:Gst.Object """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_calibration(self, internal, external, rate_num, rate_denom): # real signature unknown; restored from __doc__
        """ set_calibration(self, internal:int, external:int, rate_num:int, rate_denom:int) """
        pass

    def set_control_bindings_disabled(self, disabled): # real signature unknown; restored from __doc__
        """ set_control_bindings_disabled(self, disabled:bool) """
        pass

    def set_control_binding_disabled(self, property_name, disabled): # real signature unknown; restored from __doc__
        """ set_control_binding_disabled(self, property_name:str, disabled:bool) """
        pass

    def set_control_rate(self, control_rate): # real signature unknown; restored from __doc__
        """ set_control_rate(self, control_rate:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_master(self, master=None): # real signature unknown; restored from __doc__
        """ set_master(self, master:Gst.Clock=None) -> bool """
        return False

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, resolution): # real signature unknown; restored from __doc__
        """ set_resolution(self, resolution:int) -> int """
        return 0

    def set_synced(self, synced): # real signature unknown; restored from __doc__
        """ set_synced(self, synced:bool) """
        pass

    def set_time(self, new_time): # real signature unknown; restored from __doc__
        """ set_time(self, new_time:int) """
        pass

    def set_timeout(self, timeout): # real signature unknown; restored from __doc__
        """ set_timeout(self, timeout:int) """
        pass

    def single_shot_id_reinit(self, id, time): # real signature unknown; restored from __doc__
        """ single_shot_id_reinit(self, id, time:int) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def timed_wait_for_multiple_pending_ids(self, count, timeout_ms): # real signature unknown; restored from __doc__
        """ timed_wait_for_multiple_pending_ids(self, count:int, timeout_ms:int) -> bool, pending_list:list """
        return False

    def unadjust_unlocked(self, external): # real signature unknown; restored from __doc__
        """ unadjust_unlocked(self, external:int) -> int """
        return 0

    def unadjust_with_calibration(self, external_target, cinternal, cexternal, cnum, cdenom): # real signature unknown; restored from __doc__
        """ unadjust_with_calibration(self, external_target:int, cinternal:int, cexternal:int, cnum:int, cdenom:int) -> int """
        return 0

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def wait_for_multiple_pending_ids(self, count): # real signature unknown; restored from __doc__
        """ wait_for_multiple_pending_ids(self, count:int) -> pending_list:list """
        pass

    def wait_for_next_pending_id(self): # real signature unknown; restored from __doc__
        """ wait_for_next_pending_id(self) -> pending_id """
        pass

    def wait_for_pending_id_count(self, count): # real signature unknown; restored from __doc__
        """ wait_for_pending_id_count(self, count:int) """
        pass

    def wait_for_sync(self, timeout): # real signature unknown; restored from __doc__
        """ wait_for_sync(self, timeout:int) -> bool """
        return False

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1802826ca0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TestClock), '__module__': 'gi.repository.GstCheck', '__gtype__': <GType GstTestClock (94052070558048)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_with_start_time': gi.FunctionInfo(new_with_start_time), 'id_list_get_latest_time': gi.FunctionInfo(id_list_get_latest_time), 'advance_time': gi.FunctionInfo(advance_time), 'crank': gi.FunctionInfo(crank), 'get_next_entry_time': gi.FunctionInfo(get_next_entry_time), 'has_id': gi.FunctionInfo(has_id), 'peek_id_count': gi.FunctionInfo(peek_id_count), 'peek_next_pending_id': gi.FunctionInfo(peek_next_pending_id), 'process_id_list': gi.FunctionInfo(process_id_list), 'process_next_clock_id': gi.FunctionInfo(process_next_clock_id), 'set_time': gi.FunctionInfo(set_time), 'timed_wait_for_multiple_pending_ids': gi.FunctionInfo(timed_wait_for_multiple_pending_ids), 'wait_for_multiple_pending_ids': gi.FunctionInfo(wait_for_multiple_pending_ids), 'wait_for_next_pending_id': gi.FunctionInfo(wait_for_next_pending_id), 'wait_for_pending_id_count': gi.FunctionInfo(wait_for_pending_id_count), 'parent': <property object at 0x7f180282c4f0>, 'priv': <property object at 0x7f180282c5e0>})"
    __gdoc__ = 'Object GstTestClock\n\nProperties from GstTestClock:\n  start-time -> guint64: Start Time\n    Start Time of the Clock\n  clock-type -> GstClockType: Clock type\n    The kind of clock implementation to be reported by this clock\n\nSignals from GstClock:\n  synced (gboolean)\n\nProperties from GstClock:\n  window-size -> gint: Window size\n    The size of the window used to calculate rate and offset\n  window-threshold -> gint: Window threshold\n    The threshold to start calculating rate and offset\n  timeout -> guint64: Timeout\n    The amount of time, in nanoseconds, to sample master and slave clocks\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstTestClock (94052070558048)>'
    __info__ = ObjectInfo(TestClock)


class TestClockClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TestClockClass()
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TestClockClass), '__module__': 'gi.repository.GstCheck', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TestClockClass' objects>, '__weakref__': <attribute '__weakref__' of 'TestClockClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f180282c770>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TestClockClass)


class TestClockPrivate(__gi.Struct):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TestClockPrivate), '__module__': 'gi.repository.GstCheck', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TestClockPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'TestClockPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TestClockPrivate)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7f1802a5f1f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7f1802a5f280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7f1802a5f310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7f1802a5f3a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f180369bd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GstCheck-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GstCheck', loader=<gi.importer.DynamicImporter object at 0x7f180369bd00>)"

