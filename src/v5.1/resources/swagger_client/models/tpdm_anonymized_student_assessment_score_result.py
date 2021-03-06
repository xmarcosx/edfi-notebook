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


class TpdmAnonymizedStudentAssessmentScoreResult(object):
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
        'assessment_reporting_method_descriptor': 'str',
        'result_datatype_type_descriptor': 'str',
        'result': 'str'
    }

    attribute_map = {
        'assessment_reporting_method_descriptor': 'assessmentReportingMethodDescriptor',
        'result_datatype_type_descriptor': 'resultDatatypeTypeDescriptor',
        'result': 'result'
    }

    def __init__(self, assessment_reporting_method_descriptor=None, result_datatype_type_descriptor=None, result=None, _configuration=None):  # noqa: E501
        """TpdmAnonymizedStudentAssessmentScoreResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assessment_reporting_method_descriptor = None
        self._result_datatype_type_descriptor = None
        self._result = None
        self.discriminator = None

        self.assessment_reporting_method_descriptor = assessment_reporting_method_descriptor
        self.result_datatype_type_descriptor = result_datatype_type_descriptor
        self.result = result

    @property
    def assessment_reporting_method_descriptor(self):
        """Gets the assessment_reporting_method_descriptor of this TpdmAnonymizedStudentAssessmentScoreResult.  # noqa: E501

        The method that the administrator of the assessment uses to report the performance and achievement of all students. It may be a qualitative method such as performance level descriptors or a quantitative method such as a numerical grade or cut score. More than one type of reporting method may be used.  # noqa: E501

        :return: The assessment_reporting_method_descriptor of this TpdmAnonymizedStudentAssessmentScoreResult.  # noqa: E501
        :rtype: str
        """
        return self._assessment_reporting_method_descriptor

    @assessment_reporting_method_descriptor.setter
    def assessment_reporting_method_descriptor(self, assessment_reporting_method_descriptor):
        """Sets the assessment_reporting_method_descriptor of this TpdmAnonymizedStudentAssessmentScoreResult.

        The method that the administrator of the assessment uses to report the performance and achievement of all students. It may be a qualitative method such as performance level descriptors or a quantitative method such as a numerical grade or cut score. More than one type of reporting method may be used.  # noqa: E501

        :param assessment_reporting_method_descriptor: The assessment_reporting_method_descriptor of this TpdmAnonymizedStudentAssessmentScoreResult.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and assessment_reporting_method_descriptor is None:
            raise ValueError("Invalid value for `assessment_reporting_method_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                assessment_reporting_method_descriptor is not None and len(assessment_reporting_method_descriptor) > 306):
            raise ValueError("Invalid value for `assessment_reporting_method_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._assessment_reporting_method_descriptor = assessment_reporting_method_descriptor

    @property
    def result_datatype_type_descriptor(self):
        """Gets the result_datatype_type_descriptor of this TpdmAnonymizedStudentAssessmentScoreResult.  # noqa: E501

        The datatype of the result. The results can be expressed as a number, percentile, range, level, etc.  # noqa: E501

        :return: The result_datatype_type_descriptor of this TpdmAnonymizedStudentAssessmentScoreResult.  # noqa: E501
        :rtype: str
        """
        return self._result_datatype_type_descriptor

    @result_datatype_type_descriptor.setter
    def result_datatype_type_descriptor(self, result_datatype_type_descriptor):
        """Sets the result_datatype_type_descriptor of this TpdmAnonymizedStudentAssessmentScoreResult.

        The datatype of the result. The results can be expressed as a number, percentile, range, level, etc.  # noqa: E501

        :param result_datatype_type_descriptor: The result_datatype_type_descriptor of this TpdmAnonymizedStudentAssessmentScoreResult.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and result_datatype_type_descriptor is None:
            raise ValueError("Invalid value for `result_datatype_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                result_datatype_type_descriptor is not None and len(result_datatype_type_descriptor) > 306):
            raise ValueError("Invalid value for `result_datatype_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._result_datatype_type_descriptor = result_datatype_type_descriptor

    @property
    def result(self):
        """Gets the result of this TpdmAnonymizedStudentAssessmentScoreResult.  # noqa: E501

        The value of a meaningful raw score or statistical expression of the performance of an individual. The results can be expressed as a number, percentile, range, level, etc.  # noqa: E501

        :return: The result of this TpdmAnonymizedStudentAssessmentScoreResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this TpdmAnonymizedStudentAssessmentScoreResult.

        The value of a meaningful raw score or statistical expression of the performance of an individual. The results can be expressed as a number, percentile, range, level, etc.  # noqa: E501

        :param result: The result of this TpdmAnonymizedStudentAssessmentScoreResult.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                result is not None and len(result) > 35):
            raise ValueError("Invalid value for `result`, length must be less than or equal to `35`")  # noqa: E501

        self._result = result

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
        if issubclass(TpdmAnonymizedStudentAssessmentScoreResult, dict):
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
        if not isinstance(other, TpdmAnonymizedStudentAssessmentScoreResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmAnonymizedStudentAssessmentScoreResult):
            return True

        return self.to_dict() != other.to_dict()
