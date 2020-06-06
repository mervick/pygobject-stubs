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


# Variables with simple values

BOOK_BACKEND_PROPERTY_REQUIRED_FIELDS = '"required-fields"'

BOOK_BACKEND_PROPERTY_REVISION = '"revision"'

BOOK_BACKEND_PROPERTY_SUPPORTED_FIELDS = '"supported-fields"'

EVC_ADR = 'ADR'
EVC_BDAY = 'BDAY'
EVC_CALURI = 'CALURI'
EVC_CATEGORIES = 'CATEGORIES'

EVC_CL_UID = 'X-EVOLUTION-CONTACT-LIST-UID'

EVC_CONTACT_LIST = 'X-EVOLUTION-CONTACT-LIST-INFO'

EVC_EMAIL = 'EMAIL'
EVC_ENCODING = 'ENCODING'
EVC_FBURL = 'FBURL'
EVC_FN = 'FN'
EVC_GEO = 'GEO'
EVC_ICSCALENDAR = 'ICSCALENDAR'
EVC_KEY = 'KEY'
EVC_LABEL = 'LABEL'
EVC_LOGO = 'LOGO'
EVC_MAILER = 'MAILER'
EVC_N = 'N'
EVC_NICKNAME = 'NICKNAME'
EVC_NOTE = 'NOTE'
EVC_ORG = 'ORG'

EVC_PARENT_CL = 'X-EVOLUTION-PARENT-UID'

EVC_PHOTO = 'PHOTO'
EVC_PRODID = 'PRODID'
EVC_QUOTEDPRINTABLE = 'QUOTED-PRINTABLE'
EVC_REV = 'REV'
EVC_ROLE = 'ROLE'
EVC_TEL = 'TEL'
EVC_TITLE = 'TITLE'
EVC_TYPE = 'TYPE'
EVC_UID = 'UID'
EVC_URL = 'URL'
EVC_VALUE = 'VALUE'
EVC_VERSION = 'VERSION'

EVC_X_AIM = 'X-AIM'
EVC_X_ANNIVERSARY = 'X-EVOLUTION-ANNIVERSARY'
EVC_X_ASSISTANT = 'X-EVOLUTION-ASSISTANT'
EVC_X_BIRTHDAY = 'X-EVOLUTION-BIRTHDAY'

EVC_X_BLOG_URL = 'X-EVOLUTION-BLOG-URL'

EVC_X_BOOK_UID = 'X-EVOLUTION-BOOK-UID'

EVC_X_CALLBACK = 'X-EVOLUTION-CALLBACK'
EVC_X_COMPANY = 'X-EVOLUTION-COMPANY'

EVC_X_DEST_CONTACT_UID = 'X-EVOLUTION-DEST-CONTACT-UID'

EVC_X_DEST_EMAIL = 'X-EVOLUTION-DEST-EMAIL'

EVC_X_DEST_EMAIL_NUM = 'X-EVOLUTION-DEST-EMAIL-NUM'

EVC_X_DEST_HTML_MAIL = 'X-EVOLUTION-DEST-HTML-MAIL'

EVC_X_DEST_NAME = 'X-EVOLUTION-DEST-NAME'

EVC_X_DEST_SOURCE_UID = 'X-EVOLUTION-DEST-SOURCE-UID'

EVC_X_E164 = 'X-EVOLUTION-E164'

EVC_X_FILE_AS = 'X-EVOLUTION-FILE-AS'

EVC_X_GADUGADU = 'X-GADUGADU'

EVC_X_GOOGLE_TALK = 'X-GOOGLE-TALK'

EVC_X_GROUPWISE = 'X-GROUPWISE'
EVC_X_ICQ = 'X-ICQ'
EVC_X_JABBER = 'X-JABBER'
EVC_X_LIST = 'X-EVOLUTION-LIST'

EVC_X_LIST_NAME = 'X-EVOLUTION-LIST-NAME'

EVC_X_LIST_SHOW_ADDRESSES = 'X-EVOLUTION-LIST-SHOW-ADDRESSES'

