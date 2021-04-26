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


class EdFiGeneralStudentProgramAssociationReference(object):
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
        'education_organization_id': 'int',
        'program_education_organization_id': 'int',
        'program_name': 'str',
        'program_type_descriptor': 'str',
        'student_unique_id': 'str',
        'link': 'Link'
    }

    attribute_map = {
        'begin_date': 'beginDate',
        'education_organization_id': 'educationOrganizationId',
        'program_education_organization_id': 'programEducationOrganizationId',
        'program_name': 'programName',
        'program_type_descriptor': 'programTypeDescriptor',
        'student_unique_id': 'studentUniqueId',
        'link': 'link'
    }

    def __init__(self, begin_date=None, education_organization_id=None, program_education_organization_id=None, program_name=None, program_type_descriptor=None, student_unique_id=None, link=None):  # noqa: E501
        """EdFiGeneralStudentProgramAssociationReference - a model defined in Swagger"""  # noqa: E501

        self._begin_date = None
        self._education_organization_id = None
        self._program_education_organization_id = None
        self._program_name = None
        self._program_type_descriptor = None
        self._student_unique_id = None
        self._link = None
        self.discriminator = None

        self.begin_date = begin_date
        self.education_organization_id = education_organization_id
        self.program_education_organization_id = program_education_organization_id
        self.program_name = program_name
        self.program_type_descriptor = program_type_descriptor
        self.student_unique_id = student_unique_id
        if link is not None:
            self.link = link

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501

        The earliest date the student is involved with the program. Typically, this is the date the student becomes eligible for the program.  # noqa: E501

        :return: The begin_date of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiGeneralStudentProgramAssociationReference.

        The earliest date the student is involved with the program. Typically, this is the date the student becomes eligible for the program.  # noqa: E501

        :param begin_date: The begin_date of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :type: date
        """
        if begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def education_organization_id(self):
        """Gets the education_organization_id of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The education_organization_id of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :rtype: int
        """
        return self._education_organization_id

    @education_organization_id.setter
    def education_organization_id(self, education_organization_id):
        """Sets the education_organization_id of this EdFiGeneralStudentProgramAssociationReference.

        The identifier assigned to an education organization.  # noqa: E501

        :param education_organization_id: The education_organization_id of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :type: int
        """
        if education_organization_id is None:
            raise ValueError("Invalid value for `education_organization_id`, must not be `None`")  # noqa: E501

        self._education_organization_id = education_organization_id

    @property
    def program_education_organization_id(self):
        """Gets the program_education_organization_id of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The program_education_organization_id of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :rtype: int
        """
        return self._program_education_organization_id

    @program_education_organization_id.setter
    def program_education_organization_id(self, program_education_organization_id):
        """Sets the program_education_organization_id of this EdFiGeneralStudentProgramAssociationReference.

        The identifier assigned to an education organization.  # noqa: E501

        :param program_education_organization_id: The program_education_organization_id of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :type: int
        """
        if program_education_organization_id is None:
            raise ValueError("Invalid value for `program_education_organization_id`, must not be `None`")  # noqa: E501

        self._program_education_organization_id = program_education_organization_id

    @property
    def program_name(self):
        """Gets the program_name of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501

        The formal name of the Program of instruction, training, services, or benefits available through federal, state, or local agencies.  # noqa: E501

        :return: The program_name of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this EdFiGeneralStudentProgramAssociationReference.

        The formal name of the Program of instruction, training, services, or benefits available through federal, state, or local agencies.  # noqa: E501

        :param program_name: The program_name of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :type: str
        """
        if program_name is None:
            raise ValueError("Invalid value for `program_name`, must not be `None`")  # noqa: E501
        if program_name is not None and len(program_name) > 60:
            raise ValueError("Invalid value for `program_name`, length must be less than or equal to `60`")  # noqa: E501

        self._program_name = program_name

    @property
    def program_type_descriptor(self):
        """Gets the program_type_descriptor of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501

        The type of program.  # noqa: E501

        :return: The program_type_descriptor of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :rtype: str
        """
        return self._program_type_descriptor

    @program_type_descriptor.setter
    def program_type_descriptor(self, program_type_descriptor):
        """Sets the program_type_descriptor of this EdFiGeneralStudentProgramAssociationReference.

        The type of program.  # noqa: E501

        :param program_type_descriptor: The program_type_descriptor of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :type: str
        """
        if program_type_descriptor is None:
            raise ValueError("Invalid value for `program_type_descriptor`, must not be `None`")  # noqa: E501
        if program_type_descriptor is not None and len(program_type_descriptor) > 306:
            raise ValueError("Invalid value for `program_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._program_type_descriptor = program_type_descriptor

    @property
    def student_unique_id(self):
        """Gets the student_unique_id of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :return: The student_unique_id of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :rtype: str
        """
        return self._student_unique_id

    @student_unique_id.setter
    def student_unique_id(self, student_unique_id):
        """Sets the student_unique_id of this EdFiGeneralStudentProgramAssociationReference.

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :param student_unique_id: The student_unique_id of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :type: str
        """
        if student_unique_id is None:
            raise ValueError("Invalid value for `student_unique_id`, must not be `None`")  # noqa: E501
        if student_unique_id is not None and len(student_unique_id) > 32:
            raise ValueError("Invalid value for `student_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._student_unique_id = student_unique_id

    @property
    def link(self):
        """Gets the link of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501


        :return: The link of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiGeneralStudentProgramAssociationReference.


        :param link: The link of this EdFiGeneralStudentProgramAssociationReference.  # noqa: E501
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
        if issubclass(EdFiGeneralStudentProgramAssociationReference, dict):
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
        if not isinstance(other, EdFiGeneralStudentProgramAssociationReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
