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


class TpdmTeacherCandidateTeacherPreparationProviderAssociation(object):
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
        'entry_date': 'date',
        'class_of_school_year_type_reference': 'EdFiSchoolYearTypeReference',
        'school_year_type_reference': 'EdFiSchoolYearTypeReference',
        'teacher_candidate_reference': 'TpdmTeacherCandidateReference',
        'teacher_preparation_provider_reference': 'TpdmTeacherPreparationProviderReference',
        'entry_type_descriptor': 'str',
        'exit_withdraw_date': 'date',
        'exit_withdraw_type_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'entry_date': 'entryDate',
        'class_of_school_year_type_reference': 'classOfSchoolYearTypeReference',
        'school_year_type_reference': 'schoolYearTypeReference',
        'teacher_candidate_reference': 'teacherCandidateReference',
        'teacher_preparation_provider_reference': 'teacherPreparationProviderReference',
        'entry_type_descriptor': 'entryTypeDescriptor',
        'exit_withdraw_date': 'exitWithdrawDate',
        'exit_withdraw_type_descriptor': 'exitWithdrawTypeDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, entry_date=None, class_of_school_year_type_reference=None, school_year_type_reference=None, teacher_candidate_reference=None, teacher_preparation_provider_reference=None, entry_type_descriptor=None, exit_withdraw_date=None, exit_withdraw_type_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmTeacherCandidateTeacherPreparationProviderAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._entry_date = None
        self._class_of_school_year_type_reference = None
        self._school_year_type_reference = None
        self._teacher_candidate_reference = None
        self._teacher_preparation_provider_reference = None
        self._entry_type_descriptor = None
        self._exit_withdraw_date = None
        self._exit_withdraw_type_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.entry_date = entry_date
        if class_of_school_year_type_reference is not None:
            self.class_of_school_year_type_reference = class_of_school_year_type_reference
        if school_year_type_reference is not None:
            self.school_year_type_reference = school_year_type_reference
        self.teacher_candidate_reference = teacher_candidate_reference
        self.teacher_preparation_provider_reference = teacher_preparation_provider_reference
        if entry_type_descriptor is not None:
            self.entry_type_descriptor = entry_type_descriptor
        if exit_withdraw_date is not None:
            self.exit_withdraw_date = exit_withdraw_date
        if exit_withdraw_type_descriptor is not None:
            self.exit_withdraw_type_descriptor = exit_withdraw_type_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.

          # noqa: E501

        :param id: The id of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def entry_date(self):
        """Gets the entry_date of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501

        Entry date for the association  # noqa: E501

        :return: The entry_date of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: date
        """
        return self._entry_date

    @entry_date.setter
    def entry_date(self, entry_date):
        """Sets the entry_date of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.

        Entry date for the association  # noqa: E501

        :param entry_date: The entry_date of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and entry_date is None:
            raise ValueError("Invalid value for `entry_date`, must not be `None`")  # noqa: E501

        self._entry_date = entry_date

    @property
    def class_of_school_year_type_reference(self):
        """Gets the class_of_school_year_type_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501


        :return: The class_of_school_year_type_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: EdFiSchoolYearTypeReference
        """
        return self._class_of_school_year_type_reference

    @class_of_school_year_type_reference.setter
    def class_of_school_year_type_reference(self, class_of_school_year_type_reference):
        """Sets the class_of_school_year_type_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.


        :param class_of_school_year_type_reference: The class_of_school_year_type_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :type: EdFiSchoolYearTypeReference
        """

        self._class_of_school_year_type_reference = class_of_school_year_type_reference

    @property
    def school_year_type_reference(self):
        """Gets the school_year_type_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501


        :return: The school_year_type_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: EdFiSchoolYearTypeReference
        """
        return self._school_year_type_reference

    @school_year_type_reference.setter
    def school_year_type_reference(self, school_year_type_reference):
        """Sets the school_year_type_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.


        :param school_year_type_reference: The school_year_type_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :type: EdFiSchoolYearTypeReference
        """

        self._school_year_type_reference = school_year_type_reference

    @property
    def teacher_candidate_reference(self):
        """Gets the teacher_candidate_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501


        :return: The teacher_candidate_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: TpdmTeacherCandidateReference
        """
        return self._teacher_candidate_reference

    @teacher_candidate_reference.setter
    def teacher_candidate_reference(self, teacher_candidate_reference):
        """Sets the teacher_candidate_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.


        :param teacher_candidate_reference: The teacher_candidate_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :type: TpdmTeacherCandidateReference
        """
        if self._configuration.client_side_validation and teacher_candidate_reference is None:
            raise ValueError("Invalid value for `teacher_candidate_reference`, must not be `None`")  # noqa: E501

        self._teacher_candidate_reference = teacher_candidate_reference

    @property
    def teacher_preparation_provider_reference(self):
        """Gets the teacher_preparation_provider_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501


        :return: The teacher_preparation_provider_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: TpdmTeacherPreparationProviderReference
        """
        return self._teacher_preparation_provider_reference

    @teacher_preparation_provider_reference.setter
    def teacher_preparation_provider_reference(self, teacher_preparation_provider_reference):
        """Sets the teacher_preparation_provider_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.


        :param teacher_preparation_provider_reference: The teacher_preparation_provider_reference of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :type: TpdmTeacherPreparationProviderReference
        """
        if self._configuration.client_side_validation and teacher_preparation_provider_reference is None:
            raise ValueError("Invalid value for `teacher_preparation_provider_reference`, must not be `None`")  # noqa: E501

        self._teacher_preparation_provider_reference = teacher_preparation_provider_reference

    @property
    def entry_type_descriptor(self):
        """Gets the entry_type_descriptor of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501

        Entry Type for the association  # noqa: E501

        :return: The entry_type_descriptor of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: str
        """
        return self._entry_type_descriptor

    @entry_type_descriptor.setter
    def entry_type_descriptor(self, entry_type_descriptor):
        """Sets the entry_type_descriptor of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.

        Entry Type for the association  # noqa: E501

        :param entry_type_descriptor: The entry_type_descriptor of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                entry_type_descriptor is not None and len(entry_type_descriptor) > 306):
            raise ValueError("Invalid value for `entry_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._entry_type_descriptor = entry_type_descriptor

    @property
    def exit_withdraw_date(self):
        """Gets the exit_withdraw_date of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501

        Exit date for the association  # noqa: E501

        :return: The exit_withdraw_date of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: date
        """
        return self._exit_withdraw_date

    @exit_withdraw_date.setter
    def exit_withdraw_date(self, exit_withdraw_date):
        """Sets the exit_withdraw_date of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.

        Exit date for the association  # noqa: E501

        :param exit_withdraw_date: The exit_withdraw_date of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :type: date
        """

        self._exit_withdraw_date = exit_withdraw_date

    @property
    def exit_withdraw_type_descriptor(self):
        """Gets the exit_withdraw_type_descriptor of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501

        Exit type for the association  # noqa: E501

        :return: The exit_withdraw_type_descriptor of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: str
        """
        return self._exit_withdraw_type_descriptor

    @exit_withdraw_type_descriptor.setter
    def exit_withdraw_type_descriptor(self, exit_withdraw_type_descriptor):
        """Sets the exit_withdraw_type_descriptor of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.

        Exit type for the association  # noqa: E501

        :param exit_withdraw_type_descriptor: The exit_withdraw_type_descriptor of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                exit_withdraw_type_descriptor is not None and len(exit_withdraw_type_descriptor) > 306):
            raise ValueError("Invalid value for `exit_withdraw_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._exit_withdraw_type_descriptor = exit_withdraw_type_descriptor

    @property
    def etag(self):
        """Gets the etag of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmTeacherCandidateTeacherPreparationProviderAssociation.  # noqa: E501
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
        if issubclass(TpdmTeacherCandidateTeacherPreparationProviderAssociation, dict):
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
        if not isinstance(other, TpdmTeacherCandidateTeacherPreparationProviderAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmTeacherCandidateTeacherPreparationProviderAssociation):
            return True

        return self.to_dict() != other.to_dict()