EVC_X_MANAGER = 'X-EVOLUTION-MANAGER'
EVC_X_MSN = 'X-MSN'
EVC_X_RADIO = 'X-EVOLUTION-RADIO'
EVC_X_SIP = 'X-SIP'
EVC_X_SKYPE = 'X-SKYPE'
EVC_X_SPOUSE = 'X-EVOLUTION-SPOUSE'
EVC_X_TELEX = 'X-EVOLUTION-TELEX'
EVC_X_TTYTDD = 'X-EVOLUTION-TTYTDD'
EVC_X_TWITTER = 'X-TWITTER'

EVC_X_VIDEO_URL = 'X-EVOLUTION-VIDEO-URL'

EVC_X_WANTS_HTML = 'X-MOZILLA-HTML'

EVC_X_YAHOO = 'X-YAHOO'

SOURCE_EXTENSION_BACKEND_SUMMARY_SETUP = 'Backend Summary Setup'

VCARD_21_VALID_PARAMETERS = 'TYPE,VALUE,ENCODING,CHARSET,LANGUAGE,DOM,INTL,POSTAL,PARCEL,HOME,WORK,PREF,VOICE,FAX,MSG,CELL,PAGER,BBS,MODEM,CAR,ISDN,VIDEO,AOL,APPLELINK,ATTMAIL,CIS,EWORLD,INTERNET,IBMMAIL,MCIMAIL,POWERSHARE,PRODIGY,TLX,X400,GIF,CGM,WMF,BMP,MET,PMB,DIB,PICT,TIFF,PDF,PS,JPEG,QTIME,MPEG,MPEG2,AVI,WAVE,AIFF,PCM,X509,PGP'
VCARD_21_VALID_PROPERTIES = 'ADR,ORG,N,AGENT,LOGO,PHOTO,LABEL,FN,TITLE,SOUND,VERSION,TEL,EMAIL,TZ,GEO,NOTE,URL,BDAY,ROLE,REV,UID,KEY,MAILER'

_namespace = 'EBookContacts'

_version = '1.2'

__weakref__ = None

# functions

def address_western_parse(in_address): # real signature unknown; restored from __doc__
    """ address_western_parse(in_address:str) -> EBookContacts.AddressWestern """
    pass

def book_client_error_create(code, custom_msg): # real signature unknown; restored from __doc__
    """ book_client_error_create(code:EBookContacts.BookClientError, custom_msg:str) -> error """
    pass

def book_client_error_quark(): # real signature unknown; restored from __doc__
    """ book_client_error_quark() -> int """
    return 0

def book_client_error_to_string(code): # real signature unknown; restored from __doc__
    """ book_client_error_to_string(code:EBookContacts.BookClientError) -> str """
    return ""

def book_query_and(nqs, qs, unref): # real signature unknown; restored from __doc__
    """ book_query_and(nqs:int, qs:EBookContacts.BookQuery, unref:bool) -> EBookContacts.BookQuery """
    pass

def book_query_any_field_contains(value): # real signature unknown; restored from __doc__
    """ book_query_any_field_contains(value:str) -> EBookContacts.BookQuery """
    pass

def book_query_field_exists(field): # real signature unknown; restored from __doc__
    """ book_query_field_exists(field:EBookContacts.ContactField) -> EBookContacts.BookQuery """
    pass

def book_query_field_test(field, test, value): # real signature unknown; restored from __doc__
    """ book_query_field_test(field:EBookContacts.ContactField, test:EBookContacts.BookQueryTest, value:str) -> EBookContacts.BookQuery """
    pass

def book_query_from_string(query_string): # real signature unknown; restored from __doc__
    """ book_query_from_string(query_string:str) -> EBookContacts.BookQuery """
    pass

def book_query_or(nqs, qs, unref): # real signature unknown; restored from __doc__
    """ book_query_or(nqs:int, qs:EBookContacts.BookQuery, unref:bool) -> EBookContacts.BookQuery """
    pass

def book_query_vcard_field_exists(field): # real signature unknown; restored from __doc__
    """ book_query_vcard_field_exists(field:str) -> EBookContacts.BookQuery """
    pass

def book_query_vcard_field_test(field, test, value): # real signature unknown; restored from __doc__
    """ book_query_vcard_field_test(field:str, test:EBookContacts.BookQueryTest, value:str) -> EBookContacts.BookQuery """
    pass

def book_util_conflict_resolution_to_operation_flags(conflict_resolution): # real signature unknown; restored from __doc__
    """ book_util_conflict_resolution_to_operation_flags(conflict_resolution:EDataServer.ConflictResolution) -> int """
    return 0

