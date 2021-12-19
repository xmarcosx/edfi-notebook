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


class TpdmCredentialExtension(object):
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
        'certification_route_descriptor': 'str',
        'credential_status_descriptor': 'str',
        'board_certification_indicator': 'bool',
        'certification_title': 'str',
        'credential_status_date': 'date',
        'certification_reference': 'TpdmCertificationReference',
        'person_reference': 'EdFiPersonReference',
        'student_academic_records': 'list[TpdmCredentialStudentAcademicRecord]'
    }

    attribute_map = {
        'certification_route_descriptor': 'certificationRouteDescriptor',
        'credential_status_descriptor': 'credentialStatusDescriptor',
        'board_certification_indicator': 'boardCertificationIndicator',
        'certification_title': 'certificationTitle',
        'credential_status_date': 'credentialStatusDate',
        'certification_reference': 'certificationReference',
        'person_reference': 'personReference',
        'student_academic_records': 'studentAcademicRecords'
    }

    def __init__(self, certification_route_descriptor=None, credential_status_descriptor=None, board_certification_indicator=None, certification_title=None, credential_status_date=None, certification_reference=None, person_reference=None, student_academic_records=None, _configuration=None):  # noqa: E501
        """TpdmCredentialExtension - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._certification_route_descriptor = None
        self._credential_status_descriptor = None
        self._board_certification_indicator = None
        self._certification_title = None
        self._credential_status_date = None
        self._certification_reference = None
        self._person_reference = None
        self._student_academic_records = None
        self.discriminator = None

        if certification_route_descriptor is not None:
            self.certification_route_descriptor = certification_route_descriptor
        if credential_status_descriptor is not None:
            self.credential_status_descriptor = credential_status_descriptor
        if board_certification_indicator is not None:
            self.board_certification_indicator = board_certification_indicator
        self.certification_title = certification_title
        if credential_status_date is not None:
            self.credential_status_date = credential_status_date
        if certification_reference is not None:
            self.certification_reference = certification_reference
        self.person_reference = person_reference
        if student_academic_records is not None:
            self.student_academic_records = student_academic_records

    @property
    def certification_route_descriptor(self):
        """Gets the certification_route_descriptor of this TpdmCredentialExtension.  # noqa: E501

        The process, program, or pathway used to obtain certification.  # noqa: E501

        :return: The certification_route_descriptor of this TpdmCredentialExtension.  # noqa: E501
        :rtype: str
        """
        return self._certification_route_descriptor

    @certification_route_descriptor.setter
    def certification_route_descriptor(self, certification_route_descriptor):
        """Sets the certification_route_descriptor of this TpdmCredentialExtension.

        The process, program, or pathway used to obtain certification.  # noqa: E501

        :param certification_route_descriptor: The certification_route_descriptor of this TpdmCredentialExtension.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                certification_route_descriptor is not None and len(certification_route_descriptor) > 306):
            raise ValueError("Invalid value for `certification_route_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._certification_route_descriptor = certification_route_descriptor

    @property
    def credential_status_descriptor(self):
        """Gets the credential_status_descriptor of this TpdmCredentialExtension.  # noqa: E501

        The most recent status of the credential (e.g., active, suspended, etc.).  # noqa: E501

        :return: The credential_status_descriptor of this TpdmCredentialExtension.  # noqa: E501
        :rtype: str
        """
        return self._credential_status_descriptor

    @credential_status_descriptor.setter
    def credential_status_descriptor(self, credential_status_descriptor):
        """Sets the credential_status_descriptor of this TpdmCredentialExtension.

        The most recent status of the credential (e.g., active, suspended, etc.).  # noqa: E501

        :param credential_status_descriptor: The credential_status_descriptor of this TpdmCredentialExtension.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                credential_status_descriptor is not None and len(credential_status_descriptor) > 306):
            raise ValueError("Invalid value for `credential_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._credential_status_descriptor = credential_status_descriptor

    @property
    def board_certification_indicator(self):
        """Gets the board_certification_indicator of this TpdmCredentialExtension.  # noqa: E501

        Indicator that the credential was granted under the authority of a national Board Certification.  # noqa: E501

        :return: The board_certification_indicator of this TpdmCredentialExtension.  # noqa: E501
        :rtype: bool
        """
        return self._board_certification_indicator

    @board_certification_indicator.setter
    def board_certification_indicator(self, board_certification_indicator):
        """Sets the board_certification_indicator of this TpdmCredentialExtension.

        Indicator that the credential was granted under the authority of a national Board Certification.  # noqa: E501

        :param board_certification_indicator: The board_certification_indicator of this TpdmCredentialExtension.  # noqa: E501
        :type: bool
        """

        self._board_certification_indicator = board_certification_indicator

    @property
    def certification_title(self):
        """Gets the certification_title of this TpdmCredentialExtension.  # noqa: E501

        The title of the certification obtained by the educator.  # noqa: E501

        :return: The certification_title of this TpdmCredentialExtension.  # noqa: E501
        :rtype: str
        """
        return self._certification_title

    @certification_title.setter
    def certification_title(self, certification_title):
        """Sets the certification_title of this TpdmCredentialExtension.

        The title of the certification obtained by the educator.  # noqa: E501

        :param certification_title: The certification_title of this TpdmCredentialExtension.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and certification_title is None:
            raise ValueError("Invalid value for `certification_title`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                certification_title is not None and len(certification_title) > 64):
            raise ValueError("Invalid value for `certification_title`, length must be less than or equal to `64`")  # noqa: E501

        self._certification_title = certification_title

    @property
    def credential_status_date(self):
        """Gets the credential_status_date of this TpdmCredentialExtension.  # noqa: E501

        The month, day, and year on which the credential status was effective.  # noqa: E501

        :return: The credential_status_date of this TpdmCredentialExtension.  # noqa: E501
        :rtype: date
        """
        return self._credential_status_date

    @credential_status_date.setter
    def credential_status_date(self, credential_status_date):
        """Sets the credential_status_date of this TpdmCredentialExtension.

        The month, day, and year on which the credential status was effective.  # noqa: E501

        :param credential_status_date: The credential_status_date of this TpdmCredentialExtension.  # noqa: E501
        :type: date
        """

        self._credential_status_date = credential_status_date

    @property
    def certification_reference(self):
        """Gets the certification_reference of this TpdmCredentialExtension.  # noqa: E501


        :return: The certification_reference of this TpdmCredentialExtension.  # noqa: E501
        :rtype: TpdmCertificationReference
        """
        return self._certification_reference

    @certification_reference.setter
    def certification_reference(self, certification_reference):
        """Sets the certification_reference of this TpdmCredentialExtension.


        :param certification_reference: The certification_reference of this TpdmCredentialExtension.  # noqa: E501
        :type: TpdmCertificationReference
        """

        self._certification_reference = certification_reference

    @property
    def person_reference(self):
        """Gets the person_reference of this TpdmCredentialExtension.  # noqa: E501


        :return: The person_reference of this TpdmCredentialExtension.  # noqa: E501
        :rtype: EdFiPersonReference
        """
        return self._person_reference

    @person_reference.setter
    def person_reference(self, person_reference):
        """Sets the person_reference of this TpdmCredentialExtension.


        :param person_reference: The person_reference of this TpdmCredentialExtension.  # noqa: E501
        :type: EdFiPersonReference
        """
        if self._configuration.client_side_validation and person_reference is None:
            raise ValueError("Invalid value for `person_reference`, must not be `None`")  # noqa: E501

        self._person_reference = person_reference

    @property
    def student_academic_records(self):
        """Gets the student_academic_records of this TpdmCredentialExtension.  # noqa: E501

        An unordered collection of credentialStudentAcademicRecords. Reference to the person's Student Academic Records for the school(s) with which the Credential is associated.  # noqa: E501

        :return: The student_academic_records of this TpdmCredentialExtension.  # noqa: E501
        :rtype: list[TpdmCredentialStudentAcademicRecord]
        """
        return self._student_academic_records

    @student_academic_records.setter
    def student_academic_records(self, student_academic_records):
        """Sets the student_academic_records of this TpdmCredentialExtension.

        An unordered collection of credentialStudentAcademicRecords. Reference to the person's Student Academic Records for the school(s) with which the Credential is associated.  # noqa: E501

        :param student_academic_records: The student_academic_records of this TpdmCredentialExtension.  # noqa: E501
        :type: list[TpdmCredentialStudentAcademicRecord]
        """

        self._student_academic_records = student_academic_records

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
        if issubclass(TpdmCredentialExtension, dict):
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
        if not isinstance(other, TpdmCredentialExtension):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmCredentialExtension):
            return True

        return self.to_dict() != other.to_dict()
