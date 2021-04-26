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


class EdFiStudentDisciplineIncidentAssociation(object):
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
        'discipline_incident_reference': 'EdFiDisciplineIncidentReference',
        'student_reference': 'EdFiStudentReference',
        'behaviors': 'list[EdFiStudentDisciplineIncidentAssociationBehavior]',
        'student_participation_code_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'discipline_incident_reference': 'disciplineIncidentReference',
        'student_reference': 'studentReference',
        'behaviors': 'behaviors',
        'student_participation_code_descriptor': 'studentParticipationCodeDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, discipline_incident_reference=None, student_reference=None, behaviors=None, student_participation_code_descriptor=None, etag=None):  # noqa: E501
        """EdFiStudentDisciplineIncidentAssociation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._discipline_incident_reference = None
        self._student_reference = None
        self._behaviors = None
        self._student_participation_code_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.discipline_incident_reference = discipline_incident_reference
        self.student_reference = student_reference
        if behaviors is not None:
            self.behaviors = behaviors
        self.student_participation_code_descriptor = student_participation_code_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentDisciplineIncidentAssociation.

          # noqa: E501

        :param id: The id of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def discipline_incident_reference(self):
        """Gets the discipline_incident_reference of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501


        :return: The discipline_incident_reference of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :rtype: EdFiDisciplineIncidentReference
        """
        return self._discipline_incident_reference

    @discipline_incident_reference.setter
    def discipline_incident_reference(self, discipline_incident_reference):
        """Sets the discipline_incident_reference of this EdFiStudentDisciplineIncidentAssociation.


        :param discipline_incident_reference: The discipline_incident_reference of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :type: EdFiDisciplineIncidentReference
        """
        if discipline_incident_reference is None:
            raise ValueError("Invalid value for `discipline_incident_reference`, must not be `None`")  # noqa: E501

        self._discipline_incident_reference = discipline_incident_reference

    @property
    def student_reference(self):
        """Gets the student_reference of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501


        :return: The student_reference of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this EdFiStudentDisciplineIncidentAssociation.


        :param student_reference: The student_reference of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :type: EdFiStudentReference
        """
        if student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def behaviors(self):
        """Gets the behaviors of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501

        An unordered collection of studentDisciplineIncidentAssociationBehaviors. Describes behavior by category and provides a detailed description.  # noqa: E501

        :return: The behaviors of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :rtype: list[EdFiStudentDisciplineIncidentAssociationBehavior]
        """
        return self._behaviors

    @behaviors.setter
    def behaviors(self, behaviors):
        """Sets the behaviors of this EdFiStudentDisciplineIncidentAssociation.

        An unordered collection of studentDisciplineIncidentAssociationBehaviors. Describes behavior by category and provides a detailed description.  # noqa: E501

        :param behaviors: The behaviors of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :type: list[EdFiStudentDisciplineIncidentAssociationBehavior]
        """

        self._behaviors = behaviors

    @property
    def student_participation_code_descriptor(self):
        """Gets the student_participation_code_descriptor of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501

        The role or type of participation of a student in a discipline incident;          for example:         Victim         Perpetrator         Witness         Reporter.  # noqa: E501

        :return: The student_participation_code_descriptor of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :rtype: str
        """
        return self._student_participation_code_descriptor

    @student_participation_code_descriptor.setter
    def student_participation_code_descriptor(self, student_participation_code_descriptor):
        """Sets the student_participation_code_descriptor of this EdFiStudentDisciplineIncidentAssociation.

        The role or type of participation of a student in a discipline incident;          for example:         Victim         Perpetrator         Witness         Reporter.  # noqa: E501

        :param student_participation_code_descriptor: The student_participation_code_descriptor of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :type: str
        """
        if student_participation_code_descriptor is None:
            raise ValueError("Invalid value for `student_participation_code_descriptor`, must not be `None`")  # noqa: E501
        if student_participation_code_descriptor is not None and len(student_participation_code_descriptor) > 306:
            raise ValueError("Invalid value for `student_participation_code_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._student_participation_code_descriptor = student_participation_code_descriptor

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentDisciplineIncidentAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentDisciplineIncidentAssociation.  # noqa: E501
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
        if issubclass(EdFiStudentDisciplineIncidentAssociation, dict):
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
        if not isinstance(other, EdFiStudentDisciplineIncidentAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
