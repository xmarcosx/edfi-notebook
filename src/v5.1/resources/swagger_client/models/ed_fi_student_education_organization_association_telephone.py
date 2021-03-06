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


class EdFiStudentEducationOrganizationAssociationTelephone(object):
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
        'telephone_number_type_descriptor': 'str',
        'telephone_number': 'str',
        'do_not_publish_indicator': 'bool',
        'order_of_priority': 'int',
        'text_message_capability_indicator': 'bool'
    }

    attribute_map = {
        'telephone_number_type_descriptor': 'telephoneNumberTypeDescriptor',
        'telephone_number': 'telephoneNumber',
        'do_not_publish_indicator': 'doNotPublishIndicator',
        'order_of_priority': 'orderOfPriority',
        'text_message_capability_indicator': 'textMessageCapabilityIndicator'
    }

    def __init__(self, telephone_number_type_descriptor=None, telephone_number=None, do_not_publish_indicator=None, order_of_priority=None, text_message_capability_indicator=None, _configuration=None):  # noqa: E501
        """EdFiStudentEducationOrganizationAssociationTelephone - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._telephone_number_type_descriptor = None
        self._telephone_number = None
        self._do_not_publish_indicator = None
        self._order_of_priority = None
        self._text_message_capability_indicator = None
        self.discriminator = None

        self.telephone_number_type_descriptor = telephone_number_type_descriptor
        self.telephone_number = telephone_number
        if do_not_publish_indicator is not None:
            self.do_not_publish_indicator = do_not_publish_indicator
        if order_of_priority is not None:
            self.order_of_priority = order_of_priority
        if text_message_capability_indicator is not None:
            self.text_message_capability_indicator = text_message_capability_indicator

    @property
    def telephone_number_type_descriptor(self):
        """Gets the telephone_number_type_descriptor of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501

        The type of communication number listed for an individual or organization.  # noqa: E501

        :return: The telephone_number_type_descriptor of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501
        :rtype: str
        """
        return self._telephone_number_type_descriptor

    @telephone_number_type_descriptor.setter
    def telephone_number_type_descriptor(self, telephone_number_type_descriptor):
        """Sets the telephone_number_type_descriptor of this EdFiStudentEducationOrganizationAssociationTelephone.

        The type of communication number listed for an individual or organization.  # noqa: E501

        :param telephone_number_type_descriptor: The telephone_number_type_descriptor of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and telephone_number_type_descriptor is None:
            raise ValueError("Invalid value for `telephone_number_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                telephone_number_type_descriptor is not None and len(telephone_number_type_descriptor) > 306):
            raise ValueError("Invalid value for `telephone_number_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._telephone_number_type_descriptor = telephone_number_type_descriptor

    @property
    def telephone_number(self):
        """Gets the telephone_number of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501

        The telephone number including the area code, and extension, if applicable.  # noqa: E501

        :return: The telephone_number of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501
        :rtype: str
        """
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, telephone_number):
        """Sets the telephone_number of this EdFiStudentEducationOrganizationAssociationTelephone.

        The telephone number including the area code, and extension, if applicable.  # noqa: E501

        :param telephone_number: The telephone_number of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and telephone_number is None:
            raise ValueError("Invalid value for `telephone_number`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                telephone_number is not None and len(telephone_number) > 24):
            raise ValueError("Invalid value for `telephone_number`, length must be less than or equal to `24`")  # noqa: E501

        self._telephone_number = telephone_number

    @property
    def do_not_publish_indicator(self):
        """Gets the do_not_publish_indicator of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501

        An indication that the telephone number should not be published.  # noqa: E501

        :return: The do_not_publish_indicator of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501
        :rtype: bool
        """
        return self._do_not_publish_indicator

    @do_not_publish_indicator.setter
    def do_not_publish_indicator(self, do_not_publish_indicator):
        """Sets the do_not_publish_indicator of this EdFiStudentEducationOrganizationAssociationTelephone.

        An indication that the telephone number should not be published.  # noqa: E501

        :param do_not_publish_indicator: The do_not_publish_indicator of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501
        :type: bool
        """

        self._do_not_publish_indicator = do_not_publish_indicator

    @property
    def order_of_priority(self):
        """Gets the order_of_priority of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501

        The order of priority assigned to telephone numbers to define which number to attempt first, second, etc.  # noqa: E501

        :return: The order_of_priority of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501
        :rtype: int
        """
        return self._order_of_priority

    @order_of_priority.setter
    def order_of_priority(self, order_of_priority):
        """Sets the order_of_priority of this EdFiStudentEducationOrganizationAssociationTelephone.

        The order of priority assigned to telephone numbers to define which number to attempt first, second, etc.  # noqa: E501

        :param order_of_priority: The order_of_priority of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501
        :type: int
        """

        self._order_of_priority = order_of_priority

    @property
    def text_message_capability_indicator(self):
        """Gets the text_message_capability_indicator of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501

        An indication that the telephone number is technically capable of sending and receiving Short Message Service (SMS) text messages.  # noqa: E501

        :return: The text_message_capability_indicator of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501
        :rtype: bool
        """
        return self._text_message_capability_indicator

    @text_message_capability_indicator.setter
    def text_message_capability_indicator(self, text_message_capability_indicator):
        """Sets the text_message_capability_indicator of this EdFiStudentEducationOrganizationAssociationTelephone.

        An indication that the telephone number is technically capable of sending and receiving Short Message Service (SMS) text messages.  # noqa: E501

        :param text_message_capability_indicator: The text_message_capability_indicator of this EdFiStudentEducationOrganizationAssociationTelephone.  # noqa: E501
        :type: bool
        """

        self._text_message_capability_indicator = text_message_capability_indicator

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
        if issubclass(EdFiStudentEducationOrganizationAssociationTelephone, dict):
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
        if not isinstance(other, EdFiStudentEducationOrganizationAssociationTelephone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentEducationOrganizationAssociationTelephone):
            return True

        return self.to_dict() != other.to_dict()
