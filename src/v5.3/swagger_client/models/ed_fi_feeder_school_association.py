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


class EdFiFeederSchoolAssociation(object):
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
        'begin_date': 'date',
        'feeder_school_reference': 'EdFiSchoolReference',
        'school_reference': 'EdFiSchoolReference',
        'end_date': 'date',
        'feeder_relationship_description': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'begin_date': 'beginDate',
        'feeder_school_reference': 'feederSchoolReference',
        'school_reference': 'schoolReference',
        'end_date': 'endDate',
        'feeder_relationship_description': 'feederRelationshipDescription',
        'etag': '_etag'
    }

    def __init__(self, id=None, begin_date=None, feeder_school_reference=None, school_reference=None, end_date=None, feeder_relationship_description=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiFeederSchoolAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._begin_date = None
        self._feeder_school_reference = None
        self._school_reference = None
        self._end_date = None
        self._feeder_relationship_description = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.begin_date = begin_date
        self.feeder_school_reference = feeder_school_reference
        self.school_reference = school_reference
        if end_date is not None:
            self.end_date = end_date
        if feeder_relationship_description is not None:
            self.feeder_relationship_description = feeder_relationship_description
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiFeederSchoolAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiFeederSchoolAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiFeederSchoolAssociation.

          # noqa: E501

        :param id: The id of this EdFiFeederSchoolAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiFeederSchoolAssociation.  # noqa: E501

        The month, day, and year of the first day of the feeder school association.  # noqa: E501

        :return: The begin_date of this EdFiFeederSchoolAssociation.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiFeederSchoolAssociation.

        The month, day, and year of the first day of the feeder school association.  # noqa: E501

        :param begin_date: The begin_date of this EdFiFeederSchoolAssociation.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def feeder_school_reference(self):
        """Gets the feeder_school_reference of this EdFiFeederSchoolAssociation.  # noqa: E501


        :return: The feeder_school_reference of this EdFiFeederSchoolAssociation.  # noqa: E501
        :rtype: EdFiSchoolReference
        """
        return self._feeder_school_reference

    @feeder_school_reference.setter
    def feeder_school_reference(self, feeder_school_reference):
        """Sets the feeder_school_reference of this EdFiFeederSchoolAssociation.


        :param feeder_school_reference: The feeder_school_reference of this EdFiFeederSchoolAssociation.  # noqa: E501
        :type: EdFiSchoolReference
        """
        if self._configuration.client_side_validation and feeder_school_reference is None:
            raise ValueError("Invalid value for `feeder_school_reference`, must not be `None`")  # noqa: E501

        self._feeder_school_reference = feeder_school_reference

    @property
    def school_reference(self):
        """Gets the school_reference of this EdFiFeederSchoolAssociation.  # noqa: E501


        :return: The school_reference of this EdFiFeederSchoolAssociation.  # noqa: E501
        :rtype: EdFiSchoolReference
        """
        return self._school_reference

    @school_reference.setter
    def school_reference(self, school_reference):
        """Sets the school_reference of this EdFiFeederSchoolAssociation.


        :param school_reference: The school_reference of this EdFiFeederSchoolAssociation.  # noqa: E501
        :type: EdFiSchoolReference
        """
        if self._configuration.client_side_validation and school_reference is None:
            raise ValueError("Invalid value for `school_reference`, must not be `None`")  # noqa: E501

        self._school_reference = school_reference

    @property
    def end_date(self):
        """Gets the end_date of this EdFiFeederSchoolAssociation.  # noqa: E501

        The month, day, and year of the last day of the feeder school association.  # noqa: E501

        :return: The end_date of this EdFiFeederSchoolAssociation.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EdFiFeederSchoolAssociation.

        The month, day, and year of the last day of the feeder school association.  # noqa: E501

        :param end_date: The end_date of this EdFiFeederSchoolAssociation.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def feeder_relationship_description(self):
        """Gets the feeder_relationship_description of this EdFiFeederSchoolAssociation.  # noqa: E501

        Describes the relationship from the feeder school to the receiving school, for example by program emphasis, such as special education, language immersion, science, or performing art.  # noqa: E501

        :return: The feeder_relationship_description of this EdFiFeederSchoolAssociation.  # noqa: E501
        :rtype: str
        """
        return self._feeder_relationship_description

    @feeder_relationship_description.setter
    def feeder_relationship_description(self, feeder_relationship_description):
        """Sets the feeder_relationship_description of this EdFiFeederSchoolAssociation.

        Describes the relationship from the feeder school to the receiving school, for example by program emphasis, such as special education, language immersion, science, or performing art.  # noqa: E501

        :param feeder_relationship_description: The feeder_relationship_description of this EdFiFeederSchoolAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                feeder_relationship_description is not None and len(feeder_relationship_description) > 1024):
            raise ValueError("Invalid value for `feeder_relationship_description`, length must be less than or equal to `1024`")  # noqa: E501

        self._feeder_relationship_description = feeder_relationship_description

    @property
    def etag(self):
        """Gets the etag of this EdFiFeederSchoolAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiFeederSchoolAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiFeederSchoolAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiFeederSchoolAssociation.  # noqa: E501
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
        if issubclass(EdFiFeederSchoolAssociation, dict):
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
        if not isinstance(other, EdFiFeederSchoolAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiFeederSchoolAssociation):
            return True

        return self.to_dict() != other.to_dict()