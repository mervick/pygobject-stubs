# encoding: utf-8
# module gi.repository.ModemManager
# from /usr/lib64/girepository-1.0/ModemManager-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


# Variables with simple values

BEARER_METHOD_CONNECT = 'Connect'
BEARER_METHOD_DISCONNECT = 'Disconnect'

BEARER_PROPERTY_BEARERTYPE = 'BearerType'
BEARER_PROPERTY_CONNECTED = 'Connected'
BEARER_PROPERTY_INTERFACE = 'Interface'
BEARER_PROPERTY_IP4CONFIG = 'Ip4Config'
BEARER_PROPERTY_IP6CONFIG = 'Ip6Config'
BEARER_PROPERTY_IPTIMEOUT = 'IpTimeout'
BEARER_PROPERTY_PROPERTIES = 'Properties'
BEARER_PROPERTY_STATS = 'Stats'
BEARER_PROPERTY_SUSPENDED = 'Suspended'

CALL_METHOD_ACCEPT = 'Accept'
CALL_METHOD_DEFLECT = 'Deflect'
CALL_METHOD_HANGUP = 'Hangup'
CALL_METHOD_JOINMULTIPARTY = 'JoinMultiparty'
CALL_METHOD_LEAVEMULTIPARTY = 'LeaveMultiparty'
CALL_METHOD_SENDDTMF = 'SendDtmf'
CALL_METHOD_START = 'Start'

CALL_PROPERTY_AUDIOFORMAT = 'AudioFormat'
CALL_PROPERTY_AUDIOPORT = 'AudioPort'
CALL_PROPERTY_DIRECTION = 'Direction'
CALL_PROPERTY_MULTIPARTY = 'Multiparty'
CALL_PROPERTY_NUMBER = 'Number'
CALL_PROPERTY_STATE = 'State'
CALL_PROPERTY_STATEREASON = 'StateReason'

CALL_SIGNAL_DTMFRECEIVED = 'DtmfReceived'
CALL_SIGNAL_STATECHANGED = 'StateChanged'

DBUS_ERROR_PREFIX = 'org.freedesktop.ModemManager1.Error'

DBUS_INTERFACE = 'org.freedesktop.ModemManager1'

DBUS_INTERFACE_BEARER = 'org.freedesktop.ModemManager1.Bearer'
DBUS_INTERFACE_CALL = 'org.freedesktop.ModemManager1.Call'
DBUS_INTERFACE_MODEM = 'org.freedesktop.ModemManager1.Modem'

DBUS_INTERFACE_MODEM_FIRMWARE = 'org.freedesktop.ModemManager1.Modem.Firmware'
DBUS_INTERFACE_MODEM_LOCATION = 'org.freedesktop.ModemManager1.Modem.Location'
DBUS_INTERFACE_MODEM_MESSAGING = 'org.freedesktop.ModemManager1.Modem.Messaging'
DBUS_INTERFACE_MODEM_MODEM3GPP = 'org.freedesktop.ModemManager1.Modem.Modem3gpp'

DBUS_INTERFACE_MODEM_MODEM3GPP_USSD = 'org.freedesktop.ModemManager1.Modem.Modem3gpp.Ussd'

DBUS_INTERFACE_MODEM_MODEMCDMA = 'org.freedesktop.ModemManager1.Modem.ModemCdma'
DBUS_INTERFACE_MODEM_OMA = 'org.freedesktop.ModemManager1.Modem.Oma'
DBUS_INTERFACE_MODEM_SIGNAL = 'org.freedesktop.ModemManager1.Modem.Signal'
DBUS_INTERFACE_MODEM_TIME = 'org.freedesktop.ModemManager1.Modem.Time'
DBUS_INTERFACE_MODEM_VOICE = 'org.freedesktop.ModemManager1.Modem.Voice'

DBUS_INTERFACE_SIM = 'org.freedesktop.ModemManager1.Sim'
DBUS_INTERFACE_SMS = 'org.freedesktop.ModemManager1.Sms'

DBUS_PATH = '/org/freedesktop/ModemManager1'
DBUS_SERVICE = 'org.freedesktop.ModemManager1'

MAJOR_VERSION = 1

MANAGER_METHOD_INHIBITDEVICE = 'InhibitDevice'
MANAGER_METHOD_REPORTKERNELEVENT = 'ReportKernelEvent'
MANAGER_METHOD_SCANDEVICES = 'ScanDevices'
MANAGER_METHOD_SETLOGGING = 'SetLogging'

MANAGER_PROPERTY_VERSION = 'Version'

MICRO_VERSION = 8

MINOR_VERSION = 12

MODEM_CDMA_NID_UNKNOWN = 99999

MODEM_CDMA_SID_UNKNOWN = 99999

MODEM_FIRMWARE_METHOD_LIST = 'List'
MODEM_FIRMWARE_METHOD_SELECT = 'Select'

MODEM_FIRMWARE_PROPERTY_UPDATESETTINGS = 'UpdateSettings'

MODEM_LOCATION_METHOD_GETLOCATION = 'GetLocation'
MODEM_LOCATION_METHOD_INJECTASSISTANCEDATA = 'InjectAssistanceData'
MODEM_LOCATION_METHOD_SETGPSREFRESHRATE = 'SetGpsRefreshRate'
MODEM_LOCATION_METHOD_SETSUPLSERVER = 'SetSuplServer'
MODEM_LOCATION_METHOD_SETUP = 'Setup'

MODEM_LOCATION_PROPERTY_ASSISTANCEDATASERVERS = 'AssistanceDataServers'
MODEM_LOCATION_PROPERTY_CAPABILITIES = 'Capabilities'
MODEM_LOCATION_PROPERTY_ENABLED = 'Enabled'
MODEM_LOCATION_PROPERTY_GPSREFRESHRATE = 'GpsRefreshRate'
MODEM_LOCATION_PROPERTY_LOCATION = 'Location'
MODEM_LOCATION_PROPERTY_SIGNALSLOCATION = 'SignalsLocation'
MODEM_LOCATION_PROPERTY_SUPLSERVER = 'SuplServer'
MODEM_LOCATION_PROPERTY_SUPPORTEDASSISTANCEDATA = 'SupportedAssistanceData'

