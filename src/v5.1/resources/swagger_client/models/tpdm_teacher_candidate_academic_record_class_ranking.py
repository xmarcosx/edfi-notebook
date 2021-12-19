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


class TpdmTeacherCandidateAcademicRecordClassRanking(object):
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
        'class_rank': 'int',
        'class_ranking_date': 'date',
        'percentage_ranking': 'int',
        'total_number_in_class': 'int'
    }

    attribute_map = {
        'class_rank': 'classRank',
        'class_ranking_date': 'classRankingDate',
        'percentage_ranking': 'percentageRanking',
        'total_number_in_class': 'totalNumberInClass'
    }

    def __init__(self, class_rank=None, class_ranking_date=None, percentage_ranking=None, total_number_in_class=None, _configuration=None):  # noqa: E501
        """TpdmTeacherCandidateAcademicRecordClassRanking - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._class_rank = None
        self._class_ranking_date = None
        self._percentage_ranking = None
        self._total_number_in_class = None
        self.discriminator = None

        self.class_rank = class_rank
        if class_ranking_date is not None:
            self.class_ranking_date = class_ranking_date
        if percentage_ranking is not None:
            self.percentage_ranking = percentage_ranking
        self.total_number_in_class = total_number_in_class

    @property
    def class_rank(self):
        """Gets the class_rank of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501

        The academic rank of a student in relation to his or her graduating class (e.g., 1st, 2nd, 3rd).  # noqa: E501

        :return: The class_rank of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501
        :rtype: int
        """
        return self._class_rank

    @class_rank.setter
    def class_rank(self, class_rank):
        """Sets the class_rank of this TpdmTeacherCandidateAcademicRecordClassRanking.

        The academic rank of a student in relation to his or her graduating class (e.g., 1st, 2nd, 3rd).  # noqa: E501

        :param class_rank: The class_rank of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and class_rank is None:
            raise ValueError("Invalid value for `class_rank`, must not be `None`")  # noqa: E501

        self._class_rank = class_rank

    @property
    def class_ranking_date(self):
        """Gets the class_ranking_date of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501

        Date class ranking was determined.  # noqa: E501

        :return: The class_ranking_date of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501
        :rtype: date
        """
        return self._class_ranking_date

    @class_ranking_date.setter
    def class_ranking_date(self, class_ranking_date):
        """Sets the class_ranking_date of this TpdmTeacherCandidateAcademicRecordClassRanking.

        Date class ranking was determined.  # noqa: E501

        :param class_ranking_date: The class_ranking_date of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501
        :type: date
        """

        self._class_ranking_date = class_ranking_date

    @property
    def percentage_ranking(self):
        """Gets the percentage_ranking of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501

        The academic percentage rank of a student in relation to his or her graduating class (e.g., 95%, 80%, 50%).  # noqa: E501

        :return: The percentage_ranking of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501
        :rtype: int
        """
        return self._percentage_ranking

    @percentage_ranking.setter
    def percentage_ranking(self, percentage_ranking):
        """Sets the percentage_ranking of this TpdmTeacherCandidateAcademicRecordClassRanking.

        The academic percentage rank of a student in relation to his or her graduating class (e.g., 95%, 80%, 50%).  # noqa: E501

        :param percentage_ranking: The percentage_ranking of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501
        :type: int
        """

        self._percentage_ranking = percentage_ranking

    @property
    def total_number_in_class(self):
        """Gets the total_number_in_class of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501

        The total number of students in the student's graduating class.  # noqa: E501

        :return: The total_number_in_class of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501
        :rtype: int
        """
        return self._total_number_in_class

    @total_number_in_class.setter
    def total_number_in_class(self, total_number_in_class):
        """Sets the total_number_in_class of this TpdmTeacherCandidateAcademicRecordClassRanking.

        The total number of students in the student's graduating class.  # noqa: E501

        :param total_number_in_class: The total_number_in_class of this TpdmTeacherCandidateAcademicRecordClassRanking.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total_number_in_class is None:
            raise ValueError("Invalid value for `total_number_in_class`, must not be `None`")  # noqa: E501

        self._total_number_in_class = total_number_in_class

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
        if issubclass(TpdmTeacherCandidateAcademicRecordClassRanking, dict):
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
        if not isinstance(other, TpdmTeacherCandidateAcademicRecordClassRanking):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmTeacherCandidateAcademicRecordClassRanking):
            return True

        return self.to_dict() != other.to_dict()
