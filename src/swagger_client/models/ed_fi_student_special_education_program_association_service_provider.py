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


class EdFiStudentSpecialEducationProgramAssociationServiceProvider(object):
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
        'primary_provider': 'bool',
        'staff_reference': 'EdFiStaffReference'
    }

    attribute_map = {
        'primary_provider': 'primaryProvider',
        'staff_reference': 'staffReference'
    }

    def __init__(self, primary_provider=None, staff_reference=None):  # noqa: E501
        """EdFiStudentSpecialEducationProgramAssociationServiceProvider - a model defined in Swagger"""  # noqa: E501

        self._primary_provider = None
        self._staff_reference = None
        self.discriminator = None

        if primary_provider is not None:
            self.primary_provider = primary_provider
        self.staff_reference = staff_reference

    @property
    def primary_provider(self):
        """Gets the primary_provider of this EdFiStudentSpecialEducationProgramAssociationServiceProvider.  # noqa: E501

        Primary ServiceProvider.  # noqa: E501

        :return: The primary_provider of this EdFiStudentSpecialEducationProgramAssociationServiceProvider.  # noqa: E501
        :rtype: bool
        """
        return self._primary_provider

    @primary_provider.setter
    def primary_provider(self, primary_provider):
        """Sets the primary_provider of this EdFiStudentSpecialEducationProgramAssociationServiceProvider.

        Primary ServiceProvider.  # noqa: E501

        :param primary_provider: The primary_provider of this EdFiStudentSpecialEducationProgramAssociationServiceProvider.  # noqa: E501
        :type: bool
        """

        self._primary_provider = primary_provider

    @property
    def staff_reference(self):
        """Gets the staff_reference of this EdFiStudentSpecialEducationProgramAssociationServiceProvider.  # noqa: E501


        :return: The staff_reference of this EdFiStudentSpecialEducationProgramAssociationServiceProvider.  # noqa: E501
        :rtype: EdFiStaffReference
        """
        return self._staff_reference

    @staff_reference.setter
    def staff_reference(self, staff_reference):
        """Sets the staff_reference of this EdFiStudentSpecialEducationProgramAssociationServiceProvider.


        :param staff_reference: The staff_reference of this EdFiStudentSpecialEducationProgramAssociationServiceProvider.  # noqa: E501
        :type: EdFiStaffReference
        """
        if staff_reference is None:
            raise ValueError("Invalid value for `staff_reference`, must not be `None`")  # noqa: E501

        self._staff_reference = staff_reference

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
        if issubclass(EdFiStudentSpecialEducationProgramAssociationServiceProvider, dict):
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
        if not isinstance(other, EdFiStudentSpecialEducationProgramAssociationServiceProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