MODEM_MESSAGING_METHOD_CREATE = 'Create'
MODEM_MESSAGING_METHOD_DELETE = 'Delete'
MODEM_MESSAGING_METHOD_LIST = 'List'

MODEM_MESSAGING_PROPERTY_DEFAULTSTORAGE = 'DefaultStorage'
MODEM_MESSAGING_PROPERTY_MESSAGES = 'Messages'
MODEM_MESSAGING_PROPERTY_SUPPORTEDSTORAGES = 'SupportedStorages'

MODEM_MESSAGING_SIGNAL_ADDED = 'Added'
MODEM_MESSAGING_SIGNAL_DELETED = 'Deleted'

MODEM_METHOD_COMMAND = 'Command'
MODEM_METHOD_CREATEBEARER = 'CreateBearer'
MODEM_METHOD_DELETEBEARER = 'DeleteBearer'
MODEM_METHOD_ENABLE = 'Enable'
MODEM_METHOD_FACTORYRESET = 'FactoryReset'
MODEM_METHOD_LISTBEARERS = 'ListBearers'
MODEM_METHOD_RESET = 'Reset'
MODEM_METHOD_SETCURRENTBANDS = 'SetCurrentBands'
MODEM_METHOD_SETCURRENTCAPABILITIES = 'SetCurrentCapabilities'
MODEM_METHOD_SETCURRENTMODES = 'SetCurrentModes'
MODEM_METHOD_SETPOWERSTATE = 'SetPowerState'

MODEM_MODEM3GPP_METHOD_REGISTER = 'Register'
MODEM_MODEM3GPP_METHOD_SCAN = 'Scan'
MODEM_MODEM3GPP_METHOD_SETEPSUEMODEOPERATION = 'SetEpsUeModeOperation'
MODEM_MODEM3GPP_METHOD_SETINITIALEPSBEARERSETTINGS = 'SetInitialEpsBearerSettings'

MODEM_MODEM3GPP_PROPERTY_ENABLEDFACILITYLOCKS = 'EnabledFacilityLocks'
MODEM_MODEM3GPP_PROPERTY_EPSUEMODEOPERATION = 'EpsUeModeOperation'
MODEM_MODEM3GPP_PROPERTY_IMEI = 'Imei'
MODEM_MODEM3GPP_PROPERTY_INITIALEPSBEARER = 'InitialEpsBearer'
MODEM_MODEM3GPP_PROPERTY_INITIALEPSBEARERSETTINGS = 'InitialEpsBearerSettings'
MODEM_MODEM3GPP_PROPERTY_OPERATORCODE = 'OperatorCode'
MODEM_MODEM3GPP_PROPERTY_OPERATORNAME = 'OperatorName'
MODEM_MODEM3GPP_PROPERTY_PCO = 'Pco'
MODEM_MODEM3GPP_PROPERTY_REGISTRATIONSTATE = 'RegistrationState'
MODEM_MODEM3GPP_PROPERTY_SUBSCRIPTIONSTATE = 'SubscriptionState'

MODEM_MODEM3GPP_USSD_METHOD_CANCEL = 'Cancel'
MODEM_MODEM3GPP_USSD_METHOD_INITIATE = 'Initiate'
MODEM_MODEM3GPP_USSD_METHOD_RESPOND = 'Respond'

MODEM_MODEM3GPP_USSD_PROPERTY_NETWORKNOTIFICATION = 'NetworkNotification'
MODEM_MODEM3GPP_USSD_PROPERTY_NETWORKREQUEST = 'NetworkRequest'
MODEM_MODEM3GPP_USSD_PROPERTY_STATE = 'State'

MODEM_MODEMCDMA_METHOD_ACTIVATE = 'Activate'
MODEM_MODEMCDMA_METHOD_ACTIVATEMANUAL = 'ActivateManual'

MODEM_MODEMCDMA_PROPERTY_ACTIVATIONSTATE = 'ActivationState'
MODEM_MODEMCDMA_PROPERTY_CDMA1XREGISTRATIONSTATE = 'Cdma1xRegistrationState'
MODEM_MODEMCDMA_PROPERTY_ESN = 'Esn'
MODEM_MODEMCDMA_PROPERTY_EVDOREGISTRATIONSTATE = 'EvdoRegistrationState'
MODEM_MODEMCDMA_PROPERTY_MEID = 'Meid'
MODEM_MODEMCDMA_PROPERTY_NID = 'Nid'
MODEM_MODEMCDMA_PROPERTY_SID = 'Sid'

MODEM_MODEMCDMA_SIGNAL_ACTIVATIONSTATECHANGED = 'ActivationStateChanged'

MODEM_OMA_METHOD_ACCEPTNETWORKINITIATEDSESSION = 'AcceptNetworkInitiatedSession'
MODEM_OMA_METHOD_CANCELSESSION = 'CancelSession'
MODEM_OMA_METHOD_SETUP = 'Setup'
MODEM_OMA_METHOD_STARTCLIENTINITIATEDSESSION = 'StartClientInitiatedSession'

MODEM_OMA_PROPERTY_FEATURES = 'Features'
MODEM_OMA_PROPERTY_PENDINGNETWORKINITIATEDSESSIONS = 'PendingNetworkInitiatedSessions'
MODEM_OMA_PROPERTY_SESSIONSTATE = 'SessionState'
MODEM_OMA_PROPERTY_SESSIONTYPE = 'SessionType'

MODEM_OMA_SIGNAL_SESSIONSTATECHANGED = 'SessionStateChanged'

