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


class TpdmProfessionalDevelopmentEventAttendance(object):
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
        'attendance_date': 'date',
        'person_reference': 'EdFiPersonReference',
        'professional_development_event_reference': 'TpdmProfessionalDevelopmentEventReference',
        'attendance_event_category_descriptor': 'str',
        'attendance_event_reason': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'attendance_date': 'attendanceDate',
        'person_reference': 'personReference',
        'professional_development_event_reference': 'professionalDevelopmentEventReference',
        'attendance_event_category_descriptor': 'attendanceEventCategoryDescriptor',
        'attendance_event_reason': 'attendanceEventReason',
        'etag': '_etag'
    }

    def __init__(self, id=None, attendance_date=None, person_reference=None, professional_development_event_reference=None, attendance_event_category_descriptor=None, attendance_event_reason=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmProfessionalDevelopmentEventAttendance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._attendance_date = None
        self._person_reference = None
        self._professional_development_event_reference = None
        self._attendance_event_category_descriptor = None
        self._attendance_event_reason = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.attendance_date = attendance_date
        self.person_reference = person_reference
        self.professional_development_event_reference = professional_development_event_reference
        self.attendance_event_category_descriptor = attendance_event_category_descriptor
        if attendance_event_reason is not None:
            self.attendance_event_reason = attendance_event_reason
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmProfessionalDevelopmentEventAttendance.

          # noqa: E501

        :param id: The id of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def attendance_date(self):
        """Gets the attendance_date of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501

        Date for this attendance event.  # noqa: E501

        :return: The attendance_date of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :rtype: date
        """
        return self._attendance_date

    @attendance_date.setter
    def attendance_date(self, attendance_date):
        """Sets the attendance_date of this TpdmProfessionalDevelopmentEventAttendance.

        Date for this attendance event.  # noqa: E501

        :param attendance_date: The attendance_date of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and attendance_date is None:
            raise ValueError("Invalid value for `attendance_date`, must not be `None`")  # noqa: E501

        self._attendance_date = attendance_date

    @property
    def person_reference(self):
        """Gets the person_reference of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501


        :return: The person_reference of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :rtype: EdFiPersonReference
        """
        return self._person_reference

    @person_reference.setter
    def person_reference(self, person_reference):
        """Sets the person_reference of this TpdmProfessionalDevelopmentEventAttendance.


        :param person_reference: The person_reference of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :type: EdFiPersonReference
        """
        if self._configuration.client_side_validation and person_reference is None:
            raise ValueError("Invalid value for `person_reference`, must not be `None`")  # noqa: E501

        self._person_reference = person_reference

    @property
    def professional_development_event_reference(self):
        """Gets the professional_development_event_reference of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501


        :return: The professional_development_event_reference of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :rtype: TpdmProfessionalDevelopmentEventReference
        """
        return self._professional_development_event_reference

    @professional_development_event_reference.setter
    def professional_development_event_reference(self, professional_development_event_reference):
        """Sets the professional_development_event_reference of this TpdmProfessionalDevelopmentEventAttendance.


        :param professional_development_event_reference: The professional_development_event_reference of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :type: TpdmProfessionalDevelopmentEventReference
        """
        if self._configuration.client_side_validation and professional_development_event_reference is None:
            raise ValueError("Invalid value for `professional_development_event_reference`, must not be `None`")  # noqa: E501

        self._professional_development_event_reference = professional_development_event_reference

    @property
    def attendance_event_category_descriptor(self):
        """Gets the attendance_event_category_descriptor of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501

        A code describing the attendance event, for example:       Present       Unexcused absence       Excused absence       Tardy.  # noqa: E501

        :return: The attendance_event_category_descriptor of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :rtype: str
        """
        return self._attendance_event_category_descriptor

    @attendance_event_category_descriptor.setter
    def attendance_event_category_descriptor(self, attendance_event_category_descriptor):
        """Sets the attendance_event_category_descriptor of this TpdmProfessionalDevelopmentEventAttendance.

        A code describing the attendance event, for example:       Present       Unexcused absence       Excused absence       Tardy.  # noqa: E501

        :param attendance_event_category_descriptor: The attendance_event_category_descriptor of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and attendance_event_category_descriptor is None:
            raise ValueError("Invalid value for `attendance_event_category_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                attendance_event_category_descriptor is not None and len(attendance_event_category_descriptor) > 306):
            raise ValueError("Invalid value for `attendance_event_category_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._attendance_event_category_descriptor = attendance_event_category_descriptor

    @property
    def attendance_event_reason(self):
        """Gets the attendance_event_reason of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501

        The reported reason for a teacher candidate's absence.  # noqa: E501

        :return: The attendance_event_reason of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :rtype: str
        """
        return self._attendance_event_reason

    @attendance_event_reason.setter
    def attendance_event_reason(self, attendance_event_reason):
        """Sets the attendance_event_reason of this TpdmProfessionalDevelopmentEventAttendance.

        The reported reason for a teacher candidate's absence.  # noqa: E501

        :param attendance_event_reason: The attendance_event_reason of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                attendance_event_reason is not None and len(attendance_event_reason) > 255):
            raise ValueError("Invalid value for `attendance_event_reason`, length must be less than or equal to `255`")  # noqa: E501

        self._attendance_event_reason = attendance_event_reason

    @property
    def etag(self):
        """Gets the etag of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmProfessionalDevelopmentEventAttendance.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmProfessionalDevelopmentEventAttendance.  # noqa: E501
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
        if issubclass(TpdmProfessionalDevelopmentEventAttendance, dict):
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
        if not isinstance(other, TpdmProfessionalDevelopmentEventAttendance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmProfessionalDevelopmentEventAttendance):
            return True

        return self.to_dict() != other.to_dict()