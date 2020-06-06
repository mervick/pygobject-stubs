# encoding: utf-8
# module gi.repository.GstMpegts
# from /usr/lib64/girepository-1.0/GstMpegts-1.0.typelib
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
import gobject as __gobject


class Section(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Section()
        new(pid:int, data:list) -> GstMpegts.Section
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def from_nit(self, nit): # real signature unknown; restored from __doc__
        """ from_nit(nit:GstMpegts.NIT) -> GstMpegts.Section """
        pass

    def from_pat(self, programs, ts_id): # real signature unknown; restored from __doc__
        """ from_pat(programs:list, ts_id:int) -> GstMpegts.Section """
        pass

    def from_pmt(self, pmt, pid): # real signature unknown; restored from __doc__
        """ from_pmt(pmt:GstMpegts.PMT, pid:int) -> GstMpegts.Section """
        pass

    def from_sdt(self, sdt): # real signature unknown; restored from __doc__
        """ from_sdt(sdt:GstMpegts.SDT) -> GstMpegts.Section """
        pass

    def get_atsc_cvct(self): # real signature unknown; restored from __doc__
        """ get_atsc_cvct(self) -> GstMpegts.AtscVCT """
        pass

    def get_atsc_eit(self): # real signature unknown; restored from __doc__
        """ get_atsc_eit(self) -> GstMpegts.AtscEIT """
        pass

    def get_atsc_ett(self): # real signature unknown; restored from __doc__
        """ get_atsc_ett(self) -> GstMpegts.AtscETT """
        pass

    def get_atsc_mgt(self): # real signature unknown; restored from __doc__
        """ get_atsc_mgt(self) -> GstMpegts.AtscMGT """
        pass

    def get_atsc_stt(self): # real signature unknown; restored from __doc__
        """ get_atsc_stt(self) -> GstMpegts.AtscSTT """
        pass

    def get_atsc_tvct(self): # real signature unknown; restored from __doc__
        """ get_atsc_tvct(self) -> GstMpegts.AtscVCT """
        pass

    def get_bat(self): # real signature unknown; restored from __doc__
        """ get_bat(self) -> GstMpegts.BAT """
        pass

    def get_cat(self): # real signature unknown; restored from __doc__
        """ get_cat(self) -> list """
        return []

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> GLib.Bytes """
        pass

    def get_eit(self): # real signature unknown; restored from __doc__
        """ get_eit(self) -> GstMpegts.EIT """
        pass

    def get_nit(self): # real signature unknown; restored from __doc__
        """ get_nit(self) -> GstMpegts.NIT """
        pass

    def get_pat(self): # real signature unknown; restored from __doc__
        """ get_pat(self) -> list """
        return []

    def get_pmt(self): # real signature unknown; restored from __doc__
        """ get_pmt(self) -> GstMpegts.PMT """
        pass

    def get_sdt(self): # real signature unknown; restored from __doc__
        """ get_sdt(self) -> GstMpegts.SDT """
        pass

    def get_tdt(self): # real signature unknown; restored from __doc__
        """ get_tdt(self) -> Gst.DateTime """
        pass

    def get_tot(self): # real signature unknown; restored from __doc__
        """ get_tot(self) -> GstMpegts.TOT """
        pass

    def get_tsdt(self): # real signature unknown; restored from __doc__
        """ get_tsdt(self) -> list """
        return []

    def new(self, pid, data): # real signature unknown; restored from __doc__
        """ new(pid:int, data:list) -> GstMpegts.Section """
        pass

    def packetize(self): # real signature unknown; restored from __doc__
        """ packetize(self) -> int, output_size:int """
        return 0

    def send_event(self, element): # real signature unknown; restored from __doc__
        """ send_event(self, element:Gst.Element) -> bool """
        return False

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

    cached_parsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    crc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current_next_indicator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destroy_parsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_section_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    packetizer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    section_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    section_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    section_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    short_section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subtable_extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Section), '__module__': 'gi.repository.GstMpegts', '__gtype__': <GType GstMpegtsSection (94624018705104)>, '__dict__': <attribute '__dict__' of 'Section' objects>, '__weakref__': <attribute '__weakref__' of 'Section' objects>, '__doc__': None, 'parent': <property object at 0x7faa5f6bf3b0>, 'section_type': <property object at 0x7faa5f6bf4a0>, 'pid': <property object at 0x7faa5f6bf590>, 'table_id': <property object at 0x7faa5f6bf680>, 'subtable_extension': <property object at 0x7faa5f6bf7c0>, 'version_number': <property object at 0x7faa5f6bf8b0>, 'current_next_indicator': <property object at 0x7faa5f6bf9f0>, 'section_number': <property object at 0x7faa5f6bfae0>, 'last_section_number': <property object at 0x7faa5f6bfc20>, 'crc': <property object at 0x7faa5f6bfd10>, 'data': <property object at 0x7faa5f6bfe00>, 'section_length': <property object at 0x7faa5f6bfef0>, 'cached_parsed': <property object at 0x7faa5f6c2040>, 'destroy_parsed': <property object at 0x7faa5f6c2130>, 'offset': <property object at 0x7faa5f6c2220>, 'short_section': <property object at 0x7faa5f6c2310>, 'packetizer': <property object at 0x7faa5f6c2400>, '_gst_reserved': <property object at 0x7faa5f6c24f0>, 'new': gi.FunctionInfo(new), 'get_atsc_cvct': gi.FunctionInfo(get_atsc_cvct), 'get_atsc_eit': gi.FunctionInfo(get_atsc_eit), 'get_atsc_ett': gi.FunctionInfo(get_atsc_ett), 'get_atsc_mgt': gi.FunctionInfo(get_atsc_mgt), 'get_atsc_stt': gi.FunctionInfo(get_atsc_stt), 'get_atsc_tvct': gi.FunctionInfo(get_atsc_tvct), 'get_bat': gi.FunctionInfo(get_bat), 'get_cat': gi.FunctionInfo(get_cat), 'get_data': gi.FunctionInfo(get_data), 'get_eit': gi.FunctionInfo(get_eit), 'get_nit': gi.FunctionInfo(get_nit), 'get_pat': gi.FunctionInfo(get_pat), 'get_pmt': gi.FunctionInfo(get_pmt), 'get_sdt': gi.FunctionInfo(get_sdt), 'get_tdt': gi.FunctionInfo(get_tdt), 'get_tot': gi.FunctionInfo(get_tot), 'get_tsdt': gi.FunctionInfo(get_tsdt), 'packetize': gi.FunctionInfo(packetize), 'send_event': gi.FunctionInfo(send_event), 'from_nit': gi.FunctionInfo(from_nit), 'from_pat': gi.FunctionInfo(from_pat), 'from_pmt': gi.FunctionInfo(from_pmt), 'from_sdt': gi.FunctionInfo(from_sdt)})"
    __gtype__ = None # (!) real value is '<GType GstMpegtsSection (94624018705104)>'
    __info__ = StructInfo(Section)


