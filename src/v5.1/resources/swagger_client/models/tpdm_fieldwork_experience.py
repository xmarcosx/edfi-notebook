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


class TpdmFieldworkExperience(object):
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
        'fieldwork_identifier': 'str',
        'schools': 'list[TpdmFieldworkExperienceSchool]',
        'student_reference': 'EdFiStudentReference',
        'coteaching': 'TpdmFieldworkExperienceCoteaching',
        'end_date': 'date',
        'fieldwork_type_descriptor': 'str',
        'hours_completed': 'float',
        'program_gateway_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'begin_date': 'beginDate',
        'fieldwork_identifier': 'fieldworkIdentifier',
        'schools': 'schools',
        'student_reference': 'studentReference',
        'coteaching': 'coteaching',
        'end_date': 'endDate',
        'fieldwork_type_descriptor': 'fieldworkTypeDescriptor',
        'hours_completed': 'hoursCompleted',
        'program_gateway_descriptor': 'programGatewayDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, begin_date=None, fieldwork_identifier=None, schools=None, student_reference=None, coteaching=None, end_date=None, fieldwork_type_descriptor=None, hours_completed=None, program_gateway_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmFieldworkExperience - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._begin_date = None
        self._fieldwork_identifier = None
        self._schools = None
        self._student_reference = None
        self._coteaching = None
        self._end_date = None
        self._fieldwork_type_descriptor = None
        self._hours_completed = None
        self._program_gateway_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.begin_date = begin_date
        self.fieldwork_identifier = fieldwork_identifier
        self.schools = schools
        self.student_reference = student_reference
        if coteaching is not None:
            self.coteaching = coteaching
        if end_date is not None:
            self.end_date = end_date
        self.fieldwork_type_descriptor = fieldwork_type_descriptor
        if hours_completed is not None:
            self.hours_completed = hours_completed
        if program_gateway_descriptor is not None:
            self.program_gateway_descriptor = program_gateway_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmFieldworkExperience.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmFieldworkExperience.

          # noqa: E501

        :param id: The id of this TpdmFieldworkExperience.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def begin_date(self):
        """Gets the begin_date of this TpdmFieldworkExperience.  # noqa: E501

        The month, day, and year on which the staff first starts fieldwork.  # noqa: E501

        :return: The begin_date of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this TpdmFieldworkExperience.

        The month, day, and year on which the staff first starts fieldwork.  # noqa: E501

        :param begin_date: The begin_date of this TpdmFieldworkExperience.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def fieldwork_identifier(self):
        """Gets the fieldwork_identifier of this TpdmFieldworkExperience.  # noqa: E501

        The unique identifier for the fieldwork experience  # noqa: E501

        :return: The fieldwork_identifier of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: str
        """
        return self._fieldwork_identifier

    @fieldwork_identifier.setter
    def fieldwork_identifier(self, fieldwork_identifier):
        """Sets the fieldwork_identifier of this TpdmFieldworkExperience.

        The unique identifier for the fieldwork experience  # noqa: E501

        :param fieldwork_identifier: The fieldwork_identifier of this TpdmFieldworkExperience.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and fieldwork_identifier is None:
            raise ValueError("Invalid value for `fieldwork_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                fieldwork_identifier is not None and len(fieldwork_identifier) > 64):
            raise ValueError("Invalid value for `fieldwork_identifier`, length must be less than or equal to `64`")  # noqa: E501

        self._fieldwork_identifier = fieldwork_identifier

    @property
    def schools(self):
        """Gets the schools of this TpdmFieldworkExperience.  # noqa: E501

        An unordered collection of fieldworkExperienceSchools. The school the field work experience is associated with  # noqa: E501

        :return: The schools of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: list[TpdmFieldworkExperienceSchool]
        """
        return self._schools

    @schools.setter
    def schools(self, schools):
        """Sets the schools of this TpdmFieldworkExperience.

        An unordered collection of fieldworkExperienceSchools. The school the field work experience is associated with  # noqa: E501

        :param schools: The schools of this TpdmFieldworkExperience.  # noqa: E501
        :type: list[TpdmFieldworkExperienceSchool]
        """
        if self._configuration.client_side_validation and schools is None:
            raise ValueError("Invalid value for `schools`, must not be `None`")  # noqa: E501

        self._schools = schools

    @property
    def student_reference(self):
        """Gets the student_reference of this TpdmFieldworkExperience.  # noqa: E501


        :return: The student_reference of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this TpdmFieldworkExperience.


        :param student_reference: The student_reference of this TpdmFieldworkExperience.  # noqa: E501
        :type: EdFiStudentReference
        """
        if self._configuration.client_side_validation and student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def coteaching(self):
        """Gets the coteaching of this TpdmFieldworkExperience.  # noqa: E501


        :return: The coteaching of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: TpdmFieldworkExperienceCoteaching
        """
        return self._coteaching

    @coteaching.setter
    def coteaching(self, coteaching):
        """Sets the coteaching of this TpdmFieldworkExperience.


        :param coteaching: The coteaching of this TpdmFieldworkExperience.  # noqa: E501
        :type: TpdmFieldworkExperienceCoteaching
        """

        self._coteaching = coteaching

    @property
    def end_date(self):
        """Gets the end_date of this TpdmFieldworkExperience.  # noqa: E501

        The month, day, and year on which the staff ends fieldwork.  # noqa: E501

        :return: The end_date of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TpdmFieldworkExperience.

        The month, day, and year on which the staff ends fieldwork.  # noqa: E501

        :param end_date: The end_date of this TpdmFieldworkExperience.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def fieldwork_type_descriptor(self):
        """Gets the fieldwork_type_descriptor of this TpdmFieldworkExperience.  # noqa: E501

        The type of fieldwork being executed by a staff.  # noqa: E501

        :return: The fieldwork_type_descriptor of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: str
        """
        return self._fieldwork_type_descriptor

    @fieldwork_type_descriptor.setter
    def fieldwork_type_descriptor(self, fieldwork_type_descriptor):
        """Sets the fieldwork_type_descriptor of this TpdmFieldworkExperience.

        The type of fieldwork being executed by a staff.  # noqa: E501

        :param fieldwork_type_descriptor: The fieldwork_type_descriptor of this TpdmFieldworkExperience.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and fieldwork_type_descriptor is None:
            raise ValueError("Invalid value for `fieldwork_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                fieldwork_type_descriptor is not None and len(fieldwork_type_descriptor) > 306):
            raise ValueError("Invalid value for `fieldwork_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._fieldwork_type_descriptor = fieldwork_type_descriptor

    @property
    def hours_completed(self):
        """Gets the hours_completed of this TpdmFieldworkExperience.  # noqa: E501

        The number of hours completed during the fieldwork experience.  # noqa: E501

        :return: The hours_completed of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: float
        """
        return self._hours_completed

    @hours_completed.setter
    def hours_completed(self, hours_completed):
        """Sets the hours_completed of this TpdmFieldworkExperience.

        The number of hours completed during the fieldwork experience.  # noqa: E501

        :param hours_completed: The hours_completed of this TpdmFieldworkExperience.  # noqa: E501
        :type: float
        """

        self._hours_completed = hours_completed

    @property
    def program_gateway_descriptor(self):
        """Gets the program_gateway_descriptor of this TpdmFieldworkExperience.  # noqa: E501

        The descriptor holds the program gateway that is associated with continuation in a program.  # noqa: E501

        :return: The program_gateway_descriptor of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: str
        """
        return self._program_gateway_descriptor

    @program_gateway_descriptor.setter
    def program_gateway_descriptor(self, program_gateway_descriptor):
        """Sets the program_gateway_descriptor of this TpdmFieldworkExperience.

        The descriptor holds the program gateway that is associated with continuation in a program.  # noqa: E501

        :param program_gateway_descriptor: The program_gateway_descriptor of this TpdmFieldworkExperience.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                program_gateway_descriptor is not None and len(program_gateway_descriptor) > 306):
            raise ValueError("Invalid value for `program_gateway_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._program_gateway_descriptor = program_gateway_descriptor

    @property
    def etag(self):
        """Gets the etag of this TpdmFieldworkExperience.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmFieldworkExperience.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmFieldworkExperience.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmFieldworkExperience.  # noqa: E501
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
        if issubclass(TpdmFieldworkExperience, dict):
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
        if not isinstance(other, TpdmFieldworkExperience):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmFieldworkExperience):
            return True

        return self.to_dict() != other.to_dict()