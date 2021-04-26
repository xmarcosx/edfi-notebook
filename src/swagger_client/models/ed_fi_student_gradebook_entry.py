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


class EdFiStudentGradebookEntry(object):
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
        'gradebook_entry_reference': 'EdFiGradebookEntryReference',
        'student_section_association_reference': 'EdFiStudentSectionAssociationReference',
        'competency_level_descriptor': 'str',
        'date_fulfilled': 'date',
        'diagnostic_statement': 'str',
        'letter_grade_earned': 'str',
        'numeric_grade_earned': 'float',
        'etag': 'str',
        'ext': 'StudentGradebookEntryExtensions'
    }

    attribute_map = {
        'id': 'id',
        'gradebook_entry_reference': 'gradebookEntryReference',
        'student_section_association_reference': 'studentSectionAssociationReference',
        'competency_level_descriptor': 'competencyLevelDescriptor',
        'date_fulfilled': 'dateFulfilled',
        'diagnostic_statement': 'diagnosticStatement',
        'letter_grade_earned': 'letterGradeEarned',
        'numeric_grade_earned': 'numericGradeEarned',
        'etag': '_etag',
        'ext': '_ext'
    }

    def __init__(self, id=None, gradebook_entry_reference=None, student_section_association_reference=None, competency_level_descriptor=None, date_fulfilled=None, diagnostic_statement=None, letter_grade_earned=None, numeric_grade_earned=None, etag=None, ext=None):  # noqa: E501
        """EdFiStudentGradebookEntry - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._gradebook_entry_reference = None
        self._student_section_association_reference = None
        self._competency_level_descriptor = None
        self._date_fulfilled = None
        self._diagnostic_statement = None
        self._letter_grade_earned = None
        self._numeric_grade_earned = None
        self._etag = None
        self._ext = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.gradebook_entry_reference = gradebook_entry_reference
        self.student_section_association_reference = student_section_association_reference
        if competency_level_descriptor is not None:
            self.competency_level_descriptor = competency_level_descriptor
        if date_fulfilled is not None:
            self.date_fulfilled = date_fulfilled
        if diagnostic_statement is not None:
            self.diagnostic_statement = diagnostic_statement
        if letter_grade_earned is not None:
            self.letter_grade_earned = letter_grade_earned
        if numeric_grade_earned is not None:
            self.numeric_grade_earned = numeric_grade_earned
        if etag is not None:
            self.etag = etag
        if ext is not None:
            self.ext = ext

    @property
    def id(self):
        """Gets the id of this EdFiStudentGradebookEntry.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentGradebookEntry.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentGradebookEntry.

          # noqa: E501

        :param id: The id of this EdFiStudentGradebookEntry.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def gradebook_entry_reference(self):
        """Gets the gradebook_entry_reference of this EdFiStudentGradebookEntry.  # noqa: E501


        :return: The gradebook_entry_reference of this EdFiStudentGradebookEntry.  # noqa: E501
        :rtype: EdFiGradebookEntryReference
        """
        return self._gradebook_entry_reference

    @gradebook_entry_reference.setter
    def gradebook_entry_reference(self, gradebook_entry_reference):
        """Sets the gradebook_entry_reference of this EdFiStudentGradebookEntry.


        :param gradebook_entry_reference: The gradebook_entry_reference of this EdFiStudentGradebookEntry.  # noqa: E501
        :type: EdFiGradebookEntryReference
        """
        if gradebook_entry_reference is None:
            raise ValueError("Invalid value for `gradebook_entry_reference`, must not be `None`")  # noqa: E501

        self._gradebook_entry_reference = gradebook_entry_reference

    @property
    def student_section_association_reference(self):
        """Gets the student_section_association_reference of this EdFiStudentGradebookEntry.  # noqa: E501


        :return: The student_section_association_reference of this EdFiStudentGradebookEntry.  # noqa: E501
        :rtype: EdFiStudentSectionAssociationReference
        """
        return self._student_section_association_reference

    @student_section_association_reference.setter
    def student_section_association_reference(self, student_section_association_reference):
        """Sets the student_section_association_reference of this EdFiStudentGradebookEntry.


        :param student_section_association_reference: The student_section_association_reference of this EdFiStudentGradebookEntry.  # noqa: E501
        :type: EdFiStudentSectionAssociationReference
        """
        if student_section_association_reference is None:
            raise ValueError("Invalid value for `student_section_association_reference`, must not be `None`")  # noqa: E501

        self._student_section_association_reference = student_section_association_reference

    @property
    def competency_level_descriptor(self):
        """Gets the competency_level_descriptor of this EdFiStudentGradebookEntry.  # noqa: E501

        The CompetencyLevel assessed for the student for the referenced LearningObjective.  # noqa: E501

        :return: The competency_level_descriptor of this EdFiStudentGradebookEntry.  # noqa: E501
        :rtype: str
        """
        return self._competency_level_descriptor

    @competency_level_descriptor.setter
    def competency_level_descriptor(self, competency_level_descriptor):
        """Sets the competency_level_descriptor of this EdFiStudentGradebookEntry.

        The CompetencyLevel assessed for the student for the referenced LearningObjective.  # noqa: E501

        :param competency_level_descriptor: The competency_level_descriptor of this EdFiStudentGradebookEntry.  # noqa: E501
        :type: str
        """
        if competency_level_descriptor is not None and len(competency_level_descriptor) > 306:
            raise ValueError("Invalid value for `competency_level_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._competency_level_descriptor = competency_level_descriptor

    @property
    def date_fulfilled(self):
        """Gets the date_fulfilled of this EdFiStudentGradebookEntry.  # noqa: E501

        The date an assignment was turned in or the date of an assessment.  # noqa: E501

        :return: The date_fulfilled of this EdFiStudentGradebookEntry.  # noqa: E501
        :rtype: date
        """
        return self._date_fulfilled

    @date_fulfilled.setter
    def date_fulfilled(self, date_fulfilled):
        """Sets the date_fulfilled of this EdFiStudentGradebookEntry.

        The date an assignment was turned in or the date of an assessment.  # noqa: E501

        :param date_fulfilled: The date_fulfilled of this EdFiStudentGradebookEntry.  # noqa: E501
        :type: date
        """

        self._date_fulfilled = date_fulfilled

    @property
    def diagnostic_statement(self):
        """Gets the diagnostic_statement of this EdFiStudentGradebookEntry.  # noqa: E501

        A statement provided by the teacher that provides information in addition to the grade or assessment score.  # noqa: E501

        :return: The diagnostic_statement of this EdFiStudentGradebookEntry.  # noqa: E501
        :rtype: str
        """
        return self._diagnostic_statement

    @diagnostic_statement.setter
    def diagnostic_statement(self, diagnostic_statement):
        """Sets the diagnostic_statement of this EdFiStudentGradebookEntry.

        A statement provided by the teacher that provides information in addition to the grade or assessment score.  # noqa: E501

        :param diagnostic_statement: The diagnostic_statement of this EdFiStudentGradebookEntry.  # noqa: E501
        :type: str
        """
        if diagnostic_statement is not None and len(diagnostic_statement) > 1024:
            raise ValueError("Invalid value for `diagnostic_statement`, length must be less than or equal to `1024`")  # noqa: E501

        self._diagnostic_statement = diagnostic_statement

    @property
    def letter_grade_earned(self):
        """Gets the letter_grade_earned of this EdFiStudentGradebookEntry.  # noqa: E501

        A final or interim (grading period) indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :return: The letter_grade_earned of this EdFiStudentGradebookEntry.  # noqa: E501
        :rtype: str
        """
        return self._letter_grade_earned

    @letter_grade_earned.setter
    def letter_grade_earned(self, letter_grade_earned):
        """Sets the letter_grade_earned of this EdFiStudentGradebookEntry.

        A final or interim (grading period) indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :param letter_grade_earned: The letter_grade_earned of this EdFiStudentGradebookEntry.  # noqa: E501
        :type: str
        """
        if letter_grade_earned is not None and len(letter_grade_earned) > 20:
            raise ValueError("Invalid value for `letter_grade_earned`, length must be less than or equal to `20`")  # noqa: E501

        self._letter_grade_earned = letter_grade_earned

    @property
    def numeric_grade_earned(self):
        """Gets the numeric_grade_earned of this EdFiStudentGradebookEntry.  # noqa: E501

        A final or interim (grading period) indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :return: The numeric_grade_earned of this EdFiStudentGradebookEntry.  # noqa: E501
        :rtype: float
        """
        return self._numeric_grade_earned

    @numeric_grade_earned.setter
    def numeric_grade_earned(self, numeric_grade_earned):
        """Sets the numeric_grade_earned of this EdFiStudentGradebookEntry.

        A final or interim (grading period) indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :param numeric_grade_earned: The numeric_grade_earned of this EdFiStudentGradebookEntry.  # noqa: E501
        :type: float
        """

        self._numeric_grade_earned = numeric_grade_earned

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentGradebookEntry.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentGradebookEntry.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentGradebookEntry.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentGradebookEntry.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def ext(self):
        """Gets the ext of this EdFiStudentGradebookEntry.  # noqa: E501


        :return: The ext of this EdFiStudentGradebookEntry.  # noqa: E501
        :rtype: StudentGradebookEntryExtensions
        """
        return self._ext

    @ext.setter
    def ext(self, ext):
        """Sets the ext of this EdFiStudentGradebookEntry.


        :param ext: The ext of this EdFiStudentGradebookEntry.  # noqa: E501
        :type: StudentGradebookEntryExtensions
        """

        self._ext = ext

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
        if issubclass(EdFiStudentGradebookEntry, dict):
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
        if not isinstance(other, EdFiStudentGradebookEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
