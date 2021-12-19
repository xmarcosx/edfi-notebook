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


class TpdmApplicantTeacherPreparationProgram(object):
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
        'teacher_preparation_program_name': 'str',
        'level_of_degree_awarded_descriptor': 'str',
        'teacher_preparation_program_type_descriptor': 'str',
        'gpa': 'float',
        'major_specialization': 'str',
        'name_of_institution': 'str',
        'teacher_preparation_program_identifier': 'str'
    }

    attribute_map = {
        'teacher_preparation_program_name': 'teacherPreparationProgramName',
        'level_of_degree_awarded_descriptor': 'levelOfDegreeAwardedDescriptor',
        'teacher_preparation_program_type_descriptor': 'teacherPreparationProgramTypeDescriptor',
        'gpa': 'gpa',
        'major_specialization': 'majorSpecialization',
        'name_of_institution': 'nameOfInstitution',
        'teacher_preparation_program_identifier': 'teacherPreparationProgramIdentifier'
    }

    def __init__(self, teacher_preparation_program_name=None, level_of_degree_awarded_descriptor=None, teacher_preparation_program_type_descriptor=None, gpa=None, major_specialization=None, name_of_institution=None, teacher_preparation_program_identifier=None, _configuration=None):  # noqa: E501
        """TpdmApplicantTeacherPreparationProgram - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._teacher_preparation_program_name = None
        self._level_of_degree_awarded_descriptor = None
        self._teacher_preparation_program_type_descriptor = None
        self._gpa = None
        self._major_specialization = None
        self._name_of_institution = None
        self._teacher_preparation_program_identifier = None
        self.discriminator = None

        self.teacher_preparation_program_name = teacher_preparation_program_name
        self.level_of_degree_awarded_descriptor = level_of_degree_awarded_descriptor
        self.teacher_preparation_program_type_descriptor = teacher_preparation_program_type_descriptor
        if gpa is not None:
            self.gpa = gpa
        self.major_specialization = major_specialization
        self.name_of_institution = name_of_institution
        if teacher_preparation_program_identifier is not None:
            self.teacher_preparation_program_identifier = teacher_preparation_program_identifier

    @property
    def teacher_preparation_program_name(self):
        """Gets the teacher_preparation_program_name of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501

        The name of the Teacher Preparation Program.  # noqa: E501

        :return: The teacher_preparation_program_name of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :rtype: str
        """
        return self._teacher_preparation_program_name

    @teacher_preparation_program_name.setter
    def teacher_preparation_program_name(self, teacher_preparation_program_name):
        """Sets the teacher_preparation_program_name of this TpdmApplicantTeacherPreparationProgram.

        The name of the Teacher Preparation Program.  # noqa: E501

        :param teacher_preparation_program_name: The teacher_preparation_program_name of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and teacher_preparation_program_name is None:
            raise ValueError("Invalid value for `teacher_preparation_program_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                teacher_preparation_program_name is not None and len(teacher_preparation_program_name) > 255):
            raise ValueError("Invalid value for `teacher_preparation_program_name`, length must be less than or equal to `255`")  # noqa: E501

        self._teacher_preparation_program_name = teacher_preparation_program_name

    @property
    def level_of_degree_awarded_descriptor(self):
        """Gets the level_of_degree_awarded_descriptor of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501

        The level of degree awarded by the teacher preparation program to the person (e.g., Certificate Only, Bachelor's, Master's, etc.).  # noqa: E501

        :return: The level_of_degree_awarded_descriptor of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :rtype: str
        """
        return self._level_of_degree_awarded_descriptor

    @level_of_degree_awarded_descriptor.setter
    def level_of_degree_awarded_descriptor(self, level_of_degree_awarded_descriptor):
        """Sets the level_of_degree_awarded_descriptor of this TpdmApplicantTeacherPreparationProgram.

        The level of degree awarded by the teacher preparation program to the person (e.g., Certificate Only, Bachelor's, Master's, etc.).  # noqa: E501

        :param level_of_degree_awarded_descriptor: The level_of_degree_awarded_descriptor of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and level_of_degree_awarded_descriptor is None:
            raise ValueError("Invalid value for `level_of_degree_awarded_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                level_of_degree_awarded_descriptor is not None and len(level_of_degree_awarded_descriptor) > 306):
            raise ValueError("Invalid value for `level_of_degree_awarded_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._level_of_degree_awarded_descriptor = level_of_degree_awarded_descriptor

    @property
    def teacher_preparation_program_type_descriptor(self):
        """Gets the teacher_preparation_program_type_descriptor of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501

        The type of teacher prep program (e.g., college, alternative, TFA, etc.).  # noqa: E501

        :return: The teacher_preparation_program_type_descriptor of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :rtype: str
        """
        return self._teacher_preparation_program_type_descriptor

    @teacher_preparation_program_type_descriptor.setter
    def teacher_preparation_program_type_descriptor(self, teacher_preparation_program_type_descriptor):
        """Sets the teacher_preparation_program_type_descriptor of this TpdmApplicantTeacherPreparationProgram.

        The type of teacher prep program (e.g., college, alternative, TFA, etc.).  # noqa: E501

        :param teacher_preparation_program_type_descriptor: The teacher_preparation_program_type_descriptor of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and teacher_preparation_program_type_descriptor is None:
            raise ValueError("Invalid value for `teacher_preparation_program_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                teacher_preparation_program_type_descriptor is not None and len(teacher_preparation_program_type_descriptor) > 306):
            raise ValueError("Invalid value for `teacher_preparation_program_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._teacher_preparation_program_type_descriptor = teacher_preparation_program_type_descriptor

    @property
    def gpa(self):
        """Gets the gpa of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501

        The final GPA the teacher achieved in the program.  # noqa: E501

        :return: The gpa of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :rtype: float
        """
        return self._gpa

    @gpa.setter
    def gpa(self, gpa):
        """Sets the gpa of this TpdmApplicantTeacherPreparationProgram.

        The final GPA the teacher achieved in the program.  # noqa: E501

        :param gpa: The gpa of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :type: float
        """

        self._gpa = gpa

    @property
    def major_specialization(self):
        """Gets the major_specialization of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501

        The major area for a degree or area of specialization for a certificate.  # noqa: E501

        :return: The major_specialization of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :rtype: str
        """
        return self._major_specialization

    @major_specialization.setter
    def major_specialization(self, major_specialization):
        """Sets the major_specialization of this TpdmApplicantTeacherPreparationProgram.

        The major area for a degree or area of specialization for a certificate.  # noqa: E501

        :param major_specialization: The major_specialization of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and major_specialization is None:
            raise ValueError("Invalid value for `major_specialization`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                major_specialization is not None and len(major_specialization) > 75):
            raise ValueError("Invalid value for `major_specialization`, length must be less than or equal to `75`")  # noqa: E501

        self._major_specialization = major_specialization

    @property
    def name_of_institution(self):
        """Gets the name_of_institution of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501

        The name of the organization providing the teacher preparation program.  # noqa: E501

        :return: The name_of_institution of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :rtype: str
        """
        return self._name_of_institution

    @name_of_institution.setter
    def name_of_institution(self, name_of_institution):
        """Sets the name_of_institution of this TpdmApplicantTeacherPreparationProgram.

        The name of the organization providing the teacher preparation program.  # noqa: E501

        :param name_of_institution: The name_of_institution of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name_of_institution is None:
            raise ValueError("Invalid value for `name_of_institution`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name_of_institution is not None and len(name_of_institution) > 75):
            raise ValueError("Invalid value for `name_of_institution`, length must be less than or equal to `75`")  # noqa: E501

        self._name_of_institution = name_of_institution

    @property
    def teacher_preparation_program_identifier(self):
        """Gets the teacher_preparation_program_identifier of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501

        An identifier assigned to the teacher preparation program.  # noqa: E501

        :return: The teacher_preparation_program_identifier of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :rtype: str
        """
        return self._teacher_preparation_program_identifier

    @teacher_preparation_program_identifier.setter
    def teacher_preparation_program_identifier(self, teacher_preparation_program_identifier):
        """Sets the teacher_preparation_program_identifier of this TpdmApplicantTeacherPreparationProgram.

        An identifier assigned to the teacher preparation program.  # noqa: E501

        :param teacher_preparation_program_identifier: The teacher_preparation_program_identifier of this TpdmApplicantTeacherPreparationProgram.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                teacher_preparation_program_identifier is not None and len(teacher_preparation_program_identifier) > 75):
            raise ValueError("Invalid value for `teacher_preparation_program_identifier`, length must be less than or equal to `75`")  # noqa: E501

        self._teacher_preparation_program_identifier = teacher_preparation_program_identifier

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
        if issubclass(TpdmApplicantTeacherPreparationProgram, dict):
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
        if not isinstance(other, TpdmApplicantTeacherPreparationProgram):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmApplicantTeacherPreparationProgram):
            return True

        return self.to_dict() != other.to_dict()