def book_util_operation_flags_to_conflict_resolution(flags): # real signature unknown; restored from __doc__
    """ book_util_operation_flags_to_conflict_resolution(flags:int) -> EDataServer.ConflictResolution """
    pass

def contact_attr_list_copy(p_list): # real signature unknown; restored from __doc__
    """ contact_attr_list_copy(list:list) -> list """
    return []

def contact_attr_list_free(p_list): # real signature unknown; restored from __doc__
    """ contact_attr_list_free(list:list) """
    pass

def contact_date_from_string(p_str): # real signature unknown; restored from __doc__
    """ contact_date_from_string(str:str) -> EBookContacts.ContactDate """
    pass

def contact_name_from_string(name_str): # real signature unknown; restored from __doc__
    """ contact_name_from_string(name_str:str) -> EBookContacts.ContactName """
    pass

def name_western_parse(full_name): # real signature unknown; restored from __doc__
    """ name_western_parse(full_name:str) -> EBookContacts.NameWestern """
    pass

def phone_number_compare_strings(first_number, second_number): # real signature unknown; restored from __doc__
    """ phone_number_compare_strings(first_number:str, second_number:str) -> EBookContacts.PhoneNumberMatch """
    pass

def phone_number_compare_strings_with_region(first_number, second_number, region_code=None): # real signature unknown; restored from __doc__
    """ phone_number_compare_strings_with_region(first_number:str, second_number:str, region_code:str=None) -> EBookContacts.PhoneNumberMatch """
    pass

def phone_number_error_quark(): # real signature unknown; restored from __doc__
    """ phone_number_error_quark() -> int """
    return 0

def phone_number_from_string(phone_number, region_code=None): # real signature unknown; restored from __doc__
    """ phone_number_from_string(phone_number:str, region_code:str=None) -> EBookContacts.PhoneNumber """
    pass

def phone_number_get_country_code_for_region(region_code=None): # real signature unknown; restored from __doc__
    """ phone_number_get_country_code_for_region(region_code:str=None) -> int """
    return 0

def phone_number_get_default_region(): # real signature unknown; restored from __doc__
    """ phone_number_get_default_region() -> str """
    return ""

def phone_number_is_supported(): # real signature unknown; restored from __doc__
    """ phone_number_is_supported() -> bool """
    return False

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

from .AddressWestern import AddressWestern
from .BookChange import BookChange
from .BookChangeType import BookChangeType
from .BookClientError import BookClientError
from .BookClientViewFlags import BookClientViewFlags
from .BookCursorOrigin import BookCursorOrigin
from .BookCursorSortType import BookCursorSortType
from .BookCursorStepFlags import BookCursorStepFlags
from .BookIndexType import BookIndexType
from .BookOperationFlags import BookOperationFlags
from .BookQuery import BookQuery
from .BookQueryTest import BookQueryTest
from .BookViewStatus import BookViewStatus
from .VCard import VCard
from .Contact import Contact
from .ContactAddress import ContactAddress
from .ContactAttrList import ContactAttrList
from .ContactCert import ContactCert
from .ContactClass import ContactClass
from .ContactDate import ContactDate
from .ContactField import ContactField
from .ContactGeo import ContactGeo
from .ContactName import ContactName
from .ContactPhoto import ContactPhoto
from .ContactPhotoType import ContactPhotoType
from .ContactPrivate import ContactPrivate
from .NameWestern import NameWestern
from .PhoneNumber import PhoneNumber
from .PhoneNumberCountrySource import PhoneNumberCountrySource
from .PhoneNumberError import PhoneNumberError
from .PhoneNumberFormat import PhoneNumberFormat
from .PhoneNumberMatch import PhoneNumberMatch
from .SourceBackendSummarySetup import SourceBackendSummarySetup
from .SourceBackendSummarySetupClass import SourceBackendSummarySetupClass
from .SourceBackendSummarySetupPrivate import SourceBackendSummarySetupPrivate
from .VCardAttribute import VCardAttribute
from .VCardAttributeParam import VCardAttributeParam
from .VCardClass import VCardClass
from .VCardFormat import VCardFormat
from .VCardPrivate import VCardPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f714ca22d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/EBookContacts-1.2.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.EBookContacts', loader=<gi.importer.DynamicImporter object at 0x7f714ca22d00>)"

