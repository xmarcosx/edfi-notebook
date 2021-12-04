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


class Section(object):
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
        'local_course_code': 'str',
        'section_identifier': 'str',
        'academic_subject_descriptor': 'str',
        'available_credits': 'float',
        'class_periods': 'list[SectionSectionClassPeriod]',
        'educational_environment_descriptor': 'str',
        'local_course_title': 'str',
        'location': 'SectionLocation',
        'sequence_of_course': 'int',
        'session': 'SectionSession',
        'staff': 'list[SectionStaffSectionAssociation]',
        'students': 'list[SectionStudentSectionAssociation]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'local_course_code': 'localCourseCode',
        'section_identifier': 'sectionIdentifier',
        'academic_subject_descriptor': 'academicSubjectDescriptor',
        'available_credits': 'availableCredits',
        'class_periods': 'classPeriods',
        'educational_environment_descriptor': 'educationalEnvironmentDescriptor',
        'local_course_title': 'localCourseTitle',
        'location': 'location',
        'sequence_of_course': 'sequenceOfCourse',
        'session': 'session',
        'staff': 'staff',
        'students': 'students',
        'etag': '_etag'
    }

    def __init__(self, id=None, local_course_code=None, section_identifier=None, academic_subject_descriptor=None, available_credits=None, class_periods=None, educational_environment_descriptor=None, local_course_title=None, location=None, sequence_of_course=None, session=None, staff=None, students=None, etag=None, _configuration=None):  # noqa: E501
        """Section - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._local_course_code = None
        self._section_identifier = None
        self._academic_subject_descriptor = None
        self._available_credits = None
        self._class_periods = None
        self._educational_environment_descriptor = None
        self._local_course_title = None
        self._location = None
        self._sequence_of_course = None
        self._session = None
        self._staff = None
        self._students = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.local_course_code = local_course_code
        self.section_identifier = section_identifier
        if academic_subject_descriptor is not None:
            self.academic_subject_descriptor = academic_subject_descriptor
        if available_credits is not None:
            self.available_credits = available_credits
        if class_periods is not None:
            self.class_periods = class_periods
        if educational_environment_descriptor is not None:
            self.educational_environment_descriptor = educational_environment_descriptor
        if local_course_title is not None:
            self.local_course_title = local_course_title
        if location is not None:
            self.location = location
        if sequence_of_course is not None:
            self.sequence_of_course = sequence_of_course
        if session is not None:
            self.session = session
        if staff is not None:
            self.staff = staff
        if students is not None:
            self.students = students
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this Section.  # noqa: E501

          # noqa: E501

        :return: The id of this Section.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Section.

          # noqa: E501

        :param id: The id of this Section.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def local_course_code(self):
        """Gets the local_course_code of this Section.  # noqa: E501

        The local code assigned by the School that identifies the course offering provided for the instruction of students.  # noqa: E501

        :return: The local_course_code of this Section.  # noqa: E501
        :rtype: str
        """
        return self._local_course_code

    @local_course_code.setter
    def local_course_code(self, local_course_code):
        """Sets the local_course_code of this Section.

        The local code assigned by the School that identifies the course offering provided for the instruction of students.  # noqa: E501

        :param local_course_code: The local_course_code of this Section.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and local_course_code is None:
            raise ValueError("Invalid value for `local_course_code`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                local_course_code is not None and len(local_course_code) > 60):
            raise ValueError("Invalid value for `local_course_code`, length must be less than or equal to `60`")  # noqa: E501

        self._local_course_code = local_course_code

    @property
    def section_identifier(self):
        """Gets the section_identifier of this Section.  # noqa: E501

        The local identifier assigned to a section.  # noqa: E501

        :return: The section_identifier of this Section.  # noqa: E501
        :rtype: str
        """
        return self._section_identifier

    @section_identifier.setter
    def section_identifier(self, section_identifier):
        """Sets the section_identifier of this Section.

        The local identifier assigned to a section.  # noqa: E501

        :param section_identifier: The section_identifier of this Section.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and section_identifier is None:
            raise ValueError("Invalid value for `section_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                section_identifier is not None and len(section_identifier) > 255):
            raise ValueError("Invalid value for `section_identifier`, length must be less than or equal to `255`")  # noqa: E501

        self._section_identifier = section_identifier

    @property
    def academic_subject_descriptor(self):
        """Gets the academic_subject_descriptor of this Section.  # noqa: E501

        The intended major subject area of the course.  # noqa: E501

        :return: The academic_subject_descriptor of this Section.  # noqa: E501
        :rtype: str
        """
        return self._academic_subject_descriptor

    @academic_subject_descriptor.setter
    def academic_subject_descriptor(self, academic_subject_descriptor):
        """Sets the academic_subject_descriptor of this Section.

        The intended major subject area of the course.  # noqa: E501

        :param academic_subject_descriptor: The academic_subject_descriptor of this Section.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                academic_subject_descriptor is not None and len(academic_subject_descriptor) > 306):
            raise ValueError("Invalid value for `academic_subject_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._academic_subject_descriptor = academic_subject_descriptor

    @property
    def available_credits(self):
        """Gets the available_credits of this Section.  # noqa: E501

        The value of credits or units of value awarded for the completion of a course.  # noqa: E501

        :return: The available_credits of this Section.  # noqa: E501
        :rtype: float
        """
        return self._available_credits

    @available_credits.setter
    def available_credits(self, available_credits):
        """Sets the available_credits of this Section.

        The value of credits or units of value awarded for the completion of a course.  # noqa: E501

        :param available_credits: The available_credits of this Section.  # noqa: E501
        :type: float
        """

        self._available_credits = available_credits

    @property
    def class_periods(self):
        """Gets the class_periods of this Section.  # noqa: E501

        An unordered collection of sectionClassPeriods.   # noqa: E501

        :return: The class_periods of this Section.  # noqa: E501
        :rtype: list[SectionSectionClassPeriod]
        """
        return self._class_periods

    @class_periods.setter
    def class_periods(self, class_periods):
        """Sets the class_periods of this Section.

        An unordered collection of sectionClassPeriods.   # noqa: E501

        :param class_periods: The class_periods of this Section.  # noqa: E501
        :type: list[SectionSectionClassPeriod]
        """

        self._class_periods = class_periods

    @property
    def educational_environment_descriptor(self):
        """Gets the educational_environment_descriptor of this Section.  # noqa: E501

        The setting in which a child receives education and related services; for example:        Center-based instruction        Home-based instruction        Hospital class        Mainstream        Residential care and treatment facility        ...  # noqa: E501

        :return: The educational_environment_descriptor of this Section.  # noqa: E501
        :rtype: str
        """
        return self._educational_environment_descriptor

    @educational_environment_descriptor.setter
    def educational_environment_descriptor(self, educational_environment_descriptor):
        """Sets the educational_environment_descriptor of this Section.

        The setting in which a child receives education and related services; for example:        Center-based instruction        Home-based instruction        Hospital class        Mainstream        Residential care and treatment facility        ...  # noqa: E501

        :param educational_environment_descriptor: The educational_environment_descriptor of this Section.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                educational_environment_descriptor is not None and len(educational_environment_descriptor) > 306):
            raise ValueError("Invalid value for `educational_environment_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._educational_environment_descriptor = educational_environment_descriptor

    @property
    def local_course_title(self):
        """Gets the local_course_title of this Section.  # noqa: E501

        The descriptive name given to a course of study offered in the school, if different from the CourseTitle.  # noqa: E501

        :return: The local_course_title of this Section.  # noqa: E501
        :rtype: str
        """
        return self._local_course_title

    @local_course_title.setter
    def local_course_title(self, local_course_title):
        """Sets the local_course_title of this Section.

        The descriptive name given to a course of study offered in the school, if different from the CourseTitle.  # noqa: E501

        :param local_course_title: The local_course_title of this Section.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                local_course_title is not None and len(local_course_title) > 60):
            raise ValueError("Invalid value for `local_course_title`, length must be less than or equal to `60`")  # noqa: E501

        self._local_course_title = local_course_title

    @property
    def location(self):
        """Gets the location of this Section.  # noqa: E501


        :return: The location of this Section.  # noqa: E501
        :rtype: SectionLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Section.


        :param location: The location of this Section.  # noqa: E501
        :type: SectionLocation
        """

        self._location = location

    @property
    def sequence_of_course(self):
        """Gets the sequence_of_course of this Section.  # noqa: E501

        When a section is part of a sequence of parts for a course, the number of the sequence. If the course has only one part, the value of this section attribute should be 1.  # noqa: E501

        :return: The sequence_of_course of this Section.  # noqa: E501
        :rtype: int
        """
        return self._sequence_of_course

    @sequence_of_course.setter
    def sequence_of_course(self, sequence_of_course):
        """Sets the sequence_of_course of this Section.

        When a section is part of a sequence of parts for a course, the number of the sequence. If the course has only one part, the value of this section attribute should be 1.  # noqa: E501

        :param sequence_of_course: The sequence_of_course of this Section.  # noqa: E501
        :type: int
        """

        self._sequence_of_course = sequence_of_course

    @property
    def session(self):
        """Gets the session of this Section.  # noqa: E501


        :return: The session of this Section.  # noqa: E501
        :rtype: SectionSession
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this Section.


        :param session: The session of this Section.  # noqa: E501
        :type: SectionSession
        """

        self._session = session

    @property
    def staff(self):
        """Gets the staff of this Section.  # noqa: E501

        An unordered collection of staffSectionAssociations.   # noqa: E501

        :return: The staff of this Section.  # noqa: E501
        :rtype: list[SectionStaffSectionAssociation]
        """
        return self._staff

    @staff.setter
    def staff(self, staff):
        """Sets the staff of this Section.

        An unordered collection of staffSectionAssociations.   # noqa: E501

        :param staff: The staff of this Section.  # noqa: E501
        :type: list[SectionStaffSectionAssociation]
        """

        self._staff = staff

    @property
    def students(self):
        """Gets the students of this Section.  # noqa: E501

        An unordered collection of studentSectionAssociations.   # noqa: E501

        :return: The students of this Section.  # noqa: E501
        :rtype: list[SectionStudentSectionAssociation]
        """
        return self._students

    @students.setter
    def students(self, students):
        """Sets the students of this Section.

        An unordered collection of studentSectionAssociations.   # noqa: E501

        :param students: The students of this Section.  # noqa: E501
        :type: list[SectionStudentSectionAssociation]
        """

        self._students = students

    @property
    def etag(self):
        """Gets the etag of this Section.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this Section.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this Section.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this Section.  # noqa: E501
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
        if issubclass(Section, dict):
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
        if not isinstance(other, Section):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Section):
            return True

        return self.to_dict() != other.to_dict()
