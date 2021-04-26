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


class EdFiStudentInterventionAssociation(object):
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
        'cohort_reference': 'EdFiCohortReference',
        'intervention_reference': 'EdFiInterventionReference',
        'student_reference': 'EdFiStudentReference',
        'diagnostic_statement': 'str',
        'dosage': 'int',
        'intervention_effectivenesses': 'list[EdFiStudentInterventionAssociationInterventionEffectiveness]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cohort_reference': 'cohortReference',
        'intervention_reference': 'interventionReference',
        'student_reference': 'studentReference',
        'diagnostic_statement': 'diagnosticStatement',
        'dosage': 'dosage',
        'intervention_effectivenesses': 'interventionEffectivenesses',
        'etag': '_etag'
    }

    def __init__(self, id=None, cohort_reference=None, intervention_reference=None, student_reference=None, diagnostic_statement=None, dosage=None, intervention_effectivenesses=None, etag=None):  # noqa: E501
        """EdFiStudentInterventionAssociation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._cohort_reference = None
        self._intervention_reference = None
        self._student_reference = None
        self._diagnostic_statement = None
        self._dosage = None
        self._intervention_effectivenesses = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cohort_reference is not None:
            self.cohort_reference = cohort_reference
        self.intervention_reference = intervention_reference
        self.student_reference = student_reference
        if diagnostic_statement is not None:
            self.diagnostic_statement = diagnostic_statement
        if dosage is not None:
            self.dosage = dosage
        if intervention_effectivenesses is not None:
            self.intervention_effectivenesses = intervention_effectivenesses
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStudentInterventionAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentInterventionAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentInterventionAssociation.

          # noqa: E501

        :param id: The id of this EdFiStudentInterventionAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def cohort_reference(self):
        """Gets the cohort_reference of this EdFiStudentInterventionAssociation.  # noqa: E501


        :return: The cohort_reference of this EdFiStudentInterventionAssociation.  # noqa: E501
        :rtype: EdFiCohortReference
        """
        return self._cohort_reference

    @cohort_reference.setter
    def cohort_reference(self, cohort_reference):
        """Sets the cohort_reference of this EdFiStudentInterventionAssociation.


        :param cohort_reference: The cohort_reference of this EdFiStudentInterventionAssociation.  # noqa: E501
        :type: EdFiCohortReference
        """

        self._cohort_reference = cohort_reference

    @property
    def intervention_reference(self):
        """Gets the intervention_reference of this EdFiStudentInterventionAssociation.  # noqa: E501


        :return: The intervention_reference of this EdFiStudentInterventionAssociation.  # noqa: E501
        :rtype: EdFiInterventionReference
        """
        return self._intervention_reference

    @intervention_reference.setter
    def intervention_reference(self, intervention_reference):
        """Sets the intervention_reference of this EdFiStudentInterventionAssociation.


        :param intervention_reference: The intervention_reference of this EdFiStudentInterventionAssociation.  # noqa: E501
        :type: EdFiInterventionReference
        """
        if intervention_reference is None:
            raise ValueError("Invalid value for `intervention_reference`, must not be `None`")  # noqa: E501

        self._intervention_reference = intervention_reference

    @property
    def student_reference(self):
        """Gets the student_reference of this EdFiStudentInterventionAssociation.  # noqa: E501


        :return: The student_reference of this EdFiStudentInterventionAssociation.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this EdFiStudentInterventionAssociation.


        :param student_reference: The student_reference of this EdFiStudentInterventionAssociation.  # noqa: E501
        :type: EdFiStudentReference
        """
        if student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def diagnostic_statement(self):
        """Gets the diagnostic_statement of this EdFiStudentInterventionAssociation.  # noqa: E501

        A statement provided by the assigner that provides information regarding why the student was assigned to this intervention.  # noqa: E501

        :return: The diagnostic_statement of this EdFiStudentInterventionAssociation.  # noqa: E501
        :rtype: str
        """
        return self._diagnostic_statement

    @diagnostic_statement.setter
    def diagnostic_statement(self, diagnostic_statement):
        """Sets the diagnostic_statement of this EdFiStudentInterventionAssociation.

        A statement provided by the assigner that provides information regarding why the student was assigned to this intervention.  # noqa: E501

        :param diagnostic_statement: The diagnostic_statement of this EdFiStudentInterventionAssociation.  # noqa: E501
        :type: str
        """
        if diagnostic_statement is not None and len(diagnostic_statement) > 1024:
            raise ValueError("Invalid value for `diagnostic_statement`, length must be less than or equal to `1024`")  # noqa: E501

        self._diagnostic_statement = diagnostic_statement

    @property
    def dosage(self):
        """Gets the dosage of this EdFiStudentInterventionAssociation.  # noqa: E501

        The duration of time in minutes for which the student was assigned to participate in the intervention.  # noqa: E501

        :return: The dosage of this EdFiStudentInterventionAssociation.  # noqa: E501
        :rtype: int
        """
        return self._dosage

    @dosage.setter
    def dosage(self, dosage):
        """Sets the dosage of this EdFiStudentInterventionAssociation.

        The duration of time in minutes for which the student was assigned to participate in the intervention.  # noqa: E501

        :param dosage: The dosage of this EdFiStudentInterventionAssociation.  # noqa: E501
        :type: int
        """

        self._dosage = dosage

    @property
    def intervention_effectivenesses(self):
        """Gets the intervention_effectivenesses of this EdFiStudentInterventionAssociation.  # noqa: E501

        An unordered collection of studentInterventionAssociationInterventionEffectivenesses. A measure of the effects of an intervention in each outcome domain. The rating of effectiveness takes into account four factors: the quality of the research on the intervention, the statistical significance of the research findings, the size of the differences between participants in the intervention and comparison groups and the consistency in results.  # noqa: E501

        :return: The intervention_effectivenesses of this EdFiStudentInterventionAssociation.  # noqa: E501
        :rtype: list[EdFiStudentInterventionAssociationInterventionEffectiveness]
        """
        return self._intervention_effectivenesses

    @intervention_effectivenesses.setter
    def intervention_effectivenesses(self, intervention_effectivenesses):
        """Sets the intervention_effectivenesses of this EdFiStudentInterventionAssociation.

        An unordered collection of studentInterventionAssociationInterventionEffectivenesses. A measure of the effects of an intervention in each outcome domain. The rating of effectiveness takes into account four factors: the quality of the research on the intervention, the statistical significance of the research findings, the size of the differences between participants in the intervention and comparison groups and the consistency in results.  # noqa: E501

        :param intervention_effectivenesses: The intervention_effectivenesses of this EdFiStudentInterventionAssociation.  # noqa: E501
        :type: list[EdFiStudentInterventionAssociationInterventionEffectiveness]
        """

        self._intervention_effectivenesses = intervention_effectivenesses

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentInterventionAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentInterventionAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentInterventionAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentInterventionAssociation.  # noqa: E501
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
        if issubclass(EdFiStudentInterventionAssociation, dict):
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
        if not isinstance(other, EdFiStudentInterventionAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
