# encoding: utf-8
# module gi.repository.Soup
# from /usr/lib64/girepository-1.0/Soup-2.4.typelib
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


class Multipart(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(mime_type:str) -> Soup.Multipart
        new_from_message(headers:Soup.MessageHeaders, body:Soup.MessageBody) -> Soup.Multipart or None
    """
    def append_form_file(self, control_name, filename, content_type, body): # real signature unknown; restored from __doc__
        """ append_form_file(self, control_name:str, filename:str, content_type:str, body:Soup.Buffer) """
        pass

    def append_form_string(self, control_name, data): # real signature unknown; restored from __doc__
        """ append_form_string(self, control_name:str, data:str) """
        pass

    def append_part(self, headers, body): # real signature unknown; restored from __doc__
        """ append_part(self, headers:Soup.MessageHeaders, body:Soup.Buffer) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def get_part(self, part): # real signature unknown; restored from __doc__
        """ get_part(self, part:int) -> bool, headers:Soup.MessageHeaders, body:Soup.Buffer """
        return False

    def new(self, mime_type): # real signature unknown; restored from __doc__
        """ new(mime_type:str) -> Soup.Multipart """
        pass

    def new_from_message(self, headers, body): # real signature unknown; restored from __doc__
        """ new_from_message(headers:Soup.MessageHeaders, body:Soup.MessageBody) -> Soup.Multipart or None """
        pass

    def to_message(self, dest_headers, dest_body): # real signature unknown; restored from __doc__
        """ to_message(self, dest_headers:Soup.MessageHeaders, dest_body:Soup.MessageBody) """
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
        """ new(mime_type:str) -> Soup.Multipart """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Multipart), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupMultipart (94750594758192)>, '__dict__': <attribute '__dict__' of 'Multipart' objects>, '__weakref__': <attribute '__weakref__' of 'Multipart' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_from_message': gi.FunctionInfo(new_from_message), 'append_form_file': gi.FunctionInfo(append_form_file), 'append_form_string': gi.FunctionInfo(append_form_string), 'append_part': gi.FunctionInfo(append_part), 'free': gi.FunctionInfo(free), 'get_length': gi.FunctionInfo(get_length), 'get_part': gi.FunctionInfo(get_part), 'to_message': gi.FunctionInfo(to_message), '__new__': <staticmethod object at 0x7f8e47ee34c0>, '__init__': <function nothing at 0x7f8e4884dee0>})"
    __gtype__ = None # (!) real value is '<GType SoupMultipart (94750594758192)>'
    __info__ = StructInfo(Multipart)


