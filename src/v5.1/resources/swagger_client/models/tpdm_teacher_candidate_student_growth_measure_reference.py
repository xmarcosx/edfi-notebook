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


class TpdmTeacherCandidateStudentGrowthMeasureReference(object):
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
        'fact_as_of_date': 'date',
        'school_year': 'int',
        'teacher_candidate_identifier': 'str',
        'teacher_candidate_student_growth_measure_identifier': 'str',
        'link': 'Link'
    }

    attribute_map = {
        'fact_as_of_date': 'factAsOfDate',
        'school_year': 'schoolYear',
        'teacher_candidate_identifier': 'teacherCandidateIdentifier',
        'teacher_candidate_student_growth_measure_identifier': 'teacherCandidateStudentGrowthMeasureIdentifier',
        'link': 'link'
    }

    def __init__(self, fact_as_of_date=None, school_year=None, teacher_candidate_identifier=None, teacher_candidate_student_growth_measure_identifier=None, link=None, _configuration=None):  # noqa: E501
        """TpdmTeacherCandidateStudentGrowthMeasureReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._fact_as_of_date = None
        self._school_year = None
        self._teacher_candidate_identifier = None
        self._teacher_candidate_student_growth_measure_identifier = None
        self._link = None
        self.discriminator = None

        self.fact_as_of_date = fact_as_of_date
        self.school_year = school_year
        self.teacher_candidate_identifier = teacher_candidate_identifier
        self.teacher_candidate_student_growth_measure_identifier = teacher_candidate_student_growth_measure_identifier
        if link is not None:
            self.link = link

    @property
    def fact_as_of_date(self):
        """Gets the fact_as_of_date of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501

        The date for which the data element is relevant  # noqa: E501

        :return: The fact_as_of_date of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501
        :rtype: date
        """
        return self._fact_as_of_date

    @fact_as_of_date.setter
    def fact_as_of_date(self, fact_as_of_date):
        """Sets the fact_as_of_date of this TpdmTeacherCandidateStudentGrowthMeasureReference.

        The date for which the data element is relevant  # noqa: E501

        :param fact_as_of_date: The fact_as_of_date of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and fact_as_of_date is None:
            raise ValueError("Invalid value for `fact_as_of_date`, must not be `None`")  # noqa: E501

        self._fact_as_of_date = fact_as_of_date

    @property
    def school_year(self):
        """Gets the school_year of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501

        The school year for which the data is associated  # noqa: E501

        :return: The school_year of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501
        :rtype: int
        """
        return self._school_year

    @school_year.setter
    def school_year(self, school_year):
        """Sets the school_year of this TpdmTeacherCandidateStudentGrowthMeasureReference.

        The school year for which the data is associated  # noqa: E501

        :param school_year: The school_year of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and school_year is None:
            raise ValueError("Invalid value for `school_year`, must not be `None`")  # noqa: E501

        self._school_year = school_year

    @property
    def teacher_candidate_identifier(self):
        """Gets the teacher_candidate_identifier of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501

        A unique alphanumeric code assigned to a teacher candidate.  # noqa: E501

        :return: The teacher_candidate_identifier of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501
        :rtype: str
        """
        return self._teacher_candidate_identifier

    @teacher_candidate_identifier.setter
    def teacher_candidate_identifier(self, teacher_candidate_identifier):
        """Sets the teacher_candidate_identifier of this TpdmTeacherCandidateStudentGrowthMeasureReference.

        A unique alphanumeric code assigned to a teacher candidate.  # noqa: E501

        :param teacher_candidate_identifier: The teacher_candidate_identifier of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and teacher_candidate_identifier is None:
            raise ValueError("Invalid value for `teacher_candidate_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                teacher_candidate_identifier is not None and len(teacher_candidate_identifier) > 32):
            raise ValueError("Invalid value for `teacher_candidate_identifier`, length must be less than or equal to `32`")  # noqa: E501

        self._teacher_candidate_identifier = teacher_candidate_identifier

    @property
    def teacher_candidate_student_growth_measure_identifier(self):
        """Gets the teacher_candidate_student_growth_measure_identifier of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501

        Assigned unique identifier for the student growth measure.  # noqa: E501

        :return: The teacher_candidate_student_growth_measure_identifier of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501
        :rtype: str
        """
        return self._teacher_candidate_student_growth_measure_identifier

    @teacher_candidate_student_growth_measure_identifier.setter
    def teacher_candidate_student_growth_measure_identifier(self, teacher_candidate_student_growth_measure_identifier):
        """Sets the teacher_candidate_student_growth_measure_identifier of this TpdmTeacherCandidateStudentGrowthMeasureReference.

        Assigned unique identifier for the student growth measure.  # noqa: E501

        :param teacher_candidate_student_growth_measure_identifier: The teacher_candidate_student_growth_measure_identifier of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and teacher_candidate_student_growth_measure_identifier is None:
            raise ValueError("Invalid value for `teacher_candidate_student_growth_measure_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                teacher_candidate_student_growth_measure_identifier is not None and len(teacher_candidate_student_growth_measure_identifier) > 64):
            raise ValueError("Invalid value for `teacher_candidate_student_growth_measure_identifier`, length must be less than or equal to `64`")  # noqa: E501

        self._teacher_candidate_student_growth_measure_identifier = teacher_candidate_student_growth_measure_identifier

    @property
    def link(self):
        """Gets the link of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501


        :return: The link of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TpdmTeacherCandidateStudentGrowthMeasureReference.


        :param link: The link of this TpdmTeacherCandidateStudentGrowthMeasureReference.  # noqa: E501
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
        if issubclass(TpdmTeacherCandidateStudentGrowthMeasureReference, dict):
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
        if not isinstance(other, TpdmTeacherCandidateStudentGrowthMeasureReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmTeacherCandidateStudentGrowthMeasureReference):
            return True

        return self.to_dict() != other.to_dict()