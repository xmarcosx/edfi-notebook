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


class EdFiStaffEducationOrganizationContactAssociation(object):
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
        'contact_title': 'str',
        'education_organization_reference': 'EdFiEducationOrganizationReference',
        'staff_reference': 'EdFiStaffReference',
        'address': 'EdFiStaffEducationOrganizationContactAssociationAddress',
        'contact_type_descriptor': 'str',
        'electronic_mail_address': 'str',
        'telephones': 'list[EdFiStaffEducationOrganizationContactAssociationTelephone]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'contact_title': 'contactTitle',
        'education_organization_reference': 'educationOrganizationReference',
        'staff_reference': 'staffReference',
        'address': 'address',
        'contact_type_descriptor': 'contactTypeDescriptor',
        'electronic_mail_address': 'electronicMailAddress',
        'telephones': 'telephones',
        'etag': '_etag'
    }

    def __init__(self, id=None, contact_title=None, education_organization_reference=None, staff_reference=None, address=None, contact_type_descriptor=None, electronic_mail_address=None, telephones=None, etag=None):  # noqa: E501
        """EdFiStaffEducationOrganizationContactAssociation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._contact_title = None
        self._education_organization_reference = None
        self._staff_reference = None
        self._address = None
        self._contact_type_descriptor = None
        self._electronic_mail_address = None
        self._telephones = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.contact_title = contact_title
        self.education_organization_reference = education_organization_reference
        self.staff_reference = staff_reference
        if address is not None:
            self.address = address
        if contact_type_descriptor is not None:
            self.contact_type_descriptor = contact_type_descriptor
        self.electronic_mail_address = electronic_mail_address
        if telephones is not None:
            self.telephones = telephones
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStaffEducationOrganizationContactAssociation.

          # noqa: E501

        :param id: The id of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def contact_title(self):
        """Gets the contact_title of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501

        The title of the contact in the context of the EducationOrganization.  # noqa: E501

        :return: The contact_title of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :rtype: str
        """
        return self._contact_title

    @contact_title.setter
    def contact_title(self, contact_title):
        """Sets the contact_title of this EdFiStaffEducationOrganizationContactAssociation.

        The title of the contact in the context of the EducationOrganization.  # noqa: E501

        :param contact_title: The contact_title of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :type: str
        """
        if contact_title is None:
            raise ValueError("Invalid value for `contact_title`, must not be `None`")  # noqa: E501
        if contact_title is not None and len(contact_title) > 75:
            raise ValueError("Invalid value for `contact_title`, length must be less than or equal to `75`")  # noqa: E501

        self._contact_title = contact_title

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501


        :return: The education_organization_reference of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiStaffEducationOrganizationContactAssociation.


        :param education_organization_reference: The education_organization_reference of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def staff_reference(self):
        """Gets the staff_reference of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501


        :return: The staff_reference of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :rtype: EdFiStaffReference
        """
        return self._staff_reference

    @staff_reference.setter
    def staff_reference(self, staff_reference):
        """Sets the staff_reference of this EdFiStaffEducationOrganizationContactAssociation.


        :param staff_reference: The staff_reference of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :type: EdFiStaffReference
        """
        if staff_reference is None:
            raise ValueError("Invalid value for `staff_reference`, must not be `None`")  # noqa: E501

        self._staff_reference = staff_reference

    @property
    def address(self):
        """Gets the address of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501


        :return: The address of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :rtype: EdFiStaffEducationOrganizationContactAssociationAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this EdFiStaffEducationOrganizationContactAssociation.


        :param address: The address of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :type: EdFiStaffEducationOrganizationContactAssociationAddress
        """

        self._address = address

    @property
    def contact_type_descriptor(self):
        """Gets the contact_type_descriptor of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501

        Indicates the type for the contact information.  # noqa: E501

        :return: The contact_type_descriptor of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :rtype: str
        """
        return self._contact_type_descriptor

    @contact_type_descriptor.setter
    def contact_type_descriptor(self, contact_type_descriptor):
        """Sets the contact_type_descriptor of this EdFiStaffEducationOrganizationContactAssociation.

        Indicates the type for the contact information.  # noqa: E501

        :param contact_type_descriptor: The contact_type_descriptor of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :type: str
        """
        if contact_type_descriptor is not None and len(contact_type_descriptor) > 306:
            raise ValueError("Invalid value for `contact_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._contact_type_descriptor = contact_type_descriptor

    @property
    def electronic_mail_address(self):
        """Gets the electronic_mail_address of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501

        The email for the contact associated with the EducationOrganization.  # noqa: E501

        :return: The electronic_mail_address of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :rtype: str
        """
        return self._electronic_mail_address

    @electronic_mail_address.setter
    def electronic_mail_address(self, electronic_mail_address):
        """Sets the electronic_mail_address of this EdFiStaffEducationOrganizationContactAssociation.

        The email for the contact associated with the EducationOrganization.  # noqa: E501

        :param electronic_mail_address: The electronic_mail_address of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :type: str
        """
        if electronic_mail_address is None:
            raise ValueError("Invalid value for `electronic_mail_address`, must not be `None`")  # noqa: E501
        if electronic_mail_address is not None and len(electronic_mail_address) > 128:
            raise ValueError("Invalid value for `electronic_mail_address`, length must be less than or equal to `128`")  # noqa: E501

        self._electronic_mail_address = electronic_mail_address

    @property
    def telephones(self):
        """Gets the telephones of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501

        An unordered collection of staffEducationOrganizationContactAssociationTelephones. The optional telephone for the contact associated with the EducationOrganization.  # noqa: E501

        :return: The telephones of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :rtype: list[EdFiStaffEducationOrganizationContactAssociationTelephone]
        """
        return self._telephones

    @telephones.setter
    def telephones(self, telephones):
        """Sets the telephones of this EdFiStaffEducationOrganizationContactAssociation.

        An unordered collection of staffEducationOrganizationContactAssociationTelephones. The optional telephone for the contact associated with the EducationOrganization.  # noqa: E501

        :param telephones: The telephones of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :type: list[EdFiStaffEducationOrganizationContactAssociationTelephone]
        """

        self._telephones = telephones

    @property
    def etag(self):
        """Gets the etag of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStaffEducationOrganizationContactAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStaffEducationOrganizationContactAssociation.  # noqa: E501
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
        if issubclass(EdFiStaffEducationOrganizationContactAssociation, dict):
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
        if not isinstance(other, EdFiStaffEducationOrganizationContactAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
