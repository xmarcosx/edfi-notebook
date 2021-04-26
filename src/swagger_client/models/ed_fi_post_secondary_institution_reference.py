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


class EdFiPostSecondaryInstitutionReference(object):
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
        'post_secondary_institution_id': 'int',
        'link': 'Link'
    }

    attribute_map = {
        'post_secondary_institution_id': 'postSecondaryInstitutionId',
        'link': 'link'
    }

    def __init__(self, post_secondary_institution_id=None, link=None):  # noqa: E501
        """EdFiPostSecondaryInstitutionReference - a model defined in Swagger"""  # noqa: E501

        self._post_secondary_institution_id = None
        self._link = None
        self.discriminator = None

        self.post_secondary_institution_id = post_secondary_institution_id
        if link is not None:
            self.link = link

    @property
    def post_secondary_institution_id(self):
        """Gets the post_secondary_institution_id of this EdFiPostSecondaryInstitutionReference.  # noqa: E501

        The ID of the post secondary institution.  # noqa: E501

        :return: The post_secondary_institution_id of this EdFiPostSecondaryInstitutionReference.  # noqa: E501
        :rtype: int
        """
        return self._post_secondary_institution_id

    @post_secondary_institution_id.setter
    def post_secondary_institution_id(self, post_secondary_institution_id):
        """Sets the post_secondary_institution_id of this EdFiPostSecondaryInstitutionReference.

        The ID of the post secondary institution.  # noqa: E501

        :param post_secondary_institution_id: The post_secondary_institution_id of this EdFiPostSecondaryInstitutionReference.  # noqa: E501
        :type: int
        """
        if post_secondary_institution_id is None:
            raise ValueError("Invalid value for `post_secondary_institution_id`, must not be `None`")  # noqa: E501

        self._post_secondary_institution_id = post_secondary_institution_id

    @property
    def link(self):
        """Gets the link of this EdFiPostSecondaryInstitutionReference.  # noqa: E501


        :return: The link of this EdFiPostSecondaryInstitutionReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiPostSecondaryInstitutionReference.


        :param link: The link of this EdFiPostSecondaryInstitutionReference.  # noqa: E501
        :type: Link
        """

        self._link = link

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
        if issubclass(EdFiPostSecondaryInstitutionReference, dict):
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
        if not isinstance(other, EdFiPostSecondaryInstitutionReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
