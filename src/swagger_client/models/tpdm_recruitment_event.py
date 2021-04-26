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


class TpdmRecruitmentEvent(object):
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
        'event_title': 'str',
        'event_description': 'str',
        'event_location': 'str',
        'recruitment_event_type_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'event_date': 'eventDate',
        'event_title': 'eventTitle',
        'event_description': 'eventDescription',
        'event_location': 'eventLocation',
        'recruitment_event_type_descriptor': 'recruitmentEventTypeDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, event_date=None, event_title=None, event_description=None, event_location=None, recruitment_event_type_descriptor=None, etag=None):  # noqa: E501
        """TpdmRecruitmentEvent - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._event_date = None
        self._event_title = None
        self._event_description = None
        self._event_location = None
        self._recruitment_event_type_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.event_date = event_date
        self.event_title = event_title
        if event_description is not None:
            self.event_description = event_description
        if event_location is not None:
            self.event_location = event_location
        self.recruitment_event_type_descriptor = recruitment_event_type_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmRecruitmentEvent.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmRecruitmentEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmRecruitmentEvent.

          # noqa: E501

        :param id: The id of this TpdmRecruitmentEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def event_date(self):
        """Gets the event_date of this TpdmRecruitmentEvent.  # noqa: E501

        The date of the event.  # noqa: E501

        :return: The event_date of this TpdmRecruitmentEvent.  # noqa: E501
        :rtype: date
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this TpdmRecruitmentEvent.

        The date of the event.  # noqa: E501

        :param event_date: The event_date of this TpdmRecruitmentEvent.  # noqa: E501
        :type: date
        """
        if event_date is None:
            raise ValueError("Invalid value for `event_date`, must not be `None`")  # noqa: E501

        self._event_date = event_date

    @property
    def event_title(self):
        """Gets the event_title of this TpdmRecruitmentEvent.  # noqa: E501

        The title of the event.  # noqa: E501

        :return: The event_title of this TpdmRecruitmentEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_title

    @event_title.setter
    def event_title(self, event_title):
        """Sets the event_title of this TpdmRecruitmentEvent.

        The title of the event.  # noqa: E501

        :param event_title: The event_title of this TpdmRecruitmentEvent.  # noqa: E501
        :type: str
        """
        if event_title is None:
            raise ValueError("Invalid value for `event_title`, must not be `None`")  # noqa: E501
        if event_title is not None and len(event_title) > 50:
            raise ValueError("Invalid value for `event_title`, length must be less than or equal to `50`")  # noqa: E501

        self._event_title = event_title

    @property
    def event_description(self):
        """Gets the event_description of this TpdmRecruitmentEvent.  # noqa: E501

        The long description of the event.  # noqa: E501

        :return: The event_description of this TpdmRecruitmentEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        """Sets the event_description of this TpdmRecruitmentEvent.

        The long description of the event.  # noqa: E501

        :param event_description: The event_description of this TpdmRecruitmentEvent.  # noqa: E501
        :type: str
        """
        if event_description is not None and len(event_description) > 255:
            raise ValueError("Invalid value for `event_description`, length must be less than or equal to `255`")  # noqa: E501

        self._event_description = event_description

    @property
    def event_location(self):
        """Gets the event_location of this TpdmRecruitmentEvent.  # noqa: E501

        The location of the event.  # noqa: E501

        :return: The event_location of this TpdmRecruitmentEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_location

    @event_location.setter
    def event_location(self, event_location):
        """Sets the event_location of this TpdmRecruitmentEvent.

        The location of the event.  # noqa: E501

        :param event_location: The event_location of this TpdmRecruitmentEvent.  # noqa: E501
        :type: str
        """
        if event_location is not None and len(event_location) > 255:
            raise ValueError("Invalid value for `event_location`, length must be less than or equal to `255`")  # noqa: E501

        self._event_location = event_location

    @property
    def recruitment_event_type_descriptor(self):
        """Gets the recruitment_event_type_descriptor of this TpdmRecruitmentEvent.  # noqa: E501

        The type of event.  # noqa: E501

        :return: The recruitment_event_type_descriptor of this TpdmRecruitmentEvent.  # noqa: E501
        :rtype: str
        """
        return self._recruitment_event_type_descriptor

    @recruitment_event_type_descriptor.setter
    def recruitment_event_type_descriptor(self, recruitment_event_type_descriptor):
        """Sets the recruitment_event_type_descriptor of this TpdmRecruitmentEvent.

        The type of event.  # noqa: E501

        :param recruitment_event_type_descriptor: The recruitment_event_type_descriptor of this TpdmRecruitmentEvent.  # noqa: E501
        :type: str
        """
        if recruitment_event_type_descriptor is None:
            raise ValueError("Invalid value for `recruitment_event_type_descriptor`, must not be `None`")  # noqa: E501
        if recruitment_event_type_descriptor is not None and len(recruitment_event_type_descriptor) > 306:
            raise ValueError("Invalid value for `recruitment_event_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._recruitment_event_type_descriptor = recruitment_event_type_descriptor

    @property
    def etag(self):
        """Gets the etag of this TpdmRecruitmentEvent.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmRecruitmentEvent.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmRecruitmentEvent.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmRecruitmentEvent.  # noqa: E501
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
        if issubclass(TpdmRecruitmentEvent, dict):
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
        if not isinstance(other, TpdmRecruitmentEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
