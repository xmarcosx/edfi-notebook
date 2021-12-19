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


class TpdmFieldworkExperienceSectionAssociation(object):
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
        'fieldwork_experience_reference': 'TpdmFieldworkExperienceReference',
        'section_reference': 'EdFiSectionReference',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'fieldwork_experience_reference': 'fieldworkExperienceReference',
        'section_reference': 'sectionReference',
        'etag': '_etag'
    }

    def __init__(self, id=None, fieldwork_experience_reference=None, section_reference=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmFieldworkExperienceSectionAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._fieldwork_experience_reference = None
        self._section_reference = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.fieldwork_experience_reference = fieldwork_experience_reference
        self.section_reference = section_reference
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmFieldworkExperienceSectionAssociation.

          # noqa: E501

        :param id: The id of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def fieldwork_experience_reference(self):
        """Gets the fieldwork_experience_reference of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501


        :return: The fieldwork_experience_reference of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501
        :rtype: TpdmFieldworkExperienceReference
        """
        return self._fieldwork_experience_reference

    @fieldwork_experience_reference.setter
    def fieldwork_experience_reference(self, fieldwork_experience_reference):
        """Sets the fieldwork_experience_reference of this TpdmFieldworkExperienceSectionAssociation.


        :param fieldwork_experience_reference: The fieldwork_experience_reference of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501
        :type: TpdmFieldworkExperienceReference
        """
        if self._configuration.client_side_validation and fieldwork_experience_reference is None:
            raise ValueError("Invalid value for `fieldwork_experience_reference`, must not be `None`")  # noqa: E501

        self._fieldwork_experience_reference = fieldwork_experience_reference

    @property
    def section_reference(self):
        """Gets the section_reference of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501


        :return: The section_reference of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501
        :rtype: EdFiSectionReference
        """
        return self._section_reference

    @section_reference.setter
    def section_reference(self, section_reference):
        """Sets the section_reference of this TpdmFieldworkExperienceSectionAssociation.


        :param section_reference: The section_reference of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501
        :type: EdFiSectionReference
        """
        if self._configuration.client_side_validation and section_reference is None:
            raise ValueError("Invalid value for `section_reference`, must not be `None`")  # noqa: E501

        self._section_reference = section_reference

    @property
    def etag(self):
        """Gets the etag of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmFieldworkExperienceSectionAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmFieldworkExperienceSectionAssociation.  # noqa: E501
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
        if issubclass(TpdmFieldworkExperienceSectionAssociation, dict):
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
        if not isinstance(other, TpdmFieldworkExperienceSectionAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmFieldworkExperienceSectionAssociation):
            return True

        return self.to_dict() != other.to_dict()
