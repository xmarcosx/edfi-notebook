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


class EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod(object):
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
        'begin_date': 'date',
        'end_date': 'date'
    }

    attribute_map = {
        'begin_date': 'beginDate',
        'end_date': 'endDate'
    }

    def __init__(self, begin_date=None, end_date=None, _configuration=None):  # noqa: E501
        """EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._begin_date = None
        self._end_date = None
        self.discriminator = None

        self.begin_date = begin_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod.  # noqa: E501

        The month, day, and year for the start of the period.  # noqa: E501

        :return: The begin_date of this EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod.

        The month, day, and year for the start of the period.  # noqa: E501

        :param begin_date: The begin_date of this EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def end_date(self):
        """Gets the end_date of this EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod.  # noqa: E501

        The month, day, and year for the end of the period.  # noqa: E501

        :return: The end_date of this EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod.

        The month, day, and year for the end of the period.  # noqa: E501

        :param end_date: The end_date of this EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

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
        if issubclass(EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod, dict):
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
        if not isinstance(other, EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentEducationOrganizationAssociationStudentCharacteristicPeriod):
            return True

        return self.to_dict() != other.to_dict()
