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


class EdFiStudentDisciplineIncidentBehaviorAssociation(object):
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
        'behavior_descriptor': 'str',
        'discipline_incident_reference': 'EdFiDisciplineIncidentReference',
        'student_reference': 'EdFiStudentReference',
        'behavior_detailed_description': 'str',
        'discipline_incident_participation_codes': 'list[EdFiStudentDisciplineIncidentBehaviorAssociationDisciplineIncidentParticipationCode]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'behavior_descriptor': 'behaviorDescriptor',
        'discipline_incident_reference': 'disciplineIncidentReference',
        'student_reference': 'studentReference',
        'behavior_detailed_description': 'behaviorDetailedDescription',
        'discipline_incident_participation_codes': 'disciplineIncidentParticipationCodes',
        'etag': '_etag'
    }

    def __init__(self, id=None, behavior_descriptor=None, discipline_incident_reference=None, student_reference=None, behavior_detailed_description=None, discipline_incident_participation_codes=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiStudentDisciplineIncidentBehaviorAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._behavior_descriptor = None
        self._discipline_incident_reference = None
        self._student_reference = None
        self._behavior_detailed_description = None
        self._discipline_incident_participation_codes = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.behavior_descriptor = behavior_descriptor
        self.discipline_incident_reference = discipline_incident_reference
        self.student_reference = student_reference
        if behavior_detailed_description is not None:
            self.behavior_detailed_description = behavior_detailed_description
        if discipline_incident_participation_codes is not None:
            self.discipline_incident_participation_codes = discipline_incident_participation_codes
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentDisciplineIncidentBehaviorAssociation.

          # noqa: E501

        :param id: The id of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def behavior_descriptor(self):
        """Gets the behavior_descriptor of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501

        Describes behavior by category.  # noqa: E501

        :return: The behavior_descriptor of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :rtype: str
        """
        return self._behavior_descriptor

    @behavior_descriptor.setter
    def behavior_descriptor(self, behavior_descriptor):
        """Sets the behavior_descriptor of this EdFiStudentDisciplineIncidentBehaviorAssociation.

        Describes behavior by category.  # noqa: E501

        :param behavior_descriptor: The behavior_descriptor of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and behavior_descriptor is None:
            raise ValueError("Invalid value for `behavior_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                behavior_descriptor is not None and len(behavior_descriptor) > 306):
            raise ValueError("Invalid value for `behavior_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._behavior_descriptor = behavior_descriptor

    @property
    def discipline_incident_reference(self):
        """Gets the discipline_incident_reference of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501


        :return: The discipline_incident_reference of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :rtype: EdFiDisciplineIncidentReference
        """
        return self._discipline_incident_reference

    @discipline_incident_reference.setter
    def discipline_incident_reference(self, discipline_incident_reference):
        """Sets the discipline_incident_reference of this EdFiStudentDisciplineIncidentBehaviorAssociation.


        :param discipline_incident_reference: The discipline_incident_reference of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :type: EdFiDisciplineIncidentReference
        """
        if self._configuration.client_side_validation and discipline_incident_reference is None:
            raise ValueError("Invalid value for `discipline_incident_reference`, must not be `None`")  # noqa: E501

        self._discipline_incident_reference = discipline_incident_reference

    @property
    def student_reference(self):
        """Gets the student_reference of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501


        :return: The student_reference of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this EdFiStudentDisciplineIncidentBehaviorAssociation.


        :param student_reference: The student_reference of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :type: EdFiStudentReference
        """
        if self._configuration.client_side_validation and student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def behavior_detailed_description(self):
        """Gets the behavior_detailed_description of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501

        Specifies a more granular level of detail of a behavior involved in the incident.  # noqa: E501

        :return: The behavior_detailed_description of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :rtype: str
        """
        return self._behavior_detailed_description

    @behavior_detailed_description.setter
    def behavior_detailed_description(self, behavior_detailed_description):
        """Sets the behavior_detailed_description of this EdFiStudentDisciplineIncidentBehaviorAssociation.

        Specifies a more granular level of detail of a behavior involved in the incident.  # noqa: E501

        :param behavior_detailed_description: The behavior_detailed_description of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                behavior_detailed_description is not None and len(behavior_detailed_description) > 1024):
            raise ValueError("Invalid value for `behavior_detailed_description`, length must be less than or equal to `1024`")  # noqa: E501

        self._behavior_detailed_description = behavior_detailed_description

    @property
    def discipline_incident_participation_codes(self):
        """Gets the discipline_incident_participation_codes of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501

        An unordered collection of studentDisciplineIncidentBehaviorAssociationDisciplineIncidentParticipationCodes. The role or type of participation of a student in a discipline incident.  # noqa: E501

        :return: The discipline_incident_participation_codes of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :rtype: list[EdFiStudentDisciplineIncidentBehaviorAssociationDisciplineIncidentParticipationCode]
        """
        return self._discipline_incident_participation_codes

    @discipline_incident_participation_codes.setter
    def discipline_incident_participation_codes(self, discipline_incident_participation_codes):
        """Sets the discipline_incident_participation_codes of this EdFiStudentDisciplineIncidentBehaviorAssociation.

        An unordered collection of studentDisciplineIncidentBehaviorAssociationDisciplineIncidentParticipationCodes. The role or type of participation of a student in a discipline incident.  # noqa: E501

        :param discipline_incident_participation_codes: The discipline_incident_participation_codes of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :type: list[EdFiStudentDisciplineIncidentBehaviorAssociationDisciplineIncidentParticipationCode]
        """

        self._discipline_incident_participation_codes = discipline_incident_participation_codes

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentDisciplineIncidentBehaviorAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentDisciplineIncidentBehaviorAssociation.  # noqa: E501
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
        if issubclass(EdFiStudentDisciplineIncidentBehaviorAssociation, dict):
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
        if not isinstance(other, EdFiStudentDisciplineIncidentBehaviorAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentDisciplineIncidentBehaviorAssociation):
            return True

        return self.to_dict() != other.to_dict()
