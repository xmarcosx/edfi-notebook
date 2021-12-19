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


class TpdmApplicantBackgroundCheck(object):
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
        'background_check_type_descriptor': 'str',
        'background_check_status_descriptor': 'str',
        'background_check_completed_date': 'date',
        'background_check_requested_date': 'date',
        'fingerprint': 'bool'
    }

    attribute_map = {
        'background_check_type_descriptor': 'backgroundCheckTypeDescriptor',
        'background_check_status_descriptor': 'backgroundCheckStatusDescriptor',
        'background_check_completed_date': 'backgroundCheckCompletedDate',
        'background_check_requested_date': 'backgroundCheckRequestedDate',
        'fingerprint': 'fingerprint'
    }

    def __init__(self, background_check_type_descriptor=None, background_check_status_descriptor=None, background_check_completed_date=None, background_check_requested_date=None, fingerprint=None, _configuration=None):  # noqa: E501
        """TpdmApplicantBackgroundCheck - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._background_check_type_descriptor = None
        self._background_check_status_descriptor = None
        self._background_check_completed_date = None
        self._background_check_requested_date = None
        self._fingerprint = None
        self.discriminator = None

        self.background_check_type_descriptor = background_check_type_descriptor
        if background_check_status_descriptor is not None:
            self.background_check_status_descriptor = background_check_status_descriptor
        if background_check_completed_date is not None:
            self.background_check_completed_date = background_check_completed_date
        self.background_check_requested_date = background_check_requested_date
        if fingerprint is not None:
            self.fingerprint = fingerprint

    @property
    def background_check_type_descriptor(self):
        """Gets the background_check_type_descriptor of this TpdmApplicantBackgroundCheck.  # noqa: E501

        The type of background check (e.g., online, criminal, employment).  # noqa: E501

        :return: The background_check_type_descriptor of this TpdmApplicantBackgroundCheck.  # noqa: E501
        :rtype: str
        """
        return self._background_check_type_descriptor

    @background_check_type_descriptor.setter
    def background_check_type_descriptor(self, background_check_type_descriptor):
        """Sets the background_check_type_descriptor of this TpdmApplicantBackgroundCheck.

        The type of background check (e.g., online, criminal, employment).  # noqa: E501

        :param background_check_type_descriptor: The background_check_type_descriptor of this TpdmApplicantBackgroundCheck.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and background_check_type_descriptor is None:
            raise ValueError("Invalid value for `background_check_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                background_check_type_descriptor is not None and len(background_check_type_descriptor) > 306):
            raise ValueError("Invalid value for `background_check_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._background_check_type_descriptor = background_check_type_descriptor

    @property
    def background_check_status_descriptor(self):
        """Gets the background_check_status_descriptor of this TpdmApplicantBackgroundCheck.  # noqa: E501

        The status of the background check (e.g., pending, under investigation, offense(s) found, etc.).  # noqa: E501

        :return: The background_check_status_descriptor of this TpdmApplicantBackgroundCheck.  # noqa: E501
        :rtype: str
        """
        return self._background_check_status_descriptor

    @background_check_status_descriptor.setter
    def background_check_status_descriptor(self, background_check_status_descriptor):
        """Sets the background_check_status_descriptor of this TpdmApplicantBackgroundCheck.

        The status of the background check (e.g., pending, under investigation, offense(s) found, etc.).  # noqa: E501

        :param background_check_status_descriptor: The background_check_status_descriptor of this TpdmApplicantBackgroundCheck.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                background_check_status_descriptor is not None and len(background_check_status_descriptor) > 306):
            raise ValueError("Invalid value for `background_check_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._background_check_status_descriptor = background_check_status_descriptor

    @property
    def background_check_completed_date(self):
        """Gets the background_check_completed_date of this TpdmApplicantBackgroundCheck.  # noqa: E501

        The date the background check was completed.  # noqa: E501

        :return: The background_check_completed_date of this TpdmApplicantBackgroundCheck.  # noqa: E501
        :rtype: date
        """
        return self._background_check_completed_date

    @background_check_completed_date.setter
    def background_check_completed_date(self, background_check_completed_date):
        """Sets the background_check_completed_date of this TpdmApplicantBackgroundCheck.

        The date the background check was completed.  # noqa: E501

        :param background_check_completed_date: The background_check_completed_date of this TpdmApplicantBackgroundCheck.  # noqa: E501
        :type: date
        """

        self._background_check_completed_date = background_check_completed_date

    @property
    def background_check_requested_date(self):
        """Gets the background_check_requested_date of this TpdmApplicantBackgroundCheck.  # noqa: E501

        The date the background check was requested.  # noqa: E501

        :return: The background_check_requested_date of this TpdmApplicantBackgroundCheck.  # noqa: E501
        :rtype: date
        """
        return self._background_check_requested_date

    @background_check_requested_date.setter
    def background_check_requested_date(self, background_check_requested_date):
        """Sets the background_check_requested_date of this TpdmApplicantBackgroundCheck.

        The date the background check was requested.  # noqa: E501

        :param background_check_requested_date: The background_check_requested_date of this TpdmApplicantBackgroundCheck.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and background_check_requested_date is None:
            raise ValueError("Invalid value for `background_check_requested_date`, must not be `None`")  # noqa: E501

        self._background_check_requested_date = background_check_requested_date

    @property
    def fingerprint(self):
        """Gets the fingerprint of this TpdmApplicantBackgroundCheck.  # noqa: E501

        Indicates that a person has or has not completed a fingerprint.  # noqa: E501

        :return: The fingerprint of this TpdmApplicantBackgroundCheck.  # noqa: E501
        :rtype: bool
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this TpdmApplicantBackgroundCheck.

        Indicates that a person has or has not completed a fingerprint.  # noqa: E501

        :param fingerprint: The fingerprint of this TpdmApplicantBackgroundCheck.  # noqa: E501
        :type: bool
        """

        self._fingerprint = fingerprint

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
        if issubclass(TpdmApplicantBackgroundCheck, dict):
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
        if not isinstance(other, TpdmApplicantBackgroundCheck):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmApplicantBackgroundCheck):
            return True

        return self.to_dict() != other.to_dict()