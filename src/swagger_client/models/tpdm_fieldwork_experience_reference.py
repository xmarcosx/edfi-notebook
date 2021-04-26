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


class TpdmFieldworkExperienceReference(object):
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
        'fieldwork_identifier': 'str',
        'student_unique_id': 'str',
        'link': 'Link'
    }

    attribute_map = {
        'begin_date': 'beginDate',
        'fieldwork_identifier': 'fieldworkIdentifier',
        'student_unique_id': 'studentUniqueId',
        'link': 'link'
    }

    def __init__(self, begin_date=None, fieldwork_identifier=None, student_unique_id=None, link=None):  # noqa: E501
        """TpdmFieldworkExperienceReference - a model defined in Swagger"""  # noqa: E501

        self._begin_date = None
        self._fieldwork_identifier = None
        self._student_unique_id = None
        self._link = None
        self.discriminator = None

        self.begin_date = begin_date
        self.fieldwork_identifier = fieldwork_identifier
        self.student_unique_id = student_unique_id
        if link is not None:
            self.link = link

    @property
    def begin_date(self):
        """Gets the begin_date of this TpdmFieldworkExperienceReference.  # noqa: E501

        The month, day, and year on which the staff first starts fieldwork.  # noqa: E501

        :return: The begin_date of this TpdmFieldworkExperienceReference.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this TpdmFieldworkExperienceReference.

        The month, day, and year on which the staff first starts fieldwork.  # noqa: E501

        :param begin_date: The begin_date of this TpdmFieldworkExperienceReference.  # noqa: E501
        :type: date
        """
        if begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def fieldwork_identifier(self):
        """Gets the fieldwork_identifier of this TpdmFieldworkExperienceReference.  # noqa: E501

        The unique identifier for the fieldwork experience  # noqa: E501

        :return: The fieldwork_identifier of this TpdmFieldworkExperienceReference.  # noqa: E501
        :rtype: str
        """
        return self._fieldwork_identifier

    @fieldwork_identifier.setter
    def fieldwork_identifier(self, fieldwork_identifier):
        """Sets the fieldwork_identifier of this TpdmFieldworkExperienceReference.

        The unique identifier for the fieldwork experience  # noqa: E501

        :param fieldwork_identifier: The fieldwork_identifier of this TpdmFieldworkExperienceReference.  # noqa: E501
        :type: str
        """
        if fieldwork_identifier is None:
            raise ValueError("Invalid value for `fieldwork_identifier`, must not be `None`")  # noqa: E501
        if fieldwork_identifier is not None and len(fieldwork_identifier) > 64:
            raise ValueError("Invalid value for `fieldwork_identifier`, length must be less than or equal to `64`")  # noqa: E501

        self._fieldwork_identifier = fieldwork_identifier

    @property
    def student_unique_id(self):
        """Gets the student_unique_id of this TpdmFieldworkExperienceReference.  # noqa: E501

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :return: The student_unique_id of this TpdmFieldworkExperienceReference.  # noqa: E501
        :rtype: str
        """
        return self._student_unique_id

    @student_unique_id.setter
    def student_unique_id(self, student_unique_id):
        """Sets the student_unique_id of this TpdmFieldworkExperienceReference.

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :param student_unique_id: The student_unique_id of this TpdmFieldworkExperienceReference.  # noqa: E501
        :type: str
        """
        if student_unique_id is None:
            raise ValueError("Invalid value for `student_unique_id`, must not be `None`")  # noqa: E501
        if student_unique_id is not None and len(student_unique_id) > 32:
            raise ValueError("Invalid value for `student_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._student_unique_id = student_unique_id

    @property
    def link(self):
        """Gets the link of this TpdmFieldworkExperienceReference.  # noqa: E501


        :return: The link of this TpdmFieldworkExperienceReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TpdmFieldworkExperienceReference.


        :param link: The link of this TpdmFieldworkExperienceReference.  # noqa: E501
        :type: Link
        """

        self._link = link

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
        if issubclass(TpdmFieldworkExperienceReference, dict):
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
        if not isinstance(other, TpdmFieldworkExperienceReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
