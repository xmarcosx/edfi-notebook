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


class TpdmProspectTouchpoint(object):
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
        'touchpoint_content': 'str',
        'touchpoint_date': 'date'
    }

    attribute_map = {
        'touchpoint_content': 'touchpointContent',
        'touchpoint_date': 'touchpointDate'
    }

    def __init__(self, touchpoint_content=None, touchpoint_date=None, _configuration=None):  # noqa: E501
        """TpdmProspectTouchpoint - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._touchpoint_content = None
        self._touchpoint_date = None
        self.discriminator = None

        self.touchpoint_content = touchpoint_content
        self.touchpoint_date = touchpoint_date

    @property
    def touchpoint_content(self):
        """Gets the touchpoint_content of this TpdmProspectTouchpoint.  # noqa: E501

        The content associated with or an artifact from the touchpoint.  # noqa: E501

        :return: The touchpoint_content of this TpdmProspectTouchpoint.  # noqa: E501
        :rtype: str
        """
        return self._touchpoint_content

    @touchpoint_content.setter
    def touchpoint_content(self, touchpoint_content):
        """Sets the touchpoint_content of this TpdmProspectTouchpoint.

        The content associated with or an artifact from the touchpoint.  # noqa: E501

        :param touchpoint_content: The touchpoint_content of this TpdmProspectTouchpoint.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and touchpoint_content is None:
            raise ValueError("Invalid value for `touchpoint_content`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                touchpoint_content is not None and len(touchpoint_content) > 255):
            raise ValueError("Invalid value for `touchpoint_content`, length must be less than or equal to `255`")  # noqa: E501

        self._touchpoint_content = touchpoint_content

    @property
    def touchpoint_date(self):
        """Gets the touchpoint_date of this TpdmProspectTouchpoint.  # noqa: E501

        The date of the touchpoint.  # noqa: E501

        :return: The touchpoint_date of this TpdmProspectTouchpoint.  # noqa: E501
        :rtype: date
        """
        return self._touchpoint_date

    @touchpoint_date.setter
    def touchpoint_date(self, touchpoint_date):
        """Sets the touchpoint_date of this TpdmProspectTouchpoint.

        The date of the touchpoint.  # noqa: E501

        :param touchpoint_date: The touchpoint_date of this TpdmProspectTouchpoint.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and touchpoint_date is None:
            raise ValueError("Invalid value for `touchpoint_date`, must not be `None`")  # noqa: E501

        self._touchpoint_date = touchpoint_date

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
        if issubclass(TpdmProspectTouchpoint, dict):
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
        if not isinstance(other, TpdmProspectTouchpoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmProspectTouchpoint):
            return True

        return self.to_dict() != other.to_dict()
