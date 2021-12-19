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


class EdFiSurveyQuestionResponseChoice(object):
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
        'sort_order': 'int',
        'numeric_value': 'int',
        'text_value': 'str'
    }

    attribute_map = {
        'sort_order': 'sortOrder',
        'numeric_value': 'numericValue',
        'text_value': 'textValue'
    }

    def __init__(self, sort_order=None, numeric_value=None, text_value=None, _configuration=None):  # noqa: E501
        """EdFiSurveyQuestionResponseChoice - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sort_order = None
        self._numeric_value = None
        self._text_value = None
        self.discriminator = None

        self.sort_order = sort_order
        if numeric_value is not None:
            self.numeric_value = numeric_value
        if text_value is not None:
            self.text_value = text_value

    @property
    def sort_order(self):
        """Gets the sort_order of this EdFiSurveyQuestionResponseChoice.  # noqa: E501

        Sort order of this ResponseChoice within the complete list of choices attached to a SurveyQuestion. If sort order doesn't apply, the value of NumericValue or a unique, possibly sequential numeric value.  # noqa: E501

        :return: The sort_order of this EdFiSurveyQuestionResponseChoice.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this EdFiSurveyQuestionResponseChoice.

        Sort order of this ResponseChoice within the complete list of choices attached to a SurveyQuestion. If sort order doesn't apply, the value of NumericValue or a unique, possibly sequential numeric value.  # noqa: E501

        :param sort_order: The sort_order of this EdFiSurveyQuestionResponseChoice.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and sort_order is None:
            raise ValueError("Invalid value for `sort_order`, must not be `None`")  # noqa: E501

        self._sort_order = sort_order

    @property
    def numeric_value(self):
        """Gets the numeric_value of this EdFiSurveyQuestionResponseChoice.  # noqa: E501

        A valid numeric response. If paired with a TextValue, the numeric equivalent of the TextValue.  # noqa: E501

        :return: The numeric_value of this EdFiSurveyQuestionResponseChoice.  # noqa: E501
        :rtype: int
        """
        return self._numeric_value

    @numeric_value.setter
    def numeric_value(self, numeric_value):
        """Sets the numeric_value of this EdFiSurveyQuestionResponseChoice.

        A valid numeric response. If paired with a TextValue, the numeric equivalent of the TextValue.  # noqa: E501

        :param numeric_value: The numeric_value of this EdFiSurveyQuestionResponseChoice.  # noqa: E501
        :type: int
        """

        self._numeric_value = numeric_value

    @property
    def text_value(self):
        """Gets the text_value of this EdFiSurveyQuestionResponseChoice.  # noqa: E501

        A valid text response. If paired with a NumericValue, the text equivalent of the NumericValue.  # noqa: E501

        :return: The text_value of this EdFiSurveyQuestionResponseChoice.  # noqa: E501
        :rtype: str
        """
        return self._text_value

    @text_value.setter
    def text_value(self, text_value):
        """Sets the text_value of this EdFiSurveyQuestionResponseChoice.

        A valid text response. If paired with a NumericValue, the text equivalent of the NumericValue.  # noqa: E501

        :param text_value: The text_value of this EdFiSurveyQuestionResponseChoice.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                text_value is not None and len(text_value) > 255):
            raise ValueError("Invalid value for `text_value`, length must be less than or equal to `255`")  # noqa: E501

        self._text_value = text_value

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
        if issubclass(EdFiSurveyQuestionResponseChoice, dict):
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
        if not isinstance(other, EdFiSurveyQuestionResponseChoice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiSurveyQuestionResponseChoice):
            return True

        return self.to_dict() != other.to_dict()
