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


class EdFiAccountReference(object):
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
        'account_identifier': 'str',
        'education_organization_id': 'int',
        'fiscal_year': 'int',
        'link': 'Link'
    }

    attribute_map = {
        'account_identifier': 'accountIdentifier',
        'education_organization_id': 'educationOrganizationId',
        'fiscal_year': 'fiscalYear',
        'link': 'link'
    }

    def __init__(self, account_identifier=None, education_organization_id=None, fiscal_year=None, link=None, _configuration=None):  # noqa: E501
        """EdFiAccountReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_identifier = None
        self._education_organization_id = None
        self._fiscal_year = None
        self._link = None
        self.discriminator = None

        self.account_identifier = account_identifier
        self.education_organization_id = education_organization_id
        self.fiscal_year = fiscal_year
        if link is not None:
            self.link = link

    @property
    def account_identifier(self):
        """Gets the account_identifier of this EdFiAccountReference.  # noqa: E501

        The alphanumeric string that identifies the account.  # noqa: E501

        :return: The account_identifier of this EdFiAccountReference.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this EdFiAccountReference.

        The alphanumeric string that identifies the account.  # noqa: E501

        :param account_identifier: The account_identifier of this EdFiAccountReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_identifier is None:
            raise ValueError("Invalid value for `account_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                account_identifier is not None and len(account_identifier) > 50):
            raise ValueError("Invalid value for `account_identifier`, length must be less than or equal to `50`")  # noqa: E501

        self._account_identifier = account_identifier

    @property
    def education_organization_id(self):
        """Gets the education_organization_id of this EdFiAccountReference.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The education_organization_id of this EdFiAccountReference.  # noqa: E501
        :rtype: int
        """
        return self._education_organization_id

    @education_organization_id.setter
    def education_organization_id(self, education_organization_id):
        """Sets the education_organization_id of this EdFiAccountReference.

        The identifier assigned to an education organization.  # noqa: E501

        :param education_organization_id: The education_organization_id of this EdFiAccountReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and education_organization_id is None:
            raise ValueError("Invalid value for `education_organization_id`, must not be `None`")  # noqa: E501

        self._education_organization_id = education_organization_id

    @property
    def fiscal_year(self):
        """Gets the fiscal_year of this EdFiAccountReference.  # noqa: E501

        The financial accounting year.  # noqa: E501

        :return: The fiscal_year of this EdFiAccountReference.  # noqa: E501
        :rtype: int
        """
        return self._fiscal_year

    @fiscal_year.setter
    def fiscal_year(self, fiscal_year):
        """Sets the fiscal_year of this EdFiAccountReference.

        The financial accounting year.  # noqa: E501

        :param fiscal_year: The fiscal_year of this EdFiAccountReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and fiscal_year is None:
            raise ValueError("Invalid value for `fiscal_year`, must not be `None`")  # noqa: E501

        self._fiscal_year = fiscal_year

    @property
    def link(self):
        """Gets the link of this EdFiAccountReference.  # noqa: E501


        :return: The link of this EdFiAccountReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiAccountReference.


        :param link: The link of this EdFiAccountReference.  # noqa: E501
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
        if issubclass(EdFiAccountReference, dict):
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
        if not isinstance(other, EdFiAccountReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiAccountReference):
            return True

        return self.to_dict() != other.to_dict()
