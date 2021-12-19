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


class TpdmTeacherCandidateIdentificationCode(object):
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
        'student_identification_system_descriptor': 'str',
        'assigning_organization_identification_code': 'str',
        'identification_code': 'str'
    }

    attribute_map = {
        'student_identification_system_descriptor': 'studentIdentificationSystemDescriptor',
        'assigning_organization_identification_code': 'assigningOrganizationIdentificationCode',
        'identification_code': 'identificationCode'
    }

    def __init__(self, student_identification_system_descriptor=None, assigning_organization_identification_code=None, identification_code=None, _configuration=None):  # noqa: E501
        """TpdmTeacherCandidateIdentificationCode - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._student_identification_system_descriptor = None
        self._assigning_organization_identification_code = None
        self._identification_code = None
        self.discriminator = None

        self.student_identification_system_descriptor = student_identification_system_descriptor
        self.assigning_organization_identification_code = assigning_organization_identification_code
        self.identification_code = identification_code

    @property
    def student_identification_system_descriptor(self):
        """Gets the student_identification_system_descriptor of this TpdmTeacherCandidateIdentificationCode.  # noqa: E501

        A coding scheme that is used for identification and record-keeping purposes by schools, social services, or other agencies to refer to a student.  # noqa: E501

        :return: The student_identification_system_descriptor of this TpdmTeacherCandidateIdentificationCode.  # noqa: E501
        :rtype: str
        """
        return self._student_identification_system_descriptor

    @student_identification_system_descriptor.setter
    def student_identification_system_descriptor(self, student_identification_system_descriptor):
        """Sets the student_identification_system_descriptor of this TpdmTeacherCandidateIdentificationCode.

        A coding scheme that is used for identification and record-keeping purposes by schools, social services, or other agencies to refer to a student.  # noqa: E501

        :param student_identification_system_descriptor: The student_identification_system_descriptor of this TpdmTeacherCandidateIdentificationCode.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and student_identification_system_descriptor is None:
            raise ValueError("Invalid value for `student_identification_system_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                student_identification_system_descriptor is not None and len(student_identification_system_descriptor) > 306):
            raise ValueError("Invalid value for `student_identification_system_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._student_identification_system_descriptor = student_identification_system_descriptor

    @property
    def assigning_organization_identification_code(self):
        """Gets the assigning_organization_identification_code of this TpdmTeacherCandidateIdentificationCode.  # noqa: E501

        The organization code or name assigning the StudentIdentificationCode.  # noqa: E501

        :return: The assigning_organization_identification_code of this TpdmTeacherCandidateIdentificationCode.  # noqa: E501
        :rtype: str
        """
        return self._assigning_organization_identification_code

    @assigning_organization_identification_code.setter
    def assigning_organization_identification_code(self, assigning_organization_identification_code):
        """Sets the assigning_organization_identification_code of this TpdmTeacherCandidateIdentificationCode.

        The organization code or name assigning the StudentIdentificationCode.  # noqa: E501

        :param assigning_organization_identification_code: The assigning_organization_identification_code of this TpdmTeacherCandidateIdentificationCode.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and assigning_organization_identification_code is None:
            raise ValueError("Invalid value for `assigning_organization_identification_code`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                assigning_organization_identification_code is not None and len(assigning_organization_identification_code) > 60):
            raise ValueError("Invalid value for `assigning_organization_identification_code`, length must be less than or equal to `60`")  # noqa: E501

        self._assigning_organization_identification_code = assigning_organization_identification_code

    @property
    def identification_code(self):
        """Gets the identification_code of this TpdmTeacherCandidateIdentificationCode.  # noqa: E501

        A unique number or alphanumeric code assigned to a student by a school, school system, a state, or other agency or entity.  # noqa: E501

        :return: The identification_code of this TpdmTeacherCandidateIdentificationCode.  # noqa: E501
        :rtype: str
        """
        return self._identification_code

    @identification_code.setter
    def identification_code(self, identification_code):
        """Sets the identification_code of this TpdmTeacherCandidateIdentificationCode.

        A unique number or alphanumeric code assigned to a student by a school, school system, a state, or other agency or entity.  # noqa: E501

        :param identification_code: The identification_code of this TpdmTeacherCandidateIdentificationCode.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and identification_code is None:
            raise ValueError("Invalid value for `identification_code`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                identification_code is not None and len(identification_code) > 60):
            raise ValueError("Invalid value for `identification_code`, length must be less than or equal to `60`")  # noqa: E501

        self._identification_code = identification_code

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
        if issubclass(TpdmTeacherCandidateIdentificationCode, dict):
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
        if not isinstance(other, TpdmTeacherCandidateIdentificationCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmTeacherCandidateIdentificationCode):
            return True

        return self.to_dict() != other.to_dict()
