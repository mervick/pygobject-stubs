# encoding: utf-8
# module gi.repository.GstVideo
# from /usr/lib64/girepository-1.0/GstVideo-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


class Navigation(__gobject.GInterface):
    # no doc
    def event_get_type(self, event): # real signature unknown; restored from __doc__
        """ event_get_type(event:Gst.Event) -> GstVideo.NavigationEventType """
        pass

    def event_parse_command(self, event): # real signature unknown; restored from __doc__
        """ event_parse_command(event:Gst.Event) -> bool, command:GstVideo.NavigationCommand """
        return False

    def event_parse_key_event(self, event): # real signature unknown; restored from __doc__
        """ event_parse_key_event(event:Gst.Event) -> bool, key:str """
        return False

    def event_parse_mouse_button_event(self, event): # real signature unknown; restored from __doc__
        """ event_parse_mouse_button_event(event:Gst.Event) -> bool, button:int, x:float, y:float """
        return False

    def event_parse_mouse_move_event(self, event): # real signature unknown; restored from __doc__
        """ event_parse_mouse_move_event(event:Gst.Event) -> bool, x:float, y:float """
        return False

    def message_get_type(self, message): # real signature unknown; restored from __doc__
        """ message_get_type(message:Gst.Message) -> GstVideo.NavigationMessageType """
        pass

    def message_new_angles_changed(self, src, cur_angle, n_angles): # real signature unknown; restored from __doc__
        """ message_new_angles_changed(src:Gst.Object, cur_angle:int, n_angles:int) -> Gst.Message """
        pass

    def message_new_commands_changed(self, src): # real signature unknown; restored from __doc__
        """ message_new_commands_changed(src:Gst.Object) -> Gst.Message """
        pass

    def message_new_event(self, src, event): # real signature unknown; restored from __doc__
        """ message_new_event(src:Gst.Object, event:Gst.Event) -> Gst.Message """
        pass

    def message_new_mouse_over(self, src, active): # real signature unknown; restored from __doc__
        """ message_new_mouse_over(src:Gst.Object, active:bool) -> Gst.Message """
        pass

    def message_parse_angles_changed(self, message): # real signature unknown; restored from __doc__
        """ message_parse_angles_changed(message:Gst.Message) -> bool, cur_angle:int, n_angles:int """
        return False

    def message_parse_event(self, message): # real signature unknown; restored from __doc__
        """ message_parse_event(message:Gst.Message) -> bool, event:Gst.Event """
        return False

    def message_parse_mouse_over(self, message): # real signature unknown; restored from __doc__
        """ message_parse_mouse_over(message:Gst.Message) -> bool, active:bool """
        return False

    def query_get_type(self, query): # real signature unknown; restored from __doc__
        """ query_get_type(query:Gst.Query) -> GstVideo.NavigationQueryType """
        pass

    def query_new_angles(self): # real signature unknown; restored from __doc__
        """ query_new_angles() -> Gst.Query """
        pass

    def query_new_commands(self): # real signature unknown; restored from __doc__
        """ query_new_commands() -> Gst.Query """
        pass

    def query_parse_angles(self, query): # real signature unknown; restored from __doc__
        """ query_parse_angles(query:Gst.Query) -> bool, cur_angle:int, n_angles:int """
        return False

    def query_parse_commands_length(self, query): # real signature unknown; restored from __doc__
        """ query_parse_commands_length(query:Gst.Query) -> bool, n_cmds:int """
        return False

    def query_parse_commands_nth(self, query, nth): # real signature unknown; restored from __doc__
        """ query_parse_commands_nth(query:Gst.Query, nth:int) -> bool, cmd:GstVideo.NavigationCommand """
        return False

    def query_set_angles(self, query, cur_angle, n_angles): # real signature unknown; restored from __doc__
        """ query_set_angles(query:Gst.Query, cur_angle:int, n_angles:int) """
        pass

    def query_set_commandsv(self, query, cmds): # real signature unknown; restored from __doc__
        """ query_set_commandsv(query:Gst.Query, cmds:list) """
        pass

    def send_command(self, command): # real signature unknown; restored from __doc__
        """ send_command(self, command:GstVideo.NavigationCommand) """
        pass

    def send_event(self, structure): # real signature unknown; restored from __doc__
        """ send_event(self, structure:Gst.Structure) """
        pass

    def send_key_event(self, event, key): # real signature unknown; restored from __doc__
        """ send_key_event(self, event:str, key:str) """
        pass

    def send_mouse_event(self, event, button, x, y): # real signature unknown; restored from __doc__
        """ send_mouse_event(self, event:str, button:int, x:float, y:float) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Navigation), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType GstNavigation (94743668809872)>, '__dict__': <attribute '__dict__' of 'Navigation' objects>, '__weakref__': <attribute '__weakref__' of 'Navigation' objects>, '__doc__': None, '__gsignals__': {}, 'event_get_type': gi.FunctionInfo(event_get_type), 'event_parse_command': gi.FunctionInfo(event_parse_command), 'event_parse_key_event': gi.FunctionInfo(event_parse_key_event), 'event_parse_mouse_button_event': gi.FunctionInfo(event_parse_mouse_button_event), 'event_parse_mouse_move_event': gi.FunctionInfo(event_parse_mouse_move_event), 'message_get_type': gi.FunctionInfo(message_get_type), 'message_new_angles_changed': gi.FunctionInfo(message_new_angles_changed), 'message_new_commands_changed': gi.FunctionInfo(message_new_commands_changed), 'message_new_event': gi.FunctionInfo(message_new_event), 'message_new_mouse_over': gi.FunctionInfo(message_new_mouse_over), 'message_parse_angles_changed': gi.FunctionInfo(message_parse_angles_changed), 'message_parse_event': gi.FunctionInfo(message_parse_event), 'message_parse_mouse_over': gi.FunctionInfo(message_parse_mouse_over), 'query_get_type': gi.FunctionInfo(query_get_type), 'query_new_angles': gi.FunctionInfo(query_new_angles), 'query_new_commands': gi.FunctionInfo(query_new_commands), 'query_parse_angles': gi.FunctionInfo(query_parse_angles), 'query_parse_commands_length': gi.FunctionInfo(query_parse_commands_length), 'query_parse_commands_nth': gi.FunctionInfo(query_parse_commands_nth), 'query_set_angles': gi.FunctionInfo(query_set_angles), 'query_set_commandsv': gi.FunctionInfo(query_set_commandsv), 'send_command': gi.FunctionInfo(send_command), 'send_event': gi.FunctionInfo(send_event), 'send_key_event': gi.FunctionInfo(send_key_event), 'send_mouse_event': gi.FunctionInfo(send_mouse_event)})"
    __gdoc__ = 'Interface GstNavigation\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstNavigation (94743668809872)>'
    __info__ = InterfaceInfo(Navigation)


