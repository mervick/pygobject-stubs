# encoding: utf-8
# module gi.repository.HarfBuzz
# from /usr/lib64/girepository-1.0/HarfBuzz-0.0.typelib
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


class aat_layout_feature_selector_t(__gobject.GEnum):
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


    ABBREV_SQUARED_LIGATURES_OFF = 15
    ABBREV_SQUARED_LIGATURES_ON = 14
    ALL_CAPS = 1
    ALL_LOWER_CASE = 2
    ALL_TYPE_FEATURES_OFF = 1
    ALL_TYPE_FEATURES_ON = 0
    ALTERNATE_HORIZ_KANA_OFF = 1
    ALTERNATE_HORIZ_KANA_ON = 0
    ALTERNATE_VERT_KANA_OFF = 3
    ALTERNATE_VERT_KANA_ON = 2
    ALT_HALF_WIDTH_TEXT = 6
    ALT_PROPORTIONAL_TEXT = 5
    ASTERISK_TO_MULTIPLY_OFF = 3
    ASTERISK_TO_MULTIPLY_ON = 2
    BOX_ANNOTATION = 1
    CANONICAL_COMPOSITION_OFF = 1
    CANONICAL_COMPOSITION_ON = 0
    CASE_SENSITIVE_LAYOUT_OFF = 1
    CASE_SENSITIVE_LAYOUT_ON = 0
    CASE_SENSITIVE_SPACING_OFF = 3
    CASE_SENSITIVE_SPACING_ON = 2
    CIRCLE_ANNOTATION = 3
    CJK_ITALIC_ROMAN = 1
    CJK_ITALIC_ROMAN_OFF = 3
    CJK_ITALIC_ROMAN_ON = 2
    CJK_SYMBOL_ALT_FIVE = 5
    CJK_SYMBOL_ALT_FOUR = 4
    CJK_SYMBOL_ALT_ONE = 1
    CJK_SYMBOL_ALT_THREE = 3
    CJK_SYMBOL_ALT_TWO = 2
    CJK_VERTICAL_ROMAN_CENTERED = 0
    CJK_VERTICAL_ROMAN_HBASELINE = 1
    COMMON_LIGATURES_OFF = 3
    COMMON_LIGATURES_ON = 2
    COMPATIBILITY_COMPOSITION_OFF = 3
    COMPATIBILITY_COMPOSITION_ON = 2
    CONTEXTUAL_ALTERNATES_OFF = 1
    CONTEXTUAL_ALTERNATES_ON = 0
    CONTEXTUAL_LIGATURES_OFF = 19
    CONTEXTUAL_LIGATURES_ON = 18
    CONTEXTUAL_SWASH_ALTERNATES_OFF = 5
    CONTEXTUAL_SWASH_ALTERNATES_ON = 4
    CURSIVE = 2
    DECOMPOSE_DIACRITICS = 2
    DECORATIVE_BORDERS = 4
    DEFAULT_CJK_ROMAN = 2
    DEFAULT_LOWER_CASE = 0
    DEFAULT_UPPER_CASE = 0
    DESIGN_LEVEL1 = 0
    DESIGN_LEVEL2 = 1
    DESIGN_LEVEL3 = 2
    DESIGN_LEVEL4 = 3
    DESIGN_LEVEL5 = 4
    DIAGONAL_FRACTIONS = 2
    DIAMOND_ANNOTATION = 8
    DINGBATS = 1
    DIPHTHONG_LIGATURES_OFF = 11
    DIPHTHONG_LIGATURES_ON = 10
    DISPLAY_TEXT = 1
    ENGRAVED_TEXT = 2
    EXPERT_CHARACTERS = 10
    EXPONENTS_OFF = 9
    EXPONENTS_ON = 8
    FLEURONS = 3
    FORM_INTERROBANG_OFF = 7
    FORM_INTERROBANG_ON = 6
    FULL_WIDTH_CJK_ROMAN = 3
    FULL_WIDTH_IDEOGRAPHS = 0
    FULL_WIDTH_KANA = 0
    HALF_WIDTH_CJK_ROMAN = 0
    HALF_WIDTH_IDEOGRAPHS = 2
    HALF_WIDTH_TEXT = 2
    HANJA_TO_HANGUL = 1
    HANJA_TO_HANGUL_ALT_ONE = 7
    HANJA_TO_HANGUL_ALT_THREE = 9
    HANJA_TO_HANGUL_ALT_TWO = 8
    HIDE_DIACRITICS = 1
    HIRAGANA_TO_KATAKANA = 2
    HISTORICAL_LIGATURES_OFF = 21
    HISTORICAL_LIGATURES_ON = 20
    HOJO_CHARACTERS = 12
    HYPHENS_TO_EM_DASH_OFF = 1
    HYPHENS_TO_EM_DASH_ON = 0
    HYPHEN_TO_EN_DASH_OFF = 3
    HYPHEN_TO_EN_DASH_ON = 2
    HYPHEN_TO_MINUS_OFF = 1
    HYPHEN_TO_MINUS_ON = 0
    IDEOGRAPHIC_ALT_FIVE = 5
    IDEOGRAPHIC_ALT_FOUR = 4
    IDEOGRAPHIC_ALT_ONE = 1
    IDEOGRAPHIC_ALT_THREE = 3
    IDEOGRAPHIC_ALT_TWO = 2
    ILLUMINATED_CAPS = 3
    INEQUALITY_LIGATURES_OFF = 7
    INEQUALITY_LIGATURES_ON = 6
    INFERIORS = 2
    INITIAL_CAPS = 4
    INITIAL_CAPS_AND_SMALL_CAPS = 5
    INTERNATIONAL_SYMBOLS = 5
    INVALID = 65535
    INVERTED_BOX_ANNOTATION = 9
    INVERTED_CIRCLE_ANNOTATION = 4
    INVERTED_ROUNDED_BOX_ANNOTATION = 10
    JIS1978_CHARACTERS = 2
    JIS1983_CHARACTERS = 3
    JIS1990_CHARACTERS = 4
    JIS2004_CHARACTERS = 11
    KANA_TO_ROMANIZATION = 4
    KATAKANA_TO_HIRAGANA = 3
    LINE_FINAL_SWASHES_OFF = 7
    LINE_FINAL_SWASHES_ON = 6
    LINE_INITIAL_SWASHES_OFF = 5
    LINE_INITIAL_SWASHES_ON = 4
    LINGUISTIC_REARRANGEMENT_OFF = 1
    LINGUISTIC_REARRANGEMENT_ON = 0
    LOGOS_OFF = 7
    LOGOS_ON = 6
    LOWER_CASE_NUMBERS = 0
    LOWER_CASE_PETITE_CAPS = 2
    LOWER_CASE_SMALL_CAPS = 1
    MATHEMATICAL_GREEK_OFF = 11
    MATHEMATICAL_GREEK_ON = 10
    MATH_SYMBOLS = 6
    MONOSPACED_NUMBERS = 0
    MONOSPACED_TEXT = 1
    NLCCHARACTERS = 13
    NON_FINAL_SWASHES_OFF = 9
    NON_FINAL_SWASHES_ON = 8
    NORMAL_POSITION = 0
    NO_ALTERNATES = 0
    NO_ANNOTATION = 0
    NO_CJK_ITALIC_ROMAN = 0
    NO_CJK_SYMBOL_ALTERNATIVES = 0
    NO_FRACTIONS = 0
    NO_IDEOGRAPHIC_ALTERNATIVES = 0
    NO_ORNAMENTS = 0
    NO_RUBY_KANA = 0
    NO_STYLE_OPTIONS = 0
    NO_STYLISTIC_ALTERNATES = 0
    NO_TRANSLITERATION = 0
    ORDINALS = 3
    PARENTHESIS_ANNOTATION = 5
    PARTIALLY_CONNECTED = 1
    PERIODS_TO_ELLIPSIS_OFF = 11
    PERIODS_TO_ELLIPSIS_ON = 10
    PERIOD_ANNOTATION = 6
    PI_CHARACTERS = 2
    PREVENT_OVERLAP_OFF = 1
    PREVENT_OVERLAP_ON = 0
    PROPORTIONAL_CJK_ROMAN = 1
    PROPORTIONAL_IDEOGRAPHS = 1
    PROPORTIONAL_KANA = 1
    PROPORTIONAL_NUMBERS = 1
    PROPORTIONAL_TEXT = 0
    QUARTER_WIDTH_NUMBERS = 3
    QUARTER_WIDTH_TEXT = 4
    RARE_LIGATURES_OFF = 5
    RARE_LIGATURES_ON = 4
    REBUS_PICTURES_OFF = 9
    REBUS_PICTURES_ON = 8
    REQUIRED_LIGATURES_OFF = 1
    REQUIRED_LIGATURES_ON = 0
    ROMANIZATION_TO_HIRAGANA = 5
    ROMANIZATION_TO_KATAKANA = 6
    ROMAN_NUMERAL_ANNOTATION = 7
    ROUNDED_BOX_ANNOTATION = 2
    RUBY_KANA = 1
    RUBY_KANA_OFF = 3
    RUBY_KANA_ON = 2
    SCIENTIFIC_INFERIORS = 4
    SHOW_DIACRITICS = 0
    SIMPLIFIED_CHARACTERS = 1
    SLASHED_ZERO_OFF = 5
    SLASHED_ZERO_ON = 4
    SLASH_TO_DIVIDE_OFF = 5
    SLASH_TO_DIVIDE_ON = 4
    SMALL_CAPS = 3
    SMART_QUOTES_OFF = 9
    SMART_QUOTES_ON = 8
    SQUARED_LIGATURES_OFF = 13
    SQUARED_LIGATURES_ON = 12
    STYLISTIC_ALT_EIGHTEEN_OFF = 37
    STYLISTIC_ALT_EIGHTEEN_ON = 36
    STYLISTIC_ALT_EIGHT_OFF = 17
    STYLISTIC_ALT_EIGHT_ON = 16
    STYLISTIC_ALT_ELEVEN_OFF = 23
    STYLISTIC_ALT_ELEVEN_ON = 22
    STYLISTIC_ALT_FIFTEEN_OFF = 31
    STYLISTIC_ALT_FIFTEEN_ON = 30
    STYLISTIC_ALT_FIVE_OFF = 11
    STYLISTIC_ALT_FIVE_ON = 10
    STYLISTIC_ALT_FOURTEEN_OFF = 29
    STYLISTIC_ALT_FOURTEEN_ON = 28
    STYLISTIC_ALT_FOUR_OFF = 9
    STYLISTIC_ALT_FOUR_ON = 8
    STYLISTIC_ALT_NINETEEN_OFF = 39
    STYLISTIC_ALT_NINETEEN_ON = 38
    STYLISTIC_ALT_NINE_OFF = 19
    STYLISTIC_ALT_NINE_ON = 18
    STYLISTIC_ALT_ONE_OFF = 3
    STYLISTIC_ALT_ONE_ON = 2
    STYLISTIC_ALT_SEVENTEEN_OFF = 35
    STYLISTIC_ALT_SEVENTEEN_ON = 34
    STYLISTIC_ALT_SEVEN_OFF = 15
    STYLISTIC_ALT_SEVEN_ON = 14
    STYLISTIC_ALT_SIXTEEN_OFF = 33
    STYLISTIC_ALT_SIXTEEN_ON = 32
    STYLISTIC_ALT_SIX_OFF = 13
    STYLISTIC_ALT_SIX_ON = 12
    STYLISTIC_ALT_TEN_OFF = 21
    STYLISTIC_ALT_TEN_ON = 20
    STYLISTIC_ALT_THIRTEEN_OFF = 27
    STYLISTIC_ALT_THIRTEEN_ON = 26
    STYLISTIC_ALT_THREE_OFF = 7
    STYLISTIC_ALT_THREE_ON = 6
    STYLISTIC_ALT_TWELVE_OFF = 25
    STYLISTIC_ALT_TWELVE_ON = 24
    STYLISTIC_ALT_TWENTY_OFF = 41
    STYLISTIC_ALT_TWENTY_ON = 40
    STYLISTIC_ALT_TWO_OFF = 5
    STYLISTIC_ALT_TWO_ON = 4
    SUBSTITUTE_VERTICAL_FORMS_OFF = 1
    SUBSTITUTE_VERTICAL_FORMS_ON = 0
    SUPERIORS = 1
    SWASH_ALTERNATES_OFF = 3
    SWASH_ALTERNATES_ON = 2
    SYMBOL_LIGATURES_OFF = 17
    SYMBOL_LIGATURES_ON = 16
    TALL_CAPS = 5
    THIRD_WIDTH_NUMBERS = 2
    THIRD_WIDTH_TEXT = 3
    TITLING_CAPS = 4
    TRADITIONAL_ALT_FIVE = 9
    TRADITIONAL_ALT_FOUR = 8
    TRADITIONAL_ALT_ONE = 5
    TRADITIONAL_ALT_THREE = 7
    TRADITIONAL_ALT_TWO = 6
    TRADITIONAL_CHARACTERS = 0
    TRADITIONAL_NAMES_CHARACTERS = 14
    TRANSCODING_COMPOSITION_OFF = 5
    TRANSCODING_COMPOSITION_ON = 4
    UNCONNECTED = 0
    UPPER_AND_LOWER_CASE = 0
    UPPER_CASE_NUMBERS = 1
    UPPER_CASE_PETITE_CAPS = 2
    UPPER_CASE_SMALL_CAPS = 1
    VERTICAL_FRACTIONS = 1
    WORD_FINAL_SWASHES_OFF = 3
    WORD_FINAL_SWASHES_ON = 2
    WORD_INITIAL_SWASHES_OFF = 1
    WORD_INITIAL_SWASHES_ON = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.HarfBuzz', '__dict__': <attribute '__dict__' of 'aat_layout_feature_selector_t' objects>, '__doc__': None, '__gtype__': <GType hb_aat_layout_feature_selector_t (94618627277792)>, '__enum_values__': {65535: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_INVALID of type HarfBuzz.aat_layout_feature_selector_t>, 0: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 1: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 2: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 3: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 4: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 5: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 6: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 7: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 8: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 9: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 10: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 11: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 12: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 13: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 14: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 15: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 16: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 17: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 18: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 19: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 20: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 21: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 22: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_ELEVEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 23: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_ELEVEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 24: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWELVE_ON of type HarfBuzz.aat_layout_feature_selector_t>, 25: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWELVE_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 26: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_THIRTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 27: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_THIRTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 28: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FOURTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 29: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FOURTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 30: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FIFTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 31: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FIFTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 32: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIXTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 33: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIXTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 34: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SEVENTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 35: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SEVENTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 36: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_EIGHTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 37: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_EIGHTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 38: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_NINETEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 39: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_NINETEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 40: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWENTY_ON of type HarfBuzz.aat_layout_feature_selector_t>, 41: <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWENTY_OFF of type HarfBuzz.aat_layout_feature_selector_t>}, '__info__': gi.EnumInfo(aat_layout_feature_selector_t), 'INVALID': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_INVALID of type HarfBuzz.aat_layout_feature_selector_t>, 'ALL_TYPE_FEATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ALL_TYPE_FEATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'REQUIRED_LIGATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'REQUIRED_LIGATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'COMMON_LIGATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'COMMON_LIGATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'RARE_LIGATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'RARE_LIGATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'LOGOS_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'LOGOS_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'REBUS_PICTURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'REBUS_PICTURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'DIPHTHONG_LIGATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'DIPHTHONG_LIGATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'SQUARED_LIGATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'SQUARED_LIGATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'ABBREV_SQUARED_LIGATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ABBREV_SQUARED_LIGATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'SYMBOL_LIGATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'SYMBOL_LIGATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'CONTEXTUAL_LIGATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CONTEXTUAL_LIGATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'HISTORICAL_LIGATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'HISTORICAL_LIGATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'UNCONNECTED': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'PARTIALLY_CONNECTED': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'CURSIVE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'UPPER_AND_LOWER_CASE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ALL_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'ALL_LOWER_CASE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'SMALL_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'INITIAL_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'INITIAL_CAPS_AND_SMALL_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'SUBSTITUTE_VERTICAL_FORMS_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'SUBSTITUTE_VERTICAL_FORMS_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'LINGUISTIC_REARRANGEMENT_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'LINGUISTIC_REARRANGEMENT_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'MONOSPACED_NUMBERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'PROPORTIONAL_NUMBERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'THIRD_WIDTH_NUMBERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'QUARTER_WIDTH_NUMBERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'WORD_INITIAL_SWASHES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'WORD_INITIAL_SWASHES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'WORD_FINAL_SWASHES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'WORD_FINAL_SWASHES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'LINE_INITIAL_SWASHES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'LINE_INITIAL_SWASHES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'LINE_FINAL_SWASHES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'LINE_FINAL_SWASHES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'NON_FINAL_SWASHES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'NON_FINAL_SWASHES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'SHOW_DIACRITICS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'HIDE_DIACRITICS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'DECOMPOSE_DIACRITICS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'NORMAL_POSITION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'SUPERIORS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'INFERIORS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ORDINALS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'SCIENTIFIC_INFERIORS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_FRACTIONS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'VERTICAL_FRACTIONS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'DIAGONAL_FRACTIONS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'PREVENT_OVERLAP_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'PREVENT_OVERLAP_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'HYPHENS_TO_EM_DASH_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'HYPHENS_TO_EM_DASH_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'HYPHEN_TO_EN_DASH_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'HYPHEN_TO_EN_DASH_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'SLASHED_ZERO_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'SLASHED_ZERO_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'FORM_INTERROBANG_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'FORM_INTERROBANG_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'SMART_QUOTES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'SMART_QUOTES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'PERIODS_TO_ELLIPSIS_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'PERIODS_TO_ELLIPSIS_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'HYPHEN_TO_MINUS_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'HYPHEN_TO_MINUS_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'ASTERISK_TO_MULTIPLY_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ASTERISK_TO_MULTIPLY_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'SLASH_TO_DIVIDE_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'SLASH_TO_DIVIDE_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'INEQUALITY_LIGATURES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'INEQUALITY_LIGATURES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'EXPONENTS_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'EXPONENTS_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'MATHEMATICAL_GREEK_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'MATHEMATICAL_GREEK_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_ORNAMENTS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'DINGBATS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'PI_CHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'FLEURONS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'DECORATIVE_BORDERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'INTERNATIONAL_SYMBOLS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'MATH_SYMBOLS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_ALTERNATES': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'DESIGN_LEVEL1': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'DESIGN_LEVEL2': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'DESIGN_LEVEL3': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'DESIGN_LEVEL4': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'DESIGN_LEVEL5': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_STYLE_OPTIONS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'DISPLAY_TEXT': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'ENGRAVED_TEXT': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ILLUMINATED_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'TITLING_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'TALL_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'TRADITIONAL_CHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'SIMPLIFIED_CHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'JIS1978_CHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'JIS1983_CHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'JIS1990_CHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'TRADITIONAL_ALT_ONE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'TRADITIONAL_ALT_TWO': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'TRADITIONAL_ALT_THREE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'TRADITIONAL_ALT_FOUR': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'TRADITIONAL_ALT_FIVE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'EXPERT_CHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'JIS2004_CHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'HOJO_CHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'NLCCHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'TRADITIONAL_NAMES_CHARACTERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'LOWER_CASE_NUMBERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'UPPER_CASE_NUMBERS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'PROPORTIONAL_TEXT': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'MONOSPACED_TEXT': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'HALF_WIDTH_TEXT': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'THIRD_WIDTH_TEXT': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'QUARTER_WIDTH_TEXT': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ALT_PROPORTIONAL_TEXT': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'ALT_HALF_WIDTH_TEXT': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_TRANSLITERATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'HANJA_TO_HANGUL': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'HIRAGANA_TO_KATAKANA': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'KATAKANA_TO_HIRAGANA': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'KANA_TO_ROMANIZATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ROMANIZATION_TO_HIRAGANA': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'ROMANIZATION_TO_KATAKANA': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'HANJA_TO_HANGUL_ALT_ONE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'HANJA_TO_HANGUL_ALT_TWO': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'HANJA_TO_HANGUL_ALT_THREE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'BOX_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'ROUNDED_BOX_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CIRCLE_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'INVERTED_CIRCLE_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'PARENTHESIS_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'PERIOD_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ROMAN_NUMERAL_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'DIAMOND_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'INVERTED_BOX_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'INVERTED_ROUNDED_BOX_ANNOTATION': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'FULL_WIDTH_KANA': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'PROPORTIONAL_KANA': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'FULL_WIDTH_IDEOGRAPHS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'PROPORTIONAL_IDEOGRAPHS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'HALF_WIDTH_IDEOGRAPHS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CANONICAL_COMPOSITION_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CANONICAL_COMPOSITION_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'COMPATIBILITY_COMPOSITION_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'COMPATIBILITY_COMPOSITION_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'TRANSCODING_COMPOSITION_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'TRANSCODING_COMPOSITION_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_RUBY_KANA': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'RUBY_KANA': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'RUBY_KANA_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'RUBY_KANA_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_CJK_SYMBOL_ALTERNATIVES': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CJK_SYMBOL_ALT_ONE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'CJK_SYMBOL_ALT_TWO': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CJK_SYMBOL_ALT_THREE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'CJK_SYMBOL_ALT_FOUR': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CJK_SYMBOL_ALT_FIVE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_IDEOGRAPHIC_ALTERNATIVES': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'IDEOGRAPHIC_ALT_ONE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'IDEOGRAPHIC_ALT_TWO': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'IDEOGRAPHIC_ALT_THREE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'IDEOGRAPHIC_ALT_FOUR': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'IDEOGRAPHIC_ALT_FIVE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'CJK_VERTICAL_ROMAN_CENTERED': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CJK_VERTICAL_ROMAN_HBASELINE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_CJK_ITALIC_ROMAN': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CJK_ITALIC_ROMAN': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'CJK_ITALIC_ROMAN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CJK_ITALIC_ROMAN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'CASE_SENSITIVE_LAYOUT_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CASE_SENSITIVE_LAYOUT_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'CASE_SENSITIVE_SPACING_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CASE_SENSITIVE_SPACING_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'ALTERNATE_HORIZ_KANA_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ALTERNATE_HORIZ_KANA_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'ALTERNATE_VERT_KANA_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'ALTERNATE_VERT_KANA_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'NO_STYLISTIC_ALTERNATES': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_ONE_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_ONE_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_TWO_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_TWO_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_THREE_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_THREE_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_FOUR_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_FOUR_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_FIVE_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_FIVE_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_SIX_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_SIX_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_SEVEN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_SEVEN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_EIGHT_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_EIGHT_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_NINE_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_NINE_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_TEN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_TEN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_ELEVEN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_ELEVEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_ELEVEN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_ELEVEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_TWELVE_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWELVE_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_TWELVE_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWELVE_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_THIRTEEN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_THIRTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_THIRTEEN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_THIRTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_FOURTEEN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FOURTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_FOURTEEN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FOURTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_FIFTEEN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FIFTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_FIFTEEN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FIFTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_SIXTEEN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIXTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_SIXTEEN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIXTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_SEVENTEEN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SEVENTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_SEVENTEEN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SEVENTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_EIGHTEEN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_EIGHTEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_EIGHTEEN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_EIGHTEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_NINETEEN_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_NINETEEN_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_NINETEEN_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_NINETEEN_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_TWENTY_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWENTY_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'STYLISTIC_ALT_TWENTY_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWENTY_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'CONTEXTUAL_ALTERNATES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CONTEXTUAL_ALTERNATES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'SWASH_ALTERNATES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'SWASH_ALTERNATES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'CONTEXTUAL_SWASH_ALTERNATES_ON': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'CONTEXTUAL_SWASH_ALTERNATES_OFF': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'DEFAULT_LOWER_CASE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'LOWER_CASE_SMALL_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'LOWER_CASE_PETITE_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'DEFAULT_UPPER_CASE': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'UPPER_CASE_SMALL_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'UPPER_CASE_PETITE_CAPS': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'HALF_WIDTH_CJK_ROMAN': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'PROPORTIONAL_CJK_ROMAN': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>, 'DEFAULT_CJK_ROMAN': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON of type HarfBuzz.aat_layout_feature_selector_t>, 'FULL_WIDTH_CJK_ROMAN': <enum HB_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF of type HarfBuzz.aat_layout_feature_selector_t>})"
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
        65535: 65535,
    }
    __gtype__ = None # (!) real value is '<GType hb_aat_layout_feature_selector_t (94618627277792)>'
    __info__ = gi.EnumInfo(aat_layout_feature_selector_t)


