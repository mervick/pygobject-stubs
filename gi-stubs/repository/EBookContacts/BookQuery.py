# encoding: utf-8
# module gi.repository.EBookContacts
# from /usr/lib64/girepository-1.0/EBookContacts-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gobject as __gobject


class BookQuery(__gi.Boxed):
    # no doc
    def and_(self, nqs, qs, unref): # real signature unknown; restored from __doc__
        """ and_(nqs:int, qs:EBookContacts.BookQuery, unref:bool) -> EBookContacts.BookQuery """
        pass

    def any_field_contains(self, value): # real signature unknown; restored from __doc__
        """ any_field_contains(value:str) -> EBookContacts.BookQuery """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EBookContacts.BookQuery """
        pass

    def field_exists(self, field): # real signature unknown; restored from __doc__
        """ field_exists(field:EBookContacts.ContactField) -> EBookContacts.BookQuery """
        pass

    def field_test(self, field, test, value): # real signature unknown; restored from __doc__
        """ field_test(field:EBookContacts.ContactField, test:EBookContacts.BookQueryTest, value:str) -> EBookContacts.BookQuery """
        pass

    def from_string(self, query_string): # real signature unknown; restored from __doc__
        """ from_string(query_string:str) -> EBookContacts.BookQuery """
        pass

    def not_(self, unref): # real signature unknown; restored from __doc__
        """ not_(self, unref:bool) -> EBookContacts.BookQuery """
        pass

    def or_(self, nqs, qs, unref): # real signature unknown; restored from __doc__
        """ or_(nqs:int, qs:EBookContacts.BookQuery, unref:bool) -> EBookContacts.BookQuery """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> EBookContacts.BookQuery """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def vcard_field_exists(self, field): # real signature unknown; restored from __doc__
        """ vcard_field_exists(field:str) -> EBookContacts.BookQuery """
        pass

    def vcard_field_test(self, field, test, value): # real signature unknown; restored from __doc__
        """ vcard_field_test(field:str, test:EBookContacts.BookQueryTest, value:str) -> EBookContacts.BookQuery """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BookQuery), '__module__': 'gi.repository.EBookContacts', '__gtype__': <GType EBookQuery (94769385539264)>, '__dict__': <attribute '__dict__' of 'BookQuery' objects>, '__weakref__': <attribute '__weakref__' of 'BookQuery' objects>, '__doc__': None, 'copy': gi.FunctionInfo(copy), 'not_': gi.FunctionInfo(not), 'ref': gi.FunctionInfo(ref), 'to_string': gi.FunctionInfo(to_string), 'unref': gi.FunctionInfo(unref), 'and_': gi.FunctionInfo(and), 'any_field_contains': gi.FunctionInfo(any_field_contains), 'field_exists': gi.FunctionInfo(field_exists), 'field_test': gi.FunctionInfo(field_test), 'from_string': gi.FunctionInfo(from_string), 'or_': gi.FunctionInfo(or), 'vcard_field_exists': gi.FunctionInfo(vcard_field_exists), 'vcard_field_test': gi.FunctionInfo(vcard_field_test)})"
    __gtype__ = None # (!) real value is '<GType EBookQuery (94769385539264)>'
    __info__ = StructInfo(BookQuery)


