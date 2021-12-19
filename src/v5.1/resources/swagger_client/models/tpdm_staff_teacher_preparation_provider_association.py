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


class TpdmStaffTeacherPreparationProviderAssociation(object):
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
        'id': 'str',
        'school_year_type_reference': 'EdFiSchoolYearTypeReference',
        'staff_reference': 'EdFiStaffReference',
        'teacher_preparation_provider_reference': 'TpdmTeacherPreparationProviderReference',
        'academic_subjects': 'list[TpdmStaffTeacherPreparationProviderAssociationAcademicSubject]',
        'grade_levels': 'list[TpdmStaffTeacherPreparationProviderAssociationGradeLevel]',
        'program_assignment_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'school_year_type_reference': 'schoolYearTypeReference',
        'staff_reference': 'staffReference',
        'teacher_preparation_provider_reference': 'teacherPreparationProviderReference',
        'academic_subjects': 'academicSubjects',
        'grade_levels': 'gradeLevels',
        'program_assignment_descriptor': 'programAssignmentDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, school_year_type_reference=None, staff_reference=None, teacher_preparation_provider_reference=None, academic_subjects=None, grade_levels=None, program_assignment_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmStaffTeacherPreparationProviderAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._school_year_type_reference = None
        self._staff_reference = None
        self._teacher_preparation_provider_reference = None
        self._academic_subjects = None
        self._grade_levels = None
        self._program_assignment_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.school_year_type_reference = school_year_type_reference
        self.staff_reference = staff_reference
        self.teacher_preparation_provider_reference = teacher_preparation_provider_reference
        if academic_subjects is not None:
            self.academic_subjects = academic_subjects
        if grade_levels is not None:
            self.grade_levels = grade_levels
        self.program_assignment_descriptor = program_assignment_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmStaffTeacherPreparationProviderAssociation.

          # noqa: E501

        :param id: The id of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def school_year_type_reference(self):
        """Gets the school_year_type_reference of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501


        :return: The school_year_type_reference of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: EdFiSchoolYearTypeReference
        """
        return self._school_year_type_reference

    @school_year_type_reference.setter
    def school_year_type_reference(self, school_year_type_reference):
        """Sets the school_year_type_reference of this TpdmStaffTeacherPreparationProviderAssociation.


        :param school_year_type_reference: The school_year_type_reference of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :type: EdFiSchoolYearTypeReference
        """
        if self._configuration.client_side_validation and school_year_type_reference is None:
            raise ValueError("Invalid value for `school_year_type_reference`, must not be `None`")  # noqa: E501

        self._school_year_type_reference = school_year_type_reference

    @property
    def staff_reference(self):
        """Gets the staff_reference of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501


        :return: The staff_reference of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: EdFiStaffReference
        """
        return self._staff_reference

    @staff_reference.setter
    def staff_reference(self, staff_reference):
        """Sets the staff_reference of this TpdmStaffTeacherPreparationProviderAssociation.


        :param staff_reference: The staff_reference of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :type: EdFiStaffReference
        """
        if self._configuration.client_side_validation and staff_reference is None:
            raise ValueError("Invalid value for `staff_reference`, must not be `None`")  # noqa: E501

        self._staff_reference = staff_reference

    @property
    def teacher_preparation_provider_reference(self):
        """Gets the teacher_preparation_provider_reference of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501


        :return: The teacher_preparation_provider_reference of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: TpdmTeacherPreparationProviderReference
        """
        return self._teacher_preparation_provider_reference

    @teacher_preparation_provider_reference.setter
    def teacher_preparation_provider_reference(self, teacher_preparation_provider_reference):
        """Sets the teacher_preparation_provider_reference of this TpdmStaffTeacherPreparationProviderAssociation.


        :param teacher_preparation_provider_reference: The teacher_preparation_provider_reference of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :type: TpdmTeacherPreparationProviderReference
        """
        if self._configuration.client_side_validation and teacher_preparation_provider_reference is None:
            raise ValueError("Invalid value for `teacher_preparation_provider_reference`, must not be `None`")  # noqa: E501

        self._teacher_preparation_provider_reference = teacher_preparation_provider_reference

    @property
    def academic_subjects(self):
        """Gets the academic_subjects of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501

        An unordered collection of staffTeacherPreparationProviderAssociationAcademicSubjects. The description of the content or subject area (e.g., arts, mathematics, reading, stenography, or a foreign language) of a degree.  # noqa: E501

        :return: The academic_subjects of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: list[TpdmStaffTeacherPreparationProviderAssociationAcademicSubject]
        """
        return self._academic_subjects

    @academic_subjects.setter
    def academic_subjects(self, academic_subjects):
        """Sets the academic_subjects of this TpdmStaffTeacherPreparationProviderAssociation.

        An unordered collection of staffTeacherPreparationProviderAssociationAcademicSubjects. The description of the content or subject area (e.g., arts, mathematics, reading, stenography, or a foreign language) of a degree.  # noqa: E501

        :param academic_subjects: The academic_subjects of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :type: list[TpdmStaffTeacherPreparationProviderAssociationAcademicSubject]
        """

        self._academic_subjects = academic_subjects

    @property
    def grade_levels(self):
        """Gets the grade_levels of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501

        An unordered collection of staffTeacherPreparationProviderAssociationGradeLevels. The grade levels for the association.  # noqa: E501

        :return: The grade_levels of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: list[TpdmStaffTeacherPreparationProviderAssociationGradeLevel]
        """
        return self._grade_levels

    @grade_levels.setter
    def grade_levels(self, grade_levels):
        """Sets the grade_levels of this TpdmStaffTeacherPreparationProviderAssociation.

        An unordered collection of staffTeacherPreparationProviderAssociationGradeLevels. The grade levels for the association.  # noqa: E501

        :param grade_levels: The grade_levels of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :type: list[TpdmStaffTeacherPreparationProviderAssociationGradeLevel]
        """

        self._grade_levels = grade_levels

    @property
    def program_assignment_descriptor(self):
        """Gets the program_assignment_descriptor of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501

        Program Assignment for the association  # noqa: E501

        :return: The program_assignment_descriptor of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: str
        """
        return self._program_assignment_descriptor

    @program_assignment_descriptor.setter
    def program_assignment_descriptor(self, program_assignment_descriptor):
        """Sets the program_assignment_descriptor of this TpdmStaffTeacherPreparationProviderAssociation.

        Program Assignment for the association  # noqa: E501

        :param program_assignment_descriptor: The program_assignment_descriptor of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and program_assignment_descriptor is None:
            raise ValueError("Invalid value for `program_assignment_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                program_assignment_descriptor is not None and len(program_assignment_descriptor) > 306):
            raise ValueError("Invalid value for `program_assignment_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._program_assignment_descriptor = program_assignment_descriptor

    @property
    def etag(self):
        """Gets the etag of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmStaffTeacherPreparationProviderAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmStaffTeacherPreparationProviderAssociation.  # noqa: E501
        :type: str
        """

        self._etag = etag

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
        if issubclass(TpdmStaffTeacherPreparationProviderAssociation, dict):
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
        if not isinstance(other, TpdmStaffTeacherPreparationProviderAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmStaffTeacherPreparationProviderAssociation):
            return True

        return self.to_dict() != other.to_dict()