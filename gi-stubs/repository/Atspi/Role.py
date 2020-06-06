# encoding: utf-8
# module gi.repository.Atspi
# from /usr/lib64/girepository-1.0/Atspi-2.0.typelib
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


class Role(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def get_name(self, role): # real signature unknown; restored from __doc__
        """ get_name(role:Atspi.Role) -> str """
        return ""

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ACCELERATOR_LABEL = 1
    ALERT = 2
    ANIMATION = 3
    APPLICATION = 75
    ARROW = 4
    ARTICLE = 109
    AUDIO = 106
    AUTOCOMPLETE = 76
    BLOCK_QUOTE = 105
    CALENDAR = 5
    CANVAS = 6
    CAPTION = 81
    CHART = 80
    CHECK_BOX = 7
    CHECK_MENU_ITEM = 8
    COLOR_CHOOSER = 9
    COLUMN_HEADER = 10
    COMBO_BOX = 11
    COMMENT = 97
    CONTENT_DELETION = 125
    CONTENT_INSERTION = 126
    DATE_EDITOR = 12
    DEFINITION = 108
    DESCRIPTION_LIST = 121
    DESCRIPTION_TERM = 122
    DESCRIPTION_VALUE = 123
    DESKTOP_FRAME = 14
    DESKTOP_ICON = 13
    DIAL = 15
    DIALOG = 16
    DIRECTORY_PANE = 17
    DOCUMENT_EMAIL = 96
    DOCUMENT_FRAME = 82
    DOCUMENT_PRESENTATION = 93
    DOCUMENT_SPREADSHEET = 92
    DOCUMENT_TEXT = 94
    DOCUMENT_WEB = 95
    DRAWING_AREA = 18
    EDITBAR = 77
    EMBEDDED = 78
    ENTRY = 79
    EXTENDED = 70
    FILE_CHOOSER = 19
    FILLER = 20
    FOCUS_TRAVERSABLE = 21
    FONT_CHOOSER = 22
    FOOTER = 72
    FOOTNOTE = 124
    FORM = 87
    FRAME = 23
    GLASS_PANE = 24
    GROUPING = 99
    HEADER = 71
    HEADING = 83
    HTML_CONTAINER = 25
    ICON = 26
    IMAGE = 27
    IMAGE_MAP = 100
    INFO_BAR = 102
    INPUT_METHOD_WINDOW = 89
    INTERNAL_FRAME = 28
    INVALID = 0
    LABEL = 29
    LANDMARK = 110
    LAST_DEFINED = 129
    LAYERED_PANE = 30
    LEVEL_BAR = 103
    LINK = 88
    LIST = 31
    LIST_BOX = 98
    LIST_ITEM = 32
    LOG = 111
    MARK = 127
    MARQUEE = 112
    MATH = 113
    MATH_FRACTION = 117
    MATH_ROOT = 118
    MENU = 33
    MENU_BAR = 34
    MENU_ITEM = 35
    NOTIFICATION = 101
    OPTION_PANE = 36
    PAGE = 84
    PAGE_TAB = 37
    PAGE_TAB_LIST = 38
    PANEL = 39
    PARAGRAPH = 73
    PASSWORD_TEXT = 40
    POPUP_MENU = 41
    PROGRESS_BAR = 42
    PUSH_BUTTON = 43
    RADIO_BUTTON = 44
    RADIO_MENU_ITEM = 45
    RATING = 114
    REDUNDANT_OBJECT = 86
    ROOT_PANE = 46
    ROW_HEADER = 47
    RULER = 74
    SCROLL_BAR = 48
    SCROLL_PANE = 49
    SECTION = 85
    SEPARATOR = 50
    SLIDER = 51
    SPIN_BUTTON = 52
    SPLIT_PANE = 53
    STATIC = 116
    STATUS_BAR = 54
    SUBSCRIPT = 119
    SUGGESTION = 128
    SUPERSCRIPT = 120
    TABLE = 55
    TABLE_CELL = 56
    TABLE_COLUMN_HEADER = 57
    TABLE_ROW = 90
    TABLE_ROW_HEADER = 58
    TEAROFF_MENU_ITEM = 59
    TERMINAL = 60
    TEXT = 61
    TIMER = 115
    TITLE_BAR = 104
    TOGGLE_BUTTON = 62
    TOOL_BAR = 63
    TOOL_TIP = 64
    TREE = 65
    TREE_ITEM = 91
    TREE_TABLE = 66
    UNKNOWN = 67
    VIDEO = 107
    VIEWPORT = 68
    WINDOW = 69
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Atspi', '__dict__': <attribute '__dict__' of 'Role' objects>, '__doc__': None, '__gtype__': <GType AtspiRole (94141573830560)>, '__enum_values__': {0: <enum ATSPI_ROLE_INVALID of type Atspi.Role>, 1: <enum ATSPI_ROLE_ACCELERATOR_LABEL of type Atspi.Role>, 2: <enum ATSPI_ROLE_ALERT of type Atspi.Role>, 3: <enum ATSPI_ROLE_ANIMATION of type Atspi.Role>, 4: <enum ATSPI_ROLE_ARROW of type Atspi.Role>, 5: <enum ATSPI_ROLE_CALENDAR of type Atspi.Role>, 6: <enum ATSPI_ROLE_CANVAS of type Atspi.Role>, 7: <enum ATSPI_ROLE_CHECK_BOX of type Atspi.Role>, 8: <enum ATSPI_ROLE_CHECK_MENU_ITEM of type Atspi.Role>, 9: <enum ATSPI_ROLE_COLOR_CHOOSER of type Atspi.Role>, 10: <enum ATSPI_ROLE_COLUMN_HEADER of type Atspi.Role>, 11: <enum ATSPI_ROLE_COMBO_BOX of type Atspi.Role>, 12: <enum ATSPI_ROLE_DATE_EDITOR of type Atspi.Role>, 13: <enum ATSPI_ROLE_DESKTOP_ICON of type Atspi.Role>, 14: <enum ATSPI_ROLE_DESKTOP_FRAME of type Atspi.Role>, 15: <enum ATSPI_ROLE_DIAL of type Atspi.Role>, 16: <enum ATSPI_ROLE_DIALOG of type Atspi.Role>, 17: <enum ATSPI_ROLE_DIRECTORY_PANE of type Atspi.Role>, 18: <enum ATSPI_ROLE_DRAWING_AREA of type Atspi.Role>, 19: <enum ATSPI_ROLE_FILE_CHOOSER of type Atspi.Role>, 20: <enum ATSPI_ROLE_FILLER of type Atspi.Role>, 21: <enum ATSPI_ROLE_FOCUS_TRAVERSABLE of type Atspi.Role>, 22: <enum ATSPI_ROLE_FONT_CHOOSER of type Atspi.Role>, 23: <enum ATSPI_ROLE_FRAME of type Atspi.Role>, 24: <enum ATSPI_ROLE_GLASS_PANE of type Atspi.Role>, 25: <enum ATSPI_ROLE_HTML_CONTAINER of type Atspi.Role>, 26: <enum ATSPI_ROLE_ICON of type Atspi.Role>, 27: <enum ATSPI_ROLE_IMAGE of type Atspi.Role>, 28: <enum ATSPI_ROLE_INTERNAL_FRAME of type Atspi.Role>, 29: <enum ATSPI_ROLE_LABEL of type Atspi.Role>, 30: <enum ATSPI_ROLE_LAYERED_PANE of type Atspi.Role>, 31: <enum ATSPI_ROLE_LIST of type Atspi.Role>, 32: <enum ATSPI_ROLE_LIST_ITEM of type Atspi.Role>, 33: <enum ATSPI_ROLE_MENU of type Atspi.Role>, 34: <enum ATSPI_ROLE_MENU_BAR of type Atspi.Role>, 35: <enum ATSPI_ROLE_MENU_ITEM of type Atspi.Role>, 36: <enum ATSPI_ROLE_OPTION_PANE of type Atspi.Role>, 37: <enum ATSPI_ROLE_PAGE_TAB of type Atspi.Role>, 38: <enum ATSPI_ROLE_PAGE_TAB_LIST of type Atspi.Role>, 39: <enum ATSPI_ROLE_PANEL of type Atspi.Role>, 40: <enum ATSPI_ROLE_PASSWORD_TEXT of type Atspi.Role>, 41: <enum ATSPI_ROLE_POPUP_MENU of type Atspi.Role>, 42: <enum ATSPI_ROLE_PROGRESS_BAR of type Atspi.Role>, 43: <enum ATSPI_ROLE_PUSH_BUTTON of type Atspi.Role>, 44: <enum ATSPI_ROLE_RADIO_BUTTON of type Atspi.Role>, 45: <enum ATSPI_ROLE_RADIO_MENU_ITEM of type Atspi.Role>, 46: <enum ATSPI_ROLE_ROOT_PANE of type Atspi.Role>, 47: <enum ATSPI_ROLE_ROW_HEADER of type Atspi.Role>, 48: <enum ATSPI_ROLE_SCROLL_BAR of type Atspi.Role>, 49: <enum ATSPI_ROLE_SCROLL_PANE of type Atspi.Role>, 50: <enum ATSPI_ROLE_SEPARATOR of type Atspi.Role>, 51: <enum ATSPI_ROLE_SLIDER of type Atspi.Role>, 52: <enum ATSPI_ROLE_SPIN_BUTTON of type Atspi.Role>, 53: <enum ATSPI_ROLE_SPLIT_PANE of type Atspi.Role>, 54: <enum ATSPI_ROLE_STATUS_BAR of type Atspi.Role>, 55: <enum ATSPI_ROLE_TABLE of type Atspi.Role>, 56: <enum ATSPI_ROLE_TABLE_CELL of type Atspi.Role>, 57: <enum ATSPI_ROLE_TABLE_COLUMN_HEADER of type Atspi.Role>, 58: <enum ATSPI_ROLE_TABLE_ROW_HEADER of type Atspi.Role>, 59: <enum ATSPI_ROLE_TEAROFF_MENU_ITEM of type Atspi.Role>, 60: <enum ATSPI_ROLE_TERMINAL of type Atspi.Role>, 61: <enum ATSPI_ROLE_TEXT of type Atspi.Role>, 62: <enum ATSPI_ROLE_TOGGLE_BUTTON of type Atspi.Role>, 63: <enum ATSPI_ROLE_TOOL_BAR of type Atspi.Role>, 64: <enum ATSPI_ROLE_TOOL_TIP of type Atspi.Role>, 65: <enum ATSPI_ROLE_TREE of type Atspi.Role>, 66: <enum ATSPI_ROLE_TREE_TABLE of type Atspi.Role>, 67: <enum ATSPI_ROLE_UNKNOWN of type Atspi.Role>, 68: <enum ATSPI_ROLE_VIEWPORT of type Atspi.Role>, 69: <enum ATSPI_ROLE_WINDOW of type Atspi.Role>, 70: <enum ATSPI_ROLE_EXTENDED of type Atspi.Role>, 71: <enum ATSPI_ROLE_HEADER of type Atspi.Role>, 72: <enum ATSPI_ROLE_FOOTER of type Atspi.Role>, 73: <enum ATSPI_ROLE_PARAGRAPH of type Atspi.Role>, 74: <enum ATSPI_ROLE_RULER of type Atspi.Role>, 75: <enum ATSPI_ROLE_APPLICATION of type Atspi.Role>, 76: <enum ATSPI_ROLE_AUTOCOMPLETE of type Atspi.Role>, 77: <enum ATSPI_ROLE_EDITBAR of type Atspi.Role>, 78: <enum ATSPI_ROLE_EMBEDDED of type Atspi.Role>, 79: <enum ATSPI_ROLE_ENTRY of type Atspi.Role>, 80: <enum ATSPI_ROLE_CHART of type Atspi.Role>, 81: <enum ATSPI_ROLE_CAPTION of type Atspi.Role>, 82: <enum ATSPI_ROLE_DOCUMENT_FRAME of type Atspi.Role>, 83: <enum ATSPI_ROLE_HEADING of type Atspi.Role>, 84: <enum ATSPI_ROLE_PAGE of type Atspi.Role>, 85: <enum ATSPI_ROLE_SECTION of type Atspi.Role>, 86: <enum ATSPI_ROLE_REDUNDANT_OBJECT of type Atspi.Role>, 87: <enum ATSPI_ROLE_FORM of type Atspi.Role>, 88: <enum ATSPI_ROLE_LINK of type Atspi.Role>, 89: <enum ATSPI_ROLE_INPUT_METHOD_WINDOW of type Atspi.Role>, 90: <enum ATSPI_ROLE_TABLE_ROW of type Atspi.Role>, 91: <enum ATSPI_ROLE_TREE_ITEM of type Atspi.Role>, 92: <enum ATSPI_ROLE_DOCUMENT_SPREADSHEET of type Atspi.Role>, 93: <enum ATSPI_ROLE_DOCUMENT_PRESENTATION of type Atspi.Role>, 94: <enum ATSPI_ROLE_DOCUMENT_TEXT of type Atspi.Role>, 95: <enum ATSPI_ROLE_DOCUMENT_WEB of type Atspi.Role>, 96: <enum ATSPI_ROLE_DOCUMENT_EMAIL of type Atspi.Role>, 97: <enum ATSPI_ROLE_COMMENT of type Atspi.Role>, 98: <enum ATSPI_ROLE_LIST_BOX of type Atspi.Role>, 99: <enum ATSPI_ROLE_GROUPING of type Atspi.Role>, 100: <enum ATSPI_ROLE_IMAGE_MAP of type Atspi.Role>, 101: <enum ATSPI_ROLE_NOTIFICATION of type Atspi.Role>, 102: <enum ATSPI_ROLE_INFO_BAR of type Atspi.Role>, 103: <enum ATSPI_ROLE_LEVEL_BAR of type Atspi.Role>, 104: <enum ATSPI_ROLE_TITLE_BAR of type Atspi.Role>, 105: <enum ATSPI_ROLE_BLOCK_QUOTE of type Atspi.Role>, 106: <enum ATSPI_ROLE_AUDIO of type Atspi.Role>, 107: <enum ATSPI_ROLE_VIDEO of type Atspi.Role>, 108: <enum ATSPI_ROLE_DEFINITION of type Atspi.Role>, 109: <enum ATSPI_ROLE_ARTICLE of type Atspi.Role>, 110: <enum ATSPI_ROLE_LANDMARK of type Atspi.Role>, 111: <enum ATSPI_ROLE_LOG of type Atspi.Role>, 112: <enum ATSPI_ROLE_MARQUEE of type Atspi.Role>, 113: <enum ATSPI_ROLE_MATH of type Atspi.Role>, 114: <enum ATSPI_ROLE_RATING of type Atspi.Role>, 115: <enum ATSPI_ROLE_TIMER of type Atspi.Role>, 116: <enum ATSPI_ROLE_STATIC of type Atspi.Role>, 117: <enum ATSPI_ROLE_MATH_FRACTION of type Atspi.Role>, 118: <enum ATSPI_ROLE_MATH_ROOT of type Atspi.Role>, 119: <enum ATSPI_ROLE_SUBSCRIPT of type Atspi.Role>, 120: <enum ATSPI_ROLE_SUPERSCRIPT of type Atspi.Role>, 121: <enum ATSPI_ROLE_DESCRIPTION_LIST of type Atspi.Role>, 122: <enum ATSPI_ROLE_DESCRIPTION_TERM of type Atspi.Role>, 123: <enum ATSPI_ROLE_DESCRIPTION_VALUE of type Atspi.Role>, 124: <enum ATSPI_ROLE_FOOTNOTE of type Atspi.Role>, 125: <enum ATSPI_ROLE_CONTENT_DELETION of type Atspi.Role>, 126: <enum ATSPI_ROLE_CONTENT_INSERTION of type Atspi.Role>, 127: <enum ATSPI_ROLE_MARK of type Atspi.Role>, 128: <enum ATSPI_ROLE_SUGGESTION of type Atspi.Role>, 129: <enum ATSPI_ROLE_LAST_DEFINED of type Atspi.Role>}, '__info__': gi.EnumInfo(Role), 'INVALID': <enum ATSPI_ROLE_INVALID of type Atspi.Role>, 'ACCELERATOR_LABEL': <enum ATSPI_ROLE_ACCELERATOR_LABEL of type Atspi.Role>, 'ALERT': <enum ATSPI_ROLE_ALERT of type Atspi.Role>, 'ANIMATION': <enum ATSPI_ROLE_ANIMATION of type Atspi.Role>, 'ARROW': <enum ATSPI_ROLE_ARROW of type Atspi.Role>, 'CALENDAR': <enum ATSPI_ROLE_CALENDAR of type Atspi.Role>, 'CANVAS': <enum ATSPI_ROLE_CANVAS of type Atspi.Role>, 'CHECK_BOX': <enum ATSPI_ROLE_CHECK_BOX of type Atspi.Role>, 'CHECK_MENU_ITEM': <enum ATSPI_ROLE_CHECK_MENU_ITEM of type Atspi.Role>, 'COLOR_CHOOSER': <enum ATSPI_ROLE_COLOR_CHOOSER of type Atspi.Role>, 'COLUMN_HEADER': <enum ATSPI_ROLE_COLUMN_HEADER of type Atspi.Role>, 'COMBO_BOX': <enum ATSPI_ROLE_COMBO_BOX of type Atspi.Role>, 'DATE_EDITOR': <enum ATSPI_ROLE_DATE_EDITOR of type Atspi.Role>, 'DESKTOP_ICON': <enum ATSPI_ROLE_DESKTOP_ICON of type Atspi.Role>, 'DESKTOP_FRAME': <enum ATSPI_ROLE_DESKTOP_FRAME of type Atspi.Role>, 'DIAL': <enum ATSPI_ROLE_DIAL of type Atspi.Role>, 'DIALOG': <enum ATSPI_ROLE_DIALOG of type Atspi.Role>, 'DIRECTORY_PANE': <enum ATSPI_ROLE_DIRECTORY_PANE of type Atspi.Role>, 'DRAWING_AREA': <enum ATSPI_ROLE_DRAWING_AREA of type Atspi.Role>, 'FILE_CHOOSER': <enum ATSPI_ROLE_FILE_CHOOSER of type Atspi.Role>, 'FILLER': <enum ATSPI_ROLE_FILLER of type Atspi.Role>, 'FOCUS_TRAVERSABLE': <enum ATSPI_ROLE_FOCUS_TRAVERSABLE of type Atspi.Role>, 'FONT_CHOOSER': <enum ATSPI_ROLE_FONT_CHOOSER of type Atspi.Role>, 'FRAME': <enum ATSPI_ROLE_FRAME of type Atspi.Role>, 'GLASS_PANE': <enum ATSPI_ROLE_GLASS_PANE of type Atspi.Role>, 'HTML_CONTAINER': <enum ATSPI_ROLE_HTML_CONTAINER of type Atspi.Role>, 'ICON': <enum ATSPI_ROLE_ICON of type Atspi.Role>, 'IMAGE': <enum ATSPI_ROLE_IMAGE of type Atspi.Role>, 'INTERNAL_FRAME': <enum ATSPI_ROLE_INTERNAL_FRAME of type Atspi.Role>, 'LABEL': <enum ATSPI_ROLE_LABEL of type Atspi.Role>, 'LAYERED_PANE': <enum ATSPI_ROLE_LAYERED_PANE of type Atspi.Role>, 'LIST': <enum ATSPI_ROLE_LIST of type Atspi.Role>, 'LIST_ITEM': <enum ATSPI_ROLE_LIST_ITEM of type Atspi.Role>, 'MENU': <enum ATSPI_ROLE_MENU of type Atspi.Role>, 'MENU_BAR': <enum ATSPI_ROLE_MENU_BAR of type Atspi.Role>, 'MENU_ITEM': <enum ATSPI_ROLE_MENU_ITEM of type Atspi.Role>, 'OPTION_PANE': <enum ATSPI_ROLE_OPTION_PANE of type Atspi.Role>, 'PAGE_TAB': <enum ATSPI_ROLE_PAGE_TAB of type Atspi.Role>, 'PAGE_TAB_LIST': <enum ATSPI_ROLE_PAGE_TAB_LIST of type Atspi.Role>, 'PANEL': <enum ATSPI_ROLE_PANEL of type Atspi.Role>, 'PASSWORD_TEXT': <enum ATSPI_ROLE_PASSWORD_TEXT of type Atspi.Role>, 'POPUP_MENU': <enum ATSPI_ROLE_POPUP_MENU of type Atspi.Role>, 'PROGRESS_BAR': <enum ATSPI_ROLE_PROGRESS_BAR of type Atspi.Role>, 'PUSH_BUTTON': <enum ATSPI_ROLE_PUSH_BUTTON of type Atspi.Role>, 'RADIO_BUTTON': <enum ATSPI_ROLE_RADIO_BUTTON of type Atspi.Role>, 'RADIO_MENU_ITEM': <enum ATSPI_ROLE_RADIO_MENU_ITEM of type Atspi.Role>, 'ROOT_PANE': <enum ATSPI_ROLE_ROOT_PANE of type Atspi.Role>, 'ROW_HEADER': <enum ATSPI_ROLE_ROW_HEADER of type Atspi.Role>, 'SCROLL_BAR': <enum ATSPI_ROLE_SCROLL_BAR of type Atspi.Role>, 'SCROLL_PANE': <enum ATSPI_ROLE_SCROLL_PANE of type Atspi.Role>, 'SEPARATOR': <enum ATSPI_ROLE_SEPARATOR of type Atspi.Role>, 'SLIDER': <enum ATSPI_ROLE_SLIDER of type Atspi.Role>, 'SPIN_BUTTON': <enum ATSPI_ROLE_SPIN_BUTTON of type Atspi.Role>, 'SPLIT_PANE': <enum ATSPI_ROLE_SPLIT_PANE of type Atspi.Role>, 'STATUS_BAR': <enum ATSPI_ROLE_STATUS_BAR of type Atspi.Role>, 'TABLE': <enum ATSPI_ROLE_TABLE of type Atspi.Role>, 'TABLE_CELL': <enum ATSPI_ROLE_TABLE_CELL of type Atspi.Role>, 'TABLE_COLUMN_HEADER': <enum ATSPI_ROLE_TABLE_COLUMN_HEADER of type Atspi.Role>, 'TABLE_ROW_HEADER': <enum ATSPI_ROLE_TABLE_ROW_HEADER of type Atspi.Role>, 'TEAROFF_MENU_ITEM': <enum ATSPI_ROLE_TEAROFF_MENU_ITEM of type Atspi.Role>, 'TERMINAL': <enum ATSPI_ROLE_TERMINAL of type Atspi.Role>, 'TEXT': <enum ATSPI_ROLE_TEXT of type Atspi.Role>, 'TOGGLE_BUTTON': <enum ATSPI_ROLE_TOGGLE_BUTTON of type Atspi.Role>, 'TOOL_BAR': <enum ATSPI_ROLE_TOOL_BAR of type Atspi.Role>, 'TOOL_TIP': <enum ATSPI_ROLE_TOOL_TIP of type Atspi.Role>, 'TREE': <enum ATSPI_ROLE_TREE of type Atspi.Role>, 'TREE_TABLE': <enum ATSPI_ROLE_TREE_TABLE of type Atspi.Role>, 'UNKNOWN': <enum ATSPI_ROLE_UNKNOWN of type Atspi.Role>, 'VIEWPORT': <enum ATSPI_ROLE_VIEWPORT of type Atspi.Role>, 'WINDOW': <enum ATSPI_ROLE_WINDOW of type Atspi.Role>, 'EXTENDED': <enum ATSPI_ROLE_EXTENDED of type Atspi.Role>, 'HEADER': <enum ATSPI_ROLE_HEADER of type Atspi.Role>, 'FOOTER': <enum ATSPI_ROLE_FOOTER of type Atspi.Role>, 'PARAGRAPH': <enum ATSPI_ROLE_PARAGRAPH of type Atspi.Role>, 'RULER': <enum ATSPI_ROLE_RULER of type Atspi.Role>, 'APPLICATION': <enum ATSPI_ROLE_APPLICATION of type Atspi.Role>, 'AUTOCOMPLETE': <enum ATSPI_ROLE_AUTOCOMPLETE of type Atspi.Role>, 'EDITBAR': <enum ATSPI_ROLE_EDITBAR of type Atspi.Role>, 'EMBEDDED': <enum ATSPI_ROLE_EMBEDDED of type Atspi.Role>, 'ENTRY': <enum ATSPI_ROLE_ENTRY of type Atspi.Role>, 'CHART': <enum ATSPI_ROLE_CHART of type Atspi.Role>, 'CAPTION': <enum ATSPI_ROLE_CAPTION of type Atspi.Role>, 'DOCUMENT_FRAME': <enum ATSPI_ROLE_DOCUMENT_FRAME of type Atspi.Role>, 'HEADING': <enum ATSPI_ROLE_HEADING of type Atspi.Role>, 'PAGE': <enum ATSPI_ROLE_PAGE of type Atspi.Role>, 'SECTION': <enum ATSPI_ROLE_SECTION of type Atspi.Role>, 'REDUNDANT_OBJECT': <enum ATSPI_ROLE_REDUNDANT_OBJECT of type Atspi.Role>, 'FORM': <enum ATSPI_ROLE_FORM of type Atspi.Role>, 'LINK': <enum ATSPI_ROLE_LINK of type Atspi.Role>, 'INPUT_METHOD_WINDOW': <enum ATSPI_ROLE_INPUT_METHOD_WINDOW of type Atspi.Role>, 'TABLE_ROW': <enum ATSPI_ROLE_TABLE_ROW of type Atspi.Role>, 'TREE_ITEM': <enum ATSPI_ROLE_TREE_ITEM of type Atspi.Role>, 'DOCUMENT_SPREADSHEET': <enum ATSPI_ROLE_DOCUMENT_SPREADSHEET of type Atspi.Role>, 'DOCUMENT_PRESENTATION': <enum ATSPI_ROLE_DOCUMENT_PRESENTATION of type Atspi.Role>, 'DOCUMENT_TEXT': <enum ATSPI_ROLE_DOCUMENT_TEXT of type Atspi.Role>, 'DOCUMENT_WEB': <enum ATSPI_ROLE_DOCUMENT_WEB of type Atspi.Role>, 'DOCUMENT_EMAIL': <enum ATSPI_ROLE_DOCUMENT_EMAIL of type Atspi.Role>, 'COMMENT': <enum ATSPI_ROLE_COMMENT of type Atspi.Role>, 'LIST_BOX': <enum ATSPI_ROLE_LIST_BOX of type Atspi.Role>, 'GROUPING': <enum ATSPI_ROLE_GROUPING of type Atspi.Role>, 'IMAGE_MAP': <enum ATSPI_ROLE_IMAGE_MAP of type Atspi.Role>, 'NOTIFICATION': <enum ATSPI_ROLE_NOTIFICATION of type Atspi.Role>, 'INFO_BAR': <enum ATSPI_ROLE_INFO_BAR of type Atspi.Role>, 'LEVEL_BAR': <enum ATSPI_ROLE_LEVEL_BAR of type Atspi.Role>, 'TITLE_BAR': <enum ATSPI_ROLE_TITLE_BAR of type Atspi.Role>, 'BLOCK_QUOTE': <enum ATSPI_ROLE_BLOCK_QUOTE of type Atspi.Role>, 'AUDIO': <enum ATSPI_ROLE_AUDIO of type Atspi.Role>, 'VIDEO': <enum ATSPI_ROLE_VIDEO of type Atspi.Role>, 'DEFINITION': <enum ATSPI_ROLE_DEFINITION of type Atspi.Role>, 'ARTICLE': <enum ATSPI_ROLE_ARTICLE of type Atspi.Role>, 'LANDMARK': <enum ATSPI_ROLE_LANDMARK of type Atspi.Role>, 'LOG': <enum ATSPI_ROLE_LOG of type Atspi.Role>, 'MARQUEE': <enum ATSPI_ROLE_MARQUEE of type Atspi.Role>, 'MATH': <enum ATSPI_ROLE_MATH of type Atspi.Role>, 'RATING': <enum ATSPI_ROLE_RATING of type Atspi.Role>, 'TIMER': <enum ATSPI_ROLE_TIMER of type Atspi.Role>, 'STATIC': <enum ATSPI_ROLE_STATIC of type Atspi.Role>, 'MATH_FRACTION': <enum ATSPI_ROLE_MATH_FRACTION of type Atspi.Role>, 'MATH_ROOT': <enum ATSPI_ROLE_MATH_ROOT of type Atspi.Role>, 'SUBSCRIPT': <enum ATSPI_ROLE_SUBSCRIPT of type Atspi.Role>, 'SUPERSCRIPT': <enum ATSPI_ROLE_SUPERSCRIPT of type Atspi.Role>, 'DESCRIPTION_LIST': <enum ATSPI_ROLE_DESCRIPTION_LIST of type Atspi.Role>, 'DESCRIPTION_TERM': <enum ATSPI_ROLE_DESCRIPTION_TERM of type Atspi.Role>, 'DESCRIPTION_VALUE': <enum ATSPI_ROLE_DESCRIPTION_VALUE of type Atspi.Role>, 'FOOTNOTE': <enum ATSPI_ROLE_FOOTNOTE of type Atspi.Role>, 'CONTENT_DELETION': <enum ATSPI_ROLE_CONTENT_DELETION of type Atspi.Role>, 'CONTENT_INSERTION': <enum ATSPI_ROLE_CONTENT_INSERTION of type Atspi.Role>, 'MARK': <enum ATSPI_ROLE_MARK of type Atspi.Role>, 'SUGGESTION': <enum ATSPI_ROLE_SUGGESTION of type Atspi.Role>, 'LAST_DEFINED': <enum ATSPI_ROLE_LAST_DEFINED of type Atspi.Role>, 'get_name': gi.FunctionInfo(get_name)})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        44: 44,
        45: 45,
        46: 46,
        47: 47,
        48: 48,
        49: 49,
        50: 50,
        51: 51,
        52: 52,
        53: 53,
        54: 54,
        55: 55,
        56: 56,
        57: 57,
        58: 58,
        59: 59,
        60: 60,
        61: 61,
        62: 62,
        63: 63,
        64: 64,
        65: 65,
        66: 66,
        67: 67,
        68: 68,
        69: 69,
        70: 70,
        71: 71,
        72: 72,
        73: 73,
        74: 74,
        75: 75,
        76: 76,
        77: 77,
        78: 78,
        79: 79,
        80: 80,
        81: 81,
        82: 82,
        83: 83,
        84: 84,
        85: 85,
        86: 86,
        87: 87,
        88: 88,
        89: 89,
        90: 90,
        91: 91,
        92: 92,
        93: 93,
        94: 94,
        95: 95,
        96: 96,
        97: 97,
        98: 98,
        99: 99,
        100: 100,
        101: 101,
        102: 102,
        103: 103,
        104: 104,
        105: 105,
        106: 106,
        107: 107,
        108: 108,
        109: 109,
        110: 110,
        111: 111,
        112: 112,
        113: 113,
        114: 114,
        115: 115,
        116: 116,
        117: 117,
        118: 118,
        119: 119,
        120: 120,
        121: 121,
        122: 122,
        123: 123,
        124: 124,
        125: 125,
        126: 126,
        127: 127,
        128: 128,
        129: 129,
    }
    __gtype__ = None # (!) real value is '<GType AtspiRole (94141573830560)>'
    __info__ = gi.EnumInfo(Role)


