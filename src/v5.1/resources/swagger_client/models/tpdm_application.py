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


class TpdmApplication(object):
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
        'application_identifier': 'str',
        'applicant_reference': 'TpdmApplicantReference',
        'education_organization_reference': 'EdFiEducationOrganizationReference',
        'academic_subject_descriptor': 'str',
        'accepted_date': 'date',
        'application_date': 'date',
        'application_source_descriptor': 'str',
        'application_status_descriptor': 'str',
        'current_employee': 'bool',
        'first_contact_date': 'date',
        'grade_point_averages': 'list[TpdmApplicationGradePointAverage]',
        'highest_completed_level_of_education_descriptor': 'str',
        'highly_qualified_academic_subject_descriptor': 'str',
        'highly_qualified_teacher': 'bool',
        'high_needs_academic_subject_descriptor': 'str',
        'hire_status_descriptor': 'str',
        'hiring_source_descriptor': 'str',
        'open_staff_positions': 'list[TpdmApplicationOpenStaffPosition]',
        'score_results': 'list[TpdmApplicationScoreResult]',
        'terms': 'list[TpdmApplicationTerm]',
        'withdraw_date': 'date',
        'withdraw_reason_descriptor': 'str',
        'years_of_prior_professional_experience': 'float',
        'years_of_prior_teaching_experience': 'float',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'application_identifier': 'applicationIdentifier',
        'applicant_reference': 'applicantReference',
        'education_organization_reference': 'educationOrganizationReference',
        'academic_subject_descriptor': 'academicSubjectDescriptor',
        'accepted_date': 'acceptedDate',
        'application_date': 'applicationDate',
        'application_source_descriptor': 'applicationSourceDescriptor',
        'application_status_descriptor': 'applicationStatusDescriptor',
        'current_employee': 'currentEmployee',
        'first_contact_date': 'firstContactDate',
        'grade_point_averages': 'gradePointAverages',
        'highest_completed_level_of_education_descriptor': 'highestCompletedLevelOfEducationDescriptor',
        'highly_qualified_academic_subject_descriptor': 'highlyQualifiedAcademicSubjectDescriptor',
        'highly_qualified_teacher': 'highlyQualifiedTeacher',
        'high_needs_academic_subject_descriptor': 'highNeedsAcademicSubjectDescriptor',
        'hire_status_descriptor': 'hireStatusDescriptor',
        'hiring_source_descriptor': 'hiringSourceDescriptor',
        'open_staff_positions': 'openStaffPositions',
        'score_results': 'scoreResults',
        'terms': 'terms',
        'withdraw_date': 'withdrawDate',
        'withdraw_reason_descriptor': 'withdrawReasonDescriptor',
        'years_of_prior_professional_experience': 'yearsOfPriorProfessionalExperience',
        'years_of_prior_teaching_experience': 'yearsOfPriorTeachingExperience',
        'etag': '_etag'
    }

    def __init__(self, id=None, application_identifier=None, applicant_reference=None, education_organization_reference=None, academic_subject_descriptor=None, accepted_date=None, application_date=None, application_source_descriptor=None, application_status_descriptor=None, current_employee=None, first_contact_date=None, grade_point_averages=None, highest_completed_level_of_education_descriptor=None, highly_qualified_academic_subject_descriptor=None, highly_qualified_teacher=None, high_needs_academic_subject_descriptor=None, hire_status_descriptor=None, hiring_source_descriptor=None, open_staff_positions=None, score_results=None, terms=None, withdraw_date=None, withdraw_reason_descriptor=None, years_of_prior_professional_experience=None, years_of_prior_teaching_experience=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmApplication - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._application_identifier = None
        self._applicant_reference = None
        self._education_organization_reference = None
        self._academic_subject_descriptor = None
        self._accepted_date = None
        self._application_date = None
        self._application_source_descriptor = None
        self._application_status_descriptor = None
        self._current_employee = None
        self._first_contact_date = None
        self._grade_point_averages = None
        self._highest_completed_level_of_education_descriptor = None
        self._highly_qualified_academic_subject_descriptor = None
        self._highly_qualified_teacher = None
        self._high_needs_academic_subject_descriptor = None
        self._hire_status_descriptor = None
        self._hiring_source_descriptor = None
        self._open_staff_positions = None
        self._score_results = None
        self._terms = None
        self._withdraw_date = None
        self._withdraw_reason_descriptor = None
        self._years_of_prior_professional_experience = None
        self._years_of_prior_teaching_experience = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.application_identifier = application_identifier
        self.applicant_reference = applicant_reference
        self.education_organization_reference = education_organization_reference
        if academic_subject_descriptor is not None:
            self.academic_subject_descriptor = academic_subject_descriptor
        if accepted_date is not None:
            self.accepted_date = accepted_date
        self.application_date = application_date
        if application_source_descriptor is not None:
            self.application_source_descriptor = application_source_descriptor
        self.application_status_descriptor = application_status_descriptor
        if current_employee is not None:
            self.current_employee = current_employee
        if first_contact_date is not None:
            self.first_contact_date = first_contact_date
        if grade_point_averages is not None:
            self.grade_point_averages = grade_point_averages
        if highest_completed_level_of_education_descriptor is not None:
            self.highest_completed_level_of_education_descriptor = highest_completed_level_of_education_descriptor
        if highly_qualified_academic_subject_descriptor is not None:
            self.highly_qualified_academic_subject_descriptor = highly_qualified_academic_subject_descriptor
        if highly_qualified_teacher is not None:
            self.highly_qualified_teacher = highly_qualified_teacher
        if high_needs_academic_subject_descriptor is not None:
            self.high_needs_academic_subject_descriptor = high_needs_academic_subject_descriptor
        if hire_status_descriptor is not None:
            self.hire_status_descriptor = hire_status_descriptor
        if hiring_source_descriptor is not None:
            self.hiring_source_descriptor = hiring_source_descriptor
        if open_staff_positions is not None:
            self.open_staff_positions = open_staff_positions
        if score_results is not None:
            self.score_results = score_results
        if terms is not None:
            self.terms = terms
        if withdraw_date is not None:
            self.withdraw_date = withdraw_date
        if withdraw_reason_descriptor is not None:
            self.withdraw_reason_descriptor = withdraw_reason_descriptor
        if years_of_prior_professional_experience is not None:
            self.years_of_prior_professional_experience = years_of_prior_professional_experience
        if years_of_prior_teaching_experience is not None:
            self.years_of_prior_teaching_experience = years_of_prior_teaching_experience
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmApplication.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmApplication.

          # noqa: E501

        :param id: The id of this TpdmApplication.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def application_identifier(self):
        """Gets the application_identifier of this TpdmApplication.  # noqa: E501

        Identifier assigned to the application for an open staff position.  # noqa: E501

        :return: The application_identifier of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._application_identifier

    @application_identifier.setter
    def application_identifier(self, application_identifier):
        """Sets the application_identifier of this TpdmApplication.

        Identifier assigned to the application for an open staff position.  # noqa: E501

        :param application_identifier: The application_identifier of this TpdmApplication.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and application_identifier is None:
            raise ValueError("Invalid value for `application_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                application_identifier is not None and len(application_identifier) > 20):
            raise ValueError("Invalid value for `application_identifier`, length must be less than or equal to `20`")  # noqa: E501

        self._application_identifier = application_identifier

    @property
    def applicant_reference(self):
        """Gets the applicant_reference of this TpdmApplication.  # noqa: E501


        :return: The applicant_reference of this TpdmApplication.  # noqa: E501
        :rtype: TpdmApplicantReference
        """
        return self._applicant_reference

    @applicant_reference.setter
    def applicant_reference(self, applicant_reference):
        """Sets the applicant_reference of this TpdmApplication.


        :param applicant_reference: The applicant_reference of this TpdmApplication.  # noqa: E501
        :type: TpdmApplicantReference
        """
        if self._configuration.client_side_validation and applicant_reference is None:
            raise ValueError("Invalid value for `applicant_reference`, must not be `None`")  # noqa: E501

        self._applicant_reference = applicant_reference

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this TpdmApplication.  # noqa: E501


        :return: The education_organization_reference of this TpdmApplication.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this TpdmApplication.


        :param education_organization_reference: The education_organization_reference of this TpdmApplication.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if self._configuration.client_side_validation and education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def academic_subject_descriptor(self):
        """Gets the academic_subject_descriptor of this TpdmApplication.  # noqa: E501

        The academic subject for which the application is made.  # noqa: E501

        :return: The academic_subject_descriptor of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._academic_subject_descriptor

    @academic_subject_descriptor.setter
    def academic_subject_descriptor(self, academic_subject_descriptor):
        """Sets the academic_subject_descriptor of this TpdmApplication.

        The academic subject for which the application is made.  # noqa: E501

        :param academic_subject_descriptor: The academic_subject_descriptor of this TpdmApplication.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                academic_subject_descriptor is not None and len(academic_subject_descriptor) > 306):
            raise ValueError("Invalid value for `academic_subject_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._academic_subject_descriptor = academic_subject_descriptor

    @property
    def accepted_date(self):
        """Gets the accepted_date of this TpdmApplication.  # noqa: E501

        The date of job acceptance, if offered.  # noqa: E501

        :return: The accepted_date of this TpdmApplication.  # noqa: E501
        :rtype: date
        """
        return self._accepted_date

    @accepted_date.setter
    def accepted_date(self, accepted_date):
        """Sets the accepted_date of this TpdmApplication.

        The date of job acceptance, if offered.  # noqa: E501

        :param accepted_date: The accepted_date of this TpdmApplication.  # noqa: E501
        :type: date
        """

        self._accepted_date = accepted_date

    @property
    def application_date(self):
        """Gets the application_date of this TpdmApplication.  # noqa: E501

        The month, day, and year the application was submitted.  # noqa: E501

        :return: The application_date of this TpdmApplication.  # noqa: E501
        :rtype: date
        """
        return self._application_date

    @application_date.setter
    def application_date(self, application_date):
        """Sets the application_date of this TpdmApplication.

        The month, day, and year the application was submitted.  # noqa: E501

        :param application_date: The application_date of this TpdmApplication.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and application_date is None:
            raise ValueError("Invalid value for `application_date`, must not be `None`")  # noqa: E501

        self._application_date = application_date

    @property
    def application_source_descriptor(self):
        """Gets the application_source_descriptor of this TpdmApplication.  # noqa: E501

        Specifies the source for the application (e.g., Job fair, website, referral).  # noqa: E501

        :return: The application_source_descriptor of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._application_source_descriptor

    @application_source_descriptor.setter
    def application_source_descriptor(self, application_source_descriptor):
        """Sets the application_source_descriptor of this TpdmApplication.

        Specifies the source for the application (e.g., Job fair, website, referral).  # noqa: E501

        :param application_source_descriptor: The application_source_descriptor of this TpdmApplication.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                application_source_descriptor is not None and len(application_source_descriptor) > 306):
            raise ValueError("Invalid value for `application_source_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._application_source_descriptor = application_source_descriptor

    @property
    def application_status_descriptor(self):
        """Gets the application_status_descriptor of this TpdmApplication.  # noqa: E501

        Indicates the current status of the application (e.g., received, phone screen, interview, awaiting decision, etc.).  # noqa: E501

        :return: The application_status_descriptor of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._application_status_descriptor

    @application_status_descriptor.setter
    def application_status_descriptor(self, application_status_descriptor):
        """Sets the application_status_descriptor of this TpdmApplication.

        Indicates the current status of the application (e.g., received, phone screen, interview, awaiting decision, etc.).  # noqa: E501

        :param application_status_descriptor: The application_status_descriptor of this TpdmApplication.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and application_status_descriptor is None:
            raise ValueError("Invalid value for `application_status_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                application_status_descriptor is not None and len(application_status_descriptor) > 306):
            raise ValueError("Invalid value for `application_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._application_status_descriptor = application_status_descriptor

    @property
    def current_employee(self):
        """Gets the current_employee of this TpdmApplication.  # noqa: E501

        Indicator as to whether the applicant is a current employee of the school district.  # noqa: E501

        :return: The current_employee of this TpdmApplication.  # noqa: E501
        :rtype: bool
        """
        return self._current_employee

    @current_employee.setter
    def current_employee(self, current_employee):
        """Sets the current_employee of this TpdmApplication.

        Indicator as to whether the applicant is a current employee of the school district.  # noqa: E501

        :param current_employee: The current_employee of this TpdmApplication.  # noqa: E501
        :type: bool
        """

        self._current_employee = current_employee

    @property
    def first_contact_date(self):
        """Gets the first_contact_date of this TpdmApplication.  # noqa: E501

        Date applicant was first contacted after submitting application.  # noqa: E501

        :return: The first_contact_date of this TpdmApplication.  # noqa: E501
        :rtype: date
        """
        return self._first_contact_date

    @first_contact_date.setter
    def first_contact_date(self, first_contact_date):
        """Sets the first_contact_date of this TpdmApplication.

        Date applicant was first contacted after submitting application.  # noqa: E501

        :param first_contact_date: The first_contact_date of this TpdmApplication.  # noqa: E501
        :type: date
        """

        self._first_contact_date = first_contact_date

    @property
    def grade_point_averages(self):
        """Gets the grade_point_averages of this TpdmApplication.  # noqa: E501

        An unordered collection of applicationGradePointAverages. Data that provides information on a measure of average performance in a group of courses taken by an individual.  # noqa: E501

        :return: The grade_point_averages of this TpdmApplication.  # noqa: E501
        :rtype: list[TpdmApplicationGradePointAverage]
        """
        return self._grade_point_averages

    @grade_point_averages.setter
    def grade_point_averages(self, grade_point_averages):
        """Sets the grade_point_averages of this TpdmApplication.

        An unordered collection of applicationGradePointAverages. Data that provides information on a measure of average performance in a group of courses taken by an individual.  # noqa: E501

        :param grade_point_averages: The grade_point_averages of this TpdmApplication.  # noqa: E501
        :type: list[TpdmApplicationGradePointAverage]
        """

        self._grade_point_averages = grade_point_averages

    @property
    def highest_completed_level_of_education_descriptor(self):
        """Gets the highest_completed_level_of_education_descriptor of this TpdmApplication.  # noqa: E501

        The extent of formal instruction an individual has received (e.g., the highest grade in school completed or its equivalent or the highest degree received).  # noqa: E501

        :return: The highest_completed_level_of_education_descriptor of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._highest_completed_level_of_education_descriptor

    @highest_completed_level_of_education_descriptor.setter
    def highest_completed_level_of_education_descriptor(self, highest_completed_level_of_education_descriptor):
        """Sets the highest_completed_level_of_education_descriptor of this TpdmApplication.

        The extent of formal instruction an individual has received (e.g., the highest grade in school completed or its equivalent or the highest degree received).  # noqa: E501

        :param highest_completed_level_of_education_descriptor: The highest_completed_level_of_education_descriptor of this TpdmApplication.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                highest_completed_level_of_education_descriptor is not None and len(highest_completed_level_of_education_descriptor) > 306):
            raise ValueError("Invalid value for `highest_completed_level_of_education_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._highest_completed_level_of_education_descriptor = highest_completed_level_of_education_descriptor

    @property
    def highly_qualified_academic_subject_descriptor(self):
        """Gets the highly_qualified_academic_subject_descriptor of this TpdmApplication.  # noqa: E501

        The academic subject(s) in which the staff is deemed to be \"highly qualified\".  # noqa: E501

        :return: The highly_qualified_academic_subject_descriptor of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._highly_qualified_academic_subject_descriptor

    @highly_qualified_academic_subject_descriptor.setter
    def highly_qualified_academic_subject_descriptor(self, highly_qualified_academic_subject_descriptor):
        """Sets the highly_qualified_academic_subject_descriptor of this TpdmApplication.

        The academic subject(s) in which the staff is deemed to be \"highly qualified\".  # noqa: E501

        :param highly_qualified_academic_subject_descriptor: The highly_qualified_academic_subject_descriptor of this TpdmApplication.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                highly_qualified_academic_subject_descriptor is not None and len(highly_qualified_academic_subject_descriptor) > 306):
            raise ValueError("Invalid value for `highly_qualified_academic_subject_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._highly_qualified_academic_subject_descriptor = highly_qualified_academic_subject_descriptor

    @property
    def highly_qualified_teacher(self):
        """Gets the highly_qualified_teacher of this TpdmApplication.  # noqa: E501

        An indication of whether a teacher is classified as highly qualified for his/her assignment according to state definition. This attribute indicates the teacher is highly qualified for ALL Sections being taught.  # noqa: E501

        :return: The highly_qualified_teacher of this TpdmApplication.  # noqa: E501
        :rtype: bool
        """
        return self._highly_qualified_teacher

    @highly_qualified_teacher.setter
    def highly_qualified_teacher(self, highly_qualified_teacher):
        """Sets the highly_qualified_teacher of this TpdmApplication.

        An indication of whether a teacher is classified as highly qualified for his/her assignment according to state definition. This attribute indicates the teacher is highly qualified for ALL Sections being taught.  # noqa: E501

        :param highly_qualified_teacher: The highly_qualified_teacher of this TpdmApplication.  # noqa: E501
        :type: bool
        """

        self._highly_qualified_teacher = highly_qualified_teacher

    @property
    def high_needs_academic_subject_descriptor(self):
        """Gets the high_needs_academic_subject_descriptor of this TpdmApplication.  # noqa: E501

        The high need academic subject for the application, if any.  # noqa: E501

        :return: The high_needs_academic_subject_descriptor of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._high_needs_academic_subject_descriptor

    @high_needs_academic_subject_descriptor.setter
    def high_needs_academic_subject_descriptor(self, high_needs_academic_subject_descriptor):
        """Sets the high_needs_academic_subject_descriptor of this TpdmApplication.

        The high need academic subject for the application, if any.  # noqa: E501

        :param high_needs_academic_subject_descriptor: The high_needs_academic_subject_descriptor of this TpdmApplication.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                high_needs_academic_subject_descriptor is not None and len(high_needs_academic_subject_descriptor) > 306):
            raise ValueError("Invalid value for `high_needs_academic_subject_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._high_needs_academic_subject_descriptor = high_needs_academic_subject_descriptor

    @property
    def hire_status_descriptor(self):
        """Gets the hire_status_descriptor of this TpdmApplication.  # noqa: E501

        Indicates the current status of the application for hire (e.g., applied, recommended, rejected, exited, offered, hired).  # noqa: E501

        :return: The hire_status_descriptor of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._hire_status_descriptor

    @hire_status_descriptor.setter
    def hire_status_descriptor(self, hire_status_descriptor):
        """Sets the hire_status_descriptor of this TpdmApplication.

        Indicates the current status of the application for hire (e.g., applied, recommended, rejected, exited, offered, hired).  # noqa: E501

        :param hire_status_descriptor: The hire_status_descriptor of this TpdmApplication.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                hire_status_descriptor is not None and len(hire_status_descriptor) > 306):
            raise ValueError("Invalid value for `hire_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._hire_status_descriptor = hire_status_descriptor

    @property
    def hiring_source_descriptor(self):
        """Gets the hiring_source_descriptor of this TpdmApplication.  # noqa: E501

        The source for the application (e.g.,job fair, website, referral, etc.).  # noqa: E501

        :return: The hiring_source_descriptor of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._hiring_source_descriptor

    @hiring_source_descriptor.setter
    def hiring_source_descriptor(self, hiring_source_descriptor):
        """Sets the hiring_source_descriptor of this TpdmApplication.

        The source for the application (e.g.,job fair, website, referral, etc.).  # noqa: E501

        :param hiring_source_descriptor: The hiring_source_descriptor of this TpdmApplication.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                hiring_source_descriptor is not None and len(hiring_source_descriptor) > 306):
            raise ValueError("Invalid value for `hiring_source_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._hiring_source_descriptor = hiring_source_descriptor

    @property
    def open_staff_positions(self):
        """Gets the open_staff_positions of this TpdmApplication.  # noqa: E501

        An unordered collection of applicationOpenStaffPositions. The open staff position(s) associated with the application.  # noqa: E501

        :return: The open_staff_positions of this TpdmApplication.  # noqa: E501
        :rtype: list[TpdmApplicationOpenStaffPosition]
        """
        return self._open_staff_positions

    @open_staff_positions.setter
    def open_staff_positions(self, open_staff_positions):
        """Sets the open_staff_positions of this TpdmApplication.

        An unordered collection of applicationOpenStaffPositions. The open staff position(s) associated with the application.  # noqa: E501

        :param open_staff_positions: The open_staff_positions of this TpdmApplication.  # noqa: E501
        :type: list[TpdmApplicationOpenStaffPosition]
        """

        self._open_staff_positions = open_staff_positions

    @property
    def score_results(self):
        """Gets the score_results of this TpdmApplication.  # noqa: E501

        An unordered collection of applicationScoreResults. A meaningful score or statistical expression of the performance of an individual. The results can be expressed as a number, percentile, range, level, etc.  # noqa: E501

        :return: The score_results of this TpdmApplication.  # noqa: E501
        :rtype: list[TpdmApplicationScoreResult]
        """
        return self._score_results

    @score_results.setter
    def score_results(self, score_results):
        """Sets the score_results of this TpdmApplication.

        An unordered collection of applicationScoreResults. A meaningful score or statistical expression of the performance of an individual. The results can be expressed as a number, percentile, range, level, etc.  # noqa: E501

        :param score_results: The score_results of this TpdmApplication.  # noqa: E501
        :type: list[TpdmApplicationScoreResult]
        """

        self._score_results = score_results

    @property
    def terms(self):
        """Gets the terms of this TpdmApplication.  # noqa: E501

        An unordered collection of applicationTerms. The intended term of enrollment for which the application is being submitted.  # noqa: E501

        :return: The terms of this TpdmApplication.  # noqa: E501
        :rtype: list[TpdmApplicationTerm]
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this TpdmApplication.

        An unordered collection of applicationTerms. The intended term of enrollment for which the application is being submitted.  # noqa: E501

        :param terms: The terms of this TpdmApplication.  # noqa: E501
        :type: list[TpdmApplicationTerm]
        """

        self._terms = terms

    @property
    def withdraw_date(self):
        """Gets the withdraw_date of this TpdmApplication.  # noqa: E501

        The date the application was withdrawn by the applicant.  # noqa: E501

        :return: The withdraw_date of this TpdmApplication.  # noqa: E501
        :rtype: date
        """
        return self._withdraw_date

    @withdraw_date.setter
    def withdraw_date(self, withdraw_date):
        """Sets the withdraw_date of this TpdmApplication.

        The date the application was withdrawn by the applicant.  # noqa: E501

        :param withdraw_date: The withdraw_date of this TpdmApplication.  # noqa: E501
        :type: date
        """

        self._withdraw_date = withdraw_date

    @property
    def withdraw_reason_descriptor(self):
        """Gets the withdraw_reason_descriptor of this TpdmApplication.  # noqa: E501

        Reason applicant withdrew application.  # noqa: E501

        :return: The withdraw_reason_descriptor of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_reason_descriptor

    @withdraw_reason_descriptor.setter
    def withdraw_reason_descriptor(self, withdraw_reason_descriptor):
        """Sets the withdraw_reason_descriptor of this TpdmApplication.

        Reason applicant withdrew application.  # noqa: E501

        :param withdraw_reason_descriptor: The withdraw_reason_descriptor of this TpdmApplication.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                withdraw_reason_descriptor is not None and len(withdraw_reason_descriptor) > 306):
            raise ValueError("Invalid value for `withdraw_reason_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._withdraw_reason_descriptor = withdraw_reason_descriptor

    @property
    def years_of_prior_professional_experience(self):
        """Gets the years_of_prior_professional_experience of this TpdmApplication.  # noqa: E501

        The total number of years that an individual has previously held a similar professional position in one or more education institutions.  # noqa: E501

        :return: The years_of_prior_professional_experience of this TpdmApplication.  # noqa: E501
        :rtype: float
        """
        return self._years_of_prior_professional_experience

    @years_of_prior_professional_experience.setter
    def years_of_prior_professional_experience(self, years_of_prior_professional_experience):
        """Sets the years_of_prior_professional_experience of this TpdmApplication.

        The total number of years that an individual has previously held a similar professional position in one or more education institutions.  # noqa: E501

        :param years_of_prior_professional_experience: The years_of_prior_professional_experience of this TpdmApplication.  # noqa: E501
        :type: float
        """

        self._years_of_prior_professional_experience = years_of_prior_professional_experience

    @property
    def years_of_prior_teaching_experience(self):
        """Gets the years_of_prior_teaching_experience of this TpdmApplication.  # noqa: E501

        The total number of years that an individual has previously held a teaching position in one or more education institutions.  # noqa: E501

        :return: The years_of_prior_teaching_experience of this TpdmApplication.  # noqa: E501
        :rtype: float
        """
        return self._years_of_prior_teaching_experience

    @years_of_prior_teaching_experience.setter
    def years_of_prior_teaching_experience(self, years_of_prior_teaching_experience):
        """Sets the years_of_prior_teaching_experience of this TpdmApplication.

        The total number of years that an individual has previously held a teaching position in one or more education institutions.  # noqa: E501

        :param years_of_prior_teaching_experience: The years_of_prior_teaching_experience of this TpdmApplication.  # noqa: E501
        :type: float
        """

        self._years_of_prior_teaching_experience = years_of_prior_teaching_experience

    @property
    def etag(self):
        """Gets the etag of this TpdmApplication.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmApplication.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmApplication.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmApplication.  # noqa: E501
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
        if issubclass(TpdmApplication, dict):
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
        if not isinstance(other, TpdmApplication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmApplication):
            return True

        return self.to_dict() != other.to_dict()
