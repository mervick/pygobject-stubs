# encoding: utf-8
# module gi.repository.GData
# from /usr/lib64/girepository-1.0/GData-0.0.typelib
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


# Variables with simple values

ACCESS_ROLE_NONE = 'none'

ACCESS_SCOPE_DEFAULT = 'default'
ACCESS_SCOPE_DOMAIN = 'domain'
ACCESS_SCOPE_USER = 'user'

CALENDAR_ACCESS_ROLE_EDITOR = 'http://schemas.google.com/gCal/2005#editor'

CALENDAR_ACCESS_ROLE_FREE_BUSY = 'http://schemas.google.com/gCal/2005#freebusy'

CALENDAR_ACCESS_ROLE_OWNER = 'http://schemas.google.com/gCal/2005#owner'
CALENDAR_ACCESS_ROLE_READ = 'http://schemas.google.com/gCal/2005#read'
CALENDAR_ACCESS_ROLE_ROOT = 'http://schemas.google.com/gCal/2005#root'

CATEGORY_SCHEMA_LABELS = 'http://schemas.google.com/g/2005/labels'

CONTACTS_GENDER_FEMALE = 'female'
CONTACTS_GENDER_MALE = 'male'

CONTACTS_GROUP_CONTACTS = 'Contacts'
CONTACTS_GROUP_COWORKERS = 'Coworkers'
CONTACTS_GROUP_FAMILY = 'Family'
CONTACTS_GROUP_FRIENDS = 'Friends'

CONTACTS_PRIORITY_HIGH = 'high'
CONTACTS_PRIORITY_LOW = 'low'
CONTACTS_PRIORITY_NORMAL = 'normal'

CONTACTS_SENSITIVITY_CONFIDENTIAL = 'confidential'
CONTACTS_SENSITIVITY_NORMAL = 'normal'
CONTACTS_SENSITIVITY_PERSONAL = 'personal'
CONTACTS_SENSITIVITY_PRIVATE = 'private'

DOCUMENTS_ACCESS_ROLE_OWNER = 'owner'
DOCUMENTS_ACCESS_ROLE_READER = 'reader'
DOCUMENTS_ACCESS_ROLE_WRITER = 'writer'

DOCUMENTS_DRAWING_JPEG = 'jpeg'
DOCUMENTS_DRAWING_PDF = 'pdf'
DOCUMENTS_DRAWING_PNG = 'png'
DOCUMENTS_DRAWING_SVG = 'svg'

DOCUMENTS_PRESENTATION_PDF = 'pdf'
DOCUMENTS_PRESENTATION_PNG = 'png'
DOCUMENTS_PRESENTATION_PPT = 'ppt'
DOCUMENTS_PRESENTATION_SWF = 'swf'
DOCUMENTS_PRESENTATION_TXT = 'txt'

DOCUMENTS_PROPERTY_VISIBILITY_PRIVATE = 'PRIVATE'
DOCUMENTS_PROPERTY_VISIBILITY_PUBLIC = 'PUBLIC'

DOCUMENTS_SPREADSHEET_CSV = 'csv'
DOCUMENTS_SPREADSHEET_HTML = 'html'
DOCUMENTS_SPREADSHEET_ODS = 'ods'
DOCUMENTS_SPREADSHEET_PDF = 'pdf'
DOCUMENTS_SPREADSHEET_TSV = 'tsv'
DOCUMENTS_SPREADSHEET_XLS = 'xls'

DOCUMENTS_TEXT_DOC = 'doc'
DOCUMENTS_TEXT_HTML = 'html'
DOCUMENTS_TEXT_JPEG = 'jpeg'
DOCUMENTS_TEXT_ODT = 'odt'
DOCUMENTS_TEXT_PDF = 'pdf'
DOCUMENTS_TEXT_PNG = 'png'
DOCUMENTS_TEXT_RTF = 'rtf'
DOCUMENTS_TEXT_TXT = 'txt'
DOCUMENTS_TEXT_ZIP = 'zip'

GCONTACT_CALENDAR_FREE_BUSY = 'free-busy'

GCONTACT_CALENDAR_HOME = 'home'
GCONTACT_CALENDAR_WORK = 'work'

