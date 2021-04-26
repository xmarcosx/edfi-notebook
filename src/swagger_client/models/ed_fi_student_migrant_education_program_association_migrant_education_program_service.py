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


class EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService(object):
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
        'migrant_education_program_service_descriptor': 'str',
        'primary_indicator': 'bool',
        'service_begin_date': 'date',
        'service_end_date': 'date'
    }

    attribute_map = {
        'migrant_education_program_service_descriptor': 'migrantEducationProgramServiceDescriptor',
        'primary_indicator': 'primaryIndicator',
        'service_begin_date': 'serviceBeginDate',
        'service_end_date': 'serviceEndDate'
    }

    def __init__(self, migrant_education_program_service_descriptor=None, primary_indicator=None, service_begin_date=None, service_end_date=None):  # noqa: E501
        """EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService - a model defined in Swagger"""  # noqa: E501

        self._migrant_education_program_service_descriptor = None
        self._primary_indicator = None
        self._service_begin_date = None
        self._service_end_date = None
        self.discriminator = None

        self.migrant_education_program_service_descriptor = migrant_education_program_service_descriptor
        if primary_indicator is not None:
            self.primary_indicator = primary_indicator
        if service_begin_date is not None:
            self.service_begin_date = service_begin_date
        if service_end_date is not None:
            self.service_end_date = service_end_date

    @property
    def migrant_education_program_service_descriptor(self):
        """Gets the migrant_education_program_service_descriptor of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501

        Indicates the Service being provided to the student by the Migrant Education Program.  # noqa: E501

        :return: The migrant_education_program_service_descriptor of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501
        :rtype: str
        """
        return self._migrant_education_program_service_descriptor

    @migrant_education_program_service_descriptor.setter
    def migrant_education_program_service_descriptor(self, migrant_education_program_service_descriptor):
        """Sets the migrant_education_program_service_descriptor of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.

        Indicates the Service being provided to the student by the Migrant Education Program.  # noqa: E501

        :param migrant_education_program_service_descriptor: The migrant_education_program_service_descriptor of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501
        :type: str
        """
        if migrant_education_program_service_descriptor is None:
            raise ValueError("Invalid value for `migrant_education_program_service_descriptor`, must not be `None`")  # noqa: E501
        if migrant_education_program_service_descriptor is not None and len(migrant_education_program_service_descriptor) > 306:
            raise ValueError("Invalid value for `migrant_education_program_service_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._migrant_education_program_service_descriptor = migrant_education_program_service_descriptor

    @property
    def primary_indicator(self):
        """Gets the primary_indicator of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501

        True if service is a primary service.  # noqa: E501

        :return: The primary_indicator of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501
        :rtype: bool
        """
        return self._primary_indicator

    @primary_indicator.setter
    def primary_indicator(self, primary_indicator):
        """Sets the primary_indicator of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.

        True if service is a primary service.  # noqa: E501

        :param primary_indicator: The primary_indicator of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501
        :type: bool
        """

        self._primary_indicator = primary_indicator

    @property
    def service_begin_date(self):
        """Gets the service_begin_date of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501

        First date the Student was in this option for the current school year.  # noqa: E501

        :return: The service_begin_date of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501
        :rtype: date
        """
        return self._service_begin_date

    @service_begin_date.setter
    def service_begin_date(self, service_begin_date):
        """Sets the service_begin_date of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.

        First date the Student was in this option for the current school year.  # noqa: E501

        :param service_begin_date: The service_begin_date of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501
        :type: date
        """

        self._service_begin_date = service_begin_date

    @property
    def service_end_date(self):
        """Gets the service_end_date of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501

        Last date the Student was in this option for the current school year.  # noqa: E501

        :return: The service_end_date of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501
        :rtype: date
        """
        return self._service_end_date

    @service_end_date.setter
    def service_end_date(self, service_end_date):
        """Sets the service_end_date of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.

        Last date the Student was in this option for the current school year.  # noqa: E501

        :param service_end_date: The service_end_date of this EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService.  # noqa: E501
        :type: date
        """

        self._service_end_date = service_end_date

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
        if issubclass(EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService, dict):
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
        if not isinstance(other, EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
