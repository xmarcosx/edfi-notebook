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


class EdFiStudentSchoolAttendanceEvent(object):
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
        'attendance_event_category_descriptor': 'str',
        'event_date': 'date',
        'school_reference': 'EdFiSchoolReference',
        'session_reference': 'EdFiSessionReference',
        'student_reference': 'EdFiStudentReference',
        'arrival_time': 'str',
        'attendance_event_reason': 'str',
        'departure_time': 'str',
        'educational_environment_descriptor': 'str',
        'event_duration': 'float',
        'school_attendance_duration': 'int',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'attendance_event_category_descriptor': 'attendanceEventCategoryDescriptor',
        'event_date': 'eventDate',
        'school_reference': 'schoolReference',
        'session_reference': 'sessionReference',
        'student_reference': 'studentReference',
        'arrival_time': 'arrivalTime',
        'attendance_event_reason': 'attendanceEventReason',
        'departure_time': 'departureTime',
        'educational_environment_descriptor': 'educationalEnvironmentDescriptor',
        'event_duration': 'eventDuration',
        'school_attendance_duration': 'schoolAttendanceDuration',
        'etag': '_etag'
    }

    def __init__(self, id=None, attendance_event_category_descriptor=None, event_date=None, school_reference=None, session_reference=None, student_reference=None, arrival_time=None, attendance_event_reason=None, departure_time=None, educational_environment_descriptor=None, event_duration=None, school_attendance_duration=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiStudentSchoolAttendanceEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._attendance_event_category_descriptor = None
        self._event_date = None
        self._school_reference = None
        self._session_reference = None
        self._student_reference = None
        self._arrival_time = None
        self._attendance_event_reason = None
        self._departure_time = None
        self._educational_environment_descriptor = None
        self._event_duration = None
        self._school_attendance_duration = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.attendance_event_category_descriptor = attendance_event_category_descriptor
        self.event_date = event_date
        self.school_reference = school_reference
        self.session_reference = session_reference
        self.student_reference = student_reference
        if arrival_time is not None:
            self.arrival_time = arrival_time
        if attendance_event_reason is not None:
            self.attendance_event_reason = attendance_event_reason
        if departure_time is not None:
            self.departure_time = departure_time
        if educational_environment_descriptor is not None:
            self.educational_environment_descriptor = educational_environment_descriptor
        if event_duration is not None:
            self.event_duration = event_duration
        if school_attendance_duration is not None:
            self.school_attendance_duration = school_attendance_duration
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentSchoolAttendanceEvent.

          # noqa: E501

        :param id: The id of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def attendance_event_category_descriptor(self):
        """Gets the attendance_event_category_descriptor of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501

        A code describing the attendance event, for example:         Present         Unexcused absence         Excused absence         Tardy.  # noqa: E501

        :return: The attendance_event_category_descriptor of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: str
        """
        return self._attendance_event_category_descriptor

    @attendance_event_category_descriptor.setter
    def attendance_event_category_descriptor(self, attendance_event_category_descriptor):
        """Sets the attendance_event_category_descriptor of this EdFiStudentSchoolAttendanceEvent.

        A code describing the attendance event, for example:         Present         Unexcused absence         Excused absence         Tardy.  # noqa: E501

        :param attendance_event_category_descriptor: The attendance_event_category_descriptor of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and attendance_event_category_descriptor is None:
            raise ValueError("Invalid value for `attendance_event_category_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                attendance_event_category_descriptor is not None and len(attendance_event_category_descriptor) > 306):
            raise ValueError("Invalid value for `attendance_event_category_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._attendance_event_category_descriptor = attendance_event_category_descriptor

    @property
    def event_date(self):
        """Gets the event_date of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501

        Date for this attendance event.  # noqa: E501

        :return: The event_date of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: date
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this EdFiStudentSchoolAttendanceEvent.

        Date for this attendance event.  # noqa: E501

        :param event_date: The event_date of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and event_date is None:
            raise ValueError("Invalid value for `event_date`, must not be `None`")  # noqa: E501

        self._event_date = event_date

    @property
    def school_reference(self):
        """Gets the school_reference of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501


        :return: The school_reference of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: EdFiSchoolReference
        """
        return self._school_reference

    @school_reference.setter
    def school_reference(self, school_reference):
        """Sets the school_reference of this EdFiStudentSchoolAttendanceEvent.


        :param school_reference: The school_reference of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: EdFiSchoolReference
        """
        if self._configuration.client_side_validation and school_reference is None:
            raise ValueError("Invalid value for `school_reference`, must not be `None`")  # noqa: E501

        self._school_reference = school_reference

    @property
    def session_reference(self):
        """Gets the session_reference of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501


        :return: The session_reference of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: EdFiSessionReference
        """
        return self._session_reference

    @session_reference.setter
    def session_reference(self, session_reference):
        """Sets the session_reference of this EdFiStudentSchoolAttendanceEvent.


        :param session_reference: The session_reference of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: EdFiSessionReference
        """
        if self._configuration.client_side_validation and session_reference is None:
            raise ValueError("Invalid value for `session_reference`, must not be `None`")  # noqa: E501

        self._session_reference = session_reference

    @property
    def student_reference(self):
        """Gets the student_reference of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501


        :return: The student_reference of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this EdFiStudentSchoolAttendanceEvent.


        :param student_reference: The student_reference of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: EdFiStudentReference
        """
        if self._configuration.client_side_validation and student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def arrival_time(self):
        """Gets the arrival_time of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501

        The time of day the student arrived for the attendance event in ISO 8601 format.  # noqa: E501

        :return: The arrival_time of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: str
        """
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, arrival_time):
        """Sets the arrival_time of this EdFiStudentSchoolAttendanceEvent.

        The time of day the student arrived for the attendance event in ISO 8601 format.  # noqa: E501

        :param arrival_time: The arrival_time of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: str
        """

        self._arrival_time = arrival_time

    @property
    def attendance_event_reason(self):
        """Gets the attendance_event_reason of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501

        The reported reason for a student's absence.  # noqa: E501

        :return: The attendance_event_reason of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: str
        """
        return self._attendance_event_reason

    @attendance_event_reason.setter
    def attendance_event_reason(self, attendance_event_reason):
        """Sets the attendance_event_reason of this EdFiStudentSchoolAttendanceEvent.

        The reported reason for a student's absence.  # noqa: E501

        :param attendance_event_reason: The attendance_event_reason of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                attendance_event_reason is not None and len(attendance_event_reason) > 255):
            raise ValueError("Invalid value for `attendance_event_reason`, length must be less than or equal to `255`")  # noqa: E501

        self._attendance_event_reason = attendance_event_reason

    @property
    def departure_time(self):
        """Gets the departure_time of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501

        The time of day the student departed for the attendance event in ISO 8601 format.  # noqa: E501

        :return: The departure_time of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: str
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        """Sets the departure_time of this EdFiStudentSchoolAttendanceEvent.

        The time of day the student departed for the attendance event in ISO 8601 format.  # noqa: E501

        :param departure_time: The departure_time of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: str
        """

        self._departure_time = departure_time

    @property
    def educational_environment_descriptor(self):
        """Gets the educational_environment_descriptor of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501

        The setting in which a child receives education and related services. This attribute is only used if it differs from the EducationalEnvironment of the Section. This is only used in the AttendanceEvent if different from the associated Section.  # noqa: E501

        :return: The educational_environment_descriptor of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: str
        """
        return self._educational_environment_descriptor

    @educational_environment_descriptor.setter
    def educational_environment_descriptor(self, educational_environment_descriptor):
        """Sets the educational_environment_descriptor of this EdFiStudentSchoolAttendanceEvent.

        The setting in which a child receives education and related services. This attribute is only used if it differs from the EducationalEnvironment of the Section. This is only used in the AttendanceEvent if different from the associated Section.  # noqa: E501

        :param educational_environment_descriptor: The educational_environment_descriptor of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                educational_environment_descriptor is not None and len(educational_environment_descriptor) > 306):
            raise ValueError("Invalid value for `educational_environment_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._educational_environment_descriptor = educational_environment_descriptor

    @property
    def event_duration(self):
        """Gets the event_duration of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501

        The amount of time for the event as recognized by the school: 1 day = 1, 1/2 day = 0.5, 1/3 day = 0.33.  # noqa: E501

        :return: The event_duration of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: float
        """
        return self._event_duration

    @event_duration.setter
    def event_duration(self, event_duration):
        """Sets the event_duration of this EdFiStudentSchoolAttendanceEvent.

        The amount of time for the event as recognized by the school: 1 day = 1, 1/2 day = 0.5, 1/3 day = 0.33.  # noqa: E501

        :param event_duration: The event_duration of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: float
        """

        self._event_duration = event_duration

    @property
    def school_attendance_duration(self):
        """Gets the school_attendance_duration of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501

        The duration in minutes of the school attendance event.  # noqa: E501

        :return: The school_attendance_duration of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: int
        """
        return self._school_attendance_duration

    @school_attendance_duration.setter
    def school_attendance_duration(self, school_attendance_duration):
        """Sets the school_attendance_duration of this EdFiStudentSchoolAttendanceEvent.

        The duration in minutes of the school attendance event.  # noqa: E501

        :param school_attendance_duration: The school_attendance_duration of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :type: int
        """

        self._school_attendance_duration = school_attendance_duration

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentSchoolAttendanceEvent.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentSchoolAttendanceEvent.  # noqa: E501
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
        if issubclass(EdFiStudentSchoolAttendanceEvent, dict):
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
        if not isinstance(other, EdFiStudentSchoolAttendanceEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentSchoolAttendanceEvent):
            return True

        return self.to_dict() != other.to_dict()
