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


class EdFiEducationOrganizationInstitutionTelephone(object):
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
        'institution_telephone_number_type_descriptor': 'str',
        'telephone_number': 'str'
    }

    attribute_map = {
        'institution_telephone_number_type_descriptor': 'institutionTelephoneNumberTypeDescriptor',
        'telephone_number': 'telephoneNumber'
    }

    def __init__(self, institution_telephone_number_type_descriptor=None, telephone_number=None):  # noqa: E501
        """EdFiEducationOrganizationInstitutionTelephone - a model defined in Swagger"""  # noqa: E501

        self._institution_telephone_number_type_descriptor = None
        self._telephone_number = None
        self.discriminator = None

        self.institution_telephone_number_type_descriptor = institution_telephone_number_type_descriptor
        self.telephone_number = telephone_number

    @property
    def institution_telephone_number_type_descriptor(self):
        """Gets the institution_telephone_number_type_descriptor of this EdFiEducationOrganizationInstitutionTelephone.  # noqa: E501

        The type of communication number listed for an individual or organization.  # noqa: E501

        :return: The institution_telephone_number_type_descriptor of this EdFiEducationOrganizationInstitutionTelephone.  # noqa: E501
        :rtype: str
        """
        return self._institution_telephone_number_type_descriptor

    @institution_telephone_number_type_descriptor.setter
    def institution_telephone_number_type_descriptor(self, institution_telephone_number_type_descriptor):
        """Sets the institution_telephone_number_type_descriptor of this EdFiEducationOrganizationInstitutionTelephone.

        The type of communication number listed for an individual or organization.  # noqa: E501

        :param institution_telephone_number_type_descriptor: The institution_telephone_number_type_descriptor of this EdFiEducationOrganizationInstitutionTelephone.  # noqa: E501
        :type: str
        """
        if institution_telephone_number_type_descriptor is None:
            raise ValueError("Invalid value for `institution_telephone_number_type_descriptor`, must not be `None`")  # noqa: E501
        if institution_telephone_number_type_descriptor is not None and len(institution_telephone_number_type_descriptor) > 306:
            raise ValueError("Invalid value for `institution_telephone_number_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._institution_telephone_number_type_descriptor = institution_telephone_number_type_descriptor

    @property
    def telephone_number(self):
        """Gets the telephone_number of this EdFiEducationOrganizationInstitutionTelephone.  # noqa: E501

        The telephone number including the area code, and extension, if applicable.  # noqa: E501

        :return: The telephone_number of this EdFiEducationOrganizationInstitutionTelephone.  # noqa: E501
        :rtype: str
        """
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, telephone_number):
        """Sets the telephone_number of this EdFiEducationOrganizationInstitutionTelephone.

        The telephone number including the area code, and extension, if applicable.  # noqa: E501

        :param telephone_number: The telephone_number of this EdFiEducationOrganizationInstitutionTelephone.  # noqa: E501
        :type: str
        """
        if telephone_number is None:
            raise ValueError("Invalid value for `telephone_number`, must not be `None`")  # noqa: E501
        if telephone_number is not None and len(telephone_number) > 24:
            raise ValueError("Invalid value for `telephone_number`, length must be less than or equal to `24`")  # noqa: E501

        self._telephone_number = telephone_number

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
        if issubclass(EdFiEducationOrganizationInstitutionTelephone, dict):
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
        if not isinstance(other, EdFiEducationOrganizationInstitutionTelephone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
