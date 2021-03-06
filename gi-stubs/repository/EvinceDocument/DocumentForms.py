# encoding: utf-8
# module gi.repository.EvinceDocument
# from /usr/lib64/girepository-1.0/EvinceDocument-3.0.typelib
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
import gobject as __gobject


class DocumentForms(__gobject.GInterface):
    # no doc
    def document_is_modified(self): # real signature unknown; restored from __doc__
        """ document_is_modified(self) -> bool """
        return False

    def form_field_button_get_state(self, field): # real signature unknown; restored from __doc__
        """ form_field_button_get_state(self, field:EvinceDocument.FormField) -> bool """
        return False

    def form_field_button_set_state(self, field, state): # real signature unknown; restored from __doc__
        """ form_field_button_set_state(self, field:EvinceDocument.FormField, state:bool) """
        pass

    def form_field_choice_get_item(self, field, index): # real signature unknown; restored from __doc__
        """ form_field_choice_get_item(self, field:EvinceDocument.FormField, index:int) -> str """
        return ""

    def form_field_choice_get_n_items(self, field): # real signature unknown; restored from __doc__
        """ form_field_choice_get_n_items(self, field:EvinceDocument.FormField) -> int """
        return 0

    def form_field_choice_get_text(self, field): # real signature unknown; restored from __doc__
        """ form_field_choice_get_text(self, field:EvinceDocument.FormField) -> str """
        return ""

    def form_field_choice_is_item_selected(self, field, index): # real signature unknown; restored from __doc__
        """ form_field_choice_is_item_selected(self, field:EvinceDocument.FormField, index:int) -> bool """
        return False

    def form_field_choice_select_item(self, field, index): # real signature unknown; restored from __doc__
        """ form_field_choice_select_item(self, field:EvinceDocument.FormField, index:int) """
        pass

    def form_field_choice_set_text(self, field, text): # real signature unknown; restored from __doc__
        """ form_field_choice_set_text(self, field:EvinceDocument.FormField, text:str) """
        pass

    def form_field_choice_toggle_item(self, field, index): # real signature unknown; restored from __doc__
        """ form_field_choice_toggle_item(self, field:EvinceDocument.FormField, index:int) """
        pass

    def form_field_choice_unselect_all(self, field): # real signature unknown; restored from __doc__
        """ form_field_choice_unselect_all(self, field:EvinceDocument.FormField) """
        pass

    def form_field_text_get_text(self, field): # real signature unknown; restored from __doc__
        """ form_field_text_get_text(self, field:EvinceDocument.FormField) -> str """
        return ""

    def form_field_text_set_text(self, field, text): # real signature unknown; restored from __doc__
        """ form_field_text_set_text(self, field:EvinceDocument.FormField, text:str) """
        pass

    def get_form_fields(self, page): # real signature unknown; restored from __doc__
        """ get_form_fields(self, page:EvinceDocument.Page) -> EvinceDocument.MappingList """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(DocumentForms), '__module__': 'gi.repository.EvinceDocument', '__gtype__': <GType EvDocumentForms (94742333983424)>, '__dict__': <attribute '__dict__' of 'DocumentForms' objects>, '__weakref__': <attribute '__weakref__' of 'DocumentForms' objects>, '__doc__': None, '__gsignals__': {}, 'document_is_modified': gi.FunctionInfo(document_is_modified), 'form_field_button_get_state': gi.FunctionInfo(form_field_button_get_state), 'form_field_button_set_state': gi.FunctionInfo(form_field_button_set_state), 'form_field_choice_get_item': gi.FunctionInfo(form_field_choice_get_item), 'form_field_choice_get_n_items': gi.FunctionInfo(form_field_choice_get_n_items), 'form_field_choice_get_text': gi.FunctionInfo(form_field_choice_get_text), 'form_field_choice_is_item_selected': gi.FunctionInfo(form_field_choice_is_item_selected), 'form_field_choice_select_item': gi.FunctionInfo(form_field_choice_select_item), 'form_field_choice_set_text': gi.FunctionInfo(form_field_choice_set_text), 'form_field_choice_toggle_item': gi.FunctionInfo(form_field_choice_toggle_item), 'form_field_choice_unselect_all': gi.FunctionInfo(form_field_choice_unselect_all), 'form_field_text_get_text': gi.FunctionInfo(form_field_text_get_text), 'form_field_text_set_text': gi.FunctionInfo(form_field_text_set_text), 'get_form_fields': gi.FunctionInfo(get_form_fields)})"
    __gdoc__ = 'Interface EvDocumentForms\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EvDocumentForms (94742333983424)>'
    __info__ = InterfaceInfo(DocumentForms)


