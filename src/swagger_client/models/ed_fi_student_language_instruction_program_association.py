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


class EdFiStudentLanguageInstructionProgramAssociation(object):
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
        'education_organization_reference': 'EdFiEducationOrganizationReference',
        'program_reference': 'EdFiProgramReference',
        'student_reference': 'EdFiStudentReference',
        'dosage': 'int',
        'end_date': 'date',
        'english_language_proficiency_assessments': 'list[EdFiStudentLanguageInstructionProgramAssociationEnglishLanguageProficiencyAssessment]',
        'english_learner_participation': 'bool',
        'language_instruction_program_services': 'list[EdFiStudentLanguageInstructionProgramAssociationLanguageInstructionProgramService]',
        'participation_status': 'EdFiGeneralStudentProgramAssociationParticipationStatus',
        'reason_exited_descriptor': 'str',
        'served_outside_of_regular_session': 'bool',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'begin_date': 'beginDate',
        'education_organization_reference': 'educationOrganizationReference',
        'program_reference': 'programReference',
        'student_reference': 'studentReference',
        'dosage': 'dosage',
        'end_date': 'endDate',
        'english_language_proficiency_assessments': 'englishLanguageProficiencyAssessments',
        'english_learner_participation': 'englishLearnerParticipation',
        'language_instruction_program_services': 'languageInstructionProgramServices',
        'participation_status': 'participationStatus',
        'reason_exited_descriptor': 'reasonExitedDescriptor',
        'served_outside_of_regular_session': 'servedOutsideOfRegularSession',
        'etag': '_etag'
    }

    def __init__(self, id=None, begin_date=None, education_organization_reference=None, program_reference=None, student_reference=None, dosage=None, end_date=None, english_language_proficiency_assessments=None, english_learner_participation=None, language_instruction_program_services=None, participation_status=None, reason_exited_descriptor=None, served_outside_of_regular_session=None, etag=None):  # noqa: E501
        """EdFiStudentLanguageInstructionProgramAssociation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._begin_date = None
        self._education_organization_reference = None
        self._program_reference = None
        self._student_reference = None
        self._dosage = None
        self._end_date = None
        self._english_language_proficiency_assessments = None
        self._english_learner_participation = None
        self._language_instruction_program_services = None
        self._participation_status = None
        self._reason_exited_descriptor = None
        self._served_outside_of_regular_session = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.begin_date = begin_date
        self.education_organization_reference = education_organization_reference
        self.program_reference = program_reference
        self.student_reference = student_reference
        if dosage is not None:
            self.dosage = dosage
        if end_date is not None:
            self.end_date = end_date
        if english_language_proficiency_assessments is not None:
            self.english_language_proficiency_assessments = english_language_proficiency_assessments
        if english_learner_participation is not None:
            self.english_learner_participation = english_learner_participation
        if language_instruction_program_services is not None:
            self.language_instruction_program_services = language_instruction_program_services
        if participation_status is not None:
            self.participation_status = participation_status
        if reason_exited_descriptor is not None:
            self.reason_exited_descriptor = reason_exited_descriptor
        if served_outside_of_regular_session is not None:
            self.served_outside_of_regular_session = served_outside_of_regular_session
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentLanguageInstructionProgramAssociation.

          # noqa: E501

        :param id: The id of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501

        The earliest date the student is involved with the program. Typically, this is the date the student becomes eligible for the program.  # noqa: E501

        :return: The begin_date of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiStudentLanguageInstructionProgramAssociation.

        The earliest date the student is involved with the program. Typically, this is the date the student becomes eligible for the program.  # noqa: E501

        :param begin_date: The begin_date of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: date
        """
        if begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501


        :return: The education_organization_reference of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiStudentLanguageInstructionProgramAssociation.


        :param education_organization_reference: The education_organization_reference of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def program_reference(self):
        """Gets the program_reference of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501


        :return: The program_reference of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: EdFiProgramReference
        """
        return self._program_reference

    @program_reference.setter
    def program_reference(self, program_reference):
        """Sets the program_reference of this EdFiStudentLanguageInstructionProgramAssociation.


        :param program_reference: The program_reference of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: EdFiProgramReference
        """
        if program_reference is None:
            raise ValueError("Invalid value for `program_reference`, must not be `None`")  # noqa: E501

        self._program_reference = program_reference

    @property
    def student_reference(self):
        """Gets the student_reference of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501


        :return: The student_reference of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this EdFiStudentLanguageInstructionProgramAssociation.


        :param student_reference: The student_reference of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: EdFiStudentReference
        """
        if student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def dosage(self):
        """Gets the dosage of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501

        The duration of time in minutes for which the student was assigned to participate in the program.  # noqa: E501

        :return: The dosage of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: int
        """
        return self._dosage

    @dosage.setter
    def dosage(self, dosage):
        """Sets the dosage of this EdFiStudentLanguageInstructionProgramAssociation.

        The duration of time in minutes for which the student was assigned to participate in the program.  # noqa: E501

        :param dosage: The dosage of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: int
        """

        self._dosage = dosage

    @property
    def end_date(self):
        """Gets the end_date of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501

        The month, day, and year on which the Student exited the Program or stopped receiving services.  # noqa: E501

        :return: The end_date of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EdFiStudentLanguageInstructionProgramAssociation.

        The month, day, and year on which the Student exited the Program or stopped receiving services.  # noqa: E501

        :param end_date: The end_date of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def english_language_proficiency_assessments(self):
        """Gets the english_language_proficiency_assessments of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501

        An unordered collection of studentLanguageInstructionProgramAssociationEnglishLanguageProficiencyAssessments. Results of yearly English language assessment.  # noqa: E501

        :return: The english_language_proficiency_assessments of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: list[EdFiStudentLanguageInstructionProgramAssociationEnglishLanguageProficiencyAssessment]
        """
        return self._english_language_proficiency_assessments

    @english_language_proficiency_assessments.setter
    def english_language_proficiency_assessments(self, english_language_proficiency_assessments):
        """Sets the english_language_proficiency_assessments of this EdFiStudentLanguageInstructionProgramAssociation.

        An unordered collection of studentLanguageInstructionProgramAssociationEnglishLanguageProficiencyAssessments. Results of yearly English language assessment.  # noqa: E501

        :param english_language_proficiency_assessments: The english_language_proficiency_assessments of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: list[EdFiStudentLanguageInstructionProgramAssociationEnglishLanguageProficiencyAssessment]
        """

        self._english_language_proficiency_assessments = english_language_proficiency_assessments

    @property
    def english_learner_participation(self):
        """Gets the english_learner_participation of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501

        An indication that an English Learner student is served by an English language instruction educational program supported with Title III of ESEA funds.  # noqa: E501

        :return: The english_learner_participation of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._english_learner_participation

    @english_learner_participation.setter
    def english_learner_participation(self, english_learner_participation):
        """Sets the english_learner_participation of this EdFiStudentLanguageInstructionProgramAssociation.

        An indication that an English Learner student is served by an English language instruction educational program supported with Title III of ESEA funds.  # noqa: E501

        :param english_learner_participation: The english_learner_participation of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: bool
        """

        self._english_learner_participation = english_learner_participation

    @property
    def language_instruction_program_services(self):
        """Gets the language_instruction_program_services of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501

        An unordered collection of studentLanguageInstructionProgramAssociationLanguageInstructionProgramServices. Indicates the service(s) being provided to the Student by the Language Instruction Program.  # noqa: E501

        :return: The language_instruction_program_services of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: list[EdFiStudentLanguageInstructionProgramAssociationLanguageInstructionProgramService]
        """
        return self._language_instruction_program_services

    @language_instruction_program_services.setter
    def language_instruction_program_services(self, language_instruction_program_services):
        """Sets the language_instruction_program_services of this EdFiStudentLanguageInstructionProgramAssociation.

        An unordered collection of studentLanguageInstructionProgramAssociationLanguageInstructionProgramServices. Indicates the service(s) being provided to the Student by the Language Instruction Program.  # noqa: E501

        :param language_instruction_program_services: The language_instruction_program_services of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: list[EdFiStudentLanguageInstructionProgramAssociationLanguageInstructionProgramService]
        """

        self._language_instruction_program_services = language_instruction_program_services

    @property
    def participation_status(self):
        """Gets the participation_status of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501


        :return: The participation_status of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: EdFiGeneralStudentProgramAssociationParticipationStatus
        """
        return self._participation_status

    @participation_status.setter
    def participation_status(self, participation_status):
        """Sets the participation_status of this EdFiStudentLanguageInstructionProgramAssociation.


        :param participation_status: The participation_status of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: EdFiGeneralStudentProgramAssociationParticipationStatus
        """

        self._participation_status = participation_status

    @property
    def reason_exited_descriptor(self):
        """Gets the reason_exited_descriptor of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501

        The reason the child left the Program within a school or district.  # noqa: E501

        :return: The reason_exited_descriptor of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._reason_exited_descriptor

    @reason_exited_descriptor.setter
    def reason_exited_descriptor(self, reason_exited_descriptor):
        """Sets the reason_exited_descriptor of this EdFiStudentLanguageInstructionProgramAssociation.

        The reason the child left the Program within a school or district.  # noqa: E501

        :param reason_exited_descriptor: The reason_exited_descriptor of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: str
        """
        if reason_exited_descriptor is not None and len(reason_exited_descriptor) > 306:
            raise ValueError("Invalid value for `reason_exited_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._reason_exited_descriptor = reason_exited_descriptor

    @property
    def served_outside_of_regular_session(self):
        """Gets the served_outside_of_regular_session of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501

        Indicates whether the Student received services during the summer session or between sessions.  # noqa: E501

        :return: The served_outside_of_regular_session of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._served_outside_of_regular_session

    @served_outside_of_regular_session.setter
    def served_outside_of_regular_session(self, served_outside_of_regular_session):
        """Sets the served_outside_of_regular_session of this EdFiStudentLanguageInstructionProgramAssociation.

        Indicates whether the Student received services during the summer session or between sessions.  # noqa: E501

        :param served_outside_of_regular_session: The served_outside_of_regular_session of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :type: bool
        """

        self._served_outside_of_regular_session = served_outside_of_regular_session

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentLanguageInstructionProgramAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentLanguageInstructionProgramAssociation.  # noqa: E501
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
        if issubclass(EdFiStudentLanguageInstructionProgramAssociation, dict):
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
        if not isinstance(other, EdFiStudentLanguageInstructionProgramAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
