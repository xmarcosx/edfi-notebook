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


class TpdmOpenStaffPositionEvent(object):
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
        'event_date': 'date',
        'open_staff_position_event_type_descriptor': 'str',
        'open_staff_position_reference': 'EdFiOpenStaffPositionReference',
        'open_staff_position_event_status_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'event_date': 'eventDate',
        'open_staff_position_event_type_descriptor': 'openStaffPositionEventTypeDescriptor',
        'open_staff_position_reference': 'openStaffPositionReference',
        'open_staff_position_event_status_descriptor': 'openStaffPositionEventStatusDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, event_date=None, open_staff_position_event_type_descriptor=None, open_staff_position_reference=None, open_staff_position_event_status_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmOpenStaffPositionEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._event_date = None
        self._open_staff_position_event_type_descriptor = None
        self._open_staff_position_reference = None
        self._open_staff_position_event_status_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.event_date = event_date
        self.open_staff_position_event_type_descriptor = open_staff_position_event_type_descriptor
        self.open_staff_position_reference = open_staff_position_reference
        if open_staff_position_event_status_descriptor is not None:
            self.open_staff_position_event_status_descriptor = open_staff_position_event_status_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmOpenStaffPositionEvent.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmOpenStaffPositionEvent.

          # noqa: E501

        :param id: The id of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def event_date(self):
        """Gets the event_date of this TpdmOpenStaffPositionEvent.  # noqa: E501

        Date of the open staff position event.  # noqa: E501

        :return: The event_date of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :rtype: date
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this TpdmOpenStaffPositionEvent.

        Date of the open staff position event.  # noqa: E501

        :param event_date: The event_date of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and event_date is None:
            raise ValueError("Invalid value for `event_date`, must not be `None`")  # noqa: E501

        self._event_date = event_date

    @property
    def open_staff_position_event_type_descriptor(self):
        """Gets the open_staff_position_event_type_descriptor of this TpdmOpenStaffPositionEvent.  # noqa: E501

        Reflects milestones like vacancy approved, vacancy posted, date onboarded, processing date, orientation date, etc.  # noqa: E501

        :return: The open_staff_position_event_type_descriptor of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :rtype: str
        """
        return self._open_staff_position_event_type_descriptor

    @open_staff_position_event_type_descriptor.setter
    def open_staff_position_event_type_descriptor(self, open_staff_position_event_type_descriptor):
        """Sets the open_staff_position_event_type_descriptor of this TpdmOpenStaffPositionEvent.

        Reflects milestones like vacancy approved, vacancy posted, date onboarded, processing date, orientation date, etc.  # noqa: E501

        :param open_staff_position_event_type_descriptor: The open_staff_position_event_type_descriptor of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and open_staff_position_event_type_descriptor is None:
            raise ValueError("Invalid value for `open_staff_position_event_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                open_staff_position_event_type_descriptor is not None and len(open_staff_position_event_type_descriptor) > 306):
            raise ValueError("Invalid value for `open_staff_position_event_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._open_staff_position_event_type_descriptor = open_staff_position_event_type_descriptor

    @property
    def open_staff_position_reference(self):
        """Gets the open_staff_position_reference of this TpdmOpenStaffPositionEvent.  # noqa: E501


        :return: The open_staff_position_reference of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :rtype: EdFiOpenStaffPositionReference
        """
        return self._open_staff_position_reference

    @open_staff_position_reference.setter
    def open_staff_position_reference(self, open_staff_position_reference):
        """Sets the open_staff_position_reference of this TpdmOpenStaffPositionEvent.


        :param open_staff_position_reference: The open_staff_position_reference of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :type: EdFiOpenStaffPositionReference
        """
        if self._configuration.client_side_validation and open_staff_position_reference is None:
            raise ValueError("Invalid value for `open_staff_position_reference`, must not be `None`")  # noqa: E501

        self._open_staff_position_reference = open_staff_position_reference

    @property
    def open_staff_position_event_status_descriptor(self):
        """Gets the open_staff_position_event_status_descriptor of this TpdmOpenStaffPositionEvent.  # noqa: E501

        Reflects the status of the milestone (e.g., pending, completed, cancelled).  # noqa: E501

        :return: The open_staff_position_event_status_descriptor of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :rtype: str
        """
        return self._open_staff_position_event_status_descriptor

    @open_staff_position_event_status_descriptor.setter
    def open_staff_position_event_status_descriptor(self, open_staff_position_event_status_descriptor):
        """Sets the open_staff_position_event_status_descriptor of this TpdmOpenStaffPositionEvent.

        Reflects the status of the milestone (e.g., pending, completed, cancelled).  # noqa: E501

        :param open_staff_position_event_status_descriptor: The open_staff_position_event_status_descriptor of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                open_staff_position_event_status_descriptor is not None and len(open_staff_position_event_status_descriptor) > 306):
            raise ValueError("Invalid value for `open_staff_position_event_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._open_staff_position_event_status_descriptor = open_staff_position_event_status_descriptor

    @property
    def etag(self):
        """Gets the etag of this TpdmOpenStaffPositionEvent.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmOpenStaffPositionEvent.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmOpenStaffPositionEvent.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmOpenStaffPositionEvent.  # noqa: E501
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
        if issubclass(TpdmOpenStaffPositionEvent, dict):
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
        if not isinstance(other, TpdmOpenStaffPositionEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmOpenStaffPositionEvent):
            return True

        return self.to_dict() != other.to_dict()