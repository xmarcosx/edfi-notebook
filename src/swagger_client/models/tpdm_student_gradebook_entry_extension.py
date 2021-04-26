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


class TpdmStudentGradebookEntryExtension(object):
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
        'assignment_passed': 'bool',
        'date_completed': 'date'
    }

    attribute_map = {
        'assignment_passed': 'assignmentPassed',
        'date_completed': 'dateCompleted'
    }

    def __init__(self, assignment_passed=None, date_completed=None):  # noqa: E501
        """TpdmStudentGradebookEntryExtension - a model defined in Swagger"""  # noqa: E501

        self._assignment_passed = None
        self._date_completed = None
        self.discriminator = None

        if assignment_passed is not None:
            self.assignment_passed = assignment_passed
        if date_completed is not None:
            self.date_completed = date_completed

    @property
    def assignment_passed(self):
        """Gets the assignment_passed of this TpdmStudentGradebookEntryExtension.  # noqa: E501

        Indication of whether the assignment was passed or not.  # noqa: E501

        :return: The assignment_passed of this TpdmStudentGradebookEntryExtension.  # noqa: E501
        :rtype: bool
        """
        return self._assignment_passed

    @assignment_passed.setter
    def assignment_passed(self, assignment_passed):
        """Sets the assignment_passed of this TpdmStudentGradebookEntryExtension.

        Indication of whether the assignment was passed or not.  # noqa: E501

        :param assignment_passed: The assignment_passed of this TpdmStudentGradebookEntryExtension.  # noqa: E501
        :type: bool
        """

        self._assignment_passed = assignment_passed

    @property
    def date_completed(self):
        """Gets the date_completed of this TpdmStudentGradebookEntryExtension.  # noqa: E501

        The date that the assignment was completed.  # noqa: E501

        :return: The date_completed of this TpdmStudentGradebookEntryExtension.  # noqa: E501
        :rtype: date
        """
        return self._date_completed

    @date_completed.setter
    def date_completed(self, date_completed):
        """Sets the date_completed of this TpdmStudentGradebookEntryExtension.

        The date that the assignment was completed.  # noqa: E501

        :param date_completed: The date_completed of this TpdmStudentGradebookEntryExtension.  # noqa: E501
        :type: date
        """

        self._date_completed = date_completed

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
        if issubclass(TpdmStudentGradebookEntryExtension, dict):
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
        if not isinstance(other, TpdmStudentGradebookEntryExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