GCONTACT_EVENT_ANNIVERSARY = 'anniversary'
GCONTACT_EVENT_OTHER = 'other'

GCONTACT_EXTERNAL_ID_ACCOUNT = 'account'
GCONTACT_EXTERNAL_ID_CUSTOMER = 'customer'
GCONTACT_EXTERNAL_ID_NETWORK = 'network'
GCONTACT_EXTERNAL_ID_ORGANIZATION = 'organization'

GCONTACT_JOT_HOME = 'home'
GCONTACT_JOT_KEYWORDS = 'keywords'
GCONTACT_JOT_OTHER = 'other'
GCONTACT_JOT_USER = 'user'
GCONTACT_JOT_WORK = 'work'

GCONTACT_RELATION_ASSISTANT = 'assistant'
GCONTACT_RELATION_BROTHER = 'brother'
GCONTACT_RELATION_CHILD = 'child'

GCONTACT_RELATION_DOMESTIC_PARTNER = 'domestic-partner'

GCONTACT_RELATION_FATHER = 'father'
GCONTACT_RELATION_FRIEND = 'friend'
GCONTACT_RELATION_MANAGER = 'manager'
GCONTACT_RELATION_MOTHER = 'mother'
GCONTACT_RELATION_PARENT = 'parent'
GCONTACT_RELATION_PARTNER = 'partner'
GCONTACT_RELATION_REFERRER = 'referred-by'
GCONTACT_RELATION_RELATIVE = 'relative'
GCONTACT_RELATION_SISTER = 'sister'
GCONTACT_RELATION_SPOUSE = 'spouse'

GCONTACT_WEBSITE_BLOG = 'blog'
GCONTACT_WEBSITE_FTP = 'ftp'
GCONTACT_WEBSITE_HOME = 'home'

GCONTACT_WEBSITE_HOME_PAGE = 'home-page'

GCONTACT_WEBSITE_OTHER = 'other'
GCONTACT_WEBSITE_PROFILE = 'profile'
GCONTACT_WEBSITE_WORK = 'work'

GD_ADDRESS_USAGE_GENERAL = 'http://schemas.google.com/g/2005#general'
GD_ADDRESS_USAGE_LOCAL = 'http://schemas.google.com/g/2005#local'

GD_EMAIL_ADDRESS_HOME = 'http://schemas.google.com/g/2005#home'
GD_EMAIL_ADDRESS_OTHER = 'http://schemas.google.com/g/2005#other'
GD_EMAIL_ADDRESS_WORK = 'http://schemas.google.com/g/2005#work'

GD_EVENT_STATUS_CANCELED = 'http://schemas.google.com/g/2005#event.canceled'
GD_EVENT_STATUS_CONFIRMED = 'http://schemas.google.com/g/2005#event.confirmed'
GD_EVENT_STATUS_TENTATIVE = 'http://schemas.google.com/g/2005#event.tentative'

GD_EVENT_TRANSPARENCY_OPAQUE = 'http://schemas.google.com/g/2005#event.opaque'
GD_EVENT_TRANSPARENCY_TRANSPARENT = 'http://schemas.google.com/g/2005#event.transparent'

GD_EVENT_VISIBILITY_CONFIDENTIAL = 'http://schemas.google.com/g/2005#event.confidential'
GD_EVENT_VISIBILITY_DEFAULT = 'http://schemas.google.com/g/2005#event.default'
GD_EVENT_VISIBILITY_PRIVATE = 'http://schemas.google.com/g/2005#event.private'
GD_EVENT_VISIBILITY_PUBLIC = 'http://schemas.google.com/g/2005#event.public'

GD_IM_ADDRESS_HOME = 'http://schemas.google.com/g/2005#home'
GD_IM_ADDRESS_NETMEETING = 'http://schemas.google.com/g/2005#netmeeting'
GD_IM_ADDRESS_OTHER = 'http://schemas.google.com/g/2005#other'
GD_IM_ADDRESS_WORK = 'http://schemas.google.com/g/2005#work'

GD_IM_PROTOCOL_AIM = 'http://schemas.google.com/g/2005#AIM'

GD_IM_PROTOCOL_GOOGLE_TALK = 'http://schemas.google.com/g/2005#GOOGLE_TALK'

