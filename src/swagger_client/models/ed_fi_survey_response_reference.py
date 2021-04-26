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


class EdFiSurveyResponseReference(object):
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
        'namespace': 'str',
        'survey_identifier': 'str',
        'survey_response_identifier': 'str',
        'link': 'Link'
    }

    attribute_map = {
        'namespace': 'namespace',
        'survey_identifier': 'surveyIdentifier',
        'survey_response_identifier': 'surveyResponseIdentifier',
        'link': 'link'
    }

    def __init__(self, namespace=None, survey_identifier=None, survey_response_identifier=None, link=None):  # noqa: E501
        """EdFiSurveyResponseReference - a model defined in Swagger"""  # noqa: E501

        self._namespace = None
        self._survey_identifier = None
        self._survey_response_identifier = None
        self._link = None
        self.discriminator = None

        self.namespace = namespace
        self.survey_identifier = survey_identifier
        self.survey_response_identifier = survey_response_identifier
        if link is not None:
            self.link = link

    @property
    def namespace(self):
        """Gets the namespace of this EdFiSurveyResponseReference.  # noqa: E501

        Namespace for the Survey.  # noqa: E501

        :return: The namespace of this EdFiSurveyResponseReference.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this EdFiSurveyResponseReference.

        Namespace for the Survey.  # noqa: E501

        :param namespace: The namespace of this EdFiSurveyResponseReference.  # noqa: E501
        :type: str
        """
        if namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501
        if namespace is not None and len(namespace) > 255:
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `255`")  # noqa: E501

        self._namespace = namespace

    @property
    def survey_identifier(self):
        """Gets the survey_identifier of this EdFiSurveyResponseReference.  # noqa: E501

        The unique survey identifier from the survey tool.  # noqa: E501

        :return: The survey_identifier of this EdFiSurveyResponseReference.  # noqa: E501
        :rtype: str
        """
        return self._survey_identifier

    @survey_identifier.setter
    def survey_identifier(self, survey_identifier):
        """Sets the survey_identifier of this EdFiSurveyResponseReference.

        The unique survey identifier from the survey tool.  # noqa: E501

        :param survey_identifier: The survey_identifier of this EdFiSurveyResponseReference.  # noqa: E501
        :type: str
        """
        if survey_identifier is None:
            raise ValueError("Invalid value for `survey_identifier`, must not be `None`")  # noqa: E501
        if survey_identifier is not None and len(survey_identifier) > 60:
            raise ValueError("Invalid value for `survey_identifier`, length must be less than or equal to `60`")  # noqa: E501

        self._survey_identifier = survey_identifier

    @property
    def survey_response_identifier(self):
        """Gets the survey_response_identifier of this EdFiSurveyResponseReference.  # noqa: E501

        The identifier of the survey typically from the survey application.  # noqa: E501

        :return: The survey_response_identifier of this EdFiSurveyResponseReference.  # noqa: E501
        :rtype: str
        """
        return self._survey_response_identifier

    @survey_response_identifier.setter
    def survey_response_identifier(self, survey_response_identifier):
        """Sets the survey_response_identifier of this EdFiSurveyResponseReference.

        The identifier of the survey typically from the survey application.  # noqa: E501

        :param survey_response_identifier: The survey_response_identifier of this EdFiSurveyResponseReference.  # noqa: E501
        :type: str
        """
        if survey_response_identifier is None:
            raise ValueError("Invalid value for `survey_response_identifier`, must not be `None`")  # noqa: E501
        if survey_response_identifier is not None and len(survey_response_identifier) > 60:
            raise ValueError("Invalid value for `survey_response_identifier`, length must be less than or equal to `60`")  # noqa: E501

        self._survey_response_identifier = survey_response_identifier

    @property
    def link(self):
        """Gets the link of this EdFiSurveyResponseReference.  # noqa: E501


        :return: The link of this EdFiSurveyResponseReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiSurveyResponseReference.


        :param link: The link of this EdFiSurveyResponseReference.  # noqa: E501
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
        if issubclass(EdFiSurveyResponseReference, dict):
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
        if not isinstance(other, EdFiSurveyResponseReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
