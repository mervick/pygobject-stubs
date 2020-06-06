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


from .Entry import Entry

class ContactsContact(Entry):
    """
    :Constructors:
    
    ::
    
        ContactsContact(**properties)
        new(id:str=None) -> GData.ContactsContact
    """
    def add_author(self, author): # real signature unknown; restored from __doc__
        """ add_author(self, author:GData.Author) """
        pass

    def add_calendar(self, calendar): # real signature unknown; restored from __doc__
        """ add_calendar(self, calendar:GData.GContactCalendar) """
        pass

    def add_category(self, category): # real signature unknown; restored from __doc__
        """ add_category(self, category:GData.Category) """
        pass

    def add_email_address(self, email_address): # real signature unknown; restored from __doc__
        """ add_email_address(self, email_address:GData.GDEmailAddress) """
        pass

    def add_event(self, event): # real signature unknown; restored from __doc__
        """ add_event(self, event:GData.GContactEvent) """
        pass

    def add_external_id(self, external_id): # real signature unknown; restored from __doc__
        """ add_external_id(self, external_id:GData.GContactExternalID) """
        pass

    def add_group(self, href): # real signature unknown; restored from __doc__
        """ add_group(self, href:str) """
        pass

    def add_hobby(self, hobby): # real signature unknown; restored from __doc__
        """ add_hobby(self, hobby:str) """
        pass

    def add_im_address(self, im_address): # real signature unknown; restored from __doc__
        """ add_im_address(self, im_address:GData.GDIMAddress) """
        pass

    def add_jot(self, jot): # real signature unknown; restored from __doc__
        """ add_jot(self, jot:GData.GContactJot) """
        pass

    def add_language(self, language): # real signature unknown; restored from __doc__
        """ add_language(self, language:GData.GContactLanguage) """
        pass

    def add_link(self, _link): # real signature unknown; restored from __doc__
        """ add_link(self, _link:GData.Link) """
        pass

    def add_organization(self, organization): # real signature unknown; restored from __doc__
        """ add_organization(self, organization:GData.GDOrganization) """
        pass

    def add_phone_number(self, phone_number): # real signature unknown; restored from __doc__
        """ add_phone_number(self, phone_number:GData.GDPhoneNumber) """
        pass

    def add_postal_address(self, postal_address): # real signature unknown; restored from __doc__
        """ add_postal_address(self, postal_address:GData.GDPostalAddress) """
        pass

    def add_relation(self, relation): # real signature unknown; restored from __doc__
        """ add_relation(self, relation:GData.GContactRelation) """
        pass

    def add_website(self, website): # real signature unknown; restored from __doc__
        """ add_website(self, website:GData.GContactWebsite) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_get_json(self, *args, **kwargs): # real signature unknown
        """ get_json(self, builder:Json.Builder) """
        pass

    def do_get_namespaces(self, *args, **kwargs): # real signature unknown
        """ get_namespaces(self, namespaces:dict) """
        pass

    def do_get_xml(self, *args, **kwargs): # real signature unknown
        """ get_xml(self, xml_string:GLib.String) """
        pass

    def do_parse_json(self, *args, **kwargs): # real signature unknown
        """ parse_json(self, reader:Json.Reader, user_data=None) -> bool """
        pass

    def do_parse_xml(self, *args, **kwargs): # real signature unknown
        """ parse_xml(self, doc:libxml2.Doc, node:libxml2.Node, user_data=None) -> bool """
        pass

    def do_post_parse_json(self, *args, **kwargs): # real signature unknown
        """ post_parse_json(self, user_data=None) -> bool """
        pass

    def do_post_parse_xml(self, *args, **kwargs): # real signature unknown
        """ post_parse_xml(self, user_data=None) -> bool """
        pass

    def do_pre_get_xml(self, *args, **kwargs): # real signature unknown
        """ pre_get_xml(self, xml_string:GLib.String) """
        pass

    def do_pre_parse_xml(self, *args, **kwargs): # real signature unknown
        """ pre_parse_xml(self, doc:libxml2.Doc, root_node:libxml2.Node, user_data=None) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_authors(self): # real signature unknown; restored from __doc__
        """ get_authors(self) -> list """
        return []

    def get_billing_information(self): # real signature unknown; restored from __doc__
        """ get_billing_information(self) -> str """
        return ""

    def get_birthday(self): # real signature unknown; restored from __doc__
        """ get_birthday(self) -> bool, birthday:GLib.Date """
        return False

    def get_calendars(self): # real signature unknown; restored from __doc__
        """ get_calendars(self) -> list """
        return []

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> list """
        return []

    def get_content(self): # real signature unknown; restored from __doc__
        """ get_content(self) -> str """
        return ""

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> str """
        return ""

    def get_content_uri(self): # real signature unknown; restored from __doc__
        """ get_content_uri(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_directory_server(self): # real signature unknown; restored from __doc__
        """ get_directory_server(self) -> str """
        return ""

    def get_edited(self): # real signature unknown; restored from __doc__
        """ get_edited(self) -> int """
        return 0

    def get_email_addresses(self): # real signature unknown; restored from __doc__
        """ get_email_addresses(self) -> list """
        return []

    def get_etag(self): # real signature unknown; restored from __doc__
        """ get_etag(self) -> str or None """
        return ""

    def get_events(self): # real signature unknown; restored from __doc__
        """ get_events(self) -> list """
        return []

    def get_extended_properties(self): # real signature unknown; restored from __doc__
        """ get_extended_properties(self) -> dict """
        return {}

    def get_extended_property(self, name): # real signature unknown; restored from __doc__
        """ get_extended_property(self, name:str) -> str """
        return ""

    def get_external_ids(self): # real signature unknown; restored from __doc__
        """ get_external_ids(self) -> list """
        return []

    def get_file_as(self): # real signature unknown; restored from __doc__
        """ get_file_as(self) -> str """
        return ""

    def get_gender(self): # real signature unknown; restored from __doc__
        """ get_gender(self) -> str """
        return ""

    def get_groups(self): # real signature unknown; restored from __doc__
        """ get_groups(self) -> list """
        return []

    def get_hobbies(self): # real signature unknown; restored from __doc__
        """ get_hobbies(self) -> list """
        return []

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str or None """
        return ""

    def get_im_addresses(self): # real signature unknown; restored from __doc__
        """ get_im_addresses(self) -> list """
        return []

    def get_initials(self): # real signature unknown; restored from __doc__
        """ get_initials(self) -> str """
        return ""

    def get_jots(self): # real signature unknown; restored from __doc__
        """ get_jots(self) -> list """
        return []

    def get_json(self): # real signature unknown; restored from __doc__
        """ get_json(self) -> str """
        return ""

    def get_languages(self): # real signature unknown; restored from __doc__
        """ get_languages(self) -> list """
        return []

    def get_maiden_name(self): # real signature unknown; restored from __doc__
        """ get_maiden_name(self) -> str """
        return ""

    def get_mileage(self): # real signature unknown; restored from __doc__
        """ get_mileage(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> GData.GDName """
        pass

    def get_nickname(self): # real signature unknown; restored from __doc__
        """ get_nickname(self) -> str """
        return ""

    def get_occupation(self): # real signature unknown; restored from __doc__
        """ get_occupation(self) -> str """
        return ""

    def get_organizations(self): # real signature unknown; restored from __doc__
        """ get_organizations(self) -> list """
        return []

    def get_phone_numbers(self): # real signature unknown; restored from __doc__
        """ get_phone_numbers(self) -> list """
        return []

    def get_photo(self, service, cancellable=None): # real signature unknown; restored from __doc__
        """ get_photo(self, service:GData.ContactsService, cancellable:Gio.Cancellable=None) -> list, length:int, content_type:str """
        return []

    def get_photo_async(self, service, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_photo_async(self, service:GData.ContactsService, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_photo_etag(self): # real signature unknown; restored from __doc__
        """ get_photo_etag(self) -> str """
        return ""

    def get_photo_finish(self, async_result): # real signature unknown; restored from __doc__
        """ get_photo_finish(self, async_result:Gio.AsyncResult) -> list, length:int, content_type:str """
        return []

    def get_postal_addresses(self): # real signature unknown; restored from __doc__
        """ get_postal_addresses(self) -> list """
        return []

    def get_primary_calendar(self): # real signature unknown; restored from __doc__
        """ get_primary_calendar(self) -> GData.GContactCalendar """
        pass

    def get_primary_email_address(self): # real signature unknown; restored from __doc__
        """ get_primary_email_address(self) -> GData.GDEmailAddress """
        pass

    def get_primary_im_address(self): # real signature unknown; restored from __doc__
        """ get_primary_im_address(self) -> GData.GDIMAddress """
        pass

    def get_primary_organization(self): # real signature unknown; restored from __doc__
        """ get_primary_organization(self) -> GData.GDOrganization """
        pass

    def get_primary_phone_number(self): # real signature unknown; restored from __doc__
        """ get_primary_phone_number(self) -> GData.GDPhoneNumber """
        pass

    def get_primary_postal_address(self): # real signature unknown; restored from __doc__
        """ get_primary_postal_address(self) -> GData.GDPostalAddress """
        pass

    def get_primary_website(self): # real signature unknown; restored from __doc__
        """ get_primary_website(self) -> GData.GContactWebsite """
        pass

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_published(self): # real signature unknown; restored from __doc__
        """ get_published(self) -> int """
        return 0

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_relations(self): # real signature unknown; restored from __doc__
        """ get_relations(self) -> list """
        return []

    def get_rights(self): # real signature unknown; restored from __doc__
        """ get_rights(self) -> str """
        return ""

    def get_sensitivity(self): # real signature unknown; restored from __doc__
        """ get_sensitivity(self) -> str """
        return ""

    def get_short_name(self): # real signature unknown; restored from __doc__
        """ get_short_name(self) -> str """
        return ""

    def get_subject(self): # real signature unknown; restored from __doc__
        """ get_subject(self) -> str """
        return ""

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_updated(self): # real signature unknown; restored from __doc__
        """ get_updated(self) -> int """
        return 0

    def get_user_defined_field(self, name): # real signature unknown; restored from __doc__
        """ get_user_defined_field(self, name:str) -> str """
        return ""

    def get_user_defined_fields(self): # real signature unknown; restored from __doc__
        """ get_user_defined_fields(self) -> dict """
        return {}

    def get_websites(self): # real signature unknown; restored from __doc__
        """ get_websites(self) -> list """
        return []

    def get_xml(self): # real signature unknown; restored from __doc__
        """ get_xml(self) -> str """
        return ""

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_deleted(self): # real signature unknown; restored from __doc__
        """ is_deleted(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_group_deleted(self, href): # real signature unknown; restored from __doc__
        """ is_group_deleted(self, href:str) -> bool """
        return False

    def is_inserted(self): # real signature unknown; restored from __doc__
        """ is_inserted(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def look_up_link(self, rel): # real signature unknown; restored from __doc__
        """ look_up_link(self, rel:str) -> GData.Link """
        pass

    def look_up_links(self, rel): # real signature unknown; restored from __doc__
        """ look_up_links(self, rel:str) -> list """
        return []

    def new(self, id=None): # real signature unknown; restored from __doc__
        """ new(id:str=None) -> GData.ContactsContact """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_json(self, parsable_type, json, length): # real signature unknown; restored from __doc__
        """ new_from_json(parsable_type:GType, json:str, length:int) -> GData.Parsable """
        pass

    def new_from_xml(self, parsable_type, xml, length): # real signature unknown; restored from __doc__
        """ new_from_xml(parsable_type:GType, xml:str, length:int) -> GData.Parsable """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_all_calendars(self): # real signature unknown; restored from __doc__
        """ remove_all_calendars(self) """
        pass

    def remove_all_email_addresses(self): # real signature unknown; restored from __doc__
        """ remove_all_email_addresses(self) """
        pass

    def remove_all_events(self): # real signature unknown; restored from __doc__
        """ remove_all_events(self) """
        pass

    def remove_all_external_ids(self): # real signature unknown; restored from __doc__
        """ remove_all_external_ids(self) """
        pass

    def remove_all_hobbies(self): # real signature unknown; restored from __doc__
        """ remove_all_hobbies(self) """
        pass

    def remove_all_im_addresses(self): # real signature unknown; restored from __doc__
        """ remove_all_im_addresses(self) """
        pass

    def remove_all_jots(self): # real signature unknown; restored from __doc__
        """ remove_all_jots(self) """
        pass

    def remove_all_languages(self): # real signature unknown; restored from __doc__
        """ remove_all_languages(self) """
        pass

    def remove_all_organizations(self): # real signature unknown; restored from __doc__
        """ remove_all_organizations(self) """
        pass

    def remove_all_phone_numbers(self): # real signature unknown; restored from __doc__
        """ remove_all_phone_numbers(self) """
        pass

    def remove_all_postal_addresses(self): # real signature unknown; restored from __doc__
        """ remove_all_postal_addresses(self) """
        pass

    def remove_all_relations(self): # real signature unknown; restored from __doc__
        """ remove_all_relations(self) """
        pass

    def remove_all_websites(self): # real signature unknown; restored from __doc__
        """ remove_all_websites(self) """
        pass

    def remove_group(self, href): # real signature unknown; restored from __doc__
        """ remove_group(self, href:str) """
        pass

    def remove_link(self, _link): # real signature unknown; restored from __doc__
        """ remove_link(self, _link:GData.Link) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_billing_information(self, billing_information=None): # real signature unknown; restored from __doc__
        """ set_billing_information(self, billing_information:str=None) """
        pass

    def set_birthday(self, birthday=None, birthday_has_year): # real signature unknown; restored from __doc__
        """ set_birthday(self, birthday:GLib.Date=None, birthday_has_year:bool) """
        pass

    def set_content(self, content=None): # real signature unknown; restored from __doc__
        """ set_content(self, content:str=None) """
        pass

    def set_content_uri(self, content_uri=None): # real signature unknown; restored from __doc__
        """ set_content_uri(self, content_uri:str=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_directory_server(self, directory_server=None): # real signature unknown; restored from __doc__
        """ set_directory_server(self, directory_server:str=None) """
        pass

    def set_extended_property(self, name, value=None): # real signature unknown; restored from __doc__
        """ set_extended_property(self, name:str, value:str=None) -> bool """
        return False

    def set_file_as(self, file_as=None): # real signature unknown; restored from __doc__
        """ set_file_as(self, file_as:str=None) """
        pass

    def set_gender(self, gender=None): # real signature unknown; restored from __doc__
        """ set_gender(self, gender:str=None) """
        pass

    def set_initials(self, initials=None): # real signature unknown; restored from __doc__
        """ set_initials(self, initials:str=None) """
        pass

    def set_maiden_name(self, maiden_name=None): # real signature unknown; restored from __doc__
        """ set_maiden_name(self, maiden_name:str=None) """
        pass

    def set_mileage(self, mileage=None): # real signature unknown; restored from __doc__
        """ set_mileage(self, mileage:str=None) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:GData.GDName) """
        pass

    def set_nickname(self, nickname=None): # real signature unknown; restored from __doc__
        """ set_nickname(self, nickname:str=None) """
        pass

    def set_occupation(self, occupation=None): # real signature unknown; restored from __doc__
        """ set_occupation(self, occupation:str=None) """
        pass

    def set_photo(self, service, data=None, length, content_type=None, cancellable=None): # real signature unknown; restored from __doc__
        """ set_photo(self, service:GData.ContactsService, data:int=None, length:int, content_type:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_photo_async(self, service, data=None, length, content_type=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_photo_async(self, service:GData.ContactsService, data:int=None, length:int, content_type:str=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_photo_finish(self, async_result): # real signature unknown; restored from __doc__
        """ set_photo_finish(self, async_result:Gio.AsyncResult) -> bool """
        return False

    def set_priority(self, priority=None): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_rights(self, rights=None): # real signature unknown; restored from __doc__
        """ set_rights(self, rights:str=None) """
        pass

    def set_sensitivity(self, sensitivity=None): # real signature unknown; restored from __doc__
        """ set_sensitivity(self, sensitivity:str=None) """
        pass

    def set_short_name(self, short_name=None): # real signature unknown; restored from __doc__
        """ set_short_name(self, short_name:str=None) """
        pass

    def set_subject(self, subject=None): # real signature unknown; restored from __doc__
        """ set_subject(self, subject:str=None) """
        pass

    def set_summary(self, summary=None): # real signature unknown; restored from __doc__
        """ set_summary(self, summary:str=None) """
        pass

    def set_title(self, title=None): # real signature unknown; restored from __doc__
        """ set_title(self, title:str=None) """
        pass

    def set_user_defined_field(self, name, value=None): # real signature unknown; restored from __doc__
        """ set_user_defined_field(self, name:str, value:str=None) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fd5e170ddf0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ContactsContact), '__module__': 'gi.repository.GData', '__gtype__': <GType GDataContactsContact (94233464393200)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_calendar': gi.FunctionInfo(add_calendar), 'add_email_address': gi.FunctionInfo(add_email_address), 'add_event': gi.FunctionInfo(add_event), 'add_external_id': gi.FunctionInfo(add_external_id), 'add_group': gi.FunctionInfo(add_group), 'add_hobby': gi.FunctionInfo(add_hobby), 'add_im_address': gi.FunctionInfo(add_im_address), 'add_jot': gi.FunctionInfo(add_jot), 'add_language': gi.FunctionInfo(add_language), 'add_organization': gi.FunctionInfo(add_organization), 'add_phone_number': gi.FunctionInfo(add_phone_number), 'add_postal_address': gi.FunctionInfo(add_postal_address), 'add_relation': gi.FunctionInfo(add_relation), 'add_website': gi.FunctionInfo(add_website), 'get_billing_information': gi.FunctionInfo(get_billing_information), 'get_birthday': gi.FunctionInfo(get_birthday), 'get_calendars': gi.FunctionInfo(get_calendars), 'get_directory_server': gi.FunctionInfo(get_directory_server), 'get_edited': gi.FunctionInfo(get_edited), 'get_email_addresses': gi.FunctionInfo(get_email_addresses), 'get_events': gi.FunctionInfo(get_events), 'get_extended_properties': gi.FunctionInfo(get_extended_properties), 'get_extended_property': gi.FunctionInfo(get_extended_property), 'get_external_ids': gi.FunctionInfo(get_external_ids), 'get_file_as': gi.FunctionInfo(get_file_as), 'get_gender': gi.FunctionInfo(get_gender), 'get_groups': gi.FunctionInfo(get_groups), 'get_hobbies': gi.FunctionInfo(get_hobbies), 'get_im_addresses': gi.FunctionInfo(get_im_addresses), 'get_initials': gi.FunctionInfo(get_initials), 'get_jots': gi.FunctionInfo(get_jots), 'get_languages': gi.FunctionInfo(get_languages), 'get_maiden_name': gi.FunctionInfo(get_maiden_name), 'get_mileage': gi.FunctionInfo(get_mileage), 'get_name': gi.FunctionInfo(get_name), 'get_nickname': gi.FunctionInfo(get_nickname), 'get_occupation': gi.FunctionInfo(get_occupation), 'get_organizations': gi.FunctionInfo(get_organizations), 'get_phone_numbers': gi.FunctionInfo(get_phone_numbers), 'get_photo': gi.FunctionInfo(get_photo), 'get_photo_async': gi.FunctionInfo(get_photo_async), 'get_photo_etag': gi.FunctionInfo(get_photo_etag), 'get_photo_finish': gi.FunctionInfo(get_photo_finish), 'get_postal_addresses': gi.FunctionInfo(get_postal_addresses), 'get_primary_calendar': gi.FunctionInfo(get_primary_calendar), 'get_primary_email_address': gi.FunctionInfo(get_primary_email_address), 'get_primary_im_address': gi.FunctionInfo(get_primary_im_address), 'get_primary_organization': gi.FunctionInfo(get_primary_organization), 'get_primary_phone_number': gi.FunctionInfo(get_primary_phone_number), 'get_primary_postal_address': gi.FunctionInfo(get_primary_postal_address), 'get_primary_website': gi.FunctionInfo(get_primary_website), 'get_priority': gi.FunctionInfo(get_priority), 'get_relations': gi.FunctionInfo(get_relations), 'get_sensitivity': gi.FunctionInfo(get_sensitivity), 'get_short_name': gi.FunctionInfo(get_short_name), 'get_subject': gi.FunctionInfo(get_subject), 'get_user_defined_field': gi.FunctionInfo(get_user_defined_field), 'get_user_defined_fields': gi.FunctionInfo(get_user_defined_fields), 'get_websites': gi.FunctionInfo(get_websites), 'is_deleted': gi.FunctionInfo(is_deleted), 'is_group_deleted': gi.FunctionInfo(is_group_deleted), 'remove_all_calendars': gi.FunctionInfo(remove_all_calendars), 'remove_all_email_addresses': gi.FunctionInfo(remove_all_email_addresses), 'remove_all_events': gi.FunctionInfo(remove_all_events), 'remove_all_external_ids': gi.FunctionInfo(remove_all_external_ids), 'remove_all_hobbies': gi.FunctionInfo(remove_all_hobbies), 'remove_all_im_addresses': gi.FunctionInfo(remove_all_im_addresses), 'remove_all_jots': gi.FunctionInfo(remove_all_jots), 'remove_all_languages': gi.FunctionInfo(remove_all_languages), 'remove_all_organizations': gi.FunctionInfo(remove_all_organizations), 'remove_all_phone_numbers': gi.FunctionInfo(remove_all_phone_numbers), 'remove_all_postal_addresses': gi.FunctionInfo(remove_all_postal_addresses), 'remove_all_relations': gi.FunctionInfo(remove_all_relations), 'remove_all_websites': gi.FunctionInfo(remove_all_websites), 'remove_group': gi.FunctionInfo(remove_group), 'set_billing_information': gi.FunctionInfo(set_billing_information), 'set_birthday': gi.FunctionInfo(set_birthday), 'set_directory_server': gi.FunctionInfo(set_directory_server), 'set_extended_property': gi.FunctionInfo(set_extended_property), 'set_file_as': gi.FunctionInfo(set_file_as), 'set_gender': gi.FunctionInfo(set_gender), 'set_initials': gi.FunctionInfo(set_initials), 'set_maiden_name': gi.FunctionInfo(set_maiden_name), 'set_mileage': gi.FunctionInfo(set_mileage), 'set_name': gi.FunctionInfo(set_name), 'set_nickname': gi.FunctionInfo(set_nickname), 'set_occupation': gi.FunctionInfo(set_occupation), 'set_photo': gi.FunctionInfo(set_photo), 'set_photo_async': gi.FunctionInfo(set_photo_async), 'set_photo_finish': gi.FunctionInfo(set_photo_finish), 'set_priority': gi.FunctionInfo(set_priority), 'set_sensitivity': gi.FunctionInfo(set_sensitivity), 'set_short_name': gi.FunctionInfo(set_short_name), 'set_subject': gi.FunctionInfo(set_subject), 'set_user_defined_field': gi.FunctionInfo(set_user_defined_field), 'parent': <property object at 0x7fd5e17864f0>, 'priv': <property object at 0x7fd5e17865e0>})"
    __gdoc__ = "Object GDataContactsContact\n\nProperties from GDataContactsContact:\n  edited -> gint64: Edited\n    The last time the contact was edited.\n  deleted -> gboolean: Deleted\n    Whether the entry has been deleted.\n  name -> GDataGDName: Name\n    The contact's name in a structured representation.\n  nickname -> gchararray: Nickname\n    The contact's chosen nickname.\n  birthday -> GDate: Birthday\n    The contact's birthday.\n  birthday-has-year -> gboolean: Birthday has year?\n    Whether the contact's birthday includes their year of birth.\n  billing-information -> gchararray: Billing information\n    Billing information for the contact.\n  directory-server -> gchararray: Directory server\n    The name or address of an associated directory server.\n  gender -> gchararray: Gender\n    The gender of the contact.\n  initials -> gchararray: Initials\n    The initials of the contact.\n  maiden-name -> gchararray: Maiden name\n    The maiden name of the contact.\n  mileage -> gchararray: Mileage\n    A mileage associated with the contact.\n  occupation -> gchararray: Occupation\n    The contact's occupation.\n  priority -> gchararray: Priority\n    The contact's importance.\n  sensitivity -> gchararray: Sensitivity\n    The sensitivity of the contact's data.\n  short-name -> gchararray: Short name\n    A short name for the contact.\n  subject -> gchararray: Subject\n    The subject of the contact.\n  photo-etag -> gchararray: Photo ETag\n    The ETag of the contact's photo.\n  file-as -> gchararray: File As\n    The name to file the contact under for sorting purposes.\n\nProperties from GDataEntry:\n  title -> gchararray: Title\n    A human-readable title for the entry.\n  summary -> gchararray: Summary\n    A short summary, abstract, or excerpt of the entry.\n  etag -> gchararray: ETag\n    An identifier for a particular version of the entry.\n  id -> gchararray: ID\n    A permanent, universally unique identifier for the entry, in IRI form.\n  updated -> gint64: Updated\n    The date and time when the entry was most recently updated significantly.\n  published -> gint64: Published\n    The date and time the entry was first published or made available.\n  content -> gchararray: Content\n    The content of the entry.\n  is-inserted -> gboolean: Inserted?\n    Whether the entry has been inserted on the server.\n  rights -> gchararray: Rights\n    The ownership rights pertaining to the entry.\n  content-uri -> gchararray: Content URI\n    A URI pointing to the location of the content of the entry.\n\nProperties from GDataParsable:\n  constructed-from-xml -> gboolean: Constructed from XML?\n    Specifies whether the object was constructed by parsing XML or manually.\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDataContactsContact (94233464393200)>'
    __info__ = ObjectInfo(ContactsContact)


