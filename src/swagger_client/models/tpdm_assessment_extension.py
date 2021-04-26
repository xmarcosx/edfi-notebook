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


class TpdmAssessmentExtension(object):
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
        'program_gateway_descriptor': 'str'
    }

    attribute_map = {
        'program_gateway_descriptor': 'programGatewayDescriptor'
    }

    def __init__(self, program_gateway_descriptor=None):  # noqa: E501
        """TpdmAssessmentExtension - a model defined in Swagger"""  # noqa: E501

        self._program_gateway_descriptor = None
        self.discriminator = None

        if program_gateway_descriptor is not None:
            self.program_gateway_descriptor = program_gateway_descriptor

    @property
    def program_gateway_descriptor(self):
        """Gets the program_gateway_descriptor of this TpdmAssessmentExtension.  # noqa: E501

        Identifies the program gateway an assessment may be associated with for continuation in the program.  # noqa: E501

        :return: The program_gateway_descriptor of this TpdmAssessmentExtension.  # noqa: E501
        :rtype: str
        """
        return self._program_gateway_descriptor

    @program_gateway_descriptor.setter
    def program_gateway_descriptor(self, program_gateway_descriptor):
        """Sets the program_gateway_descriptor of this TpdmAssessmentExtension.

        Identifies the program gateway an assessment may be associated with for continuation in the program.  # noqa: E501

        :param program_gateway_descriptor: The program_gateway_descriptor of this TpdmAssessmentExtension.  # noqa: E501
        :type: str
        """
        if program_gateway_descriptor is not None and len(program_gateway_descriptor) > 306:
            raise ValueError("Invalid value for `program_gateway_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._program_gateway_descriptor = program_gateway_descriptor

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
        if issubclass(TpdmAssessmentExtension, dict):
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
        if not isinstance(other, TpdmAssessmentExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
