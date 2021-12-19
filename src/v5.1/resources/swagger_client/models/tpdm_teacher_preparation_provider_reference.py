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


class TpdmTeacherPreparationProviderReference(object):
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
        'teacher_preparation_provider_id': 'int',
        'link': 'Link'
    }

    attribute_map = {
        'teacher_preparation_provider_id': 'teacherPreparationProviderId',
        'link': 'link'
    }

    def __init__(self, teacher_preparation_provider_id=None, link=None, _configuration=None):  # noqa: E501
        """TpdmTeacherPreparationProviderReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._teacher_preparation_provider_id = None
        self._link = None
        self.discriminator = None

        self.teacher_preparation_provider_id = teacher_preparation_provider_id
        if link is not None:
            self.link = link

    @property
    def teacher_preparation_provider_id(self):
        """Gets the teacher_preparation_provider_id of this TpdmTeacherPreparationProviderReference.  # noqa: E501

        The unique identification code for the Teacher Preparation Provider  # noqa: E501

        :return: The teacher_preparation_provider_id of this TpdmTeacherPreparationProviderReference.  # noqa: E501
        :rtype: int
        """
        return self._teacher_preparation_provider_id

    @teacher_preparation_provider_id.setter
    def teacher_preparation_provider_id(self, teacher_preparation_provider_id):
        """Sets the teacher_preparation_provider_id of this TpdmTeacherPreparationProviderReference.

        The unique identification code for the Teacher Preparation Provider  # noqa: E501

        :param teacher_preparation_provider_id: The teacher_preparation_provider_id of this TpdmTeacherPreparationProviderReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and teacher_preparation_provider_id is None:
            raise ValueError("Invalid value for `teacher_preparation_provider_id`, must not be `None`")  # noqa: E501

        self._teacher_preparation_provider_id = teacher_preparation_provider_id

    @property
    def link(self):
        """Gets the link of this TpdmTeacherPreparationProviderReference.  # noqa: E501


        :return: The link of this TpdmTeacherPreparationProviderReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TpdmTeacherPreparationProviderReference.


        :param link: The link of this TpdmTeacherPreparationProviderReference.  # noqa: E501
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
        if issubclass(TpdmTeacherPreparationProviderReference, dict):
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
        if not isinstance(other, TpdmTeacherPreparationProviderReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmTeacherPreparationProviderReference):
            return True

        return self.to_dict() != other.to_dict()
