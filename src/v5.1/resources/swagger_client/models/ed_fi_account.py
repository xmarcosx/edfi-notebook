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


class EdFiAccount(object):
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
        'account_codes': 'list[EdFiAccountAccountCode]',
        'account_identifier': 'str',
        'fiscal_year': 'int',
        'education_organization_reference': 'EdFiEducationOrganizationReference',
        'account_name': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_codes': 'accountCodes',
        'account_identifier': 'accountIdentifier',
        'fiscal_year': 'fiscalYear',
        'education_organization_reference': 'educationOrganizationReference',
        'account_name': 'accountName',
        'etag': '_etag'
    }

    def __init__(self, id=None, account_codes=None, account_identifier=None, fiscal_year=None, education_organization_reference=None, account_name=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._account_codes = None
        self._account_identifier = None
        self._fiscal_year = None
        self._education_organization_reference = None
        self._account_name = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.account_codes = account_codes
        self.account_identifier = account_identifier
        self.fiscal_year = fiscal_year
        self.education_organization_reference = education_organization_reference
        if account_name is not None:
            self.account_name = account_name
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiAccount.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiAccount.

          # noqa: E501

        :param id: The id of this EdFiAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account_codes(self):
        """Gets the account_codes of this EdFiAccount.  # noqa: E501

        An unordered collection of accountAccountCodes. The set of account codes defined for the education accounting system organized by account code type (e.g., fund, function, object) that map to the account.  # noqa: E501

        :return: The account_codes of this EdFiAccount.  # noqa: E501
        :rtype: list[EdFiAccountAccountCode]
        """
        return self._account_codes

    @account_codes.setter
    def account_codes(self, account_codes):
        """Sets the account_codes of this EdFiAccount.

        An unordered collection of accountAccountCodes. The set of account codes defined for the education accounting system organized by account code type (e.g., fund, function, object) that map to the account.  # noqa: E501

        :param account_codes: The account_codes of this EdFiAccount.  # noqa: E501
        :type: list[EdFiAccountAccountCode]
        """
        if self._configuration.client_side_validation and account_codes is None:
            raise ValueError("Invalid value for `account_codes`, must not be `None`")  # noqa: E501

        self._account_codes = account_codes

    @property
    def account_identifier(self):
        """Gets the account_identifier of this EdFiAccount.  # noqa: E501

        The alphanumeric string that identifies the account.  # noqa: E501

        :return: The account_identifier of this EdFiAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this EdFiAccount.

        The alphanumeric string that identifies the account.  # noqa: E501

        :param account_identifier: The account_identifier of this EdFiAccount.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_identifier is None:
            raise ValueError("Invalid value for `account_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                account_identifier is not None and len(account_identifier) > 50):
            raise ValueError("Invalid value for `account_identifier`, length must be less than or equal to `50`")  # noqa: E501

        self._account_identifier = account_identifier

    @property
    def fiscal_year(self):
        """Gets the fiscal_year of this EdFiAccount.  # noqa: E501

        The financial accounting year.  # noqa: E501

        :return: The fiscal_year of this EdFiAccount.  # noqa: E501
        :rtype: int
        """
        return self._fiscal_year

    @fiscal_year.setter
    def fiscal_year(self, fiscal_year):
        """Sets the fiscal_year of this EdFiAccount.

        The financial accounting year.  # noqa: E501

        :param fiscal_year: The fiscal_year of this EdFiAccount.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and fiscal_year is None:
            raise ValueError("Invalid value for `fiscal_year`, must not be `None`")  # noqa: E501

        self._fiscal_year = fiscal_year

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiAccount.  # noqa: E501


        :return: The education_organization_reference of this EdFiAccount.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiAccount.


        :param education_organization_reference: The education_organization_reference of this EdFiAccount.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if self._configuration.client_side_validation and education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def account_name(self):
        """Gets the account_name of this EdFiAccount.  # noqa: E501

        A descriptive name for the account.  # noqa: E501

        :return: The account_name of this EdFiAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this EdFiAccount.

        A descriptive name for the account.  # noqa: E501

        :param account_name: The account_name of this EdFiAccount.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                account_name is not None and len(account_name) > 100):
            raise ValueError("Invalid value for `account_name`, length must be less than or equal to `100`")  # noqa: E501

        self._account_name = account_name

    @property
    def etag(self):
        """Gets the etag of this EdFiAccount.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiAccount.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiAccount.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiAccount.  # noqa: E501
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
        if issubclass(EdFiAccount, dict):
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
        if not isinstance(other, EdFiAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiAccount):
            return True

        return self.to_dict() != other.to_dict()
