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


class EdFiCourseTranscriptAcademicSubject(object):
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
        'academic_subject_descriptor': 'str'
    }

    attribute_map = {
        'academic_subject_descriptor': 'academicSubjectDescriptor'
    }

    def __init__(self, academic_subject_descriptor=None):  # noqa: E501
        """EdFiCourseTranscriptAcademicSubject - a model defined in Swagger"""  # noqa: E501

        self._academic_subject_descriptor = None
        self.discriminator = None

        self.academic_subject_descriptor = academic_subject_descriptor

    @property
    def academic_subject_descriptor(self):
        """Gets the academic_subject_descriptor of this EdFiCourseTranscriptAcademicSubject.  # noqa: E501

        The subject area for the course transcript credits awarded in the course transcript.  # noqa: E501

        :return: The academic_subject_descriptor of this EdFiCourseTranscriptAcademicSubject.  # noqa: E501
        :rtype: str
        """
        return self._academic_subject_descriptor

    @academic_subject_descriptor.setter
    def academic_subject_descriptor(self, academic_subject_descriptor):
        """Sets the academic_subject_descriptor of this EdFiCourseTranscriptAcademicSubject.

        The subject area for the course transcript credits awarded in the course transcript.  # noqa: E501

        :param academic_subject_descriptor: The academic_subject_descriptor of this EdFiCourseTranscriptAcademicSubject.  # noqa: E501
        :type: str
        """
        if academic_subject_descriptor is None:
            raise ValueError("Invalid value for `academic_subject_descriptor`, must not be `None`")  # noqa: E501
        if academic_subject_descriptor is not None and len(academic_subject_descriptor) > 306:
            raise ValueError("Invalid value for `academic_subject_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._academic_subject_descriptor = academic_subject_descriptor

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
        if issubclass(EdFiCourseTranscriptAcademicSubject, dict):
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
        if not isinstance(other, EdFiCourseTranscriptAcademicSubject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
