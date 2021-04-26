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


class TpdmEvaluationElementRatingLevel(object):
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
        'evaluation_rating_level_descriptor': 'str',
        'max_rating': 'float',
        'min_rating': 'float'
    }

    attribute_map = {
        'evaluation_rating_level_descriptor': 'evaluationRatingLevelDescriptor',
        'max_rating': 'maxRating',
        'min_rating': 'minRating'
    }

    def __init__(self, evaluation_rating_level_descriptor=None, max_rating=None, min_rating=None):  # noqa: E501
        """TpdmEvaluationElementRatingLevel - a model defined in Swagger"""  # noqa: E501

        self._evaluation_rating_level_descriptor = None
        self._max_rating = None
        self._min_rating = None
        self.discriminator = None

        self.evaluation_rating_level_descriptor = evaluation_rating_level_descriptor
        if max_rating is not None:
            self.max_rating = max_rating
        if min_rating is not None:
            self.min_rating = min_rating

    @property
    def evaluation_rating_level_descriptor(self):
        """Gets the evaluation_rating_level_descriptor of this TpdmEvaluationElementRatingLevel.  # noqa: E501

        The title for a level of rating or evaluation band (e.g., Excellent, Acceptable, Needs Improvement, Unacceptable).  # noqa: E501

        :return: The evaluation_rating_level_descriptor of this TpdmEvaluationElementRatingLevel.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_rating_level_descriptor

    @evaluation_rating_level_descriptor.setter
    def evaluation_rating_level_descriptor(self, evaluation_rating_level_descriptor):
        """Sets the evaluation_rating_level_descriptor of this TpdmEvaluationElementRatingLevel.

        The title for a level of rating or evaluation band (e.g., Excellent, Acceptable, Needs Improvement, Unacceptable).  # noqa: E501

        :param evaluation_rating_level_descriptor: The evaluation_rating_level_descriptor of this TpdmEvaluationElementRatingLevel.  # noqa: E501
        :type: str
        """
        if evaluation_rating_level_descriptor is None:
            raise ValueError("Invalid value for `evaluation_rating_level_descriptor`, must not be `None`")  # noqa: E501
        if evaluation_rating_level_descriptor is not None and len(evaluation_rating_level_descriptor) > 306:
            raise ValueError("Invalid value for `evaluation_rating_level_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._evaluation_rating_level_descriptor = evaluation_rating_level_descriptor

    @property
    def max_rating(self):
        """Gets the max_rating of this TpdmEvaluationElementRatingLevel.  # noqa: E501

        The maximum numerical rating or score to achieve the evaluation rating level.  # noqa: E501

        :return: The max_rating of this TpdmEvaluationElementRatingLevel.  # noqa: E501
        :rtype: float
        """
        return self._max_rating

    @max_rating.setter
    def max_rating(self, max_rating):
        """Sets the max_rating of this TpdmEvaluationElementRatingLevel.

        The maximum numerical rating or score to achieve the evaluation rating level.  # noqa: E501

        :param max_rating: The max_rating of this TpdmEvaluationElementRatingLevel.  # noqa: E501
        :type: float
        """

        self._max_rating = max_rating

    @property
    def min_rating(self):
        """Gets the min_rating of this TpdmEvaluationElementRatingLevel.  # noqa: E501

        The minimum numerical rating or score to achieve the evaluation rating level.  # noqa: E501

        :return: The min_rating of this TpdmEvaluationElementRatingLevel.  # noqa: E501
        :rtype: float
        """
        return self._min_rating

    @min_rating.setter
    def min_rating(self, min_rating):
        """Sets the min_rating of this TpdmEvaluationElementRatingLevel.

        The minimum numerical rating or score to achieve the evaluation rating level.  # noqa: E501

        :param min_rating: The min_rating of this TpdmEvaluationElementRatingLevel.  # noqa: E501
        :type: float
        """

        self._min_rating = min_rating

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
        if issubclass(TpdmEvaluationElementRatingLevel, dict):
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
        if not isinstance(other, TpdmEvaluationElementRatingLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
