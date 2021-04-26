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


class TpdmTeacherCandidateCourseTranscript(object):
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
        'course_attempt_result_descriptor': 'str',
        'course_reference': 'EdFiCourseReference',
        'school_reference': 'EdFiSchoolReference',
        'teacher_candidate_academic_record_reference': 'TpdmTeacherCandidateAcademicRecordReference',
        'alternative_course_code': 'str',
        'alternative_course_title': 'str',
        'attempted_credit_conversion': 'float',
        'attempted_credits': 'float',
        'attempted_credit_type_descriptor': 'str',
        'course_repeat_code_descriptor': 'str',
        'course_title': 'str',
        'earned_additional_credits': 'list[TpdmTeacherCandidateCourseTranscriptEarnedAdditionalCredits]',
        'earned_credit_conversion': 'float',
        'earned_credits': 'float',
        'earned_credit_type_descriptor': 'str',
        'final_letter_grade_earned': 'str',
        'final_numeric_grade_earned': 'float',
        'method_credit_earned_descriptor': 'str',
        'when_taken_grade_level_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'course_attempt_result_descriptor': 'courseAttemptResultDescriptor',
        'course_reference': 'courseReference',
        'school_reference': 'schoolReference',
        'teacher_candidate_academic_record_reference': 'teacherCandidateAcademicRecordReference',
        'alternative_course_code': 'alternativeCourseCode',
        'alternative_course_title': 'alternativeCourseTitle',
        'attempted_credit_conversion': 'attemptedCreditConversion',
        'attempted_credits': 'attemptedCredits',
        'attempted_credit_type_descriptor': 'attemptedCreditTypeDescriptor',
        'course_repeat_code_descriptor': 'courseRepeatCodeDescriptor',
        'course_title': 'courseTitle',
        'earned_additional_credits': 'earnedAdditionalCredits',
        'earned_credit_conversion': 'earnedCreditConversion',
        'earned_credits': 'earnedCredits',
        'earned_credit_type_descriptor': 'earnedCreditTypeDescriptor',
        'final_letter_grade_earned': 'finalLetterGradeEarned',
        'final_numeric_grade_earned': 'finalNumericGradeEarned',
        'method_credit_earned_descriptor': 'methodCreditEarnedDescriptor',
        'when_taken_grade_level_descriptor': 'whenTakenGradeLevelDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, course_attempt_result_descriptor=None, course_reference=None, school_reference=None, teacher_candidate_academic_record_reference=None, alternative_course_code=None, alternative_course_title=None, attempted_credit_conversion=None, attempted_credits=None, attempted_credit_type_descriptor=None, course_repeat_code_descriptor=None, course_title=None, earned_additional_credits=None, earned_credit_conversion=None, earned_credits=None, earned_credit_type_descriptor=None, final_letter_grade_earned=None, final_numeric_grade_earned=None, method_credit_earned_descriptor=None, when_taken_grade_level_descriptor=None, etag=None):  # noqa: E501
        """TpdmTeacherCandidateCourseTranscript - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._course_attempt_result_descriptor = None
        self._course_reference = None
        self._school_reference = None
        self._teacher_candidate_academic_record_reference = None
        self._alternative_course_code = None
        self._alternative_course_title = None
        self._attempted_credit_conversion = None
        self._attempted_credits = None
        self._attempted_credit_type_descriptor = None
        self._course_repeat_code_descriptor = None
        self._course_title = None
        self._earned_additional_credits = None
        self._earned_credit_conversion = None
        self._earned_credits = None
        self._earned_credit_type_descriptor = None
        self._final_letter_grade_earned = None
        self._final_numeric_grade_earned = None
        self._method_credit_earned_descriptor = None
        self._when_taken_grade_level_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.course_attempt_result_descriptor = course_attempt_result_descriptor
        self.course_reference = course_reference
        if school_reference is not None:
            self.school_reference = school_reference
        self.teacher_candidate_academic_record_reference = teacher_candidate_academic_record_reference
        if alternative_course_code is not None:
            self.alternative_course_code = alternative_course_code
        if alternative_course_title is not None:
            self.alternative_course_title = alternative_course_title
        if attempted_credit_conversion is not None:
            self.attempted_credit_conversion = attempted_credit_conversion
        if attempted_credits is not None:
            self.attempted_credits = attempted_credits
        if attempted_credit_type_descriptor is not None:
            self.attempted_credit_type_descriptor = attempted_credit_type_descriptor
        if course_repeat_code_descriptor is not None:
            self.course_repeat_code_descriptor = course_repeat_code_descriptor
        if course_title is not None:
            self.course_title = course_title
        if earned_additional_credits is not None:
            self.earned_additional_credits = earned_additional_credits
        if earned_credit_conversion is not None:
            self.earned_credit_conversion = earned_credit_conversion
        self.earned_credits = earned_credits
        if earned_credit_type_descriptor is not None:
            self.earned_credit_type_descriptor = earned_credit_type_descriptor
        if final_letter_grade_earned is not None:
            self.final_letter_grade_earned = final_letter_grade_earned
        if final_numeric_grade_earned is not None:
            self.final_numeric_grade_earned = final_numeric_grade_earned
        if method_credit_earned_descriptor is not None:
            self.method_credit_earned_descriptor = method_credit_earned_descriptor
        if when_taken_grade_level_descriptor is not None:
            self.when_taken_grade_level_descriptor = when_taken_grade_level_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmTeacherCandidateCourseTranscript.

          # noqa: E501

        :param id: The id of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def course_attempt_result_descriptor(self):
        """Gets the course_attempt_result_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The result from the student's attempt to take the course, for example:        Pass        Fail        Incomplete        Withdrawn.  # noqa: E501

        :return: The course_attempt_result_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._course_attempt_result_descriptor

    @course_attempt_result_descriptor.setter
    def course_attempt_result_descriptor(self, course_attempt_result_descriptor):
        """Sets the course_attempt_result_descriptor of this TpdmTeacherCandidateCourseTranscript.

        The result from the student's attempt to take the course, for example:        Pass        Fail        Incomplete        Withdrawn.  # noqa: E501

        :param course_attempt_result_descriptor: The course_attempt_result_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """
        if course_attempt_result_descriptor is None:
            raise ValueError("Invalid value for `course_attempt_result_descriptor`, must not be `None`")  # noqa: E501
        if course_attempt_result_descriptor is not None and len(course_attempt_result_descriptor) > 306:
            raise ValueError("Invalid value for `course_attempt_result_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._course_attempt_result_descriptor = course_attempt_result_descriptor

    @property
    def course_reference(self):
        """Gets the course_reference of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501


        :return: The course_reference of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: EdFiCourseReference
        """
        return self._course_reference

    @course_reference.setter
    def course_reference(self, course_reference):
        """Sets the course_reference of this TpdmTeacherCandidateCourseTranscript.


        :param course_reference: The course_reference of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: EdFiCourseReference
        """
        if course_reference is None:
            raise ValueError("Invalid value for `course_reference`, must not be `None`")  # noqa: E501

        self._course_reference = course_reference

    @property
    def school_reference(self):
        """Gets the school_reference of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501


        :return: The school_reference of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: EdFiSchoolReference
        """
        return self._school_reference

    @school_reference.setter
    def school_reference(self, school_reference):
        """Sets the school_reference of this TpdmTeacherCandidateCourseTranscript.


        :param school_reference: The school_reference of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: EdFiSchoolReference
        """

        self._school_reference = school_reference

    @property
    def teacher_candidate_academic_record_reference(self):
        """Gets the teacher_candidate_academic_record_reference of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501


        :return: The teacher_candidate_academic_record_reference of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: TpdmTeacherCandidateAcademicRecordReference
        """
        return self._teacher_candidate_academic_record_reference

    @teacher_candidate_academic_record_reference.setter
    def teacher_candidate_academic_record_reference(self, teacher_candidate_academic_record_reference):
        """Sets the teacher_candidate_academic_record_reference of this TpdmTeacherCandidateCourseTranscript.


        :param teacher_candidate_academic_record_reference: The teacher_candidate_academic_record_reference of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: TpdmTeacherCandidateAcademicRecordReference
        """
        if teacher_candidate_academic_record_reference is None:
            raise ValueError("Invalid value for `teacher_candidate_academic_record_reference`, must not be `None`")  # noqa: E501

        self._teacher_candidate_academic_record_reference = teacher_candidate_academic_record_reference

    @property
    def alternative_course_code(self):
        """Gets the alternative_course_code of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The local code assigned by the school that identifies the course offering, the code from an external educational organization, or other alternate course code.  # noqa: E501

        :return: The alternative_course_code of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._alternative_course_code

    @alternative_course_code.setter
    def alternative_course_code(self, alternative_course_code):
        """Sets the alternative_course_code of this TpdmTeacherCandidateCourseTranscript.

        The local code assigned by the school that identifies the course offering, the code from an external educational organization, or other alternate course code.  # noqa: E501

        :param alternative_course_code: The alternative_course_code of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """
        if alternative_course_code is not None and len(alternative_course_code) > 60:
            raise ValueError("Invalid value for `alternative_course_code`, length must be less than or equal to `60`")  # noqa: E501

        self._alternative_course_code = alternative_course_code

    @property
    def alternative_course_title(self):
        """Gets the alternative_course_title of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The descriptive name given to a course of study offered in the school, if different from the CourseTitle.  # noqa: E501

        :return: The alternative_course_title of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._alternative_course_title

    @alternative_course_title.setter
    def alternative_course_title(self, alternative_course_title):
        """Sets the alternative_course_title of this TpdmTeacherCandidateCourseTranscript.

        The descriptive name given to a course of study offered in the school, if different from the CourseTitle.  # noqa: E501

        :param alternative_course_title: The alternative_course_title of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """
        if alternative_course_title is not None and len(alternative_course_title) > 60:
            raise ValueError("Invalid value for `alternative_course_title`, length must be less than or equal to `60`")  # noqa: E501

        self._alternative_course_title = alternative_course_title

    @property
    def attempted_credit_conversion(self):
        """Gets the attempted_credit_conversion of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units.  # noqa: E501

        :return: The attempted_credit_conversion of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: float
        """
        return self._attempted_credit_conversion

    @attempted_credit_conversion.setter
    def attempted_credit_conversion(self, attempted_credit_conversion):
        """Sets the attempted_credit_conversion of this TpdmTeacherCandidateCourseTranscript.

        Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units.  # noqa: E501

        :param attempted_credit_conversion: The attempted_credit_conversion of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: float
        """

        self._attempted_credit_conversion = attempted_credit_conversion

    @property
    def attempted_credits(self):
        """Gets the attempted_credits of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The value of credits or units of value awarded for the completion of a course.  # noqa: E501

        :return: The attempted_credits of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: float
        """
        return self._attempted_credits

    @attempted_credits.setter
    def attempted_credits(self, attempted_credits):
        """Sets the attempted_credits of this TpdmTeacherCandidateCourseTranscript.

        The value of credits or units of value awarded for the completion of a course.  # noqa: E501

        :param attempted_credits: The attempted_credits of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: float
        """

        self._attempted_credits = attempted_credits

    @property
    def attempted_credit_type_descriptor(self):
        """Gets the attempted_credit_type_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The type of credits or units of value awarded for the completion of a course.  # noqa: E501

        :return: The attempted_credit_type_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._attempted_credit_type_descriptor

    @attempted_credit_type_descriptor.setter
    def attempted_credit_type_descriptor(self, attempted_credit_type_descriptor):
        """Sets the attempted_credit_type_descriptor of this TpdmTeacherCandidateCourseTranscript.

        The type of credits or units of value awarded for the completion of a course.  # noqa: E501

        :param attempted_credit_type_descriptor: The attempted_credit_type_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """
        if attempted_credit_type_descriptor is not None and len(attempted_credit_type_descriptor) > 306:
            raise ValueError("Invalid value for `attempted_credit_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._attempted_credit_type_descriptor = attempted_credit_type_descriptor

    @property
    def course_repeat_code_descriptor(self):
        """Gets the course_repeat_code_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        Indicates that an academic course has been repeated by a student and how that repeat is to be computed in the student's academic grade average.  # noqa: E501

        :return: The course_repeat_code_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._course_repeat_code_descriptor

    @course_repeat_code_descriptor.setter
    def course_repeat_code_descriptor(self, course_repeat_code_descriptor):
        """Sets the course_repeat_code_descriptor of this TpdmTeacherCandidateCourseTranscript.

        Indicates that an academic course has been repeated by a student and how that repeat is to be computed in the student's academic grade average.  # noqa: E501

        :param course_repeat_code_descriptor: The course_repeat_code_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """
        if course_repeat_code_descriptor is not None and len(course_repeat_code_descriptor) > 306:
            raise ValueError("Invalid value for `course_repeat_code_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._course_repeat_code_descriptor = course_repeat_code_descriptor

    @property
    def course_title(self):
        """Gets the course_title of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The descriptive name given to a course of study offered in a school or other institution or organization. In departmentalized classes at the elementary, secondary, and postsecondary levels (and for staff development activities), this refers to the name by which a course is identified (e.g., American History, English III). For elementary and other non-departmentalized classes, it refers to any portion of the instruction for which a grade or report is assigned (e.g., reading, composition, spelling, language arts).  # noqa: E501

        :return: The course_title of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._course_title

    @course_title.setter
    def course_title(self, course_title):
        """Sets the course_title of this TpdmTeacherCandidateCourseTranscript.

        The descriptive name given to a course of study offered in a school or other institution or organization. In departmentalized classes at the elementary, secondary, and postsecondary levels (and for staff development activities), this refers to the name by which a course is identified (e.g., American History, English III). For elementary and other non-departmentalized classes, it refers to any portion of the instruction for which a grade or report is assigned (e.g., reading, composition, spelling, language arts).  # noqa: E501

        :param course_title: The course_title of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """
        if course_title is not None and len(course_title) > 60:
            raise ValueError("Invalid value for `course_title`, length must be less than or equal to `60`")  # noqa: E501

        self._course_title = course_title

    @property
    def earned_additional_credits(self):
        """Gets the earned_additional_credits of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        An unordered collection of teacherCandidateCourseTranscriptEarnedAdditionalCredits. The number of additional credits a student attempted and could earn for successfully completing a given course (e.g., dual credit, AP, IB).  # noqa: E501

        :return: The earned_additional_credits of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: list[TpdmTeacherCandidateCourseTranscriptEarnedAdditionalCredits]
        """
        return self._earned_additional_credits

    @earned_additional_credits.setter
    def earned_additional_credits(self, earned_additional_credits):
        """Sets the earned_additional_credits of this TpdmTeacherCandidateCourseTranscript.

        An unordered collection of teacherCandidateCourseTranscriptEarnedAdditionalCredits. The number of additional credits a student attempted and could earn for successfully completing a given course (e.g., dual credit, AP, IB).  # noqa: E501

        :param earned_additional_credits: The earned_additional_credits of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: list[TpdmTeacherCandidateCourseTranscriptEarnedAdditionalCredits]
        """

        self._earned_additional_credits = earned_additional_credits

    @property
    def earned_credit_conversion(self):
        """Gets the earned_credit_conversion of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units.  # noqa: E501

        :return: The earned_credit_conversion of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: float
        """
        return self._earned_credit_conversion

    @earned_credit_conversion.setter
    def earned_credit_conversion(self, earned_credit_conversion):
        """Sets the earned_credit_conversion of this TpdmTeacherCandidateCourseTranscript.

        Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units.  # noqa: E501

        :param earned_credit_conversion: The earned_credit_conversion of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: float
        """

        self._earned_credit_conversion = earned_credit_conversion

    @property
    def earned_credits(self):
        """Gets the earned_credits of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The value of credits or units of value awarded for the completion of a course.  # noqa: E501

        :return: The earned_credits of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: float
        """
        return self._earned_credits

    @earned_credits.setter
    def earned_credits(self, earned_credits):
        """Sets the earned_credits of this TpdmTeacherCandidateCourseTranscript.

        The value of credits or units of value awarded for the completion of a course.  # noqa: E501

        :param earned_credits: The earned_credits of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: float
        """
        if earned_credits is None:
            raise ValueError("Invalid value for `earned_credits`, must not be `None`")  # noqa: E501

        self._earned_credits = earned_credits

    @property
    def earned_credit_type_descriptor(self):
        """Gets the earned_credit_type_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The type of credits or units of value awarded for the completion of a course.  # noqa: E501

        :return: The earned_credit_type_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._earned_credit_type_descriptor

    @earned_credit_type_descriptor.setter
    def earned_credit_type_descriptor(self, earned_credit_type_descriptor):
        """Sets the earned_credit_type_descriptor of this TpdmTeacherCandidateCourseTranscript.

        The type of credits or units of value awarded for the completion of a course.  # noqa: E501

        :param earned_credit_type_descriptor: The earned_credit_type_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """
        if earned_credit_type_descriptor is not None and len(earned_credit_type_descriptor) > 306:
            raise ValueError("Invalid value for `earned_credit_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._earned_credit_type_descriptor = earned_credit_type_descriptor

    @property
    def final_letter_grade_earned(self):
        """Gets the final_letter_grade_earned of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The final indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :return: The final_letter_grade_earned of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._final_letter_grade_earned

    @final_letter_grade_earned.setter
    def final_letter_grade_earned(self, final_letter_grade_earned):
        """Sets the final_letter_grade_earned of this TpdmTeacherCandidateCourseTranscript.

        The final indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :param final_letter_grade_earned: The final_letter_grade_earned of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """
        if final_letter_grade_earned is not None and len(final_letter_grade_earned) > 20:
            raise ValueError("Invalid value for `final_letter_grade_earned`, length must be less than or equal to `20`")  # noqa: E501

        self._final_letter_grade_earned = final_letter_grade_earned

    @property
    def final_numeric_grade_earned(self):
        """Gets the final_numeric_grade_earned of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The final indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :return: The final_numeric_grade_earned of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: float
        """
        return self._final_numeric_grade_earned

    @final_numeric_grade_earned.setter
    def final_numeric_grade_earned(self, final_numeric_grade_earned):
        """Sets the final_numeric_grade_earned of this TpdmTeacherCandidateCourseTranscript.

        The final indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :param final_numeric_grade_earned: The final_numeric_grade_earned of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: float
        """

        self._final_numeric_grade_earned = final_numeric_grade_earned

    @property
    def method_credit_earned_descriptor(self):
        """Gets the method_credit_earned_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        The method the credits were earned (e.g., Classroom, Examination, Transfer).  # noqa: E501

        :return: The method_credit_earned_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._method_credit_earned_descriptor

    @method_credit_earned_descriptor.setter
    def method_credit_earned_descriptor(self, method_credit_earned_descriptor):
        """Sets the method_credit_earned_descriptor of this TpdmTeacherCandidateCourseTranscript.

        The method the credits were earned (e.g., Classroom, Examination, Transfer).  # noqa: E501

        :param method_credit_earned_descriptor: The method_credit_earned_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """
        if method_credit_earned_descriptor is not None and len(method_credit_earned_descriptor) > 306:
            raise ValueError("Invalid value for `method_credit_earned_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._method_credit_earned_descriptor = method_credit_earned_descriptor

    @property
    def when_taken_grade_level_descriptor(self):
        """Gets the when_taken_grade_level_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        Student's grade level at time of course.  # noqa: E501

        :return: The when_taken_grade_level_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._when_taken_grade_level_descriptor

    @when_taken_grade_level_descriptor.setter
    def when_taken_grade_level_descriptor(self, when_taken_grade_level_descriptor):
        """Sets the when_taken_grade_level_descriptor of this TpdmTeacherCandidateCourseTranscript.

        Student's grade level at time of course.  # noqa: E501

        :param when_taken_grade_level_descriptor: The when_taken_grade_level_descriptor of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :type: str
        """
        if when_taken_grade_level_descriptor is not None and len(when_taken_grade_level_descriptor) > 306:
            raise ValueError("Invalid value for `when_taken_grade_level_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._when_taken_grade_level_descriptor = when_taken_grade_level_descriptor

    @property
    def etag(self):
        """Gets the etag of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmTeacherCandidateCourseTranscript.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmTeacherCandidateCourseTranscript.  # noqa: E501
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
        if issubclass(TpdmTeacherCandidateCourseTranscript, dict):
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
        if not isinstance(other, TpdmTeacherCandidateCourseTranscript):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
