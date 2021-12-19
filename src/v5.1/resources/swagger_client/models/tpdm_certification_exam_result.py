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


class TpdmCertificationExamResult(object):
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
        'certification_exam_date': 'date',
        'certification_exam_reference': 'TpdmCertificationExamReference',
        'person_reference': 'EdFiPersonReference',
        'attempt_number': 'int',
        'certification_exam_pass_indicator': 'bool',
        'certification_exam_score': 'float',
        'certification_exam_status_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'certification_exam_date': 'certificationExamDate',
        'certification_exam_reference': 'certificationExamReference',
        'person_reference': 'personReference',
        'attempt_number': 'attemptNumber',
        'certification_exam_pass_indicator': 'certificationExamPassIndicator',
        'certification_exam_score': 'certificationExamScore',
        'certification_exam_status_descriptor': 'certificationExamStatusDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, certification_exam_date=None, certification_exam_reference=None, person_reference=None, attempt_number=None, certification_exam_pass_indicator=None, certification_exam_score=None, certification_exam_status_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmCertificationExamResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._certification_exam_date = None
        self._certification_exam_reference = None
        self._person_reference = None
        self._attempt_number = None
        self._certification_exam_pass_indicator = None
        self._certification_exam_score = None
        self._certification_exam_status_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.certification_exam_date = certification_exam_date
        self.certification_exam_reference = certification_exam_reference
        self.person_reference = person_reference
        if attempt_number is not None:
            self.attempt_number = attempt_number
        if certification_exam_pass_indicator is not None:
            self.certification_exam_pass_indicator = certification_exam_pass_indicator
        if certification_exam_score is not None:
            self.certification_exam_score = certification_exam_score
        if certification_exam_status_descriptor is not None:
            self.certification_exam_status_descriptor = certification_exam_status_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmCertificationExamResult.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmCertificationExamResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmCertificationExamResult.

          # noqa: E501

        :param id: The id of this TpdmCertificationExamResult.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def certification_exam_date(self):
        """Gets the certification_exam_date of this TpdmCertificationExamResult.  # noqa: E501

        The year, month and day on which the CertificationExam is taken.  # noqa: E501

        :return: The certification_exam_date of this TpdmCertificationExamResult.  # noqa: E501
        :rtype: date
        """
        return self._certification_exam_date

    @certification_exam_date.setter
    def certification_exam_date(self, certification_exam_date):
        """Sets the certification_exam_date of this TpdmCertificationExamResult.

        The year, month and day on which the CertificationExam is taken.  # noqa: E501

        :param certification_exam_date: The certification_exam_date of this TpdmCertificationExamResult.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and certification_exam_date is None:
            raise ValueError("Invalid value for `certification_exam_date`, must not be `None`")  # noqa: E501

        self._certification_exam_date = certification_exam_date

    @property
    def certification_exam_reference(self):
        """Gets the certification_exam_reference of this TpdmCertificationExamResult.  # noqa: E501


        :return: The certification_exam_reference of this TpdmCertificationExamResult.  # noqa: E501
        :rtype: TpdmCertificationExamReference
        """
        return self._certification_exam_reference

    @certification_exam_reference.setter
    def certification_exam_reference(self, certification_exam_reference):
        """Sets the certification_exam_reference of this TpdmCertificationExamResult.


        :param certification_exam_reference: The certification_exam_reference of this TpdmCertificationExamResult.  # noqa: E501
        :type: TpdmCertificationExamReference
        """
        if self._configuration.client_side_validation and certification_exam_reference is None:
            raise ValueError("Invalid value for `certification_exam_reference`, must not be `None`")  # noqa: E501

        self._certification_exam_reference = certification_exam_reference

    @property
    def person_reference(self):
        """Gets the person_reference of this TpdmCertificationExamResult.  # noqa: E501


        :return: The person_reference of this TpdmCertificationExamResult.  # noqa: E501
        :rtype: EdFiPersonReference
        """
        return self._person_reference

    @person_reference.setter
    def person_reference(self, person_reference):
        """Sets the person_reference of this TpdmCertificationExamResult.


        :param person_reference: The person_reference of this TpdmCertificationExamResult.  # noqa: E501
        :type: EdFiPersonReference
        """
        if self._configuration.client_side_validation and person_reference is None:
            raise ValueError("Invalid value for `person_reference`, must not be `None`")  # noqa: E501

        self._person_reference = person_reference

    @property
    def attempt_number(self):
        """Gets the attempt_number of this TpdmCertificationExamResult.  # noqa: E501

        The number of the person's attempt for the Certification Exam.  # noqa: E501

        :return: The attempt_number of this TpdmCertificationExamResult.  # noqa: E501
        :rtype: int
        """
        return self._attempt_number

    @attempt_number.setter
    def attempt_number(self, attempt_number):
        """Sets the attempt_number of this TpdmCertificationExamResult.

        The number of the person's attempt for the Certification Exam.  # noqa: E501

        :param attempt_number: The attempt_number of this TpdmCertificationExamResult.  # noqa: E501
        :type: int
        """

        self._attempt_number = attempt_number

    @property
    def certification_exam_pass_indicator(self):
        """Gets the certification_exam_pass_indicator of this TpdmCertificationExamResult.  # noqa: E501

        Indicator that the person passed the Certification Exam.  # noqa: E501

        :return: The certification_exam_pass_indicator of this TpdmCertificationExamResult.  # noqa: E501
        :rtype: bool
        """
        return self._certification_exam_pass_indicator

    @certification_exam_pass_indicator.setter
    def certification_exam_pass_indicator(self, certification_exam_pass_indicator):
        """Sets the certification_exam_pass_indicator of this TpdmCertificationExamResult.

        Indicator that the person passed the Certification Exam.  # noqa: E501

        :param certification_exam_pass_indicator: The certification_exam_pass_indicator of this TpdmCertificationExamResult.  # noqa: E501
        :type: bool
        """

        self._certification_exam_pass_indicator = certification_exam_pass_indicator

    @property
    def certification_exam_score(self):
        """Gets the certification_exam_score of this TpdmCertificationExamResult.  # noqa: E501

        The score result for the Certification Exam attempt.  # noqa: E501

        :return: The certification_exam_score of this TpdmCertificationExamResult.  # noqa: E501
        :rtype: float
        """
        return self._certification_exam_score

    @certification_exam_score.setter
    def certification_exam_score(self, certification_exam_score):
        """Sets the certification_exam_score of this TpdmCertificationExamResult.

        The score result for the Certification Exam attempt.  # noqa: E501

        :param certification_exam_score: The certification_exam_score of this TpdmCertificationExamResult.  # noqa: E501
        :type: float
        """

        self._certification_exam_score = certification_exam_score

    @property
    def certification_exam_status_descriptor(self):
        """Gets the certification_exam_status_descriptor of this TpdmCertificationExamResult.  # noqa: E501

        The status of the Certification Exam attempt.  # noqa: E501

        :return: The certification_exam_status_descriptor of this TpdmCertificationExamResult.  # noqa: E501
        :rtype: str
        """
        return self._certification_exam_status_descriptor

    @certification_exam_status_descriptor.setter
    def certification_exam_status_descriptor(self, certification_exam_status_descriptor):
        """Sets the certification_exam_status_descriptor of this TpdmCertificationExamResult.

        The status of the Certification Exam attempt.  # noqa: E501

        :param certification_exam_status_descriptor: The certification_exam_status_descriptor of this TpdmCertificationExamResult.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                certification_exam_status_descriptor is not None and len(certification_exam_status_descriptor) > 306):
            raise ValueError("Invalid value for `certification_exam_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._certification_exam_status_descriptor = certification_exam_status_descriptor

    @property
    def etag(self):
        """Gets the etag of this TpdmCertificationExamResult.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmCertificationExamResult.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmCertificationExamResult.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmCertificationExamResult.  # noqa: E501
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
        if issubclass(TpdmCertificationExamResult, dict):
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
        if not isinstance(other, TpdmCertificationExamResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmCertificationExamResult):
            return True

        return self.to_dict() != other.to_dict()
