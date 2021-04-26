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


class TpdmAnonymizedStudentDisability(object):
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
        'disability_descriptor': 'str',
        'disability_determination_source_type_descriptor': 'str',
        'disability_diagnosis': 'str',
        'order_of_disability': 'int',
        'designations': 'list[TpdmAnonymizedStudentDisabilityDesignation]'
    }

    attribute_map = {
        'disability_descriptor': 'disabilityDescriptor',
        'disability_determination_source_type_descriptor': 'disabilityDeterminationSourceTypeDescriptor',
        'disability_diagnosis': 'disabilityDiagnosis',
        'order_of_disability': 'orderOfDisability',
        'designations': 'designations'
    }

    def __init__(self, disability_descriptor=None, disability_determination_source_type_descriptor=None, disability_diagnosis=None, order_of_disability=None, designations=None):  # noqa: E501
        """TpdmAnonymizedStudentDisability - a model defined in Swagger"""  # noqa: E501

        self._disability_descriptor = None
        self._disability_determination_source_type_descriptor = None
        self._disability_diagnosis = None
        self._order_of_disability = None
        self._designations = None
        self.discriminator = None

        self.disability_descriptor = disability_descriptor
        if disability_determination_source_type_descriptor is not None:
            self.disability_determination_source_type_descriptor = disability_determination_source_type_descriptor
        if disability_diagnosis is not None:
            self.disability_diagnosis = disability_diagnosis
        if order_of_disability is not None:
            self.order_of_disability = order_of_disability
        if designations is not None:
            self.designations = designations

    @property
    def disability_descriptor(self):
        """Gets the disability_descriptor of this TpdmAnonymizedStudentDisability.  # noqa: E501

        A disability category that describes a child's impairment.  # noqa: E501

        :return: The disability_descriptor of this TpdmAnonymizedStudentDisability.  # noqa: E501
        :rtype: str
        """
        return self._disability_descriptor

    @disability_descriptor.setter
    def disability_descriptor(self, disability_descriptor):
        """Sets the disability_descriptor of this TpdmAnonymizedStudentDisability.

        A disability category that describes a child's impairment.  # noqa: E501

        :param disability_descriptor: The disability_descriptor of this TpdmAnonymizedStudentDisability.  # noqa: E501
        :type: str
        """
        if disability_descriptor is None:
            raise ValueError("Invalid value for `disability_descriptor`, must not be `None`")  # noqa: E501
        if disability_descriptor is not None and len(disability_descriptor) > 306:
            raise ValueError("Invalid value for `disability_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._disability_descriptor = disability_descriptor

    @property
    def disability_determination_source_type_descriptor(self):
        """Gets the disability_determination_source_type_descriptor of this TpdmAnonymizedStudentDisability.  # noqa: E501

        The source that provided the disability determination.  # noqa: E501

        :return: The disability_determination_source_type_descriptor of this TpdmAnonymizedStudentDisability.  # noqa: E501
        :rtype: str
        """
        return self._disability_determination_source_type_descriptor

    @disability_determination_source_type_descriptor.setter
    def disability_determination_source_type_descriptor(self, disability_determination_source_type_descriptor):
        """Sets the disability_determination_source_type_descriptor of this TpdmAnonymizedStudentDisability.

        The source that provided the disability determination.  # noqa: E501

        :param disability_determination_source_type_descriptor: The disability_determination_source_type_descriptor of this TpdmAnonymizedStudentDisability.  # noqa: E501
        :type: str
        """
        if disability_determination_source_type_descriptor is not None and len(disability_determination_source_type_descriptor) > 306:
            raise ValueError("Invalid value for `disability_determination_source_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._disability_determination_source_type_descriptor = disability_determination_source_type_descriptor

    @property
    def disability_diagnosis(self):
        """Gets the disability_diagnosis of this TpdmAnonymizedStudentDisability.  # noqa: E501

        A description of the disability diagnosis.  # noqa: E501

        :return: The disability_diagnosis of this TpdmAnonymizedStudentDisability.  # noqa: E501
        :rtype: str
        """
        return self._disability_diagnosis

    @disability_diagnosis.setter
    def disability_diagnosis(self, disability_diagnosis):
        """Sets the disability_diagnosis of this TpdmAnonymizedStudentDisability.

        A description of the disability diagnosis.  # noqa: E501

        :param disability_diagnosis: The disability_diagnosis of this TpdmAnonymizedStudentDisability.  # noqa: E501
        :type: str
        """
        if disability_diagnosis is not None and len(disability_diagnosis) > 80:
            raise ValueError("Invalid value for `disability_diagnosis`, length must be less than or equal to `80`")  # noqa: E501

        self._disability_diagnosis = disability_diagnosis

    @property
    def order_of_disability(self):
        """Gets the order_of_disability of this TpdmAnonymizedStudentDisability.  # noqa: E501

        The order by severity of student's disabilities: 1- Primary, 2 -  Secondary, 3 - Tertiary, etc.  # noqa: E501

        :return: The order_of_disability of this TpdmAnonymizedStudentDisability.  # noqa: E501
        :rtype: int
        """
        return self._order_of_disability

    @order_of_disability.setter
    def order_of_disability(self, order_of_disability):
        """Sets the order_of_disability of this TpdmAnonymizedStudentDisability.

        The order by severity of student's disabilities: 1- Primary, 2 -  Secondary, 3 - Tertiary, etc.  # noqa: E501

        :param order_of_disability: The order_of_disability of this TpdmAnonymizedStudentDisability.  # noqa: E501
        :type: int
        """

        self._order_of_disability = order_of_disability

    @property
    def designations(self):
        """Gets the designations of this TpdmAnonymizedStudentDisability.  # noqa: E501

        An unordered collection of anonymizedStudentDisabilityDesignations. Whether the disability is IDEA, Section 504, or other disability designation.  # noqa: E501

        :return: The designations of this TpdmAnonymizedStudentDisability.  # noqa: E501
        :rtype: list[TpdmAnonymizedStudentDisabilityDesignation]
        """
        return self._designations

    @designations.setter
    def designations(self, designations):
        """Sets the designations of this TpdmAnonymizedStudentDisability.

        An unordered collection of anonymizedStudentDisabilityDesignations. Whether the disability is IDEA, Section 504, or other disability designation.  # noqa: E501

        :param designations: The designations of this TpdmAnonymizedStudentDisability.  # noqa: E501
        :type: list[TpdmAnonymizedStudentDisabilityDesignation]
        """

        self._designations = designations

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
        if issubclass(TpdmAnonymizedStudentDisability, dict):
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
        if not isinstance(other, TpdmAnonymizedStudentDisability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
