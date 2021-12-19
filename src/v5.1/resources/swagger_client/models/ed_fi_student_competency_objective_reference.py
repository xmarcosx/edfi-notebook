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


class EdFiStudentCompetencyObjectiveReference(object):
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
        'grading_period_descriptor': 'str',
        'grading_period_school_id': 'int',
        'grading_period_school_year': 'int',
        'grading_period_sequence': 'int',
        'objective': 'str',
        'objective_education_organization_id': 'int',
        'objective_grade_level_descriptor': 'str',
        'student_unique_id': 'str',
        'link': 'Link'
    }

    attribute_map = {
        'grading_period_descriptor': 'gradingPeriodDescriptor',
        'grading_period_school_id': 'gradingPeriodSchoolId',
        'grading_period_school_year': 'gradingPeriodSchoolYear',
        'grading_period_sequence': 'gradingPeriodSequence',
        'objective': 'objective',
        'objective_education_organization_id': 'objectiveEducationOrganizationId',
        'objective_grade_level_descriptor': 'objectiveGradeLevelDescriptor',
        'student_unique_id': 'studentUniqueId',
        'link': 'link'
    }

    def __init__(self, grading_period_descriptor=None, grading_period_school_id=None, grading_period_school_year=None, grading_period_sequence=None, objective=None, objective_education_organization_id=None, objective_grade_level_descriptor=None, student_unique_id=None, link=None, _configuration=None):  # noqa: E501
        """EdFiStudentCompetencyObjectiveReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._grading_period_descriptor = None
        self._grading_period_school_id = None
        self._grading_period_school_year = None
        self._grading_period_sequence = None
        self._objective = None
        self._objective_education_organization_id = None
        self._objective_grade_level_descriptor = None
        self._student_unique_id = None
        self._link = None
        self.discriminator = None

        self.grading_period_descriptor = grading_period_descriptor
        self.grading_period_school_id = grading_period_school_id
        self.grading_period_school_year = grading_period_school_year
        self.grading_period_sequence = grading_period_sequence
        self.objective = objective
        self.objective_education_organization_id = objective_education_organization_id
        self.objective_grade_level_descriptor = objective_grade_level_descriptor
        self.student_unique_id = student_unique_id
        if link is not None:
            self.link = link

    @property
    def grading_period_descriptor(self):
        """Gets the grading_period_descriptor of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501

        The name of the period for which grades are reported.  # noqa: E501

        :return: The grading_period_descriptor of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :rtype: str
        """
        return self._grading_period_descriptor

    @grading_period_descriptor.setter
    def grading_period_descriptor(self, grading_period_descriptor):
        """Sets the grading_period_descriptor of this EdFiStudentCompetencyObjectiveReference.

        The name of the period for which grades are reported.  # noqa: E501

        :param grading_period_descriptor: The grading_period_descriptor of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and grading_period_descriptor is None:
            raise ValueError("Invalid value for `grading_period_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                grading_period_descriptor is not None and len(grading_period_descriptor) > 306):
            raise ValueError("Invalid value for `grading_period_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._grading_period_descriptor = grading_period_descriptor

    @property
    def grading_period_school_id(self):
        """Gets the grading_period_school_id of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501

        The identifier assigned to a school.  # noqa: E501

        :return: The grading_period_school_id of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :rtype: int
        """
        return self._grading_period_school_id

    @grading_period_school_id.setter
    def grading_period_school_id(self, grading_period_school_id):
        """Sets the grading_period_school_id of this EdFiStudentCompetencyObjectiveReference.

        The identifier assigned to a school.  # noqa: E501

        :param grading_period_school_id: The grading_period_school_id of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and grading_period_school_id is None:
            raise ValueError("Invalid value for `grading_period_school_id`, must not be `None`")  # noqa: E501

        self._grading_period_school_id = grading_period_school_id

    @property
    def grading_period_school_year(self):
        """Gets the grading_period_school_year of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501

        The identifier for the grading period school year.  # noqa: E501

        :return: The grading_period_school_year of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :rtype: int
        """
        return self._grading_period_school_year

    @grading_period_school_year.setter
    def grading_period_school_year(self, grading_period_school_year):
        """Sets the grading_period_school_year of this EdFiStudentCompetencyObjectiveReference.

        The identifier for the grading period school year.  # noqa: E501

        :param grading_period_school_year: The grading_period_school_year of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and grading_period_school_year is None:
            raise ValueError("Invalid value for `grading_period_school_year`, must not be `None`")  # noqa: E501

        self._grading_period_school_year = grading_period_school_year

    @property
    def grading_period_sequence(self):
        """Gets the grading_period_sequence of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501

        The sequential order of this period relative to other periods.  # noqa: E501

        :return: The grading_period_sequence of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :rtype: int
        """
        return self._grading_period_sequence

    @grading_period_sequence.setter
    def grading_period_sequence(self, grading_period_sequence):
        """Sets the grading_period_sequence of this EdFiStudentCompetencyObjectiveReference.

        The sequential order of this period relative to other periods.  # noqa: E501

        :param grading_period_sequence: The grading_period_sequence of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and grading_period_sequence is None:
            raise ValueError("Invalid value for `grading_period_sequence`, must not be `None`")  # noqa: E501

        self._grading_period_sequence = grading_period_sequence

    @property
    def objective(self):
        """Gets the objective of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501

        The designated title of the CompetencyObjective.  # noqa: E501

        :return: The objective of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this EdFiStudentCompetencyObjectiveReference.

        The designated title of the CompetencyObjective.  # noqa: E501

        :param objective: The objective of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and objective is None:
            raise ValueError("Invalid value for `objective`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                objective is not None and len(objective) > 60):
            raise ValueError("Invalid value for `objective`, length must be less than or equal to `60`")  # noqa: E501

        self._objective = objective

    @property
    def objective_education_organization_id(self):
        """Gets the objective_education_organization_id of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The objective_education_organization_id of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :rtype: int
        """
        return self._objective_education_organization_id

    @objective_education_organization_id.setter
    def objective_education_organization_id(self, objective_education_organization_id):
        """Sets the objective_education_organization_id of this EdFiStudentCompetencyObjectiveReference.

        The identifier assigned to an education organization.  # noqa: E501

        :param objective_education_organization_id: The objective_education_organization_id of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and objective_education_organization_id is None:
            raise ValueError("Invalid value for `objective_education_organization_id`, must not be `None`")  # noqa: E501

        self._objective_education_organization_id = objective_education_organization_id

    @property
    def objective_grade_level_descriptor(self):
        """Gets the objective_grade_level_descriptor of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501

        The grade level for which the CompetencyObjective is targeted.  # noqa: E501

        :return: The objective_grade_level_descriptor of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :rtype: str
        """
        return self._objective_grade_level_descriptor

    @objective_grade_level_descriptor.setter
    def objective_grade_level_descriptor(self, objective_grade_level_descriptor):
        """Sets the objective_grade_level_descriptor of this EdFiStudentCompetencyObjectiveReference.

        The grade level for which the CompetencyObjective is targeted.  # noqa: E501

        :param objective_grade_level_descriptor: The objective_grade_level_descriptor of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and objective_grade_level_descriptor is None:
            raise ValueError("Invalid value for `objective_grade_level_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                objective_grade_level_descriptor is not None and len(objective_grade_level_descriptor) > 306):
            raise ValueError("Invalid value for `objective_grade_level_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._objective_grade_level_descriptor = objective_grade_level_descriptor

    @property
    def student_unique_id(self):
        """Gets the student_unique_id of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :return: The student_unique_id of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :rtype: str
        """
        return self._student_unique_id

    @student_unique_id.setter
    def student_unique_id(self, student_unique_id):
        """Sets the student_unique_id of this EdFiStudentCompetencyObjectiveReference.

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :param student_unique_id: The student_unique_id of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and student_unique_id is None:
            raise ValueError("Invalid value for `student_unique_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                student_unique_id is not None and len(student_unique_id) > 32):
            raise ValueError("Invalid value for `student_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._student_unique_id = student_unique_id

    @property
    def link(self):
        """Gets the link of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501


        :return: The link of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiStudentCompetencyObjectiveReference.


        :param link: The link of this EdFiStudentCompetencyObjectiveReference.  # noqa: E501
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
        if issubclass(EdFiStudentCompetencyObjectiveReference, dict):
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
        if not isinstance(other, EdFiStudentCompetencyObjectiveReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentCompetencyObjectiveReference):
            return True

        return self.to_dict() != other.to_dict()