GD_IM_PROTOCOL_ICQ = 'http://schemas.google.com/g/2005#ICQ'
GD_IM_PROTOCOL_JABBER = 'http://schemas.google.com/g/2005#JABBER'

GD_IM_PROTOCOL_LIVE_MESSENGER = 'http://schemas.google.com/g/2005#MSN'

GD_IM_PROTOCOL_QQ = 'http://schemas.google.com/g/2005#QQ'
GD_IM_PROTOCOL_SKYPE = 'http://schemas.google.com/g/2005#SKYPE'

GD_IM_PROTOCOL_YAHOO_MESSENGER = 'http://schemas.google.com/g/2005#YAHOO'

GD_MAIL_CLASS_BOTH = 'http://schemas.google.com/g/2005#both'
GD_MAIL_CLASS_LETTERS = 'http://schemas.google.com/g/2005#letters'
GD_MAIL_CLASS_NEITHER = 'http://schemas.google.com/g/2005#neither'
GD_MAIL_CLASS_PARCELS = 'http://schemas.google.com/g/2005#parcels'

GD_ORGANIZATION_OTHER = 'http://schemas.google.com/g/2005#other'
GD_ORGANIZATION_WORK = 'http://schemas.google.com/g/2005#work'

GD_PHONE_NUMBER_ASSISTANT = 'http://schemas.google.com/g/2005#assistant'
GD_PHONE_NUMBER_CALLBACK = 'http://schemas.google.com/g/2005#callback'
GD_PHONE_NUMBER_CAR = 'http://schemas.google.com/g/2005#car'

GD_PHONE_NUMBER_COMPANY_MAIN = 'http://schemas.google.com/g/2005#company_main'

GD_PHONE_NUMBER_FAX = 'http://schemas.google.com/g/2005#fax'
GD_PHONE_NUMBER_HOME = 'http://schemas.google.com/g/2005#home'

GD_PHONE_NUMBER_HOME_FAX = 'http://schemas.google.com/g/2005#home_fax'

GD_PHONE_NUMBER_ISDN = 'http://schemas.google.com/g/2005#isdn'
GD_PHONE_NUMBER_MAIN = 'http://schemas.google.com/g/2005#main'
GD_PHONE_NUMBER_MOBILE = 'http://schemas.google.com/g/2005#mobile'
GD_PHONE_NUMBER_OTHER = 'http://schemas.google.com/g/2005#other'

GD_PHONE_NUMBER_OTHER_FAX = 'http://schemas.google.com/g/2005#other_fax'

GD_PHONE_NUMBER_PAGER = 'http://schemas.google.com/g/2005#pager'
GD_PHONE_NUMBER_RADIO = 'http://schemas.google.com/g/2005#radio'
GD_PHONE_NUMBER_TELEX = 'http://schemas.google.com/g/2005#telex'

GD_PHONE_NUMBER_TTY_TDD = 'http://schemas.google.com/g/2005#tty_tdd'

GD_PHONE_NUMBER_WORK = 'http://schemas.google.com/g/2005#work'

GD_PHONE_NUMBER_WORK_FAX = 'http://schemas.google.com/g/2005#work_fax'
GD_PHONE_NUMBER_WORK_MOBILE = 'http://schemas.google.com/g/2005#work_mobile'
GD_PHONE_NUMBER_WORK_PAGER = 'http://schemas.google.com/g/2005#work_pager'

GD_POSTAL_ADDRESS_HOME = 'http://schemas.google.com/g/2005#home'
GD_POSTAL_ADDRESS_OTHER = 'http://schemas.google.com/g/2005#other'
GD_POSTAL_ADDRESS_WORK = 'http://schemas.google.com/g/2005#work'

GD_REMINDER_ALERT = 'alert'
GD_REMINDER_EMAIL = 'email'
GD_REMINDER_SMS = 'sms'

GD_WHERE_EVENT = 'http://schemas.google.com/g/2005#event'

GD_WHERE_EVENT_ALTERNATE = 'http://schemas.google.com/g/2005#event.alternate'
GD_WHERE_EVENT_PARKING = 'http://schemas.google.com/g/2005#event.parking'

