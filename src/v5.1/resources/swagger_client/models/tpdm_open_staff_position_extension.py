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


class TpdmOpenStaffPositionExtension(object):
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
        'funding_source_descriptor': 'str',
        'open_staff_position_reason_descriptor': 'str',
        'term_descriptor': 'str',
        'full_time_equivalency': 'float',
        'high_need_academic_subject': 'bool',
        'is_active': 'bool',
        'max_salary': 'float',
        'min_salary': 'float',
        'position_control_number': 'str',
        'total_budgeted': 'float',
        'school_year_type_reference': 'EdFiSchoolYearTypeReference'
    }

    attribute_map = {
        'funding_source_descriptor': 'fundingSourceDescriptor',
        'open_staff_position_reason_descriptor': 'openStaffPositionReasonDescriptor',
        'term_descriptor': 'termDescriptor',
        'full_time_equivalency': 'fullTimeEquivalency',
        'high_need_academic_subject': 'highNeedAcademicSubject',
        'is_active': 'isActive',
        'max_salary': 'maxSalary',
        'min_salary': 'minSalary',
        'position_control_number': 'positionControlNumber',
        'total_budgeted': 'totalBudgeted',
        'school_year_type_reference': 'schoolYearTypeReference'
    }

    def __init__(self, funding_source_descriptor=None, open_staff_position_reason_descriptor=None, term_descriptor=None, full_time_equivalency=None, high_need_academic_subject=None, is_active=None, max_salary=None, min_salary=None, position_control_number=None, total_budgeted=None, school_year_type_reference=None, _configuration=None):  # noqa: E501
        """TpdmOpenStaffPositionExtension - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._funding_source_descriptor = None
        self._open_staff_position_reason_descriptor = None
        self._term_descriptor = None
        self._full_time_equivalency = None
        self._high_need_academic_subject = None
        self._is_active = None
        self._max_salary = None
        self._min_salary = None
        self._position_control_number = None
        self._total_budgeted = None
        self._school_year_type_reference = None
        self.discriminator = None

        if funding_source_descriptor is not None:
            self.funding_source_descriptor = funding_source_descriptor
        if open_staff_position_reason_descriptor is not None:
            self.open_staff_position_reason_descriptor = open_staff_position_reason_descriptor
        if term_descriptor is not None:
            self.term_descriptor = term_descriptor
        if full_time_equivalency is not None:
            self.full_time_equivalency = full_time_equivalency
        if high_need_academic_subject is not None:
            self.high_need_academic_subject = high_need_academic_subject
        if is_active is not None:
            self.is_active = is_active
        if max_salary is not None:
            self.max_salary = max_salary
        if min_salary is not None:
            self.min_salary = min_salary
        if position_control_number is not None:
            self.position_control_number = position_control_number
        if total_budgeted is not None:
            self.total_budgeted = total_budgeted
        if school_year_type_reference is not None:
            self.school_year_type_reference = school_year_type_reference

    @property
    def funding_source_descriptor(self):
        """Gets the funding_source_descriptor of this TpdmOpenStaffPositionExtension.  # noqa: E501

        The funding source for open staff position.  # noqa: E501

        :return: The funding_source_descriptor of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: str
        """
        return self._funding_source_descriptor

    @funding_source_descriptor.setter
    def funding_source_descriptor(self, funding_source_descriptor):
        """Sets the funding_source_descriptor of this TpdmOpenStaffPositionExtension.

        The funding source for open staff position.  # noqa: E501

        :param funding_source_descriptor: The funding_source_descriptor of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                funding_source_descriptor is not None and len(funding_source_descriptor) > 306):
            raise ValueError("Invalid value for `funding_source_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._funding_source_descriptor = funding_source_descriptor

    @property
    def open_staff_position_reason_descriptor(self):
        """Gets the open_staff_position_reason_descriptor of this TpdmOpenStaffPositionExtension.  # noqa: E501

        The reason for the open staff position (e.g., new position, replacement, etc.).  # noqa: E501

        :return: The open_staff_position_reason_descriptor of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: str
        """
        return self._open_staff_position_reason_descriptor

    @open_staff_position_reason_descriptor.setter
    def open_staff_position_reason_descriptor(self, open_staff_position_reason_descriptor):
        """Sets the open_staff_position_reason_descriptor of this TpdmOpenStaffPositionExtension.

        The reason for the open staff position (e.g., new position, replacement, etc.).  # noqa: E501

        :param open_staff_position_reason_descriptor: The open_staff_position_reason_descriptor of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                open_staff_position_reason_descriptor is not None and len(open_staff_position_reason_descriptor) > 306):
            raise ValueError("Invalid value for `open_staff_position_reason_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._open_staff_position_reason_descriptor = open_staff_position_reason_descriptor

    @property
    def term_descriptor(self):
        """Gets the term_descriptor of this TpdmOpenStaffPositionExtension.  # noqa: E501

        The first term for the Session during the school year for which the OpenStaffPosition is seeking to fill.  # noqa: E501

        :return: The term_descriptor of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: str
        """
        return self._term_descriptor

    @term_descriptor.setter
    def term_descriptor(self, term_descriptor):
        """Sets the term_descriptor of this TpdmOpenStaffPositionExtension.

        The first term for the Session during the school year for which the OpenStaffPosition is seeking to fill.  # noqa: E501

        :param term_descriptor: The term_descriptor of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                term_descriptor is not None and len(term_descriptor) > 306):
            raise ValueError("Invalid value for `term_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._term_descriptor = term_descriptor

    @property
    def full_time_equivalency(self):
        """Gets the full_time_equivalency of this TpdmOpenStaffPositionExtension.  # noqa: E501

        The ratio between the hours of work expected in a position and the hours of work normally expected in a full-time position in the same setting.  # noqa: E501

        :return: The full_time_equivalency of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: float
        """
        return self._full_time_equivalency

    @full_time_equivalency.setter
    def full_time_equivalency(self, full_time_equivalency):
        """Sets the full_time_equivalency of this TpdmOpenStaffPositionExtension.

        The ratio between the hours of work expected in a position and the hours of work normally expected in a full-time position in the same setting.  # noqa: E501

        :param full_time_equivalency: The full_time_equivalency of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: float
        """

        self._full_time_equivalency = full_time_equivalency

    @property
    def high_need_academic_subject(self):
        """Gets the high_need_academic_subject of this TpdmOpenStaffPositionExtension.  # noqa: E501

        Indicator as to whether the OpenStaffPosition is filling a high-need subject area designated as a teacher shortage that may be eligible for special grants, aid or compensation.  # noqa: E501

        :return: The high_need_academic_subject of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: bool
        """
        return self._high_need_academic_subject

    @high_need_academic_subject.setter
    def high_need_academic_subject(self, high_need_academic_subject):
        """Sets the high_need_academic_subject of this TpdmOpenStaffPositionExtension.

        Indicator as to whether the OpenStaffPosition is filling a high-need subject area designated as a teacher shortage that may be eligible for special grants, aid or compensation.  # noqa: E501

        :param high_need_academic_subject: The high_need_academic_subject of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: bool
        """

        self._high_need_academic_subject = high_need_academic_subject

    @property
    def is_active(self):
        """Gets the is_active of this TpdmOpenStaffPositionExtension.  # noqa: E501

        Indicator of whether the OpenStaffPosition is currently Active.  # noqa: E501

        :return: The is_active of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this TpdmOpenStaffPositionExtension.

        Indicator of whether the OpenStaffPosition is currently Active.  # noqa: E501

        :param is_active: The is_active of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def max_salary(self):
        """Gets the max_salary of this TpdmOpenStaffPositionExtension.  # noqa: E501

        The maximum salary or wage a person is paid before deductions (excluding differentials) but including annuities.  # noqa: E501

        :return: The max_salary of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: float
        """
        return self._max_salary

    @max_salary.setter
    def max_salary(self, max_salary):
        """Sets the max_salary of this TpdmOpenStaffPositionExtension.

        The maximum salary or wage a person is paid before deductions (excluding differentials) but including annuities.  # noqa: E501

        :param max_salary: The max_salary of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: float
        """

        self._max_salary = max_salary

    @property
    def min_salary(self):
        """Gets the min_salary of this TpdmOpenStaffPositionExtension.  # noqa: E501

        The minimum salary or wage a person is paid before deductions (excluding differentials) but including annuities.  # noqa: E501

        :return: The min_salary of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: float
        """
        return self._min_salary

    @min_salary.setter
    def min_salary(self, min_salary):
        """Sets the min_salary of this TpdmOpenStaffPositionExtension.

        The minimum salary or wage a person is paid before deductions (excluding differentials) but including annuities.  # noqa: E501

        :param min_salary: The min_salary of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: float
        """

        self._min_salary = min_salary

    @property
    def position_control_number(self):
        """Gets the position_control_number of this TpdmOpenStaffPositionExtension.  # noqa: E501

        Identifier assigned to the position to be filled.  # noqa: E501

        :return: The position_control_number of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: str
        """
        return self._position_control_number

    @position_control_number.setter
    def position_control_number(self, position_control_number):
        """Sets the position_control_number of this TpdmOpenStaffPositionExtension.

        Identifier assigned to the position to be filled.  # noqa: E501

        :param position_control_number: The position_control_number of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                position_control_number is not None and len(position_control_number) > 20):
            raise ValueError("Invalid value for `position_control_number`, length must be less than or equal to `20`")  # noqa: E501

        self._position_control_number = position_control_number

    @property
    def total_budgeted(self):
        """Gets the total_budgeted of this TpdmOpenStaffPositionExtension.  # noqa: E501

        Including salary, the fully loaded cost budgeted for this teacher.  # noqa: E501

        :return: The total_budgeted of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: float
        """
        return self._total_budgeted

    @total_budgeted.setter
    def total_budgeted(self, total_budgeted):
        """Sets the total_budgeted of this TpdmOpenStaffPositionExtension.

        Including salary, the fully loaded cost budgeted for this teacher.  # noqa: E501

        :param total_budgeted: The total_budgeted of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: float
        """

        self._total_budgeted = total_budgeted

    @property
    def school_year_type_reference(self):
        """Gets the school_year_type_reference of this TpdmOpenStaffPositionExtension.  # noqa: E501


        :return: The school_year_type_reference of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :rtype: EdFiSchoolYearTypeReference
        """
        return self._school_year_type_reference

    @school_year_type_reference.setter
    def school_year_type_reference(self, school_year_type_reference):
        """Sets the school_year_type_reference of this TpdmOpenStaffPositionExtension.


        :param school_year_type_reference: The school_year_type_reference of this TpdmOpenStaffPositionExtension.  # noqa: E501
        :type: EdFiSchoolYearTypeReference
        """

        self._school_year_type_reference = school_year_type_reference

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
        if issubclass(TpdmOpenStaffPositionExtension, dict):
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
        if not isinstance(other, TpdmOpenStaffPositionExtension):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmOpenStaffPositionExtension):
            return True

        return self.to_dict() != other.to_dict()