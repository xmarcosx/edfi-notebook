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


class TpdmTeacherCandidateAcademicRecordReference(object):
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
        'education_organization_id': 'int',
        'school_year': 'int',
        'teacher_candidate_identifier': 'str',
        'term_descriptor': 'str',
        'link': 'Link'
    }

    attribute_map = {
        'education_organization_id': 'educationOrganizationId',
        'school_year': 'schoolYear',
        'teacher_candidate_identifier': 'teacherCandidateIdentifier',
        'term_descriptor': 'termDescriptor',
        'link': 'link'
    }

    def __init__(self, education_organization_id=None, school_year=None, teacher_candidate_identifier=None, term_descriptor=None, link=None, _configuration=None):  # noqa: E501
        """TpdmTeacherCandidateAcademicRecordReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._education_organization_id = None
        self._school_year = None
        self._teacher_candidate_identifier = None
        self._term_descriptor = None
        self._link = None
        self.discriminator = None

        self.education_organization_id = education_organization_id
        self.school_year = school_year
        self.teacher_candidate_identifier = teacher_candidate_identifier
        self.term_descriptor = term_descriptor
        if link is not None:
            self.link = link

    @property
    def education_organization_id(self):
        """Gets the education_organization_id of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The education_organization_id of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501
        :rtype: int
        """
        return self._education_organization_id

    @education_organization_id.setter
    def education_organization_id(self, education_organization_id):
        """Sets the education_organization_id of this TpdmTeacherCandidateAcademicRecordReference.

        The identifier assigned to an education organization.  # noqa: E501

        :param education_organization_id: The education_organization_id of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and education_organization_id is None:
            raise ValueError("Invalid value for `education_organization_id`, must not be `None`")  # noqa: E501

        self._education_organization_id = education_organization_id

    @property
    def school_year(self):
        """Gets the school_year of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501

        The identifier for the school year.  # noqa: E501

        :return: The school_year of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501
        :rtype: int
        """
        return self._school_year

    @school_year.setter
    def school_year(self, school_year):
        """Sets the school_year of this TpdmTeacherCandidateAcademicRecordReference.

        The identifier for the school year.  # noqa: E501

        :param school_year: The school_year of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and school_year is None:
            raise ValueError("Invalid value for `school_year`, must not be `None`")  # noqa: E501

        self._school_year = school_year

    @property
    def teacher_candidate_identifier(self):
        """Gets the teacher_candidate_identifier of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501

        A unique alphanumeric code assigned to a teacher candidate.  # noqa: E501

        :return: The teacher_candidate_identifier of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501
        :rtype: str
        """
        return self._teacher_candidate_identifier

    @teacher_candidate_identifier.setter
    def teacher_candidate_identifier(self, teacher_candidate_identifier):
        """Sets the teacher_candidate_identifier of this TpdmTeacherCandidateAcademicRecordReference.

        A unique alphanumeric code assigned to a teacher candidate.  # noqa: E501

        :param teacher_candidate_identifier: The teacher_candidate_identifier of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and teacher_candidate_identifier is None:
            raise ValueError("Invalid value for `teacher_candidate_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                teacher_candidate_identifier is not None and len(teacher_candidate_identifier) > 32):
            raise ValueError("Invalid value for `teacher_candidate_identifier`, length must be less than or equal to `32`")  # noqa: E501

        self._teacher_candidate_identifier = teacher_candidate_identifier

    @property
    def term_descriptor(self):
        """Gets the term_descriptor of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501

        The term for the session during the school year.  # noqa: E501

        :return: The term_descriptor of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501
        :rtype: str
        """
        return self._term_descriptor

    @term_descriptor.setter
    def term_descriptor(self, term_descriptor):
        """Sets the term_descriptor of this TpdmTeacherCandidateAcademicRecordReference.

        The term for the session during the school year.  # noqa: E501

        :param term_descriptor: The term_descriptor of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and term_descriptor is None:
            raise ValueError("Invalid value for `term_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                term_descriptor is not None and len(term_descriptor) > 306):
            raise ValueError("Invalid value for `term_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._term_descriptor = term_descriptor

    @property
    def link(self):
        """Gets the link of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501


        :return: The link of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TpdmTeacherCandidateAcademicRecordReference.


        :param link: The link of this TpdmTeacherCandidateAcademicRecordReference.  # noqa: E501
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
        if issubclass(TpdmTeacherCandidateAcademicRecordReference, dict):
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
        if not isinstance(other, TpdmTeacherCandidateAcademicRecordReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmTeacherCandidateAcademicRecordReference):
            return True

        return self.to_dict() != other.to_dict()
