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


class StaffEducationOrganizationAssignmentAssociationExtensions(object):
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
        'tpdm': 'TpdmStaffEducationOrganizationAssignmentAssociationExtension'
    }

    attribute_map = {
        'tpdm': 'TPDM'
    }

    def __init__(self, tpdm=None, _configuration=None):  # noqa: E501
        """StaffEducationOrganizationAssignmentAssociationExtensions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._tpdm = None
        self.discriminator = None

        if tpdm is not None:
            self.tpdm = tpdm

    @property
    def tpdm(self):
        """Gets the tpdm of this StaffEducationOrganizationAssignmentAssociationExtensions.  # noqa: E501


        :return: The tpdm of this StaffEducationOrganizationAssignmentAssociationExtensions.  # noqa: E501
        :rtype: TpdmStaffEducationOrganizationAssignmentAssociationExtension
        """
        return self._tpdm

    @tpdm.setter
    def tpdm(self, tpdm):
        """Sets the tpdm of this StaffEducationOrganizationAssignmentAssociationExtensions.


        :param tpdm: The tpdm of this StaffEducationOrganizationAssignmentAssociationExtensions.  # noqa: E501
        :type: TpdmStaffEducationOrganizationAssignmentAssociationExtension
        """

        self._tpdm = tpdm

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
        if issubclass(StaffEducationOrganizationAssignmentAssociationExtensions, dict):
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
        if not isinstance(other, StaffEducationOrganizationAssignmentAssociationExtensions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StaffEducationOrganizationAssignmentAssociationExtensions):
            return True

        return self.to_dict() != other.to_dict()