MODEM_PROPERTY_ACCESSTECHNOLOGIES = 'AccessTechnologies'
MODEM_PROPERTY_BEARERS = 'Bearers'
MODEM_PROPERTY_CARRIERCONFIGURATION = 'CarrierConfiguration'
MODEM_PROPERTY_CARRIERCONFIGURATIONREVISION = 'CarrierConfigurationRevision'
MODEM_PROPERTY_CURRENTBANDS = 'CurrentBands'
MODEM_PROPERTY_CURRENTCAPABILITIES = 'CurrentCapabilities'
MODEM_PROPERTY_CURRENTMODES = 'CurrentModes'
MODEM_PROPERTY_DEVICE = 'Device'
MODEM_PROPERTY_DEVICEIDENTIFIER = 'DeviceIdentifier'
MODEM_PROPERTY_DRIVERS = 'Drivers'
MODEM_PROPERTY_EQUIPMENTIDENTIFIER = 'EquipmentIdentifier'
MODEM_PROPERTY_HARDWAREREVISION = 'HardwareRevision'
MODEM_PROPERTY_MANUFACTURER = 'Manufacturer'
MODEM_PROPERTY_MAXACTIVEBEARERS = 'MaxActiveBearers'
MODEM_PROPERTY_MAXBEARERS = 'MaxBearers'
MODEM_PROPERTY_MODEL = 'Model'
MODEM_PROPERTY_OWNNUMBERS = 'OwnNumbers'
MODEM_PROPERTY_PLUGIN = 'Plugin'
MODEM_PROPERTY_PORTS = 'Ports'
MODEM_PROPERTY_POWERSTATE = 'PowerState'
MODEM_PROPERTY_PRIMARYPORT = 'PrimaryPort'
MODEM_PROPERTY_REVISION = 'Revision'
MODEM_PROPERTY_SIGNALQUALITY = 'SignalQuality'
MODEM_PROPERTY_SIM = 'Sim'
MODEM_PROPERTY_STATE = 'State'
MODEM_PROPERTY_STATEFAILEDREASON = 'StateFailedReason'
MODEM_PROPERTY_SUPPORTEDBANDS = 'SupportedBands'
MODEM_PROPERTY_SUPPORTEDCAPABILITIES = 'SupportedCapabilities'
MODEM_PROPERTY_SUPPORTEDIPFAMILIES = 'SupportedIpFamilies'
MODEM_PROPERTY_SUPPORTEDMODES = 'SupportedModes'
MODEM_PROPERTY_UNLOCKREQUIRED = 'UnlockRequired'
MODEM_PROPERTY_UNLOCKRETRIES = 'UnlockRetries'

MODEM_SIGNAL_METHOD_SETUP = 'Setup'

MODEM_SIGNAL_PROPERTY_CDMA = 'Cdma'
MODEM_SIGNAL_PROPERTY_EVDO = 'Evdo'
MODEM_SIGNAL_PROPERTY_GSM = 'Gsm'
MODEM_SIGNAL_PROPERTY_LTE = 'Lte'
MODEM_SIGNAL_PROPERTY_RATE = 'Rate'
MODEM_SIGNAL_PROPERTY_UMTS = 'Umts'

MODEM_SIGNAL_STATECHANGED = 'StateChanged'

MODEM_TIME_METHOD_GETNETWORKTIME = 'GetNetworkTime'

MODEM_TIME_PROPERTY_NETWORKTIMEZONE = 'NetworkTimezone'

MODEM_TIME_SIGNAL_NETWORKTIMECHANGED = 'NetworkTimeChanged'

MODEM_VOICE_METHOD_CALLWAITINGQUERY = 'CallWaitingQuery'
MODEM_VOICE_METHOD_CALLWAITINGSETUP = 'CallWaitingSetup'
MODEM_VOICE_METHOD_CREATECALL = 'CreateCall'
MODEM_VOICE_METHOD_DELETECALL = 'DeleteCall'
MODEM_VOICE_METHOD_HANGUPALL = 'HangupAll'
MODEM_VOICE_METHOD_HANGUPANDACCEPT = 'HangupAndAccept'
MODEM_VOICE_METHOD_HOLDANDACCEPT = 'HoldAndAccept'
MODEM_VOICE_METHOD_LISTCALLS = 'ListCalls'
MODEM_VOICE_METHOD_TRANSFER = 'Transfer'

MODEM_VOICE_PROPERTY_CALLS = 'Calls'
MODEM_VOICE_PROPERTY_EMERGENCYONLY = 'EmergencyOnly'

MODEM_VOICE_SIGNAL_CALLADDED = 'CallAdded'
MODEM_VOICE_SIGNAL_CALLDELETED = 'CallDeleted'

SIMPLE_PROPERTY_3GPP_OPERATOR_CODE = 'm3gpp-operator-code'
SIMPLE_PROPERTY_3GPP_OPERATOR_NAME = 'm3gpp-operator-name'

SIMPLE_PROPERTY_3GPP_REGISTRATION_STATE = 'm3gpp-registration-state'

SIMPLE_PROPERTY_3GPP_SUBSCRIPTION_STATE = 'm3gpp-subscription-state'

SIMPLE_PROPERTY_ACCESS_TECHNOLOGIES = 'access-technologies'

SIMPLE_PROPERTY_CDMA_CDMA1X_REGISTRATION_STATE = 'cdma-cdma1x-registration-state'

SIMPLE_PROPERTY_CDMA_EVDO_REGISTRATION_STATE = 'cdma-evdo-registration-state'

SIMPLE_PROPERTY_CDMA_NID = 'cdma-nid'
SIMPLE_PROPERTY_CDMA_SID = 'cdma-sid'

SIMPLE_PROPERTY_CURRENT_BANDS = 'current-bands'

SIMPLE_PROPERTY_SIGNAL_QUALITY = 'signal-quality'

SIMPLE_PROPERTY_STATE = 'state'

SIM_METHOD_CHANGEPIN = 'ChangePin'
SIM_METHOD_ENABLEPIN = 'EnablePin'
SIM_METHOD_SENDPIN = 'SendPin'
SIM_METHOD_SENDPUK = 'SendPuk'

SIM_PROPERTY_EMERGENCYNUMBERS = 'EmergencyNumbers'
SIM_PROPERTY_IMSI = 'Imsi'
SIM_PROPERTY_OPERATORIDENTIFIER = 'OperatorIdentifier'
SIM_PROPERTY_OPERATORNAME = 'OperatorName'
SIM_PROPERTY_SIMIDENTIFIER = 'SimIdentifier'

SMS_METHOD_SEND = 'Send'
SMS_METHOD_STORE = 'Store'

