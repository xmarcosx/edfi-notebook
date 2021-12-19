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


class TpdmApplicantInternationalAddress(object):
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
        'address_type_descriptor': 'str',
        'country_descriptor': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'address_line3': 'str',
        'address_line4': 'str',
        'begin_date': 'date',
        'end_date': 'date',
        'latitude': 'str',
        'longitude': 'str'
    }

    attribute_map = {
        'address_type_descriptor': 'addressTypeDescriptor',
        'country_descriptor': 'countryDescriptor',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'address_line3': 'addressLine3',
        'address_line4': 'addressLine4',
        'begin_date': 'beginDate',
        'end_date': 'endDate',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, address_type_descriptor=None, country_descriptor=None, address_line1=None, address_line2=None, address_line3=None, address_line4=None, begin_date=None, end_date=None, latitude=None, longitude=None, _configuration=None):  # noqa: E501
        """TpdmApplicantInternationalAddress - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address_type_descriptor = None
        self._country_descriptor = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_line3 = None
        self._address_line4 = None
        self._begin_date = None
        self._end_date = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None

        self.address_type_descriptor = address_type_descriptor
        self.country_descriptor = country_descriptor
        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_line3 is not None:
            self.address_line3 = address_line3
        if address_line4 is not None:
            self.address_line4 = address_line4
        if begin_date is not None:
            self.begin_date = begin_date
        if end_date is not None:
            self.end_date = end_date
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def address_type_descriptor(self):
        """Gets the address_type_descriptor of this TpdmApplicantInternationalAddress.  # noqa: E501

        The type of address listed for an individual or organization. For example:  Physical Address, Mailing Address, Home Address, etc.)  # noqa: E501

        :return: The address_type_descriptor of this TpdmApplicantInternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_type_descriptor

    @address_type_descriptor.setter
    def address_type_descriptor(self, address_type_descriptor):
        """Sets the address_type_descriptor of this TpdmApplicantInternationalAddress.

        The type of address listed for an individual or organization. For example:  Physical Address, Mailing Address, Home Address, etc.)  # noqa: E501

        :param address_type_descriptor: The address_type_descriptor of this TpdmApplicantInternationalAddress.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address_type_descriptor is None:
            raise ValueError("Invalid value for `address_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                address_type_descriptor is not None and len(address_type_descriptor) > 306):
            raise ValueError("Invalid value for `address_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._address_type_descriptor = address_type_descriptor

    @property
    def country_descriptor(self):
        """Gets the country_descriptor of this TpdmApplicantInternationalAddress.  # noqa: E501

        The name of the country. It is strongly recommended that entries use only ISO 3166 2-letter country codes.  # noqa: E501

        :return: The country_descriptor of this TpdmApplicantInternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_descriptor

    @country_descriptor.setter
    def country_descriptor(self, country_descriptor):
        """Sets the country_descriptor of this TpdmApplicantInternationalAddress.

        The name of the country. It is strongly recommended that entries use only ISO 3166 2-letter country codes.  # noqa: E501

        :param country_descriptor: The country_descriptor of this TpdmApplicantInternationalAddress.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and country_descriptor is None:
            raise ValueError("Invalid value for `country_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                country_descriptor is not None and len(country_descriptor) > 306):
            raise ValueError("Invalid value for `country_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._country_descriptor = country_descriptor

    @property
    def address_line1(self):
        """Gets the address_line1 of this TpdmApplicantInternationalAddress.  # noqa: E501

        The first line of the address.  # noqa: E501

        :return: The address_line1 of this TpdmApplicantInternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this TpdmApplicantInternationalAddress.

        The first line of the address.  # noqa: E501

        :param address_line1: The address_line1 of this TpdmApplicantInternationalAddress.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address_line1 is None:
            raise ValueError("Invalid value for `address_line1`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                address_line1 is not None and len(address_line1) > 150):
            raise ValueError("Invalid value for `address_line1`, length must be less than or equal to `150`")  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this TpdmApplicantInternationalAddress.  # noqa: E501

        The second line of the address.  # noqa: E501

        :return: The address_line2 of this TpdmApplicantInternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this TpdmApplicantInternationalAddress.

        The second line of the address.  # noqa: E501

        :param address_line2: The address_line2 of this TpdmApplicantInternationalAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                address_line2 is not None and len(address_line2) > 150):
            raise ValueError("Invalid value for `address_line2`, length must be less than or equal to `150`")  # noqa: E501

        self._address_line2 = address_line2

    @property
    def address_line3(self):
        """Gets the address_line3 of this TpdmApplicantInternationalAddress.  # noqa: E501

        The third line of the address.  # noqa: E501

        :return: The address_line3 of this TpdmApplicantInternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3):
        """Sets the address_line3 of this TpdmApplicantInternationalAddress.

        The third line of the address.  # noqa: E501

        :param address_line3: The address_line3 of this TpdmApplicantInternationalAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                address_line3 is not None and len(address_line3) > 150):
            raise ValueError("Invalid value for `address_line3`, length must be less than or equal to `150`")  # noqa: E501

        self._address_line3 = address_line3

    @property
    def address_line4(self):
        """Gets the address_line4 of this TpdmApplicantInternationalAddress.  # noqa: E501

        The fourth line of the address.  # noqa: E501

        :return: The address_line4 of this TpdmApplicantInternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line4

    @address_line4.setter
    def address_line4(self, address_line4):
        """Sets the address_line4 of this TpdmApplicantInternationalAddress.

        The fourth line of the address.  # noqa: E501

        :param address_line4: The address_line4 of this TpdmApplicantInternationalAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                address_line4 is not None and len(address_line4) > 150):
            raise ValueError("Invalid value for `address_line4`, length must be less than or equal to `150`")  # noqa: E501

        self._address_line4 = address_line4

    @property
    def begin_date(self):
        """Gets the begin_date of this TpdmApplicantInternationalAddress.  # noqa: E501

        The first date the address is valid. For physical addresses, the date the person moved to that address.  # noqa: E501

        :return: The begin_date of this TpdmApplicantInternationalAddress.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this TpdmApplicantInternationalAddress.

        The first date the address is valid. For physical addresses, the date the person moved to that address.  # noqa: E501

        :param begin_date: The begin_date of this TpdmApplicantInternationalAddress.  # noqa: E501
        :type: date
        """

        self._begin_date = begin_date

    @property
    def end_date(self):
        """Gets the end_date of this TpdmApplicantInternationalAddress.  # noqa: E501

        The last date the address is valid. For physical addresses, this would be the date the person moved from that address.  # noqa: E501

        :return: The end_date of this TpdmApplicantInternationalAddress.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TpdmApplicantInternationalAddress.

        The last date the address is valid. For physical addresses, this would be the date the person moved from that address.  # noqa: E501

        :param end_date: The end_date of this TpdmApplicantInternationalAddress.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def latitude(self):
        """Gets the latitude of this TpdmApplicantInternationalAddress.  # noqa: E501

        The geographic latitude of the physical address.  # noqa: E501

        :return: The latitude of this TpdmApplicantInternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this TpdmApplicantInternationalAddress.

        The geographic latitude of the physical address.  # noqa: E501

        :param latitude: The latitude of this TpdmApplicantInternationalAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                latitude is not None and len(latitude) > 20):
            raise ValueError("Invalid value for `latitude`, length must be less than or equal to `20`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this TpdmApplicantInternationalAddress.  # noqa: E501

        The geographic longitude of the physical address.  # noqa: E501

        :return: The longitude of this TpdmApplicantInternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this TpdmApplicantInternationalAddress.

        The geographic longitude of the physical address.  # noqa: E501

        :param longitude: The longitude of this TpdmApplicantInternationalAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                longitude is not None and len(longitude) > 20):
            raise ValueError("Invalid value for `longitude`, length must be less than or equal to `20`")  # noqa: E501

        self._longitude = longitude

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
        if issubclass(TpdmApplicantInternationalAddress, dict):
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
        if not isinstance(other, TpdmApplicantInternationalAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmApplicantInternationalAddress):
            return True

        return self.to_dict() != other.to_dict()
