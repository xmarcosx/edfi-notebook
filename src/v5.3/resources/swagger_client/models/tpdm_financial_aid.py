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


class TpdmFinancialAid(object):
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
        'aid_type_descriptor': 'str',
        'begin_date': 'date',
        'student_reference': 'EdFiStudentReference',
        'aid_amount': 'float',
        'aid_condition_description': 'str',
        'end_date': 'date',
        'pell_grant_recipient': 'bool',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'aid_type_descriptor': 'aidTypeDescriptor',
        'begin_date': 'beginDate',
        'student_reference': 'studentReference',
        'aid_amount': 'aidAmount',
        'aid_condition_description': 'aidConditionDescription',
        'end_date': 'endDate',
        'pell_grant_recipient': 'pellGrantRecipient',
        'etag': '_etag'
    }

    def __init__(self, id=None, aid_type_descriptor=None, begin_date=None, student_reference=None, aid_amount=None, aid_condition_description=None, end_date=None, pell_grant_recipient=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmFinancialAid - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._aid_type_descriptor = None
        self._begin_date = None
        self._student_reference = None
        self._aid_amount = None
        self._aid_condition_description = None
        self._end_date = None
        self._pell_grant_recipient = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.aid_type_descriptor = aid_type_descriptor
        self.begin_date = begin_date
        self.student_reference = student_reference
        if aid_amount is not None:
            self.aid_amount = aid_amount
        if aid_condition_description is not None:
            self.aid_condition_description = aid_condition_description
        if end_date is not None:
            self.end_date = end_date
        if pell_grant_recipient is not None:
            self.pell_grant_recipient = pell_grant_recipient
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmFinancialAid.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmFinancialAid.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmFinancialAid.

          # noqa: E501

        :param id: The id of this TpdmFinancialAid.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def aid_type_descriptor(self):
        """Gets the aid_type_descriptor of this TpdmFinancialAid.  # noqa: E501

        The classification of financial aid awarded to a person for the academic term/year.  # noqa: E501

        :return: The aid_type_descriptor of this TpdmFinancialAid.  # noqa: E501
        :rtype: str
        """
        return self._aid_type_descriptor

    @aid_type_descriptor.setter
    def aid_type_descriptor(self, aid_type_descriptor):
        """Sets the aid_type_descriptor of this TpdmFinancialAid.

        The classification of financial aid awarded to a person for the academic term/year.  # noqa: E501

        :param aid_type_descriptor: The aid_type_descriptor of this TpdmFinancialAid.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and aid_type_descriptor is None:
            raise ValueError("Invalid value for `aid_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                aid_type_descriptor is not None and len(aid_type_descriptor) > 306):
            raise ValueError("Invalid value for `aid_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._aid_type_descriptor = aid_type_descriptor

    @property
    def begin_date(self):
        """Gets the begin_date of this TpdmFinancialAid.  # noqa: E501

        The date the award was designated.  # noqa: E501

        :return: The begin_date of this TpdmFinancialAid.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this TpdmFinancialAid.

        The date the award was designated.  # noqa: E501

        :param begin_date: The begin_date of this TpdmFinancialAid.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def student_reference(self):
        """Gets the student_reference of this TpdmFinancialAid.  # noqa: E501


        :return: The student_reference of this TpdmFinancialAid.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this TpdmFinancialAid.


        :param student_reference: The student_reference of this TpdmFinancialAid.  # noqa: E501
        :type: EdFiStudentReference
        """
        if self._configuration.client_side_validation and student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def aid_amount(self):
        """Gets the aid_amount of this TpdmFinancialAid.  # noqa: E501

        The amount of financial aid awarded to a person for the term/year.  # noqa: E501

        :return: The aid_amount of this TpdmFinancialAid.  # noqa: E501
        :rtype: float
        """
        return self._aid_amount

    @aid_amount.setter
    def aid_amount(self, aid_amount):
        """Sets the aid_amount of this TpdmFinancialAid.

        The amount of financial aid awarded to a person for the term/year.  # noqa: E501

        :param aid_amount: The aid_amount of this TpdmFinancialAid.  # noqa: E501
        :type: float
        """

        self._aid_amount = aid_amount

    @property
    def aid_condition_description(self):
        """Gets the aid_condition_description of this TpdmFinancialAid.  # noqa: E501

        The description of the condition (e.g., placement in a high need school) under which the aid was given.  # noqa: E501

        :return: The aid_condition_description of this TpdmFinancialAid.  # noqa: E501
        :rtype: str
        """
        return self._aid_condition_description

    @aid_condition_description.setter
    def aid_condition_description(self, aid_condition_description):
        """Sets the aid_condition_description of this TpdmFinancialAid.

        The description of the condition (e.g., placement in a high need school) under which the aid was given.  # noqa: E501

        :param aid_condition_description: The aid_condition_description of this TpdmFinancialAid.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                aid_condition_description is not None and len(aid_condition_description) > 1024):
            raise ValueError("Invalid value for `aid_condition_description`, length must be less than or equal to `1024`")  # noqa: E501

        self._aid_condition_description = aid_condition_description

    @property
    def end_date(self):
        """Gets the end_date of this TpdmFinancialAid.  # noqa: E501

        The date the award was removed.  # noqa: E501

        :return: The end_date of this TpdmFinancialAid.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TpdmFinancialAid.

        The date the award was removed.  # noqa: E501

        :param end_date: The end_date of this TpdmFinancialAid.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def pell_grant_recipient(self):
        """Gets the pell_grant_recipient of this TpdmFinancialAid.  # noqa: E501

        Indicates a person who receives Pell Grant aid.  # noqa: E501

        :return: The pell_grant_recipient of this TpdmFinancialAid.  # noqa: E501
        :rtype: bool
        """
        return self._pell_grant_recipient

    @pell_grant_recipient.setter
    def pell_grant_recipient(self, pell_grant_recipient):
        """Sets the pell_grant_recipient of this TpdmFinancialAid.

        Indicates a person who receives Pell Grant aid.  # noqa: E501

        :param pell_grant_recipient: The pell_grant_recipient of this TpdmFinancialAid.  # noqa: E501
        :type: bool
        """

        self._pell_grant_recipient = pell_grant_recipient

    @property
    def etag(self):
        """Gets the etag of this TpdmFinancialAid.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmFinancialAid.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmFinancialAid.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmFinancialAid.  # noqa: E501
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
        if issubclass(TpdmFinancialAid, dict):
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
        if not isinstance(other, TpdmFinancialAid):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmFinancialAid):
            return True

        return self.to_dict() != other.to_dict()
