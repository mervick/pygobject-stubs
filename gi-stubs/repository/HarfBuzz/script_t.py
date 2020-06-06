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


class script_t(__gobject.GEnum):
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


    ADLAM = 1097100397
    AHOM = 1097363309
    ANATOLIAN_HIEROGLYPHS = 1215067511
    ARABIC = 1098015074
    ARMENIAN = 1098018158
    AVESTAN = 1098281844
    BALINESE = 1113681001
    BAMUM = 1113681269
    BASSA_VAH = 1113682803
    BATAK = 1113683051
    BENGALI = 1113943655
    BHAIKSUKI = 1114139507
    BOPOMOFO = 1114599535
    BRAHMI = 1114792296
    BRAILLE = 1114792297
    BUGINESE = 1114990441
    BUHID = 1114990692
    CANADIAN_SYLLABICS = 1130458739
    CARIAN = 1130459753
    CAUCASIAN_ALBANIAN = 1097295970
    CHAKMA = 1130457965
    CHAM = 1130914157
    CHEROKEE = 1130915186
    COMMON = 1517910393
    COPTIC = 1131376756
    CUNEIFORM = 1483961720
    CYPRIOT = 1131442804
    CYRILLIC = 1132032620
    DESERET = 1148416628
    DEVANAGARI = 1147500129
    DOGRA = 1148151666
    DUPLOYAN = 1148547180
    EGYPTIAN_HIEROGLYPHS = 1164409200
    ELBASAN = 1164730977
    ELYMAIC = 1164736877
    ETHIOPIC = 1165256809
    GEORGIAN = 1197830002
    GLAGOLITIC = 1198285159
    GOTHIC = 1198486632
    GRANTHA = 1198678382
    GREEK = 1198679403
    GUJARATI = 1198877298
    GUNJALA_GONDI = 1198485095
    GURMUKHI = 1198879349
    HAN = 1214344809
    HANGUL = 1214344807
    HANIFI_ROHINGYA = 1383032935
    HANUNOO = 1214344815
    HATRAN = 1214346354
    HEBREW = 1214603890
    HIRAGANA = 1214870113
    IMPERIAL_ARAMAIC = 1098018153
    INHERITED = 1516858984
    INSCRIPTIONAL_PAHLAVI = 1349020777
    INSCRIPTIONAL_PARTHIAN = 1349678185
    INVALID = 0
    JAVANESE = 1247901281
    KAITHI = 1265920105
    KANNADA = 1265525857
    KATAKANA = 1264676449
    KAYAH_LI = 1264675945
    KHAROSHTHI = 1265131890
    KHMER = 1265134962
    KHOJKI = 1265135466
    KHUDAWADI = 1399418468
    LAO = 1281453935
    LATIN = 1281455214
    LEPCHA = 1281716323
    LIMBU = 1281977698
    LINEAR_A = 1281977953
    LINEAR_B = 1281977954
    LISU = 1281979253
    LYCIAN = 1283023721
    LYDIAN = 1283023977
    MAHAJANI = 1298229354
    MAKASAR = 1298230113
    MALAYALAM = 1298954605
    MANDAIC = 1298230884
    MANICHAEAN = 1298230889
    MARCHEN = 1298231907
    MASARAM_GONDI = 1198485101
    MEDEFAIDRIN = 1298490470
    MEETEI_MAYEK = 1299473769
    MENDE_KIKAKUI = 1298493028
    MEROITIC_CURSIVE = 1298494051
    MEROITIC_HIEROGLYPHS = 1298494063
    MIAO = 1349284452
    MODI = 1299145833
    MONGOLIAN = 1299148391
    MRO = 1299345263
    MULTANI = 1299541108
    MYANMAR = 1299803506
    NABATAEAN = 1315070324
    NANDINAGARI = 1315008100
    NEWA = 1315272545
    NEW_TAI_LUE = 1415670901
    NKO = 1315663727
    NUSHU = 1316186229
    NYIAKENG_PUACHUE_HMONG = 1215131248
    OGHAM = 1332175213
    OLD_HUNGARIAN = 1215655527
    OLD_ITALIC = 1232363884
    OLD_NORTH_ARABIAN = 1315009122
    OLD_PERMIC = 1348825709
    OLD_PERSIAN = 1483761007
    OLD_SOGDIAN = 1399809903
    OLD_SOUTH_ARABIAN = 1398895202
    OLD_TURKIC = 1332898664
    OL_CHIKI = 1332503403
    ORIYA = 1332902241
    OSAGE = 1332963173
    OSMANYA = 1332964705
    PAHAWH_HMONG = 1215131239
    PALMYRENE = 1348562029
    PAU_CIN_HAU = 1348564323
    PHAGS_PA = 1349017959
    PHOENICIAN = 1349021304
    PSALTER_PAHLAVI = 1349020784
    REJANG = 1382706791
    RUNIC = 1383427698
    SAMARITAN = 1398893938
    SAURASHTRA = 1398895986
    SHARADA = 1399353956
    SHAVIAN = 1399349623
    SIDDHAM = 1399415908
    SIGNWRITING = 1399287415
    SINHALA = 1399418472
    SOGDIAN = 1399809892
    SORA_SOMPENG = 1399812705
    SOYOMBO = 1399814511
    SUNDANESE = 1400204900
    SYLOTI_NAGRI = 1400466543
    SYRIAC = 1400468067
    TAGALOG = 1416064103
    TAGBANWA = 1415669602
    TAI_LE = 1415670885
    TAI_THAM = 1281453665
    TAI_VIET = 1415673460
    TAKRI = 1415670642
    TAMIL = 1415671148
    TANGUT = 1415671399
    TELUGU = 1415933045
    THAANA = 1416126817
    THAI = 1416126825
    TIBETAN = 1416192628
    TIFINAGH = 1415999079
    TIRHUTA = 1416196712
    UGARITIC = 1432838514
    UNKNOWN = 1517976186
    VAI = 1449224553
    WANCHO = 1466132591
    WARANG_CITI = 1466004065
    YI = 1500080489
    ZANABAZAR_SQUARE = 1516334690
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.HarfBuzz', '__dict__': <attribute '__dict__' of 'script_t' objects>, '__doc__': None, '__gtype__': <GType hb_script_t (94618627565424)>, '__enum_values__': {1517910393: <enum HB_SCRIPT_COMMON of type HarfBuzz.script_t>, 1516858984: <enum HB_SCRIPT_INHERITED of type HarfBuzz.script_t>, 1517976186: <enum HB_SCRIPT_UNKNOWN of type HarfBuzz.script_t>, 1098015074: <enum HB_SCRIPT_ARABIC of type HarfBuzz.script_t>, 1098018158: <enum HB_SCRIPT_ARMENIAN of type HarfBuzz.script_t>, 1113943655: <enum HB_SCRIPT_BENGALI of type HarfBuzz.script_t>, 1132032620: <enum HB_SCRIPT_CYRILLIC of type HarfBuzz.script_t>, 1147500129: <enum HB_SCRIPT_DEVANAGARI of type HarfBuzz.script_t>, 1197830002: <enum HB_SCRIPT_GEORGIAN of type HarfBuzz.script_t>, 1198679403: <enum HB_SCRIPT_GREEK of type HarfBuzz.script_t>, 1198877298: <enum HB_SCRIPT_GUJARATI of type HarfBuzz.script_t>, 1198879349: <enum HB_SCRIPT_GURMUKHI of type HarfBuzz.script_t>, 1214344807: <enum HB_SCRIPT_HANGUL of type HarfBuzz.script_t>, 1214344809: <enum HB_SCRIPT_HAN of type HarfBuzz.script_t>, 1214603890: <enum HB_SCRIPT_HEBREW of type HarfBuzz.script_t>, 1214870113: <enum HB_SCRIPT_HIRAGANA of type HarfBuzz.script_t>, 1265525857: <enum HB_SCRIPT_KANNADA of type HarfBuzz.script_t>, 1264676449: <enum HB_SCRIPT_KATAKANA of type HarfBuzz.script_t>, 1281453935: <enum HB_SCRIPT_LAO of type HarfBuzz.script_t>, 1281455214: <enum HB_SCRIPT_LATIN of type HarfBuzz.script_t>, 1298954605: <enum HB_SCRIPT_MALAYALAM of type HarfBuzz.script_t>, 1332902241: <enum HB_SCRIPT_ORIYA of type HarfBuzz.script_t>, 1415671148: <enum HB_SCRIPT_TAMIL of type HarfBuzz.script_t>, 1415933045: <enum HB_SCRIPT_TELUGU of type HarfBuzz.script_t>, 1416126825: <enum HB_SCRIPT_THAI of type HarfBuzz.script_t>, 1416192628: <enum HB_SCRIPT_TIBETAN of type HarfBuzz.script_t>, 1114599535: <enum HB_SCRIPT_BOPOMOFO of type HarfBuzz.script_t>, 1114792297: <enum HB_SCRIPT_BRAILLE of type HarfBuzz.script_t>, 1130458739: <enum HB_SCRIPT_CANADIAN_SYLLABICS of type HarfBuzz.script_t>, 1130915186: <enum HB_SCRIPT_CHEROKEE of type HarfBuzz.script_t>, 1165256809: <enum HB_SCRIPT_ETHIOPIC of type HarfBuzz.script_t>, 1265134962: <enum HB_SCRIPT_KHMER of type HarfBuzz.script_t>, 1299148391: <enum HB_SCRIPT_MONGOLIAN of type HarfBuzz.script_t>, 1299803506: <enum HB_SCRIPT_MYANMAR of type HarfBuzz.script_t>, 1332175213: <enum HB_SCRIPT_OGHAM of type HarfBuzz.script_t>, 1383427698: <enum HB_SCRIPT_RUNIC of type HarfBuzz.script_t>, 1399418472: <enum HB_SCRIPT_SINHALA of type HarfBuzz.script_t>, 1400468067: <enum HB_SCRIPT_SYRIAC of type HarfBuzz.script_t>, 1416126817: <enum HB_SCRIPT_THAANA of type HarfBuzz.script_t>, 1500080489: <enum HB_SCRIPT_YI of type HarfBuzz.script_t>, 1148416628: <enum HB_SCRIPT_DESERET of type HarfBuzz.script_t>, 1198486632: <enum HB_SCRIPT_GOTHIC of type HarfBuzz.script_t>, 1232363884: <enum HB_SCRIPT_OLD_ITALIC of type HarfBuzz.script_t>, 1114990692: <enum HB_SCRIPT_BUHID of type HarfBuzz.script_t>, 1214344815: <enum HB_SCRIPT_HANUNOO of type HarfBuzz.script_t>, 1416064103: <enum HB_SCRIPT_TAGALOG of type HarfBuzz.script_t>, 1415669602: <enum HB_SCRIPT_TAGBANWA of type HarfBuzz.script_t>, 1131442804: <enum HB_SCRIPT_CYPRIOT of type HarfBuzz.script_t>, 1281977698: <enum HB_SCRIPT_LIMBU of type HarfBuzz.script_t>, 1281977954: <enum HB_SCRIPT_LINEAR_B of type HarfBuzz.script_t>, 1332964705: <enum HB_SCRIPT_OSMANYA of type HarfBuzz.script_t>, 1399349623: <enum HB_SCRIPT_SHAVIAN of type HarfBuzz.script_t>, 1415670885: <enum HB_SCRIPT_TAI_LE of type HarfBuzz.script_t>, 1432838514: <enum HB_SCRIPT_UGARITIC of type HarfBuzz.script_t>, 1114990441: <enum HB_SCRIPT_BUGINESE of type HarfBuzz.script_t>, 1131376756: <enum HB_SCRIPT_COPTIC of type HarfBuzz.script_t>, 1198285159: <enum HB_SCRIPT_GLAGOLITIC of type HarfBuzz.script_t>, 1265131890: <enum HB_SCRIPT_KHAROSHTHI of type HarfBuzz.script_t>, 1415670901: <enum HB_SCRIPT_NEW_TAI_LUE of type HarfBuzz.script_t>, 1483761007: <enum HB_SCRIPT_OLD_PERSIAN of type HarfBuzz.script_t>, 1400466543: <enum HB_SCRIPT_SYLOTI_NAGRI of type HarfBuzz.script_t>, 1415999079: <enum HB_SCRIPT_TIFINAGH of type HarfBuzz.script_t>, 1113681001: <enum HB_SCRIPT_BALINESE of type HarfBuzz.script_t>, 1483961720: <enum HB_SCRIPT_CUNEIFORM of type HarfBuzz.script_t>, 1315663727: <enum HB_SCRIPT_NKO of type HarfBuzz.script_t>, 1349017959: <enum HB_SCRIPT_PHAGS_PA of type HarfBuzz.script_t>, 1349021304: <enum HB_SCRIPT_PHOENICIAN of type HarfBuzz.script_t>, 1130459753: <enum HB_SCRIPT_CARIAN of type HarfBuzz.script_t>, 1130914157: <enum HB_SCRIPT_CHAM of type HarfBuzz.script_t>, 1264675945: <enum HB_SCRIPT_KAYAH_LI of type HarfBuzz.script_t>, 1281716323: <enum HB_SCRIPT_LEPCHA of type HarfBuzz.script_t>, 1283023721: <enum HB_SCRIPT_LYCIAN of type HarfBuzz.script_t>, 1283023977: <enum HB_SCRIPT_LYDIAN of type HarfBuzz.script_t>, 1332503403: <enum HB_SCRIPT_OL_CHIKI of type HarfBuzz.script_t>, 1382706791: <enum HB_SCRIPT_REJANG of type HarfBuzz.script_t>, 1398895986: <enum HB_SCRIPT_SAURASHTRA of type HarfBuzz.script_t>, 1400204900: <enum HB_SCRIPT_SUNDANESE of type HarfBuzz.script_t>, 1449224553: <enum HB_SCRIPT_VAI of type HarfBuzz.script_t>, 1098281844: <enum HB_SCRIPT_AVESTAN of type HarfBuzz.script_t>, 1113681269: <enum HB_SCRIPT_BAMUM of type HarfBuzz.script_t>, 1164409200: <enum HB_SCRIPT_EGYPTIAN_HIEROGLYPHS of type HarfBuzz.script_t>, 1098018153: <enum HB_SCRIPT_IMPERIAL_ARAMAIC of type HarfBuzz.script_t>, 1349020777: <enum HB_SCRIPT_INSCRIPTIONAL_PAHLAVI of type HarfBuzz.script_t>, 1349678185: <enum HB_SCRIPT_INSCRIPTIONAL_PARTHIAN of type HarfBuzz.script_t>, 1247901281: <enum HB_SCRIPT_JAVANESE of type HarfBuzz.script_t>, 1265920105: <enum HB_SCRIPT_KAITHI of type HarfBuzz.script_t>, 1281979253: <enum HB_SCRIPT_LISU of type HarfBuzz.script_t>, 1299473769: <enum HB_SCRIPT_MEETEI_MAYEK of type HarfBuzz.script_t>, 1398895202: <enum HB_SCRIPT_OLD_SOUTH_ARABIAN of type HarfBuzz.script_t>, 1332898664: <enum HB_SCRIPT_OLD_TURKIC of type HarfBuzz.script_t>, 1398893938: <enum HB_SCRIPT_SAMARITAN of type HarfBuzz.script_t>, 1281453665: <enum HB_SCRIPT_TAI_THAM of type HarfBuzz.script_t>, 1415673460: <enum HB_SCRIPT_TAI_VIET of type HarfBuzz.script_t>, 1113683051: <enum HB_SCRIPT_BATAK of type HarfBuzz.script_t>, 1114792296: <enum HB_SCRIPT_BRAHMI of type HarfBuzz.script_t>, 1298230884: <enum HB_SCRIPT_MANDAIC of type HarfBuzz.script_t>, 1130457965: <enum HB_SCRIPT_CHAKMA of type HarfBuzz.script_t>, 1298494051: <enum HB_SCRIPT_MEROITIC_CURSIVE of type HarfBuzz.script_t>, 1298494063: <enum HB_SCRIPT_MEROITIC_HIEROGLYPHS of type HarfBuzz.script_t>, 1349284452: <enum HB_SCRIPT_MIAO of type HarfBuzz.script_t>, 1399353956: <enum HB_SCRIPT_SHARADA of type HarfBuzz.script_t>, 1399812705: <enum HB_SCRIPT_SORA_SOMPENG of type HarfBuzz.script_t>, 1415670642: <enum HB_SCRIPT_TAKRI of type HarfBuzz.script_t>, 1113682803: <enum HB_SCRIPT_BASSA_VAH of type HarfBuzz.script_t>, 1097295970: <enum HB_SCRIPT_CAUCASIAN_ALBANIAN of type HarfBuzz.script_t>, 1148547180: <enum HB_SCRIPT_DUPLOYAN of type HarfBuzz.script_t>, 1164730977: <enum HB_SCRIPT_ELBASAN of type HarfBuzz.script_t>, 1198678382: <enum HB_SCRIPT_GRANTHA of type HarfBuzz.script_t>, 1265135466: <enum HB_SCRIPT_KHOJKI of type HarfBuzz.script_t>, 1399418468: <enum HB_SCRIPT_KHUDAWADI of type HarfBuzz.script_t>, 1281977953: <enum HB_SCRIPT_LINEAR_A of type HarfBuzz.script_t>, 1298229354: <enum HB_SCRIPT_MAHAJANI of type HarfBuzz.script_t>, 1298230889: <enum HB_SCRIPT_MANICHAEAN of type HarfBuzz.script_t>, 1298493028: <enum HB_SCRIPT_MENDE_KIKAKUI of type HarfBuzz.script_t>, 1299145833: <enum HB_SCRIPT_MODI of type HarfBuzz.script_t>, 1299345263: <enum HB_SCRIPT_MRO of type HarfBuzz.script_t>, 1315070324: <enum HB_SCRIPT_NABATAEAN of type HarfBuzz.script_t>, 1315009122: <enum HB_SCRIPT_OLD_NORTH_ARABIAN of type HarfBuzz.script_t>, 1348825709: <enum HB_SCRIPT_OLD_PERMIC of type HarfBuzz.script_t>, 1215131239: <enum HB_SCRIPT_PAHAWH_HMONG of type HarfBuzz.script_t>, 1348562029: <enum HB_SCRIPT_PALMYRENE of type HarfBuzz.script_t>, 1348564323: <enum HB_SCRIPT_PAU_CIN_HAU of type HarfBuzz.script_t>, 1349020784: <enum HB_SCRIPT_PSALTER_PAHLAVI of type HarfBuzz.script_t>, 1399415908: <enum HB_SCRIPT_SIDDHAM of type HarfBuzz.script_t>, 1416196712: <enum HB_SCRIPT_TIRHUTA of type HarfBuzz.script_t>, 1466004065: <enum HB_SCRIPT_WARANG_CITI of type HarfBuzz.script_t>, 1097363309: <enum HB_SCRIPT_AHOM of type HarfBuzz.script_t>, 1215067511: <enum HB_SCRIPT_ANATOLIAN_HIEROGLYPHS of type HarfBuzz.script_t>, 1214346354: <enum HB_SCRIPT_HATRAN of type HarfBuzz.script_t>, 1299541108: <enum HB_SCRIPT_MULTANI of type HarfBuzz.script_t>, 1215655527: <enum HB_SCRIPT_OLD_HUNGARIAN of type HarfBuzz.script_t>, 1399287415: <enum HB_SCRIPT_SIGNWRITING of type HarfBuzz.script_t>, 1097100397: <enum HB_SCRIPT_ADLAM of type HarfBuzz.script_t>, 1114139507: <enum HB_SCRIPT_BHAIKSUKI of type HarfBuzz.script_t>, 1298231907: <enum HB_SCRIPT_MARCHEN of type HarfBuzz.script_t>, 1332963173: <enum HB_SCRIPT_OSAGE of type HarfBuzz.script_t>, 1415671399: <enum HB_SCRIPT_TANGUT of type HarfBuzz.script_t>, 1315272545: <enum HB_SCRIPT_NEWA of type HarfBuzz.script_t>, 1198485101: <enum HB_SCRIPT_MASARAM_GONDI of type HarfBuzz.script_t>, 1316186229: <enum HB_SCRIPT_NUSHU of type HarfBuzz.script_t>, 1399814511: <enum HB_SCRIPT_SOYOMBO of type HarfBuzz.script_t>, 1516334690: <enum HB_SCRIPT_ZANABAZAR_SQUARE of type HarfBuzz.script_t>, 1148151666: <enum HB_SCRIPT_DOGRA of type HarfBuzz.script_t>, 1198485095: <enum HB_SCRIPT_GUNJALA_GONDI of type HarfBuzz.script_t>, 1383032935: <enum HB_SCRIPT_HANIFI_ROHINGYA of type HarfBuzz.script_t>, 1298230113: <enum HB_SCRIPT_MAKASAR of type HarfBuzz.script_t>, 1298490470: <enum HB_SCRIPT_MEDEFAIDRIN of type HarfBuzz.script_t>, 1399809903: <enum HB_SCRIPT_OLD_SOGDIAN of type HarfBuzz.script_t>, 1399809892: <enum HB_SCRIPT_SOGDIAN of type HarfBuzz.script_t>, 1164736877: <enum HB_SCRIPT_ELYMAIC of type HarfBuzz.script_t>, 1315008100: <enum HB_SCRIPT_NANDINAGARI of type HarfBuzz.script_t>, 1215131248: <enum HB_SCRIPT_NYIAKENG_PUACHUE_HMONG of type HarfBuzz.script_t>, 1466132591: <enum HB_SCRIPT_WANCHO of type HarfBuzz.script_t>, 0: <enum HB_SCRIPT_INVALID of type HarfBuzz.script_t>}, '__info__': gi.EnumInfo(script_t), 'COMMON': <enum HB_SCRIPT_COMMON of type HarfBuzz.script_t>, 'INHERITED': <enum HB_SCRIPT_INHERITED of type HarfBuzz.script_t>, 'UNKNOWN': <enum HB_SCRIPT_UNKNOWN of type HarfBuzz.script_t>, 'ARABIC': <enum HB_SCRIPT_ARABIC of type HarfBuzz.script_t>, 'ARMENIAN': <enum HB_SCRIPT_ARMENIAN of type HarfBuzz.script_t>, 'BENGALI': <enum HB_SCRIPT_BENGALI of type HarfBuzz.script_t>, 'CYRILLIC': <enum HB_SCRIPT_CYRILLIC of type HarfBuzz.script_t>, 'DEVANAGARI': <enum HB_SCRIPT_DEVANAGARI of type HarfBuzz.script_t>, 'GEORGIAN': <enum HB_SCRIPT_GEORGIAN of type HarfBuzz.script_t>, 'GREEK': <enum HB_SCRIPT_GREEK of type HarfBuzz.script_t>, 'GUJARATI': <enum HB_SCRIPT_GUJARATI of type HarfBuzz.script_t>, 'GURMUKHI': <enum HB_SCRIPT_GURMUKHI of type HarfBuzz.script_t>, 'HANGUL': <enum HB_SCRIPT_HANGUL of type HarfBuzz.script_t>, 'HAN': <enum HB_SCRIPT_HAN of type HarfBuzz.script_t>, 'HEBREW': <enum HB_SCRIPT_HEBREW of type HarfBuzz.script_t>, 'HIRAGANA': <enum HB_SCRIPT_HIRAGANA of type HarfBuzz.script_t>, 'KANNADA': <enum HB_SCRIPT_KANNADA of type HarfBuzz.script_t>, 'KATAKANA': <enum HB_SCRIPT_KATAKANA of type HarfBuzz.script_t>, 'LAO': <enum HB_SCRIPT_LAO of type HarfBuzz.script_t>, 'LATIN': <enum HB_SCRIPT_LATIN of type HarfBuzz.script_t>, 'MALAYALAM': <enum HB_SCRIPT_MALAYALAM of type HarfBuzz.script_t>, 'ORIYA': <enum HB_SCRIPT_ORIYA of type HarfBuzz.script_t>, 'TAMIL': <enum HB_SCRIPT_TAMIL of type HarfBuzz.script_t>, 'TELUGU': <enum HB_SCRIPT_TELUGU of type HarfBuzz.script_t>, 'THAI': <enum HB_SCRIPT_THAI of type HarfBuzz.script_t>, 'TIBETAN': <enum HB_SCRIPT_TIBETAN of type HarfBuzz.script_t>, 'BOPOMOFO': <enum HB_SCRIPT_BOPOMOFO of type HarfBuzz.script_t>, 'BRAILLE': <enum HB_SCRIPT_BRAILLE of type HarfBuzz.script_t>, 'CANADIAN_SYLLABICS': <enum HB_SCRIPT_CANADIAN_SYLLABICS of type HarfBuzz.script_t>, 'CHEROKEE': <enum HB_SCRIPT_CHEROKEE of type HarfBuzz.script_t>, 'ETHIOPIC': <enum HB_SCRIPT_ETHIOPIC of type HarfBuzz.script_t>, 'KHMER': <enum HB_SCRIPT_KHMER of type HarfBuzz.script_t>, 'MONGOLIAN': <enum HB_SCRIPT_MONGOLIAN of type HarfBuzz.script_t>, 'MYANMAR': <enum HB_SCRIPT_MYANMAR of type HarfBuzz.script_t>, 'OGHAM': <enum HB_SCRIPT_OGHAM of type HarfBuzz.script_t>, 'RUNIC': <enum HB_SCRIPT_RUNIC of type HarfBuzz.script_t>, 'SINHALA': <enum HB_SCRIPT_SINHALA of type HarfBuzz.script_t>, 'SYRIAC': <enum HB_SCRIPT_SYRIAC of type HarfBuzz.script_t>, 'THAANA': <enum HB_SCRIPT_THAANA of type HarfBuzz.script_t>, 'YI': <enum HB_SCRIPT_YI of type HarfBuzz.script_t>, 'DESERET': <enum HB_SCRIPT_DESERET of type HarfBuzz.script_t>, 'GOTHIC': <enum HB_SCRIPT_GOTHIC of type HarfBuzz.script_t>, 'OLD_ITALIC': <enum HB_SCRIPT_OLD_ITALIC of type HarfBuzz.script_t>, 'BUHID': <enum HB_SCRIPT_BUHID of type HarfBuzz.script_t>, 'HANUNOO': <enum HB_SCRIPT_HANUNOO of type HarfBuzz.script_t>, 'TAGALOG': <enum HB_SCRIPT_TAGALOG of type HarfBuzz.script_t>, 'TAGBANWA': <enum HB_SCRIPT_TAGBANWA of type HarfBuzz.script_t>, 'CYPRIOT': <enum HB_SCRIPT_CYPRIOT of type HarfBuzz.script_t>, 'LIMBU': <enum HB_SCRIPT_LIMBU of type HarfBuzz.script_t>, 'LINEAR_B': <enum HB_SCRIPT_LINEAR_B of type HarfBuzz.script_t>, 'OSMANYA': <enum HB_SCRIPT_OSMANYA of type HarfBuzz.script_t>, 'SHAVIAN': <enum HB_SCRIPT_SHAVIAN of type HarfBuzz.script_t>, 'TAI_LE': <enum HB_SCRIPT_TAI_LE of type HarfBuzz.script_t>, 'UGARITIC': <enum HB_SCRIPT_UGARITIC of type HarfBuzz.script_t>, 'BUGINESE': <enum HB_SCRIPT_BUGINESE of type HarfBuzz.script_t>, 'COPTIC': <enum HB_SCRIPT_COPTIC of type HarfBuzz.script_t>, 'GLAGOLITIC': <enum HB_SCRIPT_GLAGOLITIC of type HarfBuzz.script_t>, 'KHAROSHTHI': <enum HB_SCRIPT_KHAROSHTHI of type HarfBuzz.script_t>, 'NEW_TAI_LUE': <enum HB_SCRIPT_NEW_TAI_LUE of type HarfBuzz.script_t>, 'OLD_PERSIAN': <enum HB_SCRIPT_OLD_PERSIAN of type HarfBuzz.script_t>, 'SYLOTI_NAGRI': <enum HB_SCRIPT_SYLOTI_NAGRI of type HarfBuzz.script_t>, 'TIFINAGH': <enum HB_SCRIPT_TIFINAGH of type HarfBuzz.script_t>, 'BALINESE': <enum HB_SCRIPT_BALINESE of type HarfBuzz.script_t>, 'CUNEIFORM': <enum HB_SCRIPT_CUNEIFORM of type HarfBuzz.script_t>, 'NKO': <enum HB_SCRIPT_NKO of type HarfBuzz.script_t>, 'PHAGS_PA': <enum HB_SCRIPT_PHAGS_PA of type HarfBuzz.script_t>, 'PHOENICIAN': <enum HB_SCRIPT_PHOENICIAN of type HarfBuzz.script_t>, 'CARIAN': <enum HB_SCRIPT_CARIAN of type HarfBuzz.script_t>, 'CHAM': <enum HB_SCRIPT_CHAM of type HarfBuzz.script_t>, 'KAYAH_LI': <enum HB_SCRIPT_KAYAH_LI of type HarfBuzz.script_t>, 'LEPCHA': <enum HB_SCRIPT_LEPCHA of type HarfBuzz.script_t>, 'LYCIAN': <enum HB_SCRIPT_LYCIAN of type HarfBuzz.script_t>, 'LYDIAN': <enum HB_SCRIPT_LYDIAN of type HarfBuzz.script_t>, 'OL_CHIKI': <enum HB_SCRIPT_OL_CHIKI of type HarfBuzz.script_t>, 'REJANG': <enum HB_SCRIPT_REJANG of type HarfBuzz.script_t>, 'SAURASHTRA': <enum HB_SCRIPT_SAURASHTRA of type HarfBuzz.script_t>, 'SUNDANESE': <enum HB_SCRIPT_SUNDANESE of type HarfBuzz.script_t>, 'VAI': <enum HB_SCRIPT_VAI of type HarfBuzz.script_t>, 'AVESTAN': <enum HB_SCRIPT_AVESTAN of type HarfBuzz.script_t>, 'BAMUM': <enum HB_SCRIPT_BAMUM of type HarfBuzz.script_t>, 'EGYPTIAN_HIEROGLYPHS': <enum HB_SCRIPT_EGYPTIAN_HIEROGLYPHS of type HarfBuzz.script_t>, 'IMPERIAL_ARAMAIC': <enum HB_SCRIPT_IMPERIAL_ARAMAIC of type HarfBuzz.script_t>, 'INSCRIPTIONAL_PAHLAVI': <enum HB_SCRIPT_INSCRIPTIONAL_PAHLAVI of type HarfBuzz.script_t>, 'INSCRIPTIONAL_PARTHIAN': <enum HB_SCRIPT_INSCRIPTIONAL_PARTHIAN of type HarfBuzz.script_t>, 'JAVANESE': <enum HB_SCRIPT_JAVANESE of type HarfBuzz.script_t>, 'KAITHI': <enum HB_SCRIPT_KAITHI of type HarfBuzz.script_t>, 'LISU': <enum HB_SCRIPT_LISU of type HarfBuzz.script_t>, 'MEETEI_MAYEK': <enum HB_SCRIPT_MEETEI_MAYEK of type HarfBuzz.script_t>, 'OLD_SOUTH_ARABIAN': <enum HB_SCRIPT_OLD_SOUTH_ARABIAN of type HarfBuzz.script_t>, 'OLD_TURKIC': <enum HB_SCRIPT_OLD_TURKIC of type HarfBuzz.script_t>, 'SAMARITAN': <enum HB_SCRIPT_SAMARITAN of type HarfBuzz.script_t>, 'TAI_THAM': <enum HB_SCRIPT_TAI_THAM of type HarfBuzz.script_t>, 'TAI_VIET': <enum HB_SCRIPT_TAI_VIET of type HarfBuzz.script_t>, 'BATAK': <enum HB_SCRIPT_BATAK of type HarfBuzz.script_t>, 'BRAHMI': <enum HB_SCRIPT_BRAHMI of type HarfBuzz.script_t>, 'MANDAIC': <enum HB_SCRIPT_MANDAIC of type HarfBuzz.script_t>, 'CHAKMA': <enum HB_SCRIPT_CHAKMA of type HarfBuzz.script_t>, 'MEROITIC_CURSIVE': <enum HB_SCRIPT_MEROITIC_CURSIVE of type HarfBuzz.script_t>, 'MEROITIC_HIEROGLYPHS': <enum HB_SCRIPT_MEROITIC_HIEROGLYPHS of type HarfBuzz.script_t>, 'MIAO': <enum HB_SCRIPT_MIAO of type HarfBuzz.script_t>, 'SHARADA': <enum HB_SCRIPT_SHARADA of type HarfBuzz.script_t>, 'SORA_SOMPENG': <enum HB_SCRIPT_SORA_SOMPENG of type HarfBuzz.script_t>, 'TAKRI': <enum HB_SCRIPT_TAKRI of type HarfBuzz.script_t>, 'BASSA_VAH': <enum HB_SCRIPT_BASSA_VAH of type HarfBuzz.script_t>, 'CAUCASIAN_ALBANIAN': <enum HB_SCRIPT_CAUCASIAN_ALBANIAN of type HarfBuzz.script_t>, 'DUPLOYAN': <enum HB_SCRIPT_DUPLOYAN of type HarfBuzz.script_t>, 'ELBASAN': <enum HB_SCRIPT_ELBASAN of type HarfBuzz.script_t>, 'GRANTHA': <enum HB_SCRIPT_GRANTHA of type HarfBuzz.script_t>, 'KHOJKI': <enum HB_SCRIPT_KHOJKI of type HarfBuzz.script_t>, 'KHUDAWADI': <enum HB_SCRIPT_KHUDAWADI of type HarfBuzz.script_t>, 'LINEAR_A': <enum HB_SCRIPT_LINEAR_A of type HarfBuzz.script_t>, 'MAHAJANI': <enum HB_SCRIPT_MAHAJANI of type HarfBuzz.script_t>, 'MANICHAEAN': <enum HB_SCRIPT_MANICHAEAN of type HarfBuzz.script_t>, 'MENDE_KIKAKUI': <enum HB_SCRIPT_MENDE_KIKAKUI of type HarfBuzz.script_t>, 'MODI': <enum HB_SCRIPT_MODI of type HarfBuzz.script_t>, 'MRO': <enum HB_SCRIPT_MRO of type HarfBuzz.script_t>, 'NABATAEAN': <enum HB_SCRIPT_NABATAEAN of type HarfBuzz.script_t>, 'OLD_NORTH_ARABIAN': <enum HB_SCRIPT_OLD_NORTH_ARABIAN of type HarfBuzz.script_t>, 'OLD_PERMIC': <enum HB_SCRIPT_OLD_PERMIC of type HarfBuzz.script_t>, 'PAHAWH_HMONG': <enum HB_SCRIPT_PAHAWH_HMONG of type HarfBuzz.script_t>, 'PALMYRENE': <enum HB_SCRIPT_PALMYRENE of type HarfBuzz.script_t>, 'PAU_CIN_HAU': <enum HB_SCRIPT_PAU_CIN_HAU of type HarfBuzz.script_t>, 'PSALTER_PAHLAVI': <enum HB_SCRIPT_PSALTER_PAHLAVI of type HarfBuzz.script_t>, 'SIDDHAM': <enum HB_SCRIPT_SIDDHAM of type HarfBuzz.script_t>, 'TIRHUTA': <enum HB_SCRIPT_TIRHUTA of type HarfBuzz.script_t>, 'WARANG_CITI': <enum HB_SCRIPT_WARANG_CITI of type HarfBuzz.script_t>, 'AHOM': <enum HB_SCRIPT_AHOM of type HarfBuzz.script_t>, 'ANATOLIAN_HIEROGLYPHS': <enum HB_SCRIPT_ANATOLIAN_HIEROGLYPHS of type HarfBuzz.script_t>, 'HATRAN': <enum HB_SCRIPT_HATRAN of type HarfBuzz.script_t>, 'MULTANI': <enum HB_SCRIPT_MULTANI of type HarfBuzz.script_t>, 'OLD_HUNGARIAN': <enum HB_SCRIPT_OLD_HUNGARIAN of type HarfBuzz.script_t>, 'SIGNWRITING': <enum HB_SCRIPT_SIGNWRITING of type HarfBuzz.script_t>, 'ADLAM': <enum HB_SCRIPT_ADLAM of type HarfBuzz.script_t>, 'BHAIKSUKI': <enum HB_SCRIPT_BHAIKSUKI of type HarfBuzz.script_t>, 'MARCHEN': <enum HB_SCRIPT_MARCHEN of type HarfBuzz.script_t>, 'OSAGE': <enum HB_SCRIPT_OSAGE of type HarfBuzz.script_t>, 'TANGUT': <enum HB_SCRIPT_TANGUT of type HarfBuzz.script_t>, 'NEWA': <enum HB_SCRIPT_NEWA of type HarfBuzz.script_t>, 'MASARAM_GONDI': <enum HB_SCRIPT_MASARAM_GONDI of type HarfBuzz.script_t>, 'NUSHU': <enum HB_SCRIPT_NUSHU of type HarfBuzz.script_t>, 'SOYOMBO': <enum HB_SCRIPT_SOYOMBO of type HarfBuzz.script_t>, 'ZANABAZAR_SQUARE': <enum HB_SCRIPT_ZANABAZAR_SQUARE of type HarfBuzz.script_t>, 'DOGRA': <enum HB_SCRIPT_DOGRA of type HarfBuzz.script_t>, 'GUNJALA_GONDI': <enum HB_SCRIPT_GUNJALA_GONDI of type HarfBuzz.script_t>, 'HANIFI_ROHINGYA': <enum HB_SCRIPT_HANIFI_ROHINGYA of type HarfBuzz.script_t>, 'MAKASAR': <enum HB_SCRIPT_MAKASAR of type HarfBuzz.script_t>, 'MEDEFAIDRIN': <enum HB_SCRIPT_MEDEFAIDRIN of type HarfBuzz.script_t>, 'OLD_SOGDIAN': <enum HB_SCRIPT_OLD_SOGDIAN of type HarfBuzz.script_t>, 'SOGDIAN': <enum HB_SCRIPT_SOGDIAN of type HarfBuzz.script_t>, 'ELYMAIC': <enum HB_SCRIPT_ELYMAIC of type HarfBuzz.script_t>, 'NANDINAGARI': <enum HB_SCRIPT_NANDINAGARI of type HarfBuzz.script_t>, 'NYIAKENG_PUACHUE_HMONG': <enum HB_SCRIPT_NYIAKENG_PUACHUE_HMONG of type HarfBuzz.script_t>, 'WANCHO': <enum HB_SCRIPT_WANCHO of type HarfBuzz.script_t>, 'INVALID': <enum HB_SCRIPT_INVALID of type HarfBuzz.script_t>})"
    __enum_values__ = {
        0: 0,
        1097100397: 1097100397,
        1097295970: 1097295970,
        1097363309: 1097363309,
        1098015074: 1098015074,
        1098018153: 1098018153,
        1098018158: 1098018158,
        1098281844: 1098281844,
        1113681001: 1113681001,
        1113681269: 1113681269,
        1113682803: 1113682803,
        1113683051: 1113683051,
        1113943655: 1113943655,
        1114139507: 1114139507,
        1114599535: 1114599535,
        1114792296: 1114792296,
        1114792297: 1114792297,
        1114990441: 1114990441,
        1114990692: 1114990692,
        1130457965: 1130457965,
        1130458739: 1130458739,
        1130459753: 1130459753,
        1130914157: 1130914157,
        1130915186: 1130915186,
        1131376756: 1131376756,
        1131442804: 1131442804,
        1132032620: 1132032620,
        1147500129: 1147500129,
        1148151666: 1148151666,
        1148416628: 1148416628,
        1148547180: 1148547180,
        1164409200: 1164409200,
        1164730977: 1164730977,
        1164736877: 1164736877,
        1165256809: 1165256809,
        1197830002: 1197830002,
        1198285159: 1198285159,
        1198485095: 1198485095,
        1198485101: 1198485101,
        1198486632: 1198486632,
        1198678382: 1198678382,
        1198679403: 1198679403,
        1198877298: 1198877298,
        1198879349: 1198879349,
        1214344807: 1214344807,
        1214344809: 1214344809,
        1214344815: 1214344815,
        1214346354: 1214346354,
        1214603890: 1214603890,
        1214870113: 1214870113,
        1215067511: 1215067511,
        1215131239: 1215131239,
        1215131248: 1215131248,
        1215655527: 1215655527,
        1232363884: 1232363884,
        1247901281: 1247901281,
        1264675945: 1264675945,
        1264676449: 1264676449,
        1265131890: 1265131890,
        1265134962: 1265134962,
        1265135466: 1265135466,
        1265525857: 1265525857,
        1265920105: 1265920105,
        1281453665: 1281453665,
        1281453935: 1281453935,
        1281455214: 1281455214,
        1281716323: 1281716323,
        1281977698: 1281977698,
        1281977953: 1281977953,
        1281977954: 1281977954,
        1281979253: 1281979253,
        1283023721: 1283023721,
        1283023977: 1283023977,
        1298229354: 1298229354,
        1298230113: 1298230113,
        1298230884: 1298230884,
        1298230889: 1298230889,
        1298231907: 1298231907,
        1298490470: 1298490470,
        1298493028: 1298493028,
        1298494051: 1298494051,
        1298494063: 1298494063,
        1298954605: 1298954605,
        1299145833: 1299145833,
        1299148391: 1299148391,
        1299345263: 1299345263,
        1299473769: 1299473769,
        1299541108: 1299541108,
        1299803506: 1299803506,
        1315008100: 1315008100,
        1315009122: 1315009122,
        1315070324: 1315070324,
        1315272545: 1315272545,
        1315663727: 1315663727,
        1316186229: 1316186229,
        1332175213: 1332175213,
        1332503403: 1332503403,
        1332898664: 1332898664,
        1332902241: 1332902241,
        1332963173: 1332963173,
        1332964705: 1332964705,
        1348562029: 1348562029,
        1348564323: 1348564323,
        1348825709: 1348825709,
        1349017959: 1349017959,
        1349020777: 1349020777,
        1349020784: 1349020784,
        1349021304: 1349021304,
        1349284452: 1349284452,
        1349678185: 1349678185,
        1382706791: 1382706791,
        1383032935: 1383032935,
        1383427698: 1383427698,
        1398893938: 1398893938,
        1398895202: 1398895202,
        1398895986: 1398895986,
        1399287415: 1399287415,
        1399349623: 1399349623,
        1399353956: 1399353956,
        1399415908: 1399415908,
        1399418468: 1399418468,
        1399418472: 1399418472,
        1399809892: 1399809892,
        1399809903: 1399809903,
        1399812705: 1399812705,
        1399814511: 1399814511,
        1400204900: 1400204900,
        1400466543: 1400466543,
        1400468067: 1400468067,
        1415669602: 1415669602,
        1415670642: 1415670642,
        1415670885: 1415670885,
        1415670901: 1415670901,
        1415671148: 1415671148,
        1415671399: 1415671399,
        1415673460: 1415673460,
        1415933045: 1415933045,
        1415999079: 1415999079,
        1416064103: 1416064103,
        1416126817: 1416126817,
        1416126825: 1416126825,
        1416192628: 1416192628,
        1416196712: 1416196712,
        1432838514: 1432838514,
        1449224553: 1449224553,
        1466004065: 1466004065,
        1466132591: 1466132591,
        1483761007: 1483761007,
        1483961720: 1483961720,
        1500080489: 1500080489,
        1516334690: 1516334690,
        1516858984: 1516858984,
        1517910393: 1517910393,
        1517976186: 1517976186,
    }
    __gtype__ = None # (!) real value is '<GType hb_script_t (94618627565424)>'
    __info__ = gi.EnumInfo(script_t)


