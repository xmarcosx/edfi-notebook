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


class EdFiClassPeriodMeetingTime(object):
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
        'end_time': 'str',
        'start_time': 'str'
    }

    attribute_map = {
        'end_time': 'endTime',
        'start_time': 'startTime'
    }

    def __init__(self, end_time=None, start_time=None):  # noqa: E501
        """EdFiClassPeriodMeetingTime - a model defined in Swagger"""  # noqa: E501

        self._end_time = None
        self._start_time = None
        self.discriminator = None

        self.end_time = end_time
        self.start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this EdFiClassPeriodMeetingTime.  # noqa: E501

        An indication of the time of day the meeting time ends.  # noqa: E501

        :return: The end_time of this EdFiClassPeriodMeetingTime.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this EdFiClassPeriodMeetingTime.

        An indication of the time of day the meeting time ends.  # noqa: E501

        :param end_time: The end_time of this EdFiClassPeriodMeetingTime.  # noqa: E501
        :type: str
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this EdFiClassPeriodMeetingTime.  # noqa: E501

        An indication of the time of day the meeting time begins.  # noqa: E501

        :return: The start_time of this EdFiClassPeriodMeetingTime.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this EdFiClassPeriodMeetingTime.

        An indication of the time of day the meeting time begins.  # noqa: E501

        :param start_time: The start_time of this EdFiClassPeriodMeetingTime.  # noqa: E501
        :type: str
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

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
        if issubclass(EdFiClassPeriodMeetingTime, dict):
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
        if not isinstance(other, EdFiClassPeriodMeetingTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
