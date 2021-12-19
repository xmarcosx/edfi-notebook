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


class EdFiSchoolYearType(object):
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
        'school_year': 'int',
        'current_school_year': 'bool',
        'school_year_description': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'school_year': 'schoolYear',
        'current_school_year': 'currentSchoolYear',
        'school_year_description': 'schoolYearDescription',
        'etag': '_etag'
    }

    def __init__(self, id=None, school_year=None, current_school_year=None, school_year_description=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiSchoolYearType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._school_year = None
        self._current_school_year = None
        self._school_year_description = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.school_year = school_year
        self.current_school_year = current_school_year
        self.school_year_description = school_year_description
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiSchoolYearType.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiSchoolYearType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiSchoolYearType.

          # noqa: E501

        :param id: The id of this EdFiSchoolYearType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def school_year(self):
        """Gets the school_year of this EdFiSchoolYearType.  # noqa: E501

        Key for School Year  # noqa: E501

        :return: The school_year of this EdFiSchoolYearType.  # noqa: E501
        :rtype: int
        """
        return self._school_year

    @school_year.setter
    def school_year(self, school_year):
        """Sets the school_year of this EdFiSchoolYearType.

        Key for School Year  # noqa: E501

        :param school_year: The school_year of this EdFiSchoolYearType.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and school_year is None:
            raise ValueError("Invalid value for `school_year`, must not be `None`")  # noqa: E501

        self._school_year = school_year

    @property
    def current_school_year(self):
        """Gets the current_school_year of this EdFiSchoolYearType.  # noqa: E501

        The code for the current school year.  # noqa: E501

        :return: The current_school_year of this EdFiSchoolYearType.  # noqa: E501
        :rtype: bool
        """
        return self._current_school_year

    @current_school_year.setter
    def current_school_year(self, current_school_year):
        """Sets the current_school_year of this EdFiSchoolYearType.

        The code for the current school year.  # noqa: E501

        :param current_school_year: The current_school_year of this EdFiSchoolYearType.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and current_school_year is None:
            raise ValueError("Invalid value for `current_school_year`, must not be `None`")  # noqa: E501

        self._current_school_year = current_school_year

    @property
    def school_year_description(self):
        """Gets the school_year_description of this EdFiSchoolYearType.  # noqa: E501

        The description for the SchoolYear type.  # noqa: E501

        :return: The school_year_description of this EdFiSchoolYearType.  # noqa: E501
        :rtype: str
        """
        return self._school_year_description

    @school_year_description.setter
    def school_year_description(self, school_year_description):
        """Sets the school_year_description of this EdFiSchoolYearType.

        The description for the SchoolYear type.  # noqa: E501

        :param school_year_description: The school_year_description of this EdFiSchoolYearType.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and school_year_description is None:
            raise ValueError("Invalid value for `school_year_description`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                school_year_description is not None and len(school_year_description) > 50):
            raise ValueError("Invalid value for `school_year_description`, length must be less than or equal to `50`")  # noqa: E501

        self._school_year_description = school_year_description

    @property
    def etag(self):
        """Gets the etag of this EdFiSchoolYearType.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiSchoolYearType.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiSchoolYearType.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiSchoolYearType.  # noqa: E501
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
        if issubclass(EdFiSchoolYearType, dict):
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
        if not isinstance(other, EdFiSchoolYearType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiSchoolYearType):
            return True

        return self.to_dict() != other.to_dict()
