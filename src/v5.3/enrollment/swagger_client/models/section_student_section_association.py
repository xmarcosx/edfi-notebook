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


class SectionStudentSectionAssociation(object):
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
        'enrollment_begin_date': 'date',
        'enrollment_end_date': 'date',
        'id': 'str',
        'student_unique_id': 'str'
    }

    attribute_map = {
        'enrollment_begin_date': 'enrollmentBeginDate',
        'enrollment_end_date': 'enrollmentEndDate',
        'id': 'id',
        'student_unique_id': 'studentUniqueId'
    }

    def __init__(self, enrollment_begin_date=None, enrollment_end_date=None, id=None, student_unique_id=None, _configuration=None):  # noqa: E501
        """SectionStudentSectionAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enrollment_begin_date = None
        self._enrollment_end_date = None
        self._id = None
        self._student_unique_id = None
        self.discriminator = None

        self.enrollment_begin_date = enrollment_begin_date
        if enrollment_end_date is not None:
            self.enrollment_end_date = enrollment_end_date
        self.id = id
        self.student_unique_id = student_unique_id

    @property
    def enrollment_begin_date(self):
        """Gets the enrollment_begin_date of this SectionStudentSectionAssociation.  # noqa: E501

        Month, day, and year of the Student's entry or assignment to the Section.  # noqa: E501

        :return: The enrollment_begin_date of this SectionStudentSectionAssociation.  # noqa: E501
        :rtype: date
        """
        return self._enrollment_begin_date

    @enrollment_begin_date.setter
    def enrollment_begin_date(self, enrollment_begin_date):
        """Sets the enrollment_begin_date of this SectionStudentSectionAssociation.

        Month, day, and year of the Student's entry or assignment to the Section.  # noqa: E501

        :param enrollment_begin_date: The enrollment_begin_date of this SectionStudentSectionAssociation.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and enrollment_begin_date is None:
            raise ValueError("Invalid value for `enrollment_begin_date`, must not be `None`")  # noqa: E501

        self._enrollment_begin_date = enrollment_begin_date

    @property
    def enrollment_end_date(self):
        """Gets the enrollment_end_date of this SectionStudentSectionAssociation.  # noqa: E501

        Month, day, and year of the withdrawal or exit of the Student from the Section.  # noqa: E501

        :return: The enrollment_end_date of this SectionStudentSectionAssociation.  # noqa: E501
        :rtype: date
        """
        return self._enrollment_end_date

    @enrollment_end_date.setter
    def enrollment_end_date(self, enrollment_end_date):
        """Sets the enrollment_end_date of this SectionStudentSectionAssociation.

        Month, day, and year of the withdrawal or exit of the Student from the Section.  # noqa: E501

        :param enrollment_end_date: The enrollment_end_date of this SectionStudentSectionAssociation.  # noqa: E501
        :type: date
        """

        self._enrollment_end_date = enrollment_end_date

    @property
    def id(self):
        """Gets the id of this SectionStudentSectionAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this SectionStudentSectionAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SectionStudentSectionAssociation.

          # noqa: E501

        :param id: The id of this SectionStudentSectionAssociation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def student_unique_id(self):
        """Gets the student_unique_id of this SectionStudentSectionAssociation.  # noqa: E501

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :return: The student_unique_id of this SectionStudentSectionAssociation.  # noqa: E501
        :rtype: str
        """
        return self._student_unique_id

    @student_unique_id.setter
    def student_unique_id(self, student_unique_id):
        """Sets the student_unique_id of this SectionStudentSectionAssociation.

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :param student_unique_id: The student_unique_id of this SectionStudentSectionAssociation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and student_unique_id is None:
            raise ValueError("Invalid value for `student_unique_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                student_unique_id is not None and len(student_unique_id) > 32):
            raise ValueError("Invalid value for `student_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._student_unique_id = student_unique_id

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
        if issubclass(SectionStudentSectionAssociation, dict):
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
        if not isinstance(other, SectionStudentSectionAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SectionStudentSectionAssociation):
            return True

        return self.to_dict() != other.to_dict()