SMS_PROPERTY_CLASS = 'Class'
SMS_PROPERTY_DATA = 'Data'
SMS_PROPERTY_DELIVERYREPORTREQUEST = 'DeliveryReportRequest'
SMS_PROPERTY_DELIVERYSTATE = 'DeliveryState'
SMS_PROPERTY_DISCHARGETIMESTAMP = 'DischargeTimestamp'
SMS_PROPERTY_MESSAGEREFERENCE = 'MessageReference'
SMS_PROPERTY_NUMBER = 'Number'
SMS_PROPERTY_PDUTYPE = 'PduType'
SMS_PROPERTY_SERVICECATEGORY = 'ServiceCategory'
SMS_PROPERTY_SMSC = 'SMSC'
SMS_PROPERTY_STATE = 'State'
SMS_PROPERTY_STORAGE = 'Storage'
SMS_PROPERTY_TELESERVICEID = 'TeleserviceId'
SMS_PROPERTY_TEXT = 'Text'
SMS_PROPERTY_TIMESTAMP = 'Timestamp'
SMS_PROPERTY_VALIDITY = 'Validity'

UNLOCK_RETRIES_UNKNOWN = 999

_namespace = 'ModemManager'

_version = '1.0'

__weakref__ = None

# functions

def bearer_allowed_auth_build_string_from_mask(mask): # real signature unknown; restored from __doc__
    """ bearer_allowed_auth_build_string_from_mask(mask:ModemManager.BearerAllowedAuth) -> str """
    return ""

def bearer_ip_family_build_string_from_mask(mask): # real signature unknown; restored from __doc__
    """ bearer_ip_family_build_string_from_mask(mask:ModemManager.BearerIpFamily) -> str """
    return ""

def bearer_ip_method_get_string(val): # real signature unknown; restored from __doc__
    """ bearer_ip_method_get_string(val:ModemManager.BearerIpMethod) -> str """
    return ""

def bearer_type_get_string(val): # real signature unknown; restored from __doc__
    """ bearer_type_get_string(val:ModemManager.BearerType) -> str """
    return ""

def call_direction_get_string(val): # real signature unknown; restored from __doc__
    """ call_direction_get_string(val:ModemManager.CallDirection) -> str """
    return ""

def call_state_get_string(val): # real signature unknown; restored from __doc__
    """ call_state_get_string(val:ModemManager.CallState) -> str """
    return ""

def call_state_reason_get_string(val): # real signature unknown; restored from __doc__
    """ call_state_reason_get_string(val:ModemManager.CallStateReason) -> str """
    return ""

def cdma_activation_error_quark(): # real signature unknown; restored from __doc__
    """ cdma_activation_error_quark() -> int """
    return 0

def connection_error_quark(): # real signature unknown; restored from __doc__
    """ connection_error_quark() -> int """
    return 0

def core_error_quark(): # real signature unknown; restored from __doc__
    """ core_error_quark() -> int """
    return 0

def firmware_image_type_get_string(val): # real signature unknown; restored from __doc__
    """ firmware_image_type_get_string(val:ModemManager.FirmwareImageType) -> str """
    return ""

