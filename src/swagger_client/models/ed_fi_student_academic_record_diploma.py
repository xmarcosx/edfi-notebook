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


class EdFiStudentAcademicRecordDiploma(object):
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
        'diploma_type_descriptor': 'str',
        'diploma_award_date': 'date',
        'achievement_category_descriptor': 'str',
        'diploma_level_descriptor': 'str',
        'achievement_category_system': 'str',
        'achievement_title': 'str',
        'criteria': 'str',
        'criteria_url': 'str',
        'cte_completer': 'bool',
        'diploma_award_expires_date': 'date',
        'diploma_description': 'str',
        'evidence_statement': 'str',
        'image_url': 'str',
        'issuer_name': 'str',
        'issuer_origin_url': 'str'
    }

    attribute_map = {
        'diploma_type_descriptor': 'diplomaTypeDescriptor',
        'diploma_award_date': 'diplomaAwardDate',
        'achievement_category_descriptor': 'achievementCategoryDescriptor',
        'diploma_level_descriptor': 'diplomaLevelDescriptor',
        'achievement_category_system': 'achievementCategorySystem',
        'achievement_title': 'achievementTitle',
        'criteria': 'criteria',
        'criteria_url': 'criteriaURL',
        'cte_completer': 'cteCompleter',
        'diploma_award_expires_date': 'diplomaAwardExpiresDate',
        'diploma_description': 'diplomaDescription',
        'evidence_statement': 'evidenceStatement',
        'image_url': 'imageURL',
        'issuer_name': 'issuerName',
        'issuer_origin_url': 'issuerOriginURL'
    }

    def __init__(self, diploma_type_descriptor=None, diploma_award_date=None, achievement_category_descriptor=None, diploma_level_descriptor=None, achievement_category_system=None, achievement_title=None, criteria=None, criteria_url=None, cte_completer=None, diploma_award_expires_date=None, diploma_description=None, evidence_statement=None, image_url=None, issuer_name=None, issuer_origin_url=None):  # noqa: E501
        """EdFiStudentAcademicRecordDiploma - a model defined in Swagger"""  # noqa: E501

        self._diploma_type_descriptor = None
        self._diploma_award_date = None
        self._achievement_category_descriptor = None
        self._diploma_level_descriptor = None
        self._achievement_category_system = None
        self._achievement_title = None
        self._criteria = None
        self._criteria_url = None
        self._cte_completer = None
        self._diploma_award_expires_date = None
        self._diploma_description = None
        self._evidence_statement = None
        self._image_url = None
        self._issuer_name = None
        self._issuer_origin_url = None
        self.discriminator = None

        self.diploma_type_descriptor = diploma_type_descriptor
        self.diploma_award_date = diploma_award_date
        if achievement_category_descriptor is not None:
            self.achievement_category_descriptor = achievement_category_descriptor
        if diploma_level_descriptor is not None:
            self.diploma_level_descriptor = diploma_level_descriptor
        if achievement_category_system is not None:
            self.achievement_category_system = achievement_category_system
        if achievement_title is not None:
            self.achievement_title = achievement_title
        if criteria is not None:
            self.criteria = criteria
        if criteria_url is not None:
            self.criteria_url = criteria_url
        if cte_completer is not None:
            self.cte_completer = cte_completer
        if diploma_award_expires_date is not None:
            self.diploma_award_expires_date = diploma_award_expires_date
        if diploma_description is not None:
            self.diploma_description = diploma_description
        if evidence_statement is not None:
            self.evidence_statement = evidence_statement
        if image_url is not None:
            self.image_url = image_url
        if issuer_name is not None:
            self.issuer_name = issuer_name
        if issuer_origin_url is not None:
            self.issuer_origin_url = issuer_origin_url

    @property
    def diploma_type_descriptor(self):
        """Gets the diploma_type_descriptor of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The type of diploma/credential that is awarded to a student in recognition of his/her completion of the curricular requirements.  # noqa: E501

        :return: The diploma_type_descriptor of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._diploma_type_descriptor

    @diploma_type_descriptor.setter
    def diploma_type_descriptor(self, diploma_type_descriptor):
        """Sets the diploma_type_descriptor of this EdFiStudentAcademicRecordDiploma.

        The type of diploma/credential that is awarded to a student in recognition of his/her completion of the curricular requirements.  # noqa: E501

        :param diploma_type_descriptor: The diploma_type_descriptor of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if diploma_type_descriptor is None:
            raise ValueError("Invalid value for `diploma_type_descriptor`, must not be `None`")  # noqa: E501
        if diploma_type_descriptor is not None and len(diploma_type_descriptor) > 306:
            raise ValueError("Invalid value for `diploma_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._diploma_type_descriptor = diploma_type_descriptor

    @property
    def diploma_award_date(self):
        """Gets the diploma_award_date of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The month, day, and year on which the student met  graduation requirements and was awarded a diploma.  # noqa: E501

        :return: The diploma_award_date of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: date
        """
        return self._diploma_award_date

    @diploma_award_date.setter
    def diploma_award_date(self, diploma_award_date):
        """Sets the diploma_award_date of this EdFiStudentAcademicRecordDiploma.

        The month, day, and year on which the student met  graduation requirements and was awarded a diploma.  # noqa: E501

        :param diploma_award_date: The diploma_award_date of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: date
        """
        if diploma_award_date is None:
            raise ValueError("Invalid value for `diploma_award_date`, must not be `None`")  # noqa: E501

        self._diploma_award_date = diploma_award_date

    @property
    def achievement_category_descriptor(self):
        """Gets the achievement_category_descriptor of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The category of achievement attributed to the learner.  # noqa: E501

        :return: The achievement_category_descriptor of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._achievement_category_descriptor

    @achievement_category_descriptor.setter
    def achievement_category_descriptor(self, achievement_category_descriptor):
        """Sets the achievement_category_descriptor of this EdFiStudentAcademicRecordDiploma.

        The category of achievement attributed to the learner.  # noqa: E501

        :param achievement_category_descriptor: The achievement_category_descriptor of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if achievement_category_descriptor is not None and len(achievement_category_descriptor) > 306:
            raise ValueError("Invalid value for `achievement_category_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._achievement_category_descriptor = achievement_category_descriptor

    @property
    def diploma_level_descriptor(self):
        """Gets the diploma_level_descriptor of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The level of diploma/credential that is awarded to a student in recognition of his/her completion of the curricular requirements.         Minimum high school program         Recommended high school program         Distinguished Achievement Program.  # noqa: E501

        :return: The diploma_level_descriptor of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._diploma_level_descriptor

    @diploma_level_descriptor.setter
    def diploma_level_descriptor(self, diploma_level_descriptor):
        """Sets the diploma_level_descriptor of this EdFiStudentAcademicRecordDiploma.

        The level of diploma/credential that is awarded to a student in recognition of his/her completion of the curricular requirements.         Minimum high school program         Recommended high school program         Distinguished Achievement Program.  # noqa: E501

        :param diploma_level_descriptor: The diploma_level_descriptor of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if diploma_level_descriptor is not None and len(diploma_level_descriptor) > 306:
            raise ValueError("Invalid value for `diploma_level_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._diploma_level_descriptor = diploma_level_descriptor

    @property
    def achievement_category_system(self):
        """Gets the achievement_category_system of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The system that defines the categories by which an achievement is attributed to the learner.  # noqa: E501

        :return: The achievement_category_system of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._achievement_category_system

    @achievement_category_system.setter
    def achievement_category_system(self, achievement_category_system):
        """Sets the achievement_category_system of this EdFiStudentAcademicRecordDiploma.

        The system that defines the categories by which an achievement is attributed to the learner.  # noqa: E501

        :param achievement_category_system: The achievement_category_system of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if achievement_category_system is not None and len(achievement_category_system) > 60:
            raise ValueError("Invalid value for `achievement_category_system`, length must be less than or equal to `60`")  # noqa: E501

        self._achievement_category_system = achievement_category_system

    @property
    def achievement_title(self):
        """Gets the achievement_title of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The title assigned to the achievement.  # noqa: E501

        :return: The achievement_title of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._achievement_title

    @achievement_title.setter
    def achievement_title(self, achievement_title):
        """Sets the achievement_title of this EdFiStudentAcademicRecordDiploma.

        The title assigned to the achievement.  # noqa: E501

        :param achievement_title: The achievement_title of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if achievement_title is not None and len(achievement_title) > 60:
            raise ValueError("Invalid value for `achievement_title`, length must be less than or equal to `60`")  # noqa: E501

        self._achievement_title = achievement_title

    @property
    def criteria(self):
        """Gets the criteria of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The criteria for competency-based completion of the achievement/award.  # noqa: E501

        :return: The criteria of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """Sets the criteria of this EdFiStudentAcademicRecordDiploma.

        The criteria for competency-based completion of the achievement/award.  # noqa: E501

        :param criteria: The criteria of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if criteria is not None and len(criteria) > 150:
            raise ValueError("Invalid value for `criteria`, length must be less than or equal to `150`")  # noqa: E501

        self._criteria = criteria

    @property
    def criteria_url(self):
        """Gets the criteria_url of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The Uniform Resource Locator (URL) for the unique address of a web page describing the competency-based completion criteria for the achievement/award.  # noqa: E501

        :return: The criteria_url of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._criteria_url

    @criteria_url.setter
    def criteria_url(self, criteria_url):
        """Sets the criteria_url of this EdFiStudentAcademicRecordDiploma.

        The Uniform Resource Locator (URL) for the unique address of a web page describing the competency-based completion criteria for the achievement/award.  # noqa: E501

        :param criteria_url: The criteria_url of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if criteria_url is not None and len(criteria_url) > 255:
            raise ValueError("Invalid value for `criteria_url`, length must be less than or equal to `255`")  # noqa: E501

        self._criteria_url = criteria_url

    @property
    def cte_completer(self):
        """Gets the cte_completer of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        Indicated a student who reached a state-defined threshold of vocational education and who attained a high school diploma or its recognized state equivalent or GED.  # noqa: E501

        :return: The cte_completer of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: bool
        """
        return self._cte_completer

    @cte_completer.setter
    def cte_completer(self, cte_completer):
        """Sets the cte_completer of this EdFiStudentAcademicRecordDiploma.

        Indicated a student who reached a state-defined threshold of vocational education and who attained a high school diploma or its recognized state equivalent or GED.  # noqa: E501

        :param cte_completer: The cte_completer of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: bool
        """

        self._cte_completer = cte_completer

    @property
    def diploma_award_expires_date(self):
        """Gets the diploma_award_expires_date of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        Date on which the award expires.  # noqa: E501

        :return: The diploma_award_expires_date of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: date
        """
        return self._diploma_award_expires_date

    @diploma_award_expires_date.setter
    def diploma_award_expires_date(self, diploma_award_expires_date):
        """Sets the diploma_award_expires_date of this EdFiStudentAcademicRecordDiploma.

        Date on which the award expires.  # noqa: E501

        :param diploma_award_expires_date: The diploma_award_expires_date of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: date
        """

        self._diploma_award_expires_date = diploma_award_expires_date

    @property
    def diploma_description(self):
        """Gets the diploma_description of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The description of diploma given to the student for accomplishments.  # noqa: E501

        :return: The diploma_description of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._diploma_description

    @diploma_description.setter
    def diploma_description(self, diploma_description):
        """Sets the diploma_description of this EdFiStudentAcademicRecordDiploma.

        The description of diploma given to the student for accomplishments.  # noqa: E501

        :param diploma_description: The diploma_description of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if diploma_description is not None and len(diploma_description) > 80:
            raise ValueError("Invalid value for `diploma_description`, length must be less than or equal to `80`")  # noqa: E501

        self._diploma_description = diploma_description

    @property
    def evidence_statement(self):
        """Gets the evidence_statement of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        A statement or reference describing the evidence that the learner met the criteria for attainment of the Achievement.  # noqa: E501

        :return: The evidence_statement of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._evidence_statement

    @evidence_statement.setter
    def evidence_statement(self, evidence_statement):
        """Sets the evidence_statement of this EdFiStudentAcademicRecordDiploma.

        A statement or reference describing the evidence that the learner met the criteria for attainment of the Achievement.  # noqa: E501

        :param evidence_statement: The evidence_statement of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if evidence_statement is not None and len(evidence_statement) > 150:
            raise ValueError("Invalid value for `evidence_statement`, length must be less than or equal to `150`")  # noqa: E501

        self._evidence_statement = evidence_statement

    @property
    def image_url(self):
        """Gets the image_url of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The Uniform Resource Locator (URL) for the unique address of an image representing an award or badge associated with the Achievement.  # noqa: E501

        :return: The image_url of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this EdFiStudentAcademicRecordDiploma.

        The Uniform Resource Locator (URL) for the unique address of an image representing an award or badge associated with the Achievement.  # noqa: E501

        :param image_url: The image_url of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if image_url is not None and len(image_url) > 255:
            raise ValueError("Invalid value for `image_url`, length must be less than or equal to `255`")  # noqa: E501

        self._image_url = image_url

    @property
    def issuer_name(self):
        """Gets the issuer_name of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The name of the agent, entity, or institution issuing the element.  # noqa: E501

        :return: The issuer_name of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """Sets the issuer_name of this EdFiStudentAcademicRecordDiploma.

        The name of the agent, entity, or institution issuing the element.  # noqa: E501

        :param issuer_name: The issuer_name of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if issuer_name is not None and len(issuer_name) > 150:
            raise ValueError("Invalid value for `issuer_name`, length must be less than or equal to `150`")  # noqa: E501

        self._issuer_name = issuer_name

    @property
    def issuer_origin_url(self):
        """Gets the issuer_origin_url of this EdFiStudentAcademicRecordDiploma.  # noqa: E501

        The Uniform Resource Locator (URL) from which the award was issued.  # noqa: E501

        :return: The issuer_origin_url of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :rtype: str
        """
        return self._issuer_origin_url

    @issuer_origin_url.setter
    def issuer_origin_url(self, issuer_origin_url):
        """Sets the issuer_origin_url of this EdFiStudentAcademicRecordDiploma.

        The Uniform Resource Locator (URL) from which the award was issued.  # noqa: E501

        :param issuer_origin_url: The issuer_origin_url of this EdFiStudentAcademicRecordDiploma.  # noqa: E501
        :type: str
        """
        if issuer_origin_url is not None and len(issuer_origin_url) > 255:
            raise ValueError("Invalid value for `issuer_origin_url`, length must be less than or equal to `255`")  # noqa: E501

        self._issuer_origin_url = issuer_origin_url

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
        if issubclass(EdFiStudentAcademicRecordDiploma, dict):
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
        if not isinstance(other, EdFiStudentAcademicRecordDiploma):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
