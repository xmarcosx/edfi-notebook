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


class EdFiStaffAbsenceEvent(object):
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
        'absence_event_category_descriptor': 'str',
        'event_date': 'date',
        'staff_reference': 'EdFiStaffReference',
        'absence_event_reason': 'str',
        'hours_absent': 'float',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'absence_event_category_descriptor': 'absenceEventCategoryDescriptor',
        'event_date': 'eventDate',
        'staff_reference': 'staffReference',
        'absence_event_reason': 'absenceEventReason',
        'hours_absent': 'hoursAbsent',
        'etag': '_etag'
    }

    def __init__(self, id=None, absence_event_category_descriptor=None, event_date=None, staff_reference=None, absence_event_reason=None, hours_absent=None, etag=None):  # noqa: E501
        """EdFiStaffAbsenceEvent - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._absence_event_category_descriptor = None
        self._event_date = None
        self._staff_reference = None
        self._absence_event_reason = None
        self._hours_absent = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.absence_event_category_descriptor = absence_event_category_descriptor
        self.event_date = event_date
        self.staff_reference = staff_reference
        if absence_event_reason is not None:
            self.absence_event_reason = absence_event_reason
        if hours_absent is not None:
            self.hours_absent = hours_absent
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStaffAbsenceEvent.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStaffAbsenceEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStaffAbsenceEvent.

          # noqa: E501

        :param id: The id of this EdFiStaffAbsenceEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def absence_event_category_descriptor(self):
        """Gets the absence_event_category_descriptor of this EdFiStaffAbsenceEvent.  # noqa: E501

        The code describing the type of absence.  # noqa: E501

        :return: The absence_event_category_descriptor of this EdFiStaffAbsenceEvent.  # noqa: E501
        :rtype: str
        """
        return self._absence_event_category_descriptor

    @absence_event_category_descriptor.setter
    def absence_event_category_descriptor(self, absence_event_category_descriptor):
        """Sets the absence_event_category_descriptor of this EdFiStaffAbsenceEvent.

        The code describing the type of absence.  # noqa: E501

        :param absence_event_category_descriptor: The absence_event_category_descriptor of this EdFiStaffAbsenceEvent.  # noqa: E501
        :type: str
        """
        if absence_event_category_descriptor is None:
            raise ValueError("Invalid value for `absence_event_category_descriptor`, must not be `None`")  # noqa: E501
        if absence_event_category_descriptor is not None and len(absence_event_category_descriptor) > 306:
            raise ValueError("Invalid value for `absence_event_category_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._absence_event_category_descriptor = absence_event_category_descriptor

    @property
    def event_date(self):
        """Gets the event_date of this EdFiStaffAbsenceEvent.  # noqa: E501

        Date for this leave event.  # noqa: E501

        :return: The event_date of this EdFiStaffAbsenceEvent.  # noqa: E501
        :rtype: date
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this EdFiStaffAbsenceEvent.

        Date for this leave event.  # noqa: E501

        :param event_date: The event_date of this EdFiStaffAbsenceEvent.  # noqa: E501
        :type: date
        """
        if event_date is None:
            raise ValueError("Invalid value for `event_date`, must not be `None`")  # noqa: E501

        self._event_date = event_date

    @property
    def staff_reference(self):
        """Gets the staff_reference of this EdFiStaffAbsenceEvent.  # noqa: E501


        :return: The staff_reference of this EdFiStaffAbsenceEvent.  # noqa: E501
        :rtype: EdFiStaffReference
        """
        return self._staff_reference

    @staff_reference.setter
    def staff_reference(self, staff_reference):
        """Sets the staff_reference of this EdFiStaffAbsenceEvent.


        :param staff_reference: The staff_reference of this EdFiStaffAbsenceEvent.  # noqa: E501
        :type: EdFiStaffReference
        """
        if staff_reference is None:
            raise ValueError("Invalid value for `staff_reference`, must not be `None`")  # noqa: E501

        self._staff_reference = staff_reference

    @property
    def absence_event_reason(self):
        """Gets the absence_event_reason of this EdFiStaffAbsenceEvent.  # noqa: E501

        Expanded reason for the staff absence.  # noqa: E501

        :return: The absence_event_reason of this EdFiStaffAbsenceEvent.  # noqa: E501
        :rtype: str
        """
        return self._absence_event_reason

    @absence_event_reason.setter
    def absence_event_reason(self, absence_event_reason):
        """Sets the absence_event_reason of this EdFiStaffAbsenceEvent.

        Expanded reason for the staff absence.  # noqa: E501

        :param absence_event_reason: The absence_event_reason of this EdFiStaffAbsenceEvent.  # noqa: E501
        :type: str
        """
        if absence_event_reason is not None and len(absence_event_reason) > 40:
            raise ValueError("Invalid value for `absence_event_reason`, length must be less than or equal to `40`")  # noqa: E501

        self._absence_event_reason = absence_event_reason

    @property
    def hours_absent(self):
        """Gets the hours_absent of this EdFiStaffAbsenceEvent.  # noqa: E501

        The hours the staff was absent, if not the entire working day.  # noqa: E501

        :return: The hours_absent of this EdFiStaffAbsenceEvent.  # noqa: E501
        :rtype: float
        """
        return self._hours_absent

    @hours_absent.setter
    def hours_absent(self, hours_absent):
        """Sets the hours_absent of this EdFiStaffAbsenceEvent.

        The hours the staff was absent, if not the entire working day.  # noqa: E501

        :param hours_absent: The hours_absent of this EdFiStaffAbsenceEvent.  # noqa: E501
        :type: float
        """

        self._hours_absent = hours_absent

    @property
    def etag(self):
        """Gets the etag of this EdFiStaffAbsenceEvent.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStaffAbsenceEvent.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStaffAbsenceEvent.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStaffAbsenceEvent.  # noqa: E501
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
        if issubclass(EdFiStaffAbsenceEvent, dict):
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
        if not isinstance(other, EdFiStaffAbsenceEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
