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


class EdFiGeneralStudentProgramAssociationProgramParticipationStatus(object):
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
        'participation_status_descriptor': 'str',
        'status_begin_date': 'date',
        'designated_by': 'str',
        'status_end_date': 'date'
    }

    attribute_map = {
        'participation_status_descriptor': 'participationStatusDescriptor',
        'status_begin_date': 'statusBeginDate',
        'designated_by': 'designatedBy',
        'status_end_date': 'statusEndDate'
    }

    def __init__(self, participation_status_descriptor=None, status_begin_date=None, designated_by=None, status_end_date=None, _configuration=None):  # noqa: E501
        """EdFiGeneralStudentProgramAssociationProgramParticipationStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._participation_status_descriptor = None
        self._status_begin_date = None
        self._designated_by = None
        self._status_end_date = None
        self.discriminator = None

        self.participation_status_descriptor = participation_status_descriptor
        self.status_begin_date = status_begin_date
        if designated_by is not None:
            self.designated_by = designated_by
        if status_end_date is not None:
            self.status_end_date = status_end_date

    @property
    def participation_status_descriptor(self):
        """Gets the participation_status_descriptor of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501

        The student's program participation status.  # noqa: E501

        :return: The participation_status_descriptor of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501
        :rtype: str
        """
        return self._participation_status_descriptor

    @participation_status_descriptor.setter
    def participation_status_descriptor(self, participation_status_descriptor):
        """Sets the participation_status_descriptor of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.

        The student's program participation status.  # noqa: E501

        :param participation_status_descriptor: The participation_status_descriptor of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and participation_status_descriptor is None:
            raise ValueError("Invalid value for `participation_status_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                participation_status_descriptor is not None and len(participation_status_descriptor) > 306):
            raise ValueError("Invalid value for `participation_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._participation_status_descriptor = participation_status_descriptor

    @property
    def status_begin_date(self):
        """Gets the status_begin_date of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501

        The date the student's program participation status began.  # noqa: E501

        :return: The status_begin_date of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501
        :rtype: date
        """
        return self._status_begin_date

    @status_begin_date.setter
    def status_begin_date(self, status_begin_date):
        """Sets the status_begin_date of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.

        The date the student's program participation status began.  # noqa: E501

        :param status_begin_date: The status_begin_date of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and status_begin_date is None:
            raise ValueError("Invalid value for `status_begin_date`, must not be `None`")  # noqa: E501

        self._status_begin_date = status_begin_date

    @property
    def designated_by(self):
        """Gets the designated_by of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501

        The person, organization, or department that designated the participation status.  # noqa: E501

        :return: The designated_by of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501
        :rtype: str
        """
        return self._designated_by

    @designated_by.setter
    def designated_by(self, designated_by):
        """Sets the designated_by of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.

        The person, organization, or department that designated the participation status.  # noqa: E501

        :param designated_by: The designated_by of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                designated_by is not None and len(designated_by) > 60):
            raise ValueError("Invalid value for `designated_by`, length must be less than or equal to `60`")  # noqa: E501

        self._designated_by = designated_by

    @property
    def status_end_date(self):
        """Gets the status_end_date of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501

        The date the student's program participation status ended.  # noqa: E501

        :return: The status_end_date of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501
        :rtype: date
        """
        return self._status_end_date

    @status_end_date.setter
    def status_end_date(self, status_end_date):
        """Sets the status_end_date of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.

        The date the student's program participation status ended.  # noqa: E501

        :param status_end_date: The status_end_date of this EdFiGeneralStudentProgramAssociationProgramParticipationStatus.  # noqa: E501
        :type: date
        """

        self._status_end_date = status_end_date

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
        if issubclass(EdFiGeneralStudentProgramAssociationProgramParticipationStatus, dict):
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
        if not isinstance(other, EdFiGeneralStudentProgramAssociationProgramParticipationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiGeneralStudentProgramAssociationProgramParticipationStatus):
            return True

        return self.to_dict() != other.to_dict()
