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


class TpdmTeacherCandidateCharacteristic(object):
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
        'student_characteristic_descriptor': 'str',
        'begin_date': 'date',
        'designated_by': 'str',
        'end_date': 'date'
    }

    attribute_map = {
        'student_characteristic_descriptor': 'studentCharacteristicDescriptor',
        'begin_date': 'beginDate',
        'designated_by': 'designatedBy',
        'end_date': 'endDate'
    }

    def __init__(self, student_characteristic_descriptor=None, begin_date=None, designated_by=None, end_date=None, _configuration=None):  # noqa: E501
        """TpdmTeacherCandidateCharacteristic - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._student_characteristic_descriptor = None
        self._begin_date = None
        self._designated_by = None
        self._end_date = None
        self.discriminator = None

        self.student_characteristic_descriptor = student_characteristic_descriptor
        if begin_date is not None:
            self.begin_date = begin_date
        if designated_by is not None:
            self.designated_by = designated_by
        if end_date is not None:
            self.end_date = end_date

    @property
    def student_characteristic_descriptor(self):
        """Gets the student_characteristic_descriptor of this TpdmTeacherCandidateCharacteristic.  # noqa: E501

        The characteristic designated for the Student.  # noqa: E501

        :return: The student_characteristic_descriptor of this TpdmTeacherCandidateCharacteristic.  # noqa: E501
        :rtype: str
        """
        return self._student_characteristic_descriptor

    @student_characteristic_descriptor.setter
    def student_characteristic_descriptor(self, student_characteristic_descriptor):
        """Sets the student_characteristic_descriptor of this TpdmTeacherCandidateCharacteristic.

        The characteristic designated for the Student.  # noqa: E501

        :param student_characteristic_descriptor: The student_characteristic_descriptor of this TpdmTeacherCandidateCharacteristic.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and student_characteristic_descriptor is None:
            raise ValueError("Invalid value for `student_characteristic_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                student_characteristic_descriptor is not None and len(student_characteristic_descriptor) > 306):
            raise ValueError("Invalid value for `student_characteristic_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._student_characteristic_descriptor = student_characteristic_descriptor

    @property
    def begin_date(self):
        """Gets the begin_date of this TpdmTeacherCandidateCharacteristic.  # noqa: E501

        The date the characteristic was designated.  # noqa: E501

        :return: The begin_date of this TpdmTeacherCandidateCharacteristic.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this TpdmTeacherCandidateCharacteristic.

        The date the characteristic was designated.  # noqa: E501

        :param begin_date: The begin_date of this TpdmTeacherCandidateCharacteristic.  # noqa: E501
        :type: date
        """

        self._begin_date = begin_date

    @property
    def designated_by(self):
        """Gets the designated_by of this TpdmTeacherCandidateCharacteristic.  # noqa: E501

        The person, organization, or department that designated the characteristic.  # noqa: E501

        :return: The designated_by of this TpdmTeacherCandidateCharacteristic.  # noqa: E501
        :rtype: str
        """
        return self._designated_by

    @designated_by.setter
    def designated_by(self, designated_by):
        """Sets the designated_by of this TpdmTeacherCandidateCharacteristic.

        The person, organization, or department that designated the characteristic.  # noqa: E501

        :param designated_by: The designated_by of this TpdmTeacherCandidateCharacteristic.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                designated_by is not None and len(designated_by) > 60):
            raise ValueError("Invalid value for `designated_by`, length must be less than or equal to `60`")  # noqa: E501

        self._designated_by = designated_by

    @property
    def end_date(self):
        """Gets the end_date of this TpdmTeacherCandidateCharacteristic.  # noqa: E501

        The date the characteristic was removed.  # noqa: E501

        :return: The end_date of this TpdmTeacherCandidateCharacteristic.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TpdmTeacherCandidateCharacteristic.

        The date the characteristic was removed.  # noqa: E501

        :param end_date: The end_date of this TpdmTeacherCandidateCharacteristic.  # noqa: E501
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
        if issubclass(TpdmTeacherCandidateCharacteristic, dict):
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
        if not isinstance(other, TpdmTeacherCandidateCharacteristic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmTeacherCandidateCharacteristic):
            return True

        return self.to_dict() != other.to_dict()