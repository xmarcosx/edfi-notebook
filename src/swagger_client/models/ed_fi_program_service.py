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


class EdFiProgramService(object):
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
        'service_descriptor': 'str'
    }

    attribute_map = {
        'service_descriptor': 'serviceDescriptor'
    }

    def __init__(self, service_descriptor=None):  # noqa: E501
        """EdFiProgramService - a model defined in Swagger"""  # noqa: E501

        self._service_descriptor = None
        self.discriminator = None

        self.service_descriptor = service_descriptor

    @property
    def service_descriptor(self):
        """Gets the service_descriptor of this EdFiProgramService.  # noqa: E501

        Defines the services this program provides to students.  # noqa: E501

        :return: The service_descriptor of this EdFiProgramService.  # noqa: E501
        :rtype: str
        """
        return self._service_descriptor

    @service_descriptor.setter
    def service_descriptor(self, service_descriptor):
        """Sets the service_descriptor of this EdFiProgramService.

        Defines the services this program provides to students.  # noqa: E501

        :param service_descriptor: The service_descriptor of this EdFiProgramService.  # noqa: E501
        :type: str
        """
        if service_descriptor is None:
            raise ValueError("Invalid value for `service_descriptor`, must not be `None`")  # noqa: E501
        if service_descriptor is not None and len(service_descriptor) > 306:
            raise ValueError("Invalid value for `service_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._service_descriptor = service_descriptor

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
        if issubclass(EdFiProgramService, dict):
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
        if not isinstance(other, EdFiProgramService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
