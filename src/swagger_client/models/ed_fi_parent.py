# coding: utf-8

"""
    Ed-Fi Operational Data Store API

    The Ed-Fi ODS / API enables applications to read and write education data stored in an Ed-Fi ODS through a secure REST interface.  ***  > *Note: Consumers of ODS / API information should sanitize all data for display and storage. The ODS / API provides reasonable safeguards against cross-site scripting attacks and other malicious content, but the platform does not and cannot guarantee that the data it contains is free of all potentially harmful content.*  ***   # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EdFiParent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'parent_unique_id': 'str',
        'person_reference': 'EdFiPersonReference',
        'addresses': 'list[EdFiParentAddress]',
        'electronic_mails': 'list[EdFiParentElectronicMail]',
        'first_name': 'str',
        'generation_code_suffix': 'str',
        'international_addresses': 'list[EdFiParentInternationalAddress]',
        'languages': 'list[EdFiParentLanguage]',
        'last_surname': 'str',
        'login_id': 'str',
        'maiden_name': 'str',
        'middle_name': 'str',
        'other_names': 'list[EdFiParentOtherName]',
        'personal_identification_documents': 'list[EdFiParentPersonalIdentificationDocument]',
        'personal_title_prefix': 'str',
        'sex_descriptor': 'str',
        'telephones': 'list[EdFiParentTelephone]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_unique_id': 'parentUniqueId',
        'person_reference': 'personReference',
        'addresses': 'addresses',
        'electronic_mails': 'electronicMails',
        'first_name': 'firstName',
        'generation_code_suffix': 'generationCodeSuffix',
        'international_addresses': 'internationalAddresses',
        'languages': 'languages',
        'last_surname': 'lastSurname',
        'login_id': 'loginId',
        'maiden_name': 'maidenName',
        'middle_name': 'middleName',
        'other_names': 'otherNames',
        'personal_identification_documents': 'personalIdentificationDocuments',
        'personal_title_prefix': 'personalTitlePrefix',
        'sex_descriptor': 'sexDescriptor',
        'telephones': 'telephones',
        'etag': '_etag'
    }

    def __init__(self, id=None, parent_unique_id=None, person_reference=None, addresses=None, electronic_mails=None, first_name=None, generation_code_suffix=None, international_addresses=None, languages=None, last_surname=None, login_id=None, maiden_name=None, middle_name=None, other_names=None, personal_identification_documents=None, personal_title_prefix=None, sex_descriptor=None, telephones=None, etag=None):  # noqa: E501
        """EdFiParent - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._parent_unique_id = None
        self._person_reference = None
        self._addresses = None
        self._electronic_mails = None
        self._first_name = None
        self._generation_code_suffix = None
        self._international_addresses = None
        self._languages = None
        self._last_surname = None
        self._login_id = None
        self._maiden_name = None
        self._middle_name = None
        self._other_names = None
        self._personal_identification_documents = None
        self._personal_title_prefix = None
        self._sex_descriptor = None
        self._telephones = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.parent_unique_id = parent_unique_id
        if person_reference is not None:
            self.person_reference = person_reference
        if addresses is not None:
            self.addresses = addresses
        if electronic_mails is not None:
            self.electronic_mails = electronic_mails
        self.first_name = first_name
        if generation_code_suffix is not None:
            self.generation_code_suffix = generation_code_suffix
        if international_addresses is not None:
            self.international_addresses = international_addresses
        if languages is not None:
            self.languages = languages
        self.last_surname = last_surname
        if login_id is not None:
            self.login_id = login_id
        if maiden_name is not None:
            self.maiden_name = maiden_name
        if middle_name is not None:
            self.middle_name = middle_name
        if other_names is not None:
            self.other_names = other_names
        if personal_identification_documents is not None:
            self.personal_identification_documents = personal_identification_documents
        if personal_title_prefix is not None:
            self.personal_title_prefix = personal_title_prefix
        if sex_descriptor is not None:
            self.sex_descriptor = sex_descriptor
        if telephones is not None:
            self.telephones = telephones
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiParent.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiParent.

          # noqa: E501

        :param id: The id of this EdFiParent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parent_unique_id(self):
        """Gets the parent_unique_id of this EdFiParent.  # noqa: E501

        A unique alphanumeric code assigned to a parent.  # noqa: E501

        :return: The parent_unique_id of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._parent_unique_id

    @parent_unique_id.setter
    def parent_unique_id(self, parent_unique_id):
        """Sets the parent_unique_id of this EdFiParent.

        A unique alphanumeric code assigned to a parent.  # noqa: E501

        :param parent_unique_id: The parent_unique_id of this EdFiParent.  # noqa: E501
        :type: str
        """
        if parent_unique_id is None:
            raise ValueError("Invalid value for `parent_unique_id`, must not be `None`")  # noqa: E501
        if parent_unique_id is not None and len(parent_unique_id) > 32:
            raise ValueError("Invalid value for `parent_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._parent_unique_id = parent_unique_id

    @property
    def person_reference(self):
        """Gets the person_reference of this EdFiParent.  # noqa: E501


        :return: The person_reference of this EdFiParent.  # noqa: E501
        :rtype: EdFiPersonReference
        """
        return self._person_reference

    @person_reference.setter
    def person_reference(self, person_reference):
        """Sets the person_reference of this EdFiParent.


        :param person_reference: The person_reference of this EdFiParent.  # noqa: E501
        :type: EdFiPersonReference
        """

        self._person_reference = person_reference

    @property
    def addresses(self):
        """Gets the addresses of this EdFiParent.  # noqa: E501

        An unordered collection of parentAddresses. Parent's address, if different from the student address.  # noqa: E501

        :return: The addresses of this EdFiParent.  # noqa: E501
        :rtype: list[EdFiParentAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this EdFiParent.

        An unordered collection of parentAddresses. Parent's address, if different from the student address.  # noqa: E501

        :param addresses: The addresses of this EdFiParent.  # noqa: E501
        :type: list[EdFiParentAddress]
        """

        self._addresses = addresses

    @property
    def electronic_mails(self):
        """Gets the electronic_mails of this EdFiParent.  # noqa: E501

        An unordered collection of parentElectronicMails. The numbers, letters, and symbols used to identify an electronic mail (e-mail) user within the network to which the individual or organization belongs.  # noqa: E501

        :return: The electronic_mails of this EdFiParent.  # noqa: E501
        :rtype: list[EdFiParentElectronicMail]
        """
        return self._electronic_mails

    @electronic_mails.setter
    def electronic_mails(self, electronic_mails):
        """Sets the electronic_mails of this EdFiParent.

        An unordered collection of parentElectronicMails. The numbers, letters, and symbols used to identify an electronic mail (e-mail) user within the network to which the individual or organization belongs.  # noqa: E501

        :param electronic_mails: The electronic_mails of this EdFiParent.  # noqa: E501
        :type: list[EdFiParentElectronicMail]
        """

        self._electronic_mails = electronic_mails

    @property
    def first_name(self):
        """Gets the first_name of this EdFiParent.  # noqa: E501

        A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change.  # noqa: E501

        :return: The first_name of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this EdFiParent.

        A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change.  # noqa: E501

        :param first_name: The first_name of this EdFiParent.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if first_name is not None and len(first_name) > 75:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `75`")  # noqa: E501

        self._first_name = first_name

    @property
    def generation_code_suffix(self):
        """Gets the generation_code_suffix of this EdFiParent.  # noqa: E501

        An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III).  # noqa: E501

        :return: The generation_code_suffix of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._generation_code_suffix

    @generation_code_suffix.setter
    def generation_code_suffix(self, generation_code_suffix):
        """Sets the generation_code_suffix of this EdFiParent.

        An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III).  # noqa: E501

        :param generation_code_suffix: The generation_code_suffix of this EdFiParent.  # noqa: E501
        :type: str
        """
        if generation_code_suffix is not None and len(generation_code_suffix) > 10:
            raise ValueError("Invalid value for `generation_code_suffix`, length must be less than or equal to `10`")  # noqa: E501

        self._generation_code_suffix = generation_code_suffix

    @property
    def international_addresses(self):
        """Gets the international_addresses of this EdFiParent.  # noqa: E501

        An unordered collection of parentInternationalAddresses. The set of elements that describes an international address.  # noqa: E501

        :return: The international_addresses of this EdFiParent.  # noqa: E501
        :rtype: list[EdFiParentInternationalAddress]
        """
        return self._international_addresses

    @international_addresses.setter
    def international_addresses(self, international_addresses):
        """Sets the international_addresses of this EdFiParent.

        An unordered collection of parentInternationalAddresses. The set of elements that describes an international address.  # noqa: E501

        :param international_addresses: The international_addresses of this EdFiParent.  # noqa: E501
        :type: list[EdFiParentInternationalAddress]
        """

        self._international_addresses = international_addresses

    @property
    def languages(self):
        """Gets the languages of this EdFiParent.  # noqa: E501

        An unordered collection of parentLanguages. The language(s) the individual uses to communicate. It is strongly recommended that entries use only ISO 639-2 language codes.  # noqa: E501

        :return: The languages of this EdFiParent.  # noqa: E501
        :rtype: list[EdFiParentLanguage]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this EdFiParent.

        An unordered collection of parentLanguages. The language(s) the individual uses to communicate. It is strongly recommended that entries use only ISO 639-2 language codes.  # noqa: E501

        :param languages: The languages of this EdFiParent.  # noqa: E501
        :type: list[EdFiParentLanguage]
        """

        self._languages = languages

    @property
    def last_surname(self):
        """Gets the last_surname of this EdFiParent.  # noqa: E501

        The name borne in common by members of a family.  # noqa: E501

        :return: The last_surname of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._last_surname

    @last_surname.setter
    def last_surname(self, last_surname):
        """Sets the last_surname of this EdFiParent.

        The name borne in common by members of a family.  # noqa: E501

        :param last_surname: The last_surname of this EdFiParent.  # noqa: E501
        :type: str
        """
        if last_surname is None:
            raise ValueError("Invalid value for `last_surname`, must not be `None`")  # noqa: E501
        if last_surname is not None and len(last_surname) > 75:
            raise ValueError("Invalid value for `last_surname`, length must be less than or equal to `75`")  # noqa: E501

        self._last_surname = last_surname

    @property
    def login_id(self):
        """Gets the login_id of this EdFiParent.  # noqa: E501

        The login ID for the user; used for security access control interface.  # noqa: E501

        :return: The login_id of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._login_id

    @login_id.setter
    def login_id(self, login_id):
        """Sets the login_id of this EdFiParent.

        The login ID for the user; used for security access control interface.  # noqa: E501

        :param login_id: The login_id of this EdFiParent.  # noqa: E501
        :type: str
        """
        if login_id is not None and len(login_id) > 60:
            raise ValueError("Invalid value for `login_id`, length must be less than or equal to `60`")  # noqa: E501

        self._login_id = login_id

    @property
    def maiden_name(self):
        """Gets the maiden_name of this EdFiParent.  # noqa: E501

        The person's maiden name.  # noqa: E501

        :return: The maiden_name of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._maiden_name

    @maiden_name.setter
    def maiden_name(self, maiden_name):
        """Sets the maiden_name of this EdFiParent.

        The person's maiden name.  # noqa: E501

        :param maiden_name: The maiden_name of this EdFiParent.  # noqa: E501
        :type: str
        """
        if maiden_name is not None and len(maiden_name) > 75:
            raise ValueError("Invalid value for `maiden_name`, length must be less than or equal to `75`")  # noqa: E501

        self._maiden_name = maiden_name

    @property
    def middle_name(self):
        """Gets the middle_name of this EdFiParent.  # noqa: E501

        A secondary name given to an individual at birth, baptism, or during another naming ceremony.  # noqa: E501

        :return: The middle_name of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this EdFiParent.

        A secondary name given to an individual at birth, baptism, or during another naming ceremony.  # noqa: E501

        :param middle_name: The middle_name of this EdFiParent.  # noqa: E501
        :type: str
        """
        if middle_name is not None and len(middle_name) > 75:
            raise ValueError("Invalid value for `middle_name`, length must be less than or equal to `75`")  # noqa: E501

        self._middle_name = middle_name

    @property
    def other_names(self):
        """Gets the other_names of this EdFiParent.  # noqa: E501

        An unordered collection of parentOtherNames. Other names (e.g., alias, nickname, previous legal name) associated with a person.  # noqa: E501

        :return: The other_names of this EdFiParent.  # noqa: E501
        :rtype: list[EdFiParentOtherName]
        """
        return self._other_names

    @other_names.setter
    def other_names(self, other_names):
        """Sets the other_names of this EdFiParent.

        An unordered collection of parentOtherNames. Other names (e.g., alias, nickname, previous legal name) associated with a person.  # noqa: E501

        :param other_names: The other_names of this EdFiParent.  # noqa: E501
        :type: list[EdFiParentOtherName]
        """

        self._other_names = other_names

    @property
    def personal_identification_documents(self):
        """Gets the personal_identification_documents of this EdFiParent.  # noqa: E501

        An unordered collection of parentPersonalIdentificationDocuments. The documents presented as evident to verify one's personal identity; for example: drivers license, passport, birth certificate, etc.  # noqa: E501

        :return: The personal_identification_documents of this EdFiParent.  # noqa: E501
        :rtype: list[EdFiParentPersonalIdentificationDocument]
        """
        return self._personal_identification_documents

    @personal_identification_documents.setter
    def personal_identification_documents(self, personal_identification_documents):
        """Sets the personal_identification_documents of this EdFiParent.

        An unordered collection of parentPersonalIdentificationDocuments. The documents presented as evident to verify one's personal identity; for example: drivers license, passport, birth certificate, etc.  # noqa: E501

        :param personal_identification_documents: The personal_identification_documents of this EdFiParent.  # noqa: E501
        :type: list[EdFiParentPersonalIdentificationDocument]
        """

        self._personal_identification_documents = personal_identification_documents

    @property
    def personal_title_prefix(self):
        """Gets the personal_title_prefix of this EdFiParent.  # noqa: E501

        A prefix used to denote the title, degree, position, or seniority of the person.  # noqa: E501

        :return: The personal_title_prefix of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._personal_title_prefix

    @personal_title_prefix.setter
    def personal_title_prefix(self, personal_title_prefix):
        """Sets the personal_title_prefix of this EdFiParent.

        A prefix used to denote the title, degree, position, or seniority of the person.  # noqa: E501

        :param personal_title_prefix: The personal_title_prefix of this EdFiParent.  # noqa: E501
        :type: str
        """
        if personal_title_prefix is not None and len(personal_title_prefix) > 30:
            raise ValueError("Invalid value for `personal_title_prefix`, length must be less than or equal to `30`")  # noqa: E501

        self._personal_title_prefix = personal_title_prefix

    @property
    def sex_descriptor(self):
        """Gets the sex_descriptor of this EdFiParent.  # noqa: E501

        A person's gender.  # noqa: E501

        :return: The sex_descriptor of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._sex_descriptor

    @sex_descriptor.setter
    def sex_descriptor(self, sex_descriptor):
        """Sets the sex_descriptor of this EdFiParent.

        A person's gender.  # noqa: E501

        :param sex_descriptor: The sex_descriptor of this EdFiParent.  # noqa: E501
        :type: str
        """
        if sex_descriptor is not None and len(sex_descriptor) > 306:
            raise ValueError("Invalid value for `sex_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._sex_descriptor = sex_descriptor

    @property
    def telephones(self):
        """Gets the telephones of this EdFiParent.  # noqa: E501

        An unordered collection of parentTelephones. The 10-digit telephone number, including the area code, for the person.  # noqa: E501

        :return: The telephones of this EdFiParent.  # noqa: E501
        :rtype: list[EdFiParentTelephone]
        """
        return self._telephones

    @telephones.setter
    def telephones(self, telephones):
        """Sets the telephones of this EdFiParent.

        An unordered collection of parentTelephones. The 10-digit telephone number, including the area code, for the person.  # noqa: E501

        :param telephones: The telephones of this EdFiParent.  # noqa: E501
        :type: list[EdFiParentTelephone]
        """

        self._telephones = telephones

    @property
    def etag(self):
        """Gets the etag of this EdFiParent.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiParent.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiParent.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiParent.  # noqa: E501
        :type: str
        """

        self._etag = etag

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EdFiParent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EdFiParent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