GD_WHO_EVENT_ATTENDEE = 'http://schemas.google.com/g/2005#event.attendee'
GD_WHO_EVENT_ORGANIZER = 'http://schemas.google.com/g/2005#event.organizer'
GD_WHO_EVENT_PERFORMER = 'http://schemas.google.com/g/2005#event.performer'
GD_WHO_EVENT_SPEAKER = 'http://schemas.google.com/g/2005#event.speaker'

LINK_ACCESS_CONTROL_LIST = 'http://schemas.google.com/acl/2007#accessControlList'

LINK_ALTERNATE = 'http://www.iana.org/assignments/relation/alternate'
LINK_BATCH = 'http://schemas.google.com/g/2005#batch'
LINK_EDIT = 'http://www.iana.org/assignments/relation/edit'

LINK_EDIT_MEDIA = 'http://www.iana.org/assignments/relation/edit-media'

LINK_ENCLOSURE = 'http://www.iana.org/assignments/relation/enclosure'
LINK_PARENT = 'http://schemas.google.com/docs/2007#parent'
LINK_RELATED = 'http://www.iana.org/assignments/relation/related'

LINK_RESUMABLE_CREATE_MEDIA = 'http://schemas.google.com/g/2005#resumable-create-media'

LINK_RESUMABLE_EDIT_MEDIA = 'http://schemas.google.com/g/2005#resumable-edit-media'

LINK_SELF = 'http://www.iana.org/assignments/relation/self'
LINK_VIA = 'http://www.iana.org/assignments/relation/via'

MAJOR_VERSION = 0

MICRO_VERSION = 12

MINOR_VERSION = 17

OAUTH2_REDIRECT_URI_OOB = 'urn:ietf:wg:oauth:2.0:oob'

OAUTH2_REDIRECT_URI_OOB_AUTO = 'urn:ietf:wg:oauth:2.0:oob:auto'

PICASAWEB_VIDEO_STATUS_FAILED = 'failed'
PICASAWEB_VIDEO_STATUS_FINAL = 'final'
PICASAWEB_VIDEO_STATUS_PENDING = 'pending'
PICASAWEB_VIDEO_STATUS_READY = 'ready'

TASKS_STATUS_COMPLETED = 'completed'

TASKS_STATUS_NEEDS_ACTION = 'needsAction'

YOUTUBE_ACTION_COMMENT = 'comment'

YOUTUBE_ACTION_COMMENT_VOTE = 'commentVote'

YOUTUBE_ACTION_EMBED = 'embed'
YOUTUBE_ACTION_RATE = 'rate'
YOUTUBE_ACTION_SYNDICATE = 'syndicate'

YOUTUBE_ACTION_VIDEO_RESPOND = 'videoRespond'

YOUTUBE_ASPECT_RATIO_WIDESCREEN = 'widescreen'

YOUTUBE_CREDIT_ENTITY_PARTNER = 'partner'

YOUTUBE_LICENSE_CC = 'cc'
YOUTUBE_LICENSE_STANDARD = 'youtube'

YOUTUBE_RATING_TYPE_MPAA = 'mpaa'
YOUTUBE_RATING_TYPE_SIMPLE = 'simple'

YOUTUBE_RATING_TYPE_V_CHIP = 'v-chip'

_namespace = 'GData'

_version = '0.0'

__weakref__ = None

# functions

def client_login_authorizer_error_quark(): # real signature unknown; restored from __doc__
    """ client_login_authorizer_error_quark() -> int """
    return 0

def color_from_hexadecimal(hexadecimal): # real signature unknown; restored from __doc__
    """ color_from_hexadecimal(hexadecimal:str) -> bool, color:GData.Color """
    return False

def documents_service_error_quark(): # real signature unknown; restored from __doc__
    """ documents_service_error_quark() -> int """
    return 0

def parser_error_quark(): # real signature unknown; restored from __doc__
    """ parser_error_quark() -> int """
    return 0

def service_error_quark(): # real signature unknown; restored from __doc__
    """ service_error_quark() -> int """
    return 0

def youtube_service_error_quark(): # real signature unknown; restored from __doc__
    """ youtube_service_error_quark() -> int """
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

