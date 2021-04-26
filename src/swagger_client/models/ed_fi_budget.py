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


class EdFiBudget(object):
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
        'as_of_date': 'date',
        'account_reference': 'EdFiAccountReference',
        'amount': 'float',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'as_of_date': 'asOfDate',
        'account_reference': 'accountReference',
        'amount': 'amount',
        'etag': '_etag'
    }

    def __init__(self, id=None, as_of_date=None, account_reference=None, amount=None, etag=None):  # noqa: E501
        """EdFiBudget - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._as_of_date = None
        self._account_reference = None
        self._amount = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.as_of_date = as_of_date
        self.account_reference = account_reference
        self.amount = amount
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiBudget.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiBudget.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiBudget.

          # noqa: E501

        :param id: The id of this EdFiBudget.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def as_of_date(self):
        """Gets the as_of_date of this EdFiBudget.  # noqa: E501

        The date of the reported budget element.  # noqa: E501

        :return: The as_of_date of this EdFiBudget.  # noqa: E501
        :rtype: date
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this EdFiBudget.

        The date of the reported budget element.  # noqa: E501

        :param as_of_date: The as_of_date of this EdFiBudget.  # noqa: E501
        :type: date
        """
        if as_of_date is None:
            raise ValueError("Invalid value for `as_of_date`, must not be `None`")  # noqa: E501

        self._as_of_date = as_of_date

    @property
    def account_reference(self):
        """Gets the account_reference of this EdFiBudget.  # noqa: E501


        :return: The account_reference of this EdFiBudget.  # noqa: E501
        :rtype: EdFiAccountReference
        """
        return self._account_reference

    @account_reference.setter
    def account_reference(self, account_reference):
        """Sets the account_reference of this EdFiBudget.


        :param account_reference: The account_reference of this EdFiBudget.  # noqa: E501
        :type: EdFiAccountReference
        """
        if account_reference is None:
            raise ValueError("Invalid value for `account_reference`, must not be `None`")  # noqa: E501

        self._account_reference = account_reference

    @property
    def amount(self):
        """Gets the amount of this EdFiBudget.  # noqa: E501

        Amount budgeted for the account for this fiscal year.  # noqa: E501

        :return: The amount of this EdFiBudget.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EdFiBudget.

        Amount budgeted for the account for this fiscal year.  # noqa: E501

        :param amount: The amount of this EdFiBudget.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def etag(self):
        """Gets the etag of this EdFiBudget.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiBudget.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiBudget.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiBudget.  # noqa: E501
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
        if issubclass(EdFiBudget, dict):
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
        if not isinstance(other, EdFiBudget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
