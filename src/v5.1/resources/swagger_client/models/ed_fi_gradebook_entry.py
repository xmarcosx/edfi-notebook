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


class EdFiGradebookEntry(object):
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
        'date_assigned': 'date',
        'gradebook_entry_title': 'str',
        'grading_period_reference': 'EdFiGradingPeriodReference',
        'section_reference': 'EdFiSectionReference',
        'description': 'str',
        'due_date': 'date',
        'gradebook_entry_type_descriptor': 'str',
        'learning_objectives': 'list[EdFiGradebookEntryLearningObjective]',
        'learning_standards': 'list[EdFiGradebookEntryLearningStandard]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'date_assigned': 'dateAssigned',
        'gradebook_entry_title': 'gradebookEntryTitle',
        'grading_period_reference': 'gradingPeriodReference',
        'section_reference': 'sectionReference',
        'description': 'description',
        'due_date': 'dueDate',
        'gradebook_entry_type_descriptor': 'gradebookEntryTypeDescriptor',
        'learning_objectives': 'learningObjectives',
        'learning_standards': 'learningStandards',
        'etag': '_etag'
    }

    def __init__(self, id=None, date_assigned=None, gradebook_entry_title=None, grading_period_reference=None, section_reference=None, description=None, due_date=None, gradebook_entry_type_descriptor=None, learning_objectives=None, learning_standards=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiGradebookEntry - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._date_assigned = None
        self._gradebook_entry_title = None
        self._grading_period_reference = None
        self._section_reference = None
        self._description = None
        self._due_date = None
        self._gradebook_entry_type_descriptor = None
        self._learning_objectives = None
        self._learning_standards = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.date_assigned = date_assigned
        self.gradebook_entry_title = gradebook_entry_title
        if grading_period_reference is not None:
            self.grading_period_reference = grading_period_reference
        self.section_reference = section_reference
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if gradebook_entry_type_descriptor is not None:
            self.gradebook_entry_type_descriptor = gradebook_entry_type_descriptor
        if learning_objectives is not None:
            self.learning_objectives = learning_objectives
        if learning_standards is not None:
            self.learning_standards = learning_standards
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiGradebookEntry.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiGradebookEntry.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiGradebookEntry.

          # noqa: E501

        :param id: The id of this EdFiGradebookEntry.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_assigned(self):
        """Gets the date_assigned of this EdFiGradebookEntry.  # noqa: E501

        The date the assignment, homework, or assessment was assigned or executed.  # noqa: E501

        :return: The date_assigned of this EdFiGradebookEntry.  # noqa: E501
        :rtype: date
        """
        return self._date_assigned

    @date_assigned.setter
    def date_assigned(self, date_assigned):
        """Sets the date_assigned of this EdFiGradebookEntry.

        The date the assignment, homework, or assessment was assigned or executed.  # noqa: E501

        :param date_assigned: The date_assigned of this EdFiGradebookEntry.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and date_assigned is None:
            raise ValueError("Invalid value for `date_assigned`, must not be `None`")  # noqa: E501

        self._date_assigned = date_assigned

    @property
    def gradebook_entry_title(self):
        """Gets the gradebook_entry_title of this EdFiGradebookEntry.  # noqa: E501

        The name or title of the activity to be recorded in the GradebookEntry.  # noqa: E501

        :return: The gradebook_entry_title of this EdFiGradebookEntry.  # noqa: E501
        :rtype: str
        """
        return self._gradebook_entry_title

    @gradebook_entry_title.setter
    def gradebook_entry_title(self, gradebook_entry_title):
        """Sets the gradebook_entry_title of this EdFiGradebookEntry.

        The name or title of the activity to be recorded in the GradebookEntry.  # noqa: E501

        :param gradebook_entry_title: The gradebook_entry_title of this EdFiGradebookEntry.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and gradebook_entry_title is None:
            raise ValueError("Invalid value for `gradebook_entry_title`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                gradebook_entry_title is not None and len(gradebook_entry_title) > 60):
            raise ValueError("Invalid value for `gradebook_entry_title`, length must be less than or equal to `60`")  # noqa: E501

        self._gradebook_entry_title = gradebook_entry_title

    @property
    def grading_period_reference(self):
        """Gets the grading_period_reference of this EdFiGradebookEntry.  # noqa: E501


        :return: The grading_period_reference of this EdFiGradebookEntry.  # noqa: E501
        :rtype: EdFiGradingPeriodReference
        """
        return self._grading_period_reference

    @grading_period_reference.setter
    def grading_period_reference(self, grading_period_reference):
        """Sets the grading_period_reference of this EdFiGradebookEntry.


        :param grading_period_reference: The grading_period_reference of this EdFiGradebookEntry.  # noqa: E501
        :type: EdFiGradingPeriodReference
        """

        self._grading_period_reference = grading_period_reference

    @property
    def section_reference(self):
        """Gets the section_reference of this EdFiGradebookEntry.  # noqa: E501


        :return: The section_reference of this EdFiGradebookEntry.  # noqa: E501
        :rtype: EdFiSectionReference
        """
        return self._section_reference

    @section_reference.setter
    def section_reference(self, section_reference):
        """Sets the section_reference of this EdFiGradebookEntry.


        :param section_reference: The section_reference of this EdFiGradebookEntry.  # noqa: E501
        :type: EdFiSectionReference
        """
        if self._configuration.client_side_validation and section_reference is None:
            raise ValueError("Invalid value for `section_reference`, must not be `None`")  # noqa: E501

        self._section_reference = section_reference

    @property
    def description(self):
        """Gets the description of this EdFiGradebookEntry.  # noqa: E501

        A description of the assignment, homework, or classroom assessment.  # noqa: E501

        :return: The description of this EdFiGradebookEntry.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdFiGradebookEntry.

        A description of the assignment, homework, or classroom assessment.  # noqa: E501

        :param description: The description of this EdFiGradebookEntry.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def due_date(self):
        """Gets the due_date of this EdFiGradebookEntry.  # noqa: E501

        The date the assignment, homework, or assessment is due.  # noqa: E501

        :return: The due_date of this EdFiGradebookEntry.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this EdFiGradebookEntry.

        The date the assignment, homework, or assessment is due.  # noqa: E501

        :param due_date: The due_date of this EdFiGradebookEntry.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def gradebook_entry_type_descriptor(self):
        """Gets the gradebook_entry_type_descriptor of this EdFiGradebookEntry.  # noqa: E501

        The type of the GradebookEntry; for example, homework, assignment, quiz, unit test, oral presentation, etc.  # noqa: E501

        :return: The gradebook_entry_type_descriptor of this EdFiGradebookEntry.  # noqa: E501
        :rtype: str
        """
        return self._gradebook_entry_type_descriptor

    @gradebook_entry_type_descriptor.setter
    def gradebook_entry_type_descriptor(self, gradebook_entry_type_descriptor):
        """Sets the gradebook_entry_type_descriptor of this EdFiGradebookEntry.

        The type of the GradebookEntry; for example, homework, assignment, quiz, unit test, oral presentation, etc.  # noqa: E501

        :param gradebook_entry_type_descriptor: The gradebook_entry_type_descriptor of this EdFiGradebookEntry.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                gradebook_entry_type_descriptor is not None and len(gradebook_entry_type_descriptor) > 306):
            raise ValueError("Invalid value for `gradebook_entry_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._gradebook_entry_type_descriptor = gradebook_entry_type_descriptor

    @property
    def learning_objectives(self):
        """Gets the learning_objectives of this EdFiGradebookEntry.  # noqa: E501

        An unordered collection of gradebookEntryLearningObjectives. LearningObjectives associated with the GradebookEntry.  # noqa: E501

        :return: The learning_objectives of this EdFiGradebookEntry.  # noqa: E501
        :rtype: list[EdFiGradebookEntryLearningObjective]
        """
        return self._learning_objectives

    @learning_objectives.setter
    def learning_objectives(self, learning_objectives):
        """Sets the learning_objectives of this EdFiGradebookEntry.

        An unordered collection of gradebookEntryLearningObjectives. LearningObjectives associated with the GradebookEntry.  # noqa: E501

        :param learning_objectives: The learning_objectives of this EdFiGradebookEntry.  # noqa: E501
        :type: list[EdFiGradebookEntryLearningObjective]
        """

        self._learning_objectives = learning_objectives

    @property
    def learning_standards(self):
        """Gets the learning_standards of this EdFiGradebookEntry.  # noqa: E501

        An unordered collection of gradebookEntryLearningStandards. LearningStandard(s) associated with the GradebookEntry.  # noqa: E501

        :return: The learning_standards of this EdFiGradebookEntry.  # noqa: E501
        :rtype: list[EdFiGradebookEntryLearningStandard]
        """
        return self._learning_standards

    @learning_standards.setter
    def learning_standards(self, learning_standards):
        """Sets the learning_standards of this EdFiGradebookEntry.

        An unordered collection of gradebookEntryLearningStandards. LearningStandard(s) associated with the GradebookEntry.  # noqa: E501

        :param learning_standards: The learning_standards of this EdFiGradebookEntry.  # noqa: E501
        :type: list[EdFiGradebookEntryLearningStandard]
        """

        self._learning_standards = learning_standards

    @property
    def etag(self):
        """Gets the etag of this EdFiGradebookEntry.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiGradebookEntry.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiGradebookEntry.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiGradebookEntry.  # noqa: E501
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
        if issubclass(EdFiGradebookEntry, dict):
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
        if not isinstance(other, EdFiGradebookEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiGradebookEntry):
            return True

        return self.to_dict() != other.to_dict()
