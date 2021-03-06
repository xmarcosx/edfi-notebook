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

from swagger_client.configuration import Configuration


class EdFiStudentEducationOrganizationAssociationLanguage(object):
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
        'language_descriptor': 'str',
        'uses': 'list[EdFiStudentEducationOrganizationAssociationLanguageUse]'
    }

    attribute_map = {
        'language_descriptor': 'languageDescriptor',
        'uses': 'uses'
    }

    def __init__(self, language_descriptor=None, uses=None, _configuration=None):  # noqa: E501
        """EdFiStudentEducationOrganizationAssociationLanguage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._language_descriptor = None
        self._uses = None
        self.discriminator = None

        self.language_descriptor = language_descriptor
        if uses is not None:
            self.uses = uses

    @property
    def language_descriptor(self):
        """Gets the language_descriptor of this EdFiStudentEducationOrganizationAssociationLanguage.  # noqa: E501

        A specification of which written or spoken communication is being used.  # noqa: E501

        :return: The language_descriptor of this EdFiStudentEducationOrganizationAssociationLanguage.  # noqa: E501
        :rtype: str
        """
        return self._language_descriptor

    @language_descriptor.setter
    def language_descriptor(self, language_descriptor):
        """Sets the language_descriptor of this EdFiStudentEducationOrganizationAssociationLanguage.

        A specification of which written or spoken communication is being used.  # noqa: E501

        :param language_descriptor: The language_descriptor of this EdFiStudentEducationOrganizationAssociationLanguage.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and language_descriptor is None:
            raise ValueError("Invalid value for `language_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                language_descriptor is not None and len(language_descriptor) > 306):
            raise ValueError("Invalid value for `language_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._language_descriptor = language_descriptor

    @property
    def uses(self):
        """Gets the uses of this EdFiStudentEducationOrganizationAssociationLanguage.  # noqa: E501

        An unordered collection of studentEducationOrganizationAssociationLanguageUses. A description of how the language is used (e.g. Home Language, Native Language, Spoken Language).  # noqa: E501

        :return: The uses of this EdFiStudentEducationOrganizationAssociationLanguage.  # noqa: E501
        :rtype: list[EdFiStudentEducationOrganizationAssociationLanguageUse]
        """
        return self._uses

    @uses.setter
    def uses(self, uses):
        """Sets the uses of this EdFiStudentEducationOrganizationAssociationLanguage.

        An unordered collection of studentEducationOrganizationAssociationLanguageUses. A description of how the language is used (e.g. Home Language, Native Language, Spoken Language).  # noqa: E501

        :param uses: The uses of this EdFiStudentEducationOrganizationAssociationLanguage.  # noqa: E501
        :type: list[EdFiStudentEducationOrganizationAssociationLanguageUse]
        """

        self._uses = uses

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
        if issubclass(EdFiStudentEducationOrganizationAssociationLanguage, dict):
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
        if not isinstance(other, EdFiStudentEducationOrganizationAssociationLanguage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentEducationOrganizationAssociationLanguage):
            return True

        return self.to_dict() != other.to_dict()
