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


class EdFiSessionGradingPeriod(object):
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
        'grading_period_reference': 'EdFiGradingPeriodReference'
    }

    attribute_map = {
        'grading_period_reference': 'gradingPeriodReference'
    }

    def __init__(self, grading_period_reference=None, _configuration=None):  # noqa: E501
        """EdFiSessionGradingPeriod - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._grading_period_reference = None
        self.discriminator = None

        self.grading_period_reference = grading_period_reference

    @property
    def grading_period_reference(self):
        """Gets the grading_period_reference of this EdFiSessionGradingPeriod.  # noqa: E501


        :return: The grading_period_reference of this EdFiSessionGradingPeriod.  # noqa: E501
        :rtype: EdFiGradingPeriodReference
        """
        return self._grading_period_reference

    @grading_period_reference.setter
    def grading_period_reference(self, grading_period_reference):
        """Sets the grading_period_reference of this EdFiSessionGradingPeriod.


        :param grading_period_reference: The grading_period_reference of this EdFiSessionGradingPeriod.  # noqa: E501
        :type: EdFiGradingPeriodReference
        """
        if self._configuration.client_side_validation and grading_period_reference is None:
            raise ValueError("Invalid value for `grading_period_reference`, must not be `None`")  # noqa: E501

        self._grading_period_reference = grading_period_reference

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
        if issubclass(EdFiSessionGradingPeriod, dict):
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
        if not isinstance(other, EdFiSessionGradingPeriod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiSessionGradingPeriod):
            return True

        return self.to_dict() != other.to_dict()
