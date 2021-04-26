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


class TpdmQuantitativeMeasureScore(object):
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
        'evaluation_element_rating_reference': 'TpdmEvaluationElementRatingReference',
        'quantitative_measure_reference': 'TpdmQuantitativeMeasureReference',
        'score_value': 'float',
        'standard_error': 'float',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'evaluation_element_rating_reference': 'evaluationElementRatingReference',
        'quantitative_measure_reference': 'quantitativeMeasureReference',
        'score_value': 'scoreValue',
        'standard_error': 'standardError',
        'etag': '_etag'
    }

    def __init__(self, id=None, evaluation_element_rating_reference=None, quantitative_measure_reference=None, score_value=None, standard_error=None, etag=None):  # noqa: E501
        """TpdmQuantitativeMeasureScore - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._evaluation_element_rating_reference = None
        self._quantitative_measure_reference = None
        self._score_value = None
        self._standard_error = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.evaluation_element_rating_reference = evaluation_element_rating_reference
        self.quantitative_measure_reference = quantitative_measure_reference
        self.score_value = score_value
        if standard_error is not None:
            self.standard_error = standard_error
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmQuantitativeMeasureScore.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmQuantitativeMeasureScore.

          # noqa: E501

        :param id: The id of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def evaluation_element_rating_reference(self):
        """Gets the evaluation_element_rating_reference of this TpdmQuantitativeMeasureScore.  # noqa: E501


        :return: The evaluation_element_rating_reference of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :rtype: TpdmEvaluationElementRatingReference
        """
        return self._evaluation_element_rating_reference

    @evaluation_element_rating_reference.setter
    def evaluation_element_rating_reference(self, evaluation_element_rating_reference):
        """Sets the evaluation_element_rating_reference of this TpdmQuantitativeMeasureScore.


        :param evaluation_element_rating_reference: The evaluation_element_rating_reference of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :type: TpdmEvaluationElementRatingReference
        """
        if evaluation_element_rating_reference is None:
            raise ValueError("Invalid value for `evaluation_element_rating_reference`, must not be `None`")  # noqa: E501

        self._evaluation_element_rating_reference = evaluation_element_rating_reference

    @property
    def quantitative_measure_reference(self):
        """Gets the quantitative_measure_reference of this TpdmQuantitativeMeasureScore.  # noqa: E501


        :return: The quantitative_measure_reference of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :rtype: TpdmQuantitativeMeasureReference
        """
        return self._quantitative_measure_reference

    @quantitative_measure_reference.setter
    def quantitative_measure_reference(self, quantitative_measure_reference):
        """Sets the quantitative_measure_reference of this TpdmQuantitativeMeasureScore.


        :param quantitative_measure_reference: The quantitative_measure_reference of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :type: TpdmQuantitativeMeasureReference
        """
        if quantitative_measure_reference is None:
            raise ValueError("Invalid value for `quantitative_measure_reference`, must not be `None`")  # noqa: E501

        self._quantitative_measure_reference = quantitative_measure_reference

    @property
    def score_value(self):
        """Gets the score_value of this TpdmQuantitativeMeasureScore.  # noqa: E501

        The score value for the quantitive measure.  # noqa: E501

        :return: The score_value of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :rtype: float
        """
        return self._score_value

    @score_value.setter
    def score_value(self, score_value):
        """Sets the score_value of this TpdmQuantitativeMeasureScore.

        The score value for the quantitive measure.  # noqa: E501

        :param score_value: The score_value of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :type: float
        """
        if score_value is None:
            raise ValueError("Invalid value for `score_value`, must not be `None`")  # noqa: E501

        self._score_value = score_value

    @property
    def standard_error(self):
        """Gets the standard_error of this TpdmQuantitativeMeasureScore.  # noqa: E501

        The standard error for the quantitative measure.  # noqa: E501

        :return: The standard_error of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :rtype: float
        """
        return self._standard_error

    @standard_error.setter
    def standard_error(self, standard_error):
        """Sets the standard_error of this TpdmQuantitativeMeasureScore.

        The standard error for the quantitative measure.  # noqa: E501

        :param standard_error: The standard_error of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :type: float
        """

        self._standard_error = standard_error

    @property
    def etag(self):
        """Gets the etag of this TpdmQuantitativeMeasureScore.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmQuantitativeMeasureScore.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmQuantitativeMeasureScore.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmQuantitativeMeasureScore.  # noqa: E501
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
        if issubclass(TpdmQuantitativeMeasureScore, dict):
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
        if not isinstance(other, TpdmQuantitativeMeasureScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