from .AccessHandler import AccessHandler
from .AccessHandlerIface import AccessHandlerIface
from .Parsable import Parsable
from .Entry import Entry
from .AccessRule import AccessRule
from .AccessRuleClass import AccessRuleClass
from .AccessRulePrivate import AccessRulePrivate
from .APPCategories import APPCategories
from .APPCategoriesClass import APPCategoriesClass
from .APPCategoriesPrivate import APPCategoriesPrivate
from .Comparable import Comparable
from .Author import Author
from .AuthorClass import AuthorClass
from .AuthorizationDomain import AuthorizationDomain
from .AuthorizationDomainClass import AuthorizationDomainClass
from .AuthorizationDomainPrivate import AuthorizationDomainPrivate
from .Authorizer import Authorizer
from .AuthorizerInterface import AuthorizerInterface
from .AuthorPrivate import AuthorPrivate
from .Batchable import Batchable
from .BatchableIface import BatchableIface
from .BatchOperation import BatchOperation
from .BatchOperationClass import BatchOperationClass
from .BatchOperationPrivate import BatchOperationPrivate
from .BatchOperationType import BatchOperationType
from .CalendarAccessRule import CalendarAccessRule
from .CalendarAccessRuleClass import CalendarAccessRuleClass
from .CalendarCalendar import CalendarCalendar
from .CalendarCalendarClass import CalendarCalendarClass
from .CalendarCalendarPrivate import CalendarCalendarPrivate
from .CalendarEvent import CalendarEvent
from .CalendarEventClass import CalendarEventClass
from .CalendarEventPrivate import CalendarEventPrivate
from .Feed import Feed
from .CalendarFeed import CalendarFeed
from .CalendarFeedClass import CalendarFeedClass
from .CalendarFeedPrivate import CalendarFeedPrivate
from .Query import Query
from .CalendarQuery import CalendarQuery
from .CalendarQueryClass import CalendarQueryClass
from .CalendarQueryPrivate import CalendarQueryPrivate
from .Service import Service
from .CalendarService import CalendarService
from .CalendarServiceClass import CalendarServiceClass
from .CalendarServicePrivate import CalendarServicePrivate
from .Category import Category
from .CategoryClass import CategoryClass
from .CategoryPrivate import CategoryPrivate
from .ClientLoginAuthorizer import ClientLoginAuthorizer
from .ClientLoginAuthorizerClass import ClientLoginAuthorizerClass
from .ClientLoginAuthorizerError import ClientLoginAuthorizerError
from .ClientLoginAuthorizerPrivate import ClientLoginAuthorizerPrivate
from .Color import Color
from .Comment import Comment
from .Commentable import Commentable
from .CommentableInterface import CommentableInterface
from .CommentClass import CommentClass
from .CommentPrivate import CommentPrivate
from .ComparableIface import ComparableIface
from .ContactsContact import ContactsContact
from .ContactsContactClass import ContactsContactClass
from .ContactsContactPrivate import ContactsContactPrivate
from .ContactsGroup import ContactsGroup
from .ContactsGroupClass import ContactsGroupClass
from .ContactsGroupPrivate import ContactsGroupPrivate
from .ContactsQuery import ContactsQuery
from .ContactsQueryClass import ContactsQueryClass
from .ContactsQueryPrivate import ContactsQueryPrivate
from .ContactsService import ContactsService
from .ContactsServiceClass import ContactsServiceClass
from .ContactsServicePrivate import ContactsServicePrivate
from .DocumentsAccessRule import DocumentsAccessRule
from .DocumentsAccessRuleClass import DocumentsAccessRuleClass
from .DocumentsEntry import DocumentsEntry
from .DocumentsDocument import DocumentsDocument
from .DocumentsDocumentClass import DocumentsDocumentClass
from .DocumentsDocumentPrivate import DocumentsDocumentPrivate
from .DocumentsDrawing import DocumentsDrawing
from .DocumentsDrawingClass import DocumentsDrawingClass
from .DocumentsDrawingPrivate import DocumentsDrawingPrivate
from .DocumentsEntryClass import DocumentsEntryClass
from .DocumentsEntryPrivate import DocumentsEntryPrivate
from .DocumentsFeed import DocumentsFeed
from .DocumentsFeedClass import DocumentsFeedClass
from .DocumentsFeedPrivate import DocumentsFeedPrivate
from .DocumentsFolder import DocumentsFolder
from .DocumentsFolderClass import DocumentsFolderClass
from .DocumentsFolderPrivate import DocumentsFolderPrivate
from .DocumentsMetadata import DocumentsMetadata
from .DocumentsMetadataClass import DocumentsMetadataClass
from .DocumentsMetadataPrivate import DocumentsMetadataPrivate
from .DocumentsPdf import DocumentsPdf
from .DocumentsPdfClass import DocumentsPdfClass
from .DocumentsPdfPrivate import DocumentsPdfPrivate
from .DocumentsPresentation import DocumentsPresentation
from .DocumentsPresentationClass import DocumentsPresentationClass
from .DocumentsPresentationPrivate import DocumentsPresentationPrivate
from .DocumentsProperty import DocumentsProperty
from .DocumentsPropertyClass import DocumentsPropertyClass
from .DocumentsPropertyPrivate import DocumentsPropertyPrivate
from .DocumentsQuery import DocumentsQuery
from .DocumentsQueryClass import DocumentsQueryClass
from .DocumentsQueryPrivate import DocumentsQueryPrivate
from .DocumentsService import DocumentsService
from .DocumentsServiceClass import DocumentsServiceClass
from .DocumentsServiceError import DocumentsServiceError
from .DocumentsServicePrivate import DocumentsServicePrivate
from .DocumentsSpreadsheet import DocumentsSpreadsheet
from .DocumentsSpreadsheetClass import DocumentsSpreadsheetClass
from .DocumentsSpreadsheetPrivate import DocumentsSpreadsheetPrivate
from .DocumentsText import DocumentsText
from .DocumentsTextClass import DocumentsTextClass
from .DocumentsTextPrivate import DocumentsTextPrivate
from .DocumentsUploadQuery import DocumentsUploadQuery
from .DocumentsUploadQueryClass import DocumentsUploadQueryClass
from .DocumentsUploadQueryPrivate import DocumentsUploadQueryPrivate
from .DownloadStream import DownloadStream
from .DownloadStreamClass import DownloadStreamClass
from .DownloadStreamPrivate import DownloadStreamPrivate
from .EntryClass import EntryClass
from .EntryPrivate import EntryPrivate
from .FeedClass import FeedClass
from .FeedPrivate import FeedPrivate
from .FreebaseQuery import FreebaseQuery
from .FreebaseQueryClass import FreebaseQueryClass
from .FreebaseQueryPrivate import FreebaseQueryPrivate
from .FreebaseResult import FreebaseResult
from .FreebaseResultClass import FreebaseResultClass
from .FreebaseResultPrivate import FreebaseResultPrivate
from .FreebaseSearchFilterType import FreebaseSearchFilterType
from .FreebaseSearchQuery import FreebaseSearchQuery
from .FreebaseSearchQueryClass import FreebaseSearchQueryClass
from .FreebaseSearchQueryPrivate import FreebaseSearchQueryPrivate
from .FreebaseSearchResult import FreebaseSearchResult
from .FreebaseSearchResultClass import FreebaseSearchResultClass
from .FreebaseSearchResultItem import FreebaseSearchResultItem
from .FreebaseSearchResultPrivate import FreebaseSearchResultPrivate
from .FreebaseService import FreebaseService
from .FreebaseServiceClass import FreebaseServiceClass
from .FreebaseServicePrivate import FreebaseServicePrivate
from .FreebaseTopicObject import FreebaseTopicObject
from .FreebaseTopicQuery import FreebaseTopicQuery
from .FreebaseTopicQueryClass import FreebaseTopicQueryClass
from .FreebaseTopicQueryPrivate import FreebaseTopicQueryPrivate
from .FreebaseTopicResult import FreebaseTopicResult
from .FreebaseTopicResultClass import FreebaseTopicResultClass
from .FreebaseTopicResultPrivate import FreebaseTopicResultPrivate
from .FreebaseTopicValue import FreebaseTopicValue
from .GContactCalendar import GContactCalendar
from .GContactCalendarClass import GContactCalendarClass
from .GContactCalendarPrivate import GContactCalendarPrivate
from .GContactEvent import GContactEvent
from .GContactEventClass import GContactEventClass
from .GContactEventPrivate import GContactEventPrivate
from .GContactExternalID import GContactExternalID
from .GContactExternalIDClass import GContactExternalIDClass
from .GContactExternalIDPrivate import GContactExternalIDPrivate
from .GContactJot import GContactJot
from .GContactJotClass import GContactJotClass
from .GContactJotPrivate import GContactJotPrivate
from .GContactLanguage import GContactLanguage
from .GContactLanguageClass import GContactLanguageClass
from .GContactLanguagePrivate import GContactLanguagePrivate
from .GContactRelation import GContactRelation
from .GContactRelationClass import GContactRelationClass
from .GContactRelationPrivate import GContactRelationPrivate
from .GContactWebsite import GContactWebsite
from .GContactWebsiteClass import GContactWebsiteClass
from .GContactWebsitePrivate import GContactWebsitePrivate
from .GDEmailAddress import GDEmailAddress
from .GDEmailAddressClass import GDEmailAddressClass
from .GDEmailAddressPrivate import GDEmailAddressPrivate
from .GDIMAddress import GDIMAddress
from .GDIMAddressClass import GDIMAddressClass
from .GDIMAddressPrivate import GDIMAddressPrivate
from .GDName import GDName
from .GDNameClass import GDNameClass
from .GDNamePrivate import GDNamePrivate
from .GDOrganization import GDOrganization
from .GDOrganizationClass import GDOrganizationClass
from .GDOrganizationPrivate import GDOrganizationPrivate
from .GDPhoneNumber import GDPhoneNumber
from .GDPhoneNumberClass import GDPhoneNumberClass
from .GDPhoneNumberPrivate import GDPhoneNumberPrivate
from .GDPostalAddress import GDPostalAddress
from .GDPostalAddressClass import GDPostalAddressClass
from .GDPostalAddressPrivate import GDPostalAddressPrivate
from .GDReminder import GDReminder
from .GDReminderClass import GDReminderClass
from .GDReminderPrivate import GDReminderPrivate
from .GDWhen import GDWhen
from .GDWhenClass import GDWhenClass
from .GDWhenPrivate import GDWhenPrivate
from .GDWhere import GDWhere
from .GDWhereClass import GDWhereClass
from .GDWherePrivate import GDWherePrivate
from .GDWho import GDWho
from .GDWhoClass import GDWhoClass
from .GDWhoPrivate import GDWhoPrivate
from .Generator import Generator
from .GeneratorClass import GeneratorClass
from .GeneratorPrivate import GeneratorPrivate
from .GoaAuthorizer import GoaAuthorizer
from .GoaAuthorizerClass import GoaAuthorizerClass
from .GoaAuthorizerPrivate import GoaAuthorizerPrivate
from .Link import Link
from .LinkClass import LinkClass
from .LinkPrivate import LinkPrivate
from .MediaCategory import MediaCategory
from .MediaCategoryClass import MediaCategoryClass
from .MediaCategoryPrivate import MediaCategoryPrivate
from .MediaContent import MediaContent
from .MediaContentClass import MediaContentClass
from .MediaContentPrivate import MediaContentPrivate
from .MediaCredit import MediaCredit
from .MediaCreditClass import MediaCreditClass
from .MediaCreditPrivate import MediaCreditPrivate
from .MediaExpression import MediaExpression
from .MediaMedium import MediaMedium
from .MediaThumbnail import MediaThumbnail
from .MediaThumbnailClass import MediaThumbnailClass
from .MediaThumbnailPrivate import MediaThumbnailPrivate
from .OAuth1Authorizer import OAuth1Authorizer
from .OAuth1AuthorizerClass import OAuth1AuthorizerClass
from .OAuth1AuthorizerPrivate import OAuth1AuthorizerPrivate
from .OAuth2Authorizer import OAuth2Authorizer
from .OAuth2AuthorizerClass import OAuth2AuthorizerClass
from .OAuth2AuthorizerPrivate import OAuth2AuthorizerPrivate
from .OperationType import OperationType
from .ParsableClass import ParsableClass
from .ParsablePrivate import ParsablePrivate
from .ParserError import ParserError
from .PicasaWebAlbum import PicasaWebAlbum
from .PicasaWebAlbumClass import PicasaWebAlbumClass
from .PicasaWebAlbumPrivate import PicasaWebAlbumPrivate
from .PicasaWebComment import PicasaWebComment
from .PicasaWebCommentClass import PicasaWebCommentClass
from .PicasaWebCommentPrivate import PicasaWebCommentPrivate
from .PicasaWebFeed import PicasaWebFeed
from .PicasaWebFeedClass import PicasaWebFeedClass
from .PicasaWebFile import PicasaWebFile
from .PicasaWebFileClass import PicasaWebFileClass
from .PicasaWebFilePrivate import PicasaWebFilePrivate
from .PicasaWebQuery import PicasaWebQuery
from .PicasaWebQueryClass import PicasaWebQueryClass
from .PicasaWebQueryPrivate import PicasaWebQueryPrivate
from .PicasaWebService import PicasaWebService
from .PicasaWebServiceClass import PicasaWebServiceClass
from .PicasaWebUser import PicasaWebUser
from .PicasaWebUserClass import PicasaWebUserClass
from .PicasaWebUserPrivate import PicasaWebUserPrivate
from .PicasaWebVisibility import PicasaWebVisibility
from .QueryClass import QueryClass
from .QueryPrivate import QueryPrivate
from .ServiceClass import ServiceClass
from .ServiceError import ServiceError
from .ServicePrivate import ServicePrivate
from .TasksQuery import TasksQuery
from .TasksQueryClass import TasksQueryClass
from .TasksQueryPrivate import TasksQueryPrivate
from .TasksService import TasksService
from .TasksServiceClass import TasksServiceClass
from .TasksTask import TasksTask
from .TasksTaskClass import TasksTaskClass
from .TasksTasklist import TasksTasklist
from .TasksTasklistClass import TasksTasklistClass
from .TasksTaskPrivate import TasksTaskPrivate
from .UploadStream import UploadStream
from .UploadStreamClass import UploadStreamClass
from .UploadStreamPrivate import UploadStreamPrivate
from .YouTubeAge import YouTubeAge
from .YouTubeCategory import YouTubeCategory
from .YouTubeCategoryClass import YouTubeCategoryClass
from .YouTubeCategoryPrivate import YouTubeCategoryPrivate
from .YouTubeComment import YouTubeComment
from .YouTubeCommentClass import YouTubeCommentClass
from .YouTubeCommentPrivate import YouTubeCommentPrivate
from .YouTubeContent import YouTubeContent
from .YouTubeContentClass import YouTubeContentClass
from .YouTubeContentPrivate import YouTubeContentPrivate
from .YouTubeCredit import YouTubeCredit
from .YouTubeCreditClass import YouTubeCreditClass
from .YouTubeCreditPrivate import YouTubeCreditPrivate
from .YouTubeFeed import YouTubeFeed
from .YouTubeFeedClass import YouTubeFeedClass
from .YouTubeFeedPrivate import YouTubeFeedPrivate
from .YouTubeFormat import YouTubeFormat
from .YouTubePermission import YouTubePermission
from .YouTubeQuery import YouTubeQuery
from .YouTubeQueryClass import YouTubeQueryClass
from .YouTubeQueryPrivate import YouTubeQueryPrivate
from .YouTubeSafeSearch import YouTubeSafeSearch
from .YouTubeService import YouTubeService
from .YouTubeServiceClass import YouTubeServiceClass
from .YouTubeServiceError import YouTubeServiceError
from .YouTubeServicePrivate import YouTubeServicePrivate
from .YouTubeSortOrder import YouTubeSortOrder
from .YouTubeStandardFeedType import YouTubeStandardFeedType
from .YouTubeState import YouTubeState
from .YouTubeStateClass import YouTubeStateClass
from .YouTubeStatePrivate import YouTubeStatePrivate
from .YouTubeUploader import YouTubeUploader
from .YouTubeVideo import YouTubeVideo
from .YouTubeVideoClass import YouTubeVideoClass
from .YouTubeVideoPrivate import YouTubeVideoPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fd5e323cd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GData-0.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GData', loader=<gi.importer.DynamicImporter object at 0x7fd5e323cd00>)"