def gdbus_bearer_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_bearer_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_bearer_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_bearer_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem3gpp_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem3gpp_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem3gpp_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem3gpp_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem3gpp_ussd_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem3gpp_ussd_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem3gpp_ussd_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem3gpp_ussd_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem_cdma_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem_cdma_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem_cdma_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem_cdma_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem_firmware_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem_firmware_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem_firmware_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem_firmware_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem_location_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem_location_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem_location_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem_location_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem_messaging_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem_messaging_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem_messaging_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem_messaging_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem_oma_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem_oma_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem_oma_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem_oma_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem_signal_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem_signal_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem_signal_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem_signal_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem_simple_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem_simple_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem_simple_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem_simple_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem_time_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem_time_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem_time_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem_time_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_modem_voice_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_modem_voice_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_modem_voice_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_modem_voice_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_org_freedesktop_modem_manager1_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_org_freedesktop_modem_manager1_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_org_freedesktop_modem_manager1_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_org_freedesktop_modem_manager1_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_sim_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_sim_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_sim_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_sim_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def gdbus_sms_interface_info(): # real signature unknown; restored from __doc__
    """ gdbus_sms_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def gdbus_sms_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ gdbus_sms_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def message_error_quark(): # real signature unknown; restored from __doc__
    """ message_error_quark() -> int """
    return 0

def mobile_equipment_error_quark(): # real signature unknown; restored from __doc__
    """ mobile_equipment_error_quark() -> int """
    return 0

def modem_3gpp_eps_ue_mode_operation_get_string(val): # real signature unknown; restored from __doc__
    """ modem_3gpp_eps_ue_mode_operation_get_string(val:ModemManager.Modem3gppEpsUeModeOperation) -> str """
    return ""

def modem_3gpp_facility_build_string_from_mask(mask): # real signature unknown; restored from __doc__
    """ modem_3gpp_facility_build_string_from_mask(mask:ModemManager.Modem3gppFacility) -> str """
    return ""

def modem_3gpp_network_availability_get_string(val): # real signature unknown; restored from __doc__
    """ modem_3gpp_network_availability_get_string(val:ModemManager.Modem3gppNetworkAvailability) -> str """
    return ""

def modem_3gpp_registration_state_get_string(val): # real signature unknown; restored from __doc__
    """ modem_3gpp_registration_state_get_string(val:ModemManager.Modem3gppRegistrationState) -> str """
    return ""

def modem_3gpp_subscription_state_get_string(val): # real signature unknown; restored from __doc__
    """ modem_3gpp_subscription_state_get_string(val:ModemManager.Modem3gppSubscriptionState) -> str """
    return ""

def modem_3gpp_ussd_session_state_get_string(val): # real signature unknown; restored from __doc__
    """ modem_3gpp_ussd_session_state_get_string(val:ModemManager.Modem3gppUssdSessionState) -> str """
    return ""

def modem_access_technology_build_string_from_mask(mask): # real signature unknown; restored from __doc__
    """ modem_access_technology_build_string_from_mask(mask:ModemManager.ModemAccessTechnology) -> str """
    return ""

def modem_band_get_string(val): # real signature unknown; restored from __doc__
    """ modem_band_get_string(val:ModemManager.ModemBand) -> str """
    return ""

def modem_capability_build_string_from_mask(mask): # real signature unknown; restored from __doc__
    """ modem_capability_build_string_from_mask(mask:ModemManager.ModemCapability) -> str """
    return ""

def modem_cdma_activation_state_get_string(val): # real signature unknown; restored from __doc__
    """ modem_cdma_activation_state_get_string(val:ModemManager.ModemCdmaActivationState) -> str """
    return ""

def modem_cdma_registration_state_get_string(val): # real signature unknown; restored from __doc__
    """ modem_cdma_registration_state_get_string(val:ModemManager.ModemCdmaRegistrationState) -> str """
    return ""

def modem_cdma_rm_protocol_get_string(val): # real signature unknown; restored from __doc__
    """ modem_cdma_rm_protocol_get_string(val:ModemManager.ModemCdmaRmProtocol) -> str """
    return ""

def modem_contacts_storage_get_string(val): # real signature unknown; restored from __doc__
    """ modem_contacts_storage_get_string(val:ModemManager.ModemContactsStorage) -> str """
    return ""

def modem_firmware_update_method_build_string_from_mask(mask): # real signature unknown; restored from __doc__
    """ modem_firmware_update_method_build_string_from_mask(mask:ModemManager.ModemFirmwareUpdateMethod) -> str """
    return ""

def modem_location_assistance_data_type_build_string_from_mask(mask): # real signature unknown; restored from __doc__
    """ modem_location_assistance_data_type_build_string_from_mask(mask:ModemManager.ModemLocationAssistanceDataType) -> str """
    return ""

def modem_location_source_build_string_from_mask(mask): # real signature unknown; restored from __doc__
    """ modem_location_source_build_string_from_mask(mask:ModemManager.ModemLocationSource) -> str """
    return ""

def modem_lock_get_string(val): # real signature unknown; restored from __doc__
    """ modem_lock_get_string(val:ModemManager.ModemLock) -> str """
    return ""

def modem_mode_build_string_from_mask(mask): # real signature unknown; restored from __doc__
    """ modem_mode_build_string_from_mask(mask:ModemManager.ModemMode) -> str """
    return ""

def modem_port_type_get_string(val): # real signature unknown; restored from __doc__
    """ modem_port_type_get_string(val:ModemManager.ModemPortType) -> str """
    return ""

def modem_power_state_get_string(val): # real signature unknown; restored from __doc__
    """ modem_power_state_get_string(val:ModemManager.ModemPowerState) -> str """
    return ""

def modem_state_change_reason_get_string(val): # real signature unknown; restored from __doc__
    """ modem_state_change_reason_get_string(val:ModemManager.ModemStateChangeReason) -> str """
    return ""

def modem_state_failed_reason_get_string(val): # real signature unknown; restored from __doc__
    """ modem_state_failed_reason_get_string(val:ModemManager.ModemStateFailedReason) -> str """
    return ""

def modem_state_get_string(val): # real signature unknown; restored from __doc__
    """ modem_state_get_string(val:ModemManager.ModemState) -> str """
    return ""

def oma_feature_build_string_from_mask(mask): # real signature unknown; restored from __doc__
    """ oma_feature_build_string_from_mask(mask:ModemManager.OmaFeature) -> str """
    return ""

def oma_session_state_failed_reason_get_string(val): # real signature unknown; restored from __doc__
    """ oma_session_state_failed_reason_get_string(val:ModemManager.OmaSessionStateFailedReason) -> str """
    return ""

def oma_session_state_get_string(val): # real signature unknown; restored from __doc__
    """ oma_session_state_get_string(val:ModemManager.OmaSessionState) -> str """
    return ""

def oma_session_type_get_string(val): # real signature unknown; restored from __doc__
    """ oma_session_type_get_string(val:ModemManager.OmaSessionType) -> str """
    return ""

def serial_error_quark(): # real signature unknown; restored from __doc__
    """ serial_error_quark() -> int """
    return 0

def sms_cdma_service_category_get_string(val): # real signature unknown; restored from __doc__
    """ sms_cdma_service_category_get_string(val:ModemManager.SmsCdmaServiceCategory) -> str """
    return ""

def sms_cdma_teleservice_id_get_string(val): # real signature unknown; restored from __doc__
    """ sms_cdma_teleservice_id_get_string(val:ModemManager.SmsCdmaTeleserviceId) -> str """
    return ""

def sms_delivery_state_get_string(val): # real signature unknown; restored from __doc__
    """ sms_delivery_state_get_string(val:ModemManager.SmsDeliveryState) -> str """
    return ""

def sms_pdu_type_get_string(val): # real signature unknown; restored from __doc__
    """ sms_pdu_type_get_string(val:ModemManager.SmsPduType) -> str """
    return ""

def sms_state_get_string(val): # real signature unknown; restored from __doc__
    """ sms_state_get_string(val:ModemManager.SmsState) -> str """
    return ""

def sms_storage_get_string(val): # real signature unknown; restored from __doc__
    """ sms_storage_get_string(val:ModemManager.SmsStorage) -> str """
    return ""

def sms_validity_type_get_string(val): # real signature unknown; restored from __doc__
    """ sms_validity_type_get_string(val:ModemManager.SmsValidityType) -> str """
    return ""

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

from .GdbusBearer import GdbusBearer
from .GdbusBearerProxy import GdbusBearerProxy
from .Bearer import Bearer
from .BearerAllowedAuth import BearerAllowedAuth
from .BearerClass import BearerClass
from .BearerIpConfig import BearerIpConfig
from .BearerIpConfigClass import BearerIpConfigClass
from .BearerIpConfigPrivate import BearerIpConfigPrivate
from .BearerIpFamily import BearerIpFamily
from .BearerIpMethod import BearerIpMethod
from .BearerPrivate import BearerPrivate
from .BearerProperties import BearerProperties
from .BearerPropertiesClass import BearerPropertiesClass
from .BearerPropertiesPrivate import BearerPropertiesPrivate
from .BearerStats import BearerStats
from .BearerStatsClass import BearerStatsClass
from .BearerStatsPrivate import BearerStatsPrivate
from .BearerType import BearerType
from .Call import Call
from .CallAudioFormat import CallAudioFormat
from .CallAudioFormatClass import CallAudioFormatClass
from .CallAudioFormatPrivate import CallAudioFormatPrivate
from .CallClass import CallClass
from .CallDirection import CallDirection
from .CallPrivate import CallPrivate
from .CallProperties import CallProperties
from .CallPropertiesClass import CallPropertiesClass
from .CallPropertiesPrivate import CallPropertiesPrivate
from .CallState import CallState
from .CallStateReason import CallStateReason
from .CdmaActivationError import CdmaActivationError
from .CdmaManualActivationProperties import CdmaManualActivationProperties
from .CdmaManualActivationPropertiesClass import CdmaManualActivationPropertiesClass
from .CdmaManualActivationPropertiesPrivate import CdmaManualActivationPropertiesPrivate
from .ConnectionError import ConnectionError
from .CoreError import CoreError
from .FirmwareImageType import FirmwareImageType
from .FirmwareProperties import FirmwareProperties
from .FirmwarePropertiesClass import FirmwarePropertiesClass
from .FirmwarePropertiesPrivate import FirmwarePropertiesPrivate
from .FirmwareUpdateSettings import FirmwareUpdateSettings
from .FirmwareUpdateSettingsClass import FirmwareUpdateSettingsClass
from .FirmwareUpdateSettingsPrivate import FirmwareUpdateSettingsPrivate
from .GdbusBearerIface import GdbusBearerIface
from .GdbusBearerProxyClass import GdbusBearerProxyClass
from .GdbusBearerProxyPrivate import GdbusBearerProxyPrivate
from .GdbusBearerSkeleton import GdbusBearerSkeleton
from .GdbusBearerSkeletonClass import GdbusBearerSkeletonClass
from .GdbusBearerSkeletonPrivate import GdbusBearerSkeletonPrivate
from .GdbusModem import GdbusModem
from .GdbusModem3gpp import GdbusModem3gpp
from .GdbusModem3gppIface import GdbusModem3gppIface
from .GdbusModem3gppProxy import GdbusModem3gppProxy
from .GdbusModem3gppProxyClass import GdbusModem3gppProxyClass
from .GdbusModem3gppProxyPrivate import GdbusModem3gppProxyPrivate
from .GdbusModem3gppSkeleton import GdbusModem3gppSkeleton
from .GdbusModem3gppSkeletonClass import GdbusModem3gppSkeletonClass
from .GdbusModem3gppSkeletonPrivate import GdbusModem3gppSkeletonPrivate
from .GdbusModem3gppUssd import GdbusModem3gppUssd
from .GdbusModem3gppUssdIface import GdbusModem3gppUssdIface
from .GdbusModem3gppUssdProxy import GdbusModem3gppUssdProxy
from .GdbusModem3gppUssdProxyClass import GdbusModem3gppUssdProxyClass
from .GdbusModem3gppUssdProxyPrivate import GdbusModem3gppUssdProxyPrivate
from .GdbusModem3gppUssdSkeleton import GdbusModem3gppUssdSkeleton
from .GdbusModem3gppUssdSkeletonClass import GdbusModem3gppUssdSkeletonClass
from .GdbusModem3gppUssdSkeletonPrivate import GdbusModem3gppUssdSkeletonPrivate
from .GdbusModemCdma import GdbusModemCdma
from .GdbusModemCdmaIface import GdbusModemCdmaIface
from .GdbusModemCdmaProxy import GdbusModemCdmaProxy
from .GdbusModemCdmaProxyClass import GdbusModemCdmaProxyClass
from .GdbusModemCdmaProxyPrivate import GdbusModemCdmaProxyPrivate
from .GdbusModemCdmaSkeleton import GdbusModemCdmaSkeleton
from .GdbusModemCdmaSkeletonClass import GdbusModemCdmaSkeletonClass
from .GdbusModemCdmaSkeletonPrivate import GdbusModemCdmaSkeletonPrivate
from .GdbusModemFirmware import GdbusModemFirmware
from .GdbusModemFirmwareIface import GdbusModemFirmwareIface
from .GdbusModemFirmwareProxy import GdbusModemFirmwareProxy
from .GdbusModemFirmwareProxyClass import GdbusModemFirmwareProxyClass
from .GdbusModemFirmwareProxyPrivate import GdbusModemFirmwareProxyPrivate
from .GdbusModemFirmwareSkeleton import GdbusModemFirmwareSkeleton
from .GdbusModemFirmwareSkeletonClass import GdbusModemFirmwareSkeletonClass
from .GdbusModemFirmwareSkeletonPrivate import GdbusModemFirmwareSkeletonPrivate
from .GdbusModemIface import GdbusModemIface
from .GdbusModemLocation import GdbusModemLocation
from .GdbusModemLocationIface import GdbusModemLocationIface
from .GdbusModemLocationProxy import GdbusModemLocationProxy
from .GdbusModemLocationProxyClass import GdbusModemLocationProxyClass
from .GdbusModemLocationProxyPrivate import GdbusModemLocationProxyPrivate
from .GdbusModemLocationSkeleton import GdbusModemLocationSkeleton
from .GdbusModemLocationSkeletonClass import GdbusModemLocationSkeletonClass
from .GdbusModemLocationSkeletonPrivate import GdbusModemLocationSkeletonPrivate
from .GdbusModemMessaging import GdbusModemMessaging
from .GdbusModemMessagingIface import GdbusModemMessagingIface
from .GdbusModemMessagingProxy import GdbusModemMessagingProxy
from .GdbusModemMessagingProxyClass import GdbusModemMessagingProxyClass
from .GdbusModemMessagingProxyPrivate import GdbusModemMessagingProxyPrivate
from .GdbusModemMessagingSkeleton import GdbusModemMessagingSkeleton
from .GdbusModemMessagingSkeletonClass import GdbusModemMessagingSkeletonClass
from .GdbusModemMessagingSkeletonPrivate import GdbusModemMessagingSkeletonPrivate
from .GdbusModemOma import GdbusModemOma
from .GdbusModemOmaIface import GdbusModemOmaIface
from .GdbusModemOmaProxy import GdbusModemOmaProxy
from .GdbusModemOmaProxyClass import GdbusModemOmaProxyClass
from .GdbusModemOmaProxyPrivate import GdbusModemOmaProxyPrivate
from .GdbusModemOmaSkeleton import GdbusModemOmaSkeleton
from .GdbusModemOmaSkeletonClass import GdbusModemOmaSkeletonClass
from .GdbusModemOmaSkeletonPrivate import GdbusModemOmaSkeletonPrivate
from .GdbusModemProxy import GdbusModemProxy
from .GdbusModemProxyClass import GdbusModemProxyClass
from .GdbusModemProxyPrivate import GdbusModemProxyPrivate
from .GdbusModemSignal import GdbusModemSignal
from .GdbusModemSignalIface import GdbusModemSignalIface
from .GdbusModemSignalProxy import GdbusModemSignalProxy
from .GdbusModemSignalProxyClass import GdbusModemSignalProxyClass
from .GdbusModemSignalProxyPrivate import GdbusModemSignalProxyPrivate
from .GdbusModemSignalSkeleton import GdbusModemSignalSkeleton
from .GdbusModemSignalSkeletonClass import GdbusModemSignalSkeletonClass
from .GdbusModemSignalSkeletonPrivate import GdbusModemSignalSkeletonPrivate
from .GdbusModemSimple import GdbusModemSimple
from .GdbusModemSimpleIface import GdbusModemSimpleIface
from .GdbusModemSimpleProxy import GdbusModemSimpleProxy
from .GdbusModemSimpleProxyClass import GdbusModemSimpleProxyClass
from .GdbusModemSimpleProxyPrivate import GdbusModemSimpleProxyPrivate
from .GdbusModemSimpleSkeleton import GdbusModemSimpleSkeleton
from .GdbusModemSimpleSkeletonClass import GdbusModemSimpleSkeletonClass
from .GdbusModemSimpleSkeletonPrivate import GdbusModemSimpleSkeletonPrivate
from .GdbusModemSkeleton import GdbusModemSkeleton
from .GdbusModemSkeletonClass import GdbusModemSkeletonClass
from .GdbusModemSkeletonPrivate import GdbusModemSkeletonPrivate
from .GdbusModemTime import GdbusModemTime
from .GdbusModemTimeIface import GdbusModemTimeIface
from .GdbusModemTimeProxy import GdbusModemTimeProxy
from .GdbusModemTimeProxyClass import GdbusModemTimeProxyClass
from .GdbusModemTimeProxyPrivate import GdbusModemTimeProxyPrivate
from .GdbusModemTimeSkeleton import GdbusModemTimeSkeleton
from .GdbusModemTimeSkeletonClass import GdbusModemTimeSkeletonClass
from .GdbusModemTimeSkeletonPrivate import GdbusModemTimeSkeletonPrivate
from .GdbusModemVoice import GdbusModemVoice
from .GdbusModemVoiceIface import GdbusModemVoiceIface
from .GdbusModemVoiceProxy import GdbusModemVoiceProxy
from .GdbusModemVoiceProxyClass import GdbusModemVoiceProxyClass
from .GdbusModemVoiceProxyPrivate import GdbusModemVoiceProxyPrivate
from .GdbusModemVoiceSkeleton import GdbusModemVoiceSkeleton
from .GdbusModemVoiceSkeletonClass import GdbusModemVoiceSkeletonClass
from .GdbusModemVoiceSkeletonPrivate import GdbusModemVoiceSkeletonPrivate
from .GdbusObject import GdbusObject
from .GdbusObjectIface import GdbusObjectIface
from .GdbusObjectManagerClient import GdbusObjectManagerClient
from .GdbusObjectManagerClientClass import GdbusObjectManagerClientClass
from .GdbusObjectManagerClientPrivate import GdbusObjectManagerClientPrivate
from .GdbusObjectProxy import GdbusObjectProxy
from .GdbusObjectProxyClass import GdbusObjectProxyClass
from .GdbusObjectProxyPrivate import GdbusObjectProxyPrivate
from .GdbusObjectSkeleton import GdbusObjectSkeleton
from .GdbusObjectSkeletonClass import GdbusObjectSkeletonClass
from .GdbusObjectSkeletonPrivate import GdbusObjectSkeletonPrivate
from .GdbusOrgFreedesktopModemManager1 import GdbusOrgFreedesktopModemManager1
from .GdbusOrgFreedesktopModemManager1Iface import GdbusOrgFreedesktopModemManager1Iface
from .GdbusOrgFreedesktopModemManager1Proxy import GdbusOrgFreedesktopModemManager1Proxy
from .GdbusOrgFreedesktopModemManager1ProxyClass import GdbusOrgFreedesktopModemManager1ProxyClass
from .GdbusOrgFreedesktopModemManager1ProxyPrivate import GdbusOrgFreedesktopModemManager1ProxyPrivate
from .GdbusOrgFreedesktopModemManager1Skeleton import GdbusOrgFreedesktopModemManager1Skeleton
from .GdbusOrgFreedesktopModemManager1SkeletonClass import GdbusOrgFreedesktopModemManager1SkeletonClass
from .GdbusOrgFreedesktopModemManager1SkeletonPrivate import GdbusOrgFreedesktopModemManager1SkeletonPrivate
from .GdbusSim import GdbusSim
from .GdbusSimIface import GdbusSimIface
from .GdbusSimProxy import GdbusSimProxy
from .GdbusSimProxyClass import GdbusSimProxyClass
from .GdbusSimProxyPrivate import GdbusSimProxyPrivate
from .GdbusSimSkeleton import GdbusSimSkeleton
from .GdbusSimSkeletonClass import GdbusSimSkeletonClass
from .GdbusSimSkeletonPrivate import GdbusSimSkeletonPrivate
from .GdbusSms import GdbusSms
from .GdbusSmsIface import GdbusSmsIface
from .GdbusSmsProxy import GdbusSmsProxy
from .GdbusSmsProxyClass import GdbusSmsProxyClass
from .GdbusSmsProxyPrivate import GdbusSmsProxyPrivate
from .GdbusSmsSkeleton import GdbusSmsSkeleton
from .GdbusSmsSkeletonClass import GdbusSmsSkeletonClass
from .GdbusSmsSkeletonPrivate import GdbusSmsSkeletonPrivate
from .KernelEventProperties import KernelEventProperties
from .KernelEventPropertiesClass import KernelEventPropertiesClass
from .KernelEventPropertiesPrivate import KernelEventPropertiesPrivate
from .Location3gpp import Location3gpp
from .Location3gppClass import Location3gppClass
from .Location3gppPrivate import Location3gppPrivate
from .LocationCdmaBs import LocationCdmaBs
from .LocationCdmaBsClass import LocationCdmaBsClass
from .LocationCdmaBsPrivate import LocationCdmaBsPrivate
from .LocationGpsNmea import LocationGpsNmea
from .LocationGpsNmeaClass import LocationGpsNmeaClass
from .LocationGpsNmeaPrivate import LocationGpsNmeaPrivate
from .LocationGpsRaw import LocationGpsRaw
from .LocationGpsRawClass import LocationGpsRawClass
from .LocationGpsRawPrivate import LocationGpsRawPrivate
from .Manager import Manager
from .ManagerClass import ManagerClass
from .ManagerPrivate import ManagerPrivate
from .MessageError import MessageError
from .MobileEquipmentError import MobileEquipmentError
from .Modem import Modem
from .Modem3gpp import Modem3gpp
from .Modem3gppClass import Modem3gppClass
from .Modem3gppEpsUeModeOperation import Modem3gppEpsUeModeOperation
from .Modem3gppFacility import Modem3gppFacility
from .Modem3gppNetwork import Modem3gppNetwork
from .Modem3gppNetworkAvailability import Modem3gppNetworkAvailability
from .Modem3gppPrivate import Modem3gppPrivate
from .Modem3gppRegistrationState import Modem3gppRegistrationState
from .Modem3gppSubscriptionState import Modem3gppSubscriptionState
from .Modem3gppUssd import Modem3gppUssd
from .Modem3gppUssdClass import Modem3gppUssdClass
from .Modem3gppUssdSessionState import Modem3gppUssdSessionState
from .ModemAccessTechnology import ModemAccessTechnology
from .ModemBand import ModemBand
from .ModemCapability import ModemCapability
from .ModemCdma import ModemCdma
from .ModemCdmaActivationState import ModemCdmaActivationState
from .ModemCdmaClass import ModemCdmaClass
from .ModemCdmaRegistrationState import ModemCdmaRegistrationState
from .ModemCdmaRmProtocol import ModemCdmaRmProtocol
from .ModemClass import ModemClass
from .ModemContactsStorage import ModemContactsStorage
from .ModemFirmware import ModemFirmware
from .ModemFirmwareClass import ModemFirmwareClass
from .ModemFirmwarePrivate import ModemFirmwarePrivate
from .ModemFirmwareUpdateMethod import ModemFirmwareUpdateMethod
from .ModemLocation import ModemLocation
from .ModemLocationAssistanceDataType import ModemLocationAssistanceDataType
from .ModemLocationClass import ModemLocationClass
from .ModemLocationSource import ModemLocationSource
from .ModemLock import ModemLock
from .ModemMessaging import ModemMessaging
from .ModemMessagingClass import ModemMessagingClass
from .ModemMessagingPrivate import ModemMessagingPrivate
from .ModemMode import ModemMode
from .ModemModeCombination import ModemModeCombination
from .ModemOma import ModemOma
from .ModemOmaClass import ModemOmaClass
from .ModemOmaPrivate import ModemOmaPrivate
from .ModemPortInfo import ModemPortInfo
from .ModemPortType import ModemPortType
from .ModemPowerState import ModemPowerState
from .ModemPrivate import ModemPrivate
from .ModemSignal import ModemSignal
from .ModemSignalClass import ModemSignalClass
from .ModemSignalPrivate import ModemSignalPrivate
from .ModemSimple import ModemSimple
from .ModemSimpleClass import ModemSimpleClass
from .ModemState import ModemState
from .ModemStateChangeReason import ModemStateChangeReason
from .ModemStateFailedReason import ModemStateFailedReason
from .ModemTime import ModemTime
from .ModemTimeClass import ModemTimeClass
from .ModemTimePrivate import ModemTimePrivate
from .ModemVoice import ModemVoice
from .ModemVoiceClass import ModemVoiceClass
from .ModemVoicePrivate import ModemVoicePrivate
from .NetworkTimezone import NetworkTimezone
from .NetworkTimezoneClass import NetworkTimezoneClass
from .NetworkTimezonePrivate import NetworkTimezonePrivate
from .Object import Object
from .ObjectClass import ObjectClass
from .OmaFeature import OmaFeature
from .OmaPendingNetworkInitiatedSession import OmaPendingNetworkInitiatedSession
from .OmaSessionState import OmaSessionState
from .OmaSessionStateFailedReason import OmaSessionStateFailedReason
from .OmaSessionType import OmaSessionType
from .Pco import Pco
from .PcoClass import PcoClass
from .PcoPrivate import PcoPrivate
from .SerialError import SerialError
from .Signal import Signal
from .SignalClass import SignalClass
from .SignalPrivate import SignalPrivate
from .Sim import Sim
from .SimClass import SimClass
from .SimpleConnectProperties import SimpleConnectProperties
from .SimpleConnectPropertiesClass import SimpleConnectPropertiesClass
from .SimpleConnectPropertiesPrivate import SimpleConnectPropertiesPrivate
from .SimpleStatus import SimpleStatus
from .SimpleStatusClass import SimpleStatusClass
from .SimpleStatusPrivate import SimpleStatusPrivate
from .Sms import Sms
from .SmsCdmaServiceCategory import SmsCdmaServiceCategory
from .SmsCdmaTeleserviceId import SmsCdmaTeleserviceId
from .SmsClass import SmsClass
from .SmsDeliveryState import SmsDeliveryState
from .SmsPduType import SmsPduType
from .SmsProperties import SmsProperties
from .SmsPropertiesClass import SmsPropertiesClass
from .SmsPropertiesPrivate import SmsPropertiesPrivate
from .SmsState import SmsState
from .SmsStorage import SmsStorage
from .SmsValidityType import SmsValidityType
from .UnlockRetries import UnlockRetries
from .UnlockRetriesClass import UnlockRetriesClass
from .UnlockRetriesPrivate import UnlockRetriesPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f6944900d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/ModemManager-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.ModemManager', loader=<gi.importer.DynamicImporter object at 0x7f6944900d00>)"

