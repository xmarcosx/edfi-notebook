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


class TpdmPerformanceEvaluationRating(object):
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
        'performance_evaluation_reference': 'TpdmPerformanceEvaluationReference',
        'person_reference': 'EdFiPersonReference',
        'actual_date': 'date',
        'actual_duration': 'int',
        'actual_time': 'str',
        'announced': 'bool',
        'comments': 'str',
        'coteaching_style_observed_descriptor': 'str',
        'performance_evaluation_rating_level_descriptor': 'str',
        'results': 'list[TpdmPerformanceEvaluationRatingResult]',
        'reviewers': 'list[TpdmPerformanceEvaluationRatingReviewer]',
        'schedule_date': 'date',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'performance_evaluation_reference': 'performanceEvaluationReference',
        'person_reference': 'personReference',
        'actual_date': 'actualDate',
        'actual_duration': 'actualDuration',
        'actual_time': 'actualTime',
        'announced': 'announced',
        'comments': 'comments',
        'coteaching_style_observed_descriptor': 'coteachingStyleObservedDescriptor',
        'performance_evaluation_rating_level_descriptor': 'performanceEvaluationRatingLevelDescriptor',
        'results': 'results',
        'reviewers': 'reviewers',
        'schedule_date': 'scheduleDate',
        'etag': '_etag'
    }

    def __init__(self, id=None, performance_evaluation_reference=None, person_reference=None, actual_date=None, actual_duration=None, actual_time=None, announced=None, comments=None, coteaching_style_observed_descriptor=None, performance_evaluation_rating_level_descriptor=None, results=None, reviewers=None, schedule_date=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmPerformanceEvaluationRating - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._performance_evaluation_reference = None
        self._person_reference = None
        self._actual_date = None
        self._actual_duration = None
        self._actual_time = None
        self._announced = None
        self._comments = None
        self._coteaching_style_observed_descriptor = None
        self._performance_evaluation_rating_level_descriptor = None
        self._results = None
        self._reviewers = None
        self._schedule_date = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.performance_evaluation_reference = performance_evaluation_reference
        self.person_reference = person_reference
        self.actual_date = actual_date
        if actual_duration is not None:
            self.actual_duration = actual_duration
        if actual_time is not None:
            self.actual_time = actual_time
        if announced is not None:
            self.announced = announced
        if comments is not None:
            self.comments = comments
        if coteaching_style_observed_descriptor is not None:
            self.coteaching_style_observed_descriptor = coteaching_style_observed_descriptor
        if performance_evaluation_rating_level_descriptor is not None:
            self.performance_evaluation_rating_level_descriptor = performance_evaluation_rating_level_descriptor
        if results is not None:
            self.results = results
        if reviewers is not None:
            self.reviewers = reviewers
        if schedule_date is not None:
            self.schedule_date = schedule_date
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmPerformanceEvaluationRating.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmPerformanceEvaluationRating.

          # noqa: E501

        :param id: The id of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def performance_evaluation_reference(self):
        """Gets the performance_evaluation_reference of this TpdmPerformanceEvaluationRating.  # noqa: E501


        :return: The performance_evaluation_reference of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: TpdmPerformanceEvaluationReference
        """
        return self._performance_evaluation_reference

    @performance_evaluation_reference.setter
    def performance_evaluation_reference(self, performance_evaluation_reference):
        """Sets the performance_evaluation_reference of this TpdmPerformanceEvaluationRating.


        :param performance_evaluation_reference: The performance_evaluation_reference of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: TpdmPerformanceEvaluationReference
        """
        if self._configuration.client_side_validation and performance_evaluation_reference is None:
            raise ValueError("Invalid value for `performance_evaluation_reference`, must not be `None`")  # noqa: E501

        self._performance_evaluation_reference = performance_evaluation_reference

    @property
    def person_reference(self):
        """Gets the person_reference of this TpdmPerformanceEvaluationRating.  # noqa: E501


        :return: The person_reference of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: EdFiPersonReference
        """
        return self._person_reference

    @person_reference.setter
    def person_reference(self, person_reference):
        """Sets the person_reference of this TpdmPerformanceEvaluationRating.


        :param person_reference: The person_reference of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: EdFiPersonReference
        """
        if self._configuration.client_side_validation and person_reference is None:
            raise ValueError("Invalid value for `person_reference`, must not be `None`")  # noqa: E501

        self._person_reference = person_reference

    @property
    def actual_date(self):
        """Gets the actual_date of this TpdmPerformanceEvaluationRating.  # noqa: E501

        The month, day, and year on which the performance evaluation was conducted.  # noqa: E501

        :return: The actual_date of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: date
        """
        return self._actual_date

    @actual_date.setter
    def actual_date(self, actual_date):
        """Sets the actual_date of this TpdmPerformanceEvaluationRating.

        The month, day, and year on which the performance evaluation was conducted.  # noqa: E501

        :param actual_date: The actual_date of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and actual_date is None:
            raise ValueError("Invalid value for `actual_date`, must not be `None`")  # noqa: E501

        self._actual_date = actual_date

    @property
    def actual_duration(self):
        """Gets the actual_duration of this TpdmPerformanceEvaluationRating.  # noqa: E501

        The actual or estimated number of clock minutes during which the performance evaluation was conducted.  # noqa: E501

        :return: The actual_duration of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: int
        """
        return self._actual_duration

    @actual_duration.setter
    def actual_duration(self, actual_duration):
        """Sets the actual_duration of this TpdmPerformanceEvaluationRating.

        The actual or estimated number of clock minutes during which the performance evaluation was conducted.  # noqa: E501

        :param actual_duration: The actual_duration of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: int
        """

        self._actual_duration = actual_duration

    @property
    def actual_time(self):
        """Gets the actual_time of this TpdmPerformanceEvaluationRating.  # noqa: E501

        An indication of the the time at which the performance evaluation was conducted.  # noqa: E501

        :return: The actual_time of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: str
        """
        return self._actual_time

    @actual_time.setter
    def actual_time(self, actual_time):
        """Sets the actual_time of this TpdmPerformanceEvaluationRating.

        An indication of the the time at which the performance evaluation was conducted.  # noqa: E501

        :param actual_time: The actual_time of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: str
        """

        self._actual_time = actual_time

    @property
    def announced(self):
        """Gets the announced of this TpdmPerformanceEvaluationRating.  # noqa: E501

        An indicator of whether the performance evaluation was announced or not.  # noqa: E501

        :return: The announced of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: bool
        """
        return self._announced

    @announced.setter
    def announced(self, announced):
        """Sets the announced of this TpdmPerformanceEvaluationRating.

        An indicator of whether the performance evaluation was announced or not.  # noqa: E501

        :param announced: The announced of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: bool
        """

        self._announced = announced

    @property
    def comments(self):
        """Gets the comments of this TpdmPerformanceEvaluationRating.  # noqa: E501

        Any comments about the performance evaluation to be captured.  # noqa: E501

        :return: The comments of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this TpdmPerformanceEvaluationRating.

        Any comments about the performance evaluation to be captured.  # noqa: E501

        :param comments: The comments of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                comments is not None and len(comments) > 1024):
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `1024`")  # noqa: E501

        self._comments = comments

    @property
    def coteaching_style_observed_descriptor(self):
        """Gets the coteaching_style_observed_descriptor of this TpdmPerformanceEvaluationRating.  # noqa: E501

        A type of co-teaching observed as part of the performance evaluation.  # noqa: E501

        :return: The coteaching_style_observed_descriptor of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: str
        """
        return self._coteaching_style_observed_descriptor

    @coteaching_style_observed_descriptor.setter
    def coteaching_style_observed_descriptor(self, coteaching_style_observed_descriptor):
        """Sets the coteaching_style_observed_descriptor of this TpdmPerformanceEvaluationRating.

        A type of co-teaching observed as part of the performance evaluation.  # noqa: E501

        :param coteaching_style_observed_descriptor: The coteaching_style_observed_descriptor of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                coteaching_style_observed_descriptor is not None and len(coteaching_style_observed_descriptor) > 306):
            raise ValueError("Invalid value for `coteaching_style_observed_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._coteaching_style_observed_descriptor = coteaching_style_observed_descriptor

    @property
    def performance_evaluation_rating_level_descriptor(self):
        """Gets the performance_evaluation_rating_level_descriptor of this TpdmPerformanceEvaluationRating.  # noqa: E501

        The rating level achieved based upon the rating or score.  # noqa: E501

        :return: The performance_evaluation_rating_level_descriptor of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: str
        """
        return self._performance_evaluation_rating_level_descriptor

    @performance_evaluation_rating_level_descriptor.setter
    def performance_evaluation_rating_level_descriptor(self, performance_evaluation_rating_level_descriptor):
        """Sets the performance_evaluation_rating_level_descriptor of this TpdmPerformanceEvaluationRating.

        The rating level achieved based upon the rating or score.  # noqa: E501

        :param performance_evaluation_rating_level_descriptor: The performance_evaluation_rating_level_descriptor of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                performance_evaluation_rating_level_descriptor is not None and len(performance_evaluation_rating_level_descriptor) > 306):
            raise ValueError("Invalid value for `performance_evaluation_rating_level_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._performance_evaluation_rating_level_descriptor = performance_evaluation_rating_level_descriptor

    @property
    def results(self):
        """Gets the results of this TpdmPerformanceEvaluationRating.  # noqa: E501

        An unordered collection of performanceEvaluationRatingResults. The numerical summary rating or score for the performance evaluation.  # noqa: E501

        :return: The results of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: list[TpdmPerformanceEvaluationRatingResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this TpdmPerformanceEvaluationRating.

        An unordered collection of performanceEvaluationRatingResults. The numerical summary rating or score for the performance evaluation.  # noqa: E501

        :param results: The results of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: list[TpdmPerformanceEvaluationRatingResult]
        """

        self._results = results

    @property
    def reviewers(self):
        """Gets the reviewers of this TpdmPerformanceEvaluationRating.  # noqa: E501

        An unordered collection of performanceEvaluationRatingReviewers. The person(s) that conducted the performance evaluation.  # noqa: E501

        :return: The reviewers of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: list[TpdmPerformanceEvaluationRatingReviewer]
        """
        return self._reviewers

    @reviewers.setter
    def reviewers(self, reviewers):
        """Sets the reviewers of this TpdmPerformanceEvaluationRating.

        An unordered collection of performanceEvaluationRatingReviewers. The person(s) that conducted the performance evaluation.  # noqa: E501

        :param reviewers: The reviewers of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: list[TpdmPerformanceEvaluationRatingReviewer]
        """

        self._reviewers = reviewers

    @property
    def schedule_date(self):
        """Gets the schedule_date of this TpdmPerformanceEvaluationRating.  # noqa: E501

        The month, day, and year on which the performance evaluation was to be conducted.  # noqa: E501

        :return: The schedule_date of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: date
        """
        return self._schedule_date

    @schedule_date.setter
    def schedule_date(self, schedule_date):
        """Sets the schedule_date of this TpdmPerformanceEvaluationRating.

        The month, day, and year on which the performance evaluation was to be conducted.  # noqa: E501

        :param schedule_date: The schedule_date of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :type: date
        """

        self._schedule_date = schedule_date

    @property
    def etag(self):
        """Gets the etag of this TpdmPerformanceEvaluationRating.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmPerformanceEvaluationRating.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmPerformanceEvaluationRating.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmPerformanceEvaluationRating.  # noqa: E501
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
        if issubclass(TpdmPerformanceEvaluationRating, dict):
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
        if not isinstance(other, TpdmPerformanceEvaluationRating):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmPerformanceEvaluationRating):
            return True

        return self.to_dict() != other.to_dict()
