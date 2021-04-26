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


class EdFiStaffPersonalIdentificationDocument(object):
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
        'identification_document_use_descriptor': 'str',
        'personal_information_verification_descriptor': 'str',
        'issuer_country_descriptor': 'str',
        'document_expiration_date': 'date',
        'document_title': 'str',
        'issuer_document_identification_code': 'str',
        'issuer_name': 'str'
    }

    attribute_map = {
        'identification_document_use_descriptor': 'identificationDocumentUseDescriptor',
        'personal_information_verification_descriptor': 'personalInformationVerificationDescriptor',
        'issuer_country_descriptor': 'issuerCountryDescriptor',
        'document_expiration_date': 'documentExpirationDate',
        'document_title': 'documentTitle',
        'issuer_document_identification_code': 'issuerDocumentIdentificationCode',
        'issuer_name': 'issuerName'
    }

    def __init__(self, identification_document_use_descriptor=None, personal_information_verification_descriptor=None, issuer_country_descriptor=None, document_expiration_date=None, document_title=None, issuer_document_identification_code=None, issuer_name=None):  # noqa: E501
        """EdFiStaffPersonalIdentificationDocument - a model defined in Swagger"""  # noqa: E501

        self._identification_document_use_descriptor = None
        self._personal_information_verification_descriptor = None
        self._issuer_country_descriptor = None
        self._document_expiration_date = None
        self._document_title = None
        self._issuer_document_identification_code = None
        self._issuer_name = None
        self.discriminator = None

        self.identification_document_use_descriptor = identification_document_use_descriptor
        self.personal_information_verification_descriptor = personal_information_verification_descriptor
        if issuer_country_descriptor is not None:
            self.issuer_country_descriptor = issuer_country_descriptor
        if document_expiration_date is not None:
            self.document_expiration_date = document_expiration_date
        if document_title is not None:
            self.document_title = document_title
        if issuer_document_identification_code is not None:
            self.issuer_document_identification_code = issuer_document_identification_code
        if issuer_name is not None:
            self.issuer_name = issuer_name

    @property
    def identification_document_use_descriptor(self):
        """Gets the identification_document_use_descriptor of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501

        The primary function of the document used for establishing identity.  # noqa: E501

        :return: The identification_document_use_descriptor of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :rtype: str
        """
        return self._identification_document_use_descriptor

    @identification_document_use_descriptor.setter
    def identification_document_use_descriptor(self, identification_document_use_descriptor):
        """Sets the identification_document_use_descriptor of this EdFiStaffPersonalIdentificationDocument.

        The primary function of the document used for establishing identity.  # noqa: E501

        :param identification_document_use_descriptor: The identification_document_use_descriptor of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :type: str
        """
        if identification_document_use_descriptor is None:
            raise ValueError("Invalid value for `identification_document_use_descriptor`, must not be `None`")  # noqa: E501
        if identification_document_use_descriptor is not None and len(identification_document_use_descriptor) > 306:
            raise ValueError("Invalid value for `identification_document_use_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._identification_document_use_descriptor = identification_document_use_descriptor

    @property
    def personal_information_verification_descriptor(self):
        """Gets the personal_information_verification_descriptor of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501

        The category of the document relative to its purpose.  # noqa: E501

        :return: The personal_information_verification_descriptor of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :rtype: str
        """
        return self._personal_information_verification_descriptor

    @personal_information_verification_descriptor.setter
    def personal_information_verification_descriptor(self, personal_information_verification_descriptor):
        """Sets the personal_information_verification_descriptor of this EdFiStaffPersonalIdentificationDocument.

        The category of the document relative to its purpose.  # noqa: E501

        :param personal_information_verification_descriptor: The personal_information_verification_descriptor of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :type: str
        """
        if personal_information_verification_descriptor is None:
            raise ValueError("Invalid value for `personal_information_verification_descriptor`, must not be `None`")  # noqa: E501
        if personal_information_verification_descriptor is not None and len(personal_information_verification_descriptor) > 306:
            raise ValueError("Invalid value for `personal_information_verification_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._personal_information_verification_descriptor = personal_information_verification_descriptor

    @property
    def issuer_country_descriptor(self):
        """Gets the issuer_country_descriptor of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501

        Country of origin of the document. It is strongly recommended that entries use only ISO 3166 2-letter country codes.  # noqa: E501

        :return: The issuer_country_descriptor of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :rtype: str
        """
        return self._issuer_country_descriptor

    @issuer_country_descriptor.setter
    def issuer_country_descriptor(self, issuer_country_descriptor):
        """Sets the issuer_country_descriptor of this EdFiStaffPersonalIdentificationDocument.

        Country of origin of the document. It is strongly recommended that entries use only ISO 3166 2-letter country codes.  # noqa: E501

        :param issuer_country_descriptor: The issuer_country_descriptor of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :type: str
        """
        if issuer_country_descriptor is not None and len(issuer_country_descriptor) > 306:
            raise ValueError("Invalid value for `issuer_country_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._issuer_country_descriptor = issuer_country_descriptor

    @property
    def document_expiration_date(self):
        """Gets the document_expiration_date of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501

        The day when the document  expires, if null then never expires.  # noqa: E501

        :return: The document_expiration_date of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :rtype: date
        """
        return self._document_expiration_date

    @document_expiration_date.setter
    def document_expiration_date(self, document_expiration_date):
        """Sets the document_expiration_date of this EdFiStaffPersonalIdentificationDocument.

        The day when the document  expires, if null then never expires.  # noqa: E501

        :param document_expiration_date: The document_expiration_date of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :type: date
        """

        self._document_expiration_date = document_expiration_date

    @property
    def document_title(self):
        """Gets the document_title of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501

        The title of the document given by the issuer.  # noqa: E501

        :return: The document_title of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_title

    @document_title.setter
    def document_title(self, document_title):
        """Sets the document_title of this EdFiStaffPersonalIdentificationDocument.

        The title of the document given by the issuer.  # noqa: E501

        :param document_title: The document_title of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :type: str
        """
        if document_title is not None and len(document_title) > 60:
            raise ValueError("Invalid value for `document_title`, length must be less than or equal to `60`")  # noqa: E501

        self._document_title = document_title

    @property
    def issuer_document_identification_code(self):
        """Gets the issuer_document_identification_code of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501

        The unique identifier on the issuer's identification system.  # noqa: E501

        :return: The issuer_document_identification_code of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :rtype: str
        """
        return self._issuer_document_identification_code

    @issuer_document_identification_code.setter
    def issuer_document_identification_code(self, issuer_document_identification_code):
        """Sets the issuer_document_identification_code of this EdFiStaffPersonalIdentificationDocument.

        The unique identifier on the issuer's identification system.  # noqa: E501

        :param issuer_document_identification_code: The issuer_document_identification_code of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :type: str
        """
        if issuer_document_identification_code is not None and len(issuer_document_identification_code) > 60:
            raise ValueError("Invalid value for `issuer_document_identification_code`, length must be less than or equal to `60`")  # noqa: E501

        self._issuer_document_identification_code = issuer_document_identification_code

    @property
    def issuer_name(self):
        """Gets the issuer_name of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501

        Name of the entity or institution that issued the document.  # noqa: E501

        :return: The issuer_name of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """Sets the issuer_name of this EdFiStaffPersonalIdentificationDocument.

        Name of the entity or institution that issued the document.  # noqa: E501

        :param issuer_name: The issuer_name of this EdFiStaffPersonalIdentificationDocument.  # noqa: E501
        :type: str
        """
        if issuer_name is not None and len(issuer_name) > 150:
            raise ValueError("Invalid value for `issuer_name`, length must be less than or equal to `150`")  # noqa: E501

        self._issuer_name = issuer_name

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
        if issubclass(EdFiStaffPersonalIdentificationDocument, dict):
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
        if not isinstance(other, EdFiStaffPersonalIdentificationDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
