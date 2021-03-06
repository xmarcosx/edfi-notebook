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


class EdFiGraduationPlanRequiredAssessment(object):
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
        'assessment_reference': 'EdFiAssessmentReference',
        'scores': 'list[EdFiGraduationPlanRequiredAssessmentScore]',
        'performance_level': 'EdFiGraduationPlanRequiredAssessmentPerformanceLevel'
    }

    attribute_map = {
        'assessment_reference': 'assessmentReference',
        'scores': 'scores',
        'performance_level': 'performanceLevel'
    }

    def __init__(self, assessment_reference=None, scores=None, performance_level=None, _configuration=None):  # noqa: E501
        """EdFiGraduationPlanRequiredAssessment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assessment_reference = None
        self._scores = None
        self._performance_level = None
        self.discriminator = None

        self.assessment_reference = assessment_reference
        if scores is not None:
            self.scores = scores
        if performance_level is not None:
            self.performance_level = performance_level

    @property
    def assessment_reference(self):
        """Gets the assessment_reference of this EdFiGraduationPlanRequiredAssessment.  # noqa: E501


        :return: The assessment_reference of this EdFiGraduationPlanRequiredAssessment.  # noqa: E501
        :rtype: EdFiAssessmentReference
        """
        return self._assessment_reference

    @assessment_reference.setter
    def assessment_reference(self, assessment_reference):
        """Sets the assessment_reference of this EdFiGraduationPlanRequiredAssessment.


        :param assessment_reference: The assessment_reference of this EdFiGraduationPlanRequiredAssessment.  # noqa: E501
        :type: EdFiAssessmentReference
        """
        if self._configuration.client_side_validation and assessment_reference is None:
            raise ValueError("Invalid value for `assessment_reference`, must not be `None`")  # noqa: E501

        self._assessment_reference = assessment_reference

    @property
    def scores(self):
        """Gets the scores of this EdFiGraduationPlanRequiredAssessment.  # noqa: E501

        An unordered collection of graduationPlanRequiredAssessmentScores. Score required to be met or exceeded.  # noqa: E501

        :return: The scores of this EdFiGraduationPlanRequiredAssessment.  # noqa: E501
        :rtype: list[EdFiGraduationPlanRequiredAssessmentScore]
        """
        return self._scores

    @scores.setter
    def scores(self, scores):
        """Sets the scores of this EdFiGraduationPlanRequiredAssessment.

        An unordered collection of graduationPlanRequiredAssessmentScores. Score required to be met or exceeded.  # noqa: E501

        :param scores: The scores of this EdFiGraduationPlanRequiredAssessment.  # noqa: E501
        :type: list[EdFiGraduationPlanRequiredAssessmentScore]
        """

        self._scores = scores

    @property
    def performance_level(self):
        """Gets the performance_level of this EdFiGraduationPlanRequiredAssessment.  # noqa: E501


        :return: The performance_level of this EdFiGraduationPlanRequiredAssessment.  # noqa: E501
        :rtype: EdFiGraduationPlanRequiredAssessmentPerformanceLevel
        """
        return self._performance_level

    @performance_level.setter
    def performance_level(self, performance_level):
        """Sets the performance_level of this EdFiGraduationPlanRequiredAssessment.


        :param performance_level: The performance_level of this EdFiGraduationPlanRequiredAssessment.  # noqa: E501
        :type: EdFiGraduationPlanRequiredAssessmentPerformanceLevel
        """

        self._performance_level = performance_level

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
        if issubclass(EdFiGraduationPlanRequiredAssessment, dict):
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
        if not isinstance(other, EdFiGraduationPlanRequiredAssessment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiGraduationPlanRequiredAssessment):
            return True

        return self.to_dict() != other.to_dict()